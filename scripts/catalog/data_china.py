# Chinese brands. Names romanized as commonly used in international reviews; MSRP converted from RMB.
ROWS = """
Li-Ning|Red Hare 9 Ultra|c|2026|daily,long|road|130|246|47|42|BOOM|PEBA|none|bouncy|neutral|n|m
Li-Ning|Red Hare 9 Pro|c|2026|tempo|road|100|220|38|32|BOOM|PEBA|nylon|bouncy|neutral|n|l
Li-Ning|Red Hare 8 Pro|p|2025|tempo|road|95|215|36|30|BOOM|PEBA|nylon|bouncy|neutral|n|l
Li-Ning|Red Hare 8|p|2025|daily,tempo,budget|road|60|230|33|26|Light Foam Plus|sEVA|none|balanced|neutral|n|l
Li-Ning|Red Hare 7 Pro|p|2024|tempo|road|85|210|35|29|BOOM|PEBA|nylon|bouncy|neutral|n|l
Li-Ning|Red Hare 7|p|2024|daily,tempo,budget|road|55|230|32|25|Light Foam Plus|sEVA|none|balanced|neutral|n|l
Li-Ning|Feidian 5 Elite|c|2025|race|road|180|175|39|33|BOOM|PEBA|carbon|bouncy|neutral|n|l
Li-Ning|Feidian 4 Elite|p|2024|race|road|170|180|39|33|BOOM|PEBA|carbon|bouncy|neutral|n|l
Li-Ning|Feidian 3 Elite|p|2023|race|road|160|190|39|32|BOOM|PEBA|carbon|bouncy|neutral|n|l
Li-Ning|Feidian 4 Challenger|c|2024|tempo,race|road|110|200|38|32|BOOM|PEBA|carbon|bouncy|neutral|n|l
Li-Ning|Jueying 5|c|2025|daily,long|road|110|270|40|32|BOOM + Light Foam|blend|none|soft|neutral|n|l
Li-Ning|Jueying 4|p|2024|daily,long|road|100|270|38|30|BOOM + Light Foam|blend|none|soft|neutral|n|l
Li-Ning|Yueying 5|c|2025|daily|road|80|260|38|30|Light Foam Plus|sEVA|none|soft|neutral|n|l
Li-Ning|Yueying 4|p|2024|daily|road|75|260|36|28|Light Foam Plus|sEVA|none|soft|neutral|n|l
Li-Ning|Super Light 22|c|2025|daily,tempo|road|75|200|33|25|BOOM|PEBA|none|bouncy|neutral|n|l
Li-Ning|Super Light 21|p|2024|daily,tempo|road|70|205|32|24|BOOM|PEBA|none|bouncy|neutral|n|l
ANTA|Zone2 90%|c|2026|daily,long|road|101|188|40|34|Nitrogen PEBA|PEBA|none|bouncy|neutral|n|m
ANTA|C202 G9|c|2026|race|road|180|185|40|34|Nitrogen PEBA|PEBA|carbon|bouncy|neutral|n|l
ANTA|C202 5 GT|p|2024|race|road|170|195|40|33|Nitrogen PEBA|PEBA|carbon|bouncy|neutral|n|l
ANTA|C10 Pro|c|2025|tempo,race|road|130|200|38|31|Nitrogen Foam|sEVA|carbon|bouncy|neutral|n|l
ANTA|Mach 5|c|2025|daily,tempo,budget|road|60|230|33|25|Nitrogen Foam|sEVA|none|bouncy|neutral|n|l
ANTA|Mach 4|p|2024|daily,tempo,budget|road|55|230|32|24|Nitrogen Foam|sEVA|none|bouncy|neutral|n|l
ANTA|PG7 2|c|2025|daily,long,budget|road|60|260|36|28|PG7 Foam|EVA|none|soft|neutral|n|l
ANTA|PG7|p|2024|daily,long,budget|road|55|260|35|27|PG7 Foam|EVA|none|soft|neutral|n|l
Xtep|2000km 5 Pro|c|2026|daily,long,budget|road|58|260|38|30|Dynamic Foam|sEVA|none|balanced|neutral|n|m
Xtep|2000km 4|p|2025|daily,budget|road|50|270|35|27|Dynamic Foam|sEVA|none|balanced|neutral|n|l
Xtep|160X 7.0 Pro|c|2026|race|road|200|195|40|32|XTEP ACE|PEBA|carbon|bouncy|neutral|n|l
Xtep|160X 6.0 Pro|p|2025|race|road|190|200|40|32|XTEP ACE|PEBA|carbon|bouncy|neutral|n|l
Xtep|160X 6.0|c|2025|race,tempo|road|130|210|40|32|XTEP ACE|PEBA|carbon|bouncy|neutral|n|l
Xtep|160X 5.0 Pro|p|2024|race|road|175|205|40|32|XTEP ACE|PEBA|carbon|bouncy|neutral|n|l
Xtep|160X 3.5 Pro|p|2023|race|road|160|210|39|32|XTEP ACE|PEBA|carbon|bouncy|neutral|n|l
Xtep|360X 3.0|c|2025|tempo,long|road|130|230|40|33|XTEP ACE|PEBA|glassfiber|bouncy|neutral|n|l
Xtep|260X 2.0|c|2025|tempo|road|100|220|37|30|Dynamic Foam|sEVA|nylon|balanced|neutral|n|l
Xtep|Ultra Fast 5|c|2025|daily,budget|road|50|230|32|24|Dynamic Foam|sEVA|none|balanced|neutral|n|l
361°|Furious Future 3|c|2025|race|road|190|190|39|33|QU!K Flame PEBA|PEBA|carbon|bouncy|neutral|n|l
361°|Furious Future 2|p|2024|race|road|180|195|39|33|QU!K Flame PEBA|PEBA|carbon|bouncy|neutral|n|l
361°|Flame 5|c|2025|race,tempo|road|150|200|39|33|QU!K Flame|PEBA|carbon|bouncy|neutral|n|l
361°|Flame 4|p|2024|race,tempo|road|140|205|39|33|QU!K Flame|PEBA|carbon|bouncy|neutral|n|l
361°|Spire 6|c|2025|daily|road|130|290|34|26|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|Centauri 2|c|2024|stab,daily|road|140|300|36|27|QU!KFOAM|EVA|none|balanced|stable|n|l
361°|Meraki 6|c|2024|daily|road|120|270|33|25|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|Kairos 2|c|2024|daily,long|road|150|290|38|30|QU!KFOAM|EVA|none|soft|neutral|n|l
361°|Primo 2|c|2024|daily,budget|road|110|260|32|24|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|Fierce 3|c|2024|tempo,budget|road|100|230|30|22|QU!KFOAM|EVA|none|firm|neutral|n|l
361°|Lynx|c|2025|trail|trail|150|260|32|26|QU!KFOAM|EVA|none|balanced|neutral|n|m
361°|Taiga 5|c|2024|trail|trail|130|300|33|26|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|Yushan 2|c|2024|trail,long|trail|140|310|35|29|QU!KFOAM|EVA|none|soft|neutral|n|l
PEAK|Wave|c|2026|daily,long,budget|road|70|250|38|30|P-Motive Foam|sEVA|none|soft|neutral|n|l
PEAK|Taichi 3.0|c|2024|daily,budget|road|60|260|33|25|P-Motive|TPEE|none|bouncy|neutral|n|l
Qiaodan|Feiying PB 4.0|c|2025|race|road|160|185|39|33|PEBA|PEBA|carbon|bouncy|neutral|n|l
Qiaodan|Feiying PB 3.0|p|2024|race|road|150|190|39|33|PEBA|PEBA|carbon|bouncy|neutral|n|l
Kailas|Fuga EX 3|c|2024|trail,race|trail|200|260|34|28|PEBA|PEBA|carbon|bouncy|neutral|n|l
Kailas|Fuga DU 2|c|2024|trail,long|trail|170|290|36|30|EVA|EVA|none|soft|neutral|n|l
"""

