import html, os
e = html.escape
OUT = os.path.dirname(os.path.abspath(__file__))

STATS = [
 ("32 → 71", "years of life expectancy at birth, 1900 to 2021 (Our World in Data)"),
 ("154 million", "lives saved by immunization over 50 years, modelled by WHO"),
 ("Over 90%", "fall in disaster death rates across the last century, while the world's population grew about fourfold"),
 ("70,300 → 12,187", "nuclear warheads, from the 1986 peak to the start of 2026 (Federation of American Scientists)"),
]

# name, value text, percent, hatch
SHARES = [
 ("Smallpox", "Eradicated; certified May 1980", 100, False),
 ("Wild polio cases", "More than 99% since 1988, from about 350,000 to 2", 99, False),
 ("Disaster death rates", "More than 90% over the past century", 90, False),
 ("Child deaths before age 15", "About 84%: from roughly a quarter (1950) to 4% (2020)", 84, True),
 ("Nuclear warheads", "82–83%: from about 70,300 (1986) to about 12,200 (2026)", 82.5, True),
 ("Extreme poverty headcount", "About 64%: from 2.3 billion (1990) to 837 million (2026)", 64, True),
 ("Infant deaths, vaccination", "40% lower, from vaccination against 14 diseases (WHO model)", 40, False),
]

