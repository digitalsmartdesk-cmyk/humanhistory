from common import *

# =====================================================================
# CHAPTER 16: THE COMPARISON  (the only place the hypothesis is stated and tested)
# =====================================================================
ACC, ACCD = "#6b4a1f", "#dcc08a"

CLAIMCSS = """
.claim{border-left:5px solid var(--accent);background:var(--surface);padding:16px 20px;margin:14px 0 8px;max-width:72ch}
.claim .tag{font-family:var(--font-mono);font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-2);margin:0 0 6px}
.claim p.q{font-family:var(--font-display);font-size:21px;line-height:1.4;margin:0;color:var(--ink)}
.claim p.s{font-size:14.5px;color:var(--ink-2);margin:10px 0 0}
"""
import common
common.SHELL = common.SHELL.replace("</style>", CLAIMCSS + "</style>", 1)

CLAIM = ('<div class="claim"><p class="tag">The hypothesis</p>'
         '<p class="q">Humanity has made itself vulnerable to catastrophic outcomes through the last 100 years of advancement, unlike any other 100 years of advancement in known history.</p>'
         '<p class="s">This is the project\'s starting hypothesis. No earlier chapter stated it. They gathered evidence on one side or the other, and this chapter puts the evidence side by side.</p></div>'
         '<p>The hypothesis has parts that can be checked separately. A century that was uniquely dangerous should show at least some of these: the largest losses on record, the largest possible losses, the widest reach, harms that are hardest to undo, the heaviest dependence on a few systems, and defenses that have not kept up. Each test below states what it expects, sets out what the earlier chapters recorded for and against, and gives a result. The results are my judgment, not findings from the sources.</p>')

STATS = [
    ("30–60% against 3%", "of Europe's people lost in the Black Death, against 3.0–3.7% of the world's in the Second World War (Chapter 7)"),
    ("2 to 5 billion", "possible famine deaths in one 2022 model of nuclear war. It is a scenario, not a forecast (Chapter 6)"),
    ("7 of 9", "planetary boundaries transgressed, all at their highest recorded levels (Chapter 6)"),
    ("Over 90%", "fall in disaster death rates over the last century, with about four times as many people. The source flags the early figures as uncertain (Chapter 8)"),
]

