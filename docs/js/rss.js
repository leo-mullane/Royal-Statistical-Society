/* ==========================================================================
   rss.js — prototype behaviour specific to the RSS site.
   Written directly (never generated). Driven by data attributes; no page has
   its own script. Depends on data.js (window.RSS_INDEX, window.RSS_SYNONYMS).
   ========================================================================== */

(function () {
  'use strict';

  var TODAY = '2026-10-30'; /* prototype "today", so upcoming and past stay stable */

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function store(key, value) {
    try {
      if (value === undefined) return window.sessionStorage.getItem(key);
      window.sessionStorage.setItem(key, value);
    } catch (e) { return null; }
    return null;
  }
  function params() { return new URLSearchParams(window.location.search); }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  /* Pages live in pages/, the contents page at the root. Index URLs are page
     file names, so work out the prefix from where we are. */
  function pageHref(file) {
    var inPages = /\/pages\//.test(window.location.pathname);
    return (inPages ? '' : 'pages/') + file;
  }

  /* --- Annotations: OFF by default -------------------------------------- */
  function initNotes() {
    var btn = $('[data-notes-toggle]');
    var on = store('rss-notes') === 'on';
    function apply() {
      document.body.classList.toggle('wf-notes-hidden', !on);
      if (!btn) return;
      btn.setAttribute('aria-checked', on ? 'true' : 'false');
      var label = $('.notes-label', btn);
      if (label) label.textContent = on ? 'Annotations on' : 'Annotations off';
    }
    if (btn) {
      btn.addEventListener('click', function () {
        on = !on;
        store('rss-notes', on ? 'on' : 'off');
        apply();
      });
    }
    apply();
  }

  /* --- Persona: who is viewing (REQ-109, REQ-177, REQ-178) --------------- */
  var PERSONA_NAMES = { guest: '', registered: '(Sam)', member: '(Dr Alex Morgan)', lapsed: '(Chris)' };
  function getPersona() {
    var fromUrl = params().get('as');
    if (fromUrl && PERSONA_NAMES.hasOwnProperty(fromUrl)) store('rss-persona', fromUrl);
    return store('rss-persona') || 'guest';
  }
  function applyPersona(p) {
    document.body.setAttribute('data-persona', p);
    $$('[data-show-for]').forEach(function (el) {
      var list = el.getAttribute('data-show-for').split(/\s+/);
      el.hidden = list.indexOf(p) === -1;
    });
    $$('[data-persona-name]').forEach(function (el) { el.textContent = PERSONA_NAMES[p] || ''; });
    $$('[data-persona-select]').forEach(function (s) { s.value = p; });
  }
  function initPersona() {
    var p = getPersona();
    applyPersona(p);
    $$('[data-persona-select]').forEach(function (s) {
      s.addEventListener('change', function () {
        store('rss-persona', s.value);
        applyPersona(s.value);
      });
    });
    $$('[data-sign-in-as]').forEach(function (b) {
      b.addEventListener('click', function (ev) {
        ev.preventDefault();
        store('rss-persona', b.getAttribute('data-sign-in-as'));
        window.location.href = b.getAttribute('href');
      });
    });
    $$('[data-sign-out]').forEach(function (b) {
      b.addEventListener('click', function () { store('rss-persona', 'guest'); });
    });
  }

  /* --- Header: mobile menu and current section --------------------------- */
  function initHeader() {
    var toggle = $('[data-nav-toggle]');
    var nav = $('#primary-nav');
    if (toggle && nav) {
      toggle.addEventListener('click', function () {
        var open = !nav.classList.contains('open');
        nav.classList.toggle('open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    }
    var section = document.body.getAttribute('data-section');
    if (section) {
      var item = $('.nav-item[data-section="' + section + '"]');
      if (item) item.classList.add('is-current');
    }
    $$('[data-year]').forEach(function (el) { el.textContent = String(new Date().getFullYear()); });

    /* Compact header: once the full header has scrolled out of view, a 64px
       row is fixed to the top. The shell keeps the full height in the page so
       nothing jumps; hysteresis stops it flickering at the threshold. */
    var shell = $('[data-header-shell]');
    if (!shell) return;
    var header = $('.site-header', shell);
    var compact = false, ticking = false, pin = 0;
    /* The row that stays visible is the main navigation on desktop, or the
       logo/menu row below 1200px. The header becomes fixed at exactly the
       scroll position where that row reaches the top of the window, so it is
       never out of view. */
    function measure() {
      if (compact) return;
      shell.style.minHeight = header.offsetHeight + 'px';
      var desktop = window.matchMedia('(min-width: 1201px)').matches;
      var row = desktop ? $('.primary-nav', header) : $('.main-bar', header);
      pin = row.getBoundingClientRect().top + window.pageYOffset;
    }
    function update() {
      ticking = false;
      var y = window.pageYOffset;
      var want = compact ? y > pin - 4 : y >= pin;
      if (want !== compact) {
        compact = want;
        document.body.classList.toggle('header-compact', compact);
      }
    }
    measure();
    window.addEventListener('resize', function () {
      if (compact) { compact = false; document.body.classList.remove('header-compact'); }
      measure(); update();
    });
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  /* --- Search engine shared by type-ahead and results ------------------- */
  function norm(s) { return String(s || '').toLowerCase().replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim(); }

  function levenshtein(a, b) {
    if (a === b) return 0;
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

  var vocab = null;
  function getVocab() {
    if (vocab) return vocab;
    vocab = {};
    (window.RSS_INDEX || []).forEach(function (item) {
      norm(item.title + ' ' + item.summary + ' ' + (item.kw || '')).split(' ').forEach(function (w) {
        if (w.length > 2) vocab[w] = true;
      });
    });
    return vocab;
  }

  /* Correct each word that is not in the index vocabulary to its nearest
     neighbour (typo tolerance, REQ-043). */
  function correct(words) {
    var v = getVocab();
    var changed = false;
    var out = words.map(function (w) {
      if (w.length < 4 || v[w]) return w;
      var best = null, bestD = 99;
      Object.keys(v).forEach(function (cand) {
        if (Math.abs(cand.length - w.length) > 2) return;
        var d = levenshtein(w, cand);
        if (d < bestD) { bestD = d; best = cand; }
      });
      var limit = w.length >= 7 ? 2 : 1;
      if (best && bestD <= limit) { changed = true; return best; }
      return w;
    });
    return { words: out, changed: changed };
  }

  /* Parse a query: "exact phrases", -excluded words, and plain words. */
  function parseQuery(q) {
    var phrases = [], excludes = [];
    var rest = String(q || '').replace(/"([^"]+)"/g, function (_, p) { phrases.push(norm(p)); return ' '; });
    rest = rest.replace(/(^|\s)-(\S+)/g, function (_, s, w) { excludes.push(norm(w)); return ' '; });
    var words = norm(rest).split(' ').filter(Boolean);
    return { phrases: phrases, excludes: excludes, words: words };
  }

  function expand(words) {
    var syn = window.RSS_SYNONYMS || {};
    var extra = [];
    words.forEach(function (w) { (syn[w] || []).forEach(function (s) { extra.push(s); }); });
    return extra;
  }

  function scoreItem(item, terms, synTerms, parsed) {
    var title = norm(item.title), body = norm(item.summary + ' ' + (item.kw || '') + ' ' + (item.topicLabels || []).join(' ')), doc = norm(item.doc ? item.doc.text : '');
    var all = title + ' ' + body + ' ' + doc;
    var i;
    for (i = 0; i < parsed.excludes.length; i++) if (all.indexOf(parsed.excludes[i]) !== -1) return 0;
    for (i = 0; i < parsed.phrases.length; i++) if (all.indexOf(parsed.phrases[i]) === -1) return 0;
    var score = parsed.phrases.length ? 5 : 0, matchedAll = true;
    terms.forEach(function (t) {
      var hit = false;
      if (title.indexOf(t) !== -1) { score += 6; hit = true; }
      if (body.indexOf(t) !== -1) { score += 2; hit = true; }
      if (doc.indexOf(t) !== -1) { score += 1; hit = true; }
      if (!hit) matchedAll = false;
    });
    synTerms.forEach(function (t) {
      if (title.indexOf(t) !== -1) score += 4;
      else if (body.indexOf(t) !== -1 || doc.indexOf(t) !== -1) score += 1;
    });
    if (terms.length > 1 && matchedAll) score += 4;
    if (!terms.length && !parsed.phrases.length) score = 1;
    var synTitle = synTerms.some(function (t) { return title.indexOf(t) !== -1; });
    return { score: score, strong: matchedAll || synTitle };
  }

  function search(q) {
    var parsed = parseQuery(q);
    var fixed = correct(parsed.words);
    var syn = expand(fixed.words);
    var results = [];
    (window.RSS_INDEX || []).forEach(function (item) {
      var s = scoreItem(item, fixed.words, syn, parsed);
      if (s.score > 0) results.push({ item: item, score: s.score, strong: s.strong });
    });
    /* For several words, prefer items that match all of them (or a synonym in
       the title); fall back to partial matches only when there are none. */
    if (fixed.words.length > 1 && results.some(function (r) { return r.strong; })) {
      results = results.filter(function (r) { return r.strong; });
    }
    results.sort(function (a, b) { return b.score - a.score; });
    return {
      results: results,
      corrected: fixed.changed ? fixed.words.join(' ') : null,
      synonyms: syn,
      terms: fixed.words.concat(parsed.phrases)
    };
  }

  function highlight(text, terms) {
    var out = esc(text);
    terms.filter(function (t) { return t && t.length > 1; }).forEach(function (t) {
      var re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      out = out.replace(re, '<mark>$1</mark>');
    });
    return out;
  }

  /* --- Search overlay and type-ahead ------------------------------------- */
  function initOverlay() {
    var overlay = $('#search-overlay');
    if (!overlay) return;
    var input = $('#overlay-q', overlay);
    var box = $('#typeahead', overlay);
    var helpers = $('[data-search-helpers]', overlay);
    var opener = null;

    function open(ev) {
      if (ev) ev.preventDefault();
      opener = document.activeElement;
      overlay.hidden = false;
      document.body.style.overflow = 'hidden';
      input.focus();
    }
    function close() {
      overlay.hidden = true;
      document.body.style.overflow = '';
      if (opener && opener.focus) opener.focus();
    }
    $$('[data-search-open]').forEach(function (b) { b.addEventListener('click', open); });
    $$('[data-search-close]').forEach(function (b) { b.addEventListener('click', close); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !overlay.hidden) close();
    });

    var GROUPS = [
      { label: 'Pages', types: ['Page'] },
      { label: 'Events and courses', types: ['Event', 'Course'] },
      { label: 'News', types: ['News', 'Press release', 'Member callout'] },
      { label: 'Policy documents', types: ['Policy document'] },
      { label: 'Experts and groups', types: ['Expert', 'Group'] },
      { label: 'Jobs', types: ['Job'] }
    ];

    input.addEventListener('input', function () {
      var q = input.value.trim();
      if (q.length < 2) { box.innerHTML = ''; helpers.hidden = false; return; }
      helpers.hidden = true;
      var res = search(q);
      var html = '';
      if (res.corrected) html += '<p class="wf-meta">Showing suggestions for <strong>' + esc(res.corrected) + '</strong></p>';
      GROUPS.forEach(function (g) {
        var hits = res.results.filter(function (r) { return g.types.indexOf(r.item.type) !== -1; }).slice(0, 3);
        if (!hits.length) return;
        html += '<div class="ta-group"><h2>' + g.label + '</h2><ul>';
        hits.forEach(function (r) {
          html += '<li><a href="' + pageHref(r.item.url) + '">' + highlight(r.item.title, res.terms) +
            (r.item.when ? '<span class="ta-meta">' + esc(r.item.when) + '</span>' : '') + '</a></li>';
        });
        html += '</ul></div>';
      });
      if (!res.results.length) html += '<p>No suggestions. Press Enter to search everything.</p>';
      html += '<p><a class="ta-all" href="' + pageHref('search.html') + '?q=' + encodeURIComponent(q) + '">See all ' + res.results.length + ' results for &ldquo;' + esc(q) + '&rdquo; &rarr;</a></p>';
      box.innerHTML = html;
    });

    /* Arrow keys move through suggestions */
    overlay.addEventListener('keydown', function (e) {
      if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') return;
      var links = $$('a', box);
      if (!links.length) return;
      e.preventDefault();
      var idx = links.indexOf(document.activeElement);
      idx = e.key === 'ArrowDown' ? Math.min(idx + 1, links.length - 1) : idx - 1;
      if (idx < 0) input.focus(); else links[idx].focus();
    });
  }

  /* --- Search results page (REQ-037 to REQ-046) -------------------------- */
  var FACETS = [
    { key: 'type', label: 'Content type', get: function (it) { return [it.type]; } },
    { key: 'topic', label: 'Topic', get: function (it) { return it.topicLabels || []; } },
    { key: 'audience', label: 'Audience', get: function (it) { return it.audLabels || []; } },
    { key: 'date', label: 'Date', get: function (it) { return [dateBand(it)]; } },
    { key: 'access', label: 'Access', get: function (it) { return [it.access === 'members' ? 'Members only' : 'Public']; } }
  ];
  function dateBand(it) {
    if (!it.date) return 'Undated';
    if (it.date >= TODAY) return 'Upcoming';
    var d = new Date(it.date), t = new Date(TODAY);
    var days = (t - d) / 864e5;
    if (days <= 31) return 'Past month';
    if (days <= 365) return 'Past year';
    return 'Older';
  }

  function initResults() {
    var root = $('[data-search-results]');
    if (!root) return;
    var form = $('[data-results-form]');
    var input = $('#results-q');
    var state = { q: '', sel: {}, sort: 'relevance', per: 10, page: 1 };

    function readUrl() {
      var p = params();
      state.q = p.get('q') || '';
      state.sort = p.get('sort') || 'relevance';
      state.per = parseInt(p.get('per'), 10) || 10;
      state.page = parseInt(p.get('page'), 10) || 1;
      state.sel = {};
      FACETS.forEach(function (f) {
        var v = p.getAll(f.key);
        if (v.length) state.sel[f.key] = v;
      });
      /* Advanced search: date range */
      state.from = p.get('from') || '';
      state.to = p.get('to') || '';
      input.value = state.q;
    }
    function writeUrl() {
      var p = new URLSearchParams();
      if (state.q) p.set('q', state.q);
      Object.keys(state.sel).forEach(function (k) { state.sel[k].forEach(function (v) { p.append(k, v); }); });
      if (state.sort !== 'relevance') p.set('sort', state.sort);
      if (state.per !== 10) p.set('per', String(state.per));
      if (state.page > 1) p.set('page', String(state.page));
      if (state.from) p.set('from', state.from);
      if (state.to) p.set('to', state.to);
      window.history.replaceState(null, '', '?' + p.toString());
    }

    function passes(item, exceptKey) {
      for (var i = 0; i < FACETS.length; i++) {
        var f = FACETS[i];
        if (f.key === exceptKey || !state.sel[f.key]) continue;
        var vals = f.get(item);
        var ok = state.sel[f.key].some(function (v) { return vals.indexOf(v) !== -1; });
        if (!ok) return false;
      }
      if (state.from && (!item.date || item.date < state.from)) return false;
      if (state.to && (!item.date || item.date > state.to)) return false;
      return true;
    }

    function render() {
      var res = state.q ? search(state.q) : { results: [], terms: [], synonyms: [], corrected: null };
      var base = res.results;
      var shown = base.filter(function (r) { return passes(r.item); });

      if (state.sort === 'newest' || state.sort === 'oldest') {
        shown.sort(function (a, b) {
          var x = a.item.date || '0000', y = b.item.date || '0000';
          return state.sort === 'newest' ? (x < y ? 1 : -1) : (x > y ? 1 : -1);
        });
      } else if (state.sort === 'type') {
        shown.sort(function (a, b) { return a.item.type.localeCompare(b.item.type) || b.score - a.score; });
      } else if (state.sort === 'title') {
        shown.sort(function (a, b) { return a.item.title.localeCompare(b.item.title); });
      }

      /* Facets: counts reflect every other active filter. Hide a group with
         one option or none, unless it is in use. */
      var facetsHtml = '';
      FACETS.forEach(function (f) {
        var counts = {};
        base.forEach(function (r) {
          if (!passes(r.item, f.key)) return;
          f.get(r.item).forEach(function (v) { counts[v] = (counts[v] || 0) + 1; });
        });
        var keys = Object.keys(counts).sort();
        var inUse = !!state.sel[f.key];
        if (keys.length < 2 && !inUse) return;
        facetsHtml += '<fieldset class="facet"><legend>' + f.label + '</legend>';
        keys.forEach(function (v) {
          var checked = inUse && state.sel[f.key].indexOf(v) !== -1;
          facetsHtml += '<label class="check"><input type="checkbox" data-facet="' + f.key + '" value="' + esc(v) + '"' + (checked ? ' checked' : '') + '> ' + esc(v) + '<span class="facet-count">' + counts[v] + '</span></label>';
        });
        facetsHtml += '</fieldset>';
      });
      $('[data-facet-host]').innerHTML = facetsHtml || '<p class="wf-meta">No filters for these results.</p>';

      /* Active filter chips */
      var chips = '';
      Object.keys(state.sel).forEach(function (k) {
        state.sel[k].forEach(function (v) {
          chips += '<button type="button" class="chip" data-remove="' + k + '" data-value="' + esc(v) + '">' + esc(v) + ' &times;</button>';
        });
      });
      if (state.from || state.to) chips += '<button type="button" class="chip" data-remove="range">' + esc((state.from || '…') + ' to ' + (state.to || '…')) + ' &times;</button>';
      if (chips) chips += '<button type="button" class="btn-link" data-clear>Clear all</button>';
      $('[data-active-filters]').innerHTML = chips;

      /* Notices: spelling and synonyms */
      var notice = '';
      if (res.corrected) notice += '<p class="search-notice">Showing results for <strong>' + esc(res.corrected) + '</strong>. Search instead for <a href="?q=' + encodeURIComponent('"' + state.q + '"') + '">' + esc(state.q) + '</a>.</p>';
      if (res.synonyms.length) notice += '<p class="search-notice">Also including results for ' + res.synonyms.map(function (s) { return '<strong>' + esc(s) + '</strong>'; }).join(', ') + '.</p>';
      $('[data-search-notices]').innerHTML = notice;

      /* AI-assisted answer (REQ-041) */
      var ai = $('[data-ai-answer]');
      if (ai) {
        if (shown.length && state.q) {
          var top = shown.slice(0, 3);
          ai.hidden = false;
          $('[data-ai-text]', ai).innerHTML = aiSummary(state.q, top);
          $('[data-ai-sources]', ai).innerHTML = top.map(function (r, i) {
            return '<li><a href="' + pageHref(r.item.url) + '">[' + (i + 1) + '] ' + esc(r.item.title) + '</a></li>';
          }).join('');
        } else {
          ai.hidden = true;
        }
      }

      var count = $('[data-result-count]');
      var list = $('[data-result-list]');
      var empty = $('[data-zero]');
      if (!state.q) {
        count.textContent = 'Enter a search term to begin.';
        list.innerHTML = '';
        empty.hidden = true;
        $('[data-pagination]').innerHTML = '';
        return;
      }
      if (!shown.length) {
        count.textContent = 'No results for "' + state.q + '"' + (Object.keys(state.sel).length ? ' with these filters' : '') + '.';
        list.innerHTML = '';
        empty.hidden = false;
        $('[data-pagination]').innerHTML = '';
        return;
      }
      empty.hidden = true;
      var pages = Math.ceil(shown.length / state.per);
      if (state.page > pages) state.page = pages;
      var start = (state.page - 1) * state.per;
      count.textContent = 'Showing ' + (start + 1) + ' to ' + Math.min(start + state.per, shown.length) + ' of ' + shown.length + ' results for "' + state.q + '"';

      list.innerHTML = shown.slice(start, start + state.per).map(function (r) {
        var it = r.item;
        var h = '<article class="result"><p class="meta-row"><span class="tag">' + esc(it.type) + '</span>' +
          (it.access === 'members' ? '<span class="tag">Members only</span>' : '') +
          (it.when ? '<span>' + esc(it.when) + '</span>' : '') + '</p>' +
          '<h3><a href="' + pageHref(it.url) + '">' + highlight(it.title, res.terms.concat(res.synonyms)) + '</a></h3>' +
          '<p>' + highlight(it.summary, res.terms.concat(res.synonyms)) + '</p>' +
          '<p class="result-path">' + esc(it.path || '') + '</p>';
        if (it.doc) {
          var docHit = res.terms.concat(res.synonyms).some(function (t) { return norm(it.doc.text).indexOf(t) !== -1; });
          if (docHit) {
            h += '<p class="result-doc"><strong>Found in ' + esc(it.doc.file) + ', page ' + it.doc.page + ':</strong> &hellip;' + highlight(it.doc.text, res.terms.concat(res.synonyms)) + '&hellip;</p>';
          }
        }
        return h + '</article>';
      }).join('');

      var pag = '';
      if (pages > 1) {
        for (var i = 1; i <= pages; i++) {
          pag += i === state.page ? '<li><span class="current" aria-current="page">' + i + '</span></li>' : '<li><a href="#" data-page="' + i + '">' + i + '</a></li>';
        }
      }
      $('[data-pagination]').innerHTML = pag;
      $('[data-sort]').value = state.sort;
      $('[data-per]').value = String(state.per);
      var adv = $('[data-advanced-link]');
      if (adv) adv.setAttribute('href', 'search-advanced.html?' + new URLSearchParams(window.location.search).toString());
    }

    function update() { writeUrl(); render(); }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      state.q = input.value.trim();
      state.page = 1;
      update();
    });
    root.addEventListener('change', function (e) {
      var t = e.target;
      if (t.hasAttribute('data-facet')) {
        var k = t.getAttribute('data-facet');
        var arr = state.sel[k] || [];
        if (t.checked) arr.push(t.value); else arr = arr.filter(function (v) { return v !== t.value; });
        if (arr.length) state.sel[k] = arr; else delete state.sel[k];
        state.page = 1;
        update();
      } else if (t.hasAttribute('data-sort')) {
        state.sort = t.value; update();
      } else if (t.hasAttribute('data-per')) {
        state.per = parseInt(t.value, 10); state.page = 1; update();
      }
    });
    root.addEventListener('click', function (e) {
      var t = e.target.closest('[data-remove], [data-clear], [data-page]');
      if (!t) return;
      e.preventDefault();
      if (t.hasAttribute('data-clear')) { state.sel = {}; state.from = ''; state.to = ''; }
      else if (t.hasAttribute('data-page')) { state.page = parseInt(t.getAttribute('data-page'), 10); window.scrollTo(0, 0); }
      else {
        var k = t.getAttribute('data-remove');
        if (k === 'range') { state.from = ''; state.to = ''; }
        else {
          state.sel[k] = (state.sel[k] || []).filter(function (v) { return v !== t.getAttribute('data-value'); });
          if (!state.sel[k].length) delete state.sel[k];
        }
      }
      if (!t.hasAttribute('data-page')) state.page = 1;
      update();
    });

    readUrl();
    render();
  }

  function aiSummary(q, top) {
    var nq = norm(q);
    if (/chartered|cstat/.test(nq)) {
      return 'Chartered Statistician (CStat) is the Society\'s highest professional award. You apply through MyRSS once you are a member, with evidence of your qualifications and at least five years of professional experience [1]. Fees for each grade are on the membership grades and fees page.';
    }
    if (/fee|price|cost|subscription/.test(nq)) {
      return 'Membership fees depend on your grade and any concession. Fellowship is the standard grade; students pay a reduced rate, and there are concessions for career breaks, retirement and new graduates [1].';
    }
    if (/conference/.test(nq)) {
      return 'RSS Conference 2027 takes place in Edinburgh from 6 to 9 September 2027. Booking is open, with member and early-bird rates [1].';
    }
    return 'The most relevant results are ' + top.map(function (r, i) { return esc(r.item.title) + ' [' + (i + 1) + ']'; }).join(', ') + '.';
  }

  /* --- Advanced search: prefilled from the search you came from ---------- */
  function initAdvanced() {
    var form = $('[data-advanced-form]');
    if (!form) return;
    var p = params();
    var q = p.get('q') || '';
    var phrase = (q.match(/"([^"]+)"/) || [])[1] || '';
    var excl = (q.match(/(^|\s)-(\S+)/g) || []).map(function (s) { return s.trim().slice(1); }).join(' ');
    var words = q.replace(/"[^"]+"/g, '').replace(/(^|\s)-\S+/g, '').trim();
    form.elements.all.value = words;
    form.elements.phrase.value = phrase;
    form.elements.none.value = excl;
    p.getAll('type').forEach(function (t) {
      $$('input[name="type"]', form).forEach(function (cb) { if (cb.value === t) cb.checked = true; });
    });
    if (p.get('topic')) form.elements.topic.value = p.get('topic');
    if (p.get('from')) form.elements.from.value = p.get('from');
    if (p.get('to')) form.elements.to.value = p.get('to');

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var parts = [];
      if (form.elements.all.value.trim()) parts.push(form.elements.all.value.trim());
      if (form.elements.phrase.value.trim()) parts.push('"' + form.elements.phrase.value.trim() + '"');
      form.elements.none.value.trim().split(/\s+/).filter(Boolean).forEach(function (w) { parts.push('-' + w); });
      var out = new URLSearchParams();
      out.set('q', parts.join(' '));
      $$('input[name="type"]:checked', form).forEach(function (cb) { out.append('type', cb.value); });
      if (form.elements.topic.value) out.append('topic', form.elements.topic.value);
      if (form.elements.from.value) out.set('from', form.elements.from.value);
      if (form.elements.to.value) out.set('to', form.elements.to.value);
      window.location.href = 'search.html?' + out.toString();
    });
    var reset = $('[data-advanced-reset]', form);
    if (reset) reset.addEventListener('click', function () { form.reset(); });
  }

  /* --- Listing filters: events finder, news, policy, jobs, groups -------- */
  function initListings() {
    $$('[data-listing]').forEach(function (listing) {
      var items = $$('[data-item]', listing);
      var controls = $$('[data-filter]', listing);
      var countEl = $('[data-count]', listing);
      var emptyEl = $('[data-empty]', listing);
      var chipsEl = $('[data-chips]', listing);
      var moreBtn = $('[data-more]', listing);
      var sortEl = $('[data-list-sort]', listing);
      var pageSize = parseInt(listing.getAttribute('data-page-size'), 10) || 0;
      var limit = pageSize;
      var host = items.length ? items[0].parentElement : null;
      var p = params();

      /* Pre-filtered views from the URL, e.g. events.html?type=course */
      controls.forEach(function (c) {
        var key = c.getAttribute('data-filter');
        var vals = p.getAll(key);
        if (!vals.length) return;
        if (c.type === 'checkbox' || c.type === 'radio') c.checked = vals.indexOf(c.value) !== -1;
        else c.value = vals[0];
      });

      function selected() {
        var sel = {};
        controls.forEach(function (c) {
          var key = c.getAttribute('data-filter');
          if ((c.type === 'checkbox' || c.type === 'radio')) {
            if (c.checked && c.value) (sel[key] = sel[key] || []).push(c.value);
          } else if (c.value) {
            (sel[key] = sel[key] || []).push(c.value);
          }
        });
        return sel;
      }

      function matches(item, sel) {
        return Object.keys(sel).every(function (key) {
          var vals = sel[key];
          if (key === 'q') return norm(item.getAttribute('data-text') || item.textContent).indexOf(norm(vals[0])) !== -1;
          if (key === 'when') {
            var d = item.getAttribute('data-date') || '', e = item.getAttribute('data-end') || d;
            return vals.some(function (v) {
              if (v === 'upcoming') return e >= TODAY;
              if (v === 'past') return e < TODAY;
              if (v === 'month') return d >= TODAY && d <= '2026-11-30';
              if (v === 'quarter') return d >= TODAY && d <= '2027-01-31';
              return true;
            });
          }
          var have = (item.getAttribute('data-' + key) || '').split(/\s+/);
          return vals.some(function (v) { return have.indexOf(v) !== -1; });
        });
      }

      function labelFor(key, val) {
        var c = controls.filter(function (x) { return x.getAttribute('data-filter') === key; })[0];
        if (!c) return val;
        if (c.tagName === 'SELECT') {
          var o = $$('option', c).filter(function (x) { return x.value === val; })[0];
          return o ? o.textContent : val;
        }
        var lab = c.closest('label');
        var match = controls.filter(function (x) { return x.getAttribute('data-filter') === key && x.value === val; })[0];
        lab = match ? match.closest('label') : lab;
        return lab ? lab.textContent.trim() : val;
      }

      function apply() {
        var sel = selected();
        if (sortEl && host) {
          var how = sortEl.value;
          items.slice().sort(function (a, b) {
            if (how === 'title') return a.getAttribute('data-title').localeCompare(b.getAttribute('data-title'));
            var x = a.getAttribute('data-date') || '', y = b.getAttribute('data-date') || '';
            return how === 'oldest' || how === 'soonest' ? (x > y ? 1 : -1) : (x < y ? 1 : -1);
          }).forEach(function (it) { host.appendChild(it); });
          items = $$('[data-item]', listing);
        }
        var n = 0, visible = 0;
        items.forEach(function (it) {
          var ok = matches(it, sel);
          if (ok) n += 1;
          var show = ok && (!limit || n <= limit);
          it.hidden = !show;
          it.classList.toggle('is-match', ok);
          if (show) visible += 1;
        });
        if (countEl) countEl.textContent = n + (n === 1 ? ' result' : ' results');
        if (emptyEl) emptyEl.hidden = n !== 0;
        if (moreBtn) moreBtn.hidden = !limit || n <= limit;
        if (chipsEl) {
          var html = '';
          Object.keys(sel).forEach(function (k) {
            sel[k].forEach(function (v) {
              var text = k === 'q' ? '"' + v + '"' : labelFor(k, v);
              html += '<button type="button" class="chip" data-unset="' + k + '" data-value="' + esc(v) + '">' + esc(text) + ' &times;</button>';
            });
          });
          if (html) html += '<button type="button" class="btn-link" data-unset-all>Clear all</button>';
          chipsEl.innerHTML = html;
        }
        listing.dispatchEvent(new CustomEvent('listing:updated'));
      }

      listing.addEventListener('change', function (e) {
        if (e.target.hasAttribute('data-filter') || e.target.hasAttribute('data-list-sort')) { limit = pageSize; apply(); }
      });
      listing.addEventListener('input', function (e) {
        if (e.target.getAttribute('data-filter') === 'q') { limit = pageSize; apply(); }
      });
      listing.addEventListener('submit', function (e) { e.preventDefault(); apply(); });
      listing.addEventListener('click', function (e) {
        var t = e.target.closest('[data-unset], [data-unset-all], [data-more]');
        if (!t) return;
        if (t.hasAttribute('data-more')) { limit += pageSize; apply(); return; }
        controls.forEach(function (c) {
          var key = c.getAttribute('data-filter');
          if (t.hasAttribute('data-unset-all') || (key === t.getAttribute('data-unset') && (c.value === t.getAttribute('data-value') || c.tagName === 'SELECT' || c.type === 'search' || c.type === 'text'))) {
            if (c.type === 'checkbox' || c.type === 'radio') c.checked = false;
            else c.value = '';
          }
        });
        apply();
      });
      apply();
    });
  }

  /* --- Events calendar view (REQ-210, REQ-212) --------------------------- */
  function initCalendar() {
    $$('[data-calendar]').forEach(function (cal) {
      var listing = cal.closest('[data-listing]');
      var listView = $('[data-list-view]', listing);
      var grid = $('[data-cal-grid]', cal);
      var label = $('[data-cal-label]', cal);
      var month = new Date(2026, 10, 1); /* November 2026 */
      var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

      function iso(d) { return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }

      function draw() {
        label.textContent = MONTHS[month.getMonth()] + ' ' + month.getFullYear();
        var items = $$('[data-item].is-match', listing);
        var first = new Date(month.getFullYear(), month.getMonth(), 1);
        var offset = (first.getDay() + 6) % 7; /* Monday first */
        var start = new Date(first); start.setDate(1 - offset);
        var html = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map(function (d) { return '<div class="dow">' + d + '</div>'; }).join('');
        for (var i = 0; i < 42; i++) {
          var day = new Date(start); day.setDate(start.getDate() + i);
          var key = iso(day);
          var inMonth = day.getMonth() === month.getMonth();
          var cell = '<div class="' + (inMonth ? '' : 'other') + '"><span>' + day.getDate() + '</span>';
          items.forEach(function (it) {
            var s = it.getAttribute('data-date'), e = it.getAttribute('data-end') || s;
            if (key >= s && key <= e) {
              var a = $('h3 a', it);
              cell += '<a class="cal-item ' + it.getAttribute('data-kind') + '" href="' + a.getAttribute('href') + '" title="' + esc(it.getAttribute('data-snapshot') || '') + '">' + esc(it.getAttribute('data-short') || a.textContent) + '</a>';
            }
          });
          html += cell + '</div>';
        }
        grid.innerHTML = html;
      }

      $$('[data-cal-step]', cal).forEach(function (b) {
        b.addEventListener('click', function () {
          month.setMonth(month.getMonth() + parseInt(b.getAttribute('data-cal-step'), 10));
          draw();
        });
      });
      $$('[data-view]', listing).forEach(function (b) {
        b.addEventListener('click', function () {
          var showCal = b.getAttribute('data-view') === 'calendar';
          cal.hidden = !showCal;
          listView.hidden = showCal;
          $$('[data-view]', listing).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
          if (showCal) draw();
        });
      });
      listing.addEventListener('listing:updated', function () { if (!cal.hidden) draw(); });
    });
  }

  /* --- Tabs opened from the URL, e.g. groups.html?tab=local --------------- */
  function initTabFromUrl() {
    var key = params().get('tab');
    if (!key) return;
    var tab = $('.tab[data-tab-key="' + key + '"]');
    if (tab) tab.click();
  }

  /* --- Forms: validation, reveals, multi-step, totals (REQ-050, REQ-082) - */
  function fieldLabel(input) {
    var f = input.closest('.field');
    var l = f ? $('label, legend', f) : null;
    return l ? l.textContent.replace('(optional)', '').trim() : (input.name || 'This field');
  }

  function validate(scope) {
    var errors = [];
    $$('.field', scope).forEach(function (f) {
      f.classList.remove('has-error');
      var msg = $('.field-error', f);
      if (msg) msg.remove();
    });
    var seenGroups = {};
    $$('input, select, textarea', scope).forEach(function (input) {
      if (!input.required || input.disabled || input.closest('[hidden]')) return;
      var bad = false;
      if (input.type === 'checkbox') bad = !input.checked;
      else if (input.type === 'radio') {
        if (seenGroups[input.name]) return;
        seenGroups[input.name] = true;
        bad = !$$('input[name="' + input.name + '"]', scope).some(function (r) { return r.checked; });
      } else if (!input.value.trim()) bad = true;
      else if (input.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(input.value)) bad = true;
      if (!bad) return;
      var f = input.closest('.field');
      var text = input.getAttribute('data-error') || ('Enter ' + fieldLabel(input).toLowerCase());
      if (f) {
        f.classList.add('has-error');
        var p = document.createElement('p');
        p.className = 'field-error';
        p.textContent = text;
        f.appendChild(p);
      }
      if (!input.id) input.id = 'f-' + Math.random().toString(36).slice(2, 8);
      errors.push({ id: input.id, text: text });
    });
    var summary = $('.error-summary', scope);
    if (summary) summary.remove();
    if (errors.length) {
      summary = document.createElement('div');
      summary.className = 'error-summary';
      summary.setAttribute('role', 'alert');
      summary.setAttribute('tabindex', '-1');
      summary.innerHTML = '<h2>There is a problem</h2><ul>' + errors.map(function (e) {
        return '<li><a href="#' + e.id + '">' + esc(e.text) + '</a></li>';
      }).join('') + '</ul>';
      scope.insertBefore(summary, scope.firstChild);
      summary.focus();
    }
    return !errors.length;
  }

  function updateReveals(form) {
    $$('[data-reveal]', form).forEach(function (ctrl) {
      var target = document.getElementById(ctrl.getAttribute('data-reveal'));
      if (!target) return;
      var want = ctrl.getAttribute('data-reveal-value');
      var show;
      if (ctrl.tagName === 'SELECT') show = want ? ctrl.value === want : !!ctrl.value;
      else show = ctrl.checked;
      if (ctrl.type === 'radio') {
        var anyOpener = $$('input[name="' + ctrl.name + '"][data-reveal="' + ctrl.getAttribute('data-reveal') + '"]', form).some(function (r) { return r.checked; });
        show = anyOpener;
      }
      target.hidden = !show;
    });
  }

  function updateTotals(form) {
    var total = 0;
    $$('input[data-price]', form).forEach(function (el) {
      if (el.checked) total += parseFloat(el.getAttribute('data-price')) || 0;
    });
    $$('select', form).forEach(function (s) {
      var o = s.options[s.selectedIndex];
      if (o && o.hasAttribute('data-price')) total += parseFloat(o.getAttribute('data-price')) || 0;
    });
    /* The running total may sit beside the form (e.g. a summary panel) */
    var scope = form.closest('.split') || form;
    total = Math.max(total, 0);
    $$('[data-total]', scope).forEach(function (el) { el.textContent = money(total); });
    return total;
  }
  function money(n) { return '£' + Number(n).toFixed(2).replace(/\.00$/, ''); }

  /* --- Payment (REQ-084, REQ-086, REQ-089) ------------------------------
     A form with data-pay-for hands over to the payment provider's hosted
     page (pay.html) with what is being paid for, the amount and the method.
     The hosted page returns to payment-complete.html. Invoice skips payment. */
  function goToPayment(form) {
    var amount = form.hasAttribute('data-pay-amount') ? parseFloat(form.getAttribute('data-pay-amount')) : updateTotals(form);
    var method = 'card';
    var pay = $('input[name="pay"]:checked', form);
    if (pay) method = pay.value;
    var freq = $('input[name="freq"]:checked', form);
    if (freq && freq.value === 'monthly') method = 'dd';
    var other = form.elements.other;
    if (other && !other.closest('[hidden]')) amount += parseFloat(other.value) || 0;
    var desc = form.getAttribute('data-pay-desc') || 'Payment';
    var grade = $('input[name="grade"]:checked', form);
    if (grade) desc += ': ' + optionText(grade.closest('label'));
    var p = new URLSearchParams({ for: form.getAttribute('data-pay-for'), amount: amount.toFixed(2), desc: desc, method: method });
    window.location.href = (method === 'invoice' ? 'payment-complete.html?' : 'pay.html?') + p.toString();
  }

  /* "Check your answers": one block per earlier step, each with a Change link.
     Steps themselves are hidden at this point, so only conditional sections
     that are switched off (.reveal[hidden]) are left out. */
  function optionText(label) {
    var strong = $('strong', label);
    return (strong ? strong.textContent : label.textContent).trim();
  }
  function buildSummary(form) {
    var steps = $$('.form-step', form);
    $$('[data-summary]', form).forEach(function (host) {
      var html = '';
      steps.forEach(function (step, i) {
        if (step.hasAttribute('data-review')) return;
        var rows = '', done = {};
        $$('input, select, textarea', step).forEach(function (input) {
          if (!input.name || done[input.name] || input.type === 'hidden' || input.type === 'file') return;
          var rev = input.closest('.reveal');
          if (rev && rev.hidden) return;
          done[input.name] = true;
          var value;
          if (input.type === 'radio') {
            var r = $$('input[name="' + input.name + '"]:checked', step)[0];
            value = r ? optionText(r.closest('label')) : '';
          } else if (input.type === 'checkbox') {
            value = $$('input[name="' + input.name + '"]:checked', step).map(function (b) { return optionText(b.closest('label')); }).join(', ');
          } else if (input.tagName === 'SELECT') {
            var opt = input.options[input.selectedIndex];
            value = opt && !/^(choose|any )/i.test(opt.textContent) ? opt.textContent : '';
          } else {
            value = input.type === 'password' ? (input.value ? 'Set (hidden)' : '') : input.value.trim();
          }
          rows += '<dt>' + esc(fieldLabel(input)) + '</dt><dd>' + (value ? esc(value) : '<span class="wf-meta">Not given</span>') + '</dd>';
        });
        if (!rows) return;
        var h = $('h2', step);
        html += '<div class="summary-block"><div class="summary-block-head"><h3>' + esc(h ? h.textContent : 'Step ' + (i + 1)) + '</h3>' +
          '<button class="btn-link" type="button" data-goto="' + i + '">Change<span class="visually-hidden"> ' + esc(h ? h.textContent : '') + '</span></button></div>' +
          '<dl class="summary-list">' + rows + '</dl></div>';
      });
      host.innerHTML = html;
    });
  }

  function initForms() {
    $$('form').forEach(function (form) {
      form.addEventListener('change', function () { updateReveals(form); updateTotals(form); });
      updateReveals(form);
      updateTotals(form);
    });

    $$('form[data-validate]').forEach(function (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!validate(form)) return;
        if (form.hasAttribute('data-pay-for')) { goToPayment(form); return; }
        var ok = $('.form-success', form);
        if (ok) { ok.hidden = false; ok.setAttribute('tabindex', '-1'); ok.focus(); }
        $$('button[type="submit"]', form).forEach(function (b) { b.disabled = true; });
      });
    });

    $$('form[data-steps]').forEach(function (form) {
      var steps = $$('.form-step', form);
      var marks = $$('.steps li', form.closest('main') || document);
      var idx = 0;
      function show(i) {
        idx = i;
        steps.forEach(function (s, n) { s.hidden = n !== i; });
        marks.forEach(function (m, n) {
          m.classList.toggle('done', n < i);
          m.classList.toggle('current', n === i);
          if (n === i) m.setAttribute('aria-current', 'step'); else m.removeAttribute('aria-current');
        });
        if (steps[i].hasAttribute('data-review')) buildSummary(form);
        var h = $('h2', steps[i]);
        if (h) { h.setAttribute('tabindex', '-1'); h.focus(); }
      }
      form.addEventListener('click', function (e) {
        var next = e.target.closest('[data-next]'), back = e.target.closest('[data-back]'), go = e.target.closest('[data-goto]');
        if (next) {
          e.preventDefault();
          if (validate(steps[idx])) show(Math.min(idx + 1, steps.length - 1));
        } else if (back) {
          e.preventDefault();
          show(Math.max(idx - 1, 0));
        } else if (go) {
          e.preventDefault();
          show(parseInt(go.getAttribute('data-goto'), 10));
        }
      });
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!validate(steps[idx])) return;
        if (form.hasAttribute('data-pay-for')) { goToPayment(form); return; }
        var done = $('[data-complete]', form);
        steps.forEach(function (s) { s.hidden = true; });
        marks.forEach(function (m) { m.classList.add('done'); m.classList.remove('current'); });
        if (done) { done.hidden = false; done.setAttribute('tabindex', '-1'); done.focus(); }
      });
      show(0);
    });
  }

  /* --- Basket (REQ-094) -------------------------------------------------- */
  function basket(items) {
    if (items === undefined) {
      try { return JSON.parse(store('rss-basket') || '[]'); } catch (e) { return []; }
    }
    store('rss-basket', JSON.stringify(items));
    return items;
  }
  function refreshBasketCount() {
    var n = basket().length;
    $$('[data-basket-count]').forEach(function (el) { el.textContent = String(n); });
  }
  function initBasket() {
    refreshBasketCount();
    $$('[data-add-basket]').forEach(function (b) {
      b.addEventListener('click', function (e) {
        e.preventDefault();
        var parts = b.getAttribute('data-add-basket').split('|');
        var items = basket();
        items.push({ title: parts[0], detail: parts[1] || '', price: parseFloat(parts[2]) || 0 });
        basket(items);
        refreshBasketCount();
        var msg = b.parentElement.querySelector('[data-added]');
        if (msg) msg.hidden = false;
      });
    });
    var host = $('[data-basket-list]');
    if (!host) return;
    function draw() {
      var items = basket();
      var discount = store('rss-promo') === 'MEMBER10' ? 0.1 : 0;
      if (!items.length) {
        host.innerHTML = '<p class="empty-state">Your basket is empty. <a href="events.html">Find an event or course</a>.</p>';
        $$('[data-basket-total]').forEach(function (el) { el.textContent = '£0'; });
        return;
      }
      var sub = 0;
      host.innerHTML = '<table class="data-table"><thead><tr><th scope="col">Item</th><th scope="col">Price</th><th scope="col"><span class="visually-hidden">Remove</span></th></tr></thead><tbody>' +
        items.map(function (it, i) {
          sub += it.price;
          return '<tr><td><strong>' + esc(it.title) + '</strong><br><span class="wf-meta">' + esc(it.detail) + '</span></td><td>£' + it.price.toFixed(2) + '</td><td><button class="btn-link" type="button" data-remove-item="' + i + '">Remove</button></td></tr>';
        }).join('') + '</tbody></table>';
      var vat = 0; /* training is VAT-exempt in this example; shown for structure */
      var total = sub * (1 - discount) + vat;
      $$('[data-basket-sub]').forEach(function (el) { el.textContent = '£' + sub.toFixed(2); });
      $$('[data-basket-discount]').forEach(function (el) { el.textContent = discount ? '−£' + (sub * discount).toFixed(2) : '£0.00'; });
      $$('[data-basket-total]').forEach(function (el) { el.textContent = '£' + total.toFixed(2); });
    }
    host.addEventListener('click', function (e) {
      var b = e.target.closest('[data-remove-item]');
      if (!b) return;
      var items = basket();
      items.splice(parseInt(b.getAttribute('data-remove-item'), 10), 1);
      basket(items);
      refreshBasketCount();
      draw();
    });
    $$('[data-checkout]').forEach(function (b) {
      b.addEventListener('click', function (e) {
        e.preventDefault();
        var items = basket();
        if (!items.length) return;
        var sub = items.reduce(function (s, it) { return s + it.price; }, 0);
        var total = sub * (store('rss-promo') === 'MEMBER10' ? 0.9 : 1);
        var desc = items.length === 1 ? items[0].title : items.length + ' items: ' + items.map(function (it) { return it.title; }).join(', ');
        window.location.href = 'pay.html?' + new URLSearchParams({ for: 'basket', amount: total.toFixed(2), desc: desc, method: 'card' }).toString();
      });
    });
    var promo = $('[data-promo-form]');
    if (promo) {
      promo.addEventListener('submit', function (e) {
        e.preventDefault();
        var code = promo.elements.code.value.trim().toUpperCase();
        var out = $('[data-promo-msg]', promo);
        if (code === 'MEMBER10') { store('rss-promo', code); out.textContent = 'Code MEMBER10 applied: 10% off.'; }
        else { out.textContent = 'That code is not valid. Check the spelling, or that it has not expired.'; }
        draw();
      });
    }
    draw();
  }

  /* --- Hosted payment page (pay.html) ---------------------------------- */
  function initPayPage() {
    var root = $('[data-pay-page]');
    if (!root) return;
    var p = params();
    var amount = parseFloat(p.get('amount') || '0');
    var method = p.get('method') || 'card';
    $$('[data-pay-desc]').forEach(function (el) { el.textContent = p.get('desc') || 'Payment to the Royal Statistical Society'; });
    $$('[data-pay-amount]').forEach(function (el) { el.textContent = money(amount); });
    $$('[data-pay-back]').forEach(function (a) { a.setAttribute('href', document.referrer || 'home.html'); });

    var tab = $('.tab[data-tab-key="' + (method === 'dd' ? 'dd' : 'card') + '"]', root);
    if (tab) tab.click();
    /* Direct Debit only where the item allows it */
    if (!/^(join|renewal|donation)$/.test(p.get('for') || '')) {
      var ddTab = $('.tab[data-tab-key="dd"]', root);
      if (ddTab) ddTab.hidden = true;
    }

    function finish(m) {
      var out = new URLSearchParams(p.toString());
      out.set('method', m);
      out.set('ref', 'RSS-' + String(Math.floor(100000 + Math.random() * 900000)));
      window.location.href = 'payment-complete.html?' + out.toString();
    }

    var card = $('[data-card-form]', root);
    var threeDs = $('#three-ds');
    card.addEventListener('submit', function (e) {
      e.preventDefault();
      var declined = $('[data-declined]', root);
      declined.hidden = true;
      if (!validate(card)) return;
      var digits = card.elements.cardnumber.value.replace(/\D/g, '');
      if (/0002$/.test(digits)) {
        declined.hidden = false;
        declined.setAttribute('tabindex', '-1');
        declined.focus();
        return;
      }
      threeDs.classList.add('open');
      $('.wf-modal-panel', threeDs).focus();
    });
    $('[data-3ds-approve]').addEventListener('click', function () { finish('card'); });

    var dd = $('[data-dd-form]', root);
    dd.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate(dd)) return;
      finish('dd');
    });
  }

  /* --- Payment confirmation (payment-complete.html) ---------------------- */
  function initPaymentComplete() {
    var root = $('[data-pay-complete]');
    if (!root) return;
    var p = params();
    var what = p.get('for') || 'basket';
    var method = p.get('method') || 'card';
    var labels = { card: 'Card', dd: 'Direct Debit', invoice: 'Invoice' };
    $$('[data-pay-desc]').forEach(function (el) { el.textContent = p.get('desc') || ''; });
    $$('[data-pay-amount]').forEach(function (el) { el.textContent = money(parseFloat(p.get('amount') || '0')); });
    $$('[data-pay-ref]').forEach(function (el) { el.textContent = p.get('ref') || 'RSS-INV-204517'; });
    $$('[data-pay-method]').forEach(function (el) { el.textContent = labels[method] || method; });
    $$('[data-pay-for-block]').forEach(function (el) {
      el.hidden = el.getAttribute('data-pay-for-block').split(/\s+/).indexOf(what) === -1;
    });
    $$('[data-pay-method-block]').forEach(function (el) {
      el.hidden = el.getAttribute('data-pay-method-block').split(/\s+/).indexOf(method) === -1;
    });
    if (what === 'basket') { basket([]); store('rss-promo', ''); refreshBasketCount(); }
    /* In the prototype, joining or renewing makes you a member */
    if (what === 'join' || what === 'renewal') applyPersona((store('rss-persona', 'member'), 'member'));
  }

  /* --- Cookie banner (REQ-248) ------------------------------------------ */
  function initCookies() {
    var banner = $('[data-cookie-banner]');
    if (!banner) return;
    if (!store('rss-cookie')) banner.hidden = false;
    $$('[data-cookie]').forEach(function (b) {
      b.addEventListener('click', function () {
        store('rss-cookie', b.getAttribute('data-cookie'));
        banner.hidden = true;
        var modal = $('#cookie-modal');
        if (modal) modal.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
    $$('[data-cookie-settings]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var modal = $('#cookie-modal');
        if (modal) { modal.classList.add('open'); $('.wf-modal-panel', modal).focus(); }
      });
    });
  }

  /* --- Small things ------------------------------------------------------ */
  function initMisc() {
    /* Filters drawer on small screens (search results and finders) */
    $$('[data-facets-toggle]').forEach(function (t) {
      t.addEventListener('click', function () {
        var host = t.closest('[data-listing], [data-search-results]');
        var f = host ? $('.facets', host) : null;
        if (!f) return;
        var open = !f.classList.contains('open');
        f.classList.toggle('open', open);
        t.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    });
    $$('[data-copy-link]').forEach(function (b) {
      b.addEventListener('click', function () {
        var url = window.location.href.split('#')[0] + (b.getAttribute('data-copy-link') || '');
        if (navigator.clipboard) navigator.clipboard.writeText(url);
        b.textContent = 'Link copied';
      });
    });
    $$('[data-dismiss]').forEach(function (b) {
      b.addEventListener('click', function () {
        var t = document.getElementById(b.getAttribute('data-dismiss'));
        if (t) t.hidden = true;
      });
    });
    /* Course page: date picker updates the booking button label */
    $$('[data-date-choice]').forEach(function (r) {
      r.addEventListener('change', function () {
        $$('[data-chosen-date]').forEach(function (el) { el.textContent = r.getAttribute('data-date-choice'); });
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initNotes();
    initPersona();
    initHeader();
    initOverlay();
    initResults();
    initAdvanced();
    initListings();
    initCalendar();
    initTabFromUrl();
    initForms();
    initBasket();
    initCookies();
    initPayPage();
    initPaymentComplete();
    initMisc();
  });
})();
