import html, os, re
e = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))
DEF_T = os.path.join(HERE, "..", "build2", "defenses_template.html")

# ---------- shared shell (CSS reused from the defenses chapter) ----------
t = open(DEF_T, encoding="utf-8").read()
css_start = t.index("<style>")
css_end = t.index("</style>") + 8
CSS = t[css_start:css_end].replace("#0b6b6b", "@@ACC@@").replace("#52c2c0", "@@ACCD@@")
CSS = CSS.replace("@media (max-width:620px){", """.rg-pt{position:absolute;top:0;bottom:0;width:2px;margin-left:-1px;background:var(--ink)}
.rg-mark{position:absolute;top:-3px;bottom:-3px;width:0;border-left:2px dashed var(--ink)}
.legend{font-size:12.5px;color:var(--ink-2);margin:2px 0 6px}
@media (max-width:620px){""", 1)
HEAD = ('<title>@@TITLE@@</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@500;600&family=IBM+Plex+Sans:wght@400;500&display=swap">\n')
SHELL = HEAD + CSS + """
<div class="wrap">
<header>
  <div class="kicker">@@KICKER@@</div>
  <h1>@@H1@@</h1>
  <p class="sub">@@SUB@@</p>
  <p class="lede">@@LEDE@@</p>
  <div class="asof">@@ASOF@@</div>
</header>
<nav class="jump" aria-label="Sections">@@NAV@@</nav>
@@BODY@@
<footer>@@FOOTER@@</footer>
</div>
"""


# ---------- helpers ----------
def stats_html(stats):
    return '<div class="stats">' + "".join('<div class="stat"><b>%s</b><span>%s</span></div>' % (e(a), e(b)) for a, b in stats) + "</div>"


def chart_html(rows, ticks, mx, aria, mark=None):
    """rows: (name, sub, lo, hi, hatch, pt)  bar from lo to hi on a 0..mx scale; pt = optional point marker."""
    ax = "".join('<span style="left:%.3f%%">%s</span>' % (v / mx * 100, lab) for v, lab in ticks)
    out = ['<div class="rg" role="img" aria-label="%s">' % e(aria), '<div class="rg-axis"><span></span><div>%s</div></div>' % ax]
    for name, sub, lo, hi, hatch, pt in rows:
        l = lo / mx * 100
        w = max((hi - lo) / mx * 100, 0)
        extra = ""
        if pt is not None:
            extra += '<i class="rg-pt" style="left:%.2f%%"></i>' % (pt / mx * 100)
        if mark is not None and name not in NOMARK:
            extra += '<i class="rg-mark" style="left:%.2f%%"></i>' % (mark / mx * 100)
        out.append('<div class="rg-row"><div class="rg-lab"><b>%s</b><small>%s</small></div><div class="rg-track"><i class="rg-bar%s" style="left:%.2f%%;width:%.2f%%"></i>%s</div></div>'
                   % (e(name), e(sub), " hatch" if hatch else "", l, w, extra))
    out.append("</div>")
    return "".join(out)


NOMARK = set()


def chart_block(title, note, chartfn):
    return '<h3 class="chart-h">%s</h3>\n<p class="note">%s</p>\n%s' % (e(title), e(note), chartfn)


def groups_html(areas):
    out, n = [], 0
    for area, items in areas:
        lis = []
        for when, kind, title, story, kv, solid in items:
            n += 1
            dl = ('<dl class="kv">%s</dl>' % "".join("<dt>%s</dt><dd>%s</dd>" % (e(k), e(v)) for k, v in kv)) if kv else ""
            lis.append('<li class="item"><div class="when">%s<small>%s</small></div><div class="what"><h3>%s</h3><p>%s</p>%s<p class="solid"><b>How solid</b> %s</p></div></li>'
                       % (e(when), e(kind), e(title), e(story), dl, e(solid)))
        out.append('<section class="grp"><h3 class="gh">%s <span>%d %s</span></h3><ol class="list">%s</ol></section>'
                   % (e(area), len(items), "entry" if len(items) == 1 else "entries", "".join(lis)))
    return "\n".join(out), n


