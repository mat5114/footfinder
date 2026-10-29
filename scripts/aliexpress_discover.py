"""List the Chinese running shoe models that are actually for sale on AliExpress.

Report only: searches the AliExpress Affiliate API with several running keywords
per Chinese brand, pulls the model name out of each listing title (the words
right after the brand, up to words like "running", "shoes", "men's"), and counts
how many listings and sales each model has. Models already in the catalog are
flagged, so new ones are easy to spot. Results go to data/aliexpress_discovery.json.

Credentials: ALIEXPRESS_APP_KEY, ALIEXPRESS_APP_SECRET, ALIEXPRESS_TRACKING_ID.
"""
import json
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aliexpress_fetch import BRAND_TERMS, NOT_SHOES, call, is_empty, norm, note, products_of

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data")

BRANDS = dict(BRAND_TERMS)
BRANDS.update({"ERKE": ["erke", "hongxing erke"], "ONEMIX": ["onemix"]})
KEYWORDS = ["running shoes", "marathon running shoes", "carbon plate running shoes", "trail running shoes",
            "cushioning running shoes", "racing shoes"]
STOP = set("""running run runner shoes shoe sneakers sneaker trainers trainer men men's mens women women's womens unisex
male female low top low-top lowtop high mid breathable cushioning cushion cushioned lightweight light professional marathon
racing race sports sport outdoor casual new arrival 2023 2024 2025 2026 original genuine official fabric mesh rubber eva
slip resistant abrasion wear rebound shock absorption absorbing anti-slip non-slip comfortable comfort durable stable
stability support training jogging road trail fitness gym walking tennis basketball for with and the of in kids boys girls
summer winter spring autumn color s degrees""".split())
COLORS = set("white black red blue green pink grey gray orange yellow purple silver gold".split())  # "Red Hare" starts with one


def model_from(title, terms):
    t = norm(title)
    words = t.split()
    for term in sorted(terms, key=len, reverse=True):
        tw = term.split()
        for i in range(len(words) - len(tw) + 1):
            if words[i:i + len(tw)] == tw:
                rest = words[i + len(tw):]
                while rest and rest[0] in STOP:
                    rest = rest[1:]
                out = []
                for w in rest:
                    if w in STOP or (out and w in COLORS) or re.fullmatch(r"[a-z]{2,}\d{3,}.*|\d{5,}.*", w):
                        break
                    out.append(w)
                    if len(out) == 4:
                        break
                return " ".join(out) or None
    return None


def main():
    key = (os.environ.get("ALIEXPRESS_APP_KEY") or "").strip()
    secret = (os.environ.get("ALIEXPRESS_APP_SECRET") or "").strip()
    tracking = (os.environ.get("ALIEXPRESS_TRACKING_ID") or "").strip()
    if not (key and secret and tracking):
        note("error", "Missing AliExpress secrets")
        sys.exit(1)
    shoes = json.load(open(os.path.join(DATA, "running_shoes.json"), encoding="utf-8"))["shoes"]
    known = {(s["brand"], norm(s["model"])) for s in shoes}
    common = {"target_currency": "USD", "target_language": "EN", "tracking_id": tracking}
    found = defaultdict(lambda: {"listings": 0, "volume": 0, "titles": [], "prices": [], "ids": set()})

    for brand, terms in BRANDS.items():
        for kw in KEYWORDS:
            for page in (1, 2, 3):
                try:
                    res = call("aliexpress.affiliate.product.query",
                               {**common, "keywords": f"{terms[0]} {kw}", "page_size": 50, "page_no": page, "sort": "LAST_VOLUME_DESC"}, key, secret)
                except RuntimeError as e:
                    if not is_empty(e):
                        note("warning", f"{brand} / {kw}: {e}")
                    break
                prods = products_of(res)
                for p in prods:
                    title = p.get("product_title", "")
                    words = set(norm(title).split())
                    if words & NOT_SHOES:
                        continue
                    m = model_from(title, terms)
                    if not m or len(m) < 2:
                        continue
                    pid = str(p.get("product_id"))
                    e = found[(brand, m)]
                    if pid in e["ids"]:
                        continue
                    e["ids"].add(pid)
                    e["listings"] += 1
                    e["volume"] += int(p.get("lastest_volume") or 0)
                    if len(e["titles"]) < 3:
                        e["titles"].append(title[:110])
                    pr = p.get("target_sale_price") or p.get("sale_price")
                    if pr:
                        e["prices"].append(float(pr))
                if len(prods) < 50:
                    break
                time.sleep(0.35)

    rows = []
    for (brand, m), e in found.items():
        pr = sorted(e["prices"])
        rows.append({"brand": brand, "model": m, "in_catalog": (brand, m) in known, "listings": e["listings"],
                     "volume": e["volume"], "median_price_usd": pr[len(pr) // 2] if pr else None, "titles": e["titles"]})
    rows.sort(key=lambda r: (-r["volume"], -r["listings"]))
    json.dump({"checked": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "models": rows},
              open(os.path.join(DATA, "aliexpress_discovery.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    new = [r for r in rows if not r["in_catalog"]]
    note("notice", f"Discovery: {len(rows)} model names, {len(new)} not in the catalog")


if __name__ == "__main__":
    main()
