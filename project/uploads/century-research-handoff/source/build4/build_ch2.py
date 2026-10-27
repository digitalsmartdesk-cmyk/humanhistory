import math
from common import *

# =====================================================================
# CHAPTER 2: PACE OF CHANGE
# =====================================================================
ACC, ACCD = "#a02a68", "#e79ac0"

STATS = [
    ("121 → 12 years", "to add each billion people: the second billion (1805–1926) against each of the fifth to eighth (1974–2022)"),
    ("About 2.6% a year", "growth in world output in both 1900–1925 and 1925–1950, on one reconstruction; 0.74% a year in 1500–1900"),
    ("× 10 in a century", "world energy supply from 1900 to 2000, against × 2.1 from 1800 to 1900"),
    ("6 to 43 years", "for a US household technology to go from 10% to about 50% of homes, with no steady trend over time"),
]

# chart: GWP growth (hatched: my arithmetic)
CH_GWP = [
    ("1 CE – 1000", "18.50 → 35.31 billion 1990 international dollars", 0, 0.065, True, None),
    ("1000 – 1500", "35.31 → 58.67", 0, 0.102, True, None),
    ("1500 – 1900", "58.67 → 1,102.96", 0, 0.736, True, None),
    ("1900 – 1925", "1,102.96 → 2,102.88", 0, 2.61, True, None),
    ("1925 – 1950", "2,102.88 → 4,081.81", 0, 2.69, True, None),
]
# chart: years per billion (solid; stated by source)
CH_BILL = [
    ("2nd billion", "1805 – 1926", 0, 121, False, None),
    ("3rd billion", "1926 – 1960", 0, 34, False, None),
    ("4th billion", "1960 – 1974", 0, 14, False, None),
    ("5th billion", "1974 – 1986", 0, 12, False, None),
    ("6th billion", "1986 – 1998", 0, 12, False, None),
    ("7th billion", "1998 – 2010", 0, 12, False, None),
    ("8th billion", "2010 – 2022", 0, 12, False, None),
    ("9th billion", "2022 – 2037, projected", 0, 15, True, None),
    ("10th billion", "2037 – 2060, projected", 0, 23, True, None),
]
# chart: years from 10% to ~50% of US households (hatched: my subtraction)
CH_ADOPT = [
    ("Landline telephone", "1903 → 1946", 0, 43, True, None),
    ("Electric power", "1908 → 1925", 0, 17, True, None),
    ("Automobile", "1915 → 1926", 0, 11, True, None),
    ("Radio", "1925 → 1931", 0, 6, True, None),
    ("Refrigerator", "About 1930 → 1938", 0, 8, True, None),
    ("Cell phone", "1994 → 2002 (56%)", 0, 8, True, None),
    ("Internet", "1993 → 2002 (52%)", 0, 9, True, None),
]
# chart: Atlantic crossing, log scale in hours
def L(h): return math.log10(h)
CH_CROSS = [
    ("Packet, westbound average", "40 days; years not stated", 0, L(40 * 24), True, None),
    ("Packet, eastbound average", "23 days; years not stated", 0, L(23 * 24), True, None),
    ("Great Western, westbound, 1838", "15 d 12 h", 0, L(15 * 24 + 12), False, None),
    ("Mauretania, eastbound, 1924", "5 d 1 h 49 min", 0, L(5 * 24 + 1 + 49 / 60), False, None),
    ("Lindbergh, 1927", "About 33.5 h", 0, L(33.5), False, None),
    ("Fastest airliner crossing, 2020", "4 h 56 min, with a tailwind", 0, L(4 + 56 / 60), False, None),
    ("Concorde, scheduled, westbound", "About 3 h 15 min", 0, L(3.25), True, None),
]
CROSS_TICKS = [(0, "1"), (1, "10"), (2, "100"), (3, "1,000")]
# chart: energy
CH_ENERGY = [
    ("1800", "5,653 TWh, 98% traditional biomass", 0, 5653, False, None),
    ("1850", "7,791 TWh", 0, 7791, False, None),
    ("1900", "12,131 TWh", 0, 12131, False, None),
    ("1950", "28,564 TWh", 0, 28564, False, None),
    ("2000", "122,288 TWh", 0, 122288, False, None),
    ("2024", "186,383 TWh", 0, 186383, False, None),
]

