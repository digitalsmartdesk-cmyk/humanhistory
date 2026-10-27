from common import *

# =====================================================================
# CHAPTER 3: LIFE AND HEALTH
# =====================================================================
ACC, ACCD = "#0e7490", "#67d4ec"

STATS = [
    ("1 in 2 → 4%", "of children dying before age 15: around 1 in 2 two centuries ago, 4% in 2020"),
    ("32 → 71", "years of global life expectancy at birth, 1900 to 2021; WHO puts 2023 at 73.3"),
    ("300 million", "estimated deaths from smallpox in the 20th century; the disease was certified eliminated in May 1980"),
    ("154 million", "deaths estimated to have been prevented by routine vaccination over the last fifty years"),
]

CH_CHILD = [
    ("About 1800", "Around 1 in 2; no exact figure given", 0, 50, True, None),
    ("1950", "Around one-quarter", 0, 25, False, None),
    ("2020", "4% (4.3% on another line of the page)", 0, 4, False, None),
]
CH_MATERNAL = [
    ("Sweden and Finland, 1800", "Around 900", 0, 900, False, None),
    ("19th century, some countries", "Roughly 500 to 1,000 (a range)", 500, 1000, True, None),
    ("Low-income countries, 2017", "Around 450", 0, 450, False, None),
    ("World, 2015", "About 216: my division of 302,700 deaths by about 140 million births", 0, 216, True, None),
    ("High-income countries, 2017", "Around 11", 0, 11, False, None),
]
CH_LIFE = [
    ("1900", "32 (Our World in Data)", 0, 32, False, None),
    ("1950", "45.7 to 48 (Wikipedia, two sources)", 45.7, 48, True, None),
    ("2019", "73.4 (WHO)", 0, 73.4, False, None),
    ("2021, pandemic low", "71.5 (WHO)", 0, 71.5, False, None),
    ("2023", "73.3 (WHO)", 0, 73.3, False, None),
    ("2023, healthy life expectancy", "62.8 (WHO)", 0, 62.8, False, None),
]

