"""Fetch real product photos and affiliate links from the AliExpress Affiliate API.

For each shoe in scope, this script does two things:
  1. Builds an AliExpress search page link for "<brand> <model>" (the visitor
     lands on a list of listings, as if they had typed the name) and turns it
     into an affiliate link with aliexpress.affiliate.link.generate.
  2. Looks for the listing that exactly matches the model and keeps its photo,
     so the site can show a real picture of that shoe.
Results go to data/aliexpress.json; scripts/build_site.py shows them.

Credentials come from environment variables, never from files in the repo:
  ALIEXPRESS_APP_KEY, ALIEXPRESS_APP_SECRET, ALIEXPRESS_TRACKING_ID

Manual control: data/aliexpress_overrides.json maps a shoe id to an AliExpress
product id or product URL (to force the right listing), or to null (to never
link that shoe). data/aliexpress_review.csv lists what was matched so a person
can check it.

By default only Chinese brands are linked: search results for big Western
brands on AliExpress are mostly not genuine, and AliExpress's affiliate terms
forbid promoting counterfeits. Set INCLUDE_WESTERN_BRANDS = True to change that.
"""
import csv
import hashlib
import hmac
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data")
ENDPOINT = "https://api-sg.aliexpress.com/sync"

# How each brand is written in AliExpress listing titles
BRAND_TERMS = {
    "Li-Ning": ["li-ning", "li ning", "lining"],
    "ANTA": ["anta"],
    "Xtep": ["xtep"],
    "361°": ["361", "361°", "361 degrees"],
    "PEAK": ["peak"],
    "Qiaodan": ["qiaodan", "qiao dan"],
    "Kailas": ["kailas"],
}
# Search links for Nike, ASICS, HOKA and other non-Chinese brands (see the note above)
INCLUDE_WESTERN_BRANDS = False

# Alternative names some models go by in listings (English and pinyin)
MODEL_ALIASES = {
    "red hare": ["red hare", "chitu", "chi tu", "redhare"],
    "feidian": ["feidian", "fei dian"],
    "jueying": ["jueying", "jue ying", "essential"],
    "yueying": ["yueying", "yue ying", "shadow"],
    "super light": ["super light", "superlight", "chaoqing"],
    "feiying": ["feiying", "fei ying", "flying shadow"],
}


def sign(secret, params, method="md5"):
    joined = "".join(f"{k}{params[k]}" for k in sorted(params))
    if method == "sha256":  # newer apps on the AliExpress Open Platform sign with HMAC-SHA256
        return hmac.new(secret.encode("utf-8"), joined.encode("utf-8"), hashlib.sha256).hexdigest().upper()
    return hashlib.md5((secret + joined + secret).encode("utf-8")).hexdigest().upper()


SIGN_METHODS = ["sha256", "md5"]  # the one that works is moved to the front


def note(level, message):
    """Print a GitHub Actions annotation so the reason shows on the run page."""
    print(f"::{level} title=AliExpress API::{message}", flush=True)


def raw_call(method, app_params, key, secret, sign_method):
    sys_params = {
        "format": "json",
        "app_key": key,
        "sign_method": sign_method,
        "v": "2.0",
        "timestamp": str(int(time.time() * 1000)),
        "method": method,
    }
    app_params = {k: str(v) for k, v in app_params.items() if v is not None}
    sys_params["sign"] = sign(secret, {**sys_params, **app_params}, sign_method)
    url = ENDPOINT + "?" + urllib.parse.urlencode(sys_params)
    body = urllib.parse.urlencode(app_params).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read()[:300].decode('utf-8', 'replace')}")
    if "error_response" in payload:
        err = payload["error_response"]
        raise RuntimeError(f"{err.get('code')} {err.get('msg')} {err.get('sub_msg', '')}".strip())
    return payload


