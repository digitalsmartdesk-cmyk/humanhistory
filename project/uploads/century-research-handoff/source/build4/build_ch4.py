from common import *

# =====================================================================
# CHAPTER 4: FOOD, WEALTH AND COMFORT
# =====================================================================
ACC, ACCD = "#7a6a00", "#e0cf5a"

STATS = [
    ("2,184 → 3,006", "kilocalories of food supplied per person per day, world, 1961 to 2023 (FAO)"),
    ("About 3/4 → about 8%", "of the world in extreme poverty, 1820 and the latest year, by two different methods and lines"),
    ("3,168 → 1,487", "hours worked per worker per year in France, 1870 and 2023"),
    ("673 million", "people facing hunger in 2024, 8.2% of the world (UN estimate)"),
]

CH_KCAL = [
    ("1961", "2,184 kcal", 0, 2183.74, False, None),
    ("1980", "2,457 kcal", 0, 2456.63, False, None),
    ("2000", "2,659 kcal", 0, 2659.22, False, None),
    ("2010", "2,796 kcal", 0, 2795.76, False, None),
    ("2023", "3,006 kcal", 0, 3005.62, False, None),
]
CH_POOR = [
    ("1820", "965 million; $1.90 line", 0, 964.9, False, None),
    ("1950", "1,596 million; $1.90 line", 0, 1596.4, False, None),
    ("1990", "1,904 million; $1.90 line", 0, 1903.5, False, None),
    ("2010", "1,091 million; $1.90 line", 0, 1090.7, False, None),
    ("2015", "733 million; $1.90 line", 0, 733.5, False, None),
    ("1990, World Bank", "About 2.3 billion; $3 line, 2021 prices", 0, 2300, True, None),
    ("2026, World Bank", "About 837 million; $3 line, 2021 prices", 0, 837, True, None),
]
CH_HOURS = [
    ("France, 1870", "3,168 hours", 0, 3168, False, None),
    ("France, 2023", "1,487 hours", 0, 1487.10, False, None),
    ("Germany, 1870", "3,284 hours", 0, 3284, False, None),
    ("Germany, 2023", "1,335 hours", 0, 1335.27, False, None),
    ("United Kingdom, 1870", "2,755 hours", 0, 2755, False, None),
    ("United Kingdom, 2023", "1,523 hours", 0, 1522.80, False, None),
    ("United States, 1870", "3,096 hours", 0, 3096, False, None),
    ("United States, 2023", "1,789 hours", 0, 1788.88, False, None),
    ("India, 1970", "2,434 hours", 0, 2434.08, False, None),
    ("India, 2023", "2,383 hours", 0, 2382.58, False, None),
]

