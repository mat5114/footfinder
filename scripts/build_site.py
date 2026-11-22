"""Build the Footfinder site.

Reads data/running_shoes.json (plus data/aliexpress.json, data/awin.json and data/amazon.json when present), packs it into the compact array the page uses,
injects it into src/footfinder.template.html and writes (GitHub Pages serves the docs/ folder):
  - docs/index.html      a complete standalone page (deploy this folder)
  - build/artifact.html  the same page without the document shell (for Claude artifacts, not published)
"""
import datetime
import json
import shutil
import re
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
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<base href="/">
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{alternates}<script>window.PAGE_LANG="{code}"</script>
<meta property="og:type" content="website">
<meta property="og:site_name" content="Footfinder">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://footfinder.cc/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
{page}
</body>
</html>
"""


# one page per language, so search engines can find each one (code, folder, html lang, title, description)
PAGES = [
    ("en", "", "en", "Footfinder · Find your Chinese running shoe",
     "Free quiz to find Chinese running shoes. Tap a few answers, get up to 12 picks from Li-Ning, Xtep, ANTA and more. Independent, no typing."),
    ("pt", "pt/", "pt-BR", "Footfinder · Encontre seu tênis de corrida chinês",
     "Quiz grátis para achar tênis de corrida chineses. Toque em algumas respostas e receba até 12 sugestões de Li-Ning, Xtep, ANTA e outras. Independente, sem digitar."),
    ("pp", "pt-pt/", "pt-PT", "Footfinder · Encontra as tuas sapatilhas de corrida chinesas",
     "Quiz grátis para encontrar sapatilhas de corrida chinesas. Toca em algumas respostas e recebe até 12 sugestões de Li-Ning, Xtep, ANTA e outras. Independente, sem escrever."),
    ("es", "es/", "es", "Footfinder · Encuentra tu zapatilla de running china",
     "Test gratis para encontrar zapatillas de running chinas. Toca unas respuestas y recibe hasta 12 opciones de Li-Ning, Xtep, ANTA y más. Independiente, sin escribir."),
    ("fr", "fr/", "fr", "Footfinder · Trouvez votre chaussure de running chinoise",
     "Quiz gratuit pour trouver des chaussures de running chinoises. Touchez quelques réponses et recevez jusqu'à 12 modèles Li-Ning, Xtep, ANTA et plus. Indépendant, sans rien écrire."),
    ("de", "de/", "de", "Footfinder · Finde deinen chinesischen Laufschuh",
     "Kostenloses Quiz für chinesische Laufschuhe. Tippe ein paar Antworten an und erhalte bis zu 12 Vorschläge von Li-Ning, Xtep, ANTA und mehr. Unabhängig, ohne Tippen."),
    ("it", "it/", "it", "Footfinder · Trova la tua scarpa da running cinese",
     "Quiz gratuito per trovare scarpe da running cinesi. Tocca qualche risposta e ricevi fino a 12 proposte di Li-Ning, Xtep, ANTA e altri. Indipendente, senza scrivere."),
]
BASE = "https://footfinder.cc/"


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
    # the single-file copy for Claude artifacts stays out of the public site
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    open(os.path.join(ROOT, "build", "artifact.html"), "w", encoding="utf-8").write(page)
    # the live site links the icon files in docs/ (every browser shows these); the artifact keeps inline icons
    site = re.sub(r'<link rel="(?:icon|apple-touch-icon)"[^>]*>\n?', "", page)
    icons = ('<link rel="icon" href="favicon.ico" sizes="any">\n<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">\n'
             '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n')
    # the tab title and icons belong in <head>, where browsers look for them
    # everything before the first page element (title, styles, fonts) belongs in <head>
    cut = site.index('<div class="top">')
    head, body = site[:cut], site[cut:]
    # the artifact-only viewport hint does not belong on the public site
    head = re.sub(r'<meta name="claude:[^"]*"[^>]*>\n?', "", head)
    alternates = "".join(f'<link rel="alternate" hreflang="{hl}" href="{BASE}{folder}">\n' for _, folder, hl, _, _ in PAGES)
    alternates += f'<link rel="alternate" hreflang="x-default" href="{BASE}">\n'
    for code, folder, hl, title, desc in PAGES:
        page_head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, count=1)
        html = (SHELL.replace("{lang}", hl).replace("{desc}", desc).replace("{title}", title)
                .replace("{url}", BASE + folder).replace("{alternates}", alternates).replace("{code}", code))
        html = html.replace("{page}", body).replace("</head>", page_head + icons + "</head>", 1)
        os.makedirs(os.path.join(dist, folder), exist_ok=True)
        open(os.path.join(dist, folder, "index.html"), "w", encoding="utf-8").write(html)
    shutil.copyfile(os.path.join(ROOT, "src", "about.template.html"), os.path.join(dist, "about.html"))
    # help search engines find the pages
    today = datetime.date.today().isoformat()
    urls = [BASE + folder for _, folder, _, _, _ in PAGES] + [BASE + "about.html"]
    open(os.path.join(dist, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    open(os.path.join(dist, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\n\nSitemap: https://footfinder.cc/sitemap.xml\n")
    old = os.path.join(dist, "artifact.html")
    if os.path.exists(old):
        os.remove(old)
    print(f"Built docs/ with {len(shoes)} shoes on the site, {len([n for n in os.listdir(os.path.join(ROOT, 'docs', 'img')) if n.endswith('.webp')]) if os.path.isdir(os.path.join(ROOT, 'docs', 'img')) else 0} with photo cut-outs, {sum(1 for s in shoes if (ali.get(s['id']) or {}).get('search_link') or (ali.get(s['id']) or {}).get('link'))} of them with an AliExpress link, {len(awin)} with Awin offers, Amazon tag {'set' if amz['tag'] else 'not set'}")


if __name__ == "__main__":
    main()
