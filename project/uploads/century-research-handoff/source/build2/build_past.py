import html, math, os
e = html.escape
OUT = os.path.dirname(os.path.abspath(__file__))

CATS = ["Natural hazard", "Disease", "Conquest and enslavement", "War", "Famine", "Industrial accident", "Collapse"]

# sort, date, title, cat, where, story, {scale, spread, cause, after}, solid
EV = [
(-72000, "c. 74,000 years ago", "Toba eruption", "Natural hazard", "Sumatra, Indonesia",
 "The eruption rated VEI 8, the top of the scale, and is the largest known explosive eruption of the Quaternary. One theory holds that it caused a volcanic winter of six to ten years and cut the human population to a few thousand people.",
 [("Scale", "About 3,800 cubic kilometres of erupted material by the latest estimate. Earlier estimates ran from 2,000 to 6,000."),
  ("Cause", "Natural."),
  ("Aftermath", "Unknown. The population bottleneck was proposed by Ambrose in 1998.")],
 "Very contested. Models bring cooling back to normal within about five years, lake records in Malawi show no major ecological change, and stone tools in India look the same above and below the ash. Some researchers consider the theory disproved."),

(-1200, "c. 1200 BCE", "Late Bronze Age collapse", "Collapse", "Eastern Mediterranean and Near East",
 "Between the late 13th and early 12th centuries BCE, the palace economies of the region broke down. Mycenaean Greece gave way to small village cultures, the Hittite empire collapsed, and Assyria and Egypt survived in weakened form.",
 [("Scale", "Many societies across Egypt, Anatolia, the Aegean, the Levant and Mesopotamia. Effects varied, and Cyprus saw little destruction."),
  ("Cause", "Several, and still debated: drought and a cooler climate, invasions by the Sea Peoples, military change, the spread of iron, and possibly plague. Deep trade and diplomatic links meant that a disturbance in one place cascaded to others."),
  ("Aftermath", "Greece entered the Dark Ages. Phoenician city-states gained autonomy as Egyptian and Assyrian power waned.")],
 "Scholars now see the collapse as more limited than older accounts claimed, because many supposed city destructions were misdated or never happened. There is no death toll."),

(541, "541–549", "Plague of Justinian", "Disease", "Mediterranean, Near East, Europe",
 "Plague reached Roman Egypt in 541 and by 543 had spread to every corner of Justinian's empire. Constantinople lost about a fifth of its people by one account and up to 40 percent by another.",
 [("Spread", "Contemporary sources say it came on rats and fleas aboard grain ships from Egypt, a major import for the Byzantines."),
  ("Scale", "For the first plague pandemic as a whole, some historians estimate 15 to 100 million deaths over two centuries."),
  ("Aftermath", "The disease persisted in Northern Europe and Arabia until 549.")],
 "Heavily debated. Revisionist historians argue that the plague caused high mortality in some places but no widespread demographic decline. Procopius reported 10,000 deaths a day in Constantinople, a figure whose accuracy is in question."),

(1206, "1206–1405", "Mongol conquests", "Conquest and enslavement", "Eurasia",
 "Campaigns led by Genghis Khan, Kublai Khan and Timur destroyed cities that resisted. Large areas of Central Asia and northeastern Persia were seriously depopulated.",
 [("Scale", "Possibly 20 to 60 million killed over two centuries, not counting Black Death deaths."),
  ("Cause", "Military conquest.")],
 "Weak. The estimates come from a book criticized for its methods and rely on Chinese censuses that are considered unreliable. Contemporary records are scarce."),

(1346, "1346–1353", "Black Death", "Disease", "Eurasia and North Africa",
 "Plague reached Europe through the Genoese trading port of Caffa in Crimea and spread through the Mediterranean to North Africa, West Asia and the rest of Europe.",
 [("Spread", "Fleas on black rats aboard ships, moving through trading ports."),
  ("Scale", "25 to 50 million deaths in one estimate, and 75 to 200 million across Eurasia in another. Europe lost 30 to 60 percent of its people by one account and 25 to 60 percent by another. About a third of the Middle Eastern population died."),
  ("Aftermath", "Europe's population did not regain its 14th-century level until the 16th century.")],
 "Ranges are wide because few records survive. The highest and lowest totals differ by a factor of up to eight."),

(1492, "From 1492", "Population collapse in the Americas", "Conquest and enslavement", "North and South America",
 "After 1492, the Indigenous population of the Americas fell sharply. Lower estimates imply a decline of about 80 percent by the late 17th century in Central and South America, and some researchers say about 90 percent within a century of Columbus's arrival.",
 [("Scale", "Pre-contact estimates run from 8 to 112 million, with recent ones mostly between 45 and 60 million. Regional figures include a 50 to 80 percent die-off in 16th-century Mexico and a drop in Brazil from about 4 million to 300,000."),
  ("Cause", "Epidemic disease, enslavement, war, forced labor and displacement. Scholars disagree about the weight of each, and many argue that colonial disruption made communities more vulnerable to disease.")],
 "Weak. The estimates are extrapolations from small bits of data. A 2020 genetic study suggests earlier Caribbean estimates may have been at least tenfold too large."),

(1500, "16th–19th centuries", "Atlantic slave trade", "Conquest and enslavement", "Africa to the Americas",
 "About 12.75 million Africans were loaded onto slave ships bound for the Americas, by the current estimate. The trade peaked in the last two decades of the 18th century.",
 [("Scale", "Up to 2 million died on the voyage. Another historian estimates that about 4 million more died inside Africa after capture, which gives roughly 1.5 to 5.5 million deaths depending on what is counted (my arithmetic)."),
  ("Cause", "An organized human trade."),
  ("Aftermath", "Britain banned the trade in 1807, and participating nations had completely banned it by 1853.")],
 "The embarkation figure rests on ship records, though studies differ (about 12 million in one, 12.75 million in another). Deaths inside Africa are a much weaker estimate."),

(1815, "1815–1816", "Tambora and the year without a summer", "Natural hazard", "Indonesia and the Northern Hemisphere",
 "The 1815 eruption of Tambora rated VEI 7 and is the most recent confirmed eruption of that size. It lowered the global average temperature by 0.4 to 0.7 °C, and in 1816 harvests failed across New England and Europe.",
 [("Scale", "In New England, no more than a quarter of the corn ripened enough to use for food. Wheat, oat and potato harvests failed in Britain and Ireland."),
  ("Aftermath", "Typhus epidemics followed the famine between 1816 and 1819, and more than 65,000 people died as the disease spread out of Ireland. The cooling itself was temporary.")],
 "The source gives no overall death toll."),

(1845, "1845–1852", "Irish Great Famine", "Famine", "Ireland",
 "Potato blight, which probably arrived in 1844, struck a population that depended on a single crop and on absentee landlords. The worst year was 1847.",
 [("Scale", "About 1 million deaths, within a plausible range of 0.5 to 1.5 million, and more than 1 million emigrants. At least 2.1 million people left Ireland between 1845 and 1855."),
  ("Cause", "Blight, made far worse by landlordism and dependence on one crop. The government followed a laissez-faire policy and ended earlier relief, and large food exports continued."),
  ("Aftermath", "Ireland's population fell 20 to 25 percent between 1841 and 1871, from about 8.5 million before the famine to 4.4 million by 1901. Marriage ages rose, and a third of Irish men and a quarter of Irish women never married.")],
 "One million is the most widely accepted death toll, with a plausible range of half a million to one and a half million."),

(1850, "1850–1864", "Taiping Rebellion", "War", "China",
 "A civil war between the Qing dynasty and the Taiping Heavenly Kingdom, whose capital Nanjing fell in 1864. About 30 million people fled the conquered regions, and the last rebel forces were defeated in 1871.",
 [("Scale", "The most widely cited estimate is 20 to 30 million deaths, which the source puts at 5 to 10 percent of China's population. Higher estimates run from 73 to 100 million.")],
 "Speculative. There was no reliable census, and only about 10 percent of Taiping records survive."),

(1900, "20th century", "Smallpox", "Disease", "Worldwide",
 "Smallpox was still killing people at scale in the 1900s. Ordinary smallpox killed about 30 percent of those infected.",
 [("Scale", "250 to 500 million deaths in the 20th century by one estimate. Another figure often quoted is up to 300 million."),
  ("Cause", "A virus spreading from person to person."),
  ("Aftermath", "The WHO certified global eradication in May 1980.")],
 "Estimates vary widely."),

(1914, "1914–1918", "World War I", "War", "Europe, the Middle East, Africa, Asia",
 "A war among industrial powers killed 15 to 22 million people, military and civilian combined.",
 [("Scale", "About 1.7 to 2.3 percent of the population of the countries involved, which together held 959.7 million people.")],
 "The share is calculated against the countries listed in the source, not the world population."),

(1918, "1918–1920", "Influenza pandemic", "Disease", "Worldwide",
 "The pandemic is conventionally dated from a case at Camp Funston, Kansas, on 4 March 1918. The virus spread with troop movements to other American camps and to Europe, reaching the Western Front by mid-April.",
 [("Spread", "A second wave likely reached Boston and Freetown, Sierra Leone, by ship from Brest. After the Treaty of Brest-Litovsk, released Russian prisoners of war carried the disease home."),
  ("Scale", "About 500 million people were infected, nearly a third of the world's population. Deaths of 25 to 50 million are generally accepted, with other estimates from 17 million to 100 million.")],
 "Weak at the edges. Limited data leave the origin uncertain, estimates for China are unreliable, and the authors of one Russian estimate (450,000 deaths) called it a shot in the dark."),

(1939, "1939–1945", "World War II", "War", "Worldwide",
 "The deadliest conflict in the record, including deaths from deprivation, famine and disease.",
 [("Scale", "60 to 75 million deaths in one estimate and 70 to 85 million in another, about 3 percent of the 2.3 billion people alive in 1940.")],
 "The two ranges in the source differ, so the share is 3.0 to 3.7 percent depending on which is used."),

(1943, "1943", "Bengal famine", "Famine", "Bengal, British India",
 "Famine struck Bengal, a province of about 60 million people, during the Second World War. The fall of Burma cut off rice imports, a cyclone and crop disease reduced the 1942 harvest, and British wartime denial policies removed rice and seized about 45,000 boats.",
 [("Scale", "Estimated deaths range from 0.8 to 3.8 million, and the scholarly consensus is about 2.1 million."),
  ("Cause", "Debated. The Famine Inquiry Commission called it a crisis of the distribution of food and income, not of availability. Amartya Sen argued that the 1943 rice supply was only about 5 percent below the previous five-year average, while others estimated shortfalls of 20 to 33 percent. Wartime inflation cut real wages, and historians disagree about the role of the British War Cabinet in refusing or cutting import requests.")],
 "The death toll is accepted within a range. The causes are actively disputed."),

(1958, "1958–1962", "Great Chinese Famine", "Famine", "China",
 "Famine deaths began in 1958 and lasted until 1962, with the core period from 1959 to 1961. Harvests fell 15 percent in 1959 against 1958, and 1960 output was about 70 percent of the 1958 level. Grain exports continued.",
 [("Scale", "The commonly cited range is 15 to 46 million excess deaths. Newer estimates cluster around 30 to 46 million, and published estimates run from 3.5 million to 55 million."),
  ("Cause", "Government policy, including the Great Leap Forward, communes, extreme grain procurement and overreported grain output, together with drought and floods. One study attributes 69 percent of deaths to policy and 31 percent to natural disasters, and the weather's role is debated.")],
 "Highly disputed. Scholars have criticized several of the highest estimates for weak methods."),

(1984, "1984", "Bhopal gas leak", "Industrial accident", "Bhopal, India",
 "On 2 and 3 December 1984, methyl isocyanate gas escaped from a storage tank at the Union Carbide pesticide plant after water entered the tank and set off a runaway reaction. More than 500,000 people were exposed.",
 [("Scale", "Official immediate deaths were 2,259, and the Madhya Pradesh government later confirmed 3,787. Other estimates run to about 8,000 within two weeks plus 8,000 or more from gas-related disease, and some claims exceed 16,000. A 2006 government affidavit reported at least 558,125 injuries, about 3,900 of them severe and permanently disabling."),
  ("Cause", "An overfilled tank, malfunctioning safety systems and poor maintenance. How the water entered is disputed: investigators cite pipe cleaning, and the company cites sabotage.")],
 "Estimates of the death toll differ by a factor of about seven."),

(1986, "1986", "Chernobyl disaster", "Industrial accident", "Ukraine, then the Soviet Union",
 "On 26 April 1986, reactor 4 exploded during a safety test, started a core fire and spread radioactive contamination across the Soviet Union and Europe. It is rated level 7, the maximum on the international scale.",
 [("Scale", "Two workers died in the explosions and 28 more of acute radiation syndrome within three months. About 135,000 people were evacuated long term, about 100,000 square kilometres were contaminated, and the exclusion zone covers about 2,600 square kilometres."),
  ("Cause", "Reactor design flaws and operator actions.")],
 "Long-term deaths are contested. The UN figure is up to 4,000 in Ukraine, Belarus and Russia, other assessments reach 16,000 across Europe, and a few studies propose hundreds of thousands, which are widely disputed on method."),

(2020, "2020–2021", "COVID-19 pandemic", "Disease", "Worldwide",
 "The WHO declared a pandemic about three months after the first reports.",
 [("Scale", "The WHO estimated 14.9 million excess deaths associated with COVID-19 in 2020 and 2021.")],
 "I read only the WHO headline, not the full report. Excess deaths are counted as deaths associated with the pandemic, so the figure covers more than deaths caused directly by the virus."),
]

