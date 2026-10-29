"""Fetch product photos and affiliate links from Awin product feeds.

For every Awin programme the account has joined (Nike BR, Netshoes, SportsShoes...),
this script downloads the advertiser's product feed through the Awin Enhanced Feed
API, finds the products that match shoes in data/running_shoes.json and saves,
per shoe, the store offers (affiliate link, price, country) and the product photos
to data/awin.json. scripts/clean_photos.py turns the photos into cut-outs and
scripts/build_site.py adds a store button for each offer.

Credentials come from repository secrets, never from files in the repo:
  AWIN_API_TOKEN     API token from ui.awin.com/awin-api
  AWIN_PUBLISHER_ID  your publisher ID (optional; looked up from the token if missing)

Programmes that are not joined yet, or that do not publish an Enhanced Feed, are
listed in the run summary so you can see what is missing.
"""
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aliexpress_fetch import NOT_SHOES, VARIANTS, model_patterns, norm, note  # shared title matching

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data")
API = "https://api.awin.com"

# How brands are written in feeds (brand field or title); everything is compared lower-case
BRAND_ALIASES = {
    "HOKA": ["hoka", "hoka one one"], "New Balance": ["new balance", "nb"], "On": ["on", "on running", "on-running"],
    "ASICS": ["asics"], "adidas": ["adidas", "adidas performance"], "PUMA": ["puma"], "Under Armour": ["under armour"],
    "361°": ["361", "361 degrees", "361°"], "Li-Ning": ["li-ning", "li ning", "lining"], "Topo Athletic": ["topo athletic", "topo"],
    "inov-8": ["inov-8", "inov8"], "La Sportiva": ["la sportiva"], "Kiprun": ["kiprun", "decathlon kiprun"],
}
LOCALES = {"BR": ["pt_BR"], "PT": ["pt_PT"], "US": ["en_US"], "GB": ["en_GB"], "IE": ["en_IE", "en_GB"], "DE": ["de_DE"],
           "AT": ["de_AT", "de_DE"], "CH": ["de_CH", "fr_CH"], "FR": ["fr_FR"], "ES": ["es_ES"], "IT": ["it_IT"],
           "NL": ["nl_NL"], "BE": ["nl_BE", "fr_BE"], "PL": ["pl_PL"], "SE": ["sv_SE"], "DK": ["da_DK"], "NO": ["no_NO"],
           "FI": ["fi_FI"], "AU": ["en_AU"], "CA": ["en_CA"]}
KIDS = {"kids", "kid", "infant", "infantil", "junior", "juvenil", "criança", "crianca", "enfant", "kinder", "bambino", "niños", "ninos", "toddler", "gs", "ps"}


def request(path, token, params=None, stream=False):
    url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=120)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} on {path}: {e.read()[:200].decode('utf-8', 'replace')}")
    return resp if stream else json.loads(resp.read())


def find(obj, key):
    """First value for `key` anywhere in a nested dict/list (feeds differ in how they nest fields)."""
    if isinstance(obj, dict):
        if key in obj and obj[key] not in (None, "", []):
            return obj[key]
        for v in obj.values():
            r = find(v, key)
            if r not in (None, "", []):
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = find(v, key)
            if r not in (None, "", []):
                return r
    return None


def price_of(product):
    p = find(product, "sale_price") or find(product, "price") or find(product, "search_price")
    if isinstance(p, dict):
        return p.get("value") or p.get("amount"), p.get("currency")
    if isinstance(p, str):
        m = re.match(r"\s*([\d.,]+)\s*([A-Z]{3})?", p)
        if m:
            return m.group(1).replace(",", "."), m.group(2)
    return p, find(product, "currency")


def brand_ok(product, shoe):
    aliases = BRAND_ALIASES.get(shoe["brand"], [shoe["brand"].lower()])
    b = norm(str(find(product, "brand") or ""))
    if b:
        return any(b == norm(a) or b.startswith(norm(a) + " ") for a in aliases)
    title = " " + norm(str(find(product, "title") or "")) + " "
    return any(f" {norm(a)} " in title for a in aliases if a not in ("on", "nb"))


def match_score(product, shoe):
    title = norm(str(find(product, "title") or find(product, "product_name") or ""))
    words = set(title.split())
    if words & NOT_SHOES or words & KIDS or not brand_ok(product, shoe):
        return None
    for pat, toks in model_patterns(shoe["model"]):
        m = pat.search(title)
        if not m:
            continue
        nxt = title[m.end():].split()[:1]
        if nxt and nxt[0] in VARIANTS and nxt[0] not in toks:
            return None  # a different variant (Pro, Max, GTX...)
        if nxt and re.fullmatch(r"v?\d+(\.\d+)?", nxt[0]):
            return None  # a different version: "Cloudmonster" is not "Cloudmonster 2"
        if len(toks) == 1 and not re.search(r"\d", shoe["model"]):
            before = title[:m.start()].split()[-3:]
            if not any(norm(a) in " ".join(before) for a in BRAND_ALIASES.get(shoe["brand"], [shoe["brand"].lower()])):
                continue
        return 20 + (5 if m.group(0).count(" ") == len(toks) - 1 else 0) + (3 if "run" in title or "corr" in title else 0)
    return None


