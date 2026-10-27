import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data1 import ENTRIES_1, THENNOW_1, CONTEXT_1
from data2 import ENTRIES_2, THENNOW_2, CONTEXT_2

OUT = os.path.dirname(os.path.abspath(__file__))
e = html.escape

DOMAINS = [
    ("P", "Physics"),
    ("C", "Chemistry and materials"),
    ("L", "Life and medicine"),
    ("E", "Earth and cosmos"),
    ("I", "Information and mathematics"),
]
DNAME = dict(DOMAINS)

TEMPLATE = r"""<title>@@TITLE@@</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@500;600&family=IBM+Plex+Sans:wght@400;500&display=swap">
<style>
/* Layout: big date range header, a per-decade ribbon, a then-and-now table, a field filter, then entries grouped by decade along a thin rail. */
:root{
  --bg:#edf0f2;
  --surface:#f8fafb;
  --ink:#18222b;
  --ink-2:#4a5866;
  --line:#c9d1d8;
  --accent:@@ACC_L@@;
  --dP:#245f9c;--dC:#a8461f;--dL:#0f7357;--dE:#5a4fb0;--dI:#9c2f65;
  --font-display:"IBM Plex Sans Condensed","Arial Narrow",Arial,sans-serif;
  --font-body:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#10161c;--surface:#18212a;--ink:#e8edf1;--ink-2:#9fadba;--line:#2e3a45;--accent:@@ACC_D@@;
    --dP:#6aaaf0;--dC:#ee8a63;--dL:#46c4a0;--dE:#9d94ee;--dI:#e07fb0;color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#10161c;--surface:#18212a;--ink:#e8edf1;--ink-2:#9fadba;--line:#2e3a45;--accent:@@ACC_D@@;
  --dP:#6aaaf0;--dC:#ee8a63;--dL:#46c4a0;--dE:#9d94ee;--dI:#e07fb0;color-scheme:dark;
}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--font-body);font-size:15px;line-height:1.6;padding-inline:16px;padding-block:40px 64px}
.wrap{max-width:820px;margin:0 auto}
header{display:flex;flex-direction:column;gap:14px;margin-bottom:32px}
.kicker{font-family:var(--font-mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
h1{font-family:var(--font-display);font-weight:600;font-size:clamp(46px,12vw,92px);line-height:1;margin:0;color:var(--accent);letter-spacing:-.01em}
.sub{font-family:var(--font-display);font-weight:500;font-size:clamp(20px,4vw,26px);line-height:1.25;margin:0;text-wrap:balance}
.lede{margin:0;color:var(--ink-2);max-width:62ch}
.stats{display:flex;flex-wrap:wrap;gap:8px 28px;font-family:var(--font-mono);font-size:12.5px;color:var(--ink-2);padding-top:14px;border-top:2px solid var(--accent)}
.stats b{color:var(--ink);font-weight:500}
h2.sec{font-family:var(--font-display);font-weight:600;font-size:22px;margin:40px 0 12px}
.note{font-size:13px;color:var(--ink-2);margin:8px 0 0;max-width:70ch}
.ribbon{display:flex;align-items:flex-end;gap:5px;height:150px;padding-top:6px;border-bottom:1px solid var(--line)}
.col{flex:1 1 0;min-width:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:4px;height:100%}
.col .n{font-family:var(--font-mono);font-size:12px;color:var(--ink)}
.col .bar{width:100%;background:var(--accent);border-radius:2px 2px 0 0;min-height:3px}
.ribbon-l{display:flex;gap:5px;margin-top:4px}
.ribbon-l span{flex:1 1 0;min-width:0;text-align:center;font-family:var(--font-mono);font-size:11px;color:var(--ink-2)}
.tn{display:grid;gap:0;border-top:1px solid var(--line)}
.tn .row{display:grid;grid-template-columns:150px minmax(0,1fr) minmax(0,1fr);gap:4px 20px;padding:12px 0;border-bottom:1px solid var(--line)}
.tn .lab{font-family:var(--font-mono);font-size:12px;color:var(--ink-2);padding-top:2px}
.tn .cell{min-width:0}
.tn .y{display:block;font-family:var(--font-mono);font-size:11.5px;font-weight:500;color:var(--accent)}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 6px}
.chip{font:500 13px var(--font-body);color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:6px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:8px}
.chip i{width:9px;height:9px;border-radius:50%;background:var(--c,var(--ink-2));display:inline-block}
.chip[aria-pressed="true"]{border-color:var(--c,var(--ink));box-shadow:inset 0 0 0 1px var(--c,var(--ink))}
.chip:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.count{font-family:var(--font-mono);font-size:12px;color:var(--ink-2);margin:0 0 8px}
.decade{margin-top:8px}
.dh{font-family:var(--font-display);font-weight:600;font-size:24px;margin:24px 0 4px;display:flex;align-items:baseline;gap:12px;color:var(--ink)}
.dh span{font-family:var(--font-mono);font-weight:400;font-size:12px;color:var(--ink-2)}
.list{list-style:none;margin:0;padding:0 0 0 22px;border-left:2px solid var(--line)}
.item{display:grid;grid-template-columns:160px minmax(0,1fr);gap:4px 22px;padding:14px 0 16px;border-bottom:1px solid var(--line);position:relative}
.item:last-child{border-bottom:0}
.item:before{content:"";position:absolute;left:-29px;top:20px;width:12px;height:12px;border-radius:50%;background:var(--c);border:3px solid var(--bg)}
.when{font-family:var(--font-mono);font-size:14px;font-weight:500;line-height:1.4}
.when small{display:block;font-weight:400;font-size:11.5px;color:var(--c);margin-top:3px}
.what{min-width:0}
.what h3{font-family:var(--font-display);font-weight:600;font-size:19px;line-height:1.25;margin:0 0 2px}
.who{font-family:var(--font-mono);font-size:12px;color:var(--ink-2);margin:0 0 6px}
.what p.t{margin:0;max-width:62ch}
.fP{--c:var(--dP)}.fC{--c:var(--dC)}.fL{--c:var(--dL)}.fE{--c:var(--dE)}.fI{--c:var(--dI)}
.ctx{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}
.ctx div{border-top:2px solid var(--accent);padding-top:10px;min-width:0}
.ctx h3{font-family:var(--font-display);font-weight:600;font-size:17px;margin:0 0 6px}
.ctx p{margin:0;color:var(--ink-2);font-size:14px}
footer{margin-top:40px;font-size:12.5px;color:var(--ink-2);border-top:1px solid var(--line);padding-top:16px;max-width:70ch}
@media (max-width:600px){
  .item{grid-template-columns:minmax(0,1fr)}
  .list{padding-left:18px}
  .item:before{left:-25px}
  .tn .row{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
  .tn .lab{grid-column:1 / -1}
  .ribbon{gap:3px}.ribbon-l{gap:3px}
}
@media (prefers-reduced-motion:no-preference){.chip{transition:border-color .15s,box-shadow .15s}}
</style>

<div class="wrap">
<header>
  <div class="kicker">@@KICKER@@</div>
  <h1>@@RANGE@@</h1>
  <p class="sub">@@SUB@@</p>
  <p class="lede">@@LEDE@@</p>
  <div class="stats">@@STATS@@</div>
</header>

<h2 class="sec">Milestones per decade</h2>
<div class="ribbon" role="img" aria-label="Bar chart of the number of listed milestones in each decade">@@RIBBON@@</div>
<div class="ribbon-l" aria-hidden="true">@@RIBBONL@@</div>
<p class="note">Counts of the entries on this page, which I chose. They do not measure how much science happened in each decade.</p>

<h2 class="sec">Then and now</h2>
<div class="tn">@@THENNOW@@</div>

<h2 class="sec">Milestones by decade</h2>
<div class="filters" id="filters" role="group" aria-label="Filter by field">@@CHIPS@@</div>
<p class="count" id="count" aria-live="polite">Showing all @@N@@ milestones</p>

@@DECADES@@

<h2 class="sec">Context and limits</h2>
<div class="ctx">@@CTX@@</div>

<footer>@@FOOT@@</footer>
</div>

<script>
(function(){
  var bar=document.getElementById('filters');
  var chips=bar.querySelectorAll('.chip');
  var items=document.querySelectorAll('.item');
  var decades=document.querySelectorAll('.decade');
  var count=document.getElementById('count');
  var total=items.length;
  bar.addEventListener('click',function(ev){
    var b=ev.target.closest('.chip');
    if(!b)return;
    var f=b.getAttribute('data-f');
    chips.forEach(function(c){c.setAttribute('aria-pressed',c===b?'true':'false')});
    var shown=0;
    items.forEach(function(it){
      var ok=(f==='all'||it.getAttribute('data-f')===f);
      it.hidden=!ok;
      if(ok)shown++;
    });
    decades.forEach(function(d){
      d.hidden=d.querySelectorAll('.item:not([hidden])').length===0;
    });
    count.textContent=(f==='all')?('Showing all '+total+' milestones'):('Showing '+shown+' of '+total+' milestones');
  });
})();
</script>
"""

