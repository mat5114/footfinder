# brand|model|status|year|cats|surface|msrp_usd|weight_g|heel_mm|fore_mm|foam_name|foam_type|plate|feel|stability|wide|conf
ROWS = """
Nike|Pegasus 42|c|2026|daily|road|145|285|37|27|ReactX + Air Zoom|EVA|none|balanced|neutral|y|m
Nike|Pegasus 41|p|2024|daily|road|140|290|37|27|ReactX + Air Zoom|EVA|none|balanced|neutral|y|h
Nike|Pegasus 40|p|2023|daily|road|130|283|33|23|React + Air Zoom|EVA|none|balanced|neutral|y|h
Nike|Pegasus 39|p|2022|daily|road|130|285|33|23|React + Air Zoom|EVA|none|balanced|neutral|y|h
Nike|Pegasus Plus|p|2024|daily,tempo|road|180|255|37|27|ZoomX|PEBA|none|bouncy|neutral|n|h
Nike|Pegasus Plus 2|c|2026|daily,tempo|road|170|255|38|28|ZoomX|PEBA|none|bouncy|neutral|n|m
Nike|Pegasus Premium|c|2025|daily,long|road|210|300|43|33|ZoomX + Air Zoom + ReactX|PEBA|none|bouncy|neutral|n|m
Nike|Pegasus Turbo Next Nature|p|2022|tempo,long|road|160|230|35|27|ZoomX|PEBA|none|bouncy|neutral|n|m
Nike|Vomero 18|c|2025|daily,long|road|150|310|46|36|ReactX + ZoomX|blend|none|soft|neutral|y|h
Nike|Vomero 17|p|2023|daily,long|road|160|290|37|27|ZoomX + Cushlon|blend|none|soft|neutral|n|h
Nike|Vomero Plus|c|2025|daily,long|road|180|275|46|36|ZoomX|PEBA|none|bouncy|neutral|n|m
Nike|Vomero Premium|c|2025|long,recovery|road|230|320|55|45|ZoomX + Air Zoom|PEBA|none|bouncy|neutral|n|m
Nike|Invincible 3|c|2023|long,recovery|road|180|310|39|30|ZoomX|PEBA|none|soft|neutral|n|h
Nike|Invincible 2|p|2022|long,recovery|road|180|310|38|29|ZoomX|PEBA|none|soft|neutral|n|h
Nike|Structure 26|c|2025|stab,daily|road|145|294|38|29|ReactX + Cushlon|EVA|none|firm|stable|y|h
Nike|Structure 25|p|2023|stab,daily|road|140|300|35|25|Cushlon|EVA|none|firm|stable|y|h
Nike|Structure Plus|c|2025|stab,daily|road|170|290|40|30|ZoomX + ReactX|blend|none|balanced|stable|n|m
Nike|React Infinity Run 3|p|2022|stab,daily|road|160|310|33|24|React|EVA|none|balanced|stable|n|h
Nike|Infinity Run 4|p|2023|stab,daily|road|160|320|38|29|ReactX|EVA|none|balanced|stable|n|h
Nike|Winflo 12|c|2026|daily,budget|road|105|295|36|26|Cushlon 3.0|EVA|none|balanced|neutral|y|m
Nike|Winflo 11|p|2024|daily,budget|road|100|290|36|26|Cushlon 3.0|EVA|none|balanced|neutral|y|m
Nike|Downshifter 14|c|2026|daily,budget|road|80|280|30|20|EVA|EVA|none|firm|neutral|n|l
Nike|Downshifter 13|p|2023|daily,budget|road|75|280|30|20|EVA|EVA|none|firm|neutral|n|l
Nike|Revolution 8|c|2025|daily,budget|road|70|270|28|18|EVA|EVA|none|firm|neutral|n|l
Nike|Interact Run|c|2024|daily,budget|road|70|250|29|19|EVA|EVA|none|balanced|neutral|n|l
Nike|Journey Run|c|2024|daily,budget|road|85|270|33|23|EVA|EVA|none|balanced|neutral|n|l
Nike|Zoom Fly 6|c|2024|tempo,race|road|170|255|42|34|ZoomX + SR-02|blend|carbon|bouncy|neutral|n|h
Nike|Zoom Fly 5|p|2022|tempo,long|road|160|275|40|32|ZoomX|EVA|carbon|firm|neutral|n|h
Nike|Vaporfly 4|c|2025|race|road|260|185|35|29|ZoomX|PEBA|carbon|bouncy|neutral|n|h
Nike|Vaporfly 3|p|2023|race|road|260|200|40|32|ZoomX|PEBA|carbon|bouncy|neutral|n|h
Nike|Vaporfly Next% 2|p|2021|race|road|250|195|40|32|ZoomX|PEBA|carbon|bouncy|neutral|n|h
Nike|Alphafly 3|c|2024|race|road|285|218|40|32|ZoomX + Air Zoom|PEBA|carbon|bouncy|neutral|n|h
Nike|Alphafly 2|p|2022|race|road|275|230|40|32|ZoomX + Air Zoom|PEBA|carbon|bouncy|neutral|n|h
Nike|Streakfly 2|c|2025|race,tempo|road|170|160|35|29|ZoomX|PEBA|none|bouncy|neutral|n|m
Nike|Rival Fly 4|c|2024|tempo,budget|road|90|230|30|22|Cushlon|EVA|none|firm|neutral|n|l
Nike|Pegasus Trail 5|c|2024|trail,daily|mixed|155|300|37|27|ReactX|EVA|none|balanced|neutral|n|h
Nike|ACG Pegasus Trail|c|2026|trail,daily|mixed|155|300|38|28|ReactX|EVA|none|balanced|neutral|n|m
Nike|ACG Zegama 3|c|2026|trail,long|trail|190|315|42|33|ZoomX|PEBA|none|soft|neutral|n|m
Nike|Zegama 2|p|2024|trail,long|trail|180|320|41|33|ZoomX|PEBA|none|soft|neutral|n|h
Nike|ACG Ultrafly Trail 2|c|2026|trail,race|trail|260|285|40|32|ZoomX|PEBA|carbon|bouncy|neutral|n|m
Nike|Ultrafly Trail|p|2023|trail,race|trail|260|295|40|32|ZoomX|PEBA|carbon|bouncy|neutral|n|h
Nike|Wildhorse 8|c|2023|trail|trail|140|310|31|23|React|EVA|none|balanced|neutral|n|m
Nike|Juniper Trail 3|c|2025|trail,budget|trail|85|290|30|21|EVA|EVA|none|firm|neutral|n|l
Nike|Kiger 10|c|2025|trail,tempo|trail|160|270|33|28|ReactX|EVA|none|balanced|neutral|n|m
adidas|Adizero Adios Pro 4|c|2025|race|road|250|220|39|33|Lightstrike Pro|TPEE|carbon_rods|bouncy|neutral|n|h
adidas|Adizero Adios Pro 3|p|2022|race|road|250|230|39|33|Lightstrike Pro|TPEE|carbon_rods|bouncy|neutral|n|h
adidas|Adizero Adios Pro 2|p|2021|race|road|200|225|39|31|Lightstrike Pro|TPEE|carbon_rods|bouncy|neutral|n|h
adidas|Adizero Adios Pro Evo 3|c|2026|race|road|500|140|39|33|Lightstrike Pro|TPEE|carbon_rods|bouncy|neutral|n|m
adidas|Adizero Adios Pro Evo 2|p|2025|race|road|500|140|39|33|Lightstrike Pro|TPEE|carbon_rods|bouncy|neutral|n|m
adidas|Adizero Prime X Evo|c|2026|tempo,long|road|500|260|50|44|Lightstrike Pro|TPEE|carbon|bouncy|neutral|n|l
adidas|Adizero Prime X 2 Strung|p|2024|tempo,long|road|300|300|50|43|Lightstrike Pro|TPEE|carbon|bouncy|neutral|n|h
adidas|Adizero Boston 13|c|2025|tempo,long|road|180|260|39|33|Lightstrike Pro + Lightstrike 2.0|blend|glassfiber|balanced|neutral|n|h
adidas|Adizero Boston 12|p|2023|tempo,long|road|160|270|39|33|Lightstrike Pro + Lightstrike 2.0|blend|glassfiber|balanced|neutral|n|h
adidas|Adizero Boston 11|p|2022|tempo,long|road|160|275|39|31|Lightstrike Pro + Lightstrike 2.0|blend|glassfiber|firm|neutral|n|h
adidas|Adizero Adios 9|c|2025|tempo,race|road|150|210|33|26|Lightstrike Pro|TPEE|none|balanced|neutral|n|m
adidas|Adizero Adios 8|p|2023|tempo,race|road|130|220|30|22|Lightstrike|EVA|none|firm|neutral|n|m
adidas|Adizero SL2|c|2024|daily,tempo|road|130|240|35|29|Lightstrike Pro + Lightstrike 2.0|blend|none|balanced|neutral|n|h
adidas|Adizero SL|p|2023|daily,tempo|road|120|255|35|26|Lightstrike Pro + Lightstrike 2.0|blend|none|balanced|neutral|n|m
adidas|Adizero Evo SL|c|2025|daily,tempo|road|150|225|39|33|Lightstrike Pro|TPEE|none|bouncy|neutral|n|h
adidas|Adizero Evo SL ATR|c|2026|tempo,long,trail|mixed|160|245|39|33|Lightstrike Pro|TPEE|none|bouncy|neutral|n|m
adidas|Adizero Takumi Sen 10|c|2024|race|road|200|190|33|27|Lightstrike Pro|TPEE|carbon_rods|firm|neutral|n|h
adidas|Adizero Pacer|c|2026|daily,tempo,budget|road|100|240|33|25|Lightstrike 2.0|EVA|none|balanced|neutral|n|l
adidas|Supernova Rise 3|c|2026|daily,long|road|140|300|37|27|Dreamstrike+|EVA|none|soft|neutral|n|m
adidas|Supernova Rise 2|p|2025|daily,long|road|140|300|37|27|Dreamstrike+|EVA|none|soft|neutral|n|h
adidas|Supernova Rise|p|2024|daily,long|road|140|300|35|25|Dreamstrike+|EVA|none|soft|neutral|n|h
adidas|Supernova Prima 2|c|2025|daily,long|road|160|300|39|29|Lightstrike Pro + Dreamstrike+|blend|none|balanced|neutral|n|m
adidas|Supernova Stride 2|c|2025|daily,budget|road|100|290|33|23|Dreamstrike+|EVA|none|balanced|neutral|n|m
adidas|Supernova Solution 2|c|2025|stab,daily|road|140|310|37|27|Dreamstrike+|EVA|none|soft|stable|n|m
adidas|Supernova Ease|c|2025|daily,budget|road|90|290|31|21|Dreamstrike+|EVA|none|balanced|neutral|n|l
adidas|Adistar 3|c|2024|long,daily|road|140|320|39|33|Repetitor|EVA|none|firm|neutral|n|m
adidas|Hyperboost Edge|c|2026|daily,long|road|200|280|40|30|Boost|TPU|none|bouncy|neutral|n|l
adidas|Ultraboost 5|c|2024|daily|road|190|330|30|20|Light Boost|TPU|none|bouncy|neutral|n|m
adidas|Ultraboost Light|p|2023|daily|road|190|300|30|20|Light Boost|TPU|none|bouncy|neutral|n|h
adidas|Zenboost|c|2026|daily,tempo|road|100|260|35|27|Boost|TPU|none|bouncy|neutral|n|l
adidas|Solarglide 6|p|2023|daily|road|140|315|34|24|Boost + Lightstrike|blend|none|balanced|neutral|n|m
adidas|Switch FWD 2|c|2024|daily,long|road|140|300|38|31|Dreamstrike+|EVA|none|balanced|neutral|n|m
adidas|Duramo SL 2|c|2024|daily,budget|road|75|270|30|20|Lightmotion|EVA|none|firm|neutral|n|l
adidas|Duramo Speed 2|c|2025|daily,budget|road|100|250|33|25|Lightstrike|EVA|none|balanced|neutral|n|l
adidas|Runfalcon 6|c|2026|daily,budget|road|65|270|28|18|Cloudfoam|EVA|none|firm|neutral|n|l
adidas|Runfalcon 5|p|2024|daily,budget|road|65|270|28|18|Cloudfoam|EVA|none|firm|neutral|n|l
adidas|Galaxy 7|c|2024|daily,budget|road|60|280|28|18|Cloudfoam|EVA|none|firm|neutral|n|l
adidas|Response Super|c|2024|daily,budget|road|90|290|32|22|Dreamstrike|EVA|none|balanced|neutral|n|l
adidas|Terrex Agravic 4|c|2026|trail|trail|145|300|34|26|Lightstrike|EVA|none|firm|neutral|n|m
adidas|Terrex Agravic Speed 2|c|2026|trail,tempo|trail|165|270|36|28|Lightstrike Pro|TPEE|none|bouncy|neutral|n|m
adidas|Terrex Agravic Speed Ultra 2|c|2025|trail,long|trail|200|265|38|30|Lightstrike Pro|TPEE|none|bouncy|neutral|n|m
adidas|Terrex Agravic TT|c|2026|trail,tempo|trail|185|260|36|28|Lightstrike Pro|TPEE|none|bouncy|neutral|n|l
adidas|Terrex Agravic Ultra|p|2023|trail,long|trail|200|330|37|31|Lightstrike|EVA|none|balanced|neutral|n|m
adidas|Terrex Soulstride|c|2024|trail,budget|trail|100|310|30|22|Bounce|EVA|none|firm|neutral|n|l
adidas|Terrex Tracerocker 2|c|2023|trail,budget|trail|90|320|28|18|EVA|EVA|none|firm|neutral|n|l
ASICS|Novablast 6|c|2026|daily,tempo,long|road|155|248|42|33|FF Blast Max|sEVA|none|bouncy|neutral|y|h
ASICS|Novablast 5|p|2025|daily,tempo|road|145|260|42|34|FF Blast Max|sEVA|none|bouncy|neutral|y|h
ASICS|Novablast 4|p|2024|daily,tempo|road|140|260|41|33|FF Blast Plus Eco|EVA|none|bouncy|neutral|y|h
ASICS|Novablast 3|p|2023|daily,tempo|road|140|255|40|32|FF Blast Plus|EVA|none|bouncy|neutral|n|h
ASICS|Dynablast 6|c|2026|daily,tempo,budget|road|120|245|36|28|FF Blast Plus|EVA|none|balanced|neutral|n|m
ASICS|Dynablast 5|p|2025|daily,tempo,budget|road|115|245|35|27|FF Blast Plus|EVA|none|balanced|neutral|n|m
ASICS|Gel-Nimbus 28|c|2026|daily,long,recovery|road|170|300|43|35|FF Blast Plus Eco + PureGel|EVA|none|soft|neutral|y|m
ASICS|Gel-Nimbus 27|p|2025|daily,long,recovery|road|165|295|43|35|FF Blast Plus Eco + PureGel|EVA|none|soft|neutral|y|h
ASICS|Gel-Nimbus 26|p|2024|daily,long,recovery|road|160|300|41|33|FF Blast Plus Eco + PureGel|EVA|none|soft|neutral|y|h
ASICS|Gel-Nimbus 25|p|2023|daily,long,recovery|road|160|295|41|33|FF Blast Plus Eco + PureGel|EVA|none|soft|neutral|y|h
ASICS|Gel-Kayano 33|c|2026|stab,long|road|170|296|42|30|FF Blast Max|sEVA|none|soft|stable|y|h
ASICS|Gel-Kayano 32|p|2025|stab,long|road|165|300|40|32|FF Blast Plus|EVA|none|soft|stable|y|h
ASICS|Gel-Kayano 31|p|2024|stab,long|road|160|305|40|30|FF Blast Plus Eco|EVA|none|soft|stable|y|h
ASICS|Gel-Kayano 30|p|2023|stab,long|road|160|305|40|30|FF Blast Plus Eco|EVA|none|soft|stable|y|h
ASICS|Gel-Cumulus 28|c|2026|daily|road|145|275|39|31|FF Blast Plus|EVA|none|balanced|neutral|y|m
ASICS|Gel-Cumulus 27|p|2025|daily|road|140|275|39|31|FF Blast Plus|EVA|none|balanced|neutral|y|h
ASICS|Gel-Cumulus 26|p|2024|daily|road|140|280|38|30|FF Blast Plus|EVA|none|balanced|neutral|y|h
ASICS|GT-2000 15|c|2026|stab,daily|road|150|285|38|30|FF Blast Plus|EVA|none|balanced|stable|y|m
ASICS|GT-2000 14|p|2025|stab,daily|road|145|285|38|30|FF Blast Plus|EVA|none|balanced|stable|y|m
ASICS|GT-2000 13|p|2024|stab,daily|road|140|290|35|27|FF Blast Plus|EVA|none|balanced|stable|y|h
ASICS|GT-2000 12|p|2023|stab,daily|road|140|290|33|25|FF Blast Plus|EVA|none|firm|stable|y|h
ASICS|GT-1000 15|c|2026|stab,budget|road|100|275|34|26|FF Blast|EVA|none|firm|stable|y|m
ASICS|GT-1000 14|p|2025|stab,budget|road|100|275|33|25|FF Blast|EVA|none|firm|stable|y|m
ASICS|Gel-Contend 10|c|2026|daily,budget|road|80|285|28|18|Amplifoam|EVA|none|firm|neutral|y|l
ASICS|Gel-Contend 9|p|2024|daily,budget|road|75|285|28|18|Amplifoam|EVA|none|firm|neutral|y|l
ASICS|Gel-Excite 11|c|2025|daily,budget|road|75|280|30|20|Amplifoam Plus|EVA|none|firm|neutral|n|l
ASICS|Gel-Excite 10|p|2023|daily,budget|road|70|280|30|20|Amplifoam Plus|EVA|none|firm|neutral|n|l
ASICS|Gel-Pulse 16|c|2025|daily,budget|road|100|280|33|23|FF Blast|EVA|none|balanced|neutral|n|l
ASICS|Versablast 4|c|2025|daily,budget|road|80|250|31|23|FF Blast|EVA|none|balanced|neutral|n|l
ASICS|Superblast 3|c|2026|daily,tempo,long|road|210|245|45|37|FF Turbo Squared + FF Blast Max|PEBA|none|bouncy|neutral|n|m
ASICS|Superblast 2|p|2024|daily,tempo,long|road|200|240|45|37|FF Turbo Plus + FF Blast Plus|PEBA|none|bouncy|neutral|n|h
ASICS|Superblast|p|2023|daily,tempo,long|road|200|240|45|37|FF Turbo + FF Blast Plus|PEBA|none|bouncy|neutral|n|h
ASICS|Sonicblast 2|c|2026|tempo,long|road|190|260|45|37|FF Blast Max + FF Turbo|blend|none|bouncy|neutral|n|l
ASICS|Sonicblast|p|2025|tempo,long|road|180|260|45|37|FF Blast Max + FF Turbo|blend|none|bouncy|neutral|n|m
ASICS|Megablast|c|2025|tempo,long|road|225|235|46|38|FF Turbo Squared|PEBA|none|bouncy|neutral|n|h
ASICS|Metaspeed Sky Tokyo|c|2025|race|road|250|170|40|35|FF Leap|PEBA|carbon|bouncy|neutral|n|h
ASICS|Metaspeed Edge Tokyo|c|2025|race|road|250|165|40|32|FF Leap|PEBA|carbon|bouncy|neutral|n|h
ASICS|Metaspeed Sky Paris|p|2024|race|road|250|185|39|34|FF Turbo Plus|PEBA|carbon|bouncy|neutral|n|h
ASICS|Metaspeed Edge Paris|p|2024|race|road|250|180|39|31|FF Turbo Plus|PEBA|carbon|bouncy|neutral|n|h
ASICS|Metaspeed Ray|c|2025|race|road|270|130|37|32|FF Turbo Plus|PEBA|carbon|bouncy|neutral|n|m
ASICS|Magic Speed 5|c|2026|tempo,race|road|180|210|40|32|FF Blast Max + FF Turbo|blend|carbon|bouncy|neutral|n|m
ASICS|Magic Speed 4|p|2024|tempo,race|road|170|215|39|31|FF Blast Turbo|blend|carbon|bouncy|neutral|n|h
ASICS|Magic Speed 3|p|2023|tempo,race|road|170|220|39|31|FF Blast Plus + FF Turbo|blend|carbon|balanced|neutral|n|h
ASICS|Hyper Speed 6|c|2026|tempo,race,budget|road|110|210|30|25|FF Blast Plus|EVA|none|firm|neutral|n|m
ASICS|Hyper Speed 4|p|2024|tempo,race,budget|road|100|205|29|24|FF Blast Plus|EVA|none|firm|neutral|n|m
ASICS|Evoride Speed 3|c|2025|tempo|road|150|230|38|32|FF Blast Plus|EVA|nylon|balanced|neutral|n|l
ASICS|Noosa Tri 16|c|2024|tempo|road|140|235|34|29|FF Blast Plus|EVA|none|balanced|neutral|n|m
ASICS|Gel-Trabuco 14|c|2026|trail|trail|145|300|38|30|FF Blast Plus|EVA|none|balanced|neutral|n|m
ASICS|Gel-Trabuco 13|p|2025|trail|trail|150|305|38|30|FF Blast Plus|EVA|none|balanced|neutral|n|m
ASICS|Trabuco Max 5|c|2026|trail,long|trail|170|315|43|38|FF Blast Max|sEVA|none|soft|neutral|n|m
ASICS|Trabuco Max 4|p|2025|trail,long|trail|160|315|43|38|FF Blast Plus|EVA|none|soft|neutral|n|m
ASICS|Fuji Lite 7|c|2026|trail,tempo|trail|140|240|31|27|FF Blast Plus|EVA|none|balanced|neutral|n|l
ASICS|Fuji Lite 5|p|2024|trail,tempo|trail|140|240|30|26|FF Blast Plus|EVA|none|balanced|neutral|n|m
ASICS|Gel-Sonoma 8|c|2025|trail,budget|trail|80|300|30|20|Amplifoam|EVA|none|firm|neutral|n|l
ASICS|Gel-Venture 10|c|2025|trail,budget|trail|75|310|29|19|Amplifoam|EVA|none|firm|neutral|n|l
ASICS|Metafuji Trail|c|2024|trail,race|trail|250|265|40|35|FF Turbo Plus|PEBA|carbon|bouncy|neutral|n|m
ASICS|Gel-Trabuco Terra 2|c|2025|trail,daily|mixed|130|300|36|28|FF Blast|EVA|none|balanced|neutral|n|l
Brooks|Ghost 18|c|2026|daily|road|150|275|36|24|DNA Loft v3|sEVA|none|soft|neutral|y|m
Brooks|Ghost 17|p|2025|daily|road|145|280|36|24|DNA Loft v3|sEVA|none|soft|neutral|y|h
Brooks|Ghost 16|p|2024|daily|road|140|285|35|23|DNA Loft v3|sEVA|none|soft|neutral|y|h
Brooks|Ghost 15|p|2023|daily|road|140|285|35|23|DNA Loft v2|EVA|none|soft|neutral|y|h
Brooks|Ghost Amp|c|2026|daily,tempo|road|150|265|36|29|DNA Flash v2|sEVA|none|bouncy|neutral|n|m
Brooks|Ghost Max 4|c|2026|daily,long,recovery|road|165|290|40|34|DNA Loft v3|sEVA|none|soft|neutral|y|m
Brooks|Ghost Max 3|p|2025|daily,long,recovery|road|150|290|40|34|DNA Loft v3|sEVA|none|soft|neutral|y|m
Brooks|Ghost Max 2|p|2024|daily,long,recovery|road|150|295|39|33|DNA Loft v3|sEVA|none|soft|neutral|y|h
Brooks|Glycerin 23|c|2026|daily,long,recovery|road|175|295|42|32|DNA Tuned|sEVA|none|soft|neutral|y|m
Brooks|Glycerin 22|p|2025|daily,long,recovery|road|165|295|42|32|DNA Tuned|sEVA|none|soft|neutral|y|h
Brooks|Glycerin 21|p|2024|daily,long,recovery|road|165|290|38|28|DNA Loft v3|sEVA|none|soft|neutral|y|h
Brooks|Glycerin 20|p|2023|daily,long,recovery|road|160|290|38|28|DNA Loft v3|sEVA|none|soft|neutral|y|h
Brooks|Glycerin GTS 23|c|2026|stab,long|road|180|305|42|32|DNA Tuned|sEVA|none|soft|stable|y|m
Brooks|Glycerin GTS 22|p|2025|stab,long|road|170|305|42|32|DNA Tuned|sEVA|none|soft|stable|y|h
Brooks|Glycerin Max|c|2025|long,recovery|road|200|300|45|39|DNA Tuned|sEVA|none|bouncy|neutral|n|h
Brooks|Glycerin Flex|c|2026|daily,recovery|road|170|280|38|30|DNA Tuned|sEVA|none|soft|neutral|n|l
Brooks|Adrenaline GTS 25|c|2025|stab,daily|road|145|285|38|26|DNA Loft v3|sEVA|none|soft|stable|y|h
Brooks|Adrenaline GTS 24|p|2024|stab,daily|road|140|285|37|25|DNA Loft v3|sEVA|none|soft|stable|y|h
Brooks|Adrenaline GTS 23|p|2023|stab,daily|road|140|285|35|23|DNA Loft v2|EVA|none|balanced|stable|y|h
Brooks|Launch 12|c|2026|daily,tempo|road|120|240|34|24|DNA Flash v2|sEVA|none|balanced|neutral|n|m
Brooks|Launch 11|p|2025|daily,tempo|road|110|240|34|24|DNA Flash v2|sEVA|none|balanced|neutral|n|m
Brooks|Launch 10|p|2023|daily,tempo|road|110|235|30|20|DNA Flash|EVA|none|firm|neutral|n|h
Brooks|Hyperion 3|c|2025|tempo,race|road|150|200|33|25|DNA Flash v2|sEVA|none|bouncy|neutral|n|m
Brooks|Hyperion Max 4|c|2026|tempo,long|road|200|240|40|32|DNA Flash v2|sEVA|nylon|bouncy|neutral|n|m
Brooks|Hyperion Max 3|p|2025|tempo,long|road|190|240|40|32|DNA Flash v2|sEVA|nylon|bouncy|neutral|n|m
Brooks|Hyperion Elite 6|c|2026|race|road|275|200|40|32|DNA Gold|PEBA|carbon|bouncy|neutral|n|l
Brooks|Hyperion Elite 5|p|2025|race|road|250|210|40|32|DNA Gold|PEBA|carbon|bouncy|neutral|n|m
Brooks|Hyperion Elite 4|p|2024|race|road|250|210|40|32|DNA Gold|PEBA|carbon|bouncy|neutral|n|h
Brooks|Hyperion GTS 2|c|2025|stab,tempo|road|150|240|35|27|DNA Flash v2|sEVA|none|balanced|stable|n|l
Brooks|Revel 9|c|2026|daily,budget|road|100|265|32|23|DNA Loft v2|EVA|none|balanced|neutral|n|l
Brooks|Revel 7|p|2024|daily,budget|road|100|265|32|23|DNA Loft v2|EVA|none|balanced|neutral|n|l
Brooks|Trace 3|c|2024|daily,budget|road|100|275|33|21|DNA Loft v2|EVA|none|soft|neutral|n|l
Brooks|Beast GTS 26|c|2026|stab,daily|road|170|330|38|26|DNA Loft v3|sEVA|none|soft|stable|y|l
Brooks|Beast GTS 24|p|2024|stab,daily|road|160|340|37|25|DNA Loft v3|sEVA|none|soft|stable|y|m
Brooks|Caldera 8|c|2025|trail,long|trail|150|300|38|32|DNA Loft v3|sEVA|none|soft|neutral|n|m
Brooks|Cascadia 19|c|2025|trail|trail|140|310|33|27|DNA Loft v3|sEVA|none|balanced|neutral|y|m
Brooks|Cascadia 18|p|2024|trail|trail|140|315|31|25|DNA Loft v3|sEVA|none|balanced|neutral|y|m
Brooks|Cascadia Elite|c|2026|trail,race|trail|275|270|40|32|DNA Gold|PEBA|carbon|bouncy|neutral|n|l
Brooks|Catamount 4|c|2025|trail,tempo|trail|170|270|33|27|DNA Flash v2|sEVA|nylon|balanced|neutral|n|m
Brooks|Divide 6|c|2025|trail,budget|mixed|110|300|31|23|BioMoGo DNA|EVA|none|balanced|neutral|n|l
HOKA|Clifton 11|c|2026|daily,long,recovery|road|155|275|42|35|CMEVA|EVA|none|soft|neutral|y|m
HOKA|Clifton 10|p|2025|daily,long,recovery|road|145|280|42|34|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Clifton 9|p|2023|daily|road|145|250|32|27|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Clifton 8|p|2021|daily|road|140|250|29|24|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Clifton Pro|c|2026|daily,tempo,long|road|165|265|42|35|sEVA|sEVA|none|bouncy|neutral|n|l
HOKA|Bondi 9|c|2025|long,recovery|road|175|310|43|38|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Bondi 8|p|2023|long,recovery|road|165|305|39|35|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Bondi 7|p|2021|long,recovery|road|150|310|33|29|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Mach 7|c|2026|daily,tempo|road|145|240|37|32|Supercritical EVA|sEVA|none|bouncy|neutral|n|m
HOKA|Mach 6|p|2024|daily,tempo|road|140|230|37|32|Supercritical EVA|sEVA|none|bouncy|neutral|n|h
HOKA|Mach 5|p|2022|daily,tempo|road|140|235|29|24|PROFLY|EVA|none|balanced|neutral|n|h
HOKA|Mach X 3|c|2025|tempo,long|road|205|260|47|41|PEBA + sEVA|blend|nylon|bouncy|neutral|n|m
HOKA|Mach X 2|p|2024|tempo,long|road|200|265|47|41|PEBA + sEVA|blend|nylon|bouncy|neutral|n|h
HOKA|Rincon 5|c|2026|daily,tempo,budget|road|125|220|38|33|CMEVA|EVA|none|soft|neutral|n|m
HOKA|Rincon 4|p|2024|daily,tempo,budget|road|125|215|38|33|CMEVA|EVA|none|soft|neutral|n|h
HOKA|Arahi 8|c|2025|stab,daily|road|150|275|37|32|CMEVA|EVA|none|balanced|stable|y|h
HOKA|Arahi 7|p|2024|stab,daily|road|145|280|37|32|CMEVA|EVA|none|balanced|stable|y|h
HOKA|Arahi 6|p|2022|stab,daily|road|140|265|33|28|CMEVA|EVA|none|firm|stable|y|h
HOKA|Gaviota 6|c|2026|stab,long|road|180|305|42|37|CMEVA|EVA|none|soft|stable|y|m
HOKA|Gaviota 5|p|2023|stab,long|road|175|310|40|34|CMEVA|EVA|none|soft|stable|y|h
HOKA|Skyflow|c|2024|daily,long|road|160|275|40|35|sEVA|sEVA|none|soft|neutral|y|m
HOKA|Skyward X 2|c|2026|long,recovery|road|225|310|48|43|PEBA + sEVA|blend|carbon|bouncy|neutral|n|l
HOKA|Skyward X|p|2024|long,recovery|road|225|320|48|43|PEBA + sEVA|blend|carbon|bouncy|neutral|n|h
HOKA|Cielo X1 3.0|c|2026|race|road|275|200|48|41|PEBA|PEBA|carbon|bouncy|neutral|n|m
HOKA|Cielo X1 2.0|p|2024|race|road|275|240|48|41|PEBA|PEBA|carbon|bouncy|neutral|n|m
HOKA|Rocket X 3|c|2025|race|road|250|190|40|33|PEBA|PEBA|carbon|bouncy|neutral|n|m
HOKA|Rocket X 2|p|2023|race|road|250|220|36|31|PEBA|PEBA|carbon|bouncy|neutral|n|h
HOKA|Transport|c|2024|daily,budget|road|150|300|31|26|CMEVA|EVA|none|firm|neutral|n|l
HOKA|Solimar|c|2023|daily,budget|road|135|240|29|24|CMEVA|EVA|none|balanced|neutral|n|l
HOKA|Kawana 2|c|2023|daily|road|150|290|33|28|CMEVA|EVA|none|balanced|neutral|n|l
HOKA|Speedgoat 7|c|2026|trail,long|trail|165|290|40|35|CMEVA|EVA|none|soft|neutral|y|m
HOKA|Speedgoat 6|p|2024|trail,long|trail|155|270|40|35|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Speedgoat 5|p|2022|trail,long|trail|155|290|33|29|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Torrent 5|c|2026|trail,tempo|trail|130|270|33|28|PROFLY|EVA|none|balanced|neutral|n|l
HOKA|Torrent 4|p|2025|trail,tempo|trail|130|270|31|26|PROFLY|EVA|none|balanced|neutral|n|m
HOKA|Zinal 3|c|2026|trail,tempo|trail|150|250|35|30|PROFLY|EVA|none|balanced|neutral|n|l
HOKA|Zinal 2|p|2024|trail,tempo|trail|150|250|33|28|PROFLY|EVA|none|balanced|neutral|n|m
HOKA|Challenger 8|c|2025|trail,daily|mixed|150|280|38|33|CMEVA|EVA|none|soft|neutral|y|m
HOKA|Challenger 7|p|2023|trail,daily|mixed|145|275|31|26|CMEVA|EVA|none|soft|neutral|y|h
HOKA|Mafate Speed 4|c|2022|trail,long|trail|175|310|39|35|PROFLY X|EVA|none|balanced|neutral|n|m
HOKA|Mafate X|c|2024|trail,race|trail|275|300|40|35|PEBA|PEBA|carbon|bouncy|neutral|n|m
HOKA|Tecton X 3|c|2025|trail,race|trail|225|260|40|35|PEBA|PEBA|carbon|bouncy|neutral|n|m
HOKA|Tecton X 2|p|2023|trail,race|trail|225|270|33|28|PEBA|PEBA|carbon|bouncy|neutral|n|m
HOKA|Rocket X Trail|c|2025|trail,race|trail|250|256|45|39|A-TPU|TPU|carbon|bouncy|neutral|n|m
HOKA|Stinson 7|c|2023|trail,long|trail|175|330|44|39|CMEVA|EVA|none|soft|neutral|n|m
New Balance|Fresh Foam X 1080v15|c|2026|daily,long,recovery|road|170|290|38|32|Fresh Foam X|EVA|none|soft|neutral|y|m
New Balance|Fresh Foam X 1080v14|p|2024|daily,long,recovery|road|165|285|38|32|Fresh Foam X|EVA|none|soft|neutral|y|h
New Balance|Fresh Foam X 1080v13|p|2023|daily,long|road|165|280|38|32|Fresh Foam X|EVA|none|soft|neutral|y|h
New Balance|Fresh Foam X 1080v12|p|2022|daily,long|road|160|275|32|26|Fresh Foam X|EVA|none|soft|neutral|y|h
New Balance|FuelCell Rebel v5|c|2025|daily,tempo|road|140|210|35|29|FuelCell|blend|none|bouncy|neutral|n|h
New Balance|FuelCell Rebel v4|p|2024|daily,tempo|road|140|215|35|29|FuelCell|blend|none|bouncy|neutral|n|h
New Balance|FuelCell Rebel v3|p|2022|daily,tempo|road|130|215|30|24|FuelCell|EVA|none|bouncy|neutral|n|h
New Balance|FuelCell Rebel Trail|c|2026|trail,tempo|mixed|150|245|35|29|FuelCell|blend|none|bouncy|neutral|n|l
New Balance|FuelCell SuperComp Elite v6|c|2026|race|road|275|187|39|30|FuelCell|PEBA|carbon|bouncy|neutral|n|h
New Balance|FuelCell SuperComp Elite v5|p|2025|race|road|250|210|40|36|FuelCell|PEBA|carbon|bouncy|neutral|n|m
New Balance|FuelCell SuperComp Elite v4|p|2024|race|road|250|220|40|36|FuelCell|PEBA|carbon|bouncy|neutral|n|h
New Balance|FuelCell SuperComp Trainer v3|c|2025|tempo,long|road|200|280|40|34|FuelCell|PEBA|carbon|bouncy|neutral|n|m
New Balance|FuelCell SuperComp Pacer v2|c|2024|race|road|200|180|30|26|FuelCell|PEBA|carbon|bouncy|neutral|n|m
New Balance|FuelCell Propel v5|c|2024|daily,budget|road|110|270|32|28|FuelCell|EVA|none|bouncy|neutral|n|m
New Balance|Fresh Foam X 880v15|c|2025|daily|road|140|295|36|26|Fresh Foam X|EVA|none|balanced|neutral|y|m
New Balance|Fresh Foam X 880v14|p|2024|daily|road|140|295|36|26|Fresh Foam X|EVA|none|balanced|neutral|y|h
New Balance|Fresh Foam X 880v13|p|2023|daily|road|135|300|32|22|Fresh Foam X|EVA|none|balanced|neutral|y|h
New Balance|Fresh Foam X 860v15|c|2026|stab,daily|road|150|300|37|31|Fresh Foam X|EVA|none|balanced|stable|y|m
New Balance|Fresh Foam X 860v14|p|2024|stab,daily|road|145|300|35|29|Fresh Foam X|EVA|none|balanced|stable|y|h
New Balance|Fresh Foam X Vongo v6|c|2024|stab,long|road|165|300|38|32|Fresh Foam X|EVA|none|soft|stable|y|m
New Balance|Fresh Foam X More v5|c|2024|long,recovery|road|165|310|40|36|Fresh Foam X|EVA|none|soft|neutral|y|m
New Balance|Fresh Foam X Balos|c|2025|long,recovery|road|180|300|43|42|Fresh Foam X|EVA|none|soft|neutral|n|m
New Balance|Ellipse|c|2026|daily,long,recovery|road|145|290|40|32|Fresh Foam X|EVA|none|soft|neutral|n|l
New Balance|Fresh Foam 680v8|c|2024|daily,budget|road|90|290|30|20|Fresh Foam|EVA|none|firm|neutral|y|l
New Balance|Fresh Foam Arishi v4|c|2023|daily,budget|road|75|270|28|18|Fresh Foam|EVA|none|firm|neutral|n|l
New Balance|520v9|c|2025|daily,budget|road|70|270|28|18|EVA|EVA|none|firm|neutral|n|l
New Balance|FuelCell SuperComp Trail v2|c|2026|trail,race|trail|220|280|40|34|FuelCell|PEBA|carbon|bouncy|neutral|n|l
New Balance|Fresh Foam X Hierro v9|c|2025|trail,long|trail|150|320|35|27|Fresh Foam X|EVA|none|soft|neutral|y|m
New Balance|Fresh Foam X More Trail v3|c|2023|trail,long|trail|155|320|40|36|Fresh Foam X|EVA|none|soft|neutral|n|m
New Balance|FuelCell Summit Unknown v4|c|2023|trail,tempo|trail|140|280|32|26|FuelCell|EVA|none|balanced|neutral|n|m
New Balance|DynaSoft Nitrel v6|c|2024|trail,budget|trail|80|300|28|20|DynaSoft|EVA|none|firm|neutral|y|l
New Balance|Fresh Foam X Garoé v2|c|2024|trail,budget|trail|100|300|30|22|Fresh Foam X|EVA|none|balanced|neutral|n|l
Saucony|Ride 19|c|2026|daily|road|145|260|35|27|PWRRUN+|TPU|none|balanced|neutral|y|m
Saucony|Ride 18|p|2025|daily|road|140|265|35|27|PWRRUN+|TPU|none|balanced|neutral|y|h
Saucony|Ride 17|p|2024|daily|road|140|265|35|27|PWRRUN+|TPU|none|balanced|neutral|y|h
Saucony|Ride 16|p|2023|daily|road|140|260|32|24|PWRRUN|EVA|none|balanced|neutral|y|h
Saucony|Guide 19|c|2026|stab,daily,recovery|road|150|280|37|31|PWRRUN+|TPU|none|soft|stable|y|m
Saucony|Guide 18|p|2025|stab,daily|road|145|280|35|29|PWRRUN+|TPU|none|soft|stable|y|h
Saucony|Guide 17|p|2024|stab,daily|road|140|275|35|29|PWRRUN|EVA|none|balanced|stable|y|h
Saucony|Triumph 24|c|2026|daily,long|road|170|290|38|28|PWRRUN PB|PEBA|none|soft|neutral|y|m
Saucony|Triumph 23|p|2025|daily,long|road|170|290|38|28|PWRRUN PB|PEBA|none|soft|neutral|y|h
Saucony|Triumph 22|p|2024|daily,long|road|160|290|37|27|PWRRUN+|TPU|none|soft|neutral|y|h
Saucony|Triumph 21|p|2023|daily,long|road|160|290|37|27|PWRRUN+|TPU|none|soft|neutral|y|h
Saucony|Hurricane 26|c|2026|stab,long,recovery|road|170|260|41|34|PWRRUN PB|PEBA|none|soft|stable|y|h
Saucony|Hurricane 25|p|2025|stab,long|road|170|290|38|30|PWRRUN PB|PEBA|none|soft|stable|y|m
Saucony|Endorphin Speed 5|c|2025|tempo,long|road|170|230|36|28|PWRRUN PB|PEBA|nylon|bouncy|neutral|n|h
Saucony|Endorphin Speed 4|p|2024|tempo,long|road|170|235|36|28|PWRRUN PB|PEBA|nylon|bouncy|neutral|n|h
Saucony|Endorphin Speed 3|p|2022|tempo,long|road|170|235|36|28|PWRRUN PB|PEBA|nylon|bouncy|neutral|n|h
Saucony|Endorphin Pro 5|c|2026|race|road|240|210|40|32|PWRRUN HG + PWRRUN PB|PEBA|carbon|bouncy|neutral|n|m
Saucony|Endorphin Pro 4|p|2024|race|road|225|215|40|32|PWRRUN HG + PWRRUN PB|PEBA|carbon|bouncy|neutral|n|h
Saucony|Endorphin Pro 3|p|2022|race|road|225|225|39|31|PWRRUN PB|PEBA|carbon|bouncy|neutral|n|h
Saucony|Endorphin Elite 3|c|2026|race|road|290|190|40|32|PWRRUN HG|PEBA|carbon|bouncy|neutral|n|l
Saucony|Endorphin Elite 2|p|2025|race|road|275|190|40|32|PWRRUN HG|PEBA|carbon|bouncy|neutral|n|m
Saucony|Endorphin Azura|c|2026|daily,tempo,long|road|150|240|38|30|PWRRUN PB|PEBA|none|bouncy|neutral|n|l
Saucony|Endorphin Trainer|c|2025|daily,long|road|180|280|40|32|PWRRUN PB + PWRRUN|blend|none|bouncy|neutral|n|m
Saucony|Kinvara 15|c|2025|tempo,budget|road|120|200|31|27|PWRRUN|EVA|none|firm|neutral|n|m
Saucony|Kinvara 14|p|2023|tempo,budget|road|120|205|31|27|PWRRUN|EVA|none|firm|neutral|n|h
Saucony|Kinvara 13|p|2022|tempo,budget|road|110|205|28|24|PWRRUN|EVA|none|firm|neutral|n|h
Saucony|Tempus 2|c|2025|stab,tempo|road|160|260|36|28|PWRRUN PB|PEBA|none|balanced|stable|n|m
Saucony|Omni 23 ST|c|2026|stab|road|170|300|38|30|PWRRUN+|TPU|none|balanced|stable|y|l
Saucony|Cohesion 19|c|2026|daily,budget|road|80|285|30|20|EVA|EVA|none|firm|neutral|n|l
Saucony|Axon 3|c|2023|daily,budget|road|100|270|32|28|PWRRUN|EVA|none|balanced|neutral|n|m
Saucony|Paramount Max|c|2026|long,recovery|road|200|300|45|38|PWRRUN PB|PEBA|none|soft|neutral|n|l
Saucony|Procyon Max|c|2026|daily,long,recovery|road|120|290|40|32|PWRRUN|EVA|none|soft|neutral|n|l
Saucony|Peregrine 16|c|2026|trail|trail|150|290|29|25|PWRRUN|EVA|none|balanced|neutral|n|m
Saucony|Peregrine 15|p|2025|trail|trail|145|290|28|24|PWRRUN|EVA|none|balanced|neutral|n|m
Saucony|Xodus Ultra 4|c|2025|trail,long|trail|170|300|38|32|PWRRUN PB|PEBA|none|soft|neutral|n|m
Saucony|Endorphin Edge 2|c|2025|trail,race|trail|200|270|38|32|PWRRUN PB|PEBA|carbon|bouncy|neutral|n|m
Saucony|Endorphin Rift|c|2025|trail,long|trail|200|280|40|35|PWRRUN PB|PEBA|none|bouncy|neutral|n|l
Saucony|Ride TR2|c|2024|trail,daily|mixed|150|290|35|29|PWRRUN+|TPU|none|balanced|neutral|n|l
Saucony|Excursion TR17|c|2024|trail,budget|trail|80|300|28|20|EVA|EVA|none|firm|neutral|n|l
Mizuno|Wave Rider 30|c|2026|daily|road|150|280|38|26|Mizuno Enerzy NXT|sEVA|nylon|balanced|neutral|y|m
Mizuno|Wave Rider 29|p|2025|daily|road|145|280|38|26|Mizuno Enerzy NXT|sEVA|nylon|balanced|neutral|y|h
Mizuno|Wave Rider 28|p|2024|daily|road|140|285|37|25|Mizuno Enerzy NXT|sEVA|nylon|balanced|neutral|y|h
Mizuno|Wave Rider 27|p|2023|daily|road|140|285|35|23|Mizuno Enerzy|EVA|nylon|firm|neutral|y|h
Mizuno|Wave Inspire 22|c|2026|stab,daily|road|145|295|40|34|Mizuno Enerzy NXT|sEVA|nylon|balanced|stable|y|m
Mizuno|Wave Inspire 21|p|2025|stab,daily|road|145|295|40|32|Mizuno Enerzy NXT|sEVA|nylon|balanced|stable|y|m
Mizuno|Wave Inspire 20|p|2024|stab,daily|road|140|300|37|25|Mizuno Enerzy|EVA|nylon|firm|stable|y|h
Mizuno|Wave Sky 9|c|2025|daily,long|road|170|295|40|32|Mizuno Enerzy NXT|sEVA|nylon|soft|neutral|y|m
Mizuno|Wave Horizon 8|c|2025|stab,long|road|170|310|38|30|Mizuno Enerzy NXT|sEVA|nylon|soft|stable|y|m
Mizuno|Neo Zen 2|c|2026|daily,tempo|road|150|240|40|32|Mizuno Enerzy XP|TPEE|none|bouncy|neutral|n|m
Mizuno|Neo Zen|p|2025|daily,tempo|road|150|245|40|32|Mizuno Enerzy XP|TPEE|none|bouncy|neutral|n|m
Mizuno|Neo Vista 3|c|2026|tempo,long|road|200|260|46|38|Mizuno Enerzy XP|TPEE|none|bouncy|neutral|n|l
Mizuno|Neo Vista 2|p|2025|tempo,long|road|190|260|46|38|Mizuno Enerzy XP|TPEE|none|bouncy|neutral|n|m
Mizuno|Hyperwarp Elite|c|2026|race|road|275|175|40|32|PEBA|PEBA|carbon|bouncy|neutral|n|l
Mizuno|Hyperwarp Pro|c|2026|tempo,race|road|250|200|40|32|PEBA|PEBA|carbon|bouncy|neutral|n|l
Mizuno|Wave Rebellion Pro 3|c|2025|race|road|250|210|39|32|Mizuno Enerzy Lite+|sEVA|carbon|bouncy|neutral|n|m
Mizuno|Wave Rebellion Flash 2|c|2024|tempo|road|170|230|35|27|Mizuno Enerzy Lite|sEVA|glassfiber|balanced|neutral|n|m
Mizuno|Wave Rebellion Sonic 2|c|2024|tempo,budget|road|140|240|33|26|Mizuno Enerzy|EVA|none|balanced|neutral|n|m
Mizuno|Wave Skyrise 5|c|2024|daily|road|140|270|37|29|Mizuno Enerzy NXT|sEVA|none|soft|neutral|n|m
Mizuno|Wave Ultima 15|c|2024|daily,budget|road|120|270|33|23|Mizuno Enerzy|EVA|nylon|balanced|neutral|n|l
Mizuno|Wave Prodigy 6|c|2024|daily,budget|road|110|290|31|21|Mizuno Enerzy|EVA|nylon|firm|neutral|n|l
Mizuno|Wave Equate 9|c|2025|daily,budget|road|100|280|31|21|Mizuno Enerzy|EVA|nylon|firm|neutral|n|l
Mizuno|Wave Daichi 8|c|2023|trail|trail|150|300|33|25|Mizuno Enerzy|EVA|nylon|balanced|neutral|n|m
Mizuno|Wave Mujin 10|c|2024|trail,long|trail|170|320|33|24|Mizuno Enerzy|EVA|nylon|balanced|neutral|n|m
Mizuno|Wave Ibuki 4|c|2023|trail,budget|trail|110|300|30|20|Mizuno Enerzy|EVA|nylon|firm|neutral|n|l
Mizuno|Wave Rider TT 2|c|2024|trail,daily|mixed|140|290|33|23|Mizuno Enerzy|EVA|nylon|balanced|neutral|n|l
PUMA|Velocity Nitro 5|c|2026|daily|road|130|265|37|27|Nitro|sEVA|none|balanced|neutral|n|m
PUMA|Velocity Nitro 4|p|2025|daily|road|130|265|36|26|Nitro|sEVA|none|balanced|neutral|n|m
PUMA|Velocity Nitro 3|p|2024|daily|road|130|265|34|24|Nitro|sEVA|none|balanced|neutral|n|h
PUMA|Velocity Nitro 2|p|2022|daily|road|120|260|33|23|Nitro|sEVA|none|balanced|neutral|n|h
PUMA|Deviate Nitro 4|c|2026|tempo,long|road|170|260|40|30|Nitro + Nitro Elite|blend|carbon|bouncy|neutral|n|m
PUMA|Deviate Nitro 3|p|2024|tempo,long|road|160|265|40|30|Nitro + Nitro Elite|blend|carbon|bouncy|neutral|n|h
PUMA|Deviate Nitro 2|p|2022|tempo,long|road|160|270|36|28|Nitro|sEVA|carbon|balanced|neutral|n|h
PUMA|Deviate Nitro Elite 4|c|2026|race|road|250|190|40|32|Nitro Elite|PEBA|carbon|bouncy|neutral|n|m
PUMA|Deviate Nitro Elite 3|p|2024|race|road|230|200|40|32|Nitro Elite|PEBA|carbon|bouncy|neutral|n|m
PUMA|Deviate Nitro Elite 2|p|2022|race|road|200|210|36|28|Nitro Elite|PEBA|carbon|bouncy|neutral|n|h
PUMA|Deviate Pure Nitro|c|2026|tempo,race|road|150|210|36|28|Nitro Elite|PEBA|none|bouncy|neutral|n|l
PUMA|Fast-R Nitro Elite 3|c|2025|race|road|300|180|40|32|Nitro Elite|PEBA|carbon|bouncy|neutral|n|m
PUMA|Fast-FWD Nitro Elite 2|c|2026|race,tempo|road|200|200|40|32|Nitro Elite|PEBA|carbon|bouncy|neutral|n|l
PUMA|MagMax Nitro|c|2024|long,recovery|road|160|310|45|35|Nitro|sEVA|none|soft|neutral|n|m
PUMA|ForeverRun Nitro 3|c|2026|stab,daily|road|150|280|40|30|Nitro|sEVA|none|balanced|stable|n|l
PUMA|ForeverRun Nitro 2|p|2025|stab,daily|road|150|285|38|28|Nitro|sEVA|none|balanced|stable|n|m
PUMA|Electrify Nitro 4|c|2025|daily,budget|road|100|260|33|25|Nitro|sEVA|none|balanced|neutral|n|m
PUMA|Electrify Nitro 3|p|2023|daily,budget|road|100|260|32|24|Nitro|sEVA|none|balanced|neutral|n|m
PUMA|Darter Pro|c|2024|daily,budget|road|70|260|30|22|SoftFoam|EVA|none|firm|neutral|n|l
PUMA|Scend Pro 2|c|2024|daily,budget|road|80|280|31|21|ProFoam|EVA|none|firm|neutral|n|l
PUMA|Skyrocket Lite|c|2024|daily,budget|road|65|240|28|20|ProFoam Lite|EVA|none|firm|neutral|n|l
PUMA|Velocity Nitro Trail|c|2026|trail,daily|mixed|150|300|37|29|Nitro|sEVA|none|balanced|neutral|n|l
PUMA|Fast-Trac Nitro 3|c|2024|trail|trail|150|290|32|26|Nitro|sEVA|none|balanced|neutral|n|m
PUMA|Voyage Nitro 3|c|2023|trail|trail|130|300|30|24|Nitro|sEVA|none|balanced|neutral|n|m
On|Cloudmonster 3|c|2026|daily,long,recovery|road|190|275|38|32|Helion HF|sEVA|none|bouncy|neutral|n|m
On|Cloudmonster 2|p|2024|daily,long|road|180|290|36|30|Helion|sEVA|none|bouncy|neutral|n|h
On|Cloudmonster|p|2022|daily,long|road|170|275|30|24|Helion|sEVA|none|bouncy|neutral|n|h
On|Cloudmonster Hyper 3 Lightspray|c|2026|tempo,long|road|280|240|40|34|Helion HF|PEBA|none|bouncy|neutral|n|l
On|Cloudmonster Hyper|p|2024|tempo,long|road|220|255|39|33|Helion HF|PEBA|none|bouncy|neutral|n|m
On|Cloudsurfer 2|c|2025|daily|road|160|245|33|25|Helion|sEVA|none|soft|neutral|n|m
On|Cloudsurfer|p|2023|daily|road|160|245|32|23|Helion|sEVA|none|soft|neutral|n|h
On|Cloudsurfer Max|c|2025|daily,long|road|180|275|40|34|Helion|sEVA|none|soft|neutral|n|l
On|Cloudsurfer Next|c|2024|daily,budget|road|140|245|31|23|Helion|sEVA|none|balanced|neutral|n|l
On|Cloudflow 5|c|2025|tempo,daily|road|160|245|35|29|Helion HF|sEVA|nylon|balanced|neutral|n|m
On|Cloudflow 4|p|2023|tempo,daily|road|160|240|31|25|Helion|sEVA|nylon|firm|neutral|n|h
On|Cloudrunner 2|c|2024|stab,daily|road|150|275|35|25|Helion|sEVA|nylon|firm|stable|y|h
On|Cloudstratus 3|c|2023|long|road|180|295|36|30|Helion|sEVA|nylon|balanced|neutral|n|m
On|Cloudeclipse|c|2024|long,recovery|road|200|285|40|34|Helion HF|sEVA|none|soft|neutral|n|m
On|Cloudflyer 5|c|2025|stab|road|180|300|40|31|Helion|sEVA|nylon|balanced|stable|n|l
On|Cloudboom Echo 4|c|2025|race|road|300|210|40|33|Helion HF|PEBA|carbon|bouncy|neutral|n|m
On|Cloudboom Echo 3|p|2023|race|road|270|225|40|31|Helion HF|PEBA|carbon|bouncy|neutral|n|h
On|Cloudboom Strike|c|2025|race|road|300|200|40|32|Helion HF|PEBA|carbon|bouncy|neutral|n|m
On|Cloudboom Volt|c|2026|race|road|200|210|39|32|Helion HF|PEBA|carbon|bouncy|neutral|n|l
On|Cloudboom Max|c|2025|tempo,long|road|240|240|40|35|Helion HF|PEBA|carbon|bouncy|neutral|n|l
On|Cloud 6|c|2024|daily,budget|road|150|245|25|22|Helion|sEVA|none|firm|neutral|n|l
On|Cloudvista 2|c|2024|trail,daily|mixed|170|300|35|26|Helion|sEVA|nylon|balanced|neutral|n|m
On|Cloudultra 2|c|2023|trail,long|trail|180|300|35|29|Helion|sEVA|nylon|balanced|neutral|n|m
On|Cloudultra Pro|c|2025|trail,long|trail|230|263|39|33|Helion HF|sEVA|nylon|balanced|neutral|n|m
On|Cloudsoma|c|2026|trail,daily|mixed|180|280|36|30|Helion|sEVA|none|balanced|neutral|n|l
Altra|Torin 9|c|2026|daily,long|road|160|265|30|30|Altra EGO Max|EVA|none|soft|neutral|y|m
Altra|Torin 8|p|2025|daily,long|road|150|265|30|30|Altra EGO Max|EVA|none|soft|neutral|y|h
Altra|Torin 7|p|2023|daily,long|road|150|270|28|28|Altra EGO Max|EVA|none|soft|neutral|y|h
Altra|Torin 6|p|2022|daily,long|road|140|265|28|28|Altra EGO|EVA|none|balanced|neutral|y|h
Altra|Torin ST|c|2026|stab,daily|road|160|275|30|30|Altra EGO Max|EVA|none|soft|stable|y|l
Altra|Escalante 5|c|2026|daily,tempo|road|130|235|24|24|Altra EGO|EVA|none|balanced|neutral|y|m
Altra|Escalante 4|p|2024|daily,tempo|road|130|235|24|24|Altra EGO|EVA|none|balanced|neutral|y|m
Altra|Experience Flow 3|c|2026|daily|road|145|250|33|29|Altra EGO Max|EVA|none|balanced|neutral|y|m
Altra|Paradigm 8|c|2024|stab,long|road|170|290|30|30|Altra EGO Max|EVA|none|soft|stable|y|m
Altra|Via Olympus 2|c|2023|long|road|170|300|33|33|Altra EGO Max|EVA|none|soft|neutral|y|m
Altra|FWD Via|c|2024|daily,long|road|160|275|37|33|Altra EGO Max|EVA|none|soft|neutral|y|l
Altra|Rivera 4|c|2024|daily,budget|road|130|245|26|26|Altra EGO|EVA|none|balanced|neutral|y|l
Altra|Lone Peak 9|c|2025|trail|trail|155|300|25|25|Altra EGO|EVA|none|firm|neutral|y|m
Altra|Lone Peak 8|p|2024|trail|trail|150|305|25|25|Altra EGO|EVA|none|firm|neutral|y|h
Altra|Lone Peak 7|p|2023|trail|trail|150|300|25|25|Altra EGO|EVA|none|firm|neutral|y|h
Altra|Timp 6|c|2026|trail,long|trail|165|300|29|29|Altra EGO Max|EVA|none|balanced|neutral|y|m
Altra|Timp 5|p|2024|trail,long|trail|160|300|29|29|Altra EGO Max|EVA|none|balanced|neutral|y|m
Altra|Olympus 6|c|2024|trail,long|trail|180|320|33|33|Altra EGO Max|EVA|none|soft|neutral|y|m
Altra|Olympus 275 HiLo|c|2026|trail,long|trail|200|300|35|30|Altra EGO Max|EVA|none|soft|neutral|y|l
Altra|Mont Blanc Carbon|c|2024|trail,race|trail|250|270|30|30|Altra EGO Pro|PEBA|carbon|bouncy|neutral|y|m
Altra|Experience Wild 3|c|2026|trail,daily|mixed|155|285|32|28|Altra EGO Max|EVA|none|balanced|neutral|y|l
Altra|Superior 7|c|2025|trail,tempo|trail|130|240|21|21|Altra EGO|EVA|none|firm|neutral|y|l
Altra|Outroad 3|c|2024|trail,daily|mixed|140|270|30|26|Altra EGO|EVA|none|balanced|neutral|y|l
Salomon|Aero Glide 4|c|2026|daily,long|road|160|265|40|30|Energy Foam|EVA|none|soft|neutral|n|m
Salomon|Aero Glide 3|p|2024|daily,long|road|150|265|38|28|Energy Foam|EVA|none|soft|neutral|n|m
Salomon|Aero Glide 4 GRVL|c|2026|daily,trail,long|mixed|160|275|40|30|Energy Foam|EVA|none|soft|neutral|n|l
Salomon|Aero Blaze 2|c|2023|tempo|road|140|230|36|28|Energy Foam|EVA|none|bouncy|neutral|n|m
Salomon|Aero Volt 2|c|2024|daily|road|130|260|33|25|Energy Foam|EVA|none|balanced|neutral|n|l
Salomon|S/Lab Phantasm 2|c|2024|race|road|275|200|38|30|Energy Surge|PEBA|carbon|bouncy|neutral|n|m
Salomon|Speedcross 6|c|2023|trail|trail|140|315|30|20|EVA|EVA|none|firm|neutral|y|m
Salomon|Speedcross 5|p|2020|trail|trail|130|330|30|20|EVA|EVA|none|firm|neutral|y|h
Salomon|Sense Ride 5|c|2022|trail,daily|trail|140|290|31|23|Optivibe|EVA|none|balanced|neutral|n|m
Salomon|Ultra Glide 3|c|2025|trail,long|trail|160|300|38|32|Energy Foam|EVA|none|soft|neutral|n|m
Salomon|Genesis|c|2024|trail,long|trail|150|285|35|27|Energy Foam|EVA|none|balanced|neutral|n|m
Salomon|S/Lab Genesis|c|2024|trail,race|trail|200|260|33|27|Energy Surge|PEBA|none|bouncy|neutral|n|m
Salomon|Pulsar Trail 2|c|2024|trail,tempo|trail|140|250|31|25|Energy Surge|PEBA|none|bouncy|neutral|n|m
Salomon|S/Lab Ultra Glide|c|2024|trail,race|trail|210|260|39|33|Energy Surge|PEBA|none|bouncy|neutral|n|l
Salomon|Thundercross|c|2023|trail|trail|130|300|32|24|Energy Foam|EVA|none|firm|neutral|n|m
Under Armour|Infinite Elite 2|c|2025|daily,long|road|160|275|40|32|HOVR+|blend|none|soft|neutral|n|m
Under Armour|Infinite Pro|c|2024|daily|road|160|285|35|27|HOVR+|blend|none|balanced|neutral|n|m
Under Armour|Infinite 6|c|2024|daily,budget|road|140|280|33|25|Charged Cushioning|EVA|none|balanced|neutral|n|l
Under Armour|Velociti Elite 3|c|2025|race|road|250|210|40|32|PEBA|PEBA|carbon|bouncy|neutral|n|m
Under Armour|Velociti 4|c|2024|tempo|road|140|240|35|27|Flow|EVA|none|balanced|neutral|n|l
Under Armour|Charged Pursuit 3|c|2024|daily,budget|road|75|280|28|18|Charged Cushioning|EVA|none|firm|neutral|n|l
Skechers|Aero Razor|c|2026|daily,tempo|road|140|210|33|27|Hyper Burst Pro|sEVA|none|bouncy|neutral|n|l
Skechers|Aero Burst|c|2025|daily|road|130|250|36|30|Hyper Burst Pro|sEVA|none|bouncy|neutral|n|l
Skechers|Aero Spark|c|2025|tempo|road|170|230|38|30|Hyper Burst Pro|sEVA|carbon|bouncy|neutral|n|l
Skechers|Max Road 7|c|2024|long|road|130|280|40|34|Hyper Burst|sEVA|none|soft|neutral|n|l
Skechers|Speed Freek|c|2024|race|road|250|190|40|32|Hyper Burst Ice|PEBA|carbon|bouncy|neutral|n|l
Skechers|GOrun Consistent 2|c|2024|daily,budget|road|70|260|30|24|ULTRA GO|EVA|none|soft|neutral|y|l
Diadora|Mythos Blushield Vigore V|c|2026|daily,tempo|road|180|270|36|28|Diadora Energy|sEVA|none|balanced|neutral|n|l
Diadora|Atomo V7000|c|2024|daily|road|170|300|36|28|Atomo|EVA|none|balanced|neutral|n|l
Topo Athletic|Specter 3|c|2026|daily,long|road|170|270|39|34|A-TPU|TPU|none|bouncy|neutral|y|m
Topo Athletic|Ultrafly 5|c|2025|stab,daily|road|150|270|33|28|ZipFoam|EVA|none|balanced|stable|y|m
Topo Athletic|Phantom 3|c|2023|daily,long|road|150|280|35|30|ZipFoam|EVA|none|soft|neutral|y|m
Topo Athletic|Cyclone 3|c|2024|tempo|road|150|220|30|25|Pebax|PEBA|none|bouncy|neutral|y|m
Topo Athletic|Atmos|c|2024|long|road|160|290|38|33|ZipFoam|EVA|none|soft|neutral|y|m
Topo Athletic|Ultraventure 4|c|2025|trail,long|trail|150|290|35|30|ZipFoam|EVA|none|soft|neutral|y|m
Topo Athletic|MTN Racer 4|c|2025|trail,long|trail|160|285|33|28|ZipFoam|EVA|none|balanced|neutral|y|m
Topo Athletic|Traverse|c|2023|trail|trail|130|300|33|28|ZipFoam|EVA|none|balanced|neutral|y|l
Merrell|Agility Peak 6|c|2026|trail,long|trail|160|300|33|27|FloatPro|EVA|none|balanced|neutral|n|l
Merrell|MTL Long Sky 2|c|2023|trail|trail|150|260|25|19|FloatPro|EVA|none|firm|neutral|n|m
La Sportiva|Prodigio 2|c|2026|trail,long|trail|170|260|35|28|DTS|EVA|none|bouncy|neutral|n|l
La Sportiva|Bushido III|c|2023|trail|trail|160|300|25|19|EVA|EVA|none|firm|neutral|n|m
La Sportiva|Jackal II|c|2023|trail,long|trail|160|290|30|23|Infinitoo|TPU|none|balanced|neutral|n|m
La Sportiva|Akasha II|c|2023|trail,long|trail|160|310|28|22|EVA|EVA|none|balanced|neutral|n|m
inov-8|Trailfly G 270 v2|c|2023|trail|trail|160|280|25|21|PowerFlow Max|EVA|none|balanced|neutral|n|l
inov-8|Roclite Ultra G 320|c|2024|trail,long|trail|190|320|30|24|PowerFlow Max|EVA|none|balanced|neutral|n|l
inov-8|Mudtalon|c|2023|trail|trail|150|290|17|11|PowerFlow|EVA|none|firm|neutral|n|l
Craft|Pro Endur Distance|c|2024|daily,long|road|170|270|38|31|UD Foam|sEVA|none|bouncy|neutral|n|l
Craft|Nordlite Ultra|c|2023|trail,long|trail|160|300|38|32|UD Foam|sEVA|none|soft|neutral|n|l
Karhu|Ikoni 3.0|c|2024|daily|road|150|280|35|27|Aero Foam|EVA|none|balanced|neutral|n|l
Kiprun|KD900X LD 2|c|2025|race|road|220|220|39|31|Vfoam+|PEBA|carbon|bouncy|neutral|n|m
Kiprun|KD800 2|c|2024|tempo|road|130|230|36|28|Kalensole|sEVA|nylon|balanced|neutral|n|l
Kiprun|KS900 Light 2|c|2024|daily|road|130|270|35|27|Kalensole|sEVA|none|soft|neutral|n|l
Kiprun|KS500 3|c|2024|daily,budget|road|80|300|33|23|Kalensole|EVA|none|balanced|neutral|n|l
Kiprun|Jogflow 500.1|c|2024|daily,budget|road|50|260|30|22|Kalensole|EVA|none|balanced|neutral|n|l
Kiprun|Jogflow 190.1|c|2024|daily,budget|road|30|250|26|18|EVA|EVA|none|firm|neutral|n|l
Kiprun|MT Cushion 2|c|2024|trail,long|trail|110|310|33|27|Kalensole|EVA|none|soft|neutral|n|l
Kiprun|XT8|c|2023|trail|trail|90|310|30|22|EVA|EVA|none|firm|neutral|n|l
Olympikus|Corre 4|c|2025|daily,tempo|road|90|250|36|28|EVA supercrítico|sEVA|none|bouncy|neutral|n|l
Olympikus|Corre 3|p|2024|daily,tempo|road|80|250|34|26|EVA supercrítico|sEVA|none|bouncy|neutral|n|l
Olympikus|Corre Supra 2|c|2025|race|road|200|200|39|32|PEBA|PEBA|carbon|bouncy|neutral|n|l
"""