# area, [(sort, when, kind, title, story, [(k,v)], solid)]
AREAS = [
("Disease", [
 (1952, "1952", "Institution", "Global influenza surveillance",
  "WHO's global network for tracking influenza has run since 1952. It now comprises 166 institutions across 136 WHO member states.",
  [("Does", "Works as a global mechanism of surveillance, preparedness and response for seasonal, pandemic and zoonotic influenza, and as a global alert for novel influenza viruses and other respiratory pathogens."),
   ("Output", "Publishes vaccine composition recommendations, for example for the 2026–2027 northern hemisphere season.")],
  "WHO's own page. It gives the size and mission of the network but no performance data, and it does not say outright that the network selects vaccine strains; I infer that from the recommendations it publishes."),
 (1974, "1974 to now", "Programme", "Routine childhood immunization",
  "WHO estimates that immunization saved at least 154 million lives over 50 years, about six lives every minute of every year. Of these, 101 million were infants, and measles vaccine accounts for 60 percent, nearly 94 million.",
  [("Coverage", "84 percent of infants are protected with three DTP doses, up from fewer than 5 percent when the programme launched."),
   ("Effect", "Vaccination against 14 diseases has directly contributed to reducing infant deaths by 40 percent globally and by more than 50 percent in the African Region."),
   ("Health", "Each life saved gained on average 66 years of full health, 10.2 billion in total.")],
  "A modelled estimate published by WHO, measured against a world without vaccination. It is not a count of observed deaths."),
 (1980, "May 1980", "Eradication", "Smallpox",
  "WHO certified global eradication in May 1980. Ordinary smallpox had killed about 30 percent of those infected.",
  [("Before", "An estimated 250 to 500 million deaths in the 20th century by one estimate, and up to 300 million by another.")],
  "From Wikipedia, as in the record of catastrophes. Death estimates vary widely; the eradication date is not in dispute."),
 (1988, "1988 to now", "Campaign", "Polio eradication",
  "Wild poliovirus cases have fallen by more than 99 percent since 1988, from an estimated 350,000 cases in more than 125 endemic countries to two. Transmission continues in Afghanistan and Pakistan.",
  [("Effect", "Over 20 million people are able to walk who would otherwise have been paralysed, according to WHO's immunization page.")],
  "WHO's own fact sheet. My read did not show the year of the latest count of two cases, or how many of the three wild types are eradicated."),
 (2025, "20 May 2025", "Treaty", "WHO Pandemic Agreement",
  "The 78th World Health Assembly adopted the agreement by consensus. The day before, the committee approved it by 124 votes in favour, none against and 11 abstentions.",
  [("Sets out", "Principles and tools for coordinating prevention, preparedness and response, including equitable access to vaccines, therapeutics and diagnostics. Manufacturers in the access system are to provide rapid access targeting 20 percent of their real-time production of pandemic vaccines."),
   ("Not yet", "It opens for signature only after the Assembly adopts an annex on pathogen access and benefit sharing. It enters into force after 60 ratifications.")],
  "WHO's own announcement. The agreement is not in force. See the section on thinning defenses for the annex."),
]),
("Food", [
 (1958, "20th–21st c.", "Trend", "Fewer deadly famines",
  "Our World in Data lists major famines since 1990 in the Central African Republic, the DR Congo, Ethiopia, North Korea, Nigeria, Somalia and Sudan, and says recent famines have typically been far less deadly than earlier ones.",
  [("Then", "Its chart shows an estimated 36 million deaths in the Great Leap Forward famine, 1958 to 1962, and about 25 million in famines during the Second World War across the USSR, Europe and Asia."),
   ("Now", "About 340,000 estimated deaths in northeast Nigeria from 2016 to 2019."),
   ("Why", "The page credits more food per person, better markets and transport, healthcare and lower poverty, together with emergency aid and early-warning monitoring.")],
  "The page gives per-decade totals only in charts, so the text figures are single famines. The 36 million figure sits inside the 15 to 46 million range used in the record of catastrophes."),
 (2008, "2008", "Facility", "Svalbard Global Seed Vault",
  "Opened in 2008 as a partnership between Norway's Ministry of Agriculture and Food, NordGen and the Crop Trust. It holds more than 1.4 million seed samples as of 2026, from 134 institutions, with room for 4.5 million.",
  [("Purpose", "Described as the ultimate insurance policy for the world's food supply: it backs up crop collections so genebanks can restore them if the originals are lost or become inaccessible.")],
  "The Crop Trust's own page. It gives no data on how often the vault has been used."),
]),
("Disaster warning", [
 (2006, "2006", "System", "Indian Ocean tsunami warning",
  "A warning system for the Indian Ocean was up and running about eighteen months after the December 2004 tsunami, as scheduled, according to UNESCO's Director-General in 2006.",
  [("Does", "It is a component of a global system and can receive and distribute tsunami advisories at all hours.")],
  "A 2006 news report. It gives no figures on countries covered or on performance, so I have no outcome evidence for this system."),
 (2019, "May 2019", "Outcome", "Cyclone Fani evacuation",
  "Odisha's chief minister said a record 1.2 million people were evacuated in 24 hours. The UN disaster-risk office credited the almost pinpoint accuracy of the warnings for a well-targeted evacuation.",
  [("Deaths", "The article gives figures from 16 to 33 for the cyclone in India."),
   ("Compare", "The 1999 super-cyclone in the same state killed more than 10,000 people.")],
  "One event, reported by Al Jazeera. The evacuation count is the state government's, and the article gives no evacuation figure for 1999."),
 (2020, "Past century", "Trend", "Falling disaster deaths",
  "Death rates from disasters have fallen by more than 90 percent over the last century, although the world has about four times as many people. Our World in Data says: “This is not because hazards have become weaker. It’s because societies have become more resilient.”",
  [("Factors", "Weather forecasts and early warning, better buildings, national and international cooperation, and food systems that make a lost harvest less damaging."),
   ("Now", "Excluding extreme temperature, the typical figure for the last 10 to 15 years is roughly 10,000 to 20,000 deaths a year. In the 20th century, more than a million deaths in a year were not uncommon.")],
  "The page warns that records from a century ago are incomplete, that early death rates may be underestimates, and that trends should not be inferred from pre-2000 data. The size of the fall is therefore uncertain."),
]),
("Atmosphere and energy", [
 (1987, "1987", "Treaty", "Montreal Protocol and the ozone layer",
  "The phase-out covers nearly 99 percent of banned ozone-depleting substances. If current policies stay in place, the ozone layer is expected to return to 1980 levels by about 2066 over the Antarctic, 2045 over the Arctic and 2040 for the rest of the world.",
  [("Added", "The Kigali Amendment, which phases down some hydrofluorocarbons, is estimated to avoid 0.3 to 0.5 °C of warming by 2100, excluding HFC-23.")],
  "From a WMO page. I did not check which edition of the assessment it summarizes or whether a newer one is out."),
 (2025, "2024–2026", "Market", "Cheaper clean power and the investment shift",
  "IRENA reports that in 2024 solar photovoltaics were on average 41 percent cheaper than the lowest-cost fossil fuel alternatives, and onshore wind 53 percent cheaper. The IEA's World Energy Investment 2026 puts clean energy at about $2.2 trillion of roughly $3.4 trillion in global energy investment, against about $1.2 trillion for fossil fuels.",
  [("Costs", "Solar PV averaged $0.043 per kilowatt-hour in 2024. Battery storage prices fell 93 percent since 2010, to $192 per kilowatt-hour."),
   ("Ratio", "Nearly two dollars go to clean energy for every dollar committed to fossil fuels in 2026.")],
  "Weak. Both sets of figures reached me secondhand, the IRENA ones through a trade-press summary and the IEA ones through an article citing a Forbes contributor. The IEA's own page gave no figures, and it says the 2026 estimates are shaped by an energy crisis tied to the conflict in the Middle East."),
]),
("Nuclear", [
 (1970, "1968 / 1970", "Treaty", "Nuclear Non-Proliferation Treaty",
  "Opened for signature in 1968 and in force from 1970. A total of 191 states have joined, including the five nuclear-weapon states.",
  [("Aims", "To prevent the spread of nuclear weapons and weapons technology, to promote cooperation in the peaceful uses of nuclear energy, and to further the goal of nuclear disarmament and general and complete disarmament.")],
  "From the UN Office for Disarmament Affairs. The page lists the aims but does not report how many states have left or tried to acquire weapons."),
 (1986, "1986 to 2026", "Outcome", "Fewer nuclear warheads",
  "The Federation of American Scientists puts the global inventory at about 70,300 warheads in 1986 and roughly 12,187 at the beginning of 2026, a fall of about 82 to 83 percent.",
  [("Check", "The same page also gives 12,321 for the start of 2026 without reconciling the two. SIPRI's yearbook figure, used in the chapter on vulnerability, is 12,187.")],
  "Estimates by a research organization, not official counts. The page's two current figures differ by about 1 percent."),
]),
("Space", [
 (2022, "26 Sept 2022", "Test", "DART asteroid deflection",
  "NASA's DART spacecraft struck Dimorphos, a small asteroid about 160 metres wide that orbits the larger asteroid Didymos. NASA announced on 11 October that the orbit had been shortened by 32 minutes.",
  [("Orbit", "The orbital period was 11 hours 55 minutes before the impact. NASA gave an uncertainty of two minutes either side of the 32-minute change."),
   ("Goal", "The mission aimed for a change of at least 73 seconds, and scientists had hoped for about 10 minutes."),
   ("Meaning", "NASA's Lori Glaze said that for the first time humanity had changed the orbit of a planetary body. NASA knew of no large asteroid threatening Earth in the foreseeable future.")],
  "One test on one small asteroid, read through Space.com's report of NASA's announcement. It shows the method works once, not that it would work on a larger or faster body."),
 (2023, "2023", "Survey", "Near-Earth object catalogue",
  "The known near-Earth object population is over 32,000 objects. A 2023 study in the Planetary Science Journal finds the near-Earth asteroid population about 38 percent complete for objects larger than 140 metres.",
  [],
  "I read the abstract only. The study is three years old, so completeness has probably risen, and I found no figure for objects over 1 kilometre."),
]),
("Emerging technology", [
 (1972, "Date not read", "Treaty", "Biological Weapons Convention",
  "The UN disarmament office says the convention effectively prohibits the development, production, acquisition, transfer, stockpiling and use of biological and toxin weapons. It was the first multilateral disarmament treaty to ban an entire category of weapons of mass destruction.",
  [("Method", "It relies primarily on a network approach of coordination with international, regional and non-governmental organizations.")],
  "The page I read gave no opening or entry-into-force dates, no count of member states, and does not mention verification, so I say nothing on those points."),
 (2026, "3 Feb 2026", "Report", "International AI Safety Report",
  "The second edition of a review of the science on general-purpose AI capabilities and risks. It is led by Turing Award winner Yoshua Bengio, written by over 100 independent experts, and backed by over 30 countries and international organisations. Its partners are the UK AI Security Institute and Mila.",
  [("Purpose", "To give decision-makers in government and beyond a shared, authoritative global picture of AI's risks and impacts.")],
  "The report informs decisions; it does not set rules. Who commissioned it was not stated on the page I read."),
 (2027, "2024 to 2028", "Law", "EU Artificial Intelligence Act",
  "In force since 1 August 2024. The ban on certain AI systems has applied since 2 February 2025, and the obligations on general-purpose AI models since 2 August 2025.",
  [("Models", "General-purpose models already on the market before 2 August 2025 must comply by 2 August 2027."),
   ("High-risk", "High-risk systems under Annex III must comply from 2 December 2027, those under Annex I from 2 August 2028, and some public-authority systems already on the market by 2 August 2030.")],
  "From an implementation-timeline site, last updated 31 August 2026. It does not mention any proposal to postpone these dates, so I cannot confirm whether one is under way. The law covers the EU, not the world."),
]),
]