def call(method, app_params, key, secret):
    last = None
    for sm in list(SIGN_METHODS):
        try:
            payload = raw_call(method, app_params, key, secret, sm)
            if SIGN_METHODS[0] != sm:
                SIGN_METHODS.remove(sm)
                SIGN_METHODS.insert(0, sm)
            break
        except RuntimeError as e:
            last = e
            if "sign" not in str(e).lower():
                raise
    else:
        raise last
    name = method.replace(".", "_") + "_response"
    result = payload[name]["resp_result"]
    if result.get("resp_code") != 200:
        raise RuntimeError(f"{result.get('resp_code')} {result.get('resp_msg')}")
    return result.get("result") or {}


def products_of(result):
    prods = (result.get("products") or {}).get("product") or []
    return prods if isinstance(prods, list) else [prods]


def norm(text):
    text = text.lower()
    text = re.sub(r"(?<=[a-z0-9])-(?=[a-z0-9])", "", text)  # keep product codes like ARHW033-4 in one piece
    return re.sub(r"[^a-z0-9°%.]+", " ", text).strip()


# Words that mark a different version of a model (a "Red Hare 9 Pro" is not a "Red Hare 9")
VARIANTS = {"pro", "ultra", "elite", "challenger", "max", "plus", "gt", "se", "lite", "air", "gtx"}


SHOE_WORDS = {"shoe", "shoes", "sneaker", "sneakers", "trainer", "trainers", "runner", "runners"}
NOT_SHOES = {"slipper", "slippers", "slide", "slides", "sandal", "sandals", "sock", "socks", "insole", "insoles",
             "necklace", "keychain", "charm", "laces", "shoelaces", "lace", "bag", "cap", "hat", "shirt", "shorts", "kids", "children"}


def tok_pattern(tok):
    if re.fullmatch(r"\d+", tok):  # "5" also matches "5.0"
        return rf"{tok}(?:\.0)?"
    return re.escape(tok)


def model_patterns(model):
    """Regexes for the full model name: tokens in order, at most one extra word between them."""
    m = norm(model)
    names = [m]
    for key, aliases in MODEL_ALIASES.items():
        if key in m:
            names = [m.replace(key, a) for a in aliases]
            break
    pats = []
    for name in names:
        toks = name.split()
        body = r"(?:\s+\S+)?\s+".join(tok_pattern(t) for t in toks)
        pats.append((re.compile(rf"(?<!\S){body}(?!\S)"), set(toks)))
    return pats


def score(product, shoe):
    title = norm(product.get("product_title", ""))
    padded = f" {title} "
    words = set(title.split())
    if not words & SHOE_WORDS or words & NOT_SHOES:
        return None  # only real shoes: no slippers, socks, insoles or jewellery
    if not any(f" {b} " in padded or b in title for b in BRAND_TERMS[shoe["brand"]]):
        return None
    for pat, toks in model_patterns(shoe["model"]):
        m = pat.search(title)
        if not m:
            continue
        if len(toks) == 1:  # one-word names like "Wave" must sit right after the brand
            before = title[:m.start()].split()[-2:]
            if not any(b in " ".join(before) for b in BRAND_TERMS[shoe["brand"]]):
                continue
        nxt = title[m.end():].split()[:1]
        if nxt and nxt[0] in VARIANTS and nxt[0] not in toks:
            return None  # e.g. looking for "Red Hare 8", found "Red Hare 8 Pro"
        total = 20
        if m.group(0).count(" ") == len(toks) - 1:
            total += 5  # exact phrase, no extra words in between
        if "run" in title:
            total += 5
        total += min(int(product.get("lastest_volume") or 0), 1000) / 200
        return total
    return None


def queries(shoe):
    brand = BRAND_TERMS[shoe["brand"]][0]
    model = shoe["model"].replace("%", "").strip()
    qs = [f"{brand} {model} running shoes", f"{brand} {model}"]
    low = norm(model)
    for key, aliases in MODEL_ALIASES.items():
        if key in low:
            qs += [f"{brand} {low.replace(key, a)}" for a in aliases[1:3]]
    if shoe["brand"] == "361°":
        qs.append(f"361 degrees {model}")
    return list(dict.fromkeys(qs))