GROUPS = [("Before 1000", -10**9, 1000), ("1000 to 1800", 1000, 1800), ("1800 to 1900", 1800, 1900), ("1900 onward", 1900, 10**9)]

# Deaths chart: name, sub, lo, hi, hatch
DEATHS = [
 ("Plague of Justinian", "541–549 · 15–100M over two centuries", 15e6, 100e6, True),
 ("Mongol conquests", "1206–1405 · 20–60M", 20e6, 60e6, True),
 ("Black Death", "1346–53 · 25–50M (other: 75–200M)", 25e6, 50e6, False),
 ("Atlantic slave trade", "16th–19th c. · 1.5–5.5M", 1.5e6, 5.5e6, False),
 ("Irish Great Famine", "1845–52 · 0.5–1.5M", 0.5e6, 1.5e6, False),
 ("Taiping Rebellion", "1850–64 · 20–100M (most cited 20–30M)", 20e6, 100e6, True),
 ("Smallpox", "20th century · 250–500M", 250e6, 500e6, False),
 ("World War I", "1914–18 · 15–22M", 15e6, 22e6, False),
 ("Influenza pandemic", "1918–20 · 17–100M (accepted 25–50M)", 17e6, 100e6, False),
 ("World War II", "1939–45 · 60–85M", 60e6, 85e6, False),
 ("Bengal famine", "1943 · 0.8–3.8M", 0.8e6, 3.8e6, False),
 ("Great Chinese Famine", "1958–62 · 3.5–55M", 3.5e6, 55e6, True),
 ("Bhopal gas leak", "1984 · 2,259 to over 16,000", 2259, 16000, False),
 ("Chernobyl", "1986 · 30 immediate, up to 16,000 long term", 30, 16000, False),
 ("COVID-19", "2020–21 · 14.9M excess deaths", 14.9e6, 14.9e6, False),
]
LMIN, LMAX = 1, 9  # log10(10) .. log10(1e9)