COMP_COLS = ["Earlier window", "Later window", "How to read it"]
COMP = [
    ("World population",
     "About 983 million in 1800 to 2 billion in 1926: × 2.0 in 126 years.",
     "2 billion in 1926 to 8 billion in 2022: × 4.0 in 96 years.",
     "Windows are 1800–1926 and 1926–2022, not 1825–1925 and 1925–2025. The source puts the second billion at 1926 in text and 1927 in a chart."),
    ("World energy supply",
     "1800 to 1900: × 2.15, about 0.77% a year.",
     "1900 to 2000: × 10.1, about 2.3% a year. Within it: 1900–1950 × 2.35 (1.7% a year) and 1950–2000 × 4.28 (3.0% a year). 2000–2024: × 1.52 (1.8% a year).",
     "The data has no 1825 or 1925 value, so the windows are shifted by a quarter-century. The faster pace begins after 1950, not after 1925."),
    ("World output (GWP)",
     "No 1825 value in the table I read. 1500 to 1900: × 18.8, 0.74% a year.",
     "1925 to 1950: × 1.94, 2.69% a year. The table I read ends in 1950.",
     "1900–1925 grew 2.61% a year and 1925–1950 2.69%, so this series shows no change of pace at 1925. Both quarter-centuries include a world war."),
    ("Atlantic crossing time",
     "Westbound packet average, 40 days, to the 1924 Mauretania, 5 d 1 h 49 min: about × 7.9 faster.",
     "The 1924 Mauretania to the fastest 2020 airliner crossing, 4 h 56 min: about × 24.7 faster.",
     "The second step replaces a ship by an aircraft, so it measures a change of method as much as of speed. The eastbound packet average gives × 4.5 for the first step."),
    ("Spread of a household machine, 10% to about 50% of US homes",
     "Telephone 43 years, electric power 17, automobile 11.",
     "Radio 6, refrigerator 8, cell phone 8, internet 9.",
     "Radio and the refrigerator, in the 1920s and 30s, were already as fast as the cell phone and internet. Speed did not keep rising."),
]

READINGS = [
    ("Population is the clearest acceleration, and it comes after 1925",
     "It took 121 years to add the second billion and 34 for the third, then 12 each for the fifth to eighth. The projections lengthen again, to about 15 and 23 years. The time per billion has stayed at 12 years since 1974, so the fastest pace is a plateau of the late 20th and early 21st centuries."),
    ("Output growth shows no step at 1925",
     "On the DeLong reconstruction, world output grew about 2.6% a year in 1900–1925 and 2.7% in 1925–1950, against 0.74% a year over 1500–1900. The step up sits between the long pre-1900 average and the 20th century. I have no 1825 value and no value after 1950 from this series, so I cannot place the start of the step within the 19th century."),
    ("Energy speeds up after 1950",
     "Energy supply grew about 1.7% a year from 1900 to 1950 and about 3.0% from 1950 to 2000. From 2000 to 2024 it grew 1.8% a year, below the 1950–2000 rate. The measure is a rise in use, not a count of inventions."),
    ("The spread of household machines did not keep getting faster",
     "From 10% to about 50% of US homes, the telephone took 43 years and electric power 17. Radio took 6 in the 1920s and 30s, the refrigerator about 8, and the cell phone and the internet 8 and 9 around the turn of the 21st century. The fastest cases are spread across both centuries."),
    ("What the evidence supports",
     "My reading: the last century was faster than the one before on population, energy, output and travel time, but the measures do not change pace at the same date, and the speed of household adoption shows no trend. Output changes near 1900, population after 1926, energy after 1950, and travel time with the change from ship to aircraft. A neat split at 1925 describes none of them exactly."),
]
READING_NOTE = "These are my reading of the series and my arithmetic on them, not findings from the sources."

LIMITS = [
    "Almost every rate here is my own arithmetic on two endpoints. A compound annual rate hides movement inside the window, including the effect of the two world wars on the 1900–1950 figures.",
    "The windows differ from 1825–1925 and 1925–2025 because the series do not have those years. Each row states the years it uses.",
    "The world output series is a reconstruction in 1990 international dollars, with long gaps early on. I read only the six dates the Wikipedia table gives, and none after 1950.",
    "The household adoption series is for the United States only, and the 50 percent year is the nearest value I read for the colour television, cell phone and internet rows.",
    "The crossing times combine different ships, routes and measures, and the sailing averages have no stated year. They show orders of magnitude, not a tidy series.",
    "Pace is measured here by what could be counted. Changes in ideas, institutions or ways of working have no series in this chapter.",
]