def search_words(shoe):
    return f'{BRAND_TERMS.get(shoe["brand"], [shoe["brand"]])[0]} {shoe["model"]} running shoes'.replace("%", "")


# Ways to write an AliExpress search page; the API accepts some and not others,
# so the first one it converts is used for every shoe.
SEARCH_FORMATS = [
    lambda w: "https://www.aliexpress.com/w/wholesale-" + re.sub(r"[^a-z0-9]+", "-", w.lower()).strip("-") + ".html",
    lambda w: "https://www.aliexpress.com/wholesale?" + urllib.parse.urlencode({"SearchText": w}),
    lambda w: "https://www.aliexpress.com/w/wholesale-" + urllib.parse.quote(w.replace(" ", "-")) + ".html?SearchText=" + urllib.parse.quote(w),
]


def generate(urls, tracking, key, secret, link_type):
    res = call("aliexpress.affiliate.link.generate",
               {"source_values": ",".join(urls), "promotion_link_type": link_type, "tracking_id": tracking}, key, secret)
    links = (res.get("promotion_links") or {}).get("promotion_link") or []
    return {i.get("source_value"): i["promotion_link"] for i in (links if isinstance(links, list) else [links]) if i.get("promotion_link")}


def affiliate_search_links(shoes_by_id, common, key, secret):
    """Affiliate links to AliExpress search pages, keyed by shoe id."""
    words = {sid: search_words(sh) for sid, sh in shoes_by_id.items()}
    sample = next(iter(words.values()), None)
    if not sample:
        return {}
    chosen, tried = None, []
    for fi, fmt in enumerate(SEARCH_FORMATS):
        for link_type in (0, 2):
            try:
                if generate([fmt(sample)], common["tracking_id"], key, secret, link_type):
                    chosen = (fmt, link_type)
                    break
                tried.append(f"format {fi + 1}/type {link_type}: no link")
            except RuntimeError as e:
                tried.append(f"format {fi + 1}/type {link_type}: {e}")
            time.sleep(0.4)
        if chosen:
            break
    if not chosen:
        note("warning", "AliExpress did not convert search pages into affiliate links (" + "; ".join(tried)[:400] + "). Using the matched listing links instead.")
        return {}
    fmt, link_type = chosen
    url_of = {sid: fmt(w) for sid, w in words.items()}
    urls = list(dict.fromkeys(url_of.values()))
    got = {}
    for i in range(0, len(urls), 20):
        got.update(generate(urls[i:i + 20], common["tracking_id"], key, secret, link_type))
        time.sleep(0.4)
    return {sid: got[u] for sid, u in url_of.items() if u in got}


def is_empty(error):
    return "result is empty" in str(error).lower() or str(error).startswith("405")


def gallery_of(product):
    small = product.get("product_small_image_urls") or {}
    urls = small.get("string") if isinstance(small, dict) else small
    if isinstance(urls, str):
        urls = [urls]
    return [u for u in (urls or []) if isinstance(u, str)][:8]


def pick(product):
    return {
        "product_id": str(product.get("product_id")),
        "title": product.get("product_title"),
        "image": product.get("product_main_image_url"),
        "gallery": gallery_of(product),
        "link": product.get("promotion_link"),
        "price": product.get("target_sale_price") or product.get("sale_price"),
        "currency": product.get("target_sale_price_currency") or "USD",
    }


def product_id_from(value):
    m = re.search(r"(\d{8,})", str(value))
    return m.group(1) if m else None