AREAS = [
    ("Food", [
        ("1961 to 2023", "Food supply", "More calories for each person",
         "The FAO's measure of food supplied per person per day rose from 2,184 kilocalories in 1961 to 2,457 in 1980, 2,659 in 2000, 2,796 in 2010 and 3,006 in 2023. Supply grew substantially in Asia and Africa, and the regional gaps have been converging. In France the average food supply more than doubled over the last 300 years.",
         [("Not the same as eating", "The figure counts food available at retail level and leaves out waste in homes, so people eat less than the supply. It measures energy only, not vitamins or minerals.")],
         "The world figures are from the FAO series as compiled by Our World in Data. The page gives no regional values in its text and the French long-run figure is the only one before 1961."),
        ("19th and 20th centuries", "Famine", "Famines and their deaths",
         "Ó Gráda calls 100 million deaths a conservative estimate for famines in the 19th century, about the same as the 20th-century total, so the 19th century was far deadlier in proportion. The deadliest 20th-century famine was in China from 1958 to 1962, an estimated 36 million deaths, or 45 million in Dikötter's estimate. Wartime famines in the Second World War killed about 25 million.",
         [("Since", "The death rate from famine fell to very low levels in the second half of the 20th century. Northeast Nigeria in 2016–2019, with an estimated 340,000 deaths, is the only large famine in a democracy since 1870, according to the page.")],
         "Estimates differ widely: the Chinese toll is 36 or 45 million depending on the author. The page cites Devereux as calling the 20th century the highest total for any century, which sits oddly beside Ó Gráda's figure, and it gives no 21st-century total."),
        ("2022 to 2024", "Hunger", "People still without enough to eat",
         "The UN estimates 8.2% of the world, about 673 million people, faced hunger in 2024, with a range of 638 to 720 million. The share was 8.5% in 2023 and 8.7% in 2022. In Africa it was over 20%, affecting 307 million people, while in Asia it fell from 7.9% in 2022 to 6.7%, or 323 million, in 2024.",
         [("Outlook", "512 million people could be chronically undernourished by 2030, almost 60% of them in Africa. The UN goal is to end hunger by 2030.")],
         "The 2024 figure is a UN estimate with a stated range. The page gives no hunger figure for 2000 or 2019, so I cannot show the long run."),
    ]),
    ("Poverty and income", [
        ("1820 to 2015", "Extreme poverty", "The long run of extreme poverty",
         "Michail Moatsos estimates that about three-quarters of the world lived in extreme poverty in 1820. Our World in Data's count of people below $1.90 a day shows 965 million in 1820, 1,596 million in 1950, 1,904 million in 1990, 1,091 million in 2010 and 733 million in 2015.",
         [("Method", "The 1820 share uses a cost-of-basic-needs approach, while later figures use an income or consumption line. The two do not measure the same thing."),
          ("Count against share", "The count rose from 1820 to 1990 while the population also grew, and then fell.")],
         "The chart's own page names the $1.90 line but no data source and does not say how 1820–1980s values are made. The 1820 and later figures should be read as estimates with different methods."),
        ("1990 to 2026", "Extreme poverty", "Poverty at $3 a day",
         "The World Bank puts the number of people below $3 a day, in 2021 prices, at about 837 million in 2026, down from about 2.3 billion in 1990. Most of the decline came from East Asia and South Asia. Extreme poverty is increasingly concentrated in Sub-Saharan Africa and in places affected by conflict and fragility.",
         [("Slowdown", "Progress has slowed over the last decade, and at the current pace ending extreme poverty could take decades.")],
         "From the World Bank's own page, which gives a different line and different prices from the $1.90 chart above, so the two series should not be joined. The page text states no global percentage. The Our World in Data author argues that a $3 line is too high to show the incomes of the very poorest."),
        ("1900 to 2025", "Income", "World output per person",
         "World output was 1,103 billion in 1900 and 4,082 billion in 1950 in 1990 international dollars on the DeLong reconstruction. Output per person was 11,275 in 1990 and 21,914 in 2025 in 2021 international dollars, and total output was about 180 trillion in 2025.",
         [("Ratio", "By my division, output per person in 2025 was about 1.94 times that of 1990. The 1990–2025 per-person series has a different base from the DeLong series, so I do not join them.")],
         "Wikipedia's table gives no per-person figures before 1990. I found no world per-person series for 1825 or 1925."),
    ]),
    ("Work and the home", [
        ("1870 to 2023", "Working hours", "Fewer hours of work",
         "Annual hours worked per worker fell in France from 3,168 in 1870 to 1,487 in 2023, in Germany from 3,284 to 1,335, in the United Kingdom from 2,755 to 1,523 and in the United States from 3,096 to 1,789. Japan fell from 2,076 in 1950 to 1,654, while India's figure was 2,434 in 1970 and 2,383 in 2023.",
         [("Fall", "My division gives falls of 53% in France, 59% in Germany, 45% in the United Kingdom and 42% in the United States since 1870."),
          ("Rich and poor", "Workers in richer countries tend to work fewer hours than those in poorer countries, and the page notes large inequalities within and between countries.")],
         "The page does not name the source of the series or say whether it counts full-time and part-time work alike, so the long-run values need checking before use."),
        ("1925 to 2020", "Comfort", "Light, heat and clean fuel at home",
         "Half of US households had electric power in 1925 and 90% by 1949. Worldwide, more than 1.5 billion people lacked electricity in 1998 and fewer than 1 in 10 lack it now. About two-thirds of the world cooked with clean fuels in 2020, up from about half in 2000, and in the United States nearly half of homes lacked complete plumbing in 1940 and 1% did in 1990.",
         [("Detail", "The first chapter gives the full series and sources.")],
         "The US figures are from the OWID household-technology chart and the Census Bureau. The world figures are from Our World in Data's energy-access page, read through a summarizing tool."),
    ]),
]

