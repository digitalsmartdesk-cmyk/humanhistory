from common import *

# =====================================================================
# CHAPTER 14: MIND AND WELLBEING
# =====================================================================
ACC, ACCD = "#1f7a5a", "#7fd6b5"

STATS = [
    ("1.2 billion", "people living with a mental disorder in 2023, nearly 1 in 7 (WHO)"),
    ("One third", "of people with depression receive formal mental health care, and 40% of those with psychosis (WHO)"),
    ("2%", "of total health budgets is the median share governments spend on mental health (WHO, 2025)"),
    ("1 in 6", "people worldwide are affected by loneliness, linked to more than 871,000 deaths a year (WHO)"),
]

CH_COUNT = [
    ("Any mental disorder, 2023", "1.2 billion", 0, 1200, False, None),
    ("Anxiety disorders, 2023", "470 million, 146 million of them children and adolescents", 0, 470, False, None),
    ("Depression, 2023", "322 million, 43 million of them children and adolescents", 0, 322, False, None),
    ("Drug use disorders, 2022", "63 million (UN World Drug Report 2025, as reported)", 0, 63, False, None),
    ("Conduct-dissocial disorder, 2023", "39 million children and adolescents", 0, 39, False, None),
    ("Eating disorders, 2023", "4.7 million children and adolescents", 0, 4.7, False, None),
]
CH_CARE = [
    ("People with psychosis", "40% receive formal mental health care", 0, 40, False, None),
    ("People with depression", "One third receive formal care", 0, 33.3, True, None),
    ("People with serious drug use disorders", "About one in five receive treatment", 0, 20, True, None),
]
CH_LONELY = [
    ("Low-income countries", "About 24%", 0, 24, False, None),
    ("High-income countries", "About 11%", 0, 11, False, None),
    ("Aged 13 to 29", "17 to 21%, highest in teenagers", 17, 21, False, None),
    ("Whole population", "1 in 6, which I read as about 17%", 0, 16.7, True, None),
]

AREAS = [
    ("Burden and care", [
        ("2023", "Mental disorders", "How many people live with a mental disorder",
         "WHO's fact sheet says nearly 1 in 7 people, 1.2 billion, were living with a mental disorder in 2023. That included 470 million with anxiety disorders, 146 million of them children and adolescents, and 322 million with depression, 43 million of them children and adolescents. Among adolescents aged 10 to 19 it counts 3.3 million with bipolar disorder, 4.7 million with eating disorders and 39 million with conduct-dissocial disorder.",
         [("Disability", "WHO's 2025 reports describe anxiety and depression as the second leading cause of long-term disability, with over 1 billion people living with mental health conditions."),
          ("Over a life", "Our World in Data cites an estimate, with no year, that 1 in 3 women and 1 in 5 men will experience major depression in their lives.")],
         "The WHO figures are modelled estimates. The pages give no earlier figures, so they show scale and not change."),
        ("2024 to 2025", "Care", "Whether people get help",
         "Most people with mental disorders do not have access to effective care. Only 40% of people with psychosis and one third of people with depression receive formal mental health care. The median government spends just 2% of its total health budget on mental health, according to a September 2025 WHO release citing the Mental Health Atlas 2024. For drug use disorders, the UN report says only about one in five people with serious disorders receive treatment.",
         [("Gaps", "WHO describes stark disparities between high- and low-income countries and a shortage of workforce, but the pages I read give no figures.")],
         "WHO's own pages, plus a news report for the drug figure. The release gave no reference year for the spending figure."),
        ("2021", "Suicide", "Deaths by suicide",
         "WHO says 727,000 people take their own life each year, though the same page elsewhere says more than 720,000. In 2021, 73% of suicides, close to three quarters, were in low- and middle-income countries, and suicide was the third leading cause of death among 15 to 29 year olds. WHO says many people are not seeking help and so are not getting the help they need.",
         [("Support", "If this subject is close to you, speaking to a doctor, a trusted person or a local crisis line is a sensible step.")],
         "The page gives no year for the 727,000, no rate per 100,000 and no trend. I did not find a long-run series."),
        ("2022 to 2023", "Drugs", "Drug use",
         "The 2025 World Drug Report, as reported, says more than 316 million people used drugs in 2023, 6% of adults aged 15 to 65, up from 5.2% in 2013. About 63 million people had drug use disorders in 2022, and there were about 25 million cocaine users. Fentanyl caused more than 100,000 deaths in the United States in 2023.",
         [],
         "A news report of a UN report. I did not read the report, and I found no figure for drug use before 2013."),
    ]),
    ("Connection and satisfaction", [
        ("2025", "Loneliness", "Loneliness and isolation",
         "WHO's Commission on Social Connection says 1 in 6 people worldwide is affected by loneliness, linked to more than 871,000 deaths a year, about 100 an hour. Between 17% and 21% of people aged 13 to 29 report loneliness, highest among teenagers. About 24% of people in low-income countries report it, about double the 11% in high-income countries.",
         [("Isolation", "Social isolation is estimated to affect up to 1 in 3 older adults and 1 in 4 adolescents, though data on older adults are limited.")],
         "From WHO's own news release. How the 871,000 deaths were attributed is not stated on the page."),
        ("2026", "Life satisfaction", "How satisfied people say they are",
         "In the World Happiness Report 2026 Finland ranked first for a record ninth year, Costa Rica fourth, its highest ranking, and Switzerland tenth. Our World in Data says countries with higher average incomes tend to report higher life satisfaction, and that the share saying they are very or rather happy rose in most countries with two or more surveys. In Albania it went from 33.4% in 1998 to 73.9% in 2022, while in Greece satisfaction fell from about 67% in 2007 to 32.4% five years later.",
         [("Measure", "Life satisfaction is the Gallup World Poll's 0 to 10 ladder, from the worst to the best possible life, asked in more than 160 countries.")],
         "The report page gives rankings but no global average, scale or data years, and I did not read the full report. The trend figures are from two survey series that do not cover the whole world."),
        ("2026", "Young people and screens", "Screens and the well-being of the young",
         "The World Happiness Report 2026 says heavy social media use appears to be contributing to the drop in well-being among young people in English-speaking countries and Western Europe, especially among girls. WHO's report on social connection also calls for attention to excessive screen time and negative online interactions.",
         [],
         "Tentative. The wording is 'appears to be', so it is an observed association and not a proven cause, and it is limited to some regions."),
    ]),
]

