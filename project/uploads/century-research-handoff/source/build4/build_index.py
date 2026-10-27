from common import *

ACC, ACCD = "#2f5559", "#9fcdd1"
U = "https://claude.ai/artifact/"

PARTS = [
    ("Part 1 · The century", [
        ("1", "The appearance of human life", "7qSxXu33DCKP9HftfxH3Dc", "Six areas of daily life compared at about 1825, 1925 and 2025. The premise that life looked much the same in 1925 does not hold as stated for the United States, and holds better for parts of Asia and Africa. The biggest change after 1925 is in health and numbers (my reading)."),
        ("2", "The pace of change", "Ut88jmTViQUCc7jbfrZd1b", "The pace of change rose over two centuries, but the measures do not show a break at 1925: output stepped up near 1900, population after 1926 and energy use after 1950 (my reading)."),
    ]),
    ("Part 2 · Gains", [
        ("3", "Life and health", "79PSVNjqzAqJkcuARmF5wg", "Children dying before 15 fell from about 1 in 2 to 4%, and life expectancy rose from 32 to 71 (1900–2021). Drug-resistant infection is one of the setbacks it records."),
        ("4", "Food, wealth and comfort", "M7CcrBF81bKsbmrs98iQCq", "Food supply rose from 2,184 to 3,006 kilocalories per person per day, and French working hours fell by more than half. 673 million still faced hunger in 2024."),
        ("5", "Knowledge and connection", "1yPcv32YXUWW2jYuRESSNG", "Adult literacy rose from about 1 in 10 people to about 88%, and internet use from 16% to 74%. 739 million adults lack basic literacy and 2.2 billion are offline."),
    ]),
    ("Part 3 · Exposure", [
        ("6", "A century of vulnerability", "SJ3PdrbEz1U14tZftAh7p5", "Six features of exposure: planetary reach, speed, irreversibility, concentrated dependence, few hands and thin margins. 12,187 warheads, seven of nine planetary boundaries transgressed, and about half of food resting on synthetic nitrogen."),
        ("7", "The record of catastrophes", "21WkXcCqVbi5EXSyYgitEL", "Nineteen events. In share terms the worst losses came earlier: the Black Death took 30–60% of Europe, against 3.0–3.7% of the world in the Second World War."),
        ("8", "Defenses built", "GgfHSBg2uJFXYtAS7QzhRU", "Nineteen systems. Large measured falls where the hazard is known and countable, and several defenses weakening: New START expired, the US left the WHO, the pandemic annex is unfinished."),
    ]),
    ("Part 4 · Beyond humans", [
        ("9", "Nature at risk", "B7jDvigTvytm2ioPUncLbZ", "Monitored wildlife populations fell by an average of 73% from 1970 to 2022, about a million species are threatened, and 84% of reef area met bleaching-level heat in 2023–2025."),
        ("10", "Nature's catastrophes", "NUTcZosxAhd7YLJJ5s85BQ", "Mass extinctions removed about 70–85% of species at a time, and recovery took roughly 6 to 75 million years."),
        ("11", "Nature defended", "Xdv42PDasn3ETek7T5x8oB", "17.6% of land and 8.4% of ocean protected against 30% targets. Humpback whales recovered to about 93% of their pre-whaling size, and fewer than half of aligned national targets are on track."),
    ]),
    ("Part 5 · How people live", [
        ("12", "Work, inequality and population", "SNJrCBY4SongkYejYANqSt", "Child labour fell from 246 million to about 138 million. The richest 10% take 53% of income and the poorer half 8%. Population is projected to peak near 10.3 billion in the 2080s."),
        ("13", "Literacy, wisdom and knowledge", "PtP9Rvnfn7VatTSYdnv6Y9", "Measured scores rose for decades and now show reversals in several countries. Wisdom has no agreed measure, and the chapter gives no verdict."),
        ("14", "Mind and wellbeing", "9RZVCJrqYMM9PkrBB3YXEp", "1.2 billion people live with a mental disorder, one third of those with depression get formal care, and 1 in 6 people are affected by loneliness."),
        ("15", "Power and governance", "Q1B1ZSSMUHxtXhi72heMg4", "By V-Dem's 2026 count 74% of people live in autocracies and democracy for the average person is back at its 1978 level. Freedom House reports 20 years of decline."),
    ]),
    ("Part 6 · Weighing", [
        ("16", "The comparison", "6Q4xocHoggdkKuRGv4HUEa", "The hypothesis, stated and tested six ways. Realised loss: not supported. Worst case: supported as a model result only. Reach: supported in kind. Reversibility and defenses: mixed. Dependence: cannot be compared."),
        ("17", "What would change the balance", "VLRHDtiF4NdbNchLpzeUBN", "Nine open items with their latest checked status and what to watch, from the pandemic annex and nuclear limits to a century-by-century tally nobody has yet built."),
    ]),
]

SUPPORT = [
    ("Industrial breakthroughs", "EZXNpDinrBjMrY6HYzkxiS", "A timeline of the major industrial breakthroughs in human history."),
    ("Scientific progress, 1825–1925", "NJViUDxqQQfGjmSwVynETQ", "A century of science, from the first railways to the eve of quantum mechanics."),
    ("Scientific progress, 1925–2025", "32HDo7P7ycKcZG6obVjPug", "The following century of science."),
]