THIN = [
    ("Supply is not intake", "The FAO calorie supply of 3,006 a day is food available at retail, not food eaten, and it says nothing about vitamins and minerals.", "Our World in Data"),
    ("Hunger is concentrated and rising in places", "In Africa the share facing hunger passed 20% in 2024, affecting 307 million people. The UN projects 512 million chronically undernourished by 2030, almost 60% in Africa.", "WHO, from the UN report"),
    ("Poverty progress has slowed", "The World Bank says progress has slowed over the last decade and that ending extreme poverty at the current pace could take decades. The $3 line is itself argued to be too high to show the very poorest.", "World Bank; Our World in Data"),
    ("Not all workers gained time", "India's annual hours per worker were 2,434 in 1970 and 2,383 in 2023, almost unchanged, while rich countries fell by 42–59% since 1870.", "Our World in Data"),
]

PATTERNS = [
    ("Supply rose, and hunger remains", "The calorie supply per person rose by about 38% between 1961 and 2023 on my division (2,184 to 3,006), yet 8.2% of the world still faced hunger in 2024. On these numbers the problem is not the world average."),
    ("Deadly famine has become rare, and the earlier toll was large", "The famine death rate fell to very low levels in the second half of the 20th century, and the one large recent case, Northeast Nigeria, is estimated at 340,000 deaths against tens of millions in earlier cases."),
    ("The number in extreme poverty fell by about 64% since 1990 on the World Bank figures", "From about 2.3 billion to 837 million, my division, mostly in East and South Asia. The count had risen from 1820 to 1990, as population grew."),
    ("Working hours fell in the rich countries shown and hardly in India", "The four rich countries shown cut annual hours by 42–59% since 1870. India's figure barely changed from 1970. Other countries are not shown, and the numbers do not show cause."),
    ("This chapter's data do not fall on 1825 and 1925", "Calories begin in 1961, poverty counts in 1820 and 1950, the World Bank figure in 1990 and working hours in 1870. A split at 1925 cannot be tested here."),
]

LIMITS = [
    "The measures cover food, money and hours, and say nothing about security, meaning or how people felt about their lives.",
    "The poverty series use different lines, prices and methods, so the earlier and later figures should not be joined into one line.",
    "I found no world per-person income series for 1825 or 1925. The only per-person series I read starts in 1990.",
    "Several pages gave their data only in charts, which I read through downloaded data files and a summarizing tool. Check against the originals.",
    "Housing beyond plumbing and electricity, clothing cost, and the price of food relative to wages are not covered here.",
    "The list is a selection of eight entries, not a full account of material life.",
]

SRCS = [
    ("Food and hunger", [
        ("https://ourworldindata.org/food-supply", "Our World in Data, Food supply", "S"),
        ("https://ourworldindata.org/grapher/daily-per-capita-caloric-supply", "Our World in Data, Daily supply of calories per person", "S"),
        ("https://ourworldindata.org/famines", "Our World in Data, Famines", "S"),
        ("https://ourworldindata.org/hunger-and-undernourishment", "Our World in Data, Hunger and undernourishment", "S"),
        ("https://www.who.int/news/item/28-07-2025-global-hunger-declines-but-rises-in-africa-and-western-asia-un-report", "WHO, Global hunger declines but rises in Africa and Western Asia", "P")]),
    ("Poverty and income", [
        ("https://ourworldindata.org/extreme-poverty-in-brief", "Our World in Data, Extreme poverty in brief", "S"),
        ("https://ourworldindata.org/grapher/world-population-in-extreme-poverty-absolute", "Our World in Data, World population living in extreme poverty", "S"),
        ("https://www.worldbank.org/poverty", "World Bank, Poverty", "P"),
        ("https://en.wikipedia.org/wiki/Gross_world_product", "Wikipedia, Gross world product", "S")]),
    ("Work and the home", [
        ("https://ourworldindata.org/working-hours", "Our World in Data, Working hours", "S"),
        ("https://ourworldindata.org/grapher/annual-working-hours-per-worker", "Our World in Data, Annual working hours per worker", "S"),
        ("https://ourworldindata.org/energy-access", "Our World in Data, Energy access", "S"),
        ("https://ourworldindata.org/technology-adoption", "Our World in Data, Technology adoption", "S"),
        ("https://www.census.gov/data/tables/time-series/dec/coh-plumbing.html", "US Census Bureau, Historical Census of Housing Tables: Plumbing", "P")]),
]

