from common import *

# =====================================================================
# CHAPTER 17: WHAT WOULD CHANGE THE BALANCE
# =====================================================================
ACC, ACCD = "#3b4a63", "#b9c6e0"

STATS = [
    ("5 Feb 2026", "New START expired. Reports differ on whether either side still observes its limits"),
    ("Not finished", "the pandemic agreement's access annex after the seventh negotiating meeting, 6–17 July 2026. It is expected back before the Assembly no later than May 2027"),
    ("9–20 Nov 2026", "COP31 in Antalya, which launches the second Global Stocktake"),
    ("2.8 °C", "projected warming this century under current policies (UNEP 2025), against 2.3–2.5 °C if new pledges are fully implemented"),
]

CH_WARM = [
    ("Measured, 2025", "About 1.43 °C above pre-industrial, ±0.13 (WMO)", 0, 1.43, False, None),
    ("Current policies, 2025 report", "UNEP projection, 2.8 °C", 0, 2.8, False, None),
    ("Current policies, 2024 report", "UNEP, a year earlier, 3.1 °C", 0, 3.1, False, None),
    ("Pledges in full, 2025 report", "UNEP projection, 2.3–2.5 °C", 2.3, 2.5, False, None),
    ("Pledges in full, 2024 report", "UNEP, a year earlier, 2.6–2.8 °C", 2.6, 2.8, False, None),
]
CH_TARGET = [
    ("Land protected", "17.6% against a 30% target by 2030", 0, 58.7, True, None),
    ("Ocean protected", "8.4% against a 30% target by 2030", 0, 28, True, None),
    ("Biodiversity finance", "$16.8 billion in 2023 against a $20 billion target for 2025", 0, 84, True, None),
]

