from common import *

# =====================================================================
# CHAPTER 13: LITERACY, WISDOM AND ACCESS TO KNOWLEDGE
# =====================================================================
ACC, ACCD = "#5b6b2f", "#c9d98a"

STATS = [
    ("About 3 points a decade", "gain in test scores of general ability through the 20th century in the United States, the Flynn effect"),
    ("− 15 points", "fall in the average PISA mathematics score between 2018 and 2022, about three-quarters of a year of learning"),
    ("Over 40%", "fall in the share of Americans reading for pleasure on a given day, 2003 to 2023"),
    ("70%", "of 10-year-olds in low- and middle-income countries could not read and understand a simple text in 2022"),
]

CH_FLYNN = [
    ("US, Wechsler scales", "About 3 points a decade, 20th century", 0, 3, False, None),
    ("US, Trahan et al. 2014", "2.93 points a decade", 0, 2.93, False, None),
    ("Dutch conscripts, 1952–1982", "21 points in 30 years", 0, 7, False, None),
    ("Denmark, 1959–1979", "About 3", 0, 3, False, None),
    ("Denmark, 1979–1989", "Nearly 2", 0, 2, True, None),
    ("Denmark, 1989–1998", "About 1.3", 0, 1.3, False, None),
    ("WAIS-5 comparison, Winter et al. 2024", "About 1.2, against about 3 expected", 0, 1.2, False, None),
]
CH_LP = [
    ("2015", "53%, an earlier estimate", 0, 53, False, None),
    ("Before the pandemic", "57%, on revised data", 0, 57, False, None),
    ("2022", "70% in low- and middle-income countries", 0, 70, False, None),
    ("Sub-Saharan Africa, 2022", "89%", 0, 89, False, None),
    ("Latin America and the Caribbean", "From about 50% to a predicted 80%", 0, 80, True, None),
    ("South Asia", "From 60% to a predicted 78%", 0, 78, True, None),
]
CH_PISA = [
    ("Average, mathematics, 2018 to 2022", "A fall of 15 points; 20 points is about one year of learning", 0, 15, False, None),
    ("Germany, Iceland, Netherlands", "Each fell 25 points or more", 0, 25, True, None),
]

