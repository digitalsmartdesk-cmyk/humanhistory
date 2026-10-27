from common import *

# =====================================================================
# CHAPTER 1: APPEARANCE OF HUMAN LIFE
# =====================================================================
ACC, ACCD = "#4a4a9c", "#a9a9ee"
COLS = ["About 1825", "About 1925", "About 2025"]

STATS = [
    ("23–40 days → 5 days → 5 hours", "to cross the Atlantic: sailing packets (average, east and west), the fastest liner in 1924, and the fastest airliner crossing in 2020"),
    ("About half", "of US households had electric power in 1925, the year the series crosses 50 percent"),
    ("15% → 56%", "of the world's people living in cities, around 1900 and in 2020 (the two figures use different definitions)"),
    ("29 → 73", "years of life expectancy at birth: about 29 in the early 1800s and 72.6–73.2 in 2019–2020"),
]

# ---- chart 1: household adoption, US: 10%..90% with 50% point, mark at 1925 ----
Y0 = 1900
def yr(y): return y - Y0
CH_ADOPT = [
    ("Landline telephone", "10% in 1903 · 50% in 1946 · 90% in 1969", yr(1903), yr(1969), False, yr(1946)),
    ("Electric power", "10% in 1908 · 50% in 1925 · 90% in 1949", yr(1908), yr(1949), False, yr(1925)),
    ("Automobile", "10% in 1915 · 50% in 1926 · 90% in 1989", yr(1915), yr(1989), False, yr(1926)),
    ("Radio", "10% in 1925 · 50% in 1931 · 90% in 1947", yr(1925), yr(1947), False, yr(1931)),
    ("Refrigerator", "About 10% in 1930 · 50% in 1938 · 90% in 1953", yr(1930), yr(1953), False, yr(1938)),
    ("Colour television", "10% in 1966 · 57% in 1974 · 90% in 1985", yr(1966), yr(1985), True, yr(1974)),
    ("Cell phone", "10% in 1994 · 56% in 2002 · 90% in 2013", yr(1994), yr(2013), True, yr(2002)),
    ("Internet", "10% in 1993 · 52% in 2002 · peak 88% in 2016, never 90%", yr(1993), yr(2016), True, yr(2002)),
]
CH_ADOPT_TICKS = [(yr(y), str(y)) for y in (1900, 1925, 1950, 1975, 2000)]

# ---- chart 2: urban share, Africa and Asia ----
CH_URB = [
    ("Africa, 1820", "2.72%", 0, 2.72, False, None),
    ("Africa, 1920", "9.70%", 0, 9.70, False, None),
    ("Africa, 2016", "43.10%", 0, 43.10, False, None),
    ("Asia, 1820", "7.42%", 0, 7.42, False, None),
    ("Asia, 1920", "10.32%", 0, 10.32, False, None),
    ("Asia, 2016", "45.97%", 0, 45.97, False, None),
]

# ---- chart 3: life expectancy ranges ----
CH_LIFE = [
    ("Early 1800s", "About 29; 28.5–32 across the 19th century", 28.5, 32, False, 29),
    ("1900", "31–32 in one source; 32 in another", 31, 32, False, None),
    ("1950", "45.7–48", 45.7, 48, False, None),
    ("2019–2020", "72.6–73.2; WHO gives 73.3 for 2019", 72.6, 73.3, False, None),
]

# ---- domain tables ----
D_CITIES = domain_html(
    "cities", "Cities",
    "How many people live in cities, how big the largest are, and how tall the buildings have become.",
    COLS,
    [
        ("Share of the world's people in cities",
         None,
         "About 15% around the turn of the 20th century (definition not stated). OWID, using its own city definition, gives about 20% in 1950.",
         "56.2% in 2020 on the Wikipedia figure. OWID's definition gives 44% in cities, 36% in towns and suburbs and 20% rural in 2020."),
        ("A rich-country example: England and Wales",
         "17% lived in cities over 20,000 in 1801.",
         "54% in 1891, the last year the page gives.",
         None),
        ("Cities over 10 million people",
         None,
         None,
         "33 megacities, against 8 in 1975; 19 are in Asia."),
        ("Largest city",
         None,
         None,
         "Jakarta, 41.9 million, then Dhaka 36.6 million and Tokyo 33.4 million, on the UN's 2025 definition (contiguous 1 km² cells with at least 1,500 people per km², total at least 50,000)."),
        ("Tallest building",
         None,
         "Woolworth Building, New York: 241 m, opened 1913, tallest in the world from 1913 to 1929.",
         "Burj Khalifa: 828 m architectural height, opened 4 January 2010."),
    ],
    "The two world shares use different definitions and should not be subtracted. The 1825 column is empty for the world because I did not find a world city count for that date, and the England and Wales row is a rich-country example, not a world figure."
)