def main():
    key = (os.environ.get("ALIEXPRESS_APP_KEY") or "").strip()
    secret = (os.environ.get("ALIEXPRESS_APP_SECRET") or "").strip()
    tracking = (os.environ.get("ALIEXPRESS_TRACKING_ID") or "").strip()
    if not (key and secret and tracking):
        missing = [n for n, v in (("ALIEXPRESS_APP_KEY", key), ("ALIEXPRESS_APP_SECRET", secret), ("ALIEXPRESS_TRACKING_ID", tracking)) if not v]
        note("error", "Missing repository secrets: " + ", ".join(missing))
        sys.exit(1)

    shoes = json.load(open(os.path.join(DATA, "running_shoes.json"), encoding="utf-8"))["shoes"]
    overrides_path = os.path.join(DATA, "aliexpress_overrides.json")
    overrides = json.load(open(overrides_path, encoding="utf-8")) if os.path.exists(overrides_path) else {}
    out_path = os.path.join(DATA, "aliexpress.json")
    previous = json.load(open(out_path, encoding="utf-8")) if os.path.exists(out_path) else {}

    common = {"target_currency": "USD", "target_language": "EN", "tracking_id": tracking}
    found, review, failures = {}, [], 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    in_scope = [sh for sh in shoes if sh["brand"] in BRAND_TERMS or INCLUDE_WESTERN_BRANDS]
    for shoe in shoes:
        if shoe["brand"] not in BRAND_TERMS:
            continue  # exact-listing photos only for brands with official stores on AliExpress
        sid = shoe["id"]
        try:
            if sid in overrides:
                if overrides[sid] is None:
                    review.append([sid, shoe["brand"], shoe["model"], "skipped (override)", "", ""])
                    continue
                pid = product_id_from(overrides[sid])
                res = call("aliexpress.affiliate.productdetail.get", {**common, "product_ids": pid}, key, secret)
                prods = products_of(res)
                if prods:
                    found[sid] = {**pick(prods[0]), "matched_by": "override", "fetched": now}
            else:
                best = None
                for query in queries(shoe):  # try the most specific search first, then broader ones
                    try:
                        res = call("aliexpress.affiliate.product.query", {**common, "keywords": query, "page_size": 40, "sort": "LAST_VOLUME_DESC"}, key, secret)
                    except RuntimeError as e:
                        if is_empty(e):
                            continue
                        raise
                    for p in products_of(res):
                        sc = score(p, shoe)
                        if sc is not None and (best is None or sc > best[0]):
                            best = (sc, p)
                    if best:
                        break
                    time.sleep(0.3)
                if best:
                    found[sid] = {**pick(best[1]), "matched_by": "search", "fetched": now}
        except Exception as error:  # keep going; one bad call should not stop the run
            failures += 1
            print(f"! {sid}: {error}", file=sys.stderr)
            if failures <= 3:
                note("error", f"{sid}: {error}")
            if sid in previous:
                found[sid] = previous[sid]
        hit = found.get(sid)
        review.append([sid, shoe["brand"], shoe["model"], hit["matched_by"] if hit else "not found",
                       hit["title"] if hit else "", hit["product_id"] if hit else ""])
        time.sleep(0.4)

    # Search-page links for every shoe in scope (skip shoes overridden to null)
    wanted = {sh["id"]: sh for sh in in_scope if not (sh["id"] in overrides and overrides[sh["id"]] is None)}
    try:
        aff = affiliate_search_links(wanted, common, key, secret)
    except Exception as error:
        aff = {}
        note("warning", f"link.generate: {error}")
    for sid in wanted:
        link = aff.get(sid) or (previous.get(sid) or {}).get("search_link")
        if link:
            found.setdefault(sid, {"fetched": now})["search_link"] = link
    print(f"Search links: {sum(1 for v in found.values() if v.get('search_link'))} of {len(wanted)}")

    json.dump(found, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    with open(os.path.join(DATA, "aliexpress_review.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["shoe_id", "brand", "model", "result", "aliexpress_title", "product_id"])
        w.writerows(review)
    print(f"Photos: {sum(1 for v in found.values() if v.get('image'))} of {len(review)} shoes ({failures} API errors). Review data/aliexpress_review.csv.")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(f"### AliExpress\n\nPhotos: **{sum(1 for v in found.values() if v.get('image'))}**, search links: **{sum(1 for v in found.values() if v.get('search_link'))}**, {failures} API errors.\n")
    if failures and not found:
        sys.exit(1)


if __name__ == "__main__":
    main()