THIN = [
 ("US–Russia nuclear limits have lapsed", "New START expired on 5 February 2026. A public radio report (KAXE) headlined it as the first time in decades that the United States and Russia have no limits on nuclear weapons. The treaty had capped deployed warheads at 1,550.", "Source: KAXE report (S)"),
 ("The United States has left WHO", "The HHS fact sheet says the United States formally exited WHO on 22 January 2026, after a one-year notice period, citing failures in WHO's handling of COVID-19, a refusal to implement reforms and a lack of accountability. It says the US will work through targeted cooperation with partners outside WHO. I did not find figures for the effect on funding or surveillance.", "Source: HHS fact sheet (P)"),
 ("The pandemic agreement is not yet open for signature", "The resumed sixth negotiating meeting on the access and benefit-sharing annex ran from 27 April to 1 May 2026 and ended without a finished text. The 79th Assembly was to be asked to continue the work, and the result would then go to the Assembly in May 2027, or earlier to a special session in 2026. A seventh meeting was set for 6 to 17 July 2026. I did not find what that meeting or the Assembly decided.", "Source: WHO news item, 1 May 2026 (P)"),
 ("Emissions are still on a high path", "UNEP projects 2.8 °C of warming this century under current policies and 2.3 to 2.5 °C if new national pledges are fully implemented, down from 3.1 and 2.6 to 2.8 °C a year earlier. It says the new pledges have barely moved the needle and that a temporary overshoot of 1.5 °C is very likely within the next decade.", "Source: UNEP Emissions Gap Report 2025 (P)"),
 ("Most asteroids over 140 metres are still unfound", "About 38 percent of near-Earth asteroids larger than 140 metres were known as of the 2023 study. The DART test shows a deflection method exists; it does not help for an object nobody has seen.", "Source: Grav et al. 2023 abstract (P); reasoning is mine"),
 ("Progress against poverty has slowed", "The World Bank says global poverty reduction has slowed substantially over the last decade because of sluggish growth, high debt, COVID-19, conflict and severe weather shocks, and that at the current pace it could take decades to eradicate extreme poverty. About 837 million people are in extreme poverty.", "Source: World Bank (P)"),
 ("Today's famines come from conflict", "Our World in Data says the most pertinent trigger of deadly famines today is conflict or abuse of political power that blocks food supplies from reaching people. Better markets and transport help less against that cause.", "Source: Our World in Data (S); the last sentence is my reading"),
 ("AI rules start after the technology", "The EU's high-risk obligations take effect on 2 December 2027 and 2 August 2028. The international report is advisory. I found no outcome data yet on whether either has reduced harm.", "Source: EU AI Act timeline (S), AI Safety Report site (P); the last sentence is my reading"),
]