D_HOMES = domain_html(
    "homes", "Homes",
    "Electricity, plumbing and the fuel used for cooking.",
    COLS,
    [
        ("Electric power in the home",
         "No household electric supply (general knowledge).",
         "US households: 10% in 1908, 50% in 1925, 90% in 1949. No world figure found.",
         "Fewer than 1 in 10 people lack access in recent years; 2 in 10 lacked it in 2000, more than 1.5 billion in 1998, and the number fell below 1 billion in 2015."),
        ("Complete plumbing (US)",
         None,
         "No figure for 1925. Nearly half of homes lacked complete plumbing in 1940.",
         "About one-third lacked it in 1950, one-sixth in 1960 and 1% in 1990, the last figure on the Census page."),
        ("Cooking with clean fuels (world)",
         None,
         None,
         "About two-thirds of the world's people in 2020, up from about half in 2000."),
    ],
    "The US electricity series is the OWID household-technology chart. The electricity and cooking access figures are OWID's, read through a summarizing tool. The page gives no world plumbing figure and none for 1925."
)

D_LIVING = domain_html(
    "living", "Living",
    "The machines in an ordinary household, measured by the year a given share of US households had them. The chart below shows the full run: the bar spans 10 percent to 90 percent of households, the black line is the 50 percent year, and the dashed line marks 1925.",
    ["10% of households", "50%", "90%"],
    [
        ("Electric power", "1908", "1925", "1949"),
        ("Landline telephone", "1903", "1946", "1969"),
        ("Automobile", "1915", "1926", "1989"),
        ("Radio", "1925", "1931", "1947"),
        ("Refrigerator", "About 1930", "1938", "1953"),
        ("Colour television", "1966", "57% in 1974", "1985"),
        ("Microwave oven", "20% in 1982", "60% in 1986", "1998"),
        ("Cell phone", "1994", "56% in 2002", "2013"),
        ("Internet", "1993", "52% in 2002", "Not reached; peak 88% in 2016"),
        ("Smartphone", None, "54% in 2013; 35% in 2011", None),
    ],
    "The OWID page's chart is titled 'Share of United States households using specific technologies'. The page text carries no values, so the years come from the chart's data file; a few cells show the nearest value I read rather than the exact 50 percent year. This is the United States only."
)

D_HYGIENE = domain_html(
    "hygiene", "Hygiene and health",
    "Life expectancy, the death of children, and clean water, sanitation and handwashing.",
    COLS,
    [
        ("Life expectancy at birth (world)",
         "About 29 at the beginning of the 19th century.",
         "31–32 in 1900 and 45.7–48 in 1950. No figure for 1925 itself.",
         "72.6–73.2 in 2019–2020. OWID gives 32 in 1900 and 71 in 2021."),
        ("Children dying before age 15 (world)",
         None,
         "About one-quarter in 1950. No figure for 1925.",
         "4% in 2020."),
        ("Safely managed drinking water",
         None,
         None,
         "2.1 billion people, 1 in 4, lacked it; 106 million drank untreated surface water."),
        ("Safely managed sanitation",
         None,
         None,
         "3.4 billion people lacked it; 354 million practised open defecation."),
        ("Basic hygiene at home",
         None,
         None,
         "1.7 billion people lacked it; 611 million had no handwashing facility at all."),
    ],
    "The life expectancy figures are for the world and rest on historical reconstructions, which the Wikipedia page itself treats with caution; the 1900 figure differs between sources. The water, sanitation and hygiene figures are the WHO and UNICEF's 2025 report, a primary source. I found no matching world figures for 1825 or 1925."
)

