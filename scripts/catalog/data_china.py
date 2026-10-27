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