AREAS = [
    ("Surviving birth and childhood", [
        ("About 1800 to 2023", "Child survival", "Children dying before they grow up",
         "Around two centuries ago, about 1 in 2 children died before the end of puberty. By 1950 the share had fallen to around one-quarter, and by 2020 to 4%. In 2023 the UN estimated 4.8 million children died before their fifth birthday, and said child deaths had dropped by more than half since 2000.",
         [("Gaps", "In 2020, 13% of children in Nigeria and 7% in Pakistan died before 15, against 0.4% in Italy, Iceland, Japan and Norway."),
          ("Reversal", "Child mortality rose in South Africa and Zimbabwe in the 1990s and 2000s, largely because of HIV/AIDS."),
          ("Stillbirths", "About 1.9 million in 2023, down by over a third since 2000.")],
         "The 1800 figure is described only as 'around 1 in 2', with no exact value. The 1950 and 2020 figures are Our World in Data's. The 2023 count and the 'more than half since 2000' are from the UN's own estimate, as reported by WHO."),
        ("1800 to 2017", "Childbirth", "Mothers dying in childbirth",
         "In Sweden and Finland around 1800, around 900 mothers died per 100,000 live births, and in some countries in the 19th century the figure was roughly 500 to 1,000. In most rich countries it is now below 10, a fall of 50- to 100-fold.",
         [("2017", "About 11 per 100,000 live births in high-income countries and about 450 in low-income countries, about 40 times higher."),
          ("2015", "302,700 maternal deaths and about 140 million births, which I divide to about 216 per 100,000 as a rough world figure."),
          ("Lowest", "Finland 3 and Sweden 4 per 100,000, with the year not given.")],
         "The page gives no global ratio, so the 216 figure is my own division of two numbers it does give. The figures for the 1800s are for a few countries and are not world figures."),
    ]),
    ("Defeating particular diseases", [
        ("1967 to 1980", "Eradication", "Smallpox",
         "Donald Henderson estimates about 300 million people died of the disease in the 20th century. In 1967 an estimated 10 to 15 million people were infected each year while only 132,000 cases were reported. The last natural case of the milder form was in Merka, Somalia, on 26 October 1977, and the World Health Assembly certified elimination in May 1980.",
         [("Last severe case", "The last case of the more severe form was in Bangladesh in October 1975.")],
         "The death toll is one expert's estimate. The page itself says reported cases were far below the real number, so the case figures for 1967 are estimates."),
        ("1955 to 2021", "Near-eradication", "Polio",
         "Salk's vaccine was announced as effective in April 1955 and Sabin's oral vaccine was licensed in 1961. In the early 1980s an estimated 300,000 to 400,000 people were paralysed each year, and polio was endemic in 125 countries in 1988. The page gives 1,873 estimated paralytic cases in 2020 and 649 reported cases in 2021.",
         [("Where it remained", "Wild poliovirus cases were recorded only in Afghanistan, Pakistan and Malawi as of 2021."),
          ("Fall", "The page states no percentage. My arithmetic gives a fall of about 99.4–99.5% from the early 1980s to 2020 in estimated cases.")],
         "The 1980s figure is an estimate and the 2021 figure is reported cases, so the two are not the same kind of count."),
        ("1974 to 2024", "Vaccination", "Routine childhood vaccination",
         "A 2024 study by Shattock and colleagues estimated that routine vaccinations prevented 154 million deaths worldwide in the last fifty years. Measles vaccination alone is credited with 94 million lives.",
         [("Coverage", "Over 80% of infants worldwide now receive the full DTP course, a year not stated."),
          ("Threshold", "Measles needs coverage typically above 90% for herd immunity.")],
         "These are modelled estimates, not counts. The page gives no period for the measles figure, though a related chart is titled 1974 to 2024, and it gives no coverage figures for earlier decades."),
        ("1900 to the 1990s", "Infection", "Pneumonia, tuberculosis and diarrhoea in the United States",
         "In 1900 pneumonia, tuberculosis and diarrhoea and enteritis were the leading causes of death, and with diphtheria they caused one-third of all deaths. In 1900, 194 of every 100,000 US residents died of tuberculosis.",
         [("What changed it", "The CDC credits clean water, chlorination, sewage disposal and hygiene education, penicillin from the 1940s and later antimicrobials, and childhood vaccination programmes from the 1950s and 1960s."),
          ("Not a straight line", "Infectious disease mortality rose overall during the 1980s and early 1990s.")],
         "From the CDC's account of 20th-century public health. It is about the United States only, and the page text gives no overall infectious disease death rate for 1900 or 1996."),
    ]),
    ("Length of life", [
        ("1900 to 2023", "Life expectancy", "Living longer",
         "Global life expectancy at birth was 32 years in 1900 and 71 in 2021, according to Our World in Data, which says no region had a life expectancy above 40 in 1800. WHO puts it at 73.4 in 2019, 71.5 in the pandemic low of 2021 and 73.3 in 2023.",
         [("Gap", "In 2021 life expectancy in Nigeria was thirty years lower than in Japan. Hong Kong had the highest female life expectancy, 88 years."),
          ("Healthy years", "Healthy life expectancy was 62.8 in 2023, 0.4 years below its 2019 level.")],
         "The 1900 figure is a reconstruction and differs between sources (the earlier chapter shows 31 to 32 on one page). The 2023 figures are from a news report of WHO's October 2026 estimates."),
        ("2023", "Causes of death", "What people die of now",
         "Heart diseases cause a third of deaths worldwide and cancers almost one in five, together about every second death. Infectious diseases cause around 1 in 7. Neonatal and maternal deaths and accidents each account for about 4%, suicide for 1.3% and interpersonal violence for under 1%.",
         [("Trend", "Death rates from both infectious and non-communicable diseases have fallen since 1990, communicable ones faster.")],
         "From the Global Burden of Disease via Our World in Data. The page gives no percentage for non-communicable diseases as a whole and no figures for how the shares shifted."),
    ]),
]