SHARES = [
 ("Americas after 1492", "80–90% of the Indigenous population", 80, 90, True),
 ("Black Death", "30–60% of Europe", 30, 60, False),
 ("Plague of Justinian", "20–40% of Constantinople", 20, 40, True),
 ("Irish Great Famine", "20–25% of Ireland, deaths and emigration", 20, 25, False),
 ("Taiping Rebellion", "5–10% of China (base not stated)", 5, 10, True),
 ("World War II", "3.0–3.7% of the world", 3.0, 3.7, False),
 ("World War I", "1.7–2.3% of countries involved", 1.7, 2.3, False),
 ("Bengal famine", "1.3–6.3% of Bengal (my arithmetic)", 1.3, 6.3, False),
 ("COVID-19", "about 0.2% of the world (my arithmetic)", 0.2, 0.2, False),
]

def logpos(v):
    return (math.log10(v) - LMIN) / (LMAX - LMIN) * 100

def deaths_html():
    ticks = [(10, "10"), (100, "100"), (1e3, "1K"), (1e4, "10K"), (1e5, "100K"), (1e6, "1M"), (1e7, "10M"), (1e8, "100M"), (1e9, "1B")]
    ax = "".join('<span style="left:%.3f%%">%s</span>' % (logpos(v), t) for v, t in ticks)
    rows = [
        '<div class="rg-axis"><span></span><div>%s</div></div>' % ax
    ]
    for name, sub, lo, hi, hatch in DEATHS:
        l = logpos(lo)
        w = logpos(hi) - l
        rows.append(
            '<div class="rg-row"><div class="rg-lab"><b>%s</b><small>%s</small></div><div class="rg-track dlog"><i class="rg-bar%s" style="left:%.2f%%;width:%.2f%%"></i></div></div>'
            % (e(name), e(sub), " hatch" if hatch else "", l, w)
        )
    return "".join(rows)

