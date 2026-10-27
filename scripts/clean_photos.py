"""Turn AliExpress listing photos into clean product cut-outs.

For every shoe in data/aliexpress.json that has photos, this script:
  1. downloads the main image and the gallery images,
  2. picks the cleanest one: plain, light background and little text or clutter,
  3. removes the background (rembg), trims to the shoe and saves a transparent
     WebP to docs/img/<shoe id>.webp, which the site uses instead of the original.

It skips shoes whose chosen source photo has not changed since the last run
(data/photo_cache.json), so the weekly run stays quick.

Needs: pip install "rembg[cpu]" pillow
"""
import io
import json
import os
import sys
import urllib.request

from PIL import Image, ImageFilter, ImageStat

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "docs", "img")
CACHE = os.path.join(DATA, "photo_cache.json")
MAX_W = 640


def fetch(url):
    if url.startswith("//"):
        url = "https:" + url
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Footfinder photo cleaner)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return Image.open(io.BytesIO(r.read())).convert("RGB")


def cleanliness(im):
    """Higher is cleaner: light, even border and few edges (text, collages) overall."""
    small = im.resize((160, 160))
    w, h = small.size
    b = 12
    border = [small.crop(box) for box in ((0, 0, w, b), (0, h - b, w, h), (0, 0, b, h), (w - b, 0, w, h))]
    stats = [ImageStat.Stat(x) for x in border]
    spread = sum(sum(s.stddev) / 3 for s in stats) / 4          # 0 = perfectly even background
    light = sum(sum(s.mean) / 3 for s in stats) / 4            # 255 = white background
    edges = ImageStat.Stat(small.convert("L").filter(ImageFilter.FIND_EDGES)).mean[0]
    return light / 255 * 40 - spread * 1.5 - edges * 2.5


def cutout(im, remove):
    out = remove(im)  # RGBA with transparent background
    alpha = out.getchannel("A").point(lambda a: 255 if a > 24 else 0)
    box = alpha.getbbox()
    if not box:
        return None
    out = out.crop(box)
    pad = int(max(out.size) * 0.04)
    canvas = Image.new("RGBA", (out.width + 2 * pad, out.height + 2 * pad), (0, 0, 0, 0))
    canvas.paste(out, (pad, pad))
    if canvas.width > MAX_W:
        canvas = canvas.resize((MAX_W, round(canvas.height * MAX_W / canvas.width)), Image.LANCZOS)
    # A shoe is wider than tall; a near-square cut-out usually means a collage or a box shot
    return canvas if canvas.width >= canvas.height * 1.15 else None


def main():
    try:
        from rembg import new_session, remove as rembg_remove
    except ImportError:
        sys.exit('Install rembg first: pip install "rembg[cpu]"')
    session = new_session("isnet-general-use")
    remove = lambda im: rembg_remove(im, session=session)

    ali = json.load(open(os.path.join(DATA, "aliexpress.json"), encoding="utf-8"))
    cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
    os.makedirs(OUT, exist_ok=True)
    done = kept = failed = 0

    for sid, hit in ali.items():
        sources = [u for u in [hit.get("image"), *(hit.get("gallery") or [])] if u]
        if not sources:
            continue
        path = os.path.join(OUT, f"{sid}.webp")
        if cache.get(sid, {}).get("sources") == sources and os.path.exists(path):
            kept += 1
            continue
        scored = []
        for url in dict.fromkeys(sources):
            try:
                im = fetch(url)
                scored.append((cleanliness(im), url, im))
            except Exception as e:
                print(f"! {sid}: could not load {url}: {e}", file=sys.stderr)
        result = None
        for score, url, im in sorted(scored, key=lambda x: -x[0])[:3]:  # cleanest first
            result = cutout(im, remove)
            if result:
                break
        if result:
            result.save(path, "WEBP", quality=88, method=6)
            cache[sid] = {"sources": sources, "chosen": url}
            done += 1
        else:
            failed += 1
            if os.path.exists(path):
                os.remove(path)
            cache.pop(sid, None)
            print(f"! {sid}: no clean cut-out", file=sys.stderr)

    for name in os.listdir(OUT):  # drop cut-outs for shoes that lost their photo
        if name.endswith(".webp") and name[:-5] not in ali:
            os.remove(os.path.join(OUT, name))
            cache.pop(name[:-5], None)

    json.dump(cache, open(CACHE, "w", encoding="utf-8"), indent=2)
    print(f"Cut-outs: {done} new, {kept} unchanged, {failed} without a clean photo")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(f"\nCut-outs: **{done}** new, {kept} unchanged, {failed} without a clean photo.\n")


if __name__ == "__main__":
    main()
