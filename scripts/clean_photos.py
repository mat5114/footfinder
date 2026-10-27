"""Turn AliExpress listing photos into clean product cut-outs.

For every shoe in data/aliexpress.json that has photos, this script:
  1. downloads the main image and the gallery images,
  2. removes the background (rembg) from each and keeps only photos that show a
     single shoe from the side (not the outsole, the back, a pair or a collage),
  3. takes the cleanest of those, trims it to the shoe and saves a transparent
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
from collections import deque

from PIL import Image, ImageFilter, ImageStat

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "docs", "img")
CACHE = os.path.join(DATA, "photo_cache.json")
MAX_W = 640
VERSION = 2  # bump to redo every cut-out when the selection rules change


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
    return canvas


def shape_report(rgba):
    """Is this cut-out a single shoe seen from the side?"""
    a = rgba.getchannel("A")
    w0, h0 = a.size
    W = 120
    H = max(1, round(h0 * W / w0))
    m = a.resize((W, H)).point(lambda v: 1 if v > 128 else 0)
    if m.getbbox():
        m = m.crop(m.getbbox())
        W, H = m.size
    px = m.load()
    grid = [[px[x, y] for x in range(W)] for y in range(H)]
    filled = sum(map(sum, grid))
    if not filled:
        return {"ok": False, "why": "empty"}
    aspect = w0 / h0
    # top-bottom mirror overlap: an outsole seen from below is nearly symmetric, a side view is not
    inter = sum(grid[y][x] and grid[H - 1 - y][x] for y in range(H) for x in range(W))
    sym = inter / filled
    # separate blobs (pairs of shoes, extra items)
    seen = [[0] * W for _ in range(H)]
    sizes = []
    for y in range(H):
        for x in range(W):
            if grid[y][x] and not seen[y][x]:
                q, n = deque([(y, x)]), 0
                seen[y][x] = 1
                while q:
                    cy, cx = q.popleft(); n += 1
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = 1; q.append((ny, nx))
                sizes.append(n)
    big = [s for s in sizes if s > filled * 0.12]
    # leftover background stuck in the corners
    cw, ch = max(1, W // 10), max(1, H // 6)
    corners = [sum(grid[y][x] for y in ys for x in xs) / (len(ys) * len(xs))
               for ys in (range(0, ch), range(H - ch, H)) for xs in (range(0, cw), range(W - cw, W))]
    top_corner_fill = max(corners[0], corners[1])
    # a clean cut-out touches its left/right edge only at the toe and heel tips
    side_touch = max(sum(grid[y][x] for y in range(H) for x in xs) / (H * len(xs)) for xs in (range(0, 2), range(W - 2, W)))
    why = []
    if not 1.7 <= aspect <= 3.8: why.append(f"aspect {aspect:.2f}")
    if sym > 0.8: why.append(f"symmetric {sym:.2f} (sole view)")
    if len(big) > 1: why.append(f"{len(big)} objects")
    if side_touch > 0.28: why.append(f"background left at the edges ({side_touch:.2f})")
    return {"ok": not why, "why": ", ".join(why), "aspect": round(aspect, 2), "sym": round(sym, 2), "edge": round(side_touch, 2)}


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
        if cache.get(sid, {}).get("sources") == sources and cache[sid].get("v") == VERSION and os.path.exists(path):
            kept += 1
            continue
        scored = []
        for url in dict.fromkeys(sources):
            try:
                im = fetch(url)
                scored.append((cleanliness(im), url, im))
            except Exception as e:
                print(f"! {sid}: could not load {url}: {e}", file=sys.stderr)
        # Cut out every photo, keep only single shoes seen from the side, then take the cleanest
        result, reasons = None, []
        for score, url, im in sorted(scored, key=lambda x: -x[0]):
            cut = cutout(im, remove)
            report = shape_report(cut) if cut else {"ok": False, "why": "nothing left after removing the background"}
            if report["ok"]:
                result = cut
                break
            reasons.append(report["why"])
        if result:
            result.save(path, "WEBP", quality=88, method=6)
            cache[sid] = {"sources": sources, "chosen": url, "v": VERSION}
            done += 1
        else:
            failed += 1
            if os.path.exists(path):
                os.remove(path)
            cache.pop(sid, None)
            print(f"! {sid}: no side-view photo ({'; '.join(reasons)[:200]})", file=sys.stderr)

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
