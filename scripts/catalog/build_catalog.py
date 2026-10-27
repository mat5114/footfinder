import json, re, math, unicodedata
from data_western import ROWS as W
from data_china import ROWS as C

ORIGIN = {"Nike":"US","adidas":"DE","ASICS":"JP","Brooks":"US","HOKA":"US","New Balance":"US","Saucony":"US",
 "Mizuno":"JP","PUMA":"DE","On":"CH","Altra":"US","Salomon":"FR","Under Armour":"US","Skechers":"US",
 "Diadora":"IT","Topo Athletic":"US","Merrell":"US","La Sportiva":"IT","inov-8":"GB","Craft":"SE","Karhu":"FI",
 "Kiprun":"FR","Olympikus":"BR","Li-Ning":"CN","ANTA":"CN","Xtep":"CN","361°":"CN","PEAK":"CN","Qiaodan":"CN","Kailas":"CN"}

CATS={"daily","tempo","race","long","recovery","stab","trail","budget"}
SURF={"road","trail","mixed"}; FOAM={"EVA","sEVA","TPU","PEBA","TPEE","blend"}
PLATE={"none","carbon","carbon_rods","glassfiber","nylon"}; FEEL={"soft","balanced","firm","bouncy"}
STAB={"neutral","mild","stable"}; CONF={"h":"high","m":"medium","l":"low"}

# Specs cross-checked against a published source during this build
CHECKED = {
 "asics-novablast-6":"RTINGS lab measurement (247.7 g; 41.9/33.1 mm)",
 "asics-gel-kayano-33":"RTINGS lab measurement (295.9 g; 41.5/30.4 mm)",
 "saucony-hurricane-26":"RTINGS lab measurement (260.6 g; 41.4/33.7 mm)",
 "nike-structure-26":"RTINGS lab measurement (293.9 g; 37.9/29.4 mm)",
 "on-cloudrunner-2":"RTINGS lab measurement (275.3 g; 34.7/25.4 mm)",
 "new-balance-fuelcell-supercomp-elite-v6":"RTINGS lab measurement (187.1 g; 39.2/30.3 mm)",
 "brooks-ghost-amp":"RTINGS lab measurement (stack 36.1/29.4 mm)",
 "li-ning-red-hare-9-ultra":"Road Trail Run measurement (246 g US9.5; 47/42 mm), MSRP RMB899",
 "anta-zone2-90":"Road Trail Run measurement (188 g US9.5; 40/34 mm), MSRP RMB699",
 "xtep-2000km-5-pro":"Road Trail Run (MSRP RMB399)",
 "hoka-cielo-x1-3-0":"TrainingPlan.dev catalog (48/41 mm, 7 mm drop)",
 "on-cloudultra-pro":"Road Trail Run (38.5/32.5 mm, 263 g US8.5)",
 "hoka-rocket-x-trail":"Road Trail Run (45/39 mm, ~256 g US8.5)",
 "topo-athletic-specter-3":"Road Trail Run (official stack 39/34 mm)",
 "361-lynx":"RunnersPicks review (USD 150, 6 mm drop)",
}

POPULAR = {"Pegasus 41","Pegasus 40","Vomero 18","Vaporfly 3","Invincible 3","Structure 25","Zoom Fly 6","Winflo 11",
 "Adizero Boston 12","Adizero Adios Pro 3","Ultraboost Light","Supernova Rise","Adizero SL","Adizero Evo SL","Duramo SL 2",
 "Novablast 5","Novablast 4","Gel-Nimbus 26","Gel-Kayano 31","Gel-Cumulus 26","GT-2000 13","Superblast 2","Metaspeed Sky Paris","Gel-Contend 9",
 "Ghost 16","Ghost 17","Glycerin 21","Adrenaline GTS 24","Ghost Max 2",
 "Clifton 9","Clifton 10","Bondi 8","Mach 6","Arahi 7","Speedgoat 6","Rincon 4",
 "Fresh Foam X 1080v13","Fresh Foam X 1080v14","FuelCell Rebel v4","Fresh Foam X 880v14","Fresh Foam X 860v14",
 "Ride 17","Guide 17","Triumph 22","Endorphin Speed 4","Endorphin Pro 4","Kinvara 14",
 "Wave Rider 28","Wave Inspire 20","Velocity Nitro 3","Deviate Nitro 3","Cloudmonster 2","Cloudsurfer","Torin 7","Lone Peak 8",
 "Red Hare 8 Pro","Feidian 4 Elite","160X 6.0 Pro","Flame 4","Corre 3","Speedcross 5"}

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode()
    return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")

def parse(block, region):
    out=[]
    for line in block.strip().splitlines():
        p=[x.strip() for x in line.split("|")]
        assert len(p)==17, line
        b,m,st,yr,cats,surf,usd,g,h,f,fname,ftype,plate,feel,stab,wide,conf=p
        cats=cats.split(",")
        assert set(cats)<=CATS and surf in SURF and ftype in FOAM and plate in PLATE and feel in FEEL and stab in STAB and conf in CONF, line
        out.append(dict(b=b,m=m,st=st,yr=int(yr),cats=cats,surf=surf,usd=int(usd),g=int(g),h=float(h),f=float(f),
                        fname=fname,ftype=ftype,plate=plate,feel=feel,stab=stab,wide=wide=="y",conf=conf,cn=region))
    return out

rows = parse(W,False)+parse(C,True)

def cushion(h):
    return "low" if h<30 else "medium" if h<36 else "high" if h<42 else "max"
def wclass(g):
    return "light" if g<230 else "medium" if g<280 else "heavy"
def tier(u):
    return "budget" if u<100 else "mid" if u<=160 else "premium" if u<=220 else "elite"