def publisher_id(token):
    pid = (os.environ.get("AWIN_PUBLISHER_ID") or "").strip()
    if pid:
        return pid
    acc = request("/accounts", token)
    for a in acc.get("accounts", []) if isinstance(acc, dict) else acc:
        if str(a.get("accountType", "")).lower() == "publisher":
            return str(a.get("accountId"))
    raise RuntimeError("Could not find the publisher ID; add the AWIN_PUBLISHER_ID secret")


def main():
    token = (os.environ.get("AWIN_API_TOKEN") or "").strip()
    if not token:
        print("AWIN_API_TOKEN is not set; skipping Awin.")
        return
    shoes = json.load(open(os.path.join(DATA, "running_shoes.json"), encoding="utf-8"))["shoes"]
    out_path = os.path.join(DATA, "awin.json")
    previous = json.load(open(out_path, encoding="utf-8")) if os.path.exists(out_path) else {}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    try:
        pid = publisher_id(token)
        joined = request(f"/publishers/{pid}/programmes", token, {"relationship": "joined"})
        pending = request(f"/publishers/{pid}/programmes", token, {"relationship": "pending"})
    except Exception as e:
        note("error", f"Awin: {e}")
        sys.exit(1)

    found, stores, first = {}, [], True
    for prog in joined:
        adv, name = prog.get("id"), prog.get("name", "")
        cc = ((prog.get("primaryRegion") or {}).get("countryCode") or "").upper()
        best = {}  # shoe id -> (score, product)
        feed_ok, lines = False, 0
        for loc in LOCALES.get(cc, []) + ["en_GB"]:
            if not first:
                time.sleep(13)  # Awin allows at most 5 feed requests per minute
            first = False
            try:
                resp = request(f"/publishers/{pid}/awinfeeds/download/{adv}-retail-{loc}.jsonl", token, stream=True)
            except RuntimeError as e:
                if "404" in str(e):
                    continue
                note("warning", f"Awin {name}: {e}")
                break
            feed_ok = True
            for raw in resp:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    product = json.loads(raw)
                except ValueError:
                    continue
                if isinstance(product, dict) and "error" in product and len(product) <= 3:
                    note("warning", f"Awin {name}: feed download failed ({product})")
                    break
                lines += 1
                for shoe in shoes:
                    sc = match_score(product, shoe)
                    if sc is not None and (shoe["id"] not in best or sc > best[shoe["id"]][0]):
                        best[shoe["id"]] = (sc, product)
            break
        stores.append({"name": name, "id": adv, "country": cc, "feed": feed_ok, "products": lines, "matched": len(best)})
        for sid, (sc, p) in best.items():
            price, cur = price_of(p)
            link = find(p, "aw_deep_link") or find(p, "deep_link")
            if not link:
                continue
            extra = find(p, "additional_image_link") or []
            entry = found.setdefault(sid, {"offers": [], "images": [], "fetched": now})
            entry["offers"].append({"store": name, "advertiser": adv, "country": cc, "link": link, "price": price, "currency": cur or prog.get("currencyCode")})
            for u in [find(p, "image_link") or find(p, "merchant_image_url") or find(p, "aw_image_url"), *(extra if isinstance(extra, list) else [extra])]:
                if isinstance(u, str) and u not in entry["images"]:
                    entry["images"].append(u)

    # keep last week's data for a store whose feed failed this time
    failed = {s["id"] for s in stores if not s["feed"]}
    for sid, old in previous.items():
        for off in old.get("offers", []):
            if off.get("advertiser") in failed:
                e = found.setdefault(sid, {"offers": [], "images": old.get("images", []), "fetched": old.get("fetched")})
                e["offers"].append(off)

    json.dump(found, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    by_id = {s["id"]: s for s in shoes}
    with open(os.path.join(DATA, "awin_review.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["shoe_id", "brand", "model", "stores", "images"])
        for sid, e in sorted(found.items()):
            s = by_id[sid]
            w.writerow([sid, s["brand"], s["model"], "; ".join(o["store"] for o in e["offers"]), len(e["images"])])

    lines = ["### Awin", "", f"Joined programmes: **{len(joined)}**, waiting for approval: **{len(pending)}**.", "",
             "| Store | Country | Feed | Products | Shoes matched |", "|---|---|---|---|---|"]
    lines += [f"| {s['name']} | {s['country']} | {'yes' if s['feed'] else 'no Enhanced Feed'} | {s['products']} | {s['matched']} |" for s in stores]
    if pending:
        lines += ["", "Waiting for approval: " + ", ".join(p.get("name", "") for p in pending)]
    print("\n".join(lines))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