def shares_html():
    ax = "".join('<span style="left:%d%%">%d%%</span>' % (p, p) for p in (0, 25, 50, 75, 100))
    rows = ['<div class="rg-axis"><span></span><div>%s</div></div>' % ax]
    for name, sub, lo, hi, hatch in SHARES:
        rows.append(
            '<div class="rg-row"><div class="rg-lab"><b>%s</b><small>%s</small></div><div class="rg-track"><i class="rg-bar%s" style="left:%.2f%%;width:%.2f%%"></i></div></div>'
            % (e(name), e(sub), " hatch" if hatch else "", lo, max(hi - lo, 0))
        )
    return "".join(rows)

def events_html():
    out = []
    evs = sorted(EV, key=lambda x: x[0])
    for gname, lo, hi in GROUPS:
        items = [x for x in evs if lo <= x[0] < hi]
        if not items:
            continue
        lis = []
        for sort, date, title, cat, where, story, kv, solid in items:
            dl = "".join("<dt>%s</dt><dd>%s</dd>" % (e(k), e(v)) for k, v in kv)
            lis.append(
                '<li class="item" data-c="%s"><div class="when">%s<small>%s</small></div>'
                '<div class="what"><h3>%s</h3><p class="meta">%s</p><p>%s</p><dl class="kv">%s</dl>'
                '<p class="solid"><b>How solid</b> %s</p></div></li>'
                % (e(cat), e(date), e(cat), e(title), e(where), e(story), dl, e(solid))
            )
        out.append('<section class="grp"><h3 class="gh">%s <span>%d events</span></h3><ol class="list">%s</ol></section>' % (e(gname), len(items), "".join(lis)))
    return "\n".join(out)