def build(entries, thennow, context, cfg, outname):
    entries = sorted(entries, key=lambda x: x[0])
    start, end = cfg["start"], cfg["end"]
    # decades
    first_dec = (start // 10) * 10
    decs = list(range(first_dec, (end // 10) * 10 + 1, 10))
    groups = {d: [] for d in decs}
    for en in entries:
        d = (en[0] // 10) * 10
        groups[d].append(en)
    counts = [len(groups[d]) for d in decs]
    mx = max(counts)
    ribbon = "".join(
        '<div class="col"><span class="n">%d</span><div class="bar" style="height:%dpx"></div></div>' % (c, max(3, round(c / mx * 100)))
        for c in counts
    )
    ribbonl = "".join("<span>%d</span>" % d for d in decs)
    tn = "".join(
        '<div class="row"><div class="lab">%s</div><div class="cell"><span class="y">%d</span>%s</div><div class="cell"><span class="y">%d</span>%s</div></div>'
        % (e(l), start, e(a), end, e(b))
        for (l, a, b) in thennow
    )
    chips = '<button class="chip" type="button" data-f="all" aria-pressed="true">All fields</button>' + "".join(
        '<button class="chip" type="button" data-f="%s" style="--c:var(--d%s)" aria-pressed="false"><i></i>%s</button>' % (k, k, e(v))
        for k, v in DOMAINS
    )
    dec_html = []
    for d in decs:
        if not groups[d]:
            continue
        label = "%ds" % d
        sub = "%d milestone%s" % (len(groups[d]), "" if len(groups[d]) == 1 else "s")
        items = []
        for (sy, disp, dom, title, who, text) in groups[d]:
            items.append(
                '<li class="item f%s" data-f="%s"><div class="when">%s<small>%s</small></div>'
                '<div class="what"><h3>%s</h3><p class="who">%s</p><p class="t">%s</p></div></li>'
                % (dom, dom, e(disp), e(DNAME[dom]), e(title), e(who), e(text))
            )
        dec_html.append(
            '<section class="decade"><h3 class="dh">%s <span>%s</span></h3><ol class="list">%s</ol></section>'
            % (label, sub, "".join(items))
        )
    ctx = "".join("<div><h3>%s</h3><p>%s</p></div>" % (e(h), e(p)) for h, p in context)
    page = TEMPLATE
    rep = {
        "@@TITLE@@": cfg["title"],
        "@@ACC_L@@": cfg["acc_l"],
        "@@ACC_D@@": cfg["acc_d"],
        "@@KICKER@@": e(cfg["kicker"]),
        "@@RANGE@@": cfg["range"],
        "@@SUB@@": e(cfg["sub"]),
        "@@LEDE@@": e(cfg["lede"]),
        "@@STATS@@": cfg["stats"].replace("@@N@@", str(len(entries))),
        "@@RIBBON@@": ribbon,
        "@@RIBBONL@@": ribbonl,
        "@@THENNOW@@": tn,
        "@@CHIPS@@": chips,
        "@@N@@": str(len(entries)),
        "@@DECADES@@": "\n".join(dec_html),
        "@@CTX@@": ctx,
        "@@FOOT@@": e(cfg["foot"]),
    }
    for k, v in rep.items():
        page = page.replace(k, v)
    assert "@@" not in page, [x for x in page.split("@@")][:3]
    with open(os.path.join(OUT, outname), "w", encoding="utf-8") as f:
        f.write(page)
    return len(entries), counts, decs

FOOT = "Written from general knowledge of the history of science, not from a primary-source review. Dates mark first publication or demonstration, and priority is often disputed. Check dates and figures before citing."

cfg1 = dict(
    title="Scientific Progress 1825–1925", start=1825, end=1925,
    acc_l="#8c5a12", acc_d="#d9a24a",
    kicker="Scientific progress, first century",
    range="1825–1925",
    sub="The century that built the physical and biological foundations",
    lede="In 1825 the first public steam railway was opening. By 1925 electricity powered cities, X-rays and radio were routine, germs and genes had reshaped medicine and biology, and relativity and quantum theory had rewritten physics.",
    stats='<span><b>@@N@@</b> milestones</span><span><b>5</b> fields</span><span>About <b>1 billion to 2 billion</b> people</span><span>First Nobel Prizes <b>1901</b></span>',
    foot=FOOT,
)
cfg2 = dict(
    title="Scientific Progress 1925–2025", start=1925, end=2025,
    acc_l="#1b4f8f", acc_d="#7db5f2",
    kicker="Scientific progress, second century",
    range="1925–2025",
    sub="The century that scaled the foundations and added computing",
    lede="In 1925 quantum mechanics was still being written down. By 2025 antibiotics, vaccines, and fertilizer had changed who lived, chips and networks had changed how people work, and telescopes, genome sequencers, and neural networks had opened new questions.",
    stats='<span><b>@@N@@</b> milestones</span><span><b>5</b> fields</span><span>About <b>2 billion to 8 billion</b> people</span><span>Smallpox eradicated <b>1980</b></span>',
    foot=FOOT,
)

for entries, tn, ctx, cfg, name in [
    (ENTRIES_1, THENNOW_1, CONTEXT_1, cfg1, "science-1825-1925.html"),
    (ENTRIES_2, THENNOW_2, CONTEXT_2, cfg2, "science-1925-2025.html"),
]:
    n, counts, decs = build(entries, tn, ctx, cfg, name)
    print(name, n, dict(zip(decs, counts)))