AREAS = [
    ("Decisions with dates on the calendar", [
        ("6–17 Jul 2026 and after", "Negotiation", "The pandemic agreement's access annex",
         "The agreement was adopted on 20 May 2025, but it opens for signature only after the Assembly adopts the annex on pathogen access and benefit sharing, and it enters into force after 60 ratifications. The seventh negotiating meeting, on 6–17 July 2026, streamlined the draft but did not finish it. WHO says the remaining issues are challenging and the eighth meeting was set for 14–18 September 2026. A Geneva briefing from May 2026 says the annex is expected to be resubmitted no later than the Assembly of May 2027.",
         [("Watch", "An agreed annex text, the opening for signature, and the 60th ratification."),
          ("Earlier plan", "A May 2025 report said the working group was supposed to conclude the annex by the 2026 Assembly. The deadline has since moved to 2027."),
          ("Not found", "I did not find the outcome of the September 2026 meeting.")],
         "WHO's own page for the July meeting, which gives no deadline, and a Geneva dialogue briefing for the May 2027 date. The 60-ratification threshold comes from Chapter 8."),
        ("9–20 Nov 2026", "Summit", "COP31 and the climate path",
         "The 31st UN climate conference runs in Antalya, Türkiye, and launches the second Global Stocktake. A summary of what to expect lists the unfinished Global Goal on Adaptation, 59 adaptation indicators and a commitment to at least triple adaptation finance for developing countries by 2035, and says exceeding 1.5 °C appears likely. Chapter 8 records UNEP's projection of 2.8 °C under current policies, down from 3.1 a year earlier, and 2.3–2.5 °C if new national pledges are fully implemented.",
         [("Watch", "New or revised national pledges, UNEP's next projection, and the monthly carbon dioxide reading, which was 432 ppm at its May 2026 peak."),
          ("Cost side", "Chapter 8 also records solar power 41% cheaper than the lowest-cost fossil option in 2024, from a trade-press summary of IRENA, so I give it low weight.")],
         "The conference dates and agenda come from a university article about what to expect, not from the UN. The UNEP figures are from UNEP's own report, as recorded in Chapter 8. I have no result from the summit, since it has not taken place."),
        ("2025 to 2028", "Law", "Rules for artificial intelligence",
         "Chapter 8 records the EU AI Act as in force since 1 August 2024, with obligations on general-purpose models from 2 August 2025 and high-risk obligations from 2 December 2027 and 2 August 2028. The International AI Safety Report of February 2026 informs decisions but does not set rules. Chapter 6 records that the evidence for catastrophic risk from advanced AI is the least established of the exposures it lists.",
         [("Watch", "Whether the dates hold, and any figures on harm before and after the rules apply."),
          ("Not found", "I found no outcome data on whether either has reduced harm, and I did not re-check the timeline for a proposed postponement.")],
         "The dates come from an implementation-timeline site, last updated 31 August 2026, as read for Chapter 8. They cover the EU only."),
    ]),
    ("Decisions without a date", [
        ("5 Feb 2026 and after", "Treaty", "Nuclear limits after New START",
         "New START expired on 5 February 2026. It had capped deployed warheads at 1,550. Axios reported that day, citing three sources, that the United States and Russia were close to an understanding to keep observing its terms for at least six months while negotiating a new deal. Kremlin spokesman Dmitry Peskov confirmed an understanding, but one US official said it would not be formalised, and President Trump called for a new treaty. A page summarising the treaty says Russia's foreign ministry stated on 4 February that without a US response it considered the obligations no longer binding, and it does not report informal observance. Six months from 5 February is early August 2026, on my arithmetic.",
         [("Watch", "A signed text, an exchange of data, and the warhead count in the next SIPRI yearbook, against the January 2026 figure of 12,187."),
          ("Not found", "I found no report of what happened after the six months, and nothing dated later than early February on the status of the limits.")],
         "The reports conflict and rest on unnamed sources and a summary page. Chapter 8 recorded a public radio headline that there were no limits. I treat the status as unsettled."),
        ("Targets to 2030", "Frameworks", "Protection, money and the unfinished treaties",
         "Chapter 11 records 17.6% of land and 8.4% of ocean protected against 30% targets, only 5.7% of ocean actively managed and 2.8% strictly protected, and fewer than half of aligned national targets on track. International biodiversity finance was $16.8 billion in 2023 against a $20 billion target for 2025. The plastics treaty talks ended without agreement in August 2025, and the deep-seabed Mining Code is unfinished.",
         [("Watch", "The next Protected Planet figures, the finance total against the $20 billion target, and any date for resumed plastics or seabed talks."),
          ("Not found", "Chapter 11 gives no next date for the plastics talks, and I did not search for one.")],
         "Figures are as Chapter 11 recorded them, mostly from institutions' own pages. The shares of the targets in the chart are my arithmetic."),
        ("Ongoing", "Survey", "Finding the large asteroids",
         "Chapter 8 records that NASA's DART spacecraft shortened the orbit of a small asteroid by 32 minutes in 2022, and that about 38% of near-Earth asteroids larger than 140 metres were known in a 2023 study. The test shows a method exists. It does not help against an object nobody has found.",
         [("Watch", "A newer completeness figure for objects over 140 metres, and one for objects over 1 kilometre, which I did not find.")],
         "One test and one study, both three or four years old. Completeness has probably risen since."),
    ]),
    ("Exposure with no defense recorded", [
        ("Present", "Dependence", "Fertilizer, energy and chips",
         "Chapter 6 records that synthetic nitrogen fertilizer underpins about 40 to 50% of the world's food and that about 92% of the most advanced logic chips are made in Taiwan. None of the 19 entries in Chapter 8 is aimed at either. The seed vault backs up crop collections, which is a different safeguard.",
         [("Watch", "Any published measure of how many people depend on a single process or place, and any change in the share of chips made in one place."),
          ("Gap", "Chapter 12 puts the world at 8.2 billion people, but the chapters hold no dependence figure for 1825 or 1925.")],
         "The two present-day figures are secondhand. That no defense is listed in Chapter 8 reflects my selection of 19 entries, not a survey of every defense that exists."),
    ]),
    ("Evidence that would settle the open questions", [
        ("To find", "Evidence gap", "A century-by-century tally of losses",
         "The claim of “unlike any other 100 years” could be tested with a consistent series of losses per century, as a share of the people affected, with ranges and with the regions where records are thin. Chapter 7 is 19 events I selected, and it says a record kept by survivors lists only the catastrophes that were survived. I do not know of a ready-made series, and I did not search for one.",
         [("What it would change", "Test 1 in Chapter 16 would stand or fall on it, and so would the claim that no earlier century matched this one.")],
         "A research task, not a finding. The chapters give no indication of how good such a series could be for periods before about 1800."),
        ("To find", "Evidence gap", "Measured outcomes for the newest defenses",
         "For artificial intelligence, engineered pathogens and the pandemic agreement, Chapter 8 describes rules and negotiations and found no figures showing a fall in harm. Expert estimates of the risk also differ widely: for extinction from AI by 2100, domain experts gave 3% and superforecasters 0.38%, while Toby Ord gives 1 in 10 for the century, and says his figures are order-of-magnitude indications.",
         [("What it would change", "Tests 2 and 6 in Chapter 16 rest on modelled scenarios and judged probabilities. Measured outcomes would give them firmer ground in either direction.")],
         "The probability figures are opinions, not measurements. I give them only to show the spread."),
    ]),
]