def levels(r):
    c=set(r["cats"])
    if "race" in c and len(c)<=2 and r["plate"]!="none": return ["advanced"]
    lv=[]
    if c & {"daily","budget","stab","recovery"} or ("long" in c and "race" not in c): lv.append("beginner")
    lv.append("intermediate")
    if c & {"tempo","race","long"} or "trail" in c: lv.append("advanced")
    return lv

def distances(r):
    c=set(r["cats"]); d=set()
    if "trail" in c:
        d|={"5k","10k","21k"}
        if "long" in c or "race" in c: d|={"42k","ultra"}
        return sorted(d,key=["5k","10k","21k","42k","ultra"].index)
    d|={"5k","10k"}
    if r["h"]>=33 or c&{"long","race","tempo"}: d.add("21k")
    if c&{"long","race"} or r["h"]>=38: d.add("42k")
    return sorted(d,key=["5k","10k","21k","42k","ultra"].index)

def heavier_ok(r):
    # heuristic: generous stack + not ultra-light racer foam-only platform
    return r["h"]>=35 and r["g"]>=250 and "race" not in r["cats"]

FOAMSCORE={"EVA":0,"sEVA":1,"TPU":1.5,"blend":1.5,"TPEE":2,"PEBA":2.5}
FEELSCORE={"firm":0,"balanced":1,"soft":2,"bouncy":2.5}
def vec(r):
    return [r["h"]/50, (r["h"]-r["f"])/12, r["g"]/320, FOAMSCORE[r["ftype"]]/2.5, FEELSCORE[r["feel"]]/2.5,
            0 if r["plate"]=="none" else 1, {"neutral":0,"mild":.5,"stable":1}[r["stab"]], math.log(r["usd"])/math.log(500),
            1 if "race" in r["cats"] else 0, 1 if "tempo" in r["cats"] else 0]

shoes=[]; ids=set()
for r in rows:
    sid=slug(f'{r["b"]} {r["m"]}')
    assert sid not in ids, sid; ids.add(sid)
    r["id"]=sid
for r in rows:
    drop=round(r["h"]-r["f"],1)
    src = CHECKED.get(r["id"])
    shoes.append({
      "id": r["id"],
      "brand": r["b"],
      "model": r["m"],
      "brand_origin": ORIGIN[r["b"]],
      "is_chinese_brand": r["cn"],
      "status": "current" if r["st"]=="c" else "previous_version",
      "release_year": r["yr"],
      "categories": r["cats"],
      "surface": r["surf"],
      "msrp_usd": r["usd"],
      "price_tier": tier(r["usd"]),
      "weight_g_mens_us9": r["g"],
      "weight_class": wclass(r["g"]),
      "stack_heel_mm": r["h"],
      "stack_forefoot_mm": r["f"],
      "drop_mm": drop,
      "cushion_level": cushion(r["h"]),
      "foam_name": r["fname"],
      "foam_type": r["ftype"],
      "plate": r["plate"],
      "ride_feel": r["feel"],
      "stability": r["stab"],
      "wide_available": r["wide"],
      "runner_levels": levels(r),
      "distances": distances(r),
      "suits_heavier_runners": heavier_ok(r),
      "zero_drop": drop==0,
      "popular_pick": r["m"] in POPULAR,
      "gender": ["men","women"],
      "similar": [],
      "image": None,
      "affiliate_links": {"amazon_us":None,"amazon_uk":None,"amazon_de":None,"amazon_br":None,"aliexpress":None,"brand_store":None},
      "data_quality": {
        "spec_confidence": "checked" if src else CONF[r["conf"]],
        "spec_source": src or "editorial estimate from model line; verify against manufacturer spec sheet",
        "verified": bool(src),
      },
    })

# similar: nearest neighbours on same surface family
V={r["id"]:vec(r) for r in rows}
fam=lambda s:"trail" if s=="trail" else "road"
for s in shoes:
    cands=[t for t in shoes if t["id"]!=s["id"] and fam(t["surface"])==fam(s["surface"]) and t["brand"]+t["model"].split(" ")[0]!=s["brand"]+s["model"].split(" ")[0]]
    d=sorted(cands,key=lambda t:sum((a-b)**2 for a,b in zip(V[s["id"]],V[t["id"]])) + (0.05 if t["status"]!="current" else 0))
    s["similar"]=[t["id"] for t in d[:5]]

meta={
 "name":"Running shoe catalog",
 "version":"0.1.0",
 "generated":"2026-10-27",
 "count":len(shoes),
 "brands":len({s["brand"] for s in shoes}),
 "units":{"weight":"grams, men's US 9 (approx.)","stack":"mm","price":"USD list price (MSRP), not live"},
 "enums":{"categories":sorted(CATS),"surface":sorted(SURF),"foam_type":sorted(FOAM),"plate":sorted(PLATE),
          "ride_feel":sorted(FEEL),"stability":sorted(STAB),"cushion_level":["low","medium","high","max"],
          "price_tier":["budget","mid","premium","elite"]},
 "notes":["Specs marked medium/low confidence are estimates and must be checked before launch.",
          "affiliate_links are placeholders to fill per region once programs are approved.",
          "similar[] is computed from geometry, foam, plate, stability, price and use."]
}
import os
OUT=os.path.join(os.path.dirname(__file__),"..","..","data","running_shoes.json")
json.dump({"meta":meta,"shoes":shoes},open(OUT,"w"),ensure_ascii=False,indent=2)

from collections import Counter
print(len(shoes),"shoes,",meta["brands"],"brands")
print(Counter(s["data_quality"]["spec_confidence"] for s in shoes))
print(Counter(s["status"] for s in shoes))
print("chinese:",sum(s["is_chinese_brand"] for s in shoes))
print(Counter(s["surface"] for s in shoes))