AREAS = [
    ("Measured gains", [
        ("20th century to mid-1990s", "Test scores", "Scores on intelligence tests rose for decades",
         "In the United States average scores on the Wechsler scales rose by about three IQ points a decade, and Trahan and colleagues put it at 2.93 a decade in 2014. Dutch conscripts gained 21 points over 30 years, 1952 to 1982, and British children on Raven's Progressive Matrices gained 14 points from 1942 to 2008. Gains were continuous and roughly linear from the earliest testing to the mid-1990s.",
         [("Proposed causes", "Schooling, at 1 to 5 points for each extra year, nutrition, falling lead exposure, less infectious disease and a more visual, abstract environment. No single cause is agreed."),
          ("Meaning", "Whether intelligence itself has risen is still controversial, the gains may reflect test-specific skills, and school-content subtests such as vocabulary and arithmetic changed little.")],
         "From Wikipedia's article on the Flynn effect, which cites the studies. Gains were concentrated at the lower end in some studies, and the sizes differ between tests and countries."),
        ("1820 to now", "Reading", "Reading became the norm",
         "About 1 in 10 people could read and write in 1820, and about 88% of adults and 93% of 15 to 24 year olds can now, on UNESCO figures as reported. Chapter 5 gives the series, the definitions and the 739 million adults who still lack basic literacy.",
         [],
         "Repeats Chapter 5, where the early figures are described as soft and the UNESCO figures come from a news report."),
    ]),
    ("Signs of slipping", [
        ("1962 to 2008", "Reversal of the gains", "In several rich countries the rise stopped, then fell",
         "In Norway gains in general intelligence among conscripts stopped after the mid-1990s and numerical reasoning declined. Bratsberg and Rogeberg found that for men born 1962 to 1991 the rise, its turning point and the decline all appear within families, and they found no support for explanations based on genes or on factors that differ between families. In Denmark conscripts gained about 3 points a decade from 1959 to 1979 and about 1.3 from 1989 to 1998, then lost about as much between 1998 and 2004. In the UK the average 14 year old's score fell by more than two points between 1980 and 2008.",
         [("Not everywhere", "Winter and colleagues found gains of about 1.2 points a decade in a 2024 comparison, rather than the 3 expected. Gonthier and colleagues argue there is no negative Flynn effect in France, and that tests based on cultural knowledge can misstate variation."),
          ("Australia", "No rise in the scores of 6 to 12 year olds from 1975 to 2003.")],
         "Norway's data cover only men, with women's scores approximated from years of schooling. The page gives no figures for Finland or France and the reversals are for specific tests and cohorts."),
        ("2018 to 2022", "School tests", "PISA 2022",
         "The average international score in mathematics fell by 15 points between 2018 and 2022, about three-quarters of a year of learning, and reading fell by about half a year. Science stayed about the same. The survey covered 81 countries and regions, and Germany, Iceland and the Netherlands each fell by 25 points or more in mathematics. Singapore ranked first.",
         [("Cause", "School closures in the pandemic are likely part of it, but the OECD said it is not just about Covid and that long-term issues in education systems are also to blame. The report does not say how much belongs to each.")],
         "From a news report of the OECD's results. It gives no point figure for reading and does not say whether the average is for the OECD alone."),
        ("2012 to 2023", "Adult skills", "Adults' literacy and numeracy",
         "The OECD's second Survey of Adult Skills covered 31 countries and about 160,000 adults aged 16 to 65, with 27 countries also in the first survey. Only Finland and Denmark improved significantly in literacy, and most other countries declined or stayed flat. The lowest 10% fell in most countries while the top 10% rose. About one in five adults can only understand simple texts or do basic arithmetic.",
         [("Who", "Declines were larger among low-educated adults. In some places a rising share of foreign-born adults, who score lower, explains part of the fall. Men's literacy fell more than women's."),
          ("Numeracy", "Eight countries raised their averages, Finland and Singapore the most.")],
         "From a news summary of the OECD's press release. I could not read the press release itself, and the summary gives no exact count of countries that declined."),
        ("2003 to 2023", "Reading habits", "Reading for pleasure",
         "A study of the American Time Use Survey, over 236,000 Americans, found the share reading for pleasure on a given day fell by more than 40% over 20 years, a steady decline of about 3% a year. It was published in iScience in August 2025.",
         [],
         "A university's news release of the study. It gives no starting level and covers the United States only."),
        ("2022", "Learning poverty", "Children who cannot read a simple text",
         "The World Bank and UNICEF estimated in June 2022 that 70% of 10-year-olds in low- and middle-income countries could not read and understand a simple text, up from 57% before the pandemic. The rate was 89% in sub-Saharan Africa, and was predicted to rise from about 50% to 80% in Latin America and the Caribbean and from 60% to 78% in South Asia.",
         [("Definition", "Learning poverty is the share of 10-year-olds who cannot read and understand a simple text.")],
         "A UNICEF press release of the estimate. Parts are predictions for the pandemic's effect, and the pre-pandemic figure is a revised one against an earlier estimate of 53% for 2015."),
    ]),
    ("What cannot be measured", [
        ("No date", "Wisdom", "Wisdom has no agreed measure",
         "There is no scientific consensus on the definition of wisdom. Baltes's Berlin Wisdom Paradigm describes five components, among them factual and procedural knowledge of life matters and an apprehension of uncertainty. Sternberg's balance theory calls it the value-laden application of tacit knowledge to attain a common good. It is measured by self-report scales, which are prone to bias, by indices such as the Jeste-Thomas Wisdom Index, and by contextual measures of cognition, motivation and emotion in specific situations.",
         [("Over time", "I found no series that tracks wisdom over a century or even a decade.")],
         "From Wikipedia. The page itself says the usefulness of the shortest scales is increasingly questioned."),
    ]),
]

THIN = [
    ("The tests may not measure intelligence", "The Flynn gains were largest on tests of abstract and visual reasoning and small on vocabulary and arithmetic, and Neisser calls it controversial whether intelligence itself has risen.", "Wikipedia"),
    ("The reversals are partial", "Norway's data cover only men, Denmark's cover conscripts, and no reversal is shown for France or Australia. Scores are for particular tests and cohorts.", "Wikipedia"),
    ("The causes are not settled", "The OECD says the PISA fall is not just Covid, while Bratsberg and Rogeberg find the Norwegian rise and fall both appear within families, which rules out some explanations and does not name the cause.", "OECD, via a news report; PNAS"),
    ("Many pages are second-hand", "The PISA, adult skills and reading figures come from news summaries and a press release, and none was read in its full report.", "News reports; university release"),
]

PATTERNS = [
    ("The evidence points both ways, by measure", "Test scores rose for most of the 20th century and the reading rate rose from 1 in 10 to 88%. Several recent measures fell: the Flynn gains reversed in some countries, PISA mathematics dropped, adult literacy fell or stayed flat in most surveyed countries and reading for pleasure fell in the United States."),
    ("Where the evidence falls, it does not fall everywhere", "Finland and Denmark improved in adult literacy, Finland and Singapore in numeracy, Singapore led PISA 2022, and the top 10% of adults gained while the lowest 10% fell. The picture is one of widening gaps in some places, not a uniform decline."),
    ("Access and ability are separate things", "Chapter 5 shows access to schooling and the internet rising, yet 70% of 10-year-olds in low- and middle-income countries could not read a simple text in 2022 and about 1 in 5 adults in the surveyed countries read only simple texts."),
    ("The question asks about wisdom, which cannot be measured", "No agreed definition or series exists, so 'dumbed down' can be tested only on the narrower measures of tests, skills and reading, and they give a mixed answer."),
    ("The data do not reach back to 1925 on most measures", "The Flynn series start in the 1940s and 1950s, the literacy series in 1820, PISA in 2018 and the adult skills survey in 2012, so the two centuries cannot be compared."),
]

