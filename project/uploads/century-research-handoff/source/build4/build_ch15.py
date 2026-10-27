from common import *

# =====================================================================
# CHAPTER 15: POWER AND GOVERNANCE
# =====================================================================
ACC, ACCD = "#1d3f8a", "#8fb0f0"

STATS = [
    ("74%", "of the world's people live in autocracies, about 6 billion, on the V-Dem Institute's 2026 count"),
    ("20th year", "in a row that Freedom House found global freedom declined, in 2025"),
    ("25-year low", "for the average score in Reporters Without Borders' press freedom index, 2026"),
    ("122 of 182", "countries score below 50 out of 100 on Transparency International's 2025 corruption index"),
]

CH_POP = [
    ("In autocracies", "About 6 billion people", 0, 74, False, None),
    ("In democracies", "26% in all", 0, 26, False, None),
    ("In liberal democracies", "About 7%, roughly 600 million", 0, 7, False, None),
    ("In countries autocratizing", "41%, in 44 countries", 0, 41, False, None),
    ("In countries democratizing", "5%, in 18 countries", 0, 5, False, None),
]
CH_REG = [
    ("Electoral autocracies", "57 countries", 0, 57, False, None),
    ("Electoral democracies", "56 countries", 0, 56, False, None),
    ("Closed autocracies", "35 countries", 0, 35, False, None),
    ("Liberal democracies", "31 countries", 0, 31, False, None),
]
Y0 = 1880
CH_VOTE = [
    ("New Zealand", "1893, national, the first", 0, 1893 - Y0, False, None),
    ("United Kingdom", "1918 for some women; 1928 on the same terms as men", 0, 1928 - Y0, False, None),
    ("United States", "1920, with the 19th Amendment", 0, 1920 - Y0, False, None),
    ("India", "1921 in Bombay and Madras; 1929 in all provinces", 0, 1929 - Y0, False, None),
    ("France", "1944, first elections in 1945", 0, 1944 - Y0, False, None),
    ("Switzerland", "1971 federal; some cantons 1959 to 1990", 0, 1971 - Y0, False, None),
    ("Saudi Arabia", "2015, local elections", 0, 2015 - Y0, False, None),
]
VOTE_TICKS = [(1900 - Y0, "1900"), (1950 - Y0, "1950"), (2000 - Y0, "2000")]
CH_PRESS = [
    ("2002", "13.7% of countries rated difficult or very serious", 0, 13.7, False, None),
    ("2026", "52.2% of 180 countries and territories", 0, 52.2, False, None),
]

