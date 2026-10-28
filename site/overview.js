// Renders the overview from data/00-overview.json.
// Chapter pages are still the design prototypes; links point at them until they are ported.
const BOOK = '../project/book/';
const SLUGS = {1:'appearance-of-life',2:'pace-of-change',3:'life-and-health',4:'food-wealth-comfort',
  5:'knowledge-and-connection',6:'century-of-vulnerability',7:'record-of-catastrophes',8:'defenses-built',
  9:'nature-at-risk',10:'natures-catastrophes',11:'nature-defended',12:'work-inequality-population',
  13:'literacy-wisdom-knowledge',14:'mind-and-wellbeing',15:'power-and-governance',16:'the-comparison',
  17:'what-would-change-the-balance'};
const PART_COLORS = [
  ['oklch(50% 0.12 255)', 'oklch(38% 0.1 255)'],
  ['oklch(50% 0.13 150)', 'oklch(37% 0.11 150)'],
  ['oklch(56% 0.17 55)', 'oklch(40% 0.15 55)'],
  ['oklch(50% 0.11 195)', 'oklch(38% 0.09 195)'],
  ['oklch(48% 0.14 305)', 'oklch(38% 0.12 305)'],
  ['oklch(48% 0.18 29)', 'oklch(40% 0.17 29)']
];
const SUPPORT = [
  ['Industrial breakthroughs', 'A timeline of the major industrial breakthroughs in human history.', 's1-industrial-breakthroughs'],
  ['Scientific progress, 1825–1925', 'A century of science, from the first railways to the eve of quantum mechanics.', 's2-science-1825-1925'],
  ['Scientific progress, 1925–2025', 'The following century of science.', 's3-science-1925-2025']
];

function el(tag, cls, text, attrs) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text != null) e.textContent = text;
  if (attrs) for (const k in attrs) e.setAttribute(k, attrs[k]);
  return e;
}
function add(parent, ...kids) { kids.forEach(k => parent.appendChild(k)); return parent; }

function card(href, color, colorText, when, h, b) {
  const a = el('a', 'cc', null, { href });
  a.style.borderTop = '3px solid ' + color;
  if (when) { const w = el('div', 'when', when); w.style.color = colorText; a.appendChild(w); }
  return add(a, el('div', 'h', h), el('div', 'b', b));
}

function render(d) {
  const page = el('div', 'page'), wrap = el('div', 'wrap');
  page.appendChild(wrap);

  const header = el('header');
  add(header, el('div', 'bar'), el('div', 'kicker', d.kicker), el('h1', null, d.title),
    el('p', 'sub', d.sub), el('p', 'lede', d.lede), el('div', 'asof', d.asof));
  wrap.appendChild(header);

  const claim = el('div', 'claim');
  add(claim, el('div', 'tag', d.claim.tag), el('p', 'q', d.claim.q), el('p', 's', d.claim.s));
  wrap.appendChild(claim);

  const stats = el('div', 'stats');
  d.stats.forEach(s => { const c = el('div', 'stat'); add(c, el('b', null, s.b), el('span', null, s.span)); stats.appendChild(c); });
  wrap.appendChild(stats);

  add(wrap, el('h2', null, 'The chapters'), el('p', 'intro', 'Seventeen chapters in six parts. Each card opens its page.'));
  (d.groups || []).forEach((g, i) => {
    const [color, colorText] = PART_COLORS[i] || PART_COLORS[0];
    const part = el('section', 'part'), head = el('div', 'part-head'), grid = el('div', 'grid');
    const bar = el('i'); bar.style.background = color;
    add(head, bar, el('h3', null, g.header), el('span', null, g.count));
    g.items.forEach(it => {
      const num = parseInt((it.when || '').replace(/\D/g, ''), 10);
      const slug = SLUGS[num];
      const href = slug ? `${BOOK}${String(num).padStart(2, '0')}-${slug}.dc.html` : '#';
      grid.appendChild(card(href, color, colorText, it.when, it.h3, (it.p && it.p[0]) || ''));
    });
    add(part, head, grid);
    wrap.appendChild(part);
  });

  wrap.appendChild(el('h2', 'support', 'Supporting pages'));
  const sg = el('div', 'grid sm');
  SUPPORT.forEach(([h, b, slug]) => sg.appendChild(card(`${BOOK}${slug}.dc.html`, 'var(--support)', null, null, h, b)));
  wrap.appendChild(sg);

  const stands = el('section', 'stands'), pats = el('div', 'pats');
  d.patterns.forEach(p => {
    const c = el('div', 'pat');
    c.appendChild(el('h4', null, p.h3));
    p.p.forEach(t => c.appendChild(el('p', null, t)));
    pats.appendChild(c);
  });
  add(stands, el('h2', null, 'Where it stands'),
    el('p', 'note', 'This is my reading of the chapters, not a finding from the sources.'), pats);
  wrap.appendChild(stands);

  const limits = el('section', 'limits'), ul = el('ul');
  d.limits.forEach(t => ul.appendChild(el('li', null, t)));
  add(limits, el('h2', null, 'What this overview cannot show'), ul);
  wrap.appendChild(limits);

  wrap.appendChild(el('footer', null, d.footer));
  return page;
}

fetch('data/00-overview.json').then(r => r.json()).then(d => {
  document.title = d.title;
  const app = document.getElementById('app');
  app.replaceChildren(render(d));
}).catch(e => { document.getElementById('app').textContent = 'Failed to load: ' + e.message; });