THIN = [
    ("Most people get no formal care", "Only one third of people with depression, 40% of those with psychosis and about one in five with serious drug use disorders receive treatment, and the median government spends 2% of its health budget on mental health.", "WHO; UN, via a news report"),
    ("Loneliness is reported more in poorer countries", "About 24% of people in low-income countries report loneliness against about 11% in high-income ones, and WHO describes stark disparities in mental health care between high- and low-income countries.", "WHO"),
    ("Loneliness is common among the young", "17% to 21% of people aged 13 to 29 report loneliness, highest among teenagers, and the World Happiness Report links heavy social media use to falling well-being among young people in some regions.", "WHO; World Happiness Report 2026"),
    ("Satisfaction can fall quickly", "In Greece the share satisfied fell from about 67% in 2007 to 32.4% five years later, after the financial crisis.", "Our World in Data"),
]

PATTERNS = [
    ("The scale is large and the care is thin", "More than 1 in 7 people live with a mental disorder, and for depression only one third receive formal care while governments spend a median 2% of health budgets on mental health."),
    ("The record cannot say whether mental illness has become more common", "None of the pages I read gives a long-run series of prevalence, and Our World in Data says many people do not report symptoms, which makes prevalence hard to estimate. The 1925 comparison cannot be made on these figures."),
    ("Life satisfaction goes with income and is hit by crises", "Across countries higher average income goes with higher satisfaction, it rose in most countries with repeated surveys, and Greece fell sharply after the financial crisis. These are patterns in two survey series, not a cause."),
    ("The young are a focus of the 2025 and 2026 reports", "WHO and the World Happiness Report both single out young people, for loneliness and for the possible effect of screens, and both are cautious about cause."),
    ("Loneliness and care both differ by income", "Loneliness is reported about twice as often in low-income countries as in high-income ones, and WHO describes stark gaps in care between them, though the pages give no figures for the care gap."),
]

LIMITS = [
    "Mental health is measured here by modelled counts, surveys and self-reports, and many people do not report symptoms.",
    "I found no long-run series on mental disorders, suicide, loneliness or life satisfaction, so this chapter cannot compare the century before 1925 with the century after.",
    "Several figures are news reports of reports: the World Drug Report and the Happiness Report rankings were not read in full.",
    "Life satisfaction is a self-rating on a 0 to 10 ladder, and cultures answer such questions differently.",
    "Not covered: sleep, stress at work, dementia, grief, the effect of war and violence, and the experience of people with severe illness.",
    "A count of deaths by suicide says nothing about why individuals take their own lives, and I found no rate per 100,000 or share of the poorer countries' population to set the 73% against.",
]