def cards_html(items, cls="thin", withsrc=True):
    if withsrc:
        return '<div class="%s">%s</div>' % (cls, "".join('<div><h3>%s</h3><p>%s</p><p class="src-tag">%s</p></div>' % (e(a), e(b), e(c)) for a, b, c in items))
    return '<div class="%s">%s</div>' % (cls, "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in items))


def sources_html(srcs):
    s = ""
    for h, items in srcs:
        s += "<h3>%s</h3><ul>" % e(h)
        for u, tt, tag in items:
            s += '<li><a href="%s">%s</a><span>%s</span></li>' % (e(u, quote=True), e(tt), tag)
        s += "</ul>"
    return s


def build(cfg, fname):
    page = SHELL
    body = cfg["body"]
    for k, v in cfg["shell"].items():
        page = page.replace(k, v)
    page = page.replace("@@BODY@@", body)
    assert "@@" not in page, re.findall(r"@@\w+@@", page)
    with open(os.path.join(HERE, fname), "w", encoding="utf-8") as f:
        f.write(page)


def nav(items):
    return "".join('<a href="#%s">%s</a>' % (a, e(b)) for a, b in items)


def section(id_, h, intro="", inner=""):
    return '<h2 id="%s">%s</h2>\n%s%s\n' % (id_, e(h), ("<p>%s</p>\n" % e(intro)) if intro else "", inner)


# =====================================================================
# CHAPTER A: NATURE AT RISK
# =====================================================================
A_STATS = [
    ("73%", "average fall in monitored wildlife populations, 1970 to 2022 (Living Planet Report 2026)"),
    ("About 1 million", "animal and plant species threatened with extinction (IPBES, 2019)"),
    ("84%", "of the world's coral reef area hit by bleaching-level heat stress, early 2023 to mid-2025 (NOAA)"),
    ("7 of 9", "planetary boundaries transgressed, all at their highest recorded levels (2026 Planetary Health Check)"),
]

# name, sub, lo, hi, hatch, pt
A_C1 = [
    ("Cycads", "Best estimate 70%", 70, 70, False, 70),
    ("Amphibians", "Best estimate 41%, range 36–47%", 36, 47, False, 41),
    ("Reef-forming corals", "Best estimate 36%, range 31–44%", 31, 44, False, 36),
    ("Conifers", "Best estimate 34%, range 34–35%", 34, 35, False, 34),
    ("Mammals", "Best estimate 26%, range 23–37%", 23, 37, False, 26),
    ("Birds", "Best estimate 12%, range 12–13%", 12, 13, False, 12),
]
A_C2 = [
    ("South America", "Average fall in monitored populations, 1970–2022", 0, 95, False, None),
    ("Freshwater species", "Average fall, 1970–2022", 0, 85, False, None),
    ("Africa", "Average fall, 1970–2022", 0, 80, False, None),
    ("All monitored species", "35,803 populations of 5,790 species", 0, 73, False, None),
    ("Land species", "Average fall, 1970–2022", 0, 69, False, None),
    ("Marine species", "Average fall, 1970–2022", 0, 59, False, None),
]
A_C3 = [
    ("Coral reef area", "Hit by bleaching-level heat stress, 2023–2025", 0, 84, False, None),
    ("Land environment", "Significantly altered by people (IPBES, 2019)", 0, 75, False, None),
    ("Marine environment", "Significantly altered by people (IPBES, 2019)", 0, 66, False, None),
    ("Land degraded", "Up to 40% (UNCCD, as reported)", 0, 40, True, None),
    ("Fish stocks", "Overfished, 2026 FAO assessment", 0, 37.6, False, None),
    ("Wetland extent", "Lost since 1970 (Global Wetland Outlook 2025)", 0, 22, False, None),
]
A_C4 = [
    ("1976–1995", "Annual average, glaciers outside the ice sheets", 0, 100, False, None),
    ("1996–2015", "Annual average", 0, 230, False, None),
    ("2016–2025", "Annual average", 0, 390, False, None),
    ("2025", "One year; sixth-most negative on record", 0, 408, False, None),
]

A_AREAS = [
    ("Species and populations", [
        ("2019", "Assessment", "A million species threatened",
         "The IPBES global assessment found that around 1 million animal and plant species are now threatened with extinction. It put the threatened share at more than 40 percent of amphibians, almost 33 percent of reef-forming corals and more than a third of marine mammals, with a tentative 10 percent for insects. The average abundance of native species in most major land-based habitats has fallen by at least 20 percent.",
         [("Drivers", "Ranked by global impact: changes in land and sea use, direct exploitation of organisms, climate change, pollution, and invasive alien species.")],
         "A UN summary of the 2019 assessment. The insect figure is labelled tentative, and the page gives no share for all species."),
        ("2023 / 2026", "Red List", "Share of species groups threatened",
         "The IUCN Red List, in version 2023-1, puts the best-estimate threatened share at 41 percent of amphibians, 26 percent of mammals, 12 percent of birds, 36 percent of reef-forming corals, 70 percent of cycads and 34 percent of conifers. A magazine summary of the 2026 update reports 175,909 species on the list, of which 49,505 are threatened.",
         [("Ranges", "Amphibians 36–47 percent, mammals 23–37, birds 12–13, reef corals 31–44, conifers 34–35.")],
         "The 2023 percentages come from the IUCN page, which gives ranges. The 2026 counts come from a magazine summary, not from IUCN, and I did not see the release date."),
        ("1970–2022", "Index", "Wildlife populations down 73 percent on average",
         "The Living Planet Report 2026 tracks 35,803 populations of 5,790 species of mammals, birds, reptiles, amphibians and fish. Their average decline was 73 percent from 1970 to 2022, about 2.5 percent a year.",
         [("By region", "South America 95 percent, Africa 80 percent."),
          ("By habitat", "Freshwater 85 percent, land 69 percent, marine 59 percent."),
          ("Threats", "Habitat loss and degradation were reported most often, followed by overexploitation, climate change, pollution, invasive species and disease.")],
         "The report itself says the figure is not a headcount of animals lost and is especially sensitive to changes in already small populations. The 2026 edition added 295 species and 967 populations to the 2024 data."),
        ("2018", "Estimate", "Livestock outweigh wild animals",
         "Our World in Data, summarizing a 2018 study in PNAS, gives humans 0.01 percent of total biomass and 2.5 percent of animal biomass. Livestock account for 4 percent of animal biomass, more than 50 percent above all humans together. Wild mammals and birds together account for 0.38 percent, so livestock outweigh them by a factor of ten.",
         [("Poultry", "About 0.2 percent of animal biomass, more than twice that of wild birds.")],
         "An estimate of mass, not of numbers. The page gives no figure for how much wild mammal biomass has changed over time, so it shows the present balance only."),
        ("2023", "Assessment", "Invasive species",
         "IPBES reports that 37,000 alien species have established worldwide and that 3,500 have become problematic invasives. The page says invasive alien species are the sole cause of 16 percent of extinctions and a major driver of 60 percent, and that they are responsible for 90 percent of extinctions on islands.",
         [("Cost", "A 2019 IPBES estimate of $423 billion. The cost of impacts has more than quadrupled every decade since 1970, according to the page.")],
         "Read through an Australian biodiversity council's summary of the report, not IPBES's own page. The page does not say whether the $423 billion is a yearly figure."),
        ("1925–2018", "Surveys", "Insects",
         "A 2017 study of flying insect biomass at 63 German nature reserves, measured from 1989, found an average fall of 76 percent over 27 years, and 82 percent in summer. A 2020 meta-analysis in Science of 166 long-term surveys at 1,676 sites worldwide, covering 1925 to 2018, found land insect abundance falling by an average of 0.92 percent a year, about 24 percent over 30 years.",
         [("Contrast", "The same meta-analysis found freshwater insect abundance rising by an average of 1.08 percent a year, about 38 percent over 30 years, which the authors link possibly to water protection policies."),
          ("Where", "Land declines were strongest in parts of the United States and in Europe, especially Germany, with the steepest European declines since 2005. Tree-canopy insects were largely unchanged."),
          ("Cause", "The German study did not identify one; pesticides were a suggested explanation. The meta-analysis associates land declines with habitat destruction, particularly urbanization.")],
         "The 76 percent figure comes from a news report whose text gave no publication year (its web address is dated October 2017) and that says only that many reserves border farmland. The meta-analysis measures abundance, not species, and says local trends vary widely, with weaker trends in less disturbed areas described as tentative."),
    ]),
    ("Land and forests", [
        ("2019 / 2022", "Assessment", "Land altered and degraded",
         "IPBES found that three-quarters of the land-based environment and about 66 percent of the marine environment have been significantly altered by human actions, and that land degradation has cut the productivity of 23 percent of the land surface. A UNCCD report, as covered by EcoWatch, says human activity has degraded as much as 40 percent of the world's land.",
         [("Restoration", "The UNCCD scenario calls for five billion hectares to be restored, which the article puts at 35 percent of Earth's land area."),
          ("Economy", "The article says land degradation puts about half of global GDP at risk.")],
         "The 23 percent and the up-to-40 percent use different definitions and sources, so they do not conflict. The UNCCD figures reached me through a news article, and the GDP claim is the article's."),
        ("2025", "Satellite record", "Tropical forest and fire",
         "Global Forest Watch reports that the world lost 4.3 million hectares of tropical primary forest in 2025. That was 36 percent less than in 2024, and still 46 percent higher than a decade ago.",
         [("All forests", "Global tree cover loss was 25.5 million hectares in 2025, and fires caused 42 percent of it.")],
         "WRI's own summary of Global Forest Watch data. The 42 percent fire share applies to all tree cover loss, not to tropical primary forest alone."),
        ("2015 / 2023", "Assessment", "Soils",
         "FAO's 2015 Status of the World's Soil Resources reports that 33 percent of land is moderately to highly degraded through erosion, salinization, compaction, acidification and chemical pollution, and that conditions are worsening in far more cases than they are improving. Erosion removes 25 to 40 billion tonnes of topsoil each year.",
         [("Crops", "Cereal losses from erosion are estimated at 7.6 million tonnes a year, and could exceed 253 million tonnes by 2050 without action. Salinization affects an estimated 760,000 square kilometres."),
          ("Life", "A 2023 study led by Mark Anthony, in PNAS, estimates that 59 percent of all species depend on soil, including 90 percent of fungi, 86 percent of plants and 40 percent of bacteria."),
          ("Reversible", "FAO says the decline can be reversed if countries promote sustainable soil management.")],
         "The FAO figures are from its own 2015 press release and are a decade old. The 59 percent is a synthesis of earlier estimates, not a census, and the page I read gives no margin of error."),
    ]),
    ("Fresh water and wetlands", [
        ("1970–2025", "Assessment", "Wetlands",
         "The Global Wetland Outlook 2025 reports a loss of more than 4 million square kilometres of wetland since 1970 across 11 wetland types, a 22 percent fall in extent. About a quarter of the remaining wetlands are degraded and are being destroyed at 0.52 percent a year.",
         [("Dependence", "Roughly 40 percent of the world's plant and animal species rely on wetlands at some point in their lives."),
          ("Value", "The remaining 14 million square kilometres provide $8 trillion to $39 trillion of ecosystem services a year."),
          ("Outlook", "Up to 20 percent of the world's wetlands could be lost in the next 25 years.")],
         "Read through a Mongabay summary. The value range is wide because the figure depends on how services are priced, and the forecast is the report's, not mine."),
    ]),
    ("Oceans and reefs", [
        ("2024", "Assessment", "Fish stocks",
         "The FAO's State of World Fisheries and Aquaculture 2026 puts the share of sustainably fished stocks at 62.4 percent, which leaves 37.6 percent overfished. Wild catch was stable at about 92 million tonnes in 2024, inside the 86 to 94 million tonne band it has held since the late 1980s, while farmed aquatic animal production passed 100 million tonnes for the first time.",
         [("Change", "The sustainable share fell 2.1 points from the 2024 report.")],
         "Read through Mongabay. The number of assessed stocks rose from about 500 to 2,665, mostly because stocks were split into separate assessments, so comparison with earlier editions is harder."),
        ("2023–2025", "Satellite and survey", "Coral bleaching",
         "NOAA confirmed the fourth global coral bleaching event on 15 April 2024. Bleaching-level heat stress ran from early 2023 to mid-2025 and reached 84 percent of the world's coral reef area. Mass bleaching was documented in at least 83 countries and territories across the Pacific, Atlantic and Indian oceans.",
         [("Tipping point", "The 2025 Global Tipping Points report says warm-water coral reefs are now passing their tipping point, with widespread dieback under way. Reefs support nearly a billion people and a quarter of all marine life.")],
         "NOAA's own page says the event likely concluded in mid-2025 and that it was waiting on the December 2025 to February 2026 summer to be sure; my read predates that check. The tipping-point statement comes from a Stockholm Resilience Centre summary that gives no temperature threshold."),
        ("2026", "Red List", "Deep-sea habitats",
         "A magazine summary of the IUCN Red List 2026 update says about 62 percent of endemic hydrothermal vent molluscs, 125 of 201 species, are threatened by deep-sea mining. It names a deep-sea snail from the Indian Ocean, Lirapex felix, listed as Critically Endangered because of mining exploration.",
         [],
         "A secondary summary whose excerpt cut off, so other changes in the update may exist. No commercial mining has been approved; see the chapter on defenses."),
    ]),
    ("Ice and sea level", [
        ("1975–2025", "Monitoring", "Glaciers",
         "The World Glacier Monitoring Service reports net mass loss of 408 gigatonnes in the 2025 hydrological year for glaciers outside the ice sheets, sixth-most negative on record, equal to 1.1 millimetres of sea level. Since 1975 the cumulative loss is 9,583 gigatonnes, equal to 26.4 millimetres.",
         [("Rate", "Annual loss rose from under 100 gigatonnes in 1976–1995 to about 230 in 1996–2015 and about 390 in 2016–2025."),
          ("Recent", "Six of the highest mass-loss years on record fell in the past seven years.")],
         "WGMS's own report. Each figure carries an uncertainty (408 ± 132 Gt for 2025), and the page gives no share of ice lost."),
        ("1993–2025", "Satellite record", "Sea level",
         "NASA reports that average global sea level has risen about 10 centimetres since 1993, and that the annual rate of rise has more than doubled over three decades. In 2025 the rise was about 0.8 millimetres, down from about 5.9 millimetres in 2024.",
         [],
         "NASA's own page. The 2025 figure is one year and swings with ocean cycles such as La Niña; the trend over three decades is the point. I converted inches and centimetres to millimetres."),
    ]),
    ("Chemistry, waste and Earth systems", [
        ("1950–2019", "Estimate", "Plastic",
         "World plastic production rose nearly 230-fold, from 2 million tonnes in 1950 to 460 million tonnes in 2019. Roughly 350 million tonnes of plastic waste are generated each year, and about a quarter is mismanaged.",
         [("Ocean", "Between 1 and 2 million tonnes a year are estimated to enter the oceans, about 0.5 percent of waste generated. Earlier estimates ran as high as 8 million.")],
         "Our World in Data's summary of OECD and academic estimates. The page says the uncertainties are large, and the ocean figure has been revised downward."),
        ("1900–2023", "Estimate", "Nitrogen",
         "Our World in Data estimates that around half of the global population depends on synthetic nitrogen fertilizer, within a range of 40 to 50 percent. Without it the population may have been only about 4 billion, against over 8 billion in 2023.",
         [("Link", "The 2026 Planetary Health Check lists modification of biogeochemical flows, which covers nitrogen, among the transgressed boundaries. The connection between the two entries is mine.")],
         "The fertilizer share is hard to derive with confidence, because breeding, irrigation and mechanization also raised yields."),
        ("2026", "Assessment", "Planetary boundaries",
         "The 2026 Planetary Health Check finds that seven of nine boundaries are transgressed: climate change, biosphere integrity, land system change, freshwater change, biogeochemical flows, novel entities and ocean acidification. All seven are at their highest recorded levels of transgression. Ocean acidification was the most recent to be breached, in 2025.",
         [("Not breached", "Stratospheric ozone depletion and atmospheric aerosol loading, both improved over the last decade, though the authors caution that global progress may mask unsafe aerosol levels in some regions.")],
         "Read through a summary posted on Astrobiology.com. The boundaries are a scientific framework, not a measured threshold at which collapse begins."),
        ("1958–2026", "Measurement", "Carbon dioxide and temperature",
         "Carbon dioxide at Mauna Loa rose from 313 parts per million in 1958 to a May 2026 peak of 432 parts per million. The WMO puts 2025 at 1.43 °C above the pre-industrial level, with an uncertainty of 0.13 °C.",
         [],
         "Both figures were read for the chapter on vulnerability, from a Japanese research-centre page citing the Mauna Loa record and from a trade-press report of the WMO statement. Neither is the original release."),
    ]),
]

A_PATTERNS = [
    ("Reach", "Three-quarters of the land environment and two-thirds of the marine environment are significantly altered, and the 84 percent of reef area hit by heat stress shows that even remote ecosystems are affected."),
    ("Scale", "Plastic output grew about 230-fold from 1950 to 2019, carbon dioxide rose from 313 to 432 parts per million, and the yearly rate of glacier loss is roughly four times its 1976–1995 level."),
    ("Speed", "Monitored wildlife populations fell by an average of 73 percent in 52 years. The fourth global bleaching event reached 84 percent of reef area in about two and a half years."),
    ("Dependence", "Reefs support nearly a billion people, wetlands about 40 percent of species, and synthetic nitrogen about half of humanity, so pressure on these systems is linked to everything that depends on them."),
    ("No clock for recovery", "Several entries describe states, not flows: a reef tipping point said to be passing, seven boundaries at their highest recorded levels, and glaciers that lose ice faster each period."),
]

A_LIMITS = [
    "Measured records are short. The Living Planet index starts in 1970 and the satellite and bleaching records are far shorter, so the chapter cannot compare today with earlier centuries.",
    "The measures are not comparable. The charts mix population indices, shares of area and shares of stocks, and the labels say which is which.",
    "Indices have known weaknesses. The Living Planet figure is an average that is sensitive to small populations, and the Red List shares carry wide ranges.",
    "Not covered: groundwater, air pollution's effect on ecosystems, noise, and the many local losses that never reach a global index. The insect and soil entries are thinner than the others, resting on few studies and, for soils, a 2015 report.",
    "Most figures reached me through summaries, so they need checking against the original reports before use.",
]

A_SOURCES = [
    ("Species and populations", [
        ("https://www.unep.org/news-and-stories/press-release/natures-dangerous-decline-unprecedented-species-extinction-rates", "UNEP, IPBES global assessment press release (2019)", "P"),
        ("https://www.iucnredlist.org/resources/summary-statistics", "IUCN Red List, summary statistics (version 2023-1)", "P"),
        ("https://www.chronicleindia.in/online-magazine/csce-september-2026/iucn-red-list-2026-update", "Chronicle India, IUCN Red List 2026 update", "S"),
        ("https://theprint.in/environment/wwf-says-wildlife-populations-dropped-by-an-average-of-73-from-1970-to-2022/3065109/", "ThePrint, WWF Living Planet Report (73 percent)", "S"),
        ("https://ourworldindata.org/life-on-earth", "Our World in Data, biomass on Earth (Bar-On et al. 2018)", "S"),
        ("https://biodiversitycouncil.org.au/news/ipbes-intergovernmental-report-highlights-423-billion-impact-of-invasive-alien-species", "Biodiversity Council, IPBES invasive alien species report", "S"),
        ("https://phys.org/news/2017-10-three-quarters-total-insect-population-lost.html", "Phys.org, flying insect decline in German nature reserves", "S"),
        ("https://www.sciencedaily.com/releases/2020/04/200423143031.htm", "ScienceDaily, van Klink et al. 2020 insect meta-analysis", "S")]),
    ("Land, water and oceans", [
        ("https://www.ecowatch.com/land-degradation-un-report.html", "EcoWatch, UN report on land degradation", "S"),
        ("https://www.fao.org/newsroom/detail/Soils-are-endangered-but-the-degradation-can-be-rolled-back/", "FAO, soils are endangered but degradation can be rolled back (2015)", "P"),
        ("https://e360.yale.edu/digest/soil-species-biodiversity", "Yale Environment 360, species that live in soil", "S"),
        ("https://africa.wri.org/insights/tropical-rainforest-loss-slowed-2025-fire-growing-threat-forests-worldwide", "WRI and Global Forest Watch, tropical forest loss in 2025", "P"),
        ("https://news.mongabay.com/short-article/2025/07/wetlands-at-risk-but-new-report-offers-road-map-for-recovery/", "Mongabay, Global Wetland Outlook 2025", "S"),
        ("https://news.mongabay.com/2026/06/aquatic-animal-and-terrestrial-meat-trades-now-almost-on-par-fao-report-finds/", "Mongabay, FAO fisheries report 2026", "S"),
        ("https://www.nesdis.noaa.gov/news/worlds-fourth-mass-coral-bleaching-event-likely-ended-2025", "NOAA, fourth global coral bleaching event", "P"),
        ("https://www.stockholmresilience.org/research/research-stories/2025-10-13-world-reaches-first-climate-tipping-point---widespread-mortality-of-coral-reefs.html", "Stockholm Resilience Centre, Global Tipping Points report", "P")]),
    ("Ice, waste and Earth systems", [
        ("https://wgms.ch/ncc_glaciers_in_2025/", "WGMS, global glacier mass change in 2025", "P"),
        ("https://www.jpl.nasa.gov/news/nasa-analysis-shows-la-nina-limited-sea-level-rise-in-2025/", "NASA JPL, sea level rise in 2025", "P"),
        ("https://ourworldindata.org/plastic-pollution", "Our World in Data, plastic pollution", "S"),
        ("https://ourworldindata.org/how-many-people-does-synthetic-fertilizer-feed", "Our World in Data, how many people synthetic fertilizer feeds", "S"),
        ("https://astrobiology.com/2026/09/22/planetary-health-check-2026-finds-mounting-pressures-across-earths-life-support-systems-reports-and-proceedings/", "Astrobiology.com, Planetary Health Check 2026", "S"),
        ("https://www.jircas.go.jp/en/program/proc/blog/20260615", "JIRCAS, Mauna Loa carbon dioxide peak 2026", "S"),
        ("https://www.argusmedia.com/en/news-and-insights/latest-market-news/2804512-wmo-says-2025-was-1.43degc-above-pre-industrial-era", "Argus Media, WMO on 2025 temperature", "S")]),
]

a_groups, a_n = groups_html(A_AREAS)
A_BODY = (
    section("scale", "How large the changes are", "", stats_html(A_STATS)
            + chart_block("Share of species groups threatened with extinction",
                          "The bar spans the range given by the IUCN, and the black line marks the best estimate. Version 2023-1 of the Red List.",
                          chart_html(A_C1, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Range chart of the share of six species groups threatened, from 12 percent of birds to 70 percent of cycads"))
            + chart_block("Average fall in monitored wildlife populations, 1970 to 2022",
                          "Each bar is an average of changes in population size, not a count of animals. Regions and habitats overlap, so the rows are not parts of one whole.",
                          chart_html(A_C2, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of average population decline, from 59 percent for marine species to 95 percent in South America"))
            + chart_block("How much of each system is affected",
                          "These are different measures: area altered, area under heat stress, stocks overfished, extent lost. Read each label. The hatched bar is an upper limit.",
                          chart_html(A_C3, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of six measures of ecosystem change, from 22 percent of wetland extent lost to 84 percent of reef area under heat stress"))
            + chart_block("Glacier mass loss per year, in gigatonnes",
                          "Glaciers outside the Greenland and Antarctic ice sheets. The first bar is shown as 100 because the source says under 100; the others are the source's figures, and the second and third are approximate.",
                          chart_html(A_C4, [(0, "0"), (100, "100"), (200, "200"), (300, "300"), (400, "400")], 450, "Bar chart of glacier mass loss per year rising from under 100 gigatonnes to about 390 and 408")))
    + section("measures", "The measures", "Nineteen entries in six systems. Each gives the figure, how it was measured and how solid it is.", a_groups)
    + section("pattern", "What stands out", "", '<p class="note">These are my reading of the entries, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in A_PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in A_LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or an institution\'s own page, S is a secondary source such as a news report, magazine or data compilation. I read pages through a summarizing tool, so check figures against the original before citing.</p>' + sources_html(A_SOURCES) + "</section>"
)
assert a_n == 19, a_n

A_CFG = {
    "shell": {
        "@@TITLE@@": "Nature at Risk",
        "@@ACC@@": "#3f6b1f", "@@ACCD@@": "#9ccf6a",
        "@@KICKER@@": "Evidence brief: the living world",
        "@@H1@@": "Nature at risk",
        "@@SUB@@": "Nineteen measures of pressure on species, land, water, ice and the Earth system",
        "@@LEDE@@": "Wildlife populations, forests, wetlands, oceans, glaciers, plastic and the planetary boundaries, measured over the last century or as far back as the records go. Each entry says what was measured, what it found and how reliable the figure is.",
        "@@ASOF@@": "Figures current to 13 October 2026. Most reached me through summaries; see the source tags at the end.",
        "@@NAV@@": nav([("scale", "Scale"), ("measures", "The measures"), ("pattern", "What stands out"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "The age of each record differs: the Living Planet index begins in 1970, glacier records in 1975, sea level in 1993 and the bleaching event covers 2023 to 2025. The observations under “What stands out”, the link between nitrogen and the biogeochemical boundary, and the unit conversions for sea level are my own reading or arithmetic.",
    },
    "body": A_BODY,
}
build(A_CFG, "nature-at-risk.html")
print("A entries", a_n)

# =====================================================================
# CHAPTER B: NATURE DEFENDED
# =====================================================================
B_STATS = [
    ("17.6% / 8.4%", "of land and of ocean under protection, against a 30% target for each by 2030 (Protected Planet Report 2024)"),
    ("93%", "of its pre-whaling size reached by humpback whales in the western South Atlantic, from a low of 440 in 1958"),
    ("2,874 km²", "of Amazon deforestation alerts, August 2025 to July 2026, the lowest since the series began in 2016"),
    ("Fewer than half", "of aligned national biodiversity targets assessed are on track (CBD Executive Secretary, August 2026)"),
]

NOMARK.update({"Key biodiversity areas covered"})
B_C1 = [
    ("Land protected", "Terrestrial and inland waters", 0, 17.6, False, None),
    ("Ocean protected", "Marine and coastal areas", 0, 8.4, False, None),
    ("Land protected and connected", "Protected areas joined to others", 0, 8.52, False, None),
    ("Ocean in implemented or managed areas", "Marine protected areas actively managed", 0, 5.7, False, None),
    ("Ocean fully or highly protected", "Strict protection", 0, 2.8, False, None),
    ("Key biodiversity areas covered", "At least partly protected; 32% lie wholly outside (my subtraction)", 0, 68, True, None),
]
B_C2 = [
    ("1958, the low point", "440 whales against about 27,000 before whaling (my arithmetic)", 0, 1.6, True, None),
    ("About 2019", "About 25,000 whales", 0, 93, False, None),
]

B_AREAS = [
    ("Protected space", [
        ("2022 to 2030", "Framework", "Kunming-Montreal Global Biodiversity Framework",
         "The framework has 23 global targets, including the aim of protecting at least 30 percent of land and ocean by 2030. By the August 2026 meetings in Nairobi, 172 Parties, almost 90 percent, had submitted national targets, and 130 had submitted national reports. The first global review of progress is due at COP17, 19 to 30 October 2026, in Yerevan.",
         [("Verdict so far", "The Executive Secretary told the Nairobi meeting that fewer than half of aligned national targets assessed by Parties are currently on track."),
          ("Largest gaps", "Mobilizing biodiversity finance, reforming harmful subsidies, addressing business impacts and dependencies, and shifting toward sustainable consumption.")],
         "From the Convention's own press releases. The 2022 adoption date is general knowledge. The review at COP17 had not happened when I wrote this."),
        ("2024", "Report", "Protected areas",
         "The Protected Planet Report 2024 puts coverage at 17.6 percent of land and inland waters and 8.4 percent of ocean and coastal areas. Since 2020, 629,000 square kilometres of land and 1.77 million square kilometres of sea have been added. 51 countries and territories exceed 30 percent on land, and 31 exceed it at sea.",
         [("To reach 30%", "Another 16.7 million square kilometres (12.4 percent) of land and 78.3 million (21.6 percent) of sea."),
          ("Quality", "Only 8.52 percent of land is both protected and connected. Only 5.7 percent of the ocean is in marine protected areas that are implemented or actively managed, and 2.8 percent is fully or highly protected."),
          ("Key areas", "Over two-thirds of key biodiversity areas are partially or fully covered, and the remaining 32 percent lie entirely outside protected areas.")],
         "From the report's executive summary, a UN-backed dataset of official submissions. Coverage is counted by area, so it does not show whether protection is enforced."),
        ("2025 / 2026", "Treaty", "High Seas Treaty",
         "The Agreement on Biodiversity Beyond National Jurisdiction passed 60 ratifications on 20 September 2025, with Sierra Leone and Morocco the last two to deposit. It entered into force on 17 January 2026. Palau was the first to ratify, on 22 January 2024.",
         [("Allows", "Marine protected areas beyond national jurisdiction, environmental impact assessments, and rules on access to and benefit sharing from marine genetic resources.")],
         "IUCN's announcement. I found no marine protected area yet created under the treaty, and the page does not give the share of ocean the treaty covers."),
    ]),
    ("Species", [
        ("1986 to 2019", "Recovery", "Whaling ban and the humpback whale",
         "Commercial whaling was curbed and then banned in 1986. Humpbacks in the western South Atlantic fell to a low of 440 in 1958, from about 27,000 before hunting. A 2019 study estimates about 25,000 now, roughly 93 percent of the pre-hunt level.",
         [("Source", "Zerbini and colleagues, Royal Society Open Science, published online 16 October 2019.")],
         "One population of one species, reported by Science News. Other whale populations recovered less, and the ban is only one factor."),
        ("1993 to 2020", "Study", "Extinctions prevented",
         "Bolam and colleagues estimate that conservation action prevented at least 28 bird and mammal extinctions since 1993: 21 to 32 birds and 7 to 16 mammals. They drew on 137 experts.",
         [("Against", "In the same period 15 bird and mammal species went extinct or are strongly suspected to have done so. The vaquita is still declining quickly.")],
         "The figures are estimates of what would have happened without conservation, not counts. The study covers birds and mammals only."),
    ]),
    ("Forests and land", [
        ("2025 to 2026", "Satellite alerts", "Amazon deforestation alerts",
         "Brazil's DETER system recorded 2,874.38 square kilometres of deforestation alerts from August 2025 to July 2026, down from 4,495 in the previous period. That is the lowest since the series began in 2016 and 55.6 percent below the average of the last ten cycles.",
         [],
         "A report in Agência Brasil of figures from the national space research institute. The article says the fall was 36.87 percent, but the two areas it gives imply about 36.06 percent, and it does not explain the gap. Alerts are not the same as the annual official count."),
        ("2024 to 2050", "Law", "EU Nature Restoration Law",
         "The law took effect on 18 August 2024. Member States must have restoration measures in place on at least 20 percent of the EU's land and 20 percent of its sea by 2030, and for all ecosystems that need restoration by 2050.",
         [("Plans", "Draft national restoration plans are due two years after entry into force, so about August 2026, with reviews by 2032 and 2042."),
          ("Rivers", "The law aims to restore at least 25,000 kilometres of rivers by 2030.")],
         "From the European Commission's announcement. I did not check whether Member States met the 2026 deadline for draft plans."),
    ]),
    ("Oceans and chemistry", [
        ("1987 to 2066", "Treaty", "Ozone layer and the Montreal Protocol",
         "The phase-out covers nearly 99 percent of banned ozone-depleting substances. If current policies stay, the ozone layer is expected to return to 1980 levels by about 2066 over the Antarctic, 2045 over the Arctic and 2040 elsewhere. In the 2026 Planetary Health Check, stratospheric ozone is one of two boundaries that are not transgressed.",
         [],
         "The WMO page and a summary of the 2026 check. The 1987 date is general knowledge. Ozone and aerosols are the two boundaries that have improved over the last decade."),
        ("2024", "Management", "Fisheries",
         "Wild catch has stayed in a band of 86 to 94 million tonnes since the late 1980s, about 92 million tonnes in 2024, while farmed aquatic animal production passed 100 million tonnes. 62.4 percent of assessed stocks are fished sustainably.",
         [("Trend", "The sustainable share fell 2.1 points from the 2024 report.")],
         "FAO's 2026 report through Mongabay. A steady catch can reflect management or limits on stocks, and the report's stock count changed from about 500 to 2,665 between editions."),
        ("2026", "Governance", "Deep-sea mining held back",
         "At the International Seabed Authority's two-week Council session reported on 20 March 2026, no mining was approved. The Mining Code, the rulebook needed before commercial extraction, remains unfinished. 40 countries back a moratorium.",
         [("Pressure", "Concern about unilateral mining outside the Authority, centred on a Nauru-linked subsidiary of The Metals Company. A report on it was due at the July meeting.")],
         "A report in Oceanographic Magazine. I did not find the outcome of the July meeting, so this describes the position in March."),
    ]),
    ("Money", [
        ("2019 to 2030", "Finance", "Funding for nature",
         "International finance to developing countries was $29.8 billion in 2023 for biodiversity-related spending and $16.8 billion for biodiversity-specific spending, against a target of $20 billion a year by 2025. The 2030 target is $30 billion a year.",
         [("Wider targets", "$200 billion a year from all sources by 2030, and $500 billion of harmful subsidies reduced or reformed."),
          ("Gap", "A $700 billion annual biodiversity funding gap by 2030."),
          ("Nature-based solutions", "$220 billion of total annual flows in 2023, up 11 percent on 2022, of which $23.4 billion was private.")],
         "From a UK government finance dashboard. The page gives no current total for the $200 billion target or for subsidies, so I cannot say how close either is."),
    ]),
]

B_THIN = [
    ("The framework's own review shows slippage", "The Executive Secretary says fewer than half of aligned national targets assessed are on track, with the largest gaps in finance, harmful subsidies, business impacts and consumption.", "Source: CBD press release, August 2026 (P)"),
    ("Protection is mostly on paper", "17.6 percent of land and 8.4 percent of ocean are covered, but only 5.7 percent of the ocean is actively managed and only 2.8 percent strictly protected. Only 8.52 percent of land is protected and connected, and 32 percent of key biodiversity areas lie entirely outside protected areas.", "Source: Protected Planet Report 2024 (P)"),
    ("The money is short", "Biodiversity-specific international finance was $16.8 billion in 2023, below the $20 billion target for 2025, and the page cites a $700 billion annual funding gap by 2030. The wetlands report puts the cost of reaching conservation goals for wetlands alone at $275 billion to $550 billion a year.", "Source: UK finance dashboard (P); Mongabay on wetlands (S)"),
    ("The plastics treaty is deadlocked", "Negotiations in Geneva from 5 to 15 August 2025 ended with no agreement. A later session on 7 February (the page gives no year; I read it as 2026) was mainly administrative and elected a new chair, and I found no date for the next one. States disagree on ambition and on whether chemicals in plastics are covered.", "Source: Wikipedia, Global plastic pollution treaty (S)"),
    ("The deep seabed has no rules yet", "The Mining Code is unfinished and 40 countries back a moratorium, but concern about unilateral mining continues. The 2026 Red List update says 125 of 201 endemic vent molluscs are threatened by deep-sea mining.", "Source: Oceanographic Magazine (S); Chronicle India (S)"),
    ("Tropical forest loss is still high", "Loss of tropical primary forest fell 36 percent in 2025 but is still 46 percent higher than a decade ago, and fire caused 42 percent of global tree cover loss. A fall in Amazon alerts does not show the same for other forests.", "Source: WRI and Global Forest Watch (P); last sentence is my reading"),
    ("Nothing here addresses ocean heat", "The coral bleaching event reached 84 percent of reef area and a tipping point is said to be passing. None of the defenses listed acts on ocean heat itself. The emissions path is covered in the chapter on defenses against catastrophe.", "Source: NOAA (P), Stockholm Resilience Centre (P); last two sentences are my reading"),
    ("Wetlands are still being lost", "The Global Wetland Outlook says about a quarter of remaining wetlands are degraded and destroyed at 0.52 percent a year, and that up to 20 percent of wetlands could be lost in the next 25 years. It says protecting wetlands is far less expensive than restoring them.", "Source: Mongabay on the Global Wetland Outlook 2025 (S)"),
]

B_PATTERNS = [
    ("Defenses work best on a single, countable cause", "The whaling ban, the ozone chemicals and the Amazon alerts each target one act that can be monitored. The recoveries in this chapter are of that kind."),
    ("Targets are ahead of delivery", "The 30 percent targets stand against 17.6 and 8.4 percent coverage and much smaller shares that are managed or strictly protected."),
    ("Diffuse drivers have no comparable instrument", "Land-use change, consumption, plastic and ocean heat are spread across many actors. For these the entries describe frameworks and negotiations, and I found no measured turnaround."),
    ("Recovery is slow and species-specific", "The humpback population reached about 93 percent of its pre-hunt size roughly 33 years after the ban, and the same studies show other species still falling. Conservation prevented at least 28 extinctions while 15 others occurred."),
]

B_LIMITS = [
    "The list is my selection. Eleven entries cannot cover the many local and national defenses, and I did not cover freshwater protection, soil, invasive species control or national endangered species laws.",
    "Cause is hard to show. A rise in a population or fall in deforestation may reflect enforcement, prices, weather or all three, and the sources say so in only some cases.",
    "Several items are early. The framework's global review, the July seabed meeting and the national restoration plans were still pending or unchecked when I wrote this.",
    "Coverage counts area, not outcome. A protected area that is not managed is counted in the 17.6 and 8.4 percent.",
    "Most figures reached me through summaries, so they need checking against the original reports before use.",
]

B_SOURCES = [
    ("Frameworks and treaties", [
        ("https://www.cbd.int/doc/press/2026/pr-2026-08-12-sbstta28-sbi7-en.pdf", "CBD, press release on SBSTTA-28 and SBI-7 (August 2026)", "P"),
        ("https://www.cbd.int/doc/press/2026/pr-2026-03-09-nr7-en.pdf", "CBD, press release on seventh national reports (March 2026)", "P"),
        ("https://library.sprep.org/sites/default/files/2025-02/Protected-Planet-Report-2024_Executive-Summary.pdf", "Protected Planet Report 2024, executive summary", "P"),
        ("https://iucn.org/press-release/202509/high-seas-treaty-achieves-milestone-60-ratifications-paving-way-ocean", "IUCN, High Seas Treaty reaches 60 ratifications", "P"),
        ("https://en.wikipedia.org/wiki/Global_plastic_pollution_treaty", "Wikipedia, Global plastic pollution treaty", "S"),
        ("https://oceanographicmagazine.com/news/no-code-no-permits-isa-deep-sea-mining-talks-end-in-stalemate/", "Oceanographic Magazine, ISA deep-sea mining talks", "S")]),
    ("Species, forests and land", [
        ("https://www.sciencenews.org/article/humpback-whales-south-atlantic-have-recovered-near-extinction", "Science News, South Atlantic humpbacks have recovered", "S"),
        ("https://www.ncl.ac.uk/press/articles/archive/2020/09/28speciesextinctionsprevented", "Newcastle University, extinctions prevented by conservation", "P"),
        ("https://agenciabrasil.ebc.com.br/en/meio-ambiente/noticia/2026-08/amazon-deforestation-falls-3687-over-past-year", "Agência Brasil, Amazon deforestation falls", "S"),
        ("https://environment.ec.europa.eu/news/nature-restoration-law-enters-force-2024-08-15_en", "European Commission, Nature Restoration Law enters into force", "P"),
        ("https://africa.wri.org/insights/tropical-rainforest-loss-slowed-2025-fire-growing-threat-forests-worldwide", "WRI and Global Forest Watch, tropical forest loss in 2025", "P")]),
    ("Oceans, chemistry and money", [
        ("https://wmo.int/ar/node/20740", "WMO, ozone layer recovery is on track", "P"),
        ("https://astrobiology.com/2026/09/22/planetary-health-check-2026-finds-mounting-pressures-across-earths-life-support-systems-reports-and-proceedings/", "Astrobiology.com, Planetary Health Check 2026", "S"),
        ("https://news.mongabay.com/2026/06/aquatic-animal-and-terrestrial-meat-trades-now-almost-on-par-fao-report-finds/", "Mongabay, FAO fisheries report 2026", "S"),
        ("https://news.mongabay.com/short-article/2025/07/wetlands-at-risk-but-new-report-offers-road-map-for-recovery/", "Mongabay, Global Wetland Outlook 2025", "S"),
        ("https://www.gov.uk/government/publications/biodiversity-finance-trends-2025/biodiversity-finance-trends-dashboard-2025-accessible-version", "UK government, Biodiversity Finance Trends Dashboard 2025", "P"),
        ("https://www.chronicleindia.in/online-magazine/csce-september-2026/iucn-red-list-2026-update", "Chronicle India, IUCN Red List 2026 update", "S"),
        ("https://www.nesdis.noaa.gov/news/worlds-fourth-mass-coral-bleaching-event-likely-ended-2025", "NOAA, fourth global coral bleaching event", "P"),
        ("https://www.stockholmresilience.org/research/research-stories/2025-10-13-world-reaches-first-climate-tipping-point---widespread-mortality-of-coral-reefs.html", "Stockholm Resilience Centre, Global Tipping Points report", "P")]),
]

b_groups, b_n = groups_html(B_AREAS)
B_BODY = (
    section("results", "What the defenses have achieved so far", "", stats_html(B_STATS)
            + chart_block("Share covered, against the 30 percent target",
                          "The dashed line marks 30 percent, the 2030 target for land and for sea. The hatched bar is my subtraction from the source's 32 percent. Land and ocean coverage are the 2024 report's figures.",
                          chart_html(B_C1, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of protected area coverage against a 30 percent target: 17.6 percent of land, 8.4 percent of ocean, and smaller shares that are connected, managed or strictly protected", mark=30))
            + chart_block("Western South Atlantic humpback whales, share of pre-whaling size",
                          "One population. The hatched bar is my arithmetic, 440 divided by about 27,000; the second bar is the study's figure of about 93 percent.",
                          chart_html(B_C2, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart showing humpbacks at about 1.6 percent of pre-whaling size in 1958 and about 93 percent around 2019")))
    + section("defenses", "The defenses", "Eleven entries in five areas. The date is when the system began or when the result was reported.", b_groups)
    + section("thinning", "Where defenses are thinning", "These are gaps reported in the sources or plain readings of them. Where I could not find what happened next, the card says so.", cards_html(B_THIN))
    + section("patterns", "What the defenses have in common", "", '<p class="note">These are my reading of the entries, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in B_PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in B_LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is a primary source or an institution\'s own page, S is a secondary source such as a news report, magazine or encyclopedia. I read pages through a summarizing tool, so check figures against the original before citing.</p>' + sources_html(B_SOURCES) + "</section>"
)
assert b_n == 11, b_n

B_CFG = {
    "shell": {
        "@@TITLE@@": "Nature Defended",
        "@@ACC@@": "#1f5f99", "@@ACCD@@": "#7fb6e8",
        "@@KICKER@@": "Evidence brief: the living world",
        "@@H1@@": "Nature defended",
        "@@SUB@@": "Eleven defenses of species, land, forests and oceans, and where they fall short",
        "@@LEDE@@": "Protected areas, a whaling ban, the High Seas Treaty, forest monitoring, restoration law and the money behind them. Each entry says what exists, what the evidence shows it has done and how solid that evidence is. A section near the end lists where the defenses are thinning.",
        "@@ASOF@@": "Figures current to 13 October 2026. The framework's global review opens on 19 October, so its verdict is not yet in.",
        "@@NAV@@": nav([("results", "Results"), ("defenses", "The defenses"), ("thinning", "Where they thin"), ("patterns", "Patterns"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Two statements are general knowledge and were not tied to a fetched source: that the Global Biodiversity Framework was adopted in 2022 and that the Montreal Protocol dates from 1987. The 1.6 percent and 68 percent bars are my arithmetic, as is the gap I noted between the Amazon alert percentages. The observations under “What the defenses have in common” are my reading. I read the plastics-treaty session date as 2026 from the page's retrieval date, which the page does not state outright.",
    },
    "body": B_BODY,
}
build(B_CFG, "nature-defended.html")
print("B entries", b_n)


# =====================================================================
# CHAPTER C: NATURE'S CATASTROPHES (record)
# =====================================================================
C_STATS = [
    ("About 81%", "of marine species lost in the End-Permian extinction, about 252 million years ago"),
    ("About 75%", "of species lost when the asteroid struck 66 million years ago"),
    ("About 65%", "of the world's megafaunal species lost in the late Pleistocene, from about 50,000 years ago"),
    ("3 billion → 0", "passenger pigeons, from the most abundant bird in North America to the death of the last captive bird in 1914"),
]
C_C1 = [
    ("End-Ordovician", "About 445 million years ago · 85% of species", 85, 85, False, 85),
    ("End-Permian", "About 252 million years ago · 81% of marine species", 81, 81, False, 81),
    ("End-Cretaceous", "66 million years ago · about 75%", 75, 75, False, 75),
    ("End-Triassic", "About 201 million years ago · 70–75%", 70, 75, False, None),
    ("Late Devonian", "Two pulses, 372 and 359 million years ago · at least 70%", 70, 70, True, 70),
]
C_C2 = [
    ("End-Permian: global marine diversity", "Back to pre-extinction levels about 75 million years later", 0, 75, False, None),
    ("End-Permian: land vertebrates", "About 30 million years to recover fully", 0, 30, False, None),
    ("End-Permian: most marine communities", "About 10 million years by some estimates, to the Middle Triassic", 0, 10, True, None),
    ("K-Pg: lizards and snakes", "About 10 million years", 0, 10, False, None),
    ("K-Pg: forest plant diversity", "About 6 million years", 0, 6, False, None),
    ("PETM: climate back near its start", "Under 100,000 years, by helium-3 records", 0, 0.1, True, None),
]
C_C3 = [
    ("Passenger pigeon", "From about 3 billion; extinct 1914", 0, 100, False, None),
    ("American bison", "From about 60 million to 541 at the low point; the figure is rough", 0, 99.99, True, None),
    ("Aral Sea surface area", "About 10% of its original size by 2007", 0, 90, False, None),
    ("Megafauna, South America", "Share of megafaunal species lost", 0, 83, False, None),
    ("Megafauna, North America", "Share of megafaunal species lost", 0, 72, False, None),
    ("Dust Bowl topsoil", "More than 75% in many regions; the claim is uncited", 0, 75, True, None),
]

C_AREAS = [
    ("Deep time", [
        ("About 445 million years ago", "Mass extinction", "End-Ordovician extinction",
         "Two pulses of loss ended the Ordovician. One estimate puts the loss at 27 percent of families, 57 percent of genera and 85 percent of species.",
         [("Causes", "The first pulse is linked to cooling and glaciation. A 2020 study instead favoured warming, volcanism and oxygen loss, which conflicts with earlier work. A later proposal links volcanic ash to carbon dioxide reduction, glaciation and anoxia."),
          ("Range", "Genus losses run from 42–46 percent in one estimate to 57 percent in another.")],
         "Contested. The figures depend on the method, the taxonomic unit and the correction for sampling bias, and the page says the Big Five are not sharply defined and sit in a continuum with many smaller events."),
        ("372 and 359 million years ago", "Mass extinction", "Late Devonian extinction",
         "Two pulses, the Kellwasser and the Hangenberg, together removed about 19 percent of families, about 50 percent of genera and at least 70 percent of species.",
         [("Causes", "Oxygen-poor ocean events, possibly driven by volcanism, weathering by land plants and climate change. Kellwasser may have involved algal blooms fed by river nutrients."),
          ("Range", "Kellwasser genus loss ranges from 16–20 percent in one estimate to 40 percent in another.")],
         "Contested. A supernova has been proposed for the Hangenberg pulse, which the page calls speculative, and the exact mechanisms remain debated."),
        ("About 252 million years ago", "Mass extinction", "End-Permian extinction, the Great Dying",
         "The greatest of the Big Five removed about 81 percent of marine species and about 70 percent of terrestrial vertebrate species. It was also the largest known extinction of insects. The main marine pulse fell within an interval of 60,000 to 100,000 years.",
         [("Cause", "Flood basalt eruptions that formed the Siberian Traps released sulfur dioxide and carbon dioxide, leading to warming, acidified oceans and oxygen-starved, sulfurous seas. Carbon dioxide rose from about 400 to about 2,500 parts per million and temperatures by about 8 °C."),
          ("Recovery", "About 10 million years for most marine communities by some estimates, about 30 million for land vertebrates, and about 75 million for global marine diversity to regain its earlier level.")],
         "Partly settled and partly not. Earlier marine estimates of 90–96 percent were later attributed to confusing this event with an earlier one, plant losses are disputed, and whether land and sea losses were simultaneous is contested."),
        ("About 201 million years ago", "Mass extinction", "End-Triassic extinction",
         "The event removed about 23 percent of families, 48 percent of genera and 70 to 75 percent of species. Marine genus loss is put at 55 percent.",
         [("Causes", "Volcanic activity, oxygen loss and warming. Falls in sea level are also associated with the event.")],
         "Estimates vary with the method: genus loss runs from 37 percent in one estimate to 73 percent in another."),
        ("66 million years ago", "Mass extinction", "End-Cretaceous extinction",
         "About 75 percent of plant and animal species were lost. It is generally thought that an asteroid 10 to 15 kilometres wide struck the Yucatán Peninsula and caused a lingering impact winter, and a 2010 panel of 41 scientists endorsed that view.",
         [("Lost", "All non-avian dinosaurs, pterosaurs, mosasaurs, plesiosaurs and ammonites, about 60 percent of late-Cretaceous coral genera and about 98 percent of colonial coral species."),
          ("Survived", "Birds, small mammals, more than 80 percent of turtle species and about half of crocodile-group species."),
          ("Recovery", "Forest plant diversity took about 6 million years to return, and lizards and snakes about 10 million.")],
         "The asteroid is widely accepted as the cause, though whether it was the only one is disputed. Volcanism in the Deccan Traps, climate change and sea-level change are proposed as contributing factors."),
        ("About 55.8 million years ago", "Warming event", "Paleocene–Eocene Thermal Maximum",
         "Global temperature rose by 5 to 8 °C in one estimate and by 3 to 6 °C in another, as an estimated 2,000 to 7,000 gigatons of carbon entered the air and ocean. Benthic foraminifera, small seabed animals, suffered a 35 to 50 percent extinction over about 1,000 years, and seawater pH fell by about 0.46 units.",
         [("Land", "Many mammal lineages shrank in size, palms and broadleaf forests spread into the Arctic, and freshwater animals suffered mass deaths from toxic cyanobacterial blooms."),
          ("Duration", "About 200,000 years, 170,000 or 83,000 depending on the method, with an onset under 20,000 years in the helium-3 record."),
          ("Rate", "The page gives peak carbon injection of 0.3 to 1.7 petagrams a year and notes that present emissions exceed 10 gigatons of carbon a year.")],
         "The age is uncertain, the size of the warming is disputed, and the page says acidification may have contributed to the deep-sea extinctions but that temperature, oxygen loss and food supply are also cited. It was not a mass extinction of the scale of the Big Five."),
    ]),
    ("Ice Age to 1900", [
        ("From about 50,000 years ago", "Extinction", "Late Pleistocene megafauna",
         "About 65 percent of megafaunal species worldwide became extinct, 72 percent in North America, 83 percent in South America and 88 percent in Australia. All mammals over 1,000 kilograms were lost in Australia and the Americas.",
         [("When", "Australia and New Guinea from about 50,000 years ago, northern Eurasia between 50,000 and 10,000, North America around 13,800 to 11,400 years ago, and South America after humans arrived about 15,000 years ago."),
          ("Cause", "Debated between human hunting, climate change and a mix of the two. A 2020 study attributed about 96 percent of mammal extinctions over 126,000 years to humans, covering all mammals, not only megafauna. A 2025 review found the literature remained deeply divided.")],
         "Highly contested on cause. Dating is poor in places, especially North America and the Indian subcontinent, and the page uses both 40 and 45 kilograms as the size threshold."),
        ("Late 1800s to 1914", "Extinction", "Passenger pigeon",
         "The species was once the most abundant bird in North America, numbering around 3 billion and possibly up to 5 billion. A slow decline between about 1800 and 1870 became a rapid one between 1870 and 1890.",
         [("End", "The last confirmed wild bird was shot in Indiana in 1902, and the last captive bird, Martha, died at the Cincinnati Zoo on 1 September 1914."),
          ("Causes", "Hunting, which supplied a cheap meat market, together with the loss of the large breeding populations the species needed and widespread deforestation.")],
         "From Wikipedia. The peak population is an estimate, given as 3 billion and possibly up to 5 billion."),
        ("1800s", "Population collapse", "American bison",
         "The population is put at about 60 million before the 1870s and as low as 541 animals by 1889. The page attributes the fall to commercial hunting and to cattle diseases, and says the killing was part of the genocide of Native Americans, for whom the bison was a central resource.",
         [("Now", "About 31,000 wild bison in 2019 and about 500,000 in total in 2017 including private herds. IUCN counts roughly 15,000 wild, free-range animals, and as few as 12,000 to 15,000 are genetically pure.")],
         "Weak. The 60 million rests on a single observation from 1871, and the page's own low-point numbers conflict, with 541 in 1889 against 325 in 1884 and 395,000 in 1880."),
    ]),
    ("1930 to 1990", [
        ("1930–1940", "Soil loss", "Dust Bowl",
         "Waves of drought in 1934, 1936 and 1939–1940, combined with deep plowing that removed the native grasses, affected 100 million acres, about 400,000 square kilometres, centred on the Texas and Oklahoma panhandles. More than 500,000 Americans were left homeless, and about 3.5 million people left the Plains states between 1930 and 1940.",
         [("Soil", "In many regions more than 75 percent of the topsoil was blown away by the end of the 1930s, a claim the page marks as needing a citation."),
          ("Response", "The Soil Erosion Service was created in 1933 and renamed the Soil Conservation Service in 1935. The Civilian Conservation Corps planted a shelterbelt of more than 200 million trees, and by 1938 blowing soil had been reduced by 65 percent."),
          ("Cost", "By 1940 farmland values in high-erosion counties had fallen 28 percent relative to low-erosion counties, and less than a quarter of the original agricultural losses were recovered in the most eroded areas.")],
         "From Wikipedia. The topsoil figure is uncited there. The page also notes that regular rainfall returned in fall 1939."),
        ("1960 onward", "Ecosystem loss", "Aral Sea",
         "Soviet cotton irrigation diverted the two rivers that fed the sea. From 1960 to 1998 its surface area fell by 60 percent and its volume by 80 percent, and by 2007 it was about 10 percent of its original size, split into four lakes. The eastern basin of the South Aral dried up completely in August 2014.",
         [("Life", "Salinity rose from about 10 to about 30 grams a litre by 1990. A fishing industry that employed about 40,000 people and produced a sixth of the Soviet catch ended by 1987, and all native sturgeon species died out."),
          ("Recovery", "Kazakhstan finished a dam in 2005 that separated the North Aral. Its level rose 12 metres by 2008, salinity fell to about 8 grams a litre, and almost 24 freshwater species returned. The South Aral remains largely dry.")],
         "From Wikipedia. The page ranks the lake third-largest in one place and fourth-largest in another, and gives the original area as 68,000 square kilometres."),
        ("1962–1972", "Chemical poisoning", "DDT and birds of prey",
         "DDT and its breakdown products caused eggshell thinning and population declines in several North American and European birds of prey. Peregrine falcon, bald eagle, osprey and brown pelican eggshells often cracked before hatching, and DDE is considered a major reason for the bald eagle's decline.",
         [("Response", "Rachel Carson's Silent Spring appeared in 1962. In summer 1972 the US Environmental Protection Agency cancelled most DDT uses, and a federal appeals court upheld the action in 1973."),
          ("After", "The page says the restrictions aided the recovery of endangered species but gives no population figures.")],
         "From Wikipedia. It gives the causal chain and the dates but no counts, so I cannot say by how much any species fell or recovered."),
        ("1985", "Atmospheric damage", "Antarctic ozone hole",
         "British Antarctic Survey scientists Farman, Gardiner and Shanklin reported the hole in Nature in May 1985. Chlorine from chlorofluorocarbons destroys ozone, and the cold Antarctic spring greatly enhances the process. 43 nations signed the Montreal Protocol in 1987.",
         [("Size", "The seasonal maximum was 21.2 million square kilometres in 2012, and the hole was one of the largest on record at 26 million square kilometres in September 2023."),
          ("Outlook", "A 2023 UN assessment projects Antarctic ozone to return to 1980 levels around 2066.")],
         "From Wikipedia. The page gives the discovery date as both 1982 and 1985. The treaty and its effect are covered in the chapter on nature defended."),
    ]),
    ("1990 onward", [
        ("1993 onward", "Disease", "Chytrid fungus and amphibians",
         "The epizootic form of the chytrid fungus disease was first discovered in 1993 in dead and dying frogs in Queensland, Australia. A 2019 review in Science linked it to the decline of at least 501 amphibian species over 50 years, 90 of them confirmed or presumed extinct in the wild and 124 down by more than 90 percent.",
         [("Spread", "The fungus has been detected in 56 of 82 countries and in 516 of 1,240 species tested, though its presence does not always mean disease.")],
         "Contested. A follow-up comment in Science said the 2019 study lacked the evidence for its claims and could not reproduce its conclusions, and the page says it remains unclear how many and which species have been affected."),
        ("2010", "Industrial accident", "Deepwater Horizon oil spill",
         "The US government estimated that 4.9 million barrels of oil were discharged over 87 days, a figure BP argued was too high. Eleven workers died. Satellite images showed the spill directly affected about 180,000 square kilometres of ocean.",
         [("Birds", "NOAA estimated between 51,000 and 84,000 killed. Three researchers estimated more than a million coastal birds."),
          ("Other", "NOAA estimated 56,000 to 166,000 juvenile sea turtles killed, up to a 51 percent decline in the Barataria Bay dolphin population, and 2 to 5 trillion newly hatched fish."),
          ("Disputes", "Estimates of the oil that remained ranged from about half to 75 percent, scientists disagreed about the effect of dispersants and about how much microbes broke down the oil, and BP called a 2013 dolphin study inconclusive.")],
         "Estimates differ widely and several are disputed by BP. The page gave 19 September as the date the well was sealed; the 20 April start is general knowledge."),
        ("2019–2020", "Wildfire", "Australian bushfires",
         "The fires burned more than 24 million hectares, and the state total on 14 January 2020 was 18.6 million hectares. An estimated three billion terrestrial vertebrates, mostly reptiles, were killed or displaced. Some species may have been driven to extinction, with glossy black cockatoos, Kangaroo Island dunnarts and koalas named as being of concern.",
         [("People", "33 direct deaths and 417 indirect deaths from smoke are listed in the infobox, while the state table totals 34 fatalities."),
          ("Estimate", "University of Sydney ecologists first estimated 480 million mammals, birds and reptiles lost, a figure later expanded to more than a billion.")],
         "The animal figures are estimates that rose sharply, and the page gives no method or confidence range for either. I did not find the page's account of the causes of the fires."),
    ]),
]

C_PATTERNS = [
    ("Every deep-time event has an environmental shock behind it", "The six events before humans each have a change in climate or ocean chemistry among their proposed causes: glaciation, oxygen loss, volcanic carbon dioxide, warming, acidification or an impact winter."),
    ("Recovery takes millions of years", "After the End-Permian, most marine communities took about 10 million years, land vertebrates about 30 million and global marine diversity about 75 million to regain earlier levels. After the asteroid, forests took about 6 million years."),
    ("In the human era, the pages name human action for most events", "For seven of the ten events since 50,000 years ago, the pages I read name human action among the causes. The megafauna case is debated, and for the chytrid fungus and the 2019–20 fires the pages gave no cause."),
    ("Four entries record a response after which the measure improved", "Blowing soil fell 65 percent by 1938 after the Dust Bowl response, DDT uses were cancelled in 1972, the Montreal Protocol was signed in 1987, and the North Aral Sea partly refilled after a dam. In each case the cause was one that could be named and acted on."),
    ("The numbers are soft", "Estimates for the same event differ widely: Permian marine losses were once put at 90–96 percent, Deepwater Horizon bird deaths at 51,000–84,000 or more than a million, and the bison's starting population rests on one observation."),
]

C_LIMITS = [
    "The list is my selection. Sixteen events cannot cover the record of damage to the living world.",
    "The fossil record is biased by what preserves well, so the deep-time shares are estimates that depend on the method and the taxonomic unit.",
    "Not covered: the other deep-time events such as the end-Capitanian, the Holocene island extinctions such as the dodo and the moa, and other modern cases such as the collapse of the Atlantic cod fishery.",
    "Almost every entry rests on a Wikipedia summary, read through a summarizing tool. They need checking against the original studies before use.",
    "A record kept after the fact covers only what was measured or preserved, so the earlier entries in particular are the ones that left a trace.",
]

C_SOURCES = [
    ("Deep time", [
        ("https://en.wikipedia.org/wiki/Extinction_event", "Wikipedia, Extinction event", "S"),
        ("https://en.wikipedia.org/wiki/Permian%E2%80%93Triassic_extinction_event", "Wikipedia, Permian–Triassic extinction event", "S"),
        ("https://en.wikipedia.org/wiki/Cretaceous%E2%80%93Paleogene_extinction_event", "Wikipedia, Cretaceous–Paleogene extinction event", "S"),
        ("https://en.wikipedia.org/wiki/Paleocene%E2%80%93Eocene_Thermal_Maximum", "Wikipedia, Paleocene–Eocene Thermal Maximum", "S"),
        ("https://en.wikipedia.org/wiki/Quaternary_extinction_event", "Wikipedia, Quaternary extinction event", "S")]),
    ("Human era", [
        ("https://en.wikipedia.org/wiki/Passenger_pigeon", "Wikipedia, Passenger pigeon", "S"),
        ("https://en.wikipedia.org/wiki/American_bison", "Wikipedia, American bison", "S"),
        ("https://en.wikipedia.org/wiki/Dust_Bowl", "Wikipedia, Dust Bowl", "S"),
        ("https://en.wikipedia.org/wiki/Aral_Sea", "Wikipedia, Aral Sea", "S"),
        ("https://en.wikipedia.org/wiki/DDT", "Wikipedia, DDT", "S"),
        ("https://en.wikipedia.org/wiki/Ozone_depletion", "Wikipedia, Ozone depletion", "S"),
        ("https://en.wikipedia.org/wiki/Chytridiomycosis", "Wikipedia, Chytridiomycosis", "S"),
        ("https://en.wikipedia.org/wiki/Deepwater_Horizon_oil_spill", "Wikipedia, Deepwater Horizon oil spill", "S"),
        ("https://en.wikipedia.org/wiki/2019%E2%80%9320_Australian_bushfire_season", "Wikipedia, 2019–20 Australian bushfire season", "S")]),
]

c_groups, c_n = groups_html(C_AREAS)
assert c_n == 16, c_n
C_BODY = (
    section("scale", "How large they were", "", stats_html(C_STATS)
            + chart_block("Share of species lost in the Big Five mass extinctions",
                          "Each bar is the share of species lost in the best-known estimate. The black line marks it. The hatched bar is a lower limit ('at least'). The Ordovician and Devonian rows are the least certain, since their genus estimates vary widely.",
                          chart_html(C_C1, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Range chart of species lost in five mass extinctions, from at least 70 percent to 85 percent"))
            + chart_block("How long recovery took, in millions of years",
                          "Different measures of recovery, so compare the lengths, not the events. Hatched bars are the less certain: 'by some estimates' for the marine communities, and a very short bar for the PETM, about 0.1 million years, from one helium-3 record.",
                          chart_html(C_C2, [(0, "0"), (20, "20"), (40, "40"), (60, "60"), (80, "80")], 80, "Bar chart of recovery times from 0.1 million years after the PETM to about 75 million years for marine diversity after the End-Permian"))
            + chart_block("Share lost in the human-era events",
                          "These measure different things: a species, a population, an area, topsoil. Read each label. Hatched bars are rough or uncited figures.",
                          chart_html(C_C3, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of losses in six human-era events, from 72 percent of North American megafauna to the total loss of the passenger pigeon")))
    + section("events", "The events", "Sixteen events in four periods. Each gives the scale, the cause, what followed and how solid the figures are.", c_groups)
    + section("patterns", "What the record shows", "", '<p class="note">These are my reading of the entries, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in C_PATTERNS) + "</div>")
    + section("limits", "What this record cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in C_LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: S is a secondary source. Every source here is an encyclopedia article, read through a summarizing tool, so check figures against the original studies before citing.</p>' + sources_html(C_SOURCES) + "</section>"
)
C_CFG = {
    "shell": {
        "@@TITLE@@": "Nature's Catastrophes",
        "@@ACC@@": "#7a3b7a", "@@ACCD@@": "#d49ad4",
        "@@KICKER@@": "Evidence brief: the record of the living world",
        "@@H1@@": "Nature's catastrophes",
        "@@SUB@@": "Sixteen events, from a mass extinction 445 million years ago to the 2019–20 Australian fires",
        "@@LEDE@@": "Mass extinctions, a warming event, the loss of the megafauna, collapses of single species and ecosystems, and chemical, industrial and wildfire disasters, in date order. Each entry gives the scale, the cause, what followed and how reliable the numbers are.",
        "@@ASOF@@": "Figures current to 27 October 2026. Every source is an encyclopedia article; see the notes on source quality at the end.",
        "@@NAV@@": nav([("scale", "Scale"), ("events", "The events"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several statements are general knowledge and were not tied to a fetched source: that the Deepwater Horizon blowout began on 20 April 2010. The observations under “What the record shows”, the count of seven of ten events with named human causes, and the placement of the Aral Sea bar at 90 percent (the source says about 10 percent of the original size remained by 2007) are my own reading or arithmetic.",
    },
    "body": C_BODY,
}
build(C_CFG, "natures-catastrophes.html")
print("C entries", c_n)
