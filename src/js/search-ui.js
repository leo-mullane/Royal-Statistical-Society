/* ==========================================================================
   search-ui.js — everything a visitor touches in search (REQ-037 to REQ-046).
   Written directly (never generated). Depends on search-engine.js.

   1. Type-ahead: attaches to any input[data-typeahead]; data-scope narrows it.
   2. Results page (#search-app): all state lives in the URL, so Back,
      Forward, bookmarks and pasted links land on exactly the same view.
   3. Advanced search builder (#builder-app).
   4. "How search is configured" (#config-app): renders the live CONFIG.
   ========================================================================== */

(function () {
  'use strict';

  var S = window.RSSSearch;
  if (!S) return;
  var C = S.config;
  var esc = S.esc;
  var CAT_LABEL = {};
  C.categories.forEach(function (c) { CAT_LABEL[c.key] = c.label; });
  var FACET_LABEL = {};
  C.facets.forEach(function (f) { FACET_LABEL[f.key] = f.label; });

  function $(id) { return document.getElementById(id); }
  function q(s) { return '‘' + esc(s) + '’'; }
  function plural(n, one, many) { return n + ' ' + (n === 1 ? one : (many || one + 's')); }

  /* ======================================================================
     1. Type-ahead (REQ-037, REQ-043, REQ-045)
     ARIA combobox and listbox. Up/Down to move, Enter to choose, Escape to
     close. Starts at two characters; always ends with "Search … for".
     ====================================================================== */
  var uid = 0;

  function hrefFor(item, scope, form) {
    var hidden = {};
    if (form) Array.prototype.forEach.call(form.querySelectorAll('input[type="hidden"]'), function (h) { if (h.value) hidden[h.name] = h.value; });
    if (item.kind === 'topic') {
      var p = { topic: item.label };
      if (scope) p.scope = scope;
      return S.pageUrl('search.html', p);
    }
    if (item.kind === 'all') return S.pageUrl('search.html', Object.assign({}, hidden, scope ? { scope: scope } : {}, { q: item.q }));
    return S.pageUrl(item.doc.url);
  }

  function markPrefix(label, typed) {
    var nq = S.norm(typed);
    var nl = S.norm(label);
    var idx = (' ' + nl).indexOf(' ' + nq);
    /* norm() keeps length for ordinary labels, so the index maps back */
    if (idx < 0 || nl.length !== label.length) return esc(label);
    return esc(label.slice(0, idx)) + '<mark>' + esc(label.slice(idx, idx + nq.length)) + '</mark>' + esc(label.slice(idx + nq.length));
  }

  function attachTypeahead(input) {
    var form = input.closest('form');
    var wrap = input.closest('.ta-wrap') || input.parentElement;
    var listId = 'ta-list-' + (++uid);
    var list = document.createElement('ul');
    list.className = 'ta-list';
    list.id = listId;
    list.setAttribute('role', 'listbox');
    list.setAttribute('aria-label', 'Suggestions');
    list.hidden = true;
    wrap.appendChild(list);

    input.setAttribute('role', 'combobox');
    input.setAttribute('aria-autocomplete', 'list');
    input.setAttribute('aria-expanded', 'false');
    input.setAttribute('aria-controls', listId);
    input.setAttribute('autocomplete', 'off');

    var options = [];
    var active = -1;

    function close() {
      list.hidden = true;
      input.setAttribute('aria-expanded', 'false');
      input.removeAttribute('aria-activedescendant');
      active = -1;
    }
    function setActive(i) {
      options.forEach(function (o, n) { o.el.setAttribute('aria-selected', n === i ? 'true' : 'false'); });
      active = i;
      if (i >= 0) {
        input.setAttribute('aria-activedescendant', options[i].el.id);
        options[i].el.scrollIntoView({ block: 'nearest' });
      } else input.removeAttribute('aria-activedescendant');
    }
    function addOption(item, typed, scope, isAll) {
      var li = document.createElement('li');
      li.className = 'ta-option' + (isAll ? ' ta-all' : '');
      li.id = listId + '-' + options.length;
      li.setAttribute('role', 'option');
      li.setAttribute('aria-selected', 'false');
      var label = isAll ? esc(item.label) : markPrefix(item.label, typed);
      var via = item.via ? '<span class="ta-via">matches ‘' + esc(item.via) + '’</span>' : '';
      li.innerHTML = '<span class="ta-label">' + label + via + '</span><span class="ta-detail">' + esc(item.detail || '') + '</span>';
      var href = hrefFor(item, scope, form);
      li.addEventListener('mousedown', function (e) { e.preventDefault(); window.location.href = href; });
      list.appendChild(li);
      options.push({ el: li, href: href });
    }
    function place() {
      if (list.hidden) return;
      var r = input.getBoundingClientRect();
      list.style.position = 'fixed';
      list.style.left = r.left + 'px';
      list.style.width = Math.max(r.width, 280) + 'px';
      list.style.top = (r.bottom + 4) + 'px';
      list.style.maxHeight = Math.max(240, window.innerHeight - r.bottom - 16) + 'px';
    }
    function render() {
      var scope = input.getAttribute('data-scope') || '';
      var typed = input.value.trim();
      list.innerHTML = '';
      options = [];
      active = -1;
      if (S.norm(typed).length < 2) { close(); return; }
      S.suggest(typed, scope).forEach(function (g) {
        var head = document.createElement('li');
        head.className = 'ta-head';
        head.setAttribute('role', 'presentation');
        head.textContent = g.label;
        list.appendChild(head);
        g.items.forEach(function (item) { addOption(item, typed, scope); });
      });
      var where = scope ? C.scopes[scope].label.toLowerCase() : 'everything';
      addOption({ kind: 'all', q: typed, label: 'Search ' + where + ' for ‘' + typed + '’', detail: 'Enter' }, null, scope, true);
      list.hidden = false;
      place();
      input.setAttribute('aria-expanded', 'true');
    }

    input.addEventListener('input', render);
    input.addEventListener('focus', function () { if (input.value.trim()) render(); });
    input.addEventListener('blur', function () { window.setTimeout(close, 150); });
    window.addEventListener('resize', place);
    window.addEventListener('scroll', place, true);
    input.addEventListener('keydown', function (e) {
      if (list.hidden) {
        if (e.key === 'ArrowDown' && input.value.trim()) { render(); e.preventDefault(); }
        return;
      }
      if (e.key === 'ArrowDown') { e.preventDefault(); setActive((active + 1) % options.length); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(active <= 0 ? options.length - 1 : active - 1); }
      else if (e.key === 'Enter' && active >= 0) { e.preventDefault(); window.location.href = options[active].href; }
      else if (e.key === 'Escape') { e.preventDefault(); e.stopPropagation(); close(); }
    });
  }

  /* ======================================================================
     2. Results page
     ====================================================================== */
  var state, app;
  var ui = { expanded: {}, openDrop: null, panelOpen: null };

  function hasFilters(s) {
    return S.FACET_KEYS.some(function (k) { return s.filters[k] && s.filters[k].length; }) || !!s.letter;
  }
  function isBrowse(s) { return !s.q && !s.type && !hasFilters(s); }

  function commit(push) {
    var qs = new URLSearchParams(S.toParams(state)).toString();
    var url = window.location.pathname + (qs ? '?' + qs : '');
    if (push) window.history.pushState(null, '', url); else window.history.replaceState(null, '', url);
    render();
  }
  function update(fn) { fn(state); commit(true); }

  var HEADINGS = {
    '': ['Search', '', 'Search events, courses, news, policy, experts and pages'],
    events: ['Search events and training', 'Discussion meetings, section and local group events, courses and the conference.', 'Search events and courses'],
    experts: ['Find an expert', 'The Professional Register, the Consultants Directory and the Fellows Directory.', 'Name, skill or place'],
    policy: ['Search the policy library', 'Consultation responses, evidence, reports, briefings and letters.', 'Search policy documents']
  };

  function render() {
    var focusId = document.activeElement && document.activeElement.id;
    var r = S.search(state);
    var input = $('sr-q');
    if (input && document.activeElement !== input) input.value = state.q;

    renderHeading();
    renderLetters();
    renderBanners(r);
    renderTabs(r);
    renderChips();
    renderToolbar(r);

    var browse = isBrowse(state);
    $('sr-body').hidden = browse;
    $('sr-browse').hidden = !browse;
    if (browse) { $('sr-facetbar').hidden = true; renderBrowse(r); }
    else { renderFacets(r); renderResults(r); }
    renderAi(r, browse);

    if (focusId && $(focusId) && focusId !== 'sr-q') $(focusId).focus({ preventScroll: true });
  }

  /* Section searches are this page with a scope applied */
  function renderHeading() {
    var h = HEADINGS[state.scope] || HEADINGS[''];
    $('sr-title').textContent = h[0];
    $('sr-intro').textContent = h[1];
    $('sr-intro').hidden = !h[1];
    var input = $('sr-q');
    input.setAttribute('placeholder', h[2]);
    input.setAttribute('data-scope', state.scope || '');
    $('sr-scope').value = state.scope || '';
    var crumb = document.querySelector('.breadcrumb [aria-current="page"]');
    if (crumb) crumb.textContent = h[0];
    document.title = h[0] + ' | Royal Statistical Society (prototype)';
  }

  /* Surname A to Z, whenever results are limited to experts */
  function renderLetters() {
    var host = $('sr-letters');
    if (state.type !== 'experts') { host.hidden = true; host.innerHTML = ''; return; }
    var have = {};
    S.docs.forEach(function (d) { if (d.cat === 'experts') have[S.surnameLetter(d)] = true; });
    var html = '<span class="wf-meta" id="letters-label">Surname</span><span class="letter-row" role="group" aria-labelledby="letters-label">';
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach(function (L) {
      html += have[L]
        ? '<button type="button" id="letter-' + L + '" data-letter="' + L + '" aria-pressed="' + (state.letter === L) + '">' + L + '</button>'
        : '<span aria-hidden="true">' + L + '</span>';
    });
    host.innerHTML = html + '</span>';
    host.hidden = false;
  }

  function renderBanners(r) {
    var out = [];
    if (r.correctedTo) {
      out.push('<div class="banner"><!-- Spelling correction (REQ-043) -->No results for ' + q(r.correctedFrom) +
        '. Showing results for <strong>' + q(r.correctedTo) + '</strong> instead. ' +
        '<button type="button" class="btn-link" id="sr-raw" data-action="raw">Search for ' + q(r.correctedFrom) + ' exactly</button></div>');
    }
    Object.keys(r.synonyms).forEach(function (orig) {
      out.push('<div class="banner banner-muted"><!-- Synonyms (REQ-045) -->Also showing results for ' +
        r.synonyms[orig].map(q).join(', ') + (r.synonyms[orig].length === 1 ? ', which means' : ', which mean') + ' the same as ' + q(orig) + '.</div>');
    });
    if (state.scope && state.q && !r.correctedTo) {
      var inScope = r.tabCounts[state.type] || 0;
      var outside = r.total - inScope;
      out.push('<div class="banner"><!-- Section search, widenable -->You are searching ' + esc(C.scopes[state.scope].label) + ' only. ' +
        (outside > 0 ? plural(outside, 'more result') + ' elsewhere on the site. ' : 'Nothing else on the site matches. ') +
        '<button type="button" class="btn-link" id="sr-widen" data-action="widen">Search the whole site</button></div>');
    }
    $('sr-banners').innerHTML = out.join('');
  }

  function renderTabs(r) {
    var html = '<button type="button" class="cat-tab" id="tab-all" aria-pressed="' + (!state.type) + '" data-type="">All <span class="n">' + r.total + '</span></button>';
    C.categories.forEach(function (c) {
      var n = r.tabCounts[c.key];
      var on = state.type === c.key;
      html += '<button type="button" class="cat-tab" id="tab-' + c.key + '" aria-pressed="' + on + '" data-type="' + c.key + '"' +
        (!n && !on ? ' disabled' : '') + '>' + esc(c.label) + ' <span class="n">' + n + '</span></button>';
    });
    $('sr-tabs').innerHTML = html;
  }

  function renderChips() {
    var chips = [];
    if (state.scope) chips.push({ cls: 'scope', k: 'Searching', v: C.scopes[state.scope].label + ' only', act: 'widen' });
    if (state.letter) chips.push({ k: 'Surname', v: state.letter, act: 'letter' });
    S.FACET_KEYS.forEach(function (key) {
      (state.filters[key] || []).forEach(function (v) { chips.push({ k: FACET_LABEL[key], v: v, act: 'facet', key: key }); });
    });
    var html = chips.map(function (c, i) {
      return '<button type="button" class="chip ' + (c.cls || '') + '" id="chip-' + i + '" data-action="' + c.act + '"' +
        (c.key ? ' data-key="' + c.key + '" data-value="' + esc(c.v) + '"' : '') +
        ' aria-label="Remove ' + esc(c.k + ': ' + c.v) + '"><span class="chip-k">' + esc(c.k) + ':</span> ' + esc(c.v) +
        ' <span class="x" aria-hidden="true">&times;</span></button>';
    }).join('');
    if (chips.length > 1) html += '<button type="button" class="btn-link" id="chip-clear" data-action="clear">Clear all</button>';
    $('sr-chips').innerHTML = html;
    $('sr-chips').hidden = !chips.length;
  }

  function renderToolbar(r) {
    var shown = state.type ? r.tabCounts[state.type] : r.total;
    var what = state.type ? CAT_LABEL[state.type].toLowerCase() : (shown === 1 ? 'result' : 'results');
    var text;
    if (isBrowse(state)) text = 'Everything on the site, by type: ' + plural(r.total, 'item') + '.';
    else if (state.q) text = shown + ' ' + what + ' for ' + q(r.correctedTo || state.q);
    else text = 'Showing ' + shown + ' ' + what;
    $('sr-count').innerHTML = text;
    $('sr-sort').value = state.sort;
    $('sr-per').value = String(state.per);
    Array.prototype.forEach.call(document.querySelectorAll('#sr-layout button'), function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-layout') === state.layout));
    });
    $('sr-body').className = 'sr-body layout-' + state.layout;
    /* Advanced search opens on the search you are looking at */
    var ap = S.toParams(state);
    delete ap.page; delete ap.layout; delete ap.sort; delete ap.raw; delete ap.per; delete ap.scope;
    if (state.type) ap.type = state.type;
    $('sr-advanced').setAttribute('href', S.pageUrl('search-advanced.html', ap));
  }

  /* --- Facets (REQ-039) ---------------------------------------------------- */
  function facetGroup(key, values, inDrop) {
    var selected = state.filters[key] || [];
    var visible = values.filter(function (v) { return v.count > 0 || selected.indexOf(v.value) >= 0; });
    if (!visible.length) return '';
    /* A facet with one option and nothing ticked cannot narrow anything */
    if (visible.length === 1 && !selected.length) return '';
    var limit = 5;
    var expanded = ui.expanded[key];
    var sfx = inDrop ? '-d' : '';
    var html = '<fieldset class="facet" data-facet="' + key + '"><legend>' + esc(FACET_LABEL[key]) + '</legend>';
    if (visible.length > 8) {
      html += '<label class="visually-hidden" for="ff-' + key + sfx + '">Filter ' + esc(FACET_LABEL[key].toLowerCase()) + ' options</label>' +
        '<input type="search" class="facet-filter" id="ff-' + key + sfx + '" data-facet-filter="' + key + '" placeholder="Filter ' + esc(FACET_LABEL[key].toLowerCase()) + '" autocomplete="off">';
    }
    visible.forEach(function (v, i) {
      var on = selected.indexOf(v.value) >= 0;
      var hide = !expanded && i >= limit && !on;
      var id = 'f-' + key + '-' + S.slug(v.value) + sfx;
      html += '<label class="facet-opt" for="' + id + '"' + (hide ? ' data-extra hidden' : '') + ' data-v="' + esc(S.norm(v.value)) + '">' +
        '<input type="checkbox" id="' + id + '" data-key="' + key + '" value="' + esc(v.value) + '"' + (on ? ' checked' : '') + '>' +
        '<span>' + esc(v.value) + '</span><span class="n">' + v.count + '</span></label>';
    });
    if (visible.length > limit) {
      html += '<button type="button" class="btn-link" id="more-' + key + sfx + '" data-more="' + key + '">' +
        (expanded ? 'Show fewer' : 'Show all ' + visible.length) + '</button>';
    }
    return html + '</fieldset>';
  }

  function renderFacets(r) {
    var keys = C.facetsFor[state.type || ''] || [];
    var aside = $('sr-facets');
    var bar = $('sr-facetbar');
    if (state.layout === 'topbar') {
      aside.hidden = true;
      aside.innerHTML = '';
      bar.hidden = false;
      bar.innerHTML = keys.map(function (k) {
        var g = facetGroup(k, r.facets[k], true);
        if (!g) return '';
        var n = (state.filters[k] || []).length;
        return '<details class="facet-drop" data-drop="' + k + '"' + (ui.openDrop === k ? ' open' : '') + '><summary>' +
          esc(FACET_LABEL[k]) + (n ? ' (' + n + ')' : '') + '</summary><div class="facet-pop">' + g + '</div></details>';
      }).join('') || '<p class="wf-meta">No filters apply to these results.</p>';
    } else {
      bar.hidden = true;
      bar.innerHTML = '';
      aside.hidden = false;
      var groups = keys.map(function (k) { return facetGroup(k, r.facets[k], false); }).join('');
      var mobile = window.matchMedia('(max-width: 768px)').matches;
      var open = ui.panelOpen !== null ? ui.panelOpen : (!mobile || hasFilters(state));
      aside.innerHTML = '<details class="facet-panel" id="facet-panel"' + (open ? ' open' : '') + '><summary>Filter results</summary>' +
        (groups || '<p class="wf-meta">No filters apply to these results.</p>') + '</details>';
    }
  }

  /* --- Results (REQ-038, REQ-042, REQ-044) --------------------------------- */
  function resultHtml(doc, concepts, promoted) {
    var snip = S.snippet(doc, concepts);
    var expert = doc.cat === 'experts';
    var meta = doc.meta.slice(1).filter(Boolean).map(esc).join(' · ');
    var where = snip.page ? '<span class="pg">Found in ' + esc(doc.file) + ', page ' + snip.page + ':</span> “' + snip.html + '”' : snip.html;
    return '<article class="result' + (expert ? ' has-avatar' : '') + (promoted ? ' promoted' : '') + '">' +
      (expert ? '<div class="wf-placeholder avatar">Photo</div>' : '') +
      '<div><p class="result-type">' + (promoted ? 'Promoted · ' : '') + esc(doc.meta[0] || doc.typeLabel) +
      (doc.members ? ' <span class="tag">Members only</span>' : '') + '</p>' +
      '<h3><a href="' + S.pageUrl(doc.url) + '">' + S.highlight(doc.title, concepts) + '</a></h3>' +
      (meta ? '<p class="result-meta">' + meta + '</p>' : '') +
      '<p class="result-snippet">' + where + '</p></div></article>';
  }

  function renderResults(r) {
    var showBest = r.bestBet && state.page === 1 && !state.type;
    var list = showBest ? r.results.filter(function (h) { return h.doc !== r.bestBet; }) : r.results;
    var per = state.per;
    var pages = Math.max(1, Math.ceil(list.length / per));
    if (state.page > pages) state.page = pages;
    var slice = list.slice((state.page - 1) * per, state.page * per);
    var html = '';

    if (showBest) {
      html += '<!-- Promoted result, later phase (REQ-278) -->' + resultHtml(r.bestBet, r.concepts, true) +
        '<div class="wf-note query" data-note="BB"><span class="wf-note-label">Proposed</span>Promoted results ("best bets") are an editorial pin for named searches such as join, renew, fees and CStat. One example is built, for "renew". This is a Could, so it is shown for discussion, not as part of phase one. <span class="wf-req">REQ-278</span></div>';
    }
    if (!list.length) html += zeroHtml(r);
    else {
      var lastYear = null;
      slice.forEach(function (h) {
        if (state.sort === 'year') {
          var y = h.doc.date ? h.doc.date.slice(0, 4) : 'Undated';
          if (y !== lastYear) { html += '<h2 class="year-head">' + y + '</h2>'; lastYear = y; }
        }
        html += resultHtml(h.doc, r.concepts, false);
      });
    }
    $('sr-results').innerHTML = html;

    var nav = $('sr-pages');
    if (pages <= 1) { nav.innerHTML = ''; return; }
    var p = '<ul class="pagination">';
    p += '<li><button type="button" data-page="' + (state.page - 1) + '"' + (state.page === 1 ? ' disabled' : '') + '>Previous</button></li>';
    for (var i = 1; i <= pages; i++) {
      p += '<li><button type="button" data-page="' + i + '"' + (i === state.page ? ' aria-current="page"' : '') + '>' + i + '</button></li>';
    }
    p += '<li><button type="button" data-page="' + (state.page + 1) + '"' + (state.page === pages ? ' disabled' : '') + '>Next</button></li></ul>';
    nav.innerHTML = p;
  }

  /* Zero results (REQ-046): a correction, a broader search, routes, contact */
  function zeroHtml(r) {
    var tips = [];
    if (state.type && r.total) {
      return '<div class="zero"><p><strong>No ' + esc(CAT_LABEL[state.type].toLowerCase()) + ' match.</strong> ' +
        plural(r.total, 'result') + ' in other types: use the tabs above, or ' +
        '<button type="button" class="btn-link" data-action="all-types">show all types</button>.</p></div>';
    }
    if (hasFilters(state)) {
      var loose = S.search(Object.assign({}, state, { filters: {}, letter: '' }));
      if (loose.total) tips.push('<button type="button" class="btn-link" data-action="clear">Remove your filters</button> (' + plural(loose.total, 'result') + ' without them)');
    }
    if (state.raw) {
      var fixed = S.search(Object.assign({}, state, { raw: false }));
      if (fixed.correctedTo) tips.push('Did you mean <a href="?' + new URLSearchParams({ q: fixed.correctedTo }).toString() + '">' + q(fixed.correctedTo) + '</a>?');
    }
    tips.push('Check the spelling, or try a broader or different word. We match common alternatives, such as <em>CStat</em> for <em>Chartered Statistician</em>');
    tips.push('Browse <a href="' + S.pageUrl('events.html') + '">events and courses</a>, the <a href="' + S.pageUrl('policy.html') + '#library">policy library</a> or <a href="' + S.pageUrl('find-an-expert.html') + '">find an expert</a>');
    tips.push('<a href="' + S.pageUrl('about.html') + '#contact">Contact us</a>: tell us what you are looking for and we will help');
    return '<!-- Zero results (REQ-046) --><div class="zero"><h2>No results for ' + q(state.q) + '</h2><ul>' +
      tips.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul></div>';
  }

  /* --- Browse view: everything by type, before anything is typed ----------- */
  function renderBrowse(r) {
    var html = '<h2 class="section-title">Browse everything</h2><div class="browse-grid">';
    C.categories.forEach(function (c) {
      var items = r.results.filter(function (h) { return h.doc.cat === c.key; });
      if (['events', 'news', 'policy', 'jobs'].indexOf(c.key) >= 0) items.sort(function (a, b) { return (b.doc.date || '').localeCompare(a.doc.date || ''); });
      else items.sort(function (a, b) { return a.doc.title.localeCompare(b.doc.title); });
      html += '<section class="browse-card"><h3><span>' + esc(c.label) + '</span><span class="n">' + r.tabCounts[c.key] + '</span></h3><ul>' +
        items.slice(0, 4).map(function (h) { return '<li><a href="' + S.pageUrl(h.doc.url) + '">' + esc(h.doc.title) + '</a></li>'; }).join('') +
        '</ul><button type="button" class="btn btn-secondary btn-small" id="browse-' + c.key + '" data-type="' + c.key + '">Browse all ' + esc(c.label.toLowerCase()) + '</button></section>';
    });
    $('sr-browse').innerHTML = html + '</div>';
  }

  /* --- AI-assisted answer (REQ-041): never for experts --------------------- */
  function renderAi(r, browse) {
    var ai = $('sr-ai');
    if (!ai) return;
    var top = r.results.filter(function (h) { return h.doc.cat !== 'experts'; }).slice(0, 3);
    if (browse || !state.q || state.type === 'experts' || state.page > 1 || !top.length) { ai.hidden = true; return; }
    ai.hidden = false;
    $('sr-ai-text').innerHTML = aiSummary(r.correctedTo || state.q, top);
    $('sr-ai-sources').innerHTML = top.map(function (h, i) {
      return '<li><a href="' + S.pageUrl(h.doc.url) + '">[' + (i + 1) + '] ' + esc(h.doc.title) + '</a></li>';
    }).join('');
  }
  function aiSummary(query, top) {
    var nq = S.norm(query);
    if (/chartered|cstat/.test(nq)) {
      return 'Chartered Statistician (CStat) is the Society\'s highest professional award. You apply through MyRSS once you are a member, with evidence of your qualifications and at least five years of professional experience [1]. Fees for each grade are on the membership grades and fees page.';
    }
    if (/fee|price|cost|subscription/.test(nq)) {
      return 'Membership fees depend on your grade and any concession. Fellowship is the standard grade; students pay a reduced rate, and there are concessions for career breaks, retirement and new graduates [1].';
    }
    if (/conference/.test(nq)) {
      return 'RSS Conference 2027 takes place in Edinburgh from 6 to 9 September 2027. Booking is open, with member and early-bird rates [1].';
    }
    return 'The most relevant results are ' + top.map(function (h, i) { return esc(h.doc.title) + ' [' + (i + 1) + ']'; }).join(', ') + '.';
  }

  function copyLink() {
    var msg = $('sr-copied');
    var done = function () {
      msg.textContent = 'Link copied. Anyone who opens it sees this search, with these filters, kept up to date.';
      window.setTimeout(function () { msg.textContent = ''; }, 5000);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(window.location.href).then(done, function () { msg.textContent = window.location.href; });
    } else msg.textContent = window.location.href;
  }

  function bindResults() {
    $('sr-form').addEventListener('submit', function (e) {
      e.preventDefault();
      var v = $('sr-q').value.trim();
      update(function (s) { s.q = v; s.page = 1; s.raw = false; s.letter = ''; if (!s.scope) s.type = ''; });
    });

    app.addEventListener('click', function (e) {
      var t = e.target.closest('button');
      if (!t || !app.contains(t) || t.closest('.ta-list')) return;
      var act = t.getAttribute('data-action');
      if (t.hasAttribute('data-letter')) {
        var L = t.getAttribute('data-letter');
        update(function (s) { s.letter = s.letter === L ? '' : L; s.page = 1; });
      } else if (t.hasAttribute('data-type')) {
        var type = t.getAttribute('data-type');
        update(function (s) {
          s.type = type; s.page = 1;
          if (s.scope && C.scopes[s.scope].type !== type) s.scope = '';
          if (type !== 'experts') s.letter = '';
          /* Facets that do not apply to the new tab are dropped */
          var keep = C.facetsFor[type || ''] || [];
          S.FACET_KEYS.forEach(function (k) { if (keep.indexOf(k) < 0) s.filters[k] = []; });
        });
      } else if (t.hasAttribute('data-page')) {
        update(function (s) { s.page = parseInt(t.getAttribute('data-page'), 10); });
        $('sr-count').focus();
        $('sr-count').scrollIntoView({ block: 'start' });
      } else if (t.hasAttribute('data-more')) {
        var key = t.getAttribute('data-more');
        ui.expanded[key] = !ui.expanded[key];
        render();
      } else if (act === 'raw') {
        update(function (s) { s.raw = true; });
      } else if (act === 'widen') {
        update(function (s) { s.scope = ''; s.type = ''; s.letter = ''; s.page = 1; });
        $('sr-count').focus();
      } else if (act === 'letter') {
        update(function (s) { s.letter = ''; s.page = 1; });
        $('sr-count').focus();
      } else if (act === 'facet') {
        var k = t.getAttribute('data-key');
        var v = t.getAttribute('data-value');
        update(function (s) { s.filters[k] = s.filters[k].filter(function (x) { return x !== v; }); s.page = 1; });
        $('sr-count').focus();
      } else if (act === 'clear') {
        update(function (s) { S.FACET_KEYS.forEach(function (fk) { s.filters[fk] = []; }); s.letter = ''; s.page = 1; });
        $('sr-count').focus();
      } else if (act === 'all-types') {
        update(function (s) { s.type = ''; s.scope = ''; s.page = 1; });
      } else if (t.id === 'sr-copy') {
        copyLink();
      } else if (t.hasAttribute('data-layout')) {
        var layout = t.getAttribute('data-layout');
        update(function (s) { s.layout = layout; });
      }
    });

    app.addEventListener('change', function (e) {
      var t = e.target;
      if (t.matches('input[type="checkbox"][data-key]')) {
        var k = t.getAttribute('data-key');
        var drop = t.closest('[data-drop]');
        ui.openDrop = drop ? drop.getAttribute('data-drop') : null;
        update(function (s) {
          var cur = s.filters[k] || [];
          s.filters[k] = t.checked ? cur.concat([t.value]) : cur.filter(function (x) { return x !== t.value; });
          s.page = 1;
        });
      } else if (t.id === 'sr-sort') {
        update(function (s) { s.sort = t.value; s.page = 1; });
      } else if (t.id === 'sr-per') {
        update(function (s) { s.per = parseInt(t.value, 10); s.page = 1; });
      }
    });

    /* Filter within a long facet: hides options in place, no re-render */
    app.addEventListener('input', function (e) {
      var t = e.target;
      if (!t.hasAttribute('data-facet-filter')) return;
      var group = t.closest('.facet');
      var nq = S.norm(t.value);
      Array.prototype.forEach.call(group.querySelectorAll('.facet-opt'), function (opt) {
        var match = !nq || (' ' + opt.getAttribute('data-v')).indexOf(' ' + nq) >= 0;
        opt.hidden = nq ? !match : opt.hasAttribute('data-extra') && !ui.expanded[group.getAttribute('data-facet')];
      });
    });

    app.addEventListener('toggle', function (e) {
      var d = e.target;
      if (d.matches && d.matches('.facet-drop')) {
        if (d.open) {
          ui.openDrop = d.getAttribute('data-drop');
          Array.prototype.forEach.call(app.querySelectorAll('.facet-drop[open]'), function (o) { if (o !== d) o.open = false; });
        } else if (ui.openDrop === d.getAttribute('data-drop')) ui.openDrop = null;
      } else if (d.id === 'facet-panel') ui.panelOpen = d.open;
    }, true);

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      var open = app.querySelector('.facet-drop[open]');
      if (open) { open.open = false; ui.openDrop = null; open.querySelector('summary').focus(); }
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.facet-drop')) {
        Array.prototype.forEach.call(app.querySelectorAll('.facet-drop[open]'), function (o) { o.open = false; });
        ui.openDrop = null;
      }
    });
    window.addEventListener('popstate', function () { state = S.readState(); render(); });
  }

  /* ======================================================================
     3. Advanced search builder (REQ-039)
     Conditions on different fields combine with AND; two on the same field
     combine with OR. It produces an ordinary search, so "Run this search"
     opens the results page at a shareable URL.
     ====================================================================== */
  var FIELDS = [{ key: 'keyword', label: 'Keyword' }, { key: 'exclude', label: 'Leave out the word' }].concat(
    ['ctype', 'topic', 'audience', 'etype', 'format', 'when', 'ptype', 'gkind', 'region', 'status', 'directory', 'year'].map(function (k) {
      return { key: k, label: FACET_LABEL[k] };
    }));
  var TYPES = [{ key: '', label: 'Everything' }].concat(C.categories);
  var PHRASE = {
    keyword: function (v) { return 'mentioning “' + v + '”'; },
    exclude: function (v) { return 'not mentioning “' + v + '”'; },
    ctype: function (v) { return 'of type ' + v; },
    topic: function (v) { return 'on ' + v; },
    audience: function (v) { return 'for ' + v.toLowerCase(); },
    etype: function (v) { return 'that are a ' + v.toLowerCase(); },
    format: function (v) { return 'held ' + v.toLowerCase(); },
    when: function (v) { return v === 'Upcoming' ? 'still to come' : 'already held'; },
    ptype: function (v) { return 'that are a ' + v.toLowerCase(); },
    gkind: function (v) { return 'that are a ' + v.toLowerCase(); },
    region: function (v) { return 'in ' + v; },
    status: function (v) { return 'holding ' + v; },
    directory: function (v) { return 'listed in the ' + v; },
    year: function (v) { return 'from ' + v; }
  };
  var EXAMPLES = {
    'computing-courses': { type: 'events', rows: [['ctype', 'Course'], ['when', 'Upcoming'], ['topic', 'Statistical computing']] },
    'health-consultants': { type: 'experts', rows: [['status', 'CStat'], ['directory', 'Consultants Directory'], ['topic', 'Medical and health statistics']] },
    'official-policy': { type: 'policy', rows: [['topic', 'Official statistics'], ['year', '2026'], ['exclude', 'census']] }
  };
  var model = { type: '', rows: [] };
  var values = {};

  function buildValues() {
    FIELDS.forEach(function (f) {
      if (f.key === 'keyword' || f.key === 'exclude') return;
      var set = {};
      S.docs.forEach(function (d) { (d.facets[f.key] || []).forEach(function (v) { set[v] = true; }); });
      var o = (C.valueOrder || {})[f.key];
      values[f.key] = Object.keys(set).sort(function (a, b) {
        if (f.key === 'year') return b.localeCompare(a);
        if (o) return (o.indexOf(a) < 0 ? 99 : o.indexOf(a)) - (o.indexOf(b) < 0 ? 99 : o.indexOf(b));
        return a.localeCompare(b);
      });
    });
  }

  function toState() {
    var st = S.readState('');
    st.type = model.type;
    var words = [];
    model.rows.forEach(function (r) {
      if (!r.value) return;
      if (r.field === 'keyword') words.push(r.value);
      else if (r.field === 'exclude') r.value.split(/\s+/).filter(Boolean).forEach(function (w) { words.push('-' + w); });
      else st.filters[r.field] = (st.filters[r.field] || []).concat([r.value]);
    });
    st.q = words.join(' ');
    return st;
  }

  function readout() {
    var groups = {}, order = [];
    model.rows.forEach(function (r) {
      if (!r.value) return;
      if (!groups[r.field]) { groups[r.field] = []; order.push(r.field); }
      groups[r.field].push(r.value);
    });
    var typeLabel = (TYPES.filter(function (t) { return t.key === model.type; })[0] || TYPES[0]).label.toLowerCase();
    if (!order.length) return 'Find <strong>' + esc(typeLabel) + '</strong>. Add a condition to narrow it.';
    var parts = order.map(function (f) {
      return '<strong>' + groups[f].map(function (v) { return esc(PHRASE[f](v)); }).join(' <em>or</em> ') + '</strong>';
    });
    return 'Find <strong>' + esc(typeLabel) + '</strong> ' + parts.join(' and ') + '.';
  }

  function rowHtml(r, i) {
    var fieldOpts = FIELDS.map(function (f) {
      return '<option value="' + f.key + '"' + (f.key === r.field ? ' selected' : '') + '>' + esc(f.label) + '</option>';
    }).join('');
    var text = r.field === 'keyword' || r.field === 'exclude';
    var valueCtl = text
      ? '<input type="text" id="qb-v-' + i + '" data-row="' + i + '" data-part="value" value="' + esc(r.value || '') + '" placeholder="' + (r.field === 'keyword' ? 'Any words, or &quot;an exact phrase&quot;' : 'One or more words') + '" aria-label="Words for condition ' + (i + 1) + '">'
      : '<select id="qb-v-' + i + '" data-row="' + i + '" data-part="value" aria-label="Value for condition ' + (i + 1) + '"><option value="">Choose</option>' +
        values[r.field].map(function (v) { return '<option' + (v === r.value ? ' selected' : '') + '>' + esc(v) + '</option>'; }).join('') + '</select>';
    var join = i === 0 ? 'Where' : (model.rows.slice(0, i).some(function (o) { return o.field === r.field && !text; }) ? 'or' : 'and');
    return '<div class="qb-row"><span class="qb-join">' + join + '</span>' +
      '<select id="qb-f-' + i + '" data-row="' + i + '" data-part="field" aria-label="Field for condition ' + (i + 1) + '">' + fieldOpts + '</select>' +
      '<span class="wf-meta">' + (r.field === 'keyword' ? 'contains' : r.field === 'exclude' ? '' : 'is') + '</span>' + valueCtl +
      '<button type="button" class="qb-remove" id="qb-x-' + i + '" data-remove="' + i + '" aria-label="Remove condition ' + (i + 1) + '">&times;</button></div>';
  }

  function renderBuilder() {
    var focusId = document.activeElement && document.activeElement.id;
    $('qb-type').innerHTML = TYPES.map(function (t) {
      return '<option value="' + t.key + '"' + (t.key === model.type ? ' selected' : '') + '>' + esc(t.label) + '</option>';
    }).join('');
    $('qb-rows').innerHTML = model.rows.map(rowHtml).join('');
    renderBuilderOutput();
    if (focusId && $(focusId)) $(focusId).focus();
  }

  /* Count, readout and preview only, so typing never rebuilds the row */
  function renderBuilderOutput() {
    var st = toState();
    var r = S.search(st);
    var n = st.type ? r.tabCounts[st.type] : r.total;
    $('qb-readout').innerHTML = readout();
    $('qb-count').textContent = n;
    $('qb-count-label').textContent = n === 1 ? 'match' : 'matches';
    $('qb-preview').innerHTML = r.results.slice(0, 6).map(function (h) {
      return '<li><span class="result-type">' + esc(h.doc.typeLabel) + '</span> <a href="' + S.pageUrl(h.doc.url) + '">' + esc(h.doc.title) + '</a>' +
        ' <span class="wf-meta">' + h.doc.meta.slice(1).filter(Boolean).map(esc).join(' · ') + '</span></li>';
    }).join('') || '<li class="wf-meta">Nothing matches all of these conditions. Remove one, or use the same field twice to allow either value.</li>';
    $('qb-run').setAttribute('href', S.pageUrl('search.html', S.toParams(st)));
  }

  /* Start from the address bar, never from an earlier visit */
  function builderFromUrl() {
    var st = S.readState();
    var rows = [];
    var sq = S.splitQuery(st.q);
    var keep = String(st.q).replace(/(^|\s)-\S+/g, ' ').replace(/\s+/g, ' ').trim();
    if (keep) rows.push({ field: 'keyword', value: keep });
    if (sq.excludes.length) rows.push({ field: 'exclude', value: sq.excludes.join(' ') });
    FIELDS.forEach(function (f) {
      if (f.key === 'keyword' || f.key === 'exclude') return;
      (st.filters[f.key] || []).forEach(function (v) { rows.push({ field: f.key, value: v }); });
    });
    if (!rows.length) rows.push({ field: 'keyword', value: '' });
    model.type = st.type || '';
    model.rows = rows;
    renderBuilder();
  }

  function bindBuilder(host) {
    buildValues();
    builderFromUrl();
    window.addEventListener('pageshow', function (e) { if (e.persisted) builderFromUrl(); });
    host.addEventListener('change', function (e) {
      var t = e.target;
      if (t.id === 'qb-type') { model.type = t.value; renderBuilder(); return; }
      var i = t.getAttribute('data-row');
      if (i === null) return;
      var row = model.rows[parseInt(i, 10)];
      if (t.getAttribute('data-part') === 'field') { row.field = t.value; row.value = ''; }
      else row.value = t.value;
      renderBuilder();
    });
    host.addEventListener('input', function (e) {
      var t = e.target;
      if (t.getAttribute('data-part') !== 'value' || t.tagName !== 'INPUT') return;
      model.rows[parseInt(t.getAttribute('data-row'), 10)].value = t.value;
      renderBuilderOutput();
    });
    host.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      if (b.hasAttribute('data-remove')) {
        model.rows.splice(parseInt(b.getAttribute('data-remove'), 10), 1);
        renderBuilder();
        $('qb-add').focus();
      } else if (b.id === 'qb-add') {
        model.rows.push({ field: 'topic', value: '' });
        renderBuilder();
        var last = $('qb-f-' + (model.rows.length - 1));
        if (last) last.focus();
      } else if (b.id === 'qb-reset') {
        model.type = ''; model.rows = [{ field: 'keyword', value: '' }];
        renderBuilder();
      } else if (b.hasAttribute('data-example')) {
        var ex = EXAMPLES[b.getAttribute('data-example')];
        model.type = ex.type;
        model.rows = ex.rows.map(function (r) { return { field: r[0], value: r[1] }; });
        renderBuilder();
      }
    });
  }

  /* ======================================================================
     4. How search is configured: renders the live CONFIG
     ====================================================================== */
  function table(head, rows) {
    return '<div class="table-wrap"><table class="data-table"><thead><tr>' + head.map(function (h) { return '<th scope="col">' + esc(h) + '</th>'; }).join('') +
      '</tr></thead><tbody>' + rows.map(function (r) { return '<tr>' + r.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>';
  }
  function renderConfig(host) {
    var counts = {};
    S.docs.forEach(function (d) { counts[d.cat] = (counts[d.cat] || 0) + 1; });
    var tierRows = Object.keys(C.tiers).sort(function (a, b) { return C.tiers[b] - C.tiers[a]; }).map(function (k) {
      return [esc(k), '&times; ' + C.tiers[k].toFixed(1)];
    });
    var w = C.fieldWeights;
    var html = '';
    html += '<section><h2 class="section-title" id="cfg-tiers">Ranking by page type</h2><p>Every match is scored, then multiplied by its page type, so an expert or a section outranks a passing mention in a news story, and documents sit below the Society\'s own pages.</p>' +
      table(['Page type', 'Multiplier'], tierRows) + '</section>';
    html += '<section><h2 class="section-title" id="cfg-weights">Where the words are found</h2>' +
      table(['Field', 'Points'], [['Title', w.title], ['Tags (topic, type, organiser, status)', w.tags], ['Summary', w.summary], ['Body and document text', w.body], ['Whole title matches the search', '+' + w.exactTitle], ['Title starts with the search', '+' + w.titlePrefix]]) +
      '<p class="wf-meta">Every word must match somewhere (or one of its synonyms). Words of three letters or fewer match whole words only; longer words match the start of a word. Ignored words: ' + C.stopWords.map(esc).join(', ') + '.</p></section>';
    html += '<section><h2 class="section-title" id="cfg-synonyms">Synonyms</h2><p>Any word or phrase in a group finds the others. The results page says when a synonym was used.</p><ul class="cfg-syn">' +
      C.synonyms.map(function (g) { return '<li>' + g.map(function (m) { return '<span class="chip">' + esc(m) + '</span>'; }).join(' ') + '</li>'; }).join('') + '</ul></section>';
    var R = C.correction;
    html += '<section><h2 class="section-title" id="cfg-spelling">Spelling correction</h2><p>Only when a search finds nothing. Words of ' + R.minLength + ' letters or more, never ignored words and never the start of a known word, are matched to the nearest word in the index, up to ' + R.maxDistance + ' changes (' + R.maxDistanceLong + ' for words of ' + R.longFrom + ' letters or more). Ties go to the commoner word. The results page always offers the original search instead.</p></section>';
    html += '<section><h2 class="section-title" id="cfg-tabs">Result types (tabs)</h2>' +
      table(['Tab', 'Items in the prototype', 'Filters offered'], C.categories.map(function (c) {
        return [esc(c.label), counts[c.key] || 0, (C.facetsFor[c.key] || []).map(function (k) { return esc(FACET_LABEL[k]); }).join(', ') || 'None'];
      }).concat([['All', S.docs.length, (C.facetsFor[''] || []).map(function (k) { return esc(FACET_LABEL[k]); }).join(', ')]])) + '</section>';
    var vo = C.valueOrder || {};
    html += '<section><h2 class="section-title" id="cfg-facets">Filters</h2><p>Counts are worked out with every other filter applied except the filter itself. Values that would return nothing are hidden, and so is a filter left with one option. Values are listed by count, except:</p>' +
      table(['Filter', 'Order'], [['Year', 'Newest first']].concat(Object.keys(vo).map(function (k) { return [esc(FACET_LABEL[k]), vo[k].map(esc).join(', ')]; }))) + '</section>';
    html += '<section><h2 class="section-title" id="cfg-aliases">Content-type aliases</h2>' +
      table(['In the CMS', 'Shown as'], Object.keys(C.contentTypeAliases).map(function (k) { return [esc(k), esc(C.contentTypeAliases[k])]; })) +
      '<div class="wf-note query"><span class="wf-note-label">Open question</span>Statements and press releases are shown as one type. Is that right for RSS, or should statements stay separate? <span class="wf-req">REQ-039</span></div></section>';
    html += '<section><h2 class="section-title" id="cfg-scopes">Section searches</h2>' +
      table(['Scope', 'Searches', 'Used by'], Object.keys(C.scopes).map(function (k) {
        var used = { events: 'Events and training menu panel', experts: 'Resources menu panel', policy: 'Policy library link' }[k] || '';
        return [esc(C.scopes[k].label), esc(CAT_LABEL[C.scopes[k].type]), esc(used)];
      })) + '</section>';
    html += '<section><h2 class="section-title" id="cfg-bestbets">Promoted results (later phase)</h2>' +
      table(['Search', 'Pinned result'], Object.keys(C.bestBets).map(function (k) { var d = S.docById[C.bestBets[k]]; return [esc(k), d ? esc(d.title) : '']; })) +
      '<div class="wf-note query"><span class="wf-note-label">Proposed</span>Staff-editable promoted results are a Could. One example is built. <span class="wf-req">REQ-278</span></div></section>';
    host.innerHTML = html;
  }

  document.addEventListener('DOMContentLoaded', function () {
    Array.prototype.forEach.call(document.querySelectorAll('input[data-typeahead]'), attachTypeahead);
    app = $('search-app');
    if (app) {
      state = S.readState();
      bindResults();
      commit(false);
    }
    var b = $('builder-app');
    if (b) bindBuilder(b);
    var cfg = $('config-app');
    if (cfg) renderConfig(cfg);
  });
})();