PATTERNS = [
 ("Routine systems produce the measured gains", "The largest falls in the chart come from things done every day for decades: vaccination, forecasting, evacuation planning, food markets. Each has a long record that can be counted."),
 ("Treaties hold while the parties stay", "The NPT has 191 parties and the ozone phase-out reached nearly 99 percent. The lapse of New START and the US exit from WHO show that a defense of this kind can also be withdrawn."),
 ("For the newest technologies the entries describe rules, not results", "The AI safety report, the EU law and the biological weapons convention are descriptions of what exists. I found no figures in the sources showing a fall in harm from any of them."),
 ("Many results are modelled or attributed loosely", "The 154 million lives saved is a model, the disaster figure is flagged as uncertain by its own source, and the link between resilience and falling deaths is argued rather than measured."),
]

LIMITS = [
 "The list is my selection. Nineteen entries cannot cover every defense, and I left out areas such as building codes, hospital systems, financial safeguards and space weather monitoring.",
 "Cause is hard to show. A fall in deaths may come from the defense, from wealth, or from both, and several sources say so only in general terms.",
 "Several figures are secondhand: the IRENA and IEA numbers, the Cyclone Fani account and the DART report. They need checking against the original reports before use.",
 "I did not find outcomes after mid-2026 for the pandemic annex, and I did not check whether the ozone assessment has been updated.",
 "Defenses that worked without notice leave little trace in the record, so the list favours defenses with measurable results.",
]

