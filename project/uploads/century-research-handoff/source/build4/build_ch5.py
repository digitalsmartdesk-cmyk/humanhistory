from common import *

# =====================================================================
# CHAPTER 5: KNOWLEDGE AND CONNECTION
# =====================================================================
ACC, ACCD = "#c2570c", "#f4a261"

STATS = [
    ("1 in 10 → about 88%", "of adults able to read: about 1 in 10 people in 1820 (Our World in Data) and about 88% of adults now (UNESCO)"),
    ("739 million", "adults who still lack basic literacy, almost two-thirds of them women (UNESCO)"),
    ("16% → 74%", "of the world's people online, 2005 and 2025; about 6 billion users and 2.2 billion offline in 2025"),
    ("23% against 94%", "using the internet in low-income and in high-income countries in 2025 (ITU)"),
]

CH_LIT = [
    ("About 1820", "About 1 in 10 could read and write; no source named", 0, 10, True, None),
    ("About 1870", "About 1 in 5 could read; no source named", 0, 20, True, None),
    ("Youth 15–24, 2000", "UNESCO", 0, 87, False, None),
    ("Youth 15–24, latest", "UNESCO", 0, 93, False, None),
    ("Adults, latest", "About 88%, UNESCO", 0, 88, False, None),
    ("Adults, sub-Saharan Africa", "68.5%, the lowest region, UIS", 0, 68.5, False, None),
]
CH_NET = [
    ("2005", "16%", 0, 16, False, None),
    ("2010", "30%", 0, 30, False, None),
    ("2020", "60% (ITU)", 0, 60, False, None),
    ("2023", "63% (Our World in Data); another page gives 67%", 0, 63, False, None),
    ("2025", "74% (ITU)", 0, 74, False, None),
]
CH_GAP = [
    ("Africa, 2005", "2%", 0, 2, False, None),
    ("Europe, 2005", "46%", 0, 46, False, None),
    ("Africa, 2023", "37%", 0, 37, False, None),
    ("Europe, 2023", "91%", 0, 91, False, None),
    ("Low-income countries, 2025", "23% (ITU)", 0, 23, False, None),
    ("High-income countries, 2025", "94% (ITU)", 0, 94, False, None),
    ("Rural residents, 2025", "58% (ITU)", 0, 58, False, None),
    ("Urban residents, 2025", "85% (ITU)", 0, 85, False, None),
]

