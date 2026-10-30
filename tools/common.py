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
                     GROUP_KINDS, EXPERTS, PAGES, SYNONYMS, TODAY)

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
  <script src="~/js/wireframe.js"></script>
  <script src="~/js/rss.js"></script>
</body>
</html>
'''
    path = os.path.join(SRC, 'pages', file)
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(out)
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
    idx = []
    for p in PAGES:
        idx.append(dict(type='Page', title=p['title'], url=p['url'], path='rss.org.uk › ' + p['path'],
                        summary=p['summary'], kw=p['kw'], topicLabels=topic_labels(p['topics']),
                        audLabels=[AUDIENCES[a] for a in p['aud']], access='public'))
    for ev in EVENTS:
        when = drange(ev['date'], ev['end'])
        idx.append(dict(type='Course' if ev['kind'] == 'course' else 'Event', title=ev['title'], url=event_url(ev),
                        path='rss.org.uk › Events and training', summary=ev['summary'] + ' ' + fmt_label(ev['fmt']) + '. ' + ev['place'] + '.',
                        kw=ev.get('sub', '') + ' ' + ev.get('level', '') + ' ' + ev['org'], date=ev['date'], when=when,
                        topicLabels=topic_labels(ev['topics']), audLabels=[AUDIENCES[a] for a in ev['aud']], access='public'))
    for n in NEWS:
        t = {'news': 'News', 'press': 'Press release', 'callout': 'Member callout'}[n['kind']]
        idx.append(dict(type=t, title=n['title'], url='article.html', path='rss.org.uk › News and publications',
                        summary=n['summary'], kw=n.get('source', ''), date=n['date'], when=d(n['date']),
                        topicLabels=topic_labels(n['topics']), audLabels=[], access='members' if n['kind'] == 'callout' else 'public'))
    for p in POLICY:
        idx.append(dict(type='Policy document', title=p['title'], url='policy.html', path='rss.org.uk › Policy and research › Policy library',
                        summary=p['summary'], kw=PTYPES[p['ptype']], date=p['date'], when=d(p['date']),
                        topicLabels=topic_labels(p['topics']), audLabels=[AUDIENCES['policymakers']], access='public',
                        doc=dict(file=p['id'] + '.pdf', page=p['doc']['page'], text=p['doc']['text'])))
    for j in JOBS:
        idx.append(dict(type='Job', title=f"{j['title']}, {j['employer']}", url='job.html', path='rss.org.uk › Resources › Jobs',
                        summary=f"{j['place']}. {j['salary']}. {j['contract']}. Closes {d(j['closes'])}.", kw='job vacancy careers',
                        date=j['closes'], when='Closes ' + d(j['closes']), topicLabels=topic_labels(j['topics']),
                        audLabels=[AUDIENCES['professionals']], access='public'))
    for g in GROUPS:
        idx.append(dict(type='Group', title=g['title'], url='group.html', path='rss.org.uk › Get involved › Sections and groups',
                        summary=f"{GROUP_KINDS[g['kind']]}, {g['region']}. News, events and how to join.", kw='group section local',
                        topicLabels=topic_labels(g['topics']), audLabels=[AUDIENCES['professionals']], access='public'))
    for x in EXPERTS:
        idx.append(dict(type='Expert', title=f"{x['name']}, {x['status']}", url='find-an-expert.html', path='rss.org.uk › Resources › Find an expert',
                        summary=f"{x['place']}. " + ', '.join(x['areas']) + '.', kw='expert register consultant ' + ' '.join(x['dirs']),
                        topicLabels=topic_labels(x['topics']), audLabels=[AUDIENCES['employers']],
                        access='members' if x['dirs'] == ['fellows'] else 'public'))
    js = ('/* data.js: sample search index for the prototype. Generated from tools/content.py; pure data, no logic. */\n'
          'window.RSS_INDEX = ' + json.dumps(idx, indent=1, ensure_ascii=False) + ';\n'
          'window.RSS_SYNONYMS = ' + json.dumps(SYNONYMS, indent=1) + ';\n')
    with open(os.path.join(SRC, 'js', 'data.js'), 'w', encoding='utf-8') as fh:
        fh.write(js)
    return len(idx)