SRCS = [
    ("Population, energy and output", [
        ("https://ourworldindata.org/population-growth-over-time", "Our World in Data, World population growth", "S"),
        ("https://ourworldindata.org/grapher/global-energy-substitution", "Our World in Data, Global energy substitution (data file used for the 1800–2024 values)", "S"),
        ("https://en.wikipedia.org/wiki/Gross_world_product", "Wikipedia, Gross world product (DeLong 1998 table)", "S")]),
    ("Household technology", [
        ("https://ourworldindata.org/technology-adoption", "Our World in Data, Technology adoption", "S")]),
    ("Crossing times", [
        ("https://en.wikipedia.org/wiki/Black_Ball_Line_(trans-Atlantic_packet)", "Wikipedia, Black Ball Line (trans-Atlantic packet)", "S"),
        ("https://en.wikipedia.org/wiki/Blue_Riband", "Wikipedia, Blue Riband", "S"),
        ("https://en.wikipedia.org/wiki/Transatlantic_flight", "Wikipedia, Transatlantic flight", "S")]),
]

BODY = (
    section("scale", "At a glance", "", stats_html(STATS)
            + chart_block("Years taken to add each billion people",
                          "Solid bars are the figures as the source gives them. Hatched bars are the source's projections. The first billion took all of history until 1805.",
                          chart_html(CH_BILL, [(0, "0"), (30, "30"), (60, "60"), (90, "90"), (120, "120")], 125, "Bar chart of years taken to add each billion people, from 121 years for the second billion to 12 years for the fifth to eighth"))
            + chart_block("Growth in world output, percent a year",
                          "Each bar is my compound annual rate between the two dates of the DeLong reconstruction, so all bars are hatched. The 1900–1925 and 1925–1950 bars are close.",
                          chart_html(CH_GWP, [(0, "0%"), (1, "1%"), (2, "2%"), (3, "3%")], 3, "Bar chart of world output growth rates, from 0.065 percent a year to 2.69 percent a year"))
            + chart_block("World energy supply, terawatt-hours",
                          "Substituted energy, as one series, in terawatt-hours. The 1800 value is almost all traditional biomass; the 2024 value includes coal, oil, gas, hydro, nuclear and other renewables.",
                          chart_html(CH_ENERGY, [(0, "0"), (50000, "50,000"), (100000, "100,000"), (150000, "150,000")], 200000, "Bar chart of world energy supply in 1800, 1850, 1900, 1950, 2000 and 2024"))
            + chart_block("Years for a US household technology to go from 10 percent to about 50 percent of homes",
                          "Each bar is my subtraction of the two years shown. Cell phone and internet use the nearest value above 50 percent (56 and 52).",
                          chart_html(CH_ADOPT, [(0, "0"), (10, "10"), (20, "20"), (30, "30"), (40, "40")], 45, "Bar chart of years from 10 percent to about 50 percent of US households for seven technologies"))
            + chart_block("Time to cross the Atlantic, hours, on a log scale",
                          "Each tick is ten times the one before, so a bar twice as long is not twice the time. Hatched bars are averages with no stated year, or a scheduled time. The times are as the sources give them, converted to hours by me.",
                          chart_html(CH_CROSS, CROSS_TICKS, 3, "Log-scale bar chart of Atlantic crossing times from 40 days under sail to about 3 hours by Concorde")))
    + section("comparison", "Two centuries, side by side",
              "The same measure over an earlier and a later window. The windows are the nearest the data allows to 1825–1925 and 1925–2025.",
              snap_html(COMP_COLS, COMP))
    + section("reading", "What the figures say about the pace", "", '<p class="note">%s</p><div class="pat">' % e(READING_NOTE) + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in READINGS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tag: S is a secondary source such as an encyclopedia or a data compilation. Every figure was read through a summarizing tool or a data file, so check it against the original before relying on it.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Pace of Change",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 2 · The century",
        "@@H1@@": "How fast things changed",
        "@@SUB@@": "Population, energy, output, household machines and travel time, measured across the last two centuries",
        "@@LEDE@@": "The question is whether the last hundred years moved faster than the hundred before, and whether 1925 marks a clean change of pace. Each chart takes one measure, and the table sets an earlier window beside a later one.",
        "@@ASOF@@": "Figures current to 27 October 2026. Windows are the nearest the data allows to 1825–1925 and 1925–2025, and each says which years it uses.",
        "@@NAV@@": nav([("scale", "At a glance"), ("comparison", "Side by side"), ("reading", "What it says"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several statements are my own arithmetic on the sources' figures: every growth rate, every multiple, the years from 10% to about 50% of households, and the conversion of crossing times to hours. The energy figures come from a data file that carries no 1825 or 1925 value, so the windows are 1800–1900 and 1900–2000. The readings under “What the figures say” are my own. The household series is for the United States; the OWID page names it as a share of US households, but its text carries no values, so the years come from the chart's data file.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "pace-of-change.html")
    print("ok")