def chips_html():
    s = '<button class="chip" type="button" data-f="all" aria-pressed="true">All</button>'
    for c in CATS:
        s += '<button class="chip" type="button" data-f="%s" aria-pressed="false">%s</button>' % (e(c), e(c))
    return s

PATTERNS = [
 ("Connection carried disease", "Each of the three great pandemics here travelled on the transport of its day: grain ships from Egypt in 541, Genoese trading ships in 1346, and troop movements and ships in 1918."),
 ("Shortage became famine through decisions", "In Ireland, food exports continued and earlier relief ended. In Bengal, wartime denial policies and inflation are cited, and in China, grain procurement and continued exports. In each case scholars dispute how much of the toll came from policy and how much from blight, weather or war."),
 ("Recovery took generations, or did not come", "Europe regained its pre-plague population in the 16th century. Ireland's decline lasted a century. Greece entered a dark age after the Bronze Age collapse. The cooling after Tambora, by contrast, was temporary."),
 ("The numbers are soft", "Totals for the Black Death differ by up to a factor of eight, for the 1918 influenza about six, for the Taiping Rebellion five, and for the Great Chinese Famine about sixteen. The older or more political the event, the wider the range."),
 ("Industrial technology added a new kind of event", "Bhopal and Chernobyl are the only industrial accidents here, and even on the high estimates their tolls are in the thousands to tens of thousands, not millions. The two world wars were fought by industrial states and killed 15 to 22 million and 60 to 85 million people."),
 ("Most events were regional", "The entries that reached across the world are the 1918 influenza, smallpox, COVID-19 and the world wars. The rest struck a region, a continent or an empire."),
]

LIMITS = [
 "The list is my selection. Nineteen events cannot cover the record.",
 "Records are thinner for events outside Europe, East Asia and the Middle East, so the list probably understates the rest of the world.",
 "Not covered: mass extinctions and other deep-time events, the Antonine plague, the 17th-century crises, and the many earthquakes, floods and regional famines that did not reach this scale.",
 "A record kept by survivors lists only the catastrophes that humanity survived.",
]

