"""Fetch real product photos and affiliate links from the AliExpress Affiliate API.

For each shoe from a Chinese brand in data/running_shoes.json, this script
searches the AliExpress Affiliate API, picks the listing that best matches the
brand and model, and saves its main image, affiliate (promotion) link and price
to data/aliexpress.json. scripts/build_site.py then shows the photo and link.

Credentials come from environment variables, never from files in the repo:
  ALIEXPRESS_APP_KEY, ALIEXPRESS_APP_SECRET, ALIEXPRESS_TRACKING_ID

Manual control: data/aliexpress_overrides.json maps a shoe id to an AliExpress
product id or product URL (to force the right listing), or to null (to never
link that shoe). data/aliexpress_review.csv lists what was matched so a person
can check it.

Western brands are skipped on purpose: big-brand shoes on AliExpress are often
not genuine, and linking to them would put the site and the affiliate account
at risk.
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
# Alternative names some models go by in listings (English and pinyin)
MODEL_ALIASES = {
    "red hare": ["red hare", "chitu", "chi tu", "redhare"],
    "feidian": ["feidian", "fei dian"],
    "jueying": ["jueying", "jue ying", "essential"],
    "yueying": ["yueying", "yue ying", "shadow"],
    "super light": ["super light", "superlight", "chaoqing"],
    "furious future": ["furious future", "furious"],
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
    return re.sub(r"[^a-z0-9°%.]+", " ", text.lower()).strip()


def model_terms(model):
    """Groups of acceptable spellings; every group must appear in the title."""
    m = norm(model)
    groups = []
    for key, aliases in MODEL_ALIASES.items():
        if key in m:
            groups.append(aliases)
            m = m.replace(key, " ")
    for tok in m.split():
        groups.append([tok])
    return groups


def score(product, shoe):
    title = " " + norm(product.get("product_title", "")) + " "
    if not any(b in title for b in BRAND_TERMS[shoe["brand"]]):
        return None
    total = 0
    for group in model_terms(shoe["model"]):
        if not any(f" {a} " in title or (len(a) > 3 and a in title) for a in group):
            return None
        total += 10
    if "run" in title:
        total += 5
    if "official" in title or "store" in norm(product.get("shop_url", "")):
        total += 3
    volume = int(product.get("lastest_volume") or 0)
    total += min(volume, 1000) / 200
    return total


def pick(product):
    return {
        "product_id": str(product.get("product_id")),
        "title": product.get("product_title"),
        "image": product.get("product_main_image_url"),
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

    for shoe in shoes:
        if shoe["brand"] not in BRAND_TERMS:
            continue
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
                query = f'{BRAND_TERMS[shoe["brand"]][0]} {shoe["model"]} running shoes'
                res = call("aliexpress.affiliate.product.query", {**common, "keywords": query, "page_size": 20, "sort": "LAST_VOLUME_DESC"}, key, secret)
                ranked = sorted(((score(p, shoe), p) for p in products_of(res)), key=lambda x: -(x[0] or -1))
                if ranked and ranked[0][0] is not None:
                    found[sid] = {**pick(ranked[0][1]), "matched_by": "search", "fetched": now}
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

    json.dump(found, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    with open(os.path.join(DATA, "aliexpress_review.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["shoe_id", "brand", "model", "result", "aliexpress_title", "product_id"])
        w.writerows(review)
    print(f"Matched {len(found)} of {len(review)} shoes ({failures} API errors). Review data/aliexpress_review.csv.")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(f"### AliExpress\n\nMatched **{len(found)}** of {len(review)} shoes, {failures} API errors.\n")
    if failures and not found:
        sys.exit(1)


if __name__ == "__main__":
    main()
