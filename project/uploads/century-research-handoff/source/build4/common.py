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



SNAPCSS = """
.snap{width:100%;border-collapse:collapse;font-size:14.5px;margin:10px 0 6px}
.snap th{text-align:left;font-family:var(--font-mono);font-size:11.5px;font-weight:500;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-2);padding:6px 14px 6px 0;border-bottom:2px solid var(--accent)}
.snap td{vertical-align:top;padding:10px 14px 10px 0;border-bottom:1px solid var(--line);line-height:1.5}
.snap td.m{font-weight:500;width:21%}
.snap td.na{color:var(--ink-2)}
.dom{margin-top:34px}
.dom h3{font-size:22px;margin-bottom:2px}
.dom .intro{font-size:14.5px;color:var(--ink-2);max-width:68ch;margin:0 0 4px}
@media (max-width:620px){
  .snap,.snap tbody,.snap tr,.snap td{display:block;width:auto}
  .snap thead{display:none}
  .snap tr{padding:10px 0;border-bottom:1px solid var(--line)}
  .snap td{border:0;padding:2px 0}
  .snap td.m{width:auto;font-size:15.5px;padding-bottom:2px}
  .snap td[data-l]::before{content:attr(data-l);display:block;font-family:var(--font-mono);font-size:11px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-2);margin-top:6px}
}
"""
SHELL = SHELL.replace("</style>", SNAPCSS + "</style>", 1)


def snap_html(cols, rows):
    head = "<tr><th>Measure</th>" + "".join("<th>%s</th>" % e(c) for c in cols) + "</tr>"
    body = []
    for r in rows:
        tds = '<td class="m">%s</td>' % e(r[0])
        for c, v in zip(cols, r[1:]):
            if v is None:
                tds += '<td class="na" data-l="%s">No figure found</td>' % e(c)
            else:
                tds += '<td data-l="%s">%s</td>' % (e(c), e(v))
        body.append("<tr>%s</tr>" % tds)
    return '<table class="snap"><thead>%s</thead><tbody>%s</tbody></table>' % (head, "".join(body))


def domain_html(id_, title, intro, cols, rows, solid):
    return ('<section class="dom" id="%s"><h3>%s</h3><p class="intro">%s</p>%s<p class="solid"><b>How solid</b> %s</p></section>'
            % (id_, e(title), e(intro), snap_html(cols, rows), e(solid)))