D_DRESS = domain_html(
    "dress", "Dressing",
    "What was worn, what it was made of, and how much cloth the world now produces.",
    COLS,
    [
        ("Women's silhouette",
         "Full conical skirts with visible corseting, a lowered waistline and large puffed sleeves (1820s).",
         "Drop-waist chemise silhouette. Hemlines rose from the ankle in 1920 to mid-shin in 1922 and just below the knee in 1925.",
         None),
        ("Men's clothing",
         "Broad shoulders, narrow waist, full-length trousers; a 'revolution in tailoring' for fit.",
         "Oxford bags, wide-legged trousers, by 1925.",
         None),
        ("Main fabrics",
         "Wool the main outer fabric; linen or cotton shirts.",
         "Cotton and wool the abundant fabrics; rayon in working-class women's clothing; 'vastly improved production methods' made clothing affordable for working families.",
         "Polyester 59% (78 million tonnes) and all synthetics 69% of fibre production in 2024; cotton 19%."),
        ("World fibre production",
         None,
         None,
         "132 million tonnes in 2024, up 6.5% on the year. Another source gives about 57 million tonnes in 2000 and 111 million in 2020."),
        ("Synthetic fibres",
         None,
         "Commercial rayon from 1905. A polyester fibre patented in Britain in 1928. Nylon 66 first made on 28 February 1935.",
         "Synthetics' share was nine percentage points higher in 2024 than in 2020."),
    ],
    "The 1820s and 1920s rows come from Wikipedia's fashion articles, which describe Western dress only. I did not fetch a source describing present-day dress, so the 2025 cells for the silhouette rows are empty on purpose. The fibre figures are from an industry report summarized by a trade publication. The Wikipedia list dates polyester to 1953 and nylon to 1931, which conflicts with the dates in its own text; I used the text."
)

D_MOBILITY = domain_html(
    "mobility", "Mobility",
    "How long it took to cross the Atlantic, how many motor vehicles there were, and how many people fly.",
    COLS,
    [
        ("Crossing the Atlantic",
         "Sailing packets averaged 23 days eastbound and 40 days westbound (the years are not stated). The fastest passages were 15 d 16 h east (1823) and 15 d 23 h west (1830). Steam: the Great Western took 15 d 12 h west in 1838.",
         "Mauretania eastbound, August 1924: 5 d 1 h 49 min. Alcock and Brown flew it in 16 h 12 min in June 1919; Lindbergh in 33.5 h in May 1927.",
         "Fastest subsonic airliner crossing, 4 h 56 min, 8–9 February 2020, helped by a tailwind. Concorde was scheduled at about 3 h 15 min westbound. I found no sourced typical time today."),
        ("Motor vehicles",
         "None (general knowledge).",
         "United States: about 20.1 million registered in 1925, 17.5 million of them cars. Vehicles per 1,000 people: 86.8 in 1920 and 217.3 in 1930.",
         "About 1.55 billion motor vehicles in use worldwide in 2023. I found no world figure for 1925."),
        ("Air travel",
         None,
         "No scheduled airplane passenger service across the Atlantic until 1939; the Graf Zeppelin airship began scheduled crossings in 1931.",
         "4.7 billion passengers on scheduled services in 2024, 37.4 million departures."),
    ],
    "The sailing figures come from a Wikipedia article on one shipping line and may not stand for all ships. The vehicle figures for the United States are from earlier reading and I could not recover their links, so they are not listed under sources. The 2024 air figures are preliminary and come from ICAO."
)