AREAS = [
    ("Who rules and who votes", [
        ("1800 to 2025", "Regimes", "From closed autocracy to electoral democracy and back",
         "Our World in Data, using the Regimes of the World classification, says almost everyone in 1800 lived under closed autocracies, with about 20 million people in electoral autocracies, which it names as the UK and US. Electoral and liberal democracy spread widely in the 20th century, especially in its second half. The world was at its democratic all-time high in the early 2010s and has fallen since. By 2025 about 1.6 billion people lived in electoral democracies and another 600 million in liberal democracies.",
         [("Totals", "The page says population growth outpaced democratic expansion, so the number of people without democratic rights is higher than ever, with many in China."),
          ("Classification", "RoW reclassified India as an electoral autocracy in 2017, while other sources agree it has become less democratic but still count it as a democracy.")],
         "One classification among several, which the page says sometimes sort countries differently. It gives no share of the world's people in 1900 or 1950, and no count of countries by regime for 2025."),
        ("2025", "Democracy", "The V-Dem count for 2025",
         "The V-Dem Institute's 2026 report, as reported, says democracy for the average person has fallen back to the level of 1978. Of 179 countries, 87 are democracies, 31 of them liberal and 56 electoral, and 92 are autocracies, 57 electoral and 35 closed. An estimated 74% of the world's people, about 6 billion, live in autocracies and 26% in democracies. 44 countries, with 41% of the world's population, are autocratizing, and 18, with 5%, are democratizing.",
         [],
         "A news report of V-Dem's report, covering developments through 2025. I did not read the report, and V-Dem's method differs from the Regimes of the World classification above."),
        ("2025", "Freedom", "Freedom House for 2025",
         "Freedom House's Freedom in the World 2026 report says global freedom declined for the 20th consecutive year in 2025. 54 countries saw their political rights and civil liberties deteriorate and only 35 improved. 88 countries are rated Free.",
         [],
         "From Freedom House's own press release. It gave no current count of Partly Free and Not Free countries."),
        ("1893 to 2015", "Women's vote", "When women won the vote",
         "New Zealand granted women the national vote first, in 1893. The United States did so in 1920, Britain in 1918 for some women and in 1928 on the same terms as men, India in 1921 in two provinces and 1929 in all provinces, and France in 1944. Women could vote at the federal level in Switzerland from 1971 and in Saudi Arabia's local elections from 2015.",
         [("Not voting", "The page lists Vatican City and Eritrea as having no voting, and notes that some countries have suspended national elections.")],
         "From Wikipedia. The dates are for the vote, which in several places was partial or limited by race, region or class. The page gives no count of countries with women's suffrage in any year."),
    ]),
    ("Checks on power", [
        ("2002 to 2026", "Press", "Press freedom at a 25-year low",
         "Reporters Without Borders says the average score of all countries assessed in its 2026 index has never been so low in 25 years. 52.2% of countries and territories are rated difficult or very serious, against 13.7% in 2002, and less than 1% of the world's population lives in a country rated good.",
         [("Count", "52.2% of 180 is about 94 countries, my calculation.")],
         "From RSF's own page. It gives no global average score and no count of countries in each category, and I did not use its journalist-casualty figures."),
        ("2025", "Corruption", "Perceived corruption",
         "Transparency International's 2025 index, scored from 0 to 100 with lower meaning more perceived public-sector corruption, gives a global average of 42, the lowest in a decade. 122 of 182 countries score below 50. Denmark is first with 89 for the eighth year, and Somalia and South Sudan share last place with 9. 50 countries have declined since 2012.",
         [("Examples", "Declining examples include the US at 64, Canada at 75 and France at 66, while Estonia (76), South Korea (63) and Bhutan (71) are cited as consistent improvers.")],
         "A law-firm summary of the index. The index measures perceptions of corruption, not corruption itself, and the summary's statement of an 8-point drop in the average looks wrong, so I left it out."),
        ("2011", "Institutions", "States and the United Nations",
         "The United Nations now lists 193 member states, the most recent being South Sudan, admitted on 14 July 2011.",
         [],
         "Thin. The page gives the count and the latest member only, and I found no figure for the number of independent states in 1825 or 1925."),
    ]),
]

THIN = [
    ("Democracy has slipped back", "V-Dem says democracy for the average person has fallen to its 1978 level, and OWID says the world peaked in the early 2010s. 44 countries, holding 41% of the world's people, are autocratizing.", "V-Dem, via a news report; Our World in Data"),
    ("Freedom has fallen for 20 years", "Freedom House found that more countries declined than improved in 2025, 54 against 35, the 20th consecutive year of overall decline.", "Freedom House"),
    ("Press freedom and corruption scores are low", "RSF's 2026 average is the lowest in 25 years and half of countries rate difficult or very serious. Transparency International's average of 42 is the lowest in a decade.", "RSF; Transparency International, via a summary"),
    ("The vote came late to many", "Women gained the national vote between 1893 in New Zealand and 1971 in Switzerland among the examples, and 2015 in Saudi Arabia's local elections.", "Wikipedia"),
]

PATTERNS = [
    ("Four independent measures point the same way for recent years", "V-Dem, Freedom House, RSF and Transparency International all report decline in the latest year or decade, with different methods and different data. That is agreement in direction, not in size."),
    ("Counting countries and counting people give different answers", "The world is about evenly split between democracies and autocracies by country, but V-Dem puts 74% of people in autocracies, because the populous countries weigh heavily, with China named by OWID."),
    ("The spread of the vote took more than a century", "Among the examples, women's suffrage spans 1893 to 2015, and Switzerland's federal vote in 1971 came after France's in 1944."),
    ("Classification is part of the story", "India was reclassified in 2017 by one system and still counted a democracy by others, so the headline counts depend on whose rules are used."),
    ("No series here compares 1925 with now", "The regime shares start in 1800 and 2025 and the other indexes begin in 2002 or later, so the two centuries cannot be compared on these figures."),
]