STATS = [
    ("17", "chapters in six parts, each ending with its own limits and sources"),
    ("3", "supporting pages: the industrial timeline and two centuries of science"),
    ("Not supported", "the claim that this century has had the worst realised losses, on share of people lost (Chapter 16)"),
    ("Supported in kind", "the claim that human-made exposure now reaches the whole world, with global-scale harm also found in the past (Chapter 16)"),
]

CLAIM = ('<div class="claim"><p class="tag">The hypothesis</p>'
         '<p class="q">Humanity has made itself vulnerable to catastrophic outcomes through the last 100 years of advancement, unlike any other 100 years of advancement in known history.</p>'
         '<p class="s">Tested in Chapter 16 against the evidence in the other chapters.</p></div>')

import common
common.SHELL = common.SHELL.replace("</style>", """
.claim{border-left:5px solid var(--accent);background:var(--surface);padding:16px 20px;margin:14px 0 8px;max-width:72ch}
.claim .tag{font-family:var(--font-mono);font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-2);margin:0 0 6px}
.claim p.q{font-family:var(--font-display);font-size:21px;line-height:1.4;margin:0;color:var(--ink)}
.claim p.s{font-size:14.5px;color:var(--ink-2);margin:10px 0 0}
</style>""", 1)


def chapters_html():
    out = []
    for part, items in PARTS:
        lis = []
        for num, title, aid, text in items:
            lis.append('<li class="item"><div class="when">Chapter %s</div><div class="what"><h3><a href="%s%s">%s</a></h3><p>%s</p></div></li>'
                       % (num, U, aid, e(title), e(text)))
        out.append('<section class="grp"><h3 class="gh">%s <span>%d %s</span></h3><ol class="list">%s</ol></section>'
                   % (e(part), len(items), "chapter" if len(items) == 1 else "chapters", "".join(lis)))
    return "\n".join(out)


READING = [
    ("The hypothesis is only partly borne out", "The evidence does not show that this century has been the worst in realised loss. It does show exposure at the scale of the whole world that none of the 19 earlier events I selected matches."),
    ("The gains are large and counted", "Health, food, literacy and connection improved by wide margins, and Chapters 3 to 5 give the figures. The strains in Chapters 12 to 15 remain alongside them."),
    ("The two sides are different kinds of evidence", "Gains and past losses are counted. Much of the exposure is modelled or judged, so the two cannot be added into one balance."),
    ("A narrower claim fits better than the wording", "The best-supported form is that this is the first century in my record in which human choices carry measured or modelled effects at the scale of the whole world. That is my judgment, and the original claim can still be kept and tested."),
]

LIMITS = [
    "Every chapter lists its own limits and the strength of each source, and those limits carry into this overview.",
    "Most figures are secondhand: I read pages through a summarizing tool, so check figures against the originals before citing them.",
    "Chapter 7 relies mostly on Wikipedia, and several later chapters rely on news reports of institutional reports.",
    "The results in Chapters 16 and 17 are my judgment, not findings from the sources.",
    "Chapters 12 to 15 rarely reach back to 1925, so for those the two centuries cannot be compared.",
    "Figures are current to dates between 13 and 28 October 2026, and several items, such as nuclear limits and the pandemic annex, are still moving.",
]

BODY = (
    section("claim", "The question", "This project asks what the last 100 years of advancement have done to humanity, including whether they left it more exposed to catastrophe than before. The chapters gather evidence on both sides, and only the sixteenth states and tests the hypothesis.", CLAIM + stats_html(STATS))
    + section("chapters", "The chapters", "Seventeen chapters in six parts. Each title links to its page.", chapters_html())
    + section("support", "Supporting pages", "",
              '<div class="thin">' + "".join('<div><h3><a href="%s%s">%s</a></h3><p>%s</p></div>' % (U, a, e(t), e(d)) for t, a, d in SUPPORT) + "</div>")
    + section("reading", "Where it stands", "", '<p class="note">This is my reading of the chapters, not a finding from the sources.</p><div class="pat">' + "".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in READING) + "</div>")
    + section("limits", "What this overview cannot show", "", '<ul class="plain">' + "".join("<li>%s</li>" % e(x) for x in LIMITS) + "</ul>")
)

CFG = {
    "shell": {
        "@@TITLE@@": "The Last Hundred Years",
        "@@ACC@@": ACC, "@@ACCD@@": ACCD,
        "@@KICKER@@": "Project overview",
        "@@H1@@": "The last hundred years",
        "@@SUB@@": "Seventeen chapters on what a century of advancement has done to humanity",
        "@@LEDE@@": "From daily life and health to catastrophe, defenses, the living world and how people live, ending with the hypothesis tested and the open items to watch.",
        "@@ASOF@@": "Index of the chapters as published on 28 October 2026.",
        "@@NAV@@": nav([("claim", "The question"), ("chapters", "Chapters"), ("support", "Supporting pages"), ("reading", "Where it stands"), ("limits", "Limits")]),
        "@@FOOTER@@": "The headline for each chapter is a summary of that chapter's page. The statements under “Where it stands” are my own reading.",
    },
    "body": BODY,
}

if __name__ == "__main__":
    build(CFG, "last-hundred-years-overview.html")
    print("ok")