groups, n = groups_html(AREAS)
assert n == 8, n
BODY = (
    section("scale", "How large the gains are", "", stats_html(STATS)
            + chart_block("Food supplied per person per day, world, kilocalories",
                          "FAO supply as compiled by Our World in Data. It counts food available, not food eaten.",
                          chart_html(CH_KCAL, [(0, "0"), (1000, "1,000"), (2000, "2,000"), (3000, "3,000")], 3500, "Bar chart of world food supply per person per day, from 2,184 kilocalories in 1961 to 3,006 in 2023"))
            + chart_block("People in extreme poverty, millions",
                          "The first five rows use Our World in Data's $1.90 line. The last two, hatched, are the World Bank's $3 line in 2021 prices. The two sets are not comparable, so compare within each set.",
                          chart_html(CH_POOR, [(0, "0"), (500, "500"), (1000, "1,000"), (1500, "1,500"), (2000, "2,000")], 2500, "Bar chart of people in extreme poverty from 965 million in 1820 to 733 million in 2015, and World Bank figures of 2.3 billion in 1990 and 837 million in 2026"))
            + chart_block("Annual hours worked per worker",
                          "Our World in Data's series, in hours per year. India and Japan lack 1870 values, so India starts in 1970.",
                          chart_html(CH_HOURS, [(0, "0"), (1000, "1,000"), (2000, "2,000"), (3000, "3,000")], 3500, "Bar chart of annual working hours per worker in five countries, falling from over 3,000 in 1870 to under 1,800 in 2023 in the rich countries")))
    + section("gains", "The gains", "Eight entries in three groups. Each gives the scale, the cause where the source gives one, and how solid the figures are.", groups)
    + section("limits-of-gains", "Where the gains thin", "", '<p class="note">These four limits come from the same sources as the entries above.</p>' + cards_html(THIN, "thin", True))
    + section("patterns", "What the record shows", "", '<p class="note">These are my reading of the entries, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or the institution\'s own page. S is a secondary source such as a data compilation or encyclopedia.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Food, Wealth and Comfort",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 4 · Gains",
        "@@H1@@": "Food, wealth and comfort",
        "@@SUB@@": "Eight entries on food, famine, hunger, poverty, income, working hours and the home",
        "@@LEDE@@": "Food supply, famines, hunger, extreme poverty, world income, hours of work and the basics of a home. Each entry gives the scale, the cause where the source gives one and how solid the figures are, followed by the limits of the gains.",
        "@@ASOF@@": "Figures current to 27 October 2026. Many series start at different dates and use different lines, and each says which.",
        "@@NAV@@": nav([("scale", "Scale"), ("gains", "The gains"), ("limits-of-gains", "Where they thin"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several figures are my own arithmetic on the sources' numbers: the 38% rise in calorie supply, the 53%, 59%, 45% and 42% falls in working hours, the roughly 64% fall in the World Bank's count of people in extreme poverty, and the 1.94 ratio of world output per person in 2025 to 1990. The observations under “What the record shows” are my own reading. The household electricity and plumbing figures repeat those in Chapter 1.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "food-wealth-comfort.html")
    print("ok", n)
