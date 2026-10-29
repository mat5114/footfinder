"""Build the Footfinder site.

Reads data/running_shoes.json (plus data/aliexpress.json, data/awin.json and data/amazon.json when present), packs it into the compact array the page uses,
injects it into src/footfinder.template.html and writes (GitHub Pages serves the docs/ folder):
  - docs/index.html      a complete standalone page (deploy this folder)
  - docs/artifact.html   the same page without the document shell (for Claude artifacts)
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def store_fields(sid, hit, awin):
    """[photo or null, AliExpress link or null, null, Awin offers] for one shoe.

    The photo is the background-free cut-out made by scripts/clean_photos.py from
    any store's photos; without one, the site keeps the drawing. The AliExpress
    link goes to the AliExpress search for the shoe. Awin offers are
    [store, country, affiliate link, price, currency] for each joined store that sells it.
    """
    cut = os.path.join(ROOT, "docs", "img", f"{sid}.webp")
    img = f"img/{sid}.webp" if os.path.exists(cut) else None
    ali = (hit or {}).get("search_link") or (hit or {}).get("link")
    offers = [[o["store"], o.get("country"), o["link"], o.get("price"), o.get("currency")] for o in (awin or {}).get("offers", [])]
    if not (img or ali or offers):
        return []
    return [img, ali, None, offers]


def compact(shoes, ali, awin):
    idx = {s["id"]: i for i, s in enumerate(shoes)}
    out = []
    for s in shoes:
        out.append([
            s["brand"], s["model"], 1 if s["status"] == "current" else 0, s["release_year"],
            s["categories"], s["surface"], s["msrp_usd"], s["weight_g_mens_us9"],
            s["stack_heel_mm"], s["stack_forefoot_mm"], s["foam_name"], s["foam_type"],
            s["plate"], s["ride_feel"], s["stability"], 1 if s["wide_available"] else 0,
            s["distances"], 1 if s["suits_heavier_runners"] else 0, 1 if s["popular_pick"] else 0,
            [idx[x] for x in s["similar"] if x in idx], 1 if s["is_chinese_brand"] else 0,
            s["data_quality"]["spec_confidence"][0],
            *store_fields(s["id"], ali.get(s["id"]), awin.get(s["id"])),
        ])
    return json.dumps(out, ensure_ascii=False, separators=(",", ":"))


SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Answer a few taps and Footfinder matches you with the running shoes that fit how you run.">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
{page}
</body>
</html>
"""


def main():
    shoes = json.load(open(os.path.join(ROOT, "data", "running_shoes.json"), encoding="utf-8"))["shoes"]
    ali_path = os.path.join(ROOT, "data", "aliexpress.json")
    ali = json.load(open(ali_path, encoding="utf-8")) if os.path.exists(ali_path) else {}
    awin_path = os.path.join(ROOT, "data", "awin.json")
    awin = json.load(open(awin_path, encoding="utf-8")) if os.path.exists(awin_path) else {}
    template = open(os.path.join(ROOT, "src", "footfinder.template.html"), encoding="utf-8").read()
    amz_path = os.path.join(ROOT, "data", "amazon.json")
    amz = json.load(open(amz_path, encoding="utf-8")) if os.path.exists(amz_path) else {}
    amz = {"store": amz.get("store") or "amazon.com", "tag": (amz.get("tag") or "").strip()}
    site_path = os.path.join(ROOT, "data", "site.json")
    site = json.load(open(site_path, encoding="utf-8")) if os.path.exists(site_path) else {}
    if site.get("chinese_brands_only"):
        shoes = [s for s in shoes if s["is_chinese_brand"]]
    if site.get("require_photo"):
        shoes = [s for s in shoes if os.path.exists(os.path.join(ROOT, "docs", "img", f"{s['id']}.webp"))]
    if site.get("amazon") is False:
        amz["tag"] = ""
    page = template.replace("__DATA__", compact(shoes, ali, awin)).replace("__AMAZON__", json.dumps(amz))
    dist = os.path.join(ROOT, "docs")
    os.makedirs(dist, exist_ok=True)
    open(os.path.join(dist, "artifact.html"), "w", encoding="utf-8").write(page)
    open(os.path.join(dist, "index.html"), "w", encoding="utf-8").write(SHELL.replace("{page}", page))
    print(f"Built docs/ with {len(shoes)} shoes on the site, {len([n for n in os.listdir(os.path.join(ROOT, 'docs', 'img')) if n.endswith('.webp')]) if os.path.isdir(os.path.join(ROOT, 'docs', 'img')) else 0} with photo cut-outs, {sum(1 for v in ali.values() if v.get('search_link'))} with AliExpress links, {len(awin)} with Awin offers, Amazon tag {'set' if amz['tag'] else 'not set'}")


if __name__ == "__main__":
    main()
