/* ==========================================================================
   search-engine.js — the prototype search engine (REQ-037 to REQ-046).
   Written directly (never generated). Depends on data.js.

   One index over every content type. Every search box on the site calls the
   same search(): the header's Events and Resources boxes are this function
   with a scope applied, and the keyword boxes on the listing pages (events,
   news, policy, groups, experts, jobs) use matchIds() over the same index.
   Ranking, synonyms, correction, facets and promoted results are read from
   window.RSS_CONFIG, not hard-coded here.

   This is a wireframe-grade engine running in the browser over a small,
   fictional dataset. It demonstrates behaviour, not production performance.
   ========================================================================== */

(function () {
  'use strict';

  var C = window.RSS_CONFIG;
  var INDEX = window.RSS_INDEX || [];
  var TOPICS = window.RSS_TOPICS || [];
  if (!C) return;
  var STOP = C.stopWords || [];
  var W = C.fieldWeights;

  function slug(s) {
    return String(s).toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  }
  /* Lower-case, strip accents and apostrophes, collapse punctuation (REQ-043) */
  function norm(s) {
    return String(s || '').toLowerCase()
      .replace(/[’']/g, '')
      .normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/&/g, ' and ')
      .replace(/[^a-z0-9\s]/g, ' ')
      .replace(/\s+/g, ' ').trim();
  }
  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  /* Pages live in pages/, the contents page at the root. */
  function pageUrl(file, params) {
    var inPages = /\/pages\//.test(window.location.pathname);
    var qs = params ? new URLSearchParams(params).toString() : '';
    var hash = '';
    var i = file.indexOf('#');
    if (i >= 0) { hash = file.slice(i); file = file.slice(0, i); }
    if (qs) file += (file.indexOf('?') >= 0 ? '&' : '?') + qs;
    return (inPages ? '' : 'pages/') + file + hash;
  }

  var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  function formatDate(iso) {
    if (!iso) return '';
    var p = iso.split('-');
    return parseInt(p[2], 10) + ' ' + MONTHS[parseInt(p[1], 10) - 1] + ' ' + p[0];
  }

  /* --- Build the one index (REQ-037) ---------------------------------------- */
  var ALIAS = C.contentTypeAliases || {};
  var docs = INDEX.map(function (d) {
    var label = ALIAS[d.type] || d.type;
    var facets = {};
    Object.keys(d.facets || {}).forEach(function (k) {
      facets[k] = d.facets[k].map(function (v) { return k === 'ctype' ? (ALIAS[v] || v) : v; });
    });
    return {
      id: d.id, cat: d.cat, typeLabel: label, title: d.title, url: d.url, summary: d.summary || '',
      date: d.date || '', meta: (d.meta || []).map(function (m, i) { return i === 0 ? (ALIAS[m] || m) : m; }),
      pages: d.pages || null, file: d.file || '', facets: facets,
      members: (facets.access || [])[0] === 'Members only',
      tier: C.tiers[d.tier] || 1,
      n: { title: norm(d.title), tags: norm(d.tags || ''), summary: norm(d.summary || ''), body: norm(d.body || '') }
    };
  });
  var docById = {};
  docs.forEach(function (d) { docById[d.id] = d; });

  /* How much content is tagged to each topic: breaks type-ahead ties */
  var popularity = {};
  docs.forEach(function (d) {
    (d.facets.topic || []).forEach(function (v) { popularity[v] = (popularity[v] || 0) + 1; });
  });

  /* --- Vocabulary for spelling correction (REQ-043) ------------------------- */
  var vocab = {};
  docs.forEach(function (d) {
    [d.n.title, d.n.tags, d.n.summary, d.n.body].join(' ').split(' ').forEach(function (w) {
      if (w.length >= 3) vocab[w] = (vocab[w] || 0) + 1;
    });
  });
  C.synonyms.forEach(function (g) { g.forEach(function (m) { m.split(' ').forEach(function (w) { vocab[w] = (vocab[w] || 0) + 1; }); }); });
  var vocabWords = Object.keys(vocab);

  function lev(a, b) {
    var prev = [], cur, i, j;
    for (j = 0; j <= b.length; j++) prev.push(j);
    for (i = 1; i <= a.length; i++) {
      cur = [i];
      for (j = 1; j <= b.length; j++) {
        cur.push(Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a.charAt(i - 1) === b.charAt(j - 1) ? 0 : 1)));
      }
      prev = cur;
    }
    return prev[b.length];
  }

  /* Only words of 4+ letters, never stop words, never a word that starts a
     known word. Nearest word within the limit; ties go to the commoner word. */
  function correct(nq) {
    var R = C.correction;
    var changed = false;
    var out = nq.split(' ').map(function (t) {
      if (t.length < R.minLength || STOP.indexOf(t) >= 0) return t;
      if (vocabWords.some(function (w) { return w.indexOf(t) === 0; })) return t;
      var best = null;
      var bestD = (t.length >= R.longFrom ? R.maxDistanceLong : R.maxDistance) + 1;
      vocabWords.forEach(function (w) {
        if (Math.abs(w.length - t.length) > R.lengthWindow) return;
        var dist = lev(t, w);
        if (dist < bestD || (dist === bestD && best && vocab[w] > vocab[best])) { bestD = dist; best = w; }
      });
      if (best) { changed = true; return best; }
      return t;
    }).join(' ');
    return changed ? out : null;
  }

  /* --- Query parsing ---------------------------------------------------------
     "exact phrases" and -excluded words are read first. The rest becomes
     concepts: synonym groups (longest member first, one concept per group,
     REQ-045) and single words. Every concept must match (AND); any member of
     a group will do (OR). */
  function splitQuery(raw) {
    var phrases = [], excludes = [];
    var rest = String(raw || '').replace(/"([^"]+)"/g, function (_, p) { var n = norm(p); if (n) phrases.push(n); return ' '; });
    rest = rest.replace(/(^|\s)-(\S+)/g, function (_, s, w) { var n = norm(w); if (n) excludes.push(n); return ' '; });
    return { rest: norm(rest), phrases: phrases, excludes: excludes };
  }

  function parse(nq, phrases) {
    var concepts = [];
    var rest = ' ' + nq + ' ';
    var members = [];
    C.synonyms.forEach(function (g, gi) { g.forEach(function (m) { members.push({ m: m, gi: gi }); }); });
    members.sort(function (a, b) { return b.m.length - a.m.length; });
    var used = {};
    members.forEach(function (x) {
      var needle = ' ' + x.m + ' ';
      if (used[x.gi] || rest.indexOf(needle) < 0) return;
      used[x.gi] = true;
      rest = rest.replace(needle, ' ');
      concepts.push({ orig: x.m, alts: C.synonyms[x.gi].slice(), syn: true });
    });
    rest.trim().split(' ').forEach(function (t) {
      if (t && STOP.indexOf(t) < 0) concepts.push({ orig: t, alts: [t], syn: false });
    });
    (phrases || []).forEach(function (p) { concepts.push({ orig: p, alts: [p], syn: false, phrase: true }); });
    return concepts;
  }

  /* Short terms (3 letters or fewer, e.g. "ai", "r") match whole words only;
     longer terms match the start of a word. Phrases match exactly. */
  function has(text, phrase, exact) {
    if (!text) return false;
    if (exact || phrase.length <= 3) return (' ' + text + ' ').indexOf(' ' + phrase + ' ') >= 0;
    return (' ' + text).indexOf(' ' + phrase) >= 0;
  }

  function scoreDoc(doc, concepts, nq, synHits, excludes) {
    var f = doc.n, i;
    for (i = 0; i < excludes.length; i++) {
      if (has(f.title, excludes[i]) || has(f.tags, excludes[i]) || has(f.summary, excludes[i]) || has(f.body, excludes[i])) return 0;
    }
    var total = 0;
    for (i = 0; i < concepts.length; i++) {
      var c = concepts[i];
      var best = 0, bestAlt = null;
      c.alts.forEach(function (alt) {
        var s = 0;
        if (has(f.title, alt, c.phrase)) s += W.title;
        if (has(f.tags, alt, c.phrase)) s += W.tags;
        if (has(f.summary, alt, c.phrase)) s += W.summary;
        if (has(f.body, alt, c.phrase)) s += W.body;
        if (s > best) { best = s; bestAlt = alt; }
      });
      if (!best) return 0;
      if (c.syn && bestAlt !== c.orig) synHits[c.orig] = c.alts.filter(function (a) { return a !== c.orig; });
      total += best;
    }
    if (nq) {
      if (f.title === nq) total += W.exactTitle;
      else if (f.title.indexOf(nq) === 0) total += W.titlePrefix;
    }
    /* The tier is a multiplier, so an expert or group page outranks a passing
       mention elsewhere, and documents sit below the Society's own pages. */
    return total * doc.tier;
  }

  /* --- State <-> URL ------------------------------------------------------- */
  var FACET_KEYS = C.facets.map(function (f) { return f.key; });
  var CAT_KEYS = C.categories.map(function (c) { return c.key; });

  function readState(search) {
    var p = new URLSearchParams(search === undefined ? window.location.search : search);
    var scope = C.scopes[p.get('scope')] ? p.get('scope') : '';
    var type = CAT_KEYS.indexOf(p.get('type')) >= 0 ? p.get('type') : '';
    if (scope && !type) type = C.scopes[scope].type;
    var state = {
      q: p.get('q') || '',
      type: type,
      scope: scope,
      sort: p.get('sort') || 'relevance',
      page: parseInt(p.get('page'), 10) || 1,
      per: parseInt(p.get('per'), 10) || 10,
      layout: p.get('layout') === 'topbar' ? 'topbar' : 'sidebar',
      letter: (p.get('letter') || '').toUpperCase().slice(0, 1),
      raw: p.get('raw') === '1',
      filters: {}
    };
    FACET_KEYS.forEach(function (k) {
      var v = p.getAll(k);
      state.filters[k] = v.length ? [].concat.apply([], v.map(function (x) { return x.split('|'); })).filter(Boolean) : [];
    });
    return state;
  }

  function toParams(state) {
    var p = {};
    if (state.q) p.q = state.q;
    if (state.scope) p.scope = state.scope;
    if (state.type && !(state.scope && C.scopes[state.scope].type === state.type)) p.type = state.type;
    FACET_KEYS.forEach(function (k) {
      if (state.filters[k] && state.filters[k].length) p[k] = state.filters[k].join('|');
    });
    if (state.sort && state.sort !== 'relevance') p.sort = state.sort;
    if (state.per && state.per !== 10) p.per = String(state.per);
    if (state.page > 1) p.page = String(state.page);
    if (state.letter) p.letter = state.letter;
    if (state.layout === 'topbar') p.layout = 'topbar';
    if (state.raw) p.raw = '1';
    return p;
  }

  /* --- Search ---------------------------------------------------------------- */
  function run(nq, sq) {
    var concepts = parse(nq, sq.phrases);
    var synHits = {};
    var hits = [];
    if (!concepts.length) return { hits: hits, synHits: synHits, concepts: concepts };
    docs.forEach(function (d) {
      var s = scoreDoc(d, concepts, nq, synHits, sq.excludes);
      if (s > 0) hits.push({ doc: d, score: s });
    });
    return { hits: hits, synHits: synHits, concepts: concepts };
  }

  function passes(doc, filters, exceptKey) {
    for (var i = 0; i < FACET_KEYS.length; i++) {
      var k = FACET_KEYS[i];
      if (k === exceptKey) continue;
      var want = filters[k];
      if (!want || !want.length) continue;
      var vals = doc.facets[k] || [];
      if (!want.some(function (w) { return vals.indexOf(w) >= 0; })) return false;
    }
    return true;
  }

  function surnameLetter(doc) {
    var parts = doc.title.split(' ');
    return norm(parts[parts.length - 1]).charAt(0).toUpperCase();
  }

  function order(key, a, b) {
    if (key === 'year') return b.value.localeCompare(a.value);
    var o = (C.valueOrder || {})[key];
    if (o) {
      var ia = o.indexOf(a.value), ib = o.indexOf(b.value);
      return (ia < 0 ? 99 : ia) - (ib < 0 ? 99 : ib) || a.value.localeCompare(b.value);
    }
    return b.count - a.count || a.value.localeCompare(b.value);
  }

  function search(state) {
    var sq = splitQuery(state.q);
    var nq = sq.rest;
    var out = { query: state.q, correctedFrom: null, correctedTo: null, synonyms: {}, bestBet: null, concepts: [] };
    var base;

    if (nq || sq.phrases.length) {
      var r = run(nq, sq);
      if (!r.hits.length && !state.raw && nq) {
        var fixed = correct(nq);
        if (fixed) {
          var r2 = run(fixed, sq);
          if (r2.hits.length) { out.correctedFrom = state.q; out.correctedTo = fixed; r = r2; }
        }
      }
      base = r.hits;
      out.synonyms = r.synHits;
      out.concepts = r.concepts;
      var bb = (C.bestBets || {})[nq];
      if (bb && docById[bb]) out.bestBet = docById[bb];
    } else {
      base = docs.map(function (d) { return { doc: d, score: d.tier }; });
    }

    /* Surname A to Z, when results are limited to experts */
    if (state.letter) {
      base = base.filter(function (h) { return h.doc.cat === 'experts' && surnameLetter(h.doc) === state.letter; });
    }

    /* Tab counts stay accurate while one tab is showing (REQ-038) */
    out.tabCounts = {};
    out.total = 0;
    CAT_KEYS.forEach(function (k) { out.tabCounts[k] = 0; });
    base.forEach(function (h) {
      if (passes(h.doc, state.filters)) { out.tabCounts[h.doc.cat] += 1; out.total += 1; }
    });

    /* Each facet is counted with every other filter applied except its own (REQ-039) */
    out.facets = {};
    FACET_KEYS.forEach(function (k) {
      var tally = {};
      base.forEach(function (h) {
        if (state.type && h.doc.cat !== state.type) return;
        if (!passes(h.doc, state.filters, k)) return;
        (h.doc.facets[k] || []).forEach(function (v) { tally[v] = (tally[v] || 0) + 1; });
      });
      (state.filters[k] || []).forEach(function (v) { if (!tally[v]) tally[v] = 0; });
      out.facets[k] = Object.keys(tally).map(function (v) { return { value: v, count: tally[v] }; })
        .sort(function (a, b) { return order(k, a, b); });
    });

    var results = base.filter(function (h) {
      return (!state.type || h.doc.cat === state.type) && passes(h.doc, state.filters);
    });

    /* Sort (REQ-040). Undated items go last under the date sorts. */
    var byDateDesc = function (a, b) { return (b.doc.date || '').localeCompare(a.doc.date || ''); };
    var byTitle = function (a, b) { return a.doc.title.localeCompare(b.doc.title); };
    var undatedLast = function (a, b) { return !a.doc.date === !b.doc.date ? 0 : (a.doc.date ? -1 : 1); };
    var catOrder = function (a, b) { return CAT_KEYS.indexOf(a.doc.cat) - CAT_KEYS.indexOf(b.doc.cat); };
    var sorters = {
      relevance: function (a, b) { return b.score - a.score || byDateDesc(a, b) || byTitle(a, b); },
      newest: function (a, b) { return undatedLast(a, b) || byDateDesc(a, b) || b.score - a.score; },
      oldest: function (a, b) { return undatedLast(a, b) || -byDateDesc(a, b) || b.score - a.score; },
      year: function (a, b) {
        return undatedLast(a, b) || (b.doc.date || '').slice(0, 4).localeCompare((a.doc.date || '').slice(0, 4)) || b.score - a.score;
      },
      type: function (a, b) { return catOrder(a, b) || b.score - a.score; },
      az: byTitle
    };
    results.sort(sorters[state.sort] || sorters.relevance);
    out.results = results;
    return out;
  }

  /* Ids matching a keyword, for the listing pages' keyword boxes */
  function matchIds(q) {
    var st = readState('');
    st.q = q;
    var r = search(st);
    var set = {};
    r.results.forEach(function (h) { set[h.doc.id] = true; });
    return { ids: set, correctedTo: r.correctedTo, synonyms: r.synonyms };
  }

  /* --- Highlighting (REQ-042) ---------------------------------------------- */
  function highlight(text, concepts) {
    text = String(text || '');
    if (!concepts || !concepts.length) return esc(text);
    var ranges = [];
    concepts.forEach(function (c) {
      c.alts.forEach(function (alt) {
        var words = alt.split(' ').map(function (w) { return w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); });
        var tail = alt.length <= 3 || c.phrase ? '(?![A-Za-z0-9])' : '[A-Za-z0-9]*';
        var re = new RegExp('(^|[^A-Za-z0-9])(' + words.join('[^A-Za-z0-9]+') + tail + ')', 'gi');
        var m;
        while ((m = re.exec(text)) !== null) {
          var start = m.index + m[1].length;
          ranges.push([start, start + m[2].length]);
          if (re.lastIndex === m.index) re.lastIndex++;
        }
      });
    });
    if (!ranges.length) return esc(text);
    ranges.sort(function (a, b) { return a[0] - b[0]; });
    var merged = [ranges[0]];
    ranges.slice(1).forEach(function (r) {
      var last = merged[merged.length - 1];
      if (r[0] <= last[1]) last[1] = Math.max(last[1], r[1]); else merged.push(r);
    });
    var out = '', pos = 0;
    merged.forEach(function (r) {
      out += esc(text.slice(pos, r[0])) + '<mark>' + esc(text.slice(r[0], r[1])) + '</mark>';
      pos = r[1];
    });
    return out + esc(text.slice(pos));
  }

  /* For documents, the snippet is the page that matched (REQ-044) */
  function snippet(doc, concepts) {
    if (doc.pages && concepts && concepts.length) {
      for (var i = 0; i < doc.pages.length; i++) {
        var pn = norm(doc.pages[i][1]);
        var hit = concepts.some(function (c) { return c.alts.some(function (a) { return has(pn, a, c.phrase); }); });
        if (hit && (doc.pages[i][0] !== 1 || !concepts.some(function (c) { return c.alts.some(function (a) { return has(doc.n.summary, a); }); }))) {
          return { page: doc.pages[i][0], html: highlight(doc.pages[i][1], concepts) };
        }
      }
    }
    return { page: null, html: highlight(doc.summary || '', concepts) };
  }

  /* --- Type-ahead suggestions (REQ-037, REQ-043, REQ-045) -------------------
     Taxonomy first (topics, then sections and groups), then experts, then
     pages, events and documents. scope narrows it to one section. */
  function suggest(q, scope) {
    var nq = norm(q);
    if (nq.length < 2) return [];
    var groups = [];
    function wordStart(name) { return (' ' + norm(name)).indexOf(' ' + nq) >= 0; }

    var synMembers = [];
    C.synonyms.forEach(function (g) {
      var hit = g.filter(function (m) { return m.indexOf(nq) === 0 || (nq.length >= 3 && (' ' + m).indexOf(' ' + nq) >= 0); })[0];
      if (hit) synMembers.push({ hit: hit, group: g });
    });
    function viaFor(name) {
      var ns = norm(name), via = null;
      synMembers.forEach(function (x) {
        if (via) return;
        if (x.group.some(function (m) { return m !== x.hit && has(ns, m); })) via = x.hit;
      });
      return via;
    }

    var tax = [];
    TOPICS.forEach(function (t) {
      var direct = wordStart(t);
      var via = direct ? null : viaFor(t);
      if (!direct && !via) return;
      tax.push({ kind: 'topic', label: t, detail: 'Topic', via: via, pop: popularity[t] || 0,
        rank: (norm(t).indexOf(nq) === 0 ? 0 : 1) + (via ? 2 : 0) });
    });
    if (!scope || scope === 'experts') {
      docs.forEach(function (d) {
        if (d.cat !== 'groups') return;
        var direct = wordStart(d.title);
        var via = direct ? null : viaFor(d.title);
        if (!direct && !via) return;
        tax.push({ kind: 'group', label: d.title, detail: d.typeLabel, via: via, doc: d, pop: 0,
          rank: (d.n.title.indexOf(nq) === 0 ? 0.2 : 1.2) + (via ? 2 : 0) + (d.typeLabel === 'Section' ? 0 : 0.3) });
      });
    }
    tax.sort(function (a, b) { return a.rank - b.rank || b.pop - a.pop || a.label.length - b.label.length; });
    if (tax.length) groups.push({ label: scope ? 'Filter by topic' : 'Topics, sections and groups', items: tax.slice(0, 5) });

    if (!scope || scope === 'experts') {
      var ppl = docs.filter(function (d) { return d.cat === 'experts' && wordStart(d.title); }).slice(0, 4).map(function (d) {
        return { kind: 'expert', label: d.title, detail: d.meta.filter(Boolean).join(' · ') + (d.members ? ' · Members only' : ''), doc: d };
      });
      if (ppl.length) groups.push({ label: 'Experts', items: ppl });
    }

    if (scope !== 'experts') {
      var cats = scope ? [C.scopes[scope].type] : ['pages', 'events', 'news', 'policy', 'jobs'];
      var pages = docs.filter(function (d) { return cats.indexOf(d.cat) >= 0 && wordStart(d.title); })
        .sort(function (a, b) { return b.tier - a.tier || (b.date || '').localeCompare(a.date || ''); })
        .slice(0, 4).map(function (d) { return { kind: 'page', label: d.title, detail: d.typeLabel, doc: d }; });
      if (pages.length) groups.push({ label: scope ? C.scopes[scope].label : 'Pages, events and documents', items: pages });
    }
    return groups;
  }

  window.RSSSearch = {
    config: C, docs: docs, docById: docById, topics: TOPICS,
    slug: slug, norm: norm, esc: esc, pageUrl: pageUrl, formatDate: formatDate,
    readState: readState, toParams: toParams, search: search, matchIds: matchIds,
    highlight: highlight, snippet: snippet, suggest: suggest, passes: passes,
    surnameLetter: surnameLetter, splitQuery: splitQuery, FACET_KEYS: FACET_KEYS
  };
})();