PATTERNS = [
    ("Most of the levers are decisions by governments", "The treaty, the annex, the climate pledges, the AI rules and the protection targets are all choices by states or institutions. The physical measures, such as carbon dioxide, warheads and wildlife counts, change on their own schedule."),
    ("Some dates have already moved", "The pandemic annex was to be done by the 2026 Assembly and is now due by May 2027. The six-month window reported for New START has passed without a report I could find."),
    ("Targets run ahead of delivery", "The 30% targets stand against 17.6% and 8.4%, and the finance target stands against $16.8 billion. The chart shows how far each had got."),
    ("Exposure and defense update at different speeds", "Carbon dioxide is read monthly and warhead counts yearly. The defenses move by negotiation and only show up in outcome figures years later, if at all."),
    ("The hypothesis tests do not all move together", "Test 1 in Chapter 16 is about the past and changes only if a large loss occurs or the record is revised. The other tests depend on the items above, and the tally in the last group would settle whether the claim of uniqueness holds."),
]

LIMITS = [
    "This chapter makes no forecasts. It names items the earlier chapters left open, with what the sources say about their status, and gives no probabilities.",
    "Status was newly checked for three items only: New START, the pandemic annex and COP31. The others carry the dates of the earlier chapters, mostly 13 to 27 October 2026.",
    "I found nothing on the September 2026 annex meeting, on the status of nuclear limits after early February, or on any result from the November summit.",
    "The New START reports rest on unnamed sources and a summary page, and they conflict. I read the pages through a summarizing tool.",
    "The list is my selection of nine items. It leaves out many hazards and many possible defenses.",
    "Nothing here is advice on what should be done. It lists what to watch.",
]

