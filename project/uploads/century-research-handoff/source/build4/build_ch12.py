from common import *

# =====================================================================
# CHAPTER 12: WORK, INEQUALITY AND POPULATION
# =====================================================================
ACC, ACCD = "#44546a", "#a9b8cf"

STATS = [
    ("8.2 billion → 10.3 billion", "world population in 2024 and the UN's projected peak, in the mid-2080s, before a slow decline"),
    ("4.9 → 2.3", "children per woman worldwide, in the 1950s and in 2023"),
    ("246 million → 138 million", "children in child labour, 2000 and 2024 (ILO and UNICEF)"),
    ("53% and 8%", "of global income taken by the richest 10% and by the poorer half of adults (World Inequality Report 2026)"),
]

CH_CL = [
    ("2000", "246 million (ILO and UNICEF, 2025 release)", 0, 246, False, None),
    ("2013", "265 million, almost 17% of children (ILO, 2013 report)", 0, 265, True, None),
    ("2020", "At least about 158 million: 138 plus the 'over 20 million' fall since", 0, 158, True, None),
    ("2024", "Nearly 138 million; 54 million in hazardous work", 0, 138, False, None),
]
CH_SHARE = [
    ("Richest 10%, income", "53% of global income", 0, 53, False, None),
    ("Poorer half, income", "8% of global income", 0, 8, False, None),
    ("Richest 10%, wealth", "75% of global wealth", 0, 75, False, None),
    ("Richest 1%, wealth", "37% of global wealth", 0, 37, False, None),
    ("Poorer half, wealth", "2% of global wealth", 0, 2, False, None),
]
CH_FERT = [
    ("World, 1950s", "4.9 children per woman", 0, 4.9, False, None),
    ("World, 2023", "2.3", 0, 2.3, False, None),
    ("Replacement level", "2.1, the UN's figure", 0, 2.1, False, None),
    ("Niger, 2023", "6", 0, 6, False, None),
    ("South Korea, 1950s", "Around 6", 0, 6, True, None),
    ("South Korea, 2023", "Less than 1", 0, 1, True, None),
    ("India, 1970s", "About 5", 0, 5, True, None),
    ("India, 2023", "About 2", 0, 2, True, None),
]