SOURCES = [
 ("Disease and health", [
  ("https://www.who.int/news/item/24-04-2024-global-immunization-efforts-have-saved-at-least-154-million-lives-over-the-past-50-years", "WHO, global immunization efforts have saved at least 154 million lives", "P"),
  ("https://www.who.int/news-room/fact-sheets/detail/poliomyelitis", "WHO, poliomyelitis fact sheet", "P"),
  ("https://www.who.int/initiatives/global-influenza-surveillance-and-response-system", "WHO, Global Influenza Surveillance and Response System", "P"),
  ("https://www.who.int/news/item/20-05-2025-world-health-assembly-adopts-historic-pandemic-agreement-to-make-the-world-more-equitable-and-safer-from-future-pandemics", "WHO, World Health Assembly adopts the Pandemic Agreement", "P"),
  ("https://www.who.int/news/item/01-05-2026-who-member-states-agree-to-extend-negotiations-on-pathogen-access-and-benefit-sharing-annex", "WHO, Member States agree to extend negotiations on the PABS annex", "P"),
  ("https://www.hhs.gov/press-room/fact-sheet-us-withdrawal-from-the-world-health-organization.html", "HHS, fact sheet on US withdrawal from WHO", "P"),
  ("https://en.wikipedia.org/wiki/Smallpox", "Wikipedia, Smallpox", "S"),
  ("https://ourworldindata.org/life-expectancy", "Our World in Data, life expectancy", "S"),
  ("https://ourworldindata.org/child-mortality", "Our World in Data, child mortality", "S")]),
 ("Food, disasters and wealth", [
  ("https://ourworldindata.org/famines", "Our World in Data, famines", "S"),
  ("https://www.croptrust.org/work/svalbard-global-seed-vault/", "Crop Trust, Svalbard Global Seed Vault", "P"),
  ("https://ourworldindata.org/natural-disasters", "Our World in Data, natural disasters", "S"),
  ("https://www.aljazeera.com/news/2019/05/cyclone-fani-praise-india-response-devastating-storm-190505072941472.html", "Al Jazeera, UN praises India's response to Cyclone Fani", "S"),
  ("https://earsc.org/2006/06/27/indian-ocean-tsunami-warning-system-up-and-running/", "EARSC, Indian Ocean tsunami warning system up and running", "S"),
  ("https://www.worldbank.org/en/topic/poverty/overview", "World Bank, poverty overview", "P")]),
 ("Atmosphere, energy and nuclear", [
  ("https://wmo.int/ar/node/20740", "WMO, ozone layer recovery is on track", "P"),
  ("https://www.unep.org/resources/emissions-gap-report-2025", "UNEP, Emissions Gap Report 2025", "P"),
  ("https://solarquarter.com/2025/08/16/irenas-2024-renewable-power-generation-costs-report-confirms-renewables-outcompete-fossil-fuels-with-solar-pv-41-and-onshore-wind-53-cheaper-than-lowest-cost-fossil-alternatives/", "SolarQuarter, summary of IRENA's 2024 cost report", "S"),
  ("https://www.marketscale.com/industries/energy/clean-energy-investment-hits-22-trillion-in-2026-nearly-doubling-fossil-fuel-spending", "MarketScale, clean energy investment hits $2.2 trillion in 2026", "S"),
  ("https://www.iea.org/reports/world-energy-investment-2026", "IEA, World Energy Investment 2026 (landing page, no figures)", "P"),
  ("https://disarmament.unoda.org/wmd/nuclear/npt/", "UN Office for Disarmament Affairs, Nuclear Non-Proliferation Treaty", "P"),
  ("https://fas.org/initiative/status-world-nuclear-forces/", "Federation of American Scientists, status of world nuclear forces", "P"),
  ("https://www.kaxe.org/news/2026-02-04/for-the-first-time-in-decades-the-u-s-and-russia-have-no-limits-on-nuclear-weapons", "KAXE, US and Russia have no limits on nuclear weapons", "S")]),
 ("Space and emerging technology", [
  ("https://www.space.com/nasa-dart-asteroid-impact-orbit-change-success", "Space.com, NASA's DART impact changed the asteroid's orbit", "S"),
  ("https://www.ipac.caltech.edu/publication/2023PSJ.....4..228G", "Grav et al. 2023, Planetary Science Journal (abstract)", "P"),
  ("https://disarmament.unoda.org/biological-weapons/", "UN Office for Disarmament Affairs, Biological Weapons Convention", "P"),
  ("https://internationalaisafetyreport.org/", "International AI Safety Report", "P"),
  ("https://artificialintelligenceact.eu/implementation-timeline/", "EU AI Act implementation timeline", "S")]),
]