READINGS = [
    ("In the United States, the premise does not hold as stated",
     "By 1925 half of US households had electric power, and the car reached the same share the next year (1926). Radio had passed 10 percent. The 1925 hemline also differs sharply from the 1820s silhouette. Atlantic crossings had fallen from 23–40 days to about 5. I have household data only for the United States, so I cannot say the same of Europe; the dress and crossing rows cover Western fashion and the North Atlantic."),
    ("For much of the world it holds better",
     "Around 1920 the urban share was about 10 percent in both Africa and Asia, and it reached about 43 and 46 percent by 2016. In 2000, 2 in 10 people still lacked electricity and about half lacked clean cooking fuels. For these regions the large visible shift came after 1925."),
    ("The largest change in the second century is in health and numbers, not in objects",
     "Life expectancy was about 29 in the early 1800s and 31–32 in 1900, then 72.6–73.2 in 2019–2020. Child deaths before 15 fell from about a quarter in 1950 to 4% in 2020. This is the change a photograph of 1925 would not show."),
    ("Both centuries saw the speed of the journey fall by a large factor, in different ways",
     "From the 40-day westbound packet to the 1924 Mauretania, about 5 days, the time fell roughly eightfold. From 1924 to the fastest 2020 airliner crossing, about 25-fold. The second figure compares a ship with an aircraft, so it measures a change of method as much as of speed."),
    ("What the evidence supports",
     "My reading: 'visually similar by 1925' is better described as 'the shape of modern household life was in place in the United States by 1925, and reached much of the rest of the world after it'. What changed after 1925 was how many people shared it, how long they lived, and how fast and far they could travel."),
]
READING_NOTE = "These are my reading of the entries and my arithmetic on them, not findings from the sources."

LIMITS = [
    "The three snapshot dates are loose. Many sources give 1900, 1920, 1950 or 2016 instead of 1825, 1925 and 2025, and each cell names the year it uses.",
    "The household technology series is for the United States only. I found no matching world series for the same machines.",
    "The 1825 column is the thinnest. For most rows I did not find a figure for that date, and I have left it blank rather than estimate.",
    "Dress is described for Western fashion only and I have no 2025 description at all.",
    "Wikipedia and OWID pages were read through a summarizing tool, and a few values come from chart data files rather than page text. Check the figures against the originals before relying on them.",
    "A statement of appearance, such as a skirt or a skyline, cannot be reduced to a figure. These tables show what can be counted, not how life felt.",
]

SRCS = [
    ("Cities", [
        ("https://ourworldindata.org/urbanization", "Our World in Data, Urbanization", "S"),
        ("https://ourworldindata.org/grapher/urbanization-last-500-years", "Our World in Data, share of population living in urban areas (regional series, 1800–2016)", "S"),
        ("https://en.wikipedia.org/wiki/Urbanization", "Wikipedia, Urbanization", "S"),
        ("https://www.aljazeera.com/news/2025/11/26/indonesias-jakarta-now-the-worlds-largest-city-tokyo-falls-to-third-un", "Al Jazeera, Jakarta now the world's largest city (UN World Urbanization Prospects 2025)", "S"),
        ("https://en.wikipedia.org/wiki/Woolworth_Building", "Wikipedia, Woolworth Building", "S"),
        ("https://en.wikipedia.org/wiki/Burj_Khalifa", "Wikipedia, Burj Khalifa", "S")]),
    ("Homes and living", [
        ("https://ourworldindata.org/technology-adoption", "Our World in Data, Technology adoption", "S"),
        ("https://ourworldindata.org/energy-access", "Our World in Data, Energy access", "S"),
        ("https://www.census.gov/data/tables/time-series/dec/coh-plumbing.html", "US Census Bureau, Historical Census of Housing Tables: Plumbing", "P")]),
    ("Hygiene and health", [
        ("https://data.unicef.org/resources/jmp-report-2025/", "WHO/UNICEF JMP, Progress on household drinking water, sanitation and hygiene 2000–2024", "P"),
        ("https://en.wikipedia.org/wiki/Life_expectancy", "Wikipedia, Life expectancy", "S"),
        ("https://ourworldindata.org/life-expectancy", "Our World in Data, Life expectancy", "S"),
        ("https://ourworldindata.org/child-mortality", "Our World in Data, Child mortality", "S")]),
    ("Dressing", [
        ("https://en.wikipedia.org/wiki/1920s_in_Western_fashion", "Wikipedia, 1920s in Western fashion", "S"),
        ("https://en.wikipedia.org/wiki/1820s_in_fashion", "Wikipedia, 1820s in fashion", "S"),
        ("https://en.wikipedia.org/wiki/Synthetic_fiber", "Wikipedia, Synthetic fiber", "S"),
        ("https://apparelresources.com/business-news/manufacturing/global-fibre-output-grows-6-5-2024-synthetics-widening-lead-textile-exchange/", "Apparel Resources, Global fibre output grows 6.5% in 2024 (Textile Exchange)", "S")]),
    ("Mobility", [
        ("https://en.wikipedia.org/wiki/Black_Ball_Line_(trans-Atlantic_packet)", "Wikipedia, Black Ball Line (trans-Atlantic packet)", "S"),
        ("https://en.wikipedia.org/wiki/Blue_Riband", "Wikipedia, Blue Riband", "S"),
        ("https://en.wikipedia.org/wiki/Transatlantic_flight", "Wikipedia, Transatlantic flight", "S"),
        ("https://en.wikipedia.org/wiki/Motor_vehicle", "Wikipedia, Motor vehicle", "S"),
        ("https://www.icao.int/about-icao/AnnualReport2024/world-air-transport-2024", "ICAO, World air transport 2024", "P")]),
]