AREAS = [
    ("Learning to read and going to school", [
        ("1820 to now", "Literacy", "Reading becomes the norm",
         "Our World in Data says only one in ten people in the world could read and write in 1820 and one in five in 1870, and that more than four in five can now. UNESCO puts adult literacy at about 88% and youth literacy at 93%, up from 87% in 2000. At least 739 million adults still lack basic literacy, almost two-thirds of them women, with 347 million in Central and Southern Asia. Sub-Saharan Africa has the lowest regional rate, 68.5%.",
         [("Definitions", "Historical estimates often count only people who could sign documents, which the page calls a very basic lower bound. Modern figures come from a yes or no question, 'Can you read and write?', which treats literacy as all or nothing.")],
         "The 1820 and 1870 figures have no named source on the page, and its own text says both 'one in ten remain illiterate' and 'more than 4 out of 5 can read', which it does not reconcile. The UNESCO figures come from a news report of UNESCO's estimates, with no single data year given."),
        ("1820 to 2025", "Schooling", "More children in school, many still not learning",
         "Fewer than 1 in 5 adults had some basic education in 1820. Now less than 1 in 5 has none. Most children are enrolled in primary school, and girls are almost as likely as boys to be. Around 244 million children and youth were out of school in 2023 on Our World in Data's page, and a June 2025 report of UNESCO's estimate gave 272 million.",
         [("Learning", "In many lower-income countries fewer than 20% of children reach minimum reading proficiency by the end of primary school. Adults in some poorer countries average 2 to 3 years of schooling, about a decade less than in Europe or North America.")],
         "The two out-of-school figures differ and come from different reports and years. The 272 million is a news report's account, and it gave no reference year."),
    ]),
    ("Telephones, broadcasting and the internet", [
        ("1925 to 2016", "Broadcast and telephone", "Radio, telephone and television in US homes",
         "In US households radio went from 10% in 1925 to 50% in 1931 and 90% in 1947. The landline telephone took from 1903 to 1946 to reach half of homes. Colour television went from 10% in 1966 to 90% in 1985, and the internet from 10% in 1993 to a peak of 88% in 2016.",
         [("Detail", "The first chapter gives the full series and the figures for the cell phone.")],
         "From the Our World in Data household-technology chart, read from its data file. It covers the United States only, and I found no world series for these machines."),
        ("1973 to 2024", "Mobile phones", "A telephone for almost everyone",
         "The first handheld cellular call was made on 3 April 1973 with a handset weighing about 2 kilograms. The first commercial automated cellular network opened in Japan in 1979, and the first commercially available handheld phone, the DynaTAC 8000x, followed in 1983. Subscriptions passed seven billion in 2014 and reached over 9.1 billion in 2024.",
         [("Smartphones", "Smartphones were about half of mobile phone sales in 2024.")],
         "From Wikipedia. Subscriptions count connections, not people, and the page says the 2024 total is enough for one per person on Earth. It gives no figures for the 1990s or for 2000."),
        ("2005 to 2025", "Internet", "Half the world, then three-quarters, online",
         "The share of the world's people online was 16% in 2005, 30% in 2010, 60% in 2020 and 74% in 2025, about 6 billion people, with 2.2 billion still offline. The ITU puts use at 23% in low-income countries against 94% in high-income countries, and at 85% for urban residents against 58% for rural. Africa's share rose from 2% in 2005 to 37% in 2023 while Europe's went from 46% to 91%.",
         [("Quality", "5G covers an estimated 55% of the world's people, 84% in high-income countries and 4% in low-income ones. Access remains unaffordable in around 60% of low- and middle-income countries.")],
         "The 2005 to 2023 figures come from Wikipedia and the 2025 figures from a summary of the ITU's Facts and Figures 2025. Pages disagree for 2023: 63% on Our World in Data and 67% on Wikipedia."),
    ]),
]

THIN = [
    ("Basic literacy is not universal", "At least 739 million adults lack basic literacy, almost two-thirds of them women. Sub-Saharan Africa's adult rate is 68.5%.", "UNESCO, via a news report"),
    ("Being in school is not the same as learning", "In many lower-income countries fewer than 20% of children reach minimum reading proficiency by the end of primary school, and 244 to 272 million children and youth are out of school, depending on the report.", "Our World in Data; UNESCO via a news report"),
    ("Access to the internet is unequal", "In 2025 use was 23% in low-income countries against 94% in high-income countries, and 58% in rural areas against 85% in urban areas. Africa trailed Europe by 54 points in 2023.", "ITU; Wikipedia"),
    ("Being connected is not being served well", "5G covers 4% of people in low-income countries against 84% in high-income ones, and access is unaffordable in around 60% of low- and middle-income countries.", "ITU, via a summary"),
]

PATTERNS = [
    ("The reach of reading took about two centuries", "From about 1 in 10 in 1820 to about 88% of adults now. The early figures have no named source and count a very basic skill, so the starting point is soft."),
    ("The reach of the internet took about twenty years", "From 16% in 2005 to 74% in 2025. In US homes the internet took nine years to go from 10% to about half, as Chapter 2 shows."),
    ("Access and learning are different things", "Adult literacy is about 88%, yet in many lower-income countries fewer than 20% of children reach minimum reading proficiency by the end of primary school. Mobile subscriptions exceed the world's population, yet 2.2 billion people are offline."),
    ("The gaps are along income and place", "Low-income against high-income countries, rural against urban residents, Africa against Europe: in each pair the gap in 2023 or 2025 is between 27 and 71 points, on my subtraction of the figures above."),
    ("This chapter measures access, not what people do with it", "Whether wider access has made people wiser or less so is a different question, which the plan leaves to Chapter 13."),
]

