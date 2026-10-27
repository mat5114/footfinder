"""Build the Footfinder site.

Reads data/running_shoes.json (plus data/aliexpress.json when present), packs it into the compact array the page uses,
injects it into src/footfinder.template.html and writes (GitHub Pages serves the docs/ folder):
  - docs/index.html      a complete standalone page (deploy this folder)
  - docs/artifact.html   the same page without the document shell (for Claude artifacts)
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def photo_fields(hit):
    """[image, affiliate link, price] from data/aliexpress.json, or nothing."""
    if not hit or not hit.get("image") or not hit.get("link"):
        return []
    return [hit["image"], hit["link"], hit.get("price")]


def compact(shoes, ali):
    idx = {s["id"]: i for i, s in enumerate(shoes)}
    out = []
    for s in shoes:
        out.append([
            s["brand"], s["model"], 1 if s["status"] == "current" else 0, s["release_year"],
            s["categories"], s["surface"], s["msrp_usd"], s["weight_g_mens_us9"],
            s["stack_heel_mm"], s["stack_forefoot_mm"], s["foam_name"], s["foam_type"],
            s["plate"], s["ride_feel"], s["stability"], 1 if s["wide_available"] else 0,
            s["distances"], 1 if s["suits_heavier_runners"] else 0, 1 if s["popular_pick"] else 0,
            [idx[x] for x in s["similar"]], 1 if s["is_chinese_brand"] else 0,
            s["data_quality"]["spec_confidence"][0],
            *photo_fields(ali.get(s["id"])),
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
    template = open(os.path.join(ROOT, "src", "footfinder.template.html"), encoding="utf-8").read()
    page = template.replace("__DATA__", compact(shoes, ali))
    dist = os.path.join(ROOT, "docs")
    os.makedirs(dist, exist_ok=True)
    open(os.path.join(dist, "artifact.html"), "w", encoding="utf-8").write(page)
    open(os.path.join(dist, "index.html"), "w", encoding="utf-8").write(SHELL.replace("{page}", page))
    print(f"Built docs/ with {len(shoes)} shoes, {sum(1 for v in ali.values() if v.get('image'))} with AliExpress photos")


if __name__ == "__main__":
    main()