AREAS = [
    ("Work", [
        ("Today", "Sectors", "From the farm to other work",
         "Around one-quarter of the world's labour force works in agriculture. In many low- and middle-income countries the majority works in farming and relies on it as its main income, as most people did in rich countries a few centuries ago. As countries get richer the share working in agriculture tends to fall as people move into industry and services.",
         [("Productivity", "Value added per farm worker can differ ten-fold between countries.")],
         "The page gives the one-quarter figure and these statements, but its history is in charts whose data the text does not include. I have no figure for the share in agriculture in 1825 or 1925."),
        ("2000 to 2024", "Child labour", "Children at work",
         "The ILO and UNICEF estimate nearly 138 million children were in child labour in 2024, down from 246 million in 2000, with about 54 million in hazardous work. Agriculture accounts for 61%, services 27% and industry 13%. Sub-Saharan Africa has about 87 million, nearly two-thirds of the total, while in Asia and the Pacific prevalence fell from 6% to 3% since 2020.",
         [("History", "Child work was widespread in 19th-century Europe and North America and fell rapidly around the turn of the 20th century. Our World in Data says England's 1900 child labour rate was similar to today's global rate. Among 12 to 14 year olds in England and Wales it fell to about 6–7% after the First World War and rose to 15.3% by 1944."),
          ("Risk", "The release warns that global funding cuts threaten to roll back the gains.")],
         "The 2024 and 2000 figures are from the ILO and UNICEF release. Our World in Data gives 265 million in 2013 from an earlier ILO report, and the two reports may not use the same method, so I do not draw a straight line through them."),
        ("1990 to 2024", "Women's work", "Women in paid work",
         "Around half of women worldwide take part in the labour force, a figure ILO estimates say has stayed around 50% since the early 1990s, while men's participation fell from 80% in 1990 to around 73%. In 2024 it was 62% in Sweden, 56% in Germany and 41% in Italy.",
         [("Unpaid work", "Women spend more time on unpaid care than men in every country, in some by more than six times. Average US household housework fell from 58 hours a week in 1900 to 18 in 1975.")],
         "From Our World in Data's page on the ILO's modelled estimates. The page gives no regional percentages and no US participation figures for 1900 or 1950."),
        ("2026", "Informal work", "Work outside formal protection",
         "An ILO analysis reported on 12 May 2026 found nearly 58% of workers globally in informal jobs.",
         [],
         "Thin. It is a news report of an ILO analysis, with no worker count, no regions and no definition, and I did not read the ILO's own page."),
    ]),
    ("Inequality", [
        ("Today", "Between countries", "How much depends on where you live",
         "Milanovic (2015) is cited as finding that the country a person lives in explains two-thirds of the variation of income differences among all people. The poorer half of the world, almost 4 billion people, live on less than $6.70 a day, and someone on $30 a day is in the richest 15%. Swedes are about 30 times richer than in 1820, and about 96% of the world's people live in the country they were born in.",
         [("Prices", "The figures use 2011 international dollars from an earlier World Bank release, and the page notes the World Bank has since updated its data.")],
         "From Our World in Data's introduction to global inequality. The page gives no Gini or Theil values and no top-10% shares, so I cannot show how total inequality moved over two centuries."),
        ("2025", "Shares of income and wealth", "Who holds what, now",
         "The World Inequality Report 2026, as reported, says the richest 10% earn 53% of global income and the poorer half of adults, about 2.8 billion, 8%. The richest 10% own 75% of global wealth, the richest 1% own 37% and the poorer half 2%. Around 56,000 people, the top 0.001%, hold more wealth than 2.8 billion adults together.",
         [("Regions", "Average wealth in North America and Oceania in 2025 is more than sixteen times that of Sub-Saharan Africa.")],
         "From a news report of the report, not the report. It gives no earlier shares, so it shows how things stand and not whether they have changed."),
    ]),
    ("Population and where people live", [
        ("1963 to 2086", "Growth", "The peak of population",
         "Population growth peaked in the 1960s at over 2% a year, 2.3% in 1963 on the chart, and was 0.9% in 2023. The UN projects a peak of about 10.3 billion in the mid-2080s and about 10.2 billion by 2100, from 8.2 billion in 2024. 63 countries have already passed their peak, including China, Germany, Japan and Russia. The number of children under five peaked in 2017.",
         [("Versions", "Our World in Data's text says the peak is in 2086 at just over 10.4 billion, while a chart on the same page says about 10.3 billion in 2084, and the two seem to come from different UN editions.")],
         "These are projections and the page says they are sensitive to assumptions about fertility."),
        ("1950s to 2023", "Fertility", "Fewer children per woman",
         "The world's fertility rate was 4.9 in the 1950s and 2.3 in 2023. Niger had 6 in 2023. South Korea fell from around 6 in the 1950s to less than 1, and most countries in East Asia were below 1. India fell from about 5 in the 1970s to about 2. More than half of all countries are below the replacement level of 2.1, and nearly a fifth have fewer than 1.4.",
         [],
         "Our World in Data and the UN, read through a summarizing tool. The UN page gave no world fertility rate for 2024 and none for 1950 itself, so the 1950s figure is Our World in Data's."),
        ("Late 2070s", "Ageing", "More old people than children",
         "The UN expects people aged 65 or over to outnumber children under 18 by the late 2070s. Global life expectancy was 73.3 in 2024, up from 70.9 in the pandemic.",
         [],
         "A projection. The page gave no share of the population aged 65 or over today, and its pandemic life expectancy of 70.9 differs from the 71.5 that WHO gives in Chapter 3, and I did not check why."),
        ("Today", "Crowding", "Cities and slums",
         "Around one in four people in urban areas live in slum households, and in sub-Saharan Africa more than half of urban residents do, with Chad near 80%.",
         [("Link", "Chapter 1 gives the rise in the share of people living in cities.")],
         "From Our World in Data's page on urbanization. It gives no total count of people living in slums and no year for the shares."),
    ]),
]

THIN = [
    ("Child labour is concentrated", "About 87 million of the 138 million children in child labour are in sub-Saharan Africa, nearly two-thirds. 54 million are in hazardous work.", "ILO and UNICEF"),
    ("Most work is informal", "Nearly 58% of workers worldwide are in informal jobs, on a news report of an ILO analysis.", "ILO, via a news report"),
    ("Wealth is held by few", "The richest 10% own 75% of global wealth and the poorer half own 2%. Average wealth in North America and Oceania is more than sixteen times that of Sub-Saharan Africa.", "World Inequality Report 2026, via a news report"),
    ("Shrinking and ageing populations", "63 countries have passed their population peak, nearly a fifth have fertility below 1.4, and people aged 65 or over are expected to outnumber children under 18 by the late 2070s.", "UN World Population Prospects 2024"),
]

PATTERNS = [
    ("Where people live now matters more than much else", "The country of residence explains two-thirds of income differences, 96% of people live where they were born, and child labour, informal work, slum living and low internet access all concentrate in the poorer regions, on the figures in this and the earlier chapters."),
    ("Child labour has fallen by almost half in 24 years and is still large", "From 246 million in 2000 to 138 million in 2024 is a fall of 44%, on my division, and the ILO release says funding cuts could reverse it."),
    ("The turn in population is already here for many countries", "More than half of countries are below replacement fertility and 63 have passed their peak, while the world total is projected to keep rising until the 2080s."),
    ("Shares of income and wealth are given for one year only", "The 2025 figures show the shape of inequality but not its history, so this chapter cannot say whether inequality rose or fell across the century."),
    ("The data do not fall on 1825 and 1925", "Child labour starts in 2000, fertility in the 1950s, inequality shares in 2025. A comparison of the two centuries cannot be made on these figures."),
]