LIMITS = [
    "Governance indexes rest on expert judgement and perceptions, and different systems classify the same country differently.",
    "The V-Dem, Transparency International and Freedom House figures are partly from news reports and summaries. I read the Freedom House and RSF pages directly but not the full reports.",
    "I found no count of independent states, or of democracies, for 1825 or 1925.",
    "The chapter does not cover military power, nuclear weapons, state capacity, surveillance or the power of firms, and it does not measure whether people trust their governments.",
    "The women's suffrage dates describe the law and not who could vote in practice.",
    "The list is seven entries, a selection and not a full account of governance.",
]

SRCS = [
    ("Who rules and who votes", [
        ("https://ourworldindata.org/democracy", "Our World in Data, Democracy", "S"),
        ("https://www.democracywithoutborders.org/41651/v-dem-report-finds-global-democracy-is-back-at-1978-levels/", "Democracy Without Borders, V-Dem report finds global democracy is back at 1978 levels", "S"),
        ("https://freedomhouse.org/article/new-report-global-freedom-declined-20th-consecutive-year-2025", "Freedom House, Global freedom declined for the 20th consecutive year", "P"),
        ("https://en.wikipedia.org/wiki/Women%27s_suffrage", "Wikipedia, Women's suffrage", "S")]),
    ("Checks on power", [
        ("https://rsf.org/en/2026-rsf-index-press-freedom-25-year-low", "Reporters Without Borders, 2026 RSF Index", "P"),
        ("https://www.hsfkramer.com/zh_HK/notes/fsrandcorpcrime/2026-posts/transparency-international-publishes-the-cpi-2025", "Herbert Smith Freehills Kramer, Transparency International publishes the CPI 2025", "S"),
        ("https://www.un.org/en/about-us/member-states", "United Nations, Member States", "P")]),
]

groups, n = groups_html(AREAS)
assert n == 7, n
BODY = (
    section("scale", "The picture", "", stats_html(STATS)
            + chart_block("Share of the world's people, V-Dem 2026 count",
                          "As reported for developments through 2025. The first two bars add to 100%. The last two count people in countries that are moving, so they overlap the others.",
                          chart_html(CH_POP, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of share of world population in autocracies, democracies and countries autocratizing or democratizing"))
            + chart_block("Countries by regime type, V-Dem 2026, out of 179",
                          "Number of countries in each type.",
                          chart_html(CH_REG, [(0, "0"), (20, "20"), (40, "40"), (60, "60")], 60, "Bar chart of countries by regime type: 57 electoral autocracies, 56 electoral democracies, 35 closed autocracies, 31 liberal democracies"))
            + chart_block("Press freedom: share of countries rated difficult or very serious",
                          "Reporters Without Borders. The share was 13.7% in 2002 and 52.2% in 2026.",
                          chart_html(CH_PRESS, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%")], 75, "Bar chart of share of countries with difficult or very serious press freedom in 2002 and 2026"))
            + chart_block("When women won the national vote",
                          "Each bar runs from 1880 to the year shown. Several dates were partial or applied to some regions or elections only, as labelled.",
                          chart_html(CH_VOTE, VOTE_TICKS, 145, "Bar chart of years women won the national vote in seven countries, from 1893 to 2015")))
    + section("entries", "Power and governance", "Seven entries in two groups. Each gives the scale, what the source says about change and how solid the figures are.", groups)
    + section("strains", "Where the record is hard", "", '<p class="note">These four points come from the same sources as the entries above.</p>' + cards_html(THIN, "thin", True))
    + section("patterns", "What the record shows", "", '<p class="note">These are my reading of the entries, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or the institution\'s own page. S is a secondary source such as a compilation, summary or news report.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Power and Governance",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 15 · How people live",
        "@@H1@@": "Power and governance",
        "@@SUB@@": "Seven entries on regimes, votes, freedom, the press, corruption and the United Nations",
        "@@LEDE@@": "Who rules, who votes, and what checks the rulers. The sources give the present and long-run regime shares from 1800, but the other indexes begin in 2002 or later.",
        "@@ASOF@@": "Figures current to 27 October 2026. Several come from news reports of the V-Dem and Transparency International reports.",
        "@@NAV@@": nav([("scale", "The picture"), ("entries", "Power and governance"), ("strains", "Where it is hard"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several statements are my own arithmetic: that 52.2% of 180 countries is about 94, and the bar chart of voting years, which plots the year as a distance from 1880. The observations under “What the record shows” are my own reading.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "power-and-governance.html")
    print("ok", n)