LIMITS = [
    "Wisdom, judgement and the use of knowledge have no accepted measure, and nothing here tracks them over time.",
    "Test scores measure particular skills at particular dates. Tests change, and so do the people who take them, including through migration.",
    "Most of the reversal evidence is from a few rich countries, and most of the learning evidence for poorer countries is from one estimate.",
    "Several figures are news reports of reports and of studies. I could not read the OECD adult skills press release or the PNAS article and used a summary of each.",
    "Not covered: critical thinking, belief in misinformation, civic knowledge, the effect of search engines and artificial intelligence, and how people judge what they read.",
    "The chapter weighs evidence on one side and the other and does not reach a verdict on the question.",
]

SRCS = [
    ("Ability and skills", [
        ("https://en.wikipedia.org/wiki/Flynn_effect", "Wikipedia, Flynn effect", "S"),
        ("https://frisch.uio.no/english/publications/?pubid=1372", "Frisch Centre, Bratsberg and Rogeberg, Flynn effect and its reversal are both environmentally caused (PNAS 2018)", "P"),
        ("https://www.aljazeera.com/news/2023/12/5/unprecedented-decline-in-global-literacy-scores-osce-report-says", "Al Jazeera, Unprecedented decline in global literacy scores (OECD PISA 2022)", "S"),
        ("https://www.developmentaid.org/news-stream/post/189000/adult-skills-numeracy-declining", "DevelopmentAid, Adult skills in literacy and numeracy declining or stagnating (OECD 2024)", "S"),
        ("https://www.unicef.org/press-releases/70-cent-10-year-olds-learning-poverty-unable-read-and-understand-simple-text", "UNICEF, 70 per cent of 10-year-olds in learning poverty", "P")]),
    ("Reading and wisdom", [
        ("https://news.ufl.edu/2025/08/reading-for-pleasure-study/", "University of Florida, Reading for pleasure in free fall", "P"),
        ("https://en.wikipedia.org/wiki/Wisdom", "Wikipedia, Wisdom", "S"),
        ("https://ourworldindata.org/literacy", "Our World in Data, Literacy (see also Chapter 5)", "S")]),
]

groups, n = groups_html(AREAS)
assert n == 8, n
BODY = (
    section("scale", "The evidence at a glance", "", stats_html(STATS)
            + chart_block("Gains in test scores, IQ points a decade",
                          "Estimates of the Flynn effect from different tests, countries and periods. The Dutch bar is my division of 21 points over 30 years. The hatched Danish bar is 'nearly 2'.",
                          chart_html(CH_FLYNN, [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8")], 8, "Bar chart of Flynn effect gains in points per decade for several tests and countries, from 1.2 to 7"))
            + chart_block("Fall in PISA mathematics, 2018 to 2022, points",
                          "As reported. The second bar is hatched because the report gives 'a fall of 25 points or more'.",
                          chart_html(CH_PISA, [(0, "0"), (10, "10"), (20, "20"), (30, "30")], 30, "Bar chart of the fall in PISA mathematics scores between 2018 and 2022"))
            + chart_block("Learning poverty: 10-year-olds unable to read a simple text",
                          "World Bank and UNICEF estimates for low- and middle-income countries. Hatched bars are predictions.",
                          chart_html(CH_LP, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of learning poverty rates from 53 percent in 2015 to 70 percent in 2022 and 89 percent in sub-Saharan Africa")))
    + section("entries", "The evidence", "Eight entries in three groups: measured gains, signs of slipping, and what cannot be measured. Each gives the scale, the cause where the source gives one and how solid the figures are.", groups)
    + section("strains", "Where the evidence is weak", "", '<p class="note">These four points come from the same sources as the entries above.</p>' + cards_html(THIN, "thin", True))
    + section("patterns", "What the evidence shows", "", '<p class="note">These are my reading of the entries, not findings from the sources. This chapter does not give a verdict on whether people have dumbed down.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or the institution\'s own page. S is a secondary source such as an encyclopedia or news report.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Literacy, Wisdom and Knowledge",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 13 · How people live",
        "@@H1@@": "Have people dumbed down?",
        "@@SUB@@": "Literacy, test scores, reading and wisdom, with evidence on both sides of the question",
        "@@LEDE@@": "Access to knowledge has spread widely. Whether people have become wiser or less so is a different question, and wisdom has no accepted measure. This chapter sets the measurable evidence on each side and does not give a verdict.",
        "@@ASOF@@": "Figures current to 27 October 2026. Several come from news reports of OECD and other studies.",
        "@@NAV@@": nav([("scale", "At a glance"), ("entries", "The evidence"), ("strains", "Where it is weak"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several figures are my own arithmetic or reading of the sources' wording: the Dutch gain of about 7 points a decade (21 points over 30 years), and the plotting of 'nearly 2' and 'a fall of 25 points or more' as 2 and 25. The observations under “What the evidence shows” are my own reading.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "literacy-wisdom-knowledge.html")
    print("ok", n)