BODY = (
    section("scale", "At a glance", "", stats_html(STATS)
            + chart_block("When US households got each machine: 10 percent, 50 percent and 90 percent",
                          "Each bar runs from the year 10 percent of US households had the item to the year 90 percent did. The black line is the 50 percent year. The dashed line marks 1925. Hatched bars are less exact: colour television and the cell phone use the nearest value I read to 50 percent, and the internet never reached 90 percent.",
                          chart_html(CH_ADOPT, CH_ADOPT_TICKS, 125, "Range chart of the years US households adopted eight technologies, with a line marking 1925", mark=yr(1925)))
            + chart_block("Share of the population living in cities, Africa and Asia",
                          "Regional urban shares from OWID's long series, in percent. Read each bar's label for the year; the series uses its own definition of urban.",
                          chart_html(CH_URB, [(0, "0%"), (10, "10%"), (20, "20%"), (30, "30%"), (40, "40%"), (50, "50%")], 50, "Bar chart of urban population share in Africa and Asia in 1820, 1920 and 2016"))
            + chart_block("Life expectancy at birth, world, in years",
                          "Ranges are the spread between the figures each source gives. The black line marks the single figure the source calls typical.",
                          chart_html(CH_LIFE, [(0, "0"), (20, "20"), (40, "40"), (60, "60"), (80, "80")], 80, "Range chart of world life expectancy from about 29 in the early 1800s to about 73 in 2019 to 2020")))
    + section("domains", "Six parts of daily life", "Each table gives what I found for about 1825, about 1925 and about 2025. Where I found no figure, the cell says so.",
              D_CITIES + D_HOMES + D_LIVING + D_DRESS + D_MOBILITY + D_HYGIENE)
    + section("reading", "What the figures say about 1925", "", '<p class="note">%s</p><div class="pat">' % e(READING_NOTE) + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in READINGS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or the institution\'s own page. S is a secondary source such as an encyclopedia, a news report or a data compilation.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "Appearance of Life",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 1 · The century",
        "@@H1@@": "How life looked: 1825, 1925, 2025",
        "@@SUB@@": "Cities, homes, living, dress, mobility and hygiene, set side by side at three dates",
        "@@LEDE@@": "The question is whether life looked much the same in 1925 as in 1825, and how far today's look is the product of the last hundred years. Each table puts what I could count at three dates, and says where I found nothing.",
        "@@ASOF@@": "Figures current to 27 October 2026. Most series are the nearest year available, named in each cell.",
        "@@NAV@@": nav([("scale", "At a glance"), ("cities", "Cities"), ("homes", "Homes"), ("living", "Living"), ("dress", "Dressing"), ("mobility", "Mobility"), ("hygiene", "Hygiene"), ("reading", "What it says"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several statements are general knowledge, not tied to a fetched source: that there was no household electric supply and no motor vehicle in 1825. The ratios of crossing times (about eightfold and about 25-fold), the idea that the shape of household life was in place by 1925, and the reading of the regional urban shares are my own arithmetic or reading. Two groups of figures came from earlier fetches whose links I could not recover: the US vehicle registrations and vehicles per 1,000 people, and the 1800–2016 regional urban shares come from an OWID chart (see the sources). The vehicle figures are not in the source list.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "appearance-of-life.html")
    print("ok")