THIN = [
    ("Healthy years trail total years", "Healthy life expectancy was 62.8 in 2023, against a life expectancy of 73.3. The difference is 10.5 years, my subtraction, and healthy life expectancy was still 0.4 years below its 2019 level.", "WHO, via a news report"),
    ("Resistance to antibiotics is growing", "In 2021 an estimated 4.71 million deaths were associated with bacterial antimicrobial resistance and 1.14 million were attributable to it. The forecast for 2050 is 1.91 million attributable and 8.22 million associated deaths. Deaths in children under 5 fell by more than 50% from 1990 to 2021, while deaths in people over 70 rose by over 80%.", "IHME, Lancet analysis"),
    ("The gains are uneven", "In 2020, 13% of children in Nigeria died before 15, against 0.4% in Italy. In 2021, life expectancy in Nigeria was thirty years lower than in Japan.", "Our World in Data"),
    ("Setbacks have occurred", "The pandemic cut global life expectancy to 71.5 in 2021, and HIV/AIDS reversed child survival in South Africa and Zimbabwe for years. The UN warns that cuts in aid are putting decades of progress in child survival at risk.", "WHO and Our World in Data"),
]

PATTERNS = [
    ("A few named causes account for much of the change", "The entries that carry the largest numbers are infections of childhood and birth: smallpox, polio, tuberculosis, diarrhoea and childbirth. The CDC and Our World in Data both attribute the decline to clean water, vaccines and antibiotics."),
    ("Several gains came from organised campaigns", "Smallpox and polio were attacked by programmes with a target, and the 1980 certification of smallpox elimination is the one finished case in the record."),
    ("Most of the rise in life expectancy falls in the last 125 years", "No region exceeded 40 in 1800, the world averaged 32 in 1900, and it was 71 in 2021. The chapter's data give no 1825 or 1925 figure, so the split at 1925 cannot be tested here."),
    ("The gains depend on a continuing system", "Vaccination needs coverage above 90% for measles, antibiotics lose force as resistance grows, and the UN links aid cuts to disrupted vaccination and clinic closures."),
    ("The gaps between countries remain large", "The sources show a 30-year gap in life expectancy between Nigeria and Japan in 2021, and in 2020 a share of children dying before 15 that was 13% in Nigeria against 0.4% in Italy, about 32 times higher by my division."),
]

LIMITS = [
    "This chapter covers only what could be counted as survival and length of life. It does not measure pain, disability or the quality of care.",
    "The deaths 'prevented' by vaccination and the deaths 'attributable' to resistance are model estimates, not counts.",
    "Early figures are reconstructions. The 1800 and 1900 values rest on thin records, and several are given as ranges or as 'around'.",
    "I did not find world figures for 1825 or 1925, so the two-century split used in earlier chapters cannot be applied here.",
    "The list is a selection of eight gains. It leaves out insulin, anaesthesia, surgery, nutrition and many other advances.",
    "Most figures were read through a summarizing tool from Our World in Data pages, which compile other sources. Check against the original studies before citing.",
]