AX = [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")]
CH_REAL = [
    ("Americas after 1492", "80–90% of the Indigenous population", 80, 90, False, None),
    ("Black Death", "30–60% of Europe", 30, 60, False, None),
    ("Plague of Justinian", "20–40% of Constantinople, a city", 20, 40, False, None),
    ("Irish Great Famine", "20–25% of Ireland, deaths and emigration", 20, 25, False, None),
    ("Taiping Rebellion", "5–10% of China, base not stated", 5, 10, False, None),
    ("Bengal famine (last 100 years)", "1.3–6.3% of Bengal, my arithmetic", 1.3, 6.3, True, None),
    ("World War II (last 100 years)", "3.0–3.7% of the world", 3.0, 3.7, False, None),
    ("World War I", "1.7–2.3% of the countries involved", 1.7, 2.3, False, None),
    ("COVID-19 (last 100 years)", "About 0.2% of the world, my arithmetic", 0, 0.2, True, 0.2),
]
CH_MOD = [
    ("Famine after an India–Pakistan war", "More than 2 billion deaths, modelled. About 24% of 8.2 billion, my arithmetic", 0, 24, True, None),
    ("Famine after a US–Russia war", "More than 5 billion deaths, modelled. About 61% of 8.2 billion, my arithmetic", 0, 61, True, None),
]

GLANCE = [
    ("1. Realised loss", "The last 100 years should hold the largest losses on record.", "In share terms the largest losses came earlier: 30–60% of Europe, 80–90% of the Indigenous Americas, against about 3% of the world in the Second World War.", "Not supported"),
    ("2. Size of the worst case", "The worst case now possible should match or exceed past worst cases.", "One 2022 model puts famine deaths after nuclear war at more than 2 to more than 5 billion, about 24–61% of today's people on my arithmetic. No such event has happened.", "Supported as a model result only"),
    ("3. Reach", "Harm should be able to cross the whole world, by human causes.", "Planetary-scale channels are now loaded: 12,187 warheads, carbon dioxide at 432 ppm, 7 of 9 boundaries. Global-scale harm also happened before, from disease and from natural events.", "Supported in kind, not in novelty"),
    ("4. Reversibility", "Harms should be harder to undo than before.", "Past human losses were made up over generations. Several present changes to the living world have no recovery clock in the sources. Some reversals are also recorded.", "Mixed"),
    ("5. Dependence and margins", "More people should rest on fewer systems, with less slack.", "About half of food depends on synthetic nitrogen, and about 92% of the most advanced chips are made in Taiwan. The chapters give no matching figures for 1825 or 1925.", "Cannot be compared on these figures"),
    ("6. Defenses", "Defenses should lag behind exposure.", "Defenses against known, countable hazards have produced large falls in deaths. Those against climate, new pathogens and AI show rules or targets, with few measured results.", "Mixed"),
]

LEDGER = [
    ("Life and health (Ch. 3)", "Children dying before age 15 fell from about 1 in 2 to 4%. Life expectancy rose from 32 to 71 (1900–2021).", "Drug-resistant infections were linked to 4.71 million deaths in 2021, 1.14 million attributable. The forecast for 2050 is 1.91 million attributable."),
    ("Food, wealth, comfort (Ch. 4)", "Food supply rose from 2,184 to 3,006 kilocalories per person per day (1961–2023). French working hours fell from 3,168 to 1,487 a year.", "673 million people faced hunger in 2024. About 837 million were in extreme poverty in 2026 on the World Bank's $3 line."),
    ("Knowledge and connection (Ch. 5)", "Adult literacy rose from about 1 in 10 people to about 88%. Internet use rose from 16% to 74% (2005–2025).", "739 million adults lack basic literacy and 2.2 billion people are offline. Use is 23% in low-income countries against 94% in high-income ones."),
    ("Work, inequality, population (Ch. 12)", "Child labour fell from 246 million to about 138 million (2000–2024). Fertility fell from 4.9 to 2.3 children per woman.", "The richest 10% take 53% of income and hold 75% of wealth. The poorer half takes 8% of income and holds 2% of wealth."),
    ("Learning and wisdom (Ch. 13)", "Measured test scores rose for decades, about 3 points a decade in the Flynn effect.", "Reversals are reported in Norway, Denmark and the UK. PISA 2022 maths fell 15 points. Only Finland and Denmark improved in literacy among 31 countries in PIAAC 2023. Wisdom has no agreed measure."),
    ("Mind and wellbeing (Ch. 14)", None, "1.2 billion people live with a mental disorder. One third of those with depression get formal care. Governments spend a median 2% of health budgets on it."),
    ("Power and governance (Ch. 15)", "Women won the national vote between 1893 (New Zealand) and 1971 (Switzerland federal) among the examples.", "74% of people live in autocracies by V-Dem's 2026 count, and democracy for the average person is back at its 1978 level."),
]

AREAS = [
    ("Six tests of the hypothesis", [
        ("Test 1", "Not supported", "Realised loss: the worst losses came earlier",
         "If this century were uniquely dangerous, it should hold the heaviest losses on record. Chapter 7 does not show that. It puts the Black Death at 30–60% of Europe's people and the post-1492 collapse at 80–90% of the Indigenous population of the Americas. The largest share losses in the last 100 years among its entries are the Second World War at 3.0–3.7% of the world and the Bengal famine at 1.3–6.3% of Bengal. COVID-19 is about 0.2% of the world.",
         [("In headcount", "The Second World War's 60 to 85 million deaths are above the usual Black Death range of 25 to 50 million and below the higher estimates of 75 to 200 million. The world has more people now, so a headcount compares less well than a share."),
          ("Falling toll", "Chapter 8 reports that disaster death rates fell by more than 90% over the century and that recent famines have been far less deadly than earlier ones."),
          ("What this does", "It does not refute the hypothesis, which is about exposure. It does show that the hypothesis cannot rest on what has already happened.")],
         "Share figures use different bases, a region, a city, a country and the world, as the labels say. Many ranges are wide: the Black Death differs by up to a factor of eight. Most of Chapter 7 comes from Wikipedia."),
        ("Test 2", "Supported as a model result only", "Size of the worst case: potentially as large as the largest past loss",
         "Chapter 6 reports a 2022 Nature Food study that finds more than 2 billion possible famine deaths after an India–Pakistan war and more than 5 billion after a US–Russia war. Against today's 8.2 billion people that is about 24% and 61%, which is close to the Black Death's 30–60% of Europe and below the Americas' 80–90%. Those earlier losses were regional. This scenario is global.",
         [("Arsenals", "Chapter 6 gives 12,187 warheads in January 2026, about 2,100 to 2,200 of them on high alert. The chapter on defenses records that the total is about 82–83% below its 1986 peak of 70,300."),
          ("Treaty and clock", "New START expired on 5 February 2026, and the Doomsday Clock stands at 85 seconds, the closest ever."),
          ("Close calls", "The 1983 Petrov false alarm and the 1962 submarine B-59 account are both in Chapter 6. The second is debated by historians.")],
         "A modelled scenario that the chapter says shows scale and is not a forecast. I divided by 8.2 billion myself, and Chapter 6 does not say what population base the study used. Nothing like this has happened, so the evidence is a calculation and not an observed event."),
        ("Test 3", "Supported in kind, not in novelty", "Reach: human-made channels now span the world",
         "Chapter 7 finds that only a few events reached across the world: the 1918 influenza, smallpox, COVID-19 and the two world wars. The rest struck a region, a continent or an empire. Chapter 6 lists exposures that work at planetary scale by their nature: the atmosphere, the oceans, global supply chains and global travel. Carbon dioxide rose from 313 to 432 ppm between 1958 and May 2026, and seven of nine planetary boundaries are transgressed together.",
         [("Against novelty", "Disease crossed regions on the transport of its day in 541, 1346 and 1918 (Chapter 7). Chapter 10 records natural events with global reach in deep time, such as the asteroid strike that removed about 75% of species 66 million years ago. Global-scale harm is old."),
          ("Against, on speed", "Chapter 2 shows Atlantic crossing times falling by factors of about 8 and then about 25 in two stages (its arithmetic), so the speed of connection has risen. It does not show that the speed changed the size of any harm.")],
         "The counts and measurements are solid, since carbon dioxide is measured directly. The step from them to catastrophe is a judgment, and the boundary framework is a scientific proposal and not a settled threshold, as Chapter 6 says."),
        ("Test 4", "Mixed", "Reversibility: some harms have no recovery clock",
         "Past human catastrophes recovered, slowly. Chapter 7 reports that Europe regained its pre-plague population in the 16th century, Ireland's decline lasted a century, and the cooling after Tambora was temporary. Chapter 9 describes several present changes as states and not flows: a coral reef tipping point said to be passing, seven boundaries at their highest recorded levels, and glaciers losing ice faster each period. Chapter 10 puts recovery from the great extinctions at about 6 to 75 million years.",
         [("Against", "Chapter 11 records a humpback whale population back to about 93% of its pre-whaling size roughly 33 years after the ban, and Chapter 8 records the ozone layer expected to return to 1980 levels between 2040 and 2066. Some harms did reverse."),
          ("A caution", "A 73% average fall in monitored wildlife populations over 52 years is not a count of extinctions, and the source says so. Chapter 10 puts the main End-Permian marine pulse at 60,000 to 100,000 years, so the two are not like for like."),
          ("Hypothetical", "Chapter 6 also records a warning that mirror-image organisms might cause irreversible harm. They do not exist.")],
         "The living-world figures are measured averages with wide caveats. Recovery times for deep-time events are estimates, and the comparison with today's rates is mine."),
        ("Test 5", "Cannot be compared on these figures", "Dependence and margins: more people rest on fewer systems",
         "Chapter 6 gives two sharp examples. About 40 to 50% of the world's food depends on synthetic nitrogen fertilizer, and without it the world might hold around 4 billion people, not over 8 billion. About 92% of the most advanced logic chips are made in Taiwan. Chapter 12 puts world population at 8.2 billion in 2024, so any single failure now falls on more people than at any time before.",
         [("Earlier dependence", "Chapter 7 records that Ireland in the 1840s depended on a single crop and was struck by blight. Concentrated dependence is not new, though the Irish case was regional."),
          ("What is missing", "The chapters give no figure for how much of the world depended on any single system in 1825 or 1925, so I cannot say it has increased.")],
         "The two present-day figures are secondhand estimates, the fertilizer one from a single published estimate and the chip share from a news piece citing a research group. Nothing comparable exists in the earlier chapters, so this test stays open."),
        ("Test 6", "Mixed", "Defenses: large gains on known hazards, little yet on the newest",
         "Chapter 8 records large measured falls where the hazard is known and countable: smallpox eradicated, wild polio cases down by more than 99% since 1988, child deaths before 15 down by about 84% from 1950 to 2020, disaster death rates down by more than 90%. It also records weakening: New START expired, the United States left the WHO on 22 January 2026, the pandemic agreement's access annex was unfinished, UNEP projects 2.8 °C of warming under current policies, and about 38% of near-Earth asteroids over 140 metres were known in 2023.",
         [("The living world", "Chapter 11 records 17.6% of land and 8.4% of ocean protected against a 30% target for each, and fewer than half of aligned national targets on track."),
          ("The newest technology", "For AI and engineered pathogens, Chapter 8 describes a safety report, an EU law and a convention, and says it found no figures showing a fall in harm from any of them.")],
         "Cause is hard to show: a fall in deaths may come from the defense, from wealth or from both. Several figures are secondhand, and the chapter marks the 154 million lives saved by vaccination as a model."),
    ]),
    ("Two problems with the test itself", [
        ("Problem 1", "Cannot be tested as worded", "“Unlike any other 100 years” needs a century-by-century comparison",
         "The hypothesis claims that no other century, in all of known history, matches this one. My record cannot test that. Chapter 7 is 19 events I selected, not a tally of every century. It is thinner for events outside Europe, East Asia and the Middle East, and a record kept by survivors lists only the catastrophes that were survived. No other 100 years in the chapters has a measured exposure that can be set against the figures in Chapter 6.",
         [("What can be said", "Among the 19 events, none matches the modelled scenario in Test 2 for reach. That finding is limited to a list I chose."),
          ("Survivors", "A record of survived catastrophes also cannot show what was narrowly avoided in earlier centuries.")],
         "A limit of the evidence, stated in Chapter 7 itself."),
        ("Problem 2", "Cannot be netted", "The gains and the exposure are different kinds of quantity",
         "The earlier chapters also record large gains, set out in the ledger below. Deaths averted, years of life and meals supplied are counted outcomes. The exposure in Chapter 6 is mostly a modelled or judged possibility. They cannot be added into one balance, and the hypothesis does not claim they should be. It says the century is more exposed, which is compatible with the century also being healthier and richer.",
         [("Shared causes", "The same fertilizer that feeds about half the world is also a main driver of the nitrogen boundary being breached (Chapter 6)."),
          ("Expert estimates differ", "For extinction from AI by 2100, domain experts gave 3% and superforecasters 0.38% in the 2022 Existential Risk Persuasion Tournament, while Toby Ord gives 1 in 10 for this century. Ord calls his figures order-of-magnitude indications.")],
         "Probability figures are opinions, not measurements, and the tournament's 3% is about 8 times its 0.38%, and Ord's 1 in 10 is about 26 times the lower figure. Those ratios are my arithmetic.")
    ]),
]

PATTERNS = [
    ("On what has happened, this is not the worst century", "In share terms the largest losses in my record came earlier. No event in the last 100 years among my entries matches the 30–60% regional losses; the highest share is Bengal's 6.3% at the top of its range."),
    ("On what could happen, the record shows something new in reach", "The modelled worst case is global, and it comes from choices people make. Among the 19 events I selected, none has that combination."),
    ("The two kinds of evidence differ in strength", "Realised losses are counted, with wide ranges. The worst cases are modelled or judged, and expert probabilities differ widely. Weight them accordingly."),
    ("Defenses and exposure grew from the same capacity", "Fertilizer, medicine, forecasting and trade raised living standards and also built the dependence in Chapter 6. This is my reading of the chapters, not a finding."),
    ("A narrower claim fits the evidence better than the wording does", "The chapters do not show a century unlike any other in every respect. They do support this narrower form: this is the first century in my record in which human choices carry measured or modelled effects at the scale of the whole world. That is my judgment, and the hypothesis may still be worth keeping in its original form."),
]

LIMITS = [
    "This chapter uses only the earlier chapters and adds no new research. Their limits carry over, including secondhand figures and, for Chapter 7, mostly Wikipedia.",
    "The results are my judgment, labelled as such. Another reader could grade the same evidence differently.",
    "Chapters 12 to 15 rarely reach back to 1925, so for those the two centuries cannot be compared. Chapter 13 gives no verdict at all.",
    "The share figures use different bases. A region, a city, a country and the world are not the same denominator.",
    "Modelled scenarios and expert probabilities are not observations. I included only the figures the earlier chapters recorded.",
    "The chapters are dated between 13 and 27 October 2026. Developments after that, such as a replacement for New START, are not included.",
    "The ledger is a selection of seven areas. It leaves out many gains and many strains, and it does not weigh one against the other.",
]

SRCS = [
    ("Chapters used", [
        ("https://claude.ai/artifact/7qSxXu33DCKP9HftfxH3Dc", "Chapter 1, The appearance of human life", "C"),
        ("https://claude.ai/artifact/Ut88jmTViQUCc7jbfrZd1b", "Chapter 2, The pace of change", "C"),
        ("https://claude.ai/artifact/79PSVNjqzAqJkcuARmF5wg", "Chapter 3, Life and health", "C"),
        ("https://claude.ai/artifact/M7CcrBF81bKsbmrs98iQCq", "Chapter 4, Food, wealth and comfort", "C"),
        ("https://claude.ai/artifact/1yPcv32YXUWW2jYuRESSNG", "Chapter 5, Knowledge and connection", "C"),
        ("https://claude.ai/artifact/SJ3PdrbEz1U14tZftAh7p5", "Chapter 6, A century of vulnerability", "C"),
        ("https://claude.ai/artifact/21WkXcCqVbi5EXSyYgitEL", "Chapter 7, The record of catastrophes", "C"),
        ("https://claude.ai/artifact/GgfHSBg2uJFXYtAS7QzhRU", "Chapter 8, Defenses built", "C"),
        ("https://claude.ai/artifact/B7jDvigTvytm2ioPUncLbZ", "Chapter 9, Nature at risk", "C"),
        ("https://claude.ai/artifact/NUTcZosxAhd7YLJJ5s85BQ", "Chapter 10, Nature's catastrophes", "C"),
        ("https://claude.ai/artifact/Xdv42PDasn3ETek7T5x8oB", "Chapter 11, Nature defended", "C"),
        ("https://claude.ai/artifact/SNJrCBY4SongkYejYANqSt", "Chapter 12, Work, inequality and population", "C"),
        ("https://claude.ai/artifact/PtP9Rvnfn7VatTSYdnv6Y9", "Chapter 13, Literacy, wisdom and knowledge", "C"),
        ("https://claude.ai/artifact/9RZVCJrqYMM9PkrBB3YXEp", "Chapter 14, Mind and wellbeing", "C"),
        ("https://claude.ai/artifact/Q1B1ZSSMUHxtXhi72heMg4", "Chapter 15, Power and governance", "C"),
    ]),
]

groups, n = groups_html(AREAS)
assert n == 8, n
BODY = (
    section("claim", "The hypothesis", "", CLAIM)
    + section("glance", "The tests at a glance", "", stats_html(STATS)
              + snap_html(["Prediction if the claim holds", "What the chapters recorded", "My result"], GLANCE))
    + section("scale", "Realised loss and the modelled worst case", "",
              chart_block("Share of a population lost, past events",
                          "Solid bars are the source's range. Hatched bars are my arithmetic. The bases differ, so read each label. Events marked “last 100 years” fall between 1926 and 2026.",
                          chart_html(CH_REAL, AX, 100, "Bar chart of the share of a population lost in nine past events, from 0.2% for COVID-19 to 80–90% for the Americas after 1492"))
              + chart_block("A modelled scenario on the same axis",
                            "Famine deaths in one 2022 model of nuclear war, as a share of 8.2 billion people. The scenario has not happened. Both bars are my arithmetic on the study's figures.",
                            chart_html(CH_MOD, AX, 100, "Bar chart of modelled famine deaths after nuclear war as a share of world population: about 24% and 61%")))
    + section("entries", "The tests", "Six tests and two problems with testing. Each gives what the chapters recorded and how solid it is.", groups)
    + section("ledger", "The ledger: gains and strains", "",
              '<p class="note">Figures are as the earlier chapters give them. They are not added up, and a missing figure is shown as missing.</p>'
              + snap_html(["Gain recorded", "Strain that remains"], LEDGER))
    + section("patterns", "What the weighing shows", "", '<p class="note">These are my reading of the tests, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">This chapter adds no new sources. Tag C is an earlier chapter of this project, where the original sources and their reliability are listed.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "The Comparison",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 16 · Weighing",
        "@@H1@@": "The comparison",
        "@@SUB@@": "The hypothesis stated, then tested six ways against the earlier chapters",
        "@@LEDE@@": "The earlier chapters do not show the worst losses in this century. They do show exposures at the scale of the whole world that none of my 19 selected earlier events matches. This chapter sets out what supports and what weakens the hypothesis.",
        "@@ASOF@@": "Built from Chapters 1 to 15, whose figures are current to between 13 and 27 October 2026. No new research.",
        "@@NAV@@": nav([("claim", "The hypothesis"), ("glance", "At a glance"), ("scale", "Loss and worst case"), ("entries", "The tests"), ("ledger", "The ledger"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Chapters used")]),
        "@@FOOTER@@": "Several statements are my own arithmetic: that 2 and 5 billion are about 24% and 61% of 8.2 billion, that the Bengal share is 1.3–6.3% and the COVID-19 share about 0.2% (from Chapter 7), the comparison of the Second World War's headcount with the Black Death's, and the ratios between the probability estimates in Problem 2 (3 against 0.38, 10 against 0.38). The results of the tests, the pattern readings and the narrower claim are my own judgment.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "the-comparison.html")
    print("ok", n)
