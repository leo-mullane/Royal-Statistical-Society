"""Helpers for generating the RSS prototype's source pages.

Pages are written to src/pages/ as plain HTML with ~/ paths and
<!-- @@include --> markers; build-includes.js turns them into docs/.
No JavaScript is generated here except data.js, which is pure data (JSON).
"""
import datetime
import html
import json
import os

from content import (TOPICS, AUDIENCES, EVENTS, NEWS, POLICY, PTYPES, JOBS, GROUPS,
                     GROUP_KINDS, EXPERTS, PAGES, TODAY)
from search_config import CONFIG
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
e = html.escape

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']


def d(iso):
    y, m, dd = [int(x) for x in iso.split('-')]
    return f'{dd} {MONTHS[m - 1]} {y}'


def drange(a, b):
    if a == b:
        return d(a)
    ya, ma, da = [int(x) for x in a.split('-')]
    yb, mb, db = [int(x) for x in b.split('-')]
    if ya == yb and ma == mb:
        return f'{da} to {db} {MONTHS[mb - 1]} {yb}'
    return f'{d(a)} to {d(b)}'


def slug(s):
    return '-'.join(''.join(c if c.isalnum() else ' ' for c in s.lower()).split())


def trunc(text, limit):
    """Shorten at a word boundary and add an ellipsis."""
    if len(text) <= limit:
        return text
    cut = text[:limit + 1].rsplit(' ', 1)[0].rstrip(' ,:;-')
    return cut + '\u2026'


def weekday(iso):
    return datetime.date.fromisoformat(iso).strftime('%a')


class Notes:
    """Numbered annotations for one page. Kinds: Behaviour, CMS, Open question,
    Integration, Proposed. Requirement references render as small pills."""

    def __init__(self):
        self.n = 0

    def __call__(self, text, reqs='', kind='Behaviour'):
        self.n += 1
        cls = 'wf-note query' if kind == 'Open question' else 'wf-note'
        pill = f' <span class="wf-req">{e(reqs)}</span>' if reqs else ''
        q = 'Q: ' if kind == 'Open question' else ''
        return (f'<div class="{cls}" data-note="{self.n}"><span class="wf-note-label">{kind}</span>'
                f'{q}{text}{pill}</div>')


def crumbs(items):
    lis = '<li class="breadcrumb-item"><a href="~/pages/home.html">Home</a></li>'
    for label, href in items:
        if href:
            lis += f'<li class="breadcrumb-item"><a href="{href}">{e(label)}</a></li>'
        else:
            lis += f'<li class="breadcrumb-item" aria-current="page">{e(label)}</li>'
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ul class="breadcrumb-list">{lis}</ul></nav>'


def aria_tabs(html_text):
    """Give every tab set its ARIA in the markup (wireframe.js keeps it in step)."""
    import re
    def tab(m):
        attrs = m.group(1)
        active = 'active' in m.group(0).split('>')[0].split('class="')[1].split('"')[0]
        pid = re.search(r'data-tab="([^"]+)"', attrs)
        extra = f' role="tab" aria-selected="{"true" if active else "false"}"'
        if pid:
            extra += f' id="tab-{pid.group(1)}" aria-controls="{pid.group(1)}"'
        return m.group(0).replace('<button', '<button' + extra, 1)
    html_text = re.sub(r'<button class="tab[^"]*"([^>]*)>', tab, html_text)
    def panel(m):
        pid = m.group(2)
        return f'<div class="{m.group(1)}" id="{pid}" role="tabpanel" aria-labelledby="tab-{pid}">'
    html_text = re.sub(r'<div class="(tab-panel[^"]*)" id="([^"]+)">', panel, html_text)
    return html_text.replace('<div class="tabs">', '<div class="tabs" role="tablist">')