SRCS = [
    ("Burden and care", [
        ("https://www.who.int/news-room/fact-sheets/detail/mental-disorders", "WHO, Mental disorders fact sheet", "P"),
        ("https://www.who.int/thailand/news/feature-stories/detail/2-new-who-reports-reveal-urgent-need-to-scale-up-mental-health-services-globally", "WHO, Two new reports reveal urgent need to scale up mental health services", "P"),
        ("https://www.who.int/news-room/fact-sheets/detail/suicide", "WHO, Suicide fact sheet", "P"),
        ("https://ourworldindata.org/mental-health", "Our World in Data, Mental health", "S"),
        ("https://orain.eus/en/current-events/society-and-social-news-now/2025/06/26/more-than-300-million-people-use-drugs-in-the-world-6-of-adults/", "Orain, More than 300 million people use drugs (UN World Drug Report 2025)", "S")]),
    ("Connection and satisfaction", [
        ("https://who.int/news/item/30-06-2025-social-connection-linked-to-improved-heath-and-reduced-risk-of-early-death", "WHO, Social connection linked to improved health and reduced risk of early death", "P"),
        ("https://www.unsdsn.org/resources/world-happiness-report-2026", "UN Sustainable Development Solutions Network, World Happiness Report 2026", "P"),
        ("https://ourworldindata.org/happiness-and-life-satisfaction", "Our World in Data, Happiness and life satisfaction", "S")]),
]

groups, n = groups_html(AREAS)
assert n == 7, n
BODY = (
    section("scale", "The scale", "", stats_html(STATS)
            + chart_block("People living with mental disorders, millions",
                          "WHO's modelled estimates for 2023, with the drug use figure from the UN as reported. Several bars count children and adolescents only, as labelled.",
                          chart_html(CH_COUNT, [(0, "0"), (400, "400"), (800, "800"), (1200, "1,200")], 1200, "Bar chart of people with mental disorders, from 1.2 billion with any disorder to 4.7 million adolescents with eating disorders"))
            + chart_block("Share of people with each condition who receive care",
                          "WHO's figures for psychosis and depression, and the UN's for serious drug use disorders. Hatched bars are my reading of 'one third' and 'one in five'.",
                          chart_html(CH_CARE, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of share receiving care: 40 percent for psychosis, one third for depression, one in five for serious drug use disorders"))
            + chart_block("Share of people who report loneliness",
                          "WHO's Commission on Social Connection. The aged 13 to 29 bar spans 17 to 21%. The whole-population bar is my reading of '1 in 6'.",
                          chart_html(CH_LONELY, [(0, "0%"), (10, "10%"), (20, "20%"), (30, "30%")], 30, "Bar chart of loneliness in low and high income countries, among people aged 13 to 29 and overall")))
    + section("entries", "Mind and wellbeing", "Seven entries in two groups. Each gives the scale, what the source says about change and how solid the figures are.", groups)
    + section("strains", "Where the record is hard", "", '<p class="note">These four points come from the same sources as the entries above.</p>' + cards_html(THIN, "thin", True))
    + section("patterns", "What the record shows", "", '<p class="note">These are my reading of the entries, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or the institution\'s own page. S is a secondary source such as a data compilation or news report.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Mind and Wellbeing",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 14 · How people live",
        "@@H1@@": "Mind and wellbeing",
        "@@SUB@@": "Seven entries on mental disorders, care, suicide, drugs, loneliness and life satisfaction",
        "@@LEDE@@": "How many people live with a mental disorder, how many get help, how connected people are and how satisfied they say they are. The sources give the present and the recent past, with no long series.",
        "@@ASOF@@": "Figures current to 27 October 2026. This chapter includes figures on suicide. Most come from WHO's own pages.",
        "@@NAV@@": nav([("scale", "The scale"), ("entries", "Mind and wellbeing"), ("strains", "Where it is hard"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Two readings of the sources' wording are mine: that 'one third' is about 33% and 'one in five' about 20% in the chart on care, and that '1 in 6' is about 17% in the loneliness chart. The observations under “What the record shows” are my own reading.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "mind-and-wellbeing.html")
    print("ok", n)