SRCS = [
    ("Children and mothers", [
        ("https://ourworldindata.org/child-mortality", "Our World in Data, Child mortality", "S"),
        ("https://ourworldindata.org/maternal-mortality", "Our World in Data, Maternal mortality", "S"),
        ("https://www.who.int/news/item/25-03-2025-decades-of-progress-in-reducing-child-deaths-and-stillbirths-under-threat--warns-the-united-nations", "WHO, Decades of progress in reducing child deaths and stillbirths under threat", "P")]),
    ("Diseases", [
        ("https://ourworldindata.org/smallpox", "Our World in Data, Smallpox", "S"),
        ("https://ourworldindata.org/polio", "Our World in Data, Polio", "S"),
        ("https://ourworldindata.org/vaccination", "Our World in Data, Vaccination", "S"),
        ("https://www.cdc.gov/mmwr/preview/mmwrhtml/mm4829a1.htm", "CDC MMWR, Control of infectious diseases", "P"),
        ("https://healthdata.org/node/12105", "IHME, Global burden of bacterial antimicrobial resistance 1990–2021", "P")]),
    ("Length of life", [
        ("https://ourworldindata.org/life-expectancy", "Our World in Data, Life expectancy", "S"),
        ("https://ourworldindata.org/causes-of-death", "Our World in Data, Causes of death", "S"),
        ("https://www.cp24.com/news/world/2026/10/02/life-expectancy-almost-back-to-pre-covid-levels-says-who/", "CP24, Life expectancy almost back to pre-COVID levels, says WHO", "S"),
        ("https://en.wikipedia.org/wiki/Life_expectancy", "Wikipedia, Life expectancy", "S")]),
]

groups, n = groups_html(AREAS)
assert n == 8, n
BODY = (
    section("scale", "How large the gains are", "", stats_html(STATS)
            + chart_block("Share of children dying before age 15, world",
                          "Solid bars are Our World in Data's figures. The 1800 bar is hatched because the page says only 'around 1 in 2'.",
                          chart_html(CH_CHILD, [(0, "0%"), (10, "10%"), (20, "20%"), (30, "30%"), (40, "40%"), (50, "50%")], 50, "Bar chart of share of children dying before 15, from about 50 percent around 1800 to 4 percent in 2020"))
            + chart_block("Mothers dying per 100,000 live births",
                          "Different places and years, so compare the sizes, not a series. Hatched bars are a range or my own division. The 19th-century bar spans 500 to 1,000.",
                          chart_html(CH_MATERNAL, [(0, "0"), (250, "250"), (500, "500"), (750, "750"), (1000, "1,000")], 1000, "Bar chart of maternal deaths per 100,000 live births, from about 900 in Sweden and Finland around 1800 to about 11 in high-income countries in 2017"))
            + chart_block("Life expectancy at birth, world, in years",
                          "Different sources, so the 1900 and 1950 bars are not strictly comparable with the WHO bars. The 1950 bar is a range between two figures.",
                          chart_html(CH_LIFE, [(0, "0"), (20, "20"), (40, "40"), (60, "60"), (80, "80")], 80, "Bar chart of world life expectancy from 32 in 1900 to 73.3 in 2023, and healthy life expectancy of 62.8")))
    + section("gains", "The gains", "Eight entries in three groups. Each gives the scale, what drove it and how solid the figures are.", groups)
    + section("limits-of-gains", "Where the gains thin", "", '<p class="note">These four limits come from the same sources as the entries above.</p>' + cards_html(THIN, "thin", True))
    + section("patterns", "What the record shows", "", '<p class="note">These are my reading of the entries, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or the institution\'s own page. S is a secondary source such as a data compilation, encyclopedia or news report.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Life and Health",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 3 · Gains",
        "@@H1@@": "Life and health",
        "@@SUB@@": "Eight gains in survival and length of life, and where they thin",
        "@@LEDE@@": "Child survival, childbirth, smallpox, polio, vaccination, infection, life expectancy and causes of death. Each entry gives the scale, what drove the change and how solid the figures are, followed by the limits of the gains.",
        "@@ASOF@@": "Figures current to 27 October 2026. Most are from Our World in Data pages and institutions' own reports.",
        "@@NAV@@": nav([("scale", "Scale"), ("gains", "The gains"), ("limits-of-gains", "Where they thin"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several figures are my own arithmetic on the sources: the world maternal ratio of about 216 per 100,000 births (302,700 divided by about 140 million), the 99.4–99.5% fall in estimated polio cases, the 10.5-year gap between life expectancy and healthy life expectancy, and the 32-fold ratio of Nigeria's child death share to Italy's. The observations under “What the record shows” are my own reading.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "life-and-health.html")
    print("ok", n)