# Added 2026-10-29: more Chinese models found in reviews and on AliExpress
ROWS += """
Li-Ning|Feidian 6 Elite|c|2026|race|road|230|205|40|34|Super BOOM|PEBA|carbon|bouncy|neutral|n|m
Li-Ning|Feidian 6 Challenger|c|2025|race,tempo|road|115|200|38|31|BOOM|PEBA|carbon|bouncy|neutral|n|m
Li-Ning|Feidian 6 Ultra|c|2026|tempo,long|road|170|240|42|36|Super BOOM|PEBA|carbon|bouncy|neutral|n|l
Li-Ning|Red Hare 9|c|2026|daily,tempo,budget|road|70|235|35|27|Light Foam Plus|sEVA|none|balanced|neutral|n|l
Li-Ning|Yueying 5 Pro|c|2025|daily,long|road|95|270|40|32|Super BOOM|PEBA|none|soft|neutral|y|l
ANTA|C202 7|c|2025|race,tempo|road|180|204|40|34|Nitro Edge Pro|blend|carbon|bouncy|neutral|n|m
ANTA|C202 G9 2|c|2026|race|road|190|184|40|34|Nitroedge 90|PEBA|carbon|bouncy|neutral|n|m
ANTA|Mach 5 SE|c|2025|daily,budget|road|55|240|33|25|Nitrogen Foam|sEVA|none|balanced|neutral|n|l
ANTA|Bellero 3|c|2025|daily,long|road|90|265|38|30|Nitro Edge|sEVA|none|soft|neutral|n|l
361°|Feisu 4|c|2025|race|road|100|185|35|29|QU!KFLAME|PEBA|carbon|bouncy|neutral|n|m
361°|Eleos 2|c|2025|long,recovery|road|130|300|42|34|QU!KFOAM|EVA|none|soft|neutral|n|l
361°|Miro Nude ST|c|2025|tempo,daily|road|110|230|35|28|TPEE|TPEE|nylon|bouncy|neutral|n|l
Xtep|Qingyun 2.0|c|2025|long,recovery|road|110|312|44|36|Dynamic Foam|sEVA|none|soft|mild|n|m
Xtep|260X 3.0|c|2025|tempo|road|110|225|38|31|XTEP ACE|PEBA|glassfiber|bouncy|neutral|n|l
Xtep|360X 2.0|p|2024|tempo,long|road|120|235|40|33|XTEP ACE|PEBA|glassfiber|bouncy|neutral|n|l
Qiaodan|Feiying Plaid 3.0|c|2026|race|road|270|195|40|34|Q-Kungfu Pro-HP|PEBA|carbon|bouncy|neutral|n|l
Qiaodan|Feiying Plaid 2.0|c|2025|race|road|269|206|40|34|Q-Kungfu Pro-HP|PEBA|carbon|bouncy|neutral|n|m
Qiaodan|Feiying PB 6.0|c|2026|race|road|160|181|38|32|Super Q-Kungfu|TPEE|carbon|bouncy|neutral|n|m
Qiaodan|Plaid 1.5|p|2024|race|road|100|195|38|31|Q-Kungfu Pro-HP|TPEE|carbon|bouncy|neutral|n|m
Qiaodan|Wind 4.0|c|2025|daily,long|road|110|238|37|29|PEBA|PEBA|nylon|bouncy|neutral|n|m
BMAI|Jingtan 3.0 Turbo|c|2025|race,tempo|road|150|200|39|32|PEBA|PEBA|carbon|bouncy|neutral|n|l
Do-Win|Speedster 3.0|c|2025|race|road|130|200|38|31|PEBA|PEBA|carbon|firm|neutral|n|l
Dynafish|Xiaonian|c|2025|daily,tempo|road|110|204|41|34|TPEE|TPEE|none|bouncy|neutral|n|m
"""