def stats_html():
    return "".join('<div class="stat"><b>%s</b><span>%s</span></div>' % (e(a), e(b)) for a, b in STATS)


def shares_html():
    ax = "".join('<span style="left:%d%%">%d%%</span>' % (p, p) for p in (0, 25, 50, 75, 100))
    rows = ['<div class="rg-axis"><span></span><div>%s</div></div>' % ax]
    for name, sub, v, hatch in SHARES:
        rows.append(
            '<div class="rg-row"><div class="rg-lab"><b>%s</b><small>%s</small></div>'
            '<div class="rg-track"><i class="rg-bar%s" style="left:0;width:%.2f%%"></i></div></div>'
            % (e(name), e(sub), " hatch" if hatch else "", v))
    return "".join(rows)


def groups_html():
    out = []
    n = 0
    for area, items in AREAS:
        items = sorted(items, key=lambda x: x[0])
        lis = []
        for sort, when, kind, title, story, kv, solid in items:
            n += 1
            dl = ('<dl class="kv">%s</dl>' % "".join("<dt>%s</dt><dd>%s</dd>" % (e(k), e(v)) for k, v in kv)) if kv else ""
            lis.append(
                '<li class="item"><div class="when">%s<small>%s</small></div>'
                '<div class="what"><h3>%s</h3><p>%s</p>%s'
                '<p class="solid"><b>How solid</b> %s</p></div></li>'
                % (e(when), e(kind), e(title), e(story), dl, e(solid)))
        out.append('<section class="grp"><h3 class="gh">%s <span>%d %s</span></h3><ol class="list">%s</ol></section>'
                   % (e(area), len(items), "entry" if len(items) == 1 else "entries", "".join(lis)))
    return "\n".join(out), n


groups, N = groups_html()
assert N == 19, N


def sources_html():
    s = ""
    for h, items in SOURCES:
        s += "<h3>%s</h3><ul>" % e(h)
        for u, t, tag in items:
            s += '<li><a href="%s">%s</a><span>%s</span></li>' % (e(u, quote=True), e(t), tag)
        s += "</ul>"
    return s


page = open(os.path.join(OUT, "defenses_template.html"), encoding="utf-8").read()
rep = {
    "@@STATS@@": stats_html(),
    "@@SHARES@@": shares_html(),
    "@@GROUPS@@": groups,
    "@@THIN@@": "".join('<div><h3>%s</h3><p>%s</p><p class="src-tag">%s</p></div>' % (e(a), e(b), e(c)) for a, b, c in THIN),
    "@@PATTERNS@@": "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS),
    "@@LIMITS@@": "".join("<li>%s</li>" % e(x) for x in LIMITS),
    "@@SOURCES@@": sources_html(),
}
for k, v in rep.items():
    page = page.replace(k, v)
assert "@@" not in page
with open(os.path.join(OUT, "defenses-built.html"), "w", encoding="utf-8") as f:
    f.write(page)
print("entries", N, "share rows", len(SHARES), "thin", len(THIN))