LIMITS = [
    "Almost no series here reaches back to 1825 or 1925. The chapter describes the present and the last seven decades.",
    "Several figures are news reports of the World Inequality Report and ILO analyses. I did not read the reports themselves.",
    "The child labour totals for 2000 and 2013 come from different reports and may not be on the same footing.",
    "Informal work, women's work and slum living are given with few numbers and no earlier dates.",
    "Population projections depend on assumptions about fertility and differ between UN editions.",
    "Pay, hours and working conditions in rich countries are covered only in Chapter 4, and not here.",
]

SRCS = [
    ("Work", [
        ("https://ourworldindata.org/employment-in-agriculture", "Our World in Data, Employment in agriculture", "S"),
        ("https://ourworldindata.org/child-labor", "Our World in Data, Child labor", "S"),
        ("https://www.unicef.org/press-releases/despite-progress-child-labour-still-affects-138-million-children-globally-ilo-unicef", "ILO and UNICEF, Despite progress, child labour still affects 138 million children globally", "P"),
        ("https://ourworldindata.org/female-labor-force-participation-key-facts", "Our World in Data, Female labor force participation: key facts", "S"),
        ("https://www.peoplematters.in/news/economy-policy/nearly-58percent-of-global-workforce-still-trapped-in-informal-employment-ilo-report-49690", "People Matters, Nearly 58% of global workforce in informal employment (ILO)", "S")]),
    ("Inequality", [
        ("https://ourworldindata.org/global-economic-inequality-introduction", "Our World in Data, Global economic inequality", "S"),
        ("https://www.storyboard18.com/amp/how-it-works/worlds-richest-10-take-over-half-of-global-income-says-world-inequality-report-87155.htm", "Storyboard18, World's richest 10% take over half of global income (World Inequality Report 2026)", "S")]),
    ("Population", [
        ("https://ourworldindata.org/world-population-growth", "Our World in Data, World population growth", "S"),
        ("https://ourworldindata.org/fertility-rate", "Our World in Data, Fertility rate", "S"),
        ("https://www.un.org/sustainabledevelopment/blog/2024/07/press-release-wpp2024/", "United Nations, World Population Prospects 2024 press release", "P"),
        ("https://ourworldindata.org/urbanization", "Our World in Data, Urbanization", "S")]),
]

groups, n = groups_html(AREAS)
assert n == 10, n
BODY = (
    section("scale", "The picture", "", stats_html(STATS)
            + chart_block("Children in child labour, millions",
                          "The 2000 and 2024 bars are from the 2025 ILO and UNICEF release. The 2013 bar is from an earlier ILO report and may use a different method. The 2020 bar is my estimate from the 'over 20 million' fall the release reports, so it is hatched.",
                          chart_html(CH_CL, [(0, "0"), (100, "100"), (200, "200"), (300, "300")], 300, "Bar chart of children in child labour, from 246 million in 2000 to about 138 million in 2024"))
            + chart_block("Shares of global income and wealth, percent",
                          "The World Inequality Report 2026 as reported for 2025. 'Poorer half' means the poorer half of adults, about 2.8 billion people.",
                          chart_html(CH_SHARE, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of shares of income and wealth held by the richest 10 percent, richest 1 percent and poorer half"))
            + chart_block("Children per woman",
                          "Different places and years, so compare the sizes. Hatched bars are rough figures: 'around', 'about' or 'less than 1'.",
                          chart_html(CH_FERT, [(0, "0"), (2, "2"), (4, "4"), (6, "6")], 7, "Bar chart of children per woman for the world, Niger, South Korea and India")))
    + section("entries", "How people live", "Ten entries in three groups. Each gives the scale, what the source says about change and how solid the figures are.", groups)
    + section("strains", "Where the record is hard", "", '<p class="note">These four points come from the same sources as the entries above.</p>' + cards_html(THIN, "thin", True))
    + section("patterns", "What the record shows", "", '<p class="note">These are my reading of the entries and my arithmetic, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or the institution\'s own page. S is a secondary source such as a data compilation or news report.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Work, Inequality and Population",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 12 · How people live",
        "@@H1@@": "Work, inequality and population",
        "@@SUB@@": "Ten entries on jobs, child labour, shares of income and wealth, fertility and ageing",
        "@@LEDE@@": "How the world works, who holds its income and wealth, and how many people there are and will be. This chapter describes the present and the recent past, since most of its series do not reach back to 1825 or 1925.",
        "@@ASOF@@": "Figures current to 27 October 2026. Several come from news reports of ILO and World Inequality Report findings.",
        "@@NAV@@": nav([("scale", "The picture"), ("entries", "How people live"), ("strains", "Where it is hard"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several figures are my own arithmetic on the sources' numbers: the 44% fall in child labour from 2000 to 2024, and the estimate of at least about 158 million children in child labour in 2020 (138 million plus the 'over 20 million' fall the release reports). The observations under “What the record shows” are my own reading.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "work-inequality-population.html")
    print("ok", n)
