"""Find which big Western running brands have an official store on AliExpress.

Report only: this does not change the site. For each non-Chinese brand in the
catalog it searches the AliExpress Affiliate API for "<brand> running shoes",
groups the listings by shop, looks up each shop's name, and marks a shop as
official when its name has the brand and "official" in it (e.g. "PUMA Official
Store"). Results go to data/official_stores.json and the run summary.

Credentials: ALIEXPRESS_APP_KEY, ALIEXPRESS_APP_SECRET, ALIEXPRESS_TRACKING_ID.
"""
import json
import os
import re
import sys
import time
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aliexpress_fetch import BRAND_TERMS, call, is_empty, norm, note, products_of

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data")


def shop_name(product, url):
    for k in ("shop_name", "store_name", "seller_name"):
        if product.get(k):
            return product[k]
    if not url:
        return None
    try:
        req = urllib.request.Request(url if url.startswith("http") else "https:" + url,
                                     headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.8"})
        html = urllib.request.urlopen(req, timeout=20).read(200000).decode("utf-8", "replace")
    except Exception:
        return None
    for pat in (r'"storeName"\s*:\s*"([^"]+)"', r'"shopName"\s*:\s*"([^"]+)"', r"<title>([^<]+)</title>"):
        m = re.search(pat, html)
        if m:
            name = re.split(r"\s+-\s+|\|", m.group(1))[0].strip()
            if name and "aliexpress" not in name.lower():
                return name
    return None


def main():
    key = (os.environ.get("ALIEXPRESS_APP_KEY") or "").strip()
    secret = (os.environ.get("ALIEXPRESS_APP_SECRET") or "").strip()
    tracking = (os.environ.get("ALIEXPRESS_TRACKING_ID") or "").strip()
    if not (key and secret and tracking):
        note("error", "Missing AliExpress secrets")
        sys.exit(1)
    shoes = json.load(open(os.path.join(DATA, "running_shoes.json"), encoding="utf-8"))["shoes"]
    brands = sorted({s["brand"] for s in shoes if not s["is_chinese_brand"]}, key=lambda b: -sum(s["brand"] == b for s in shoes))
    common = {"target_currency": "USD", "target_language": "EN", "tracking_id": tracking}
    report, names = {}, {}

    for brand in brands:
        b = norm(brand)
        shops = defaultdict(lambda: {"listings": 0, "examples": []})
        for page in (1, 2):
            try:
                res = call("aliexpress.affiliate.product.query",
                           {**common, "keywords": f"{brand} running shoes", "page_size": 50, "page_no": page, "sort": "LAST_VOLUME_DESC"}, key, secret)
            except RuntimeError as e:
                if not is_empty(e):
                    note("warning", f"{brand}: {e}")
                break
            for p in products_of(res):
                title = norm(p.get("product_title", ""))
                if f" {b} " not in f" {title} ":
                    continue  # listing does not even name the brand
                sid = str(p.get("shop_id") or p.get("shop_url") or "?")
                sh = shops[sid]
                sh["listings"] += 1
                sh["url"] = p.get("shop_url")
                sh["_product"] = p
                if len(sh["examples"]) < 3:
                    sh["examples"].append(p.get("product_title", "")[:90])
            time.sleep(0.4)
        top = sorted(shops.items(), key=lambda kv: -kv[1]["listings"])[:6]
        out = []
        for sid, sh in top:
            if sid not in names:
                names[sid] = shop_name(sh.pop("_product", {}), sh.get("url"))
                time.sleep(0.5)
            sh.pop("_product", None)
            nm = names[sid] or ""
            official = bool(nm) and b in norm(nm) and "official" in nm.lower()
            out.append({"shop_id": sid, "name": nm or None, "official": official, **sh})
        report[brand] = {"listings": sum(s["listings"] for s in shops.values()), "shops": out,
                         "official_store": next((s["name"] for s in out if s["official"]), None)}
        print(f"{brand}: {report[brand]['listings']} listings, official: {report[brand]['official_store']}", flush=True)

    json.dump({"checked": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "brands": report},
              open(os.path.join(DATA, "official_stores.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    lines = ["### Official brand stores on AliExpress", "", "| Brand | Listings naming the brand | Official store |", "|---|---|---|"]
    lines += [f"| {b} | {r['listings']} | {r['official_store'] or '—'} |" for b, r in report.items()]
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        open(summary, "a", encoding="utf-8").write("\n".join(lines) + "\n")
    found = [f"{b} ({r['official_store']})" for b, r in report.items() if r["official_store"]]
    note("notice", "Official stores: " + (", ".join(found) if found else "none found"))


if __name__ == "__main__":
    main()