SRCS = [
    ("Checked for this chapter", [
        ("https://www.who.int/news/item/20-07-2026-who-member-states-continue-negotiations-on-the-pathogen-access-and-benefit-sharing-annex", "WHO, Member States continue negotiations on the PABS annex, 20 July 2026", "P"),
        ("https://www.kas.de/en/web/multilateraler-dialog-genf/geneva-telegram/detail/-/content/pabs-annex-zum-who-pandemieabkommen-who-mitgliedstaaten-verlaengern-verhandlungen-bis-2027", "Konrad-Adenauer-Stiftung, Geneva Telegram on the PABS annex extension", "S"),
        ("https://healthpolicy-watch.news/next-steps-tension-about-how-to-settle-the-pandemic-agreements-annex/", "Health Policy Watch, 21 May 2025, on the annex timetable", "S"),
        ("https://unu.edu/ehs/article/5-expectations-cop-31-antalya", "United Nations University, 5 expectations for COP31 in Antalya", "S"),
        ("https://www.axios.com/2026/02/05/new-start-arms-control-us-russia-extend", "Axios, US and Russia agree to observe New START after expiration (5 February 2026)", "S"),
        ("https://en.wikipedia.org/wiki/New_START", "Wikipedia, New START", "S"),
    ]),
    ("Earlier chapters", [
        ("https://claude.ai/artifact/SJ3PdrbEz1U14tZftAh7p5", "Chapter 6, A century of vulnerability", "C"),
        ("https://claude.ai/artifact/21WkXcCqVbi5EXSyYgitEL", "Chapter 7, The record of catastrophes", "C"),
        ("https://claude.ai/artifact/GgfHSBg2uJFXYtAS7QzhRU", "Chapter 8, Defenses built", "C"),
        ("https://claude.ai/artifact/Xdv42PDasn3ETek7T5x8oB", "Chapter 11, Nature defended", "C"),
        ("https://claude.ai/artifact/SNJrCBY4SongkYejYANqSt", "Chapter 12, Work, inequality and population", "C"),
        ("https://claude.ai/artifact/6Q4xocHoggdkKuRGv4HUEa", "Chapter 16, The comparison", "C"),
    ]),
]

groups, n = groups_html(AREAS)
assert n == 9, n
BODY = (
    section("scale", "Where the open items stand", "", stats_html(STATS)
            + chart_block("Warming: measured, and as projected by UNEP",
                          "Degrees above pre-industrial levels. The dashed line is 1.5 °C. Solid bars are as the sources state them. Ranges run from the lower to the upper figure.",
                          chart_html(CH_WARM, [(0, "0"), (1, "1"), (2, "2"), (3, "3")], 3.5, "Bar chart of measured warming of 1.43 degrees in 2025 and UNEP projections of 2.8 and 3.1 degrees under current policies and 2.3 to 2.8 degrees with pledges", mark=1.5))
            + chart_block("How far three targets have got",
                          "Each bar is the current figure as a share of its target. All three are my arithmetic. The finance figure is for 2023 and its target is for 2025.",
                          chart_html(CH_TARGET, [(0, "0%"), (25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")], 100, "Bar chart of progress toward targets: land protected 59 percent of target, ocean protected 28 percent, biodiversity finance 84 percent")))
    + section("entries", "What to watch", "Nine items in four groups. Each gives the recorded status, what to watch and how solid the figures are.", groups)
    + section("patterns", "What the items show", "", '<p class="note">These are my reading of the entries, not findings from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in PATTERNS) + "</div>")
    + section("limits", "What this chapter cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
    + '<section class="src" id="sources"><h2>Sources</h2><p class="note">Tags: P is an institution\'s own page, S is a secondary source such as a news report, briefing or encyclopedia, and C is an earlier chapter of this project, where the original sources are listed.</p>' + sources_html(SRCS) + "</section>"
)

CFG = {
    "shell": {
        "@@TITLE@@": "What Would Change the Balance",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Chapter 17 · Weighing",
        "@@H1@@": "What would change the balance",
        "@@SUB@@": "Nine open items, what the sources say about each, and what to watch",
        "@@LEDE@@": "Chapter 16 left several questions open. This chapter lists what could move them: decisions that are pending, exposures with no recorded defense, and evidence nobody has yet put together. It does not predict how any of them will turn out.",
        "@@ASOF@@": "Status checked on 28 October 2026 for New START, the pandemic annex and COP31. Other figures are current to the dates of the earlier chapters.",
        "@@NAV@@": nav([("scale", "Where they stand"), ("entries", "What to watch"), ("patterns", "What it shows"), ("limits", "Limits"), ("sources", "Sources")]),
        "@@FOOTER@@": "Several statements are my own arithmetic: that six months from 5 February 2026 is early August, and that 17.6, 8.4 and 16.8 are about 59%, 28% and 84% of their targets of 30, 30 and 20. The observations under “What the items show”, and the descriptions of what each evidence gap would change, are my own reading.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "what-would-change-the-balance.html")
    print("ok", n)