LIMITS = [
    "The measures are literacy, schooling and connections. They say nothing about how much people know, how well they judge what they read, or what they use the connection for.",
    "Early literacy estimates rest on signatures and small samples, and the pages that give them name no source.",
    "Different pages give different figures for the same year: 63% or 67% online in 2023, and 244 or 272 million children out of school.",
    "Mobile subscriptions count connections, not people. I found no count of unique mobile users.",
    "Several figures come from news reports of UNESCO and ITU reports, not the reports themselves.",
    "The data do not fall on 1825 and 1925. The chapter's series start in 1820, 1925, 1973 and 2005, so the two-century split cannot be tested here.",
]

SRCS = [
    ("Reading and school", [
        ("https://ourworldindata.org/literacy", "Our World in Data, Literacy", "S"),
        ("https://ourworldindata.org/global-education", "Our World in Data, Global education", "S"),
        ("https://articles.findmycollege.com/news/international-literacy-day-2026-60-years-on-739-million-adults-still-lack-basic-skills/", "Find My College, International Literacy Day 2026 (UNESCO figures)", "S"),
        ("https://www.siasat.com/over-272-million-children-out-of-school-across-the-globe-unesco-report-3233629/", "Siasat, Over 272 million children out of school (UNESCO)", "S")]),
    ("Telephones and the internet", [
        ("https://ourworldindata.org/internet", "Our World in Data, Internet", "S"),
        ("https://en.wikipedia.org/wiki/Global_Internet_usage", "Wikipedia, Global Internet usage", "S"),
        ("https://techblog.comsoc.org/?p=1074629", "IEEE ComSoc Technology Blog, ITU's Facts and Figures 2025", "S"),
        ("https://en.wikipedia.org/wiki/Mobile_phone", "Wikipedia, Mobile phone", "S"),
        ("https://ourworldindata.org/technology-adoption", "Our World in Data, Technology adoption", "S")]),
]

groups, n = groups_html(AREAS)
assert n == 5, n
BODY = (
    section("scale", "How large the gains are", "", stats_html(STATS)
            + chart_block("Share of people able to read",
                          "Hatched bars are rough figures from a page that names no source. Solid bars are UNESCO's figures as reported. The adult and youth bars measure different age groups.",
                          chart_html(CH_LIT, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of share able to read, from about 10 percent in 1820 to 88 percent of adults now"))
            + chart_block("Share of the world's people online",
                          "Figures from different pages, so the 2023 row shows Our World in Data's 63%, where Wikipedia gives 67%.",
                          chart_html(CH_NET, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of share of the world online from 16 percent in 2005 to 74 percent in 2025"))
            + chart_block("Who is online: the gaps",
                          "Each pair compares two groups in the same year. The gaps are 44 and 54 points between Africa and Europe, 71 points between low- and high-income countries, and 27 between rural and urban residents.",
                          chart_html(CH_GAP, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of internet use for Africa and Europe, low and high income countries, and rural and urban residents")))
    + section("gains", "The gains", "Five entries in two groups. Each gives the scale, the definitions and how solid the figures are.", groups)
    + section("limits-of-gains", "Where the gains thin", "", '<p class="note">These four limits come from the same sources as the entries above.</p>' + cards_html(THIN, "thin", True))
    + section("patterns", "What the record shows", "", '<p class="note">These are my reading of the entries and my arithmetic, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tag: S is a secondary source such as a data compilation, encyclopedia or news report. No primary report was read directly.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Knowledge and Connection",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 5 · Gains",
        "@@H1@@": "Knowledge and connection",
        "@@SUB@@": "Five entries on reading, school, broadcasting, the telephone and the internet",
        "@@LEDE@@": "How many people can read, how many are in school, and how many are reached by a telephone, a screen or a connection. This chapter measures access. It does not measure what people do with it.",
        "@@ASOF@@": "Figures current to 27 October 2026. Several come from news reports of UNESCO and ITU estimates.",
        "@@NAV@@": nav([("scale", "Scale"), ("gains", "The gains"), ("limits-of-gains", "Where they thin"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several figures are my own arithmetic on the sources' numbers: the gaps between groups (44 and 54 points between Africa and Europe, 71 between low- and high-income countries, 27 between rural and urban residents) and the range of 27 to 71 points. The observations under “What the record shows” are my own reading. The US household figures repeat those in Chapter 1 and the 2025 online figures rest on a summary of the ITU report.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "knowledge-and-connection.html")
    print("ok", n)