SOURCES = [
 ("Natural hazards and collapse", [
  ("https://en.wikipedia.org/wiki/Toba_catastrophe_theory", "Wikipedia, Toba catastrophe theory", "S"),
  ("https://en.wikipedia.org/wiki/Late_Bronze_Age_collapse", "Wikipedia, Late Bronze Age collapse", "S"),
  ("https://en.wikipedia.org/wiki/Year_Without_a_Summer", "Wikipedia, Year Without a Summer", "S")]),
 ("Disease", [
  ("https://en.wikipedia.org/wiki/Plague_of_Justinian", "Wikipedia, Plague of Justinian", "S"),
  ("https://en.wikipedia.org/wiki/Black_Death", "Wikipedia, Black Death", "S"),
  ("https://en.wikipedia.org/wiki/Spanish_flu", "Wikipedia, Spanish flu", "S"),
  ("https://en.wikipedia.org/wiki/Smallpox", "Wikipedia, Smallpox", "S"),
  ("https://www.who.int/news/item/05-05-2022-14.9-million-excess-deaths-were-associated-with-the-COVID-19-pandemic-in-2020-and-2021", "WHO, 14.9 million excess deaths in 2020 and 2021 (headline read, not the full page)", "P")]),
 ("Conquest, enslavement and war", [
  ("https://en.wikipedia.org/wiki/Mongol_invasions_and_conquests", "Wikipedia, Mongol invasions and conquests", "S"),
  ("https://en.wikipedia.org/wiki/Population_history_of_Indigenous_peoples_of_the_Americas", "Wikipedia, population history of Indigenous peoples of the Americas", "S"),
  ("https://en.wikipedia.org/wiki/Atlantic_slave_trade", "Wikipedia, Atlantic slave trade", "S"),
  ("https://en.wikipedia.org/wiki/Taiping_Rebellion", "Wikipedia, Taiping Rebellion", "S"),
  ("https://en.wikipedia.org/wiki/World_War_I_casualties", "Wikipedia, World War I casualties", "S"),
  ("https://en.wikipedia.org/wiki/World_War_II_casualties", "Wikipedia, World War II casualties", "S")]),
 ("Famine and industrial accidents", [
  ("https://en.wikipedia.org/wiki/Great_Famine_(Ireland)", "Wikipedia, Great Famine (Ireland)", "S"),
  ("https://en.wikipedia.org/wiki/Bengal_famine_of_1943", "Wikipedia, Bengal famine of 1943", "S"),
  ("https://en.wikipedia.org/wiki/Great_Chinese_Famine", "Wikipedia, Great Chinese Famine", "S"),
  ("https://en.wikipedia.org/wiki/Bhopal_disaster", "Wikipedia, Bhopal disaster", "S"),
  ("https://en.wikipedia.org/wiki/Chernobyl_disaster", "Wikipedia, Chernobyl disaster", "S")]),
]

def sources_html():
    s = ""
    for h, items in SOURCES:
        s += "<h3>%s</h3><ul>" % e(h)
        for u, t, tag in items:
            s += '<li><a href="%s">%s</a><span>%s</span></li>' % (e(u, quote=True), e(t), tag)
        s += "</ul>"
    return s

TEMPLATE = open(os.path.join(OUT, "past_template.html"), encoding="utf-8").read()

page = TEMPLATE
rep = {
 "@@DEATHS@@": deaths_html(),
 "@@SHARES@@": shares_html(),
 "@@CHIPS@@": chips_html(),
 "@@EVENTS@@": events_html(),
 "@@PATTERNS@@": "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS),
 "@@LIMITS@@": "".join("<li>%s</li>" % e(x) for x in LIMITS),
 "@@SOURCES@@": sources_html(),
 "@@N@@": str(len(EV)),
}
for k, v in rep.items():
    page = page.replace(k, v)
assert "@@" not in page
with open(os.path.join(OUT, "record-of-catastrophes.html"), "w", encoding="utf-8") as f:
    f.write(page)
print("events", len(EV), "deaths rows", len(DEATHS), "share rows", len(SHARES))
