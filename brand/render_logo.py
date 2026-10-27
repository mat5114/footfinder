"""Render the Footfinder logo files (PNG) with Pillow. Run: python3 brand/render_logo.py"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
INK, STONE = (41, 37, 36, 255), (245, 245, 244, 255)
FONT = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"

# The shoe mark, same path as the site's logo (22-unit grid), as cubic segments.
SEGMENTS = [
    ("M", (2, 15.5)),
    ("C", (5.5, 15.5), (6.8, 8.5), (11, 8.5)),
    ("C", (14.6, 8.5), (14.8, 11.5), (19.5, 11.5)),
    ("L", (19.5, 14.8)),
    ("C", (19.5, 16.1), (18.7, 17), (17.3, 17)),
    ("L", (3.6, 17)),
    ("C", (2.6, 17), (2, 16.4), (2, 15.5)),
]


def shoe_points(scale, ox, oy):
    pts, cur = [], None
    for seg in SEGMENTS:
        if seg[0] in ("M", "L"):
            cur = seg[1]
            pts.append(cur)
        else:
            p0, (p1, p2, p3) = cur, seg[1:]
            for i in range(1, 41):
                t = i / 40
                x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
                y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
                pts.append((x, y))
            cur = p3
    return [(ox + x * scale, oy + y * scale) for x, y in pts]


def icon(size, ss=4):
    S = size * ss
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.219), fill=INK)
    scale = S * 0.6 / 17.5  # mark is 17.5 units wide
    ox = S / 2 - 10.75 * scale
    oy = S / 2 - 12.75 * scale
    d.polygon(shoe_points(scale, ox, oy), fill=STONE)
    return im.resize((size, size), Image.LANCZOS)


def wordmark(color, height=240, ss=4):
    H = height * ss
    font = ImageFont.truetype(FONT, int(H * 0.52))
    text = "Footfinder"
    scale = H * 0.035
    mark_w = 17.5 * scale
    gap = H * 0.16
    tb = font.getbbox(text)
    W = int(H * 0.17 + mark_w + gap + (tb[2] - tb[0]) + H * 0.17)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    ox = H * 0.17 - 2 * scale
    d.polygon(shoe_points(scale, ox, H / 2 - 12.75 * scale), fill=color)
    tx = H * 0.17 + mark_w + gap
    ty = H / 2 - (tb[1] + tb[3]) / 2
    d.text((tx - tb[0], ty), text, font=font, fill=color)
    return im.resize((W // ss, height), Image.LANCZOS)


if __name__ == "__main__":
    for s in (1024, 512, 120):
        icon(s).save(os.path.join(HERE, f"icon-{s}.png"))
    wordmark(INK).save(os.path.join(HERE, "logo.png"))
    wordmark(STONE).save(os.path.join(HERE, "logo-white.png"))
    print("Rendered brand/*.png")