# Added 2026-10-29 from the AliExpress discovery report (models actually for sale there).
# Specs are estimates from each series and the listing; price is the median AliExpress price in USD.
ROWS += """
Xtep|2000km Pro|c|2026|daily,long|road|78|270|38|30|Dynamic Foam|sEVA|none|balanced|mild|n|l
Xtep|2000km 5.0|c|2025|daily,long|road|76|265|38|30|Dynamic Foam|sEVA|none|balanced|neutral|n|l
Xtep|2000km 3.0|p|2025|daily,budget|road|52|275|35|27|Dynamic Foam|sEVA|none|balanced|neutral|n|l
Xtep|2000km Plus|c|2025|daily,budget|road|52|270|35|27|Dynamic Foam|sEVA|none|balanced|neutral|n|l
Xtep|2000km 2.0|p|2024|daily,budget|road|64|280|34|26|Dynamic Foam|sEVA|none|firm|neutral|n|l
Xtep|2000km 5.5 Pro|c|2026|daily,tempo|road|79|255|38|30|Dynamic Foam|sEVA|none|bouncy|neutral|n|l
Xtep|Shyft 1.0|c|2025|tempo|road|70|240|36|28|Dynamic Foam|sEVA|none|bouncy|neutral|n|l
Xtep|Shyft Pro|c|2025|tempo,long|road|94|250|40|32|XTEP ACE|blend|none|bouncy|neutral|n|l
Xtep|Qingyun Lite|c|2025|daily|road|57|260|36|28|Dynamic Foam|sEVA|none|soft|neutral|n|l
Xtep|360X|p|2023|tempo,long|road|87|245|38|31|XTEP ACE|PEBA|carbon|bouncy|neutral|n|l
Xtep|Chase Mountain 2.0 Pro|c|2025|trail|trail|100|300|34|28|Dynamic Foam|sEVA|none|balanced|neutral|n|l
Li-Ning|Yueying 6|c|2026|daily,long,budget|road|51|265|38|30|Light Foam Plus|sEVA|none|soft|neutral|y|l
Li-Ning|Yueying 6 Pro|c|2026|daily,long|road|105|260|40|32|Super BOOM|PEBA|none|soft|neutral|y|l
Li-Ning|Feidian 5 Challenger|p|2025|race,tempo|road|100|205|38|31|BOOM|PEBA|carbon|bouncy|neutral|n|l
Li-Ning|Feidian 5 Ultra|p|2025|tempo,long|road|207|240|42|36|Super BOOM|PEBA|carbon|bouncy|neutral|n|l
Li-Ning|Chaoying|c|2025|daily|road|68|255|36|28|BOOM|PEBA|none|bouncy|neutral|n|l
Li-Ning|Chaoying Pro|c|2025|daily,tempo|road|113|245|38|30|Super BOOM|PEBA|none|bouncy|neutral|n|l
Li-Ning|Arc Pro|c|2025|daily|road|89|270|37|29|BOOM|PEBA|none|soft|neutral|n|l
Li-Ning|Shadow 4 Essential|c|2026|daily,long|road|143|265|40|32|Super BOOM|PEBA|none|bouncy|neutral|n|l
Li-Ning|Furious Rider 8 Pro|c|2025|daily,tempo|road|128|250|38|30|BOOM|PEBA|none|bouncy|neutral|n|l
Li-Ning|Ben Xiao|c|2025|trail|trail|90|310|33|27|BOOM|PEBA|none|balanced|neutral|n|l
Li-Ning|Di Lu 3|c|2026|trail,long|trail|128|295|37|31|XTRM-BOOM|PEBA|none|balanced|neutral|n|l
Li-Ning|Di Lu 2|p|2025|trail,long|trail|135|300|36|30|XTRM-BOOM|PEBA|none|balanced|neutral|n|l
Li-Ning|Longju|c|2025|trail|trail|148|330|34|28|BOOM|PEBA|none|balanced|neutral|n|l
361°|Fengye 5.0|c|2025|daily,budget|road|37|260|32|24|QU!KFOAM|EVA|none|soft|neutral|n|l
361°|PopBlaze 6|c|2026|daily,long|road|85|270|40|32|QU!KFOAM|EVA|none|soft|neutral|n|l
361°|PopBlaze 5|p|2025|daily,long|road|82|275|39|31|QU!KFOAM|EVA|none|soft|neutral|n|l
361°|AirFeather 5.0|c|2025|daily,budget|road|58|240|33|25|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|Flame 5 Future|c|2026|race|road|176|190|39|33|QU!K Flame PEBA|PEBA|carbon|bouncy|neutral|n|l
361°|Flame 4 ET|p|2025|race,tempo|road|114|205|39|33|QU!K Flame|PEBA|carbon|bouncy|neutral|n|l
361°|Flame 3.0 ET|p|2024|race,tempo|road|88|210|37|30|QU!K Flame|PEBA|carbon|bouncy|neutral|n|l
361°|Wuxia 2.0|c|2025|daily|road|81|255|36|28|QU!KFOAM|EVA|none|bouncy|neutral|n|l
361°|Feiyuan 2.0|c|2025|daily,budget|road|56|255|33|25|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|N40|c|2025|daily,budget|road|59|260|32|24|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|Steed|c|2026|tempo|road|70|235|34|27|QU!KFOAM|EVA|none|firm|neutral|n|l
361°|Swift Fox 2.0|c|2025|daily,budget|road|39|245|31|23|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|Yushan 3.0|c|2026|trail|trail|78|300|32|26|QU!KFOAM|EVA|none|balanced|neutral|n|l
361°|Yushan SE|c|2025|trail,budget|trail|54|305|31|25|QU!KFOAM|EVA|none|firm|neutral|n|l
Qiaodan|TG1.0|c|2026|race,tempo|road|75|210|38|31|Q-Kungfu|TPEE|nylon|bouncy|neutral|n|l
Qiaodan|TG2.0 Leili|c|2026|tempo,long|road|109|240|40|33|Q-Kungfu Pro|blend|none|bouncy|neutral|n|l
Qiaodan|TG2.0 Leili Max|c|2026|long,recovery|road|138|260|44|36|Q-Kungfu Pro|blend|none|soft|neutral|n|l
Qiaodan|TG2.0 SE|c|2026|tempo|road|81|235|38|31|Q-Kungfu|TPEE|none|bouncy|neutral|n|l
Qiaodan|TG Plaid|c|2026|race|road|111|205|39|32|Q-Kungfu Pro-HP|TPEE|carbon|bouncy|neutral|n|l
Qiaodan|Feiying GT|c|2026|race|road|142|200|39|32|Q-Kungfu Pro-HP|PEBA|carbon|bouncy|neutral|n|l
Qiaodan|Feiying PB 5.0|p|2025|race|road|157|190|38|32|Super Q-Kungfu|TPEE|carbon|bouncy|neutral|n|l
Qiaodan|Wind SL|c|2026|daily,tempo|road|94|225|35|28|Q-Kungfu|TPEE|nylon|bouncy|neutral|n|l
Qiaodan|Wind 3TR|c|2026|daily,long|road|80|260|38|30|Q-Kungfu|TPEE|none|soft|neutral|n|l
Qiaodan|Mountain God 3.0|c|2026|trail|trail|90|300|33|27|Q-Kungfu|TPEE|none|balanced|neutral|n|l
ANTA|Zone 2 Heart Rate 85|c|2026|daily,long|road|73|230|38|32|Nitrogen Foam|sEVA|none|bouncy|neutral|n|l
ANTA|C202 8.0|c|2026|race,tempo|road|85|200|40|34|Nitroedge|PEBA|carbon|bouncy|neutral|n|l
ANTA|C202 6.0|p|2024|race,tempo|road|86|205|39|33|Nitroedge|blend|carbon|bouncy|neutral|n|l
ONEMIX|Tupo|c|2026|race,tempo|road|60|220|38|31|Supercritical foam|sEVA|carbon|bouncy|neutral|n|l
ONEMIX|Bumper Max|c|2025|daily,long|road|71|280|40|32|EVA|EVA|none|soft|neutral|n|l
ONEMIX|Wind Wings|c|2026|tempo,budget|road|44|230|32|25|EVA|EVA|none|balanced|neutral|n|l
ONEMIX|Pace Beam|c|2026|race,tempo|road|84|220|37|30|Supercritical foam|sEVA|nylon|bouncy|neutral|n|l
ONEMIX|O-Resilio|c|2025|daily|road|75|260|36|28|EVA|EVA|none|soft|neutral|n|l
BMAI|21km|c|2025|tempo,long|road|83|240|38|30|PEBA|PEBA|carbon|bouncy|neutral|n|l
"""

# Chunta: AliExpress listings carry no model names, all sell the same carbon-plate racer (~USD 31)
ROWS += """
Chunta|Carbon|c|2026|race,tempo,budget|road|31|240|38|30|EVA|EVA|carbon|bouncy|neutral|n|l
"""