def page(file, title, body, section='', bc=None, wide=False):
    """Write one page. bc: breadcrumb list of (label, href or None)."""
    bc_html = crumbs(bc) if bc is not None else ''
    out = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(title)} | Royal Statistical Society (prototype)</title>
  <link rel="stylesheet" href="~/css/base.css">
  <link rel="stylesheet" href="~/css/components.css">
  <link rel="stylesheet" href="~/css/rss.css">
  <link rel="stylesheet" href="~/css/theme.css">
</head>
<body data-section="{section}">
  <!-- @@include header.html -->

  <main id="main">
    <div class="container">
      {bc_html}
{body}
    </div>
  </main>

  <!-- @@include footer.html -->
  <script src="~/js/data.js"></script>
  <script src="~/js/search-engine.js"></script>
  <script src="~/js/wireframe.js"></script>
  <script src="~/js/rss.js"></script>
  <script src="~/js/search-ui.js"></script>
</body>
</html>
'''
    path = os.path.join(SRC, 'pages', file)
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(aria_tabs(out))
    PAGES_BUILT.append(file)


PAGES_BUILT = []


def topic_labels(slugs):
    return [TOPICS[s] for s in slugs]


def tags(slugs):
    return ''.join(f'<span class="tag">{e(TOPICS[s])}</span>' for s in slugs)


def fmt_label(fmt):
    return {'in-person': 'In person', 'online': 'Online', 'hybrid': 'Hybrid'}[fmt]


def event_url(ev):
    if ev['id'] == 'conference-2027':
        return 'conference.html'
    return 'course.html' if ev['kind'] == 'course' else 'event.html'


# -----------------------------------------------------------------------------
# Search index (data.js)
# -----------------------------------------------------------------------------
def write_data():
    """One index over every content type (REQ-037). Each entry carries the
    fields the engine scores (title, tags, summary, body), the facet values it
    filters on, and the line of meta that says what the result is."""
    idx = []
    aud = lambda keys: [AUDIENCES[a] for a in keys]

    for p in PAGES:
        idx.append(dict(id='page-' + slug(p['title']), cat='pages', tier='Page', type='Page', title=p['title'], url=p['url'],
                        summary=p['summary'], meta=['Page', p['path']],
                        tags=' '.join([p['kw'], p['path']] + topic_labels(p['topics'])), body='',
                        facets=dict(ctype=['Page'], topic=topic_labels(p['topics']), audience=aud(p['aud']), access=['Public'])))
    for ev in EVENTS:
        kind = 'Course' if ev['kind'] == 'course' else 'Event'
        sub = ev.get('sub', kind)
        when = 'Upcoming' if ev['end'] >= TODAY else 'Past'
        idx.append(dict(id='event-' + ev['id'], cat='events', tier=kind, type=kind, title=ev['title'], url=event_url(ev),
                        summary=ev['summary'], date=ev['date'],
                        meta=[sub, drange(ev['date'], ev['end']), fmt_label(ev['fmt']), ev['place']],
                        tags=' '.join([sub, ev.get('level', ''), ev['org'], fmt_label(ev['fmt'])] + topic_labels(ev['topics'])),
                        body=' '.join([ev['place'], ev['time'], ev['price']]),
                        facets=dict(ctype=[kind], etype=[sub], format=[fmt_label(ev['fmt'])], when=[when], topic=topic_labels(ev['topics']),
                                    audience=aud(ev['aud']), year=[ev['date'][:4]], access=['Public'])))
    for n in NEWS:
        t = n.get('rawtype') or {'news': 'News', 'press': 'Press release', 'callout': 'Member callout'}[n['kind']]
        access = 'Members only' if n['kind'] == 'callout' else 'Public'
        idx.append(dict(id='news-' + n['id'], cat='news', tier='News', type=t, title=n['title'], url='article.html',
                        summary=n['summary'], date=n['date'], meta=[t, d(n['date'])] + ([n['source']] if n.get('source') else []),
                        tags=' '.join([n.get('source', '')] + topic_labels(n['topics'])), body='',
                        facets=dict(ctype=[t], topic=topic_labels(n['topics']), year=[n['date'][:4]], access=[access])))
    for p in POLICY:
        pages = [[1, p['summary']]]
        if p['doc']['page'] != 1:
            pages.append([p['doc']['page'], p['doc']['text']])
        else:
            pages[0][1] += ' ' + p['doc']['text']
        idx.append(dict(id='doc-' + p['id'], cat='policy', tier='Document', type='Policy document', title=p['title'], url='policy.html',
                        summary=p['summary'], date=p['date'], meta=[PTYPES[p['ptype']], 'PDF, ' + p['size'], d(p['date'])],
                        tags=' '.join([PTYPES[p['ptype']]] + topic_labels(p['topics'])),
                        body=' '.join(x[1] for x in pages), pages=pages, file=p['id'] + '.pdf',
                        facets=dict(ctype=['Policy document'], ptype=[PTYPES[p['ptype']]], topic=topic_labels(p['topics']),
                                    audience=[AUDIENCES['policymakers']], year=[p['date'][:4]], access=['Public'])))
    for j in JOBS:
        idx.append(dict(id='job-' + j['id'], cat='jobs', tier='Job', type='Job', title=j['title'], url='job.html',
                        summary=f"{j['employer']}. {j['place']}. {j['salary']}.", date=j['closes'],
                        meta=['Job', j['employer'], j['place'], 'Closes ' + d(j['closes'])],
                        tags=' '.join([j['employer'], j['contract']] + topic_labels(j['topics'])), body=j['place'],
                        facets=dict(ctype=['Job'], topic=topic_labels(j['topics']), audience=[AUDIENCES['professionals']], access=['Public'])))
    for g in GROUPS:
        kind = GROUP_KINDS[g['kind']]
        idx.append(dict(id='group-' + g['id'], cat='groups', tier='Group', type=kind, title=g['title'], url='group.html',
                        summary=f"{kind}, {g['region']}. News, events and how to join.", meta=[kind, g['region']],
                        tags=' '.join([kind, g['region']] + topic_labels(g['topics'])), body='',
                        facets=dict(ctype=[kind], gkind=[kind], region=[g['region']], topic=topic_labels(g['topics']),
                                    audience=[AUDIENCES['professionals']], access=['Public'])))
    dirs = {'register': 'Professional Register', 'consultants': 'Consultants Directory', 'fellows': 'Fellows Directory'}
    for x in EXPERTS:
        plain = ' '.join(w for w in x['name'].split() if w not in ('Dr', 'Professor'))
        members = x['dirs'] == ['fellows']
        idx.append(dict(id='expert-' + x['id'], cat='experts', tier='Expert', type='Expert', title=x['name'],
                        url='find-an-expert.html?q=' + quote(plain) + ('&tab=fellows' if members else ''),
                        summary=', '.join(x['areas']) + '.', meta=[x['status'], x['areas'][0], x['place']],
                        tags=' '.join([x['status'], x['place']] + x['areas'] + [dirs[k] for k in x['dirs']] + topic_labels(x['topics'])), body='',
                        facets=dict(ctype=['Expert'], status=x['status'].split(', '), directory=[dirs[k] for k in x['dirs']],
                                    topic=topic_labels(x['topics']), audience=[AUDIENCES['employers']],
                                    access=['Members only' if members else 'Public'])))
    js = ('/* data.js: search index and search configuration. Generated from tools/content.py and\n'
          '   tools/search_config.py; pure data, no logic. All people, employers and documents are fictional. */\n'
          'window.RSS_CONFIG = ' + json.dumps(CONFIG, indent=1, ensure_ascii=False) + ';\n'
          'window.RSS_TOPICS = ' + json.dumps(list(TOPICS.values()), ensure_ascii=False) + ';\n'
          'window.RSS_INDEX = ' + json.dumps(idx, indent=1, ensure_ascii=False) + ';\n')
    with open(os.path.join(SRC, 'js', 'data.js'), 'w', encoding='utf-8') as fh:
        fh.write(js)
    return len(idx)
