/* ==========================================================================
   rss.js — prototype behaviour specific to the RSS site.
   Written directly (never generated). Driven by data attributes; no page has
   its own script. Depends on data.js and search-engine.js (window.RSSSearch).
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
        /* Reload so prices, bookings and gated content all follow the viewer */
        window.location.reload();
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

  function norm(s) { return String(s || '').toLowerCase().replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim(); }

  /* Search itself (type-ahead, results, advanced search) lives in
     search-engine.js and search-ui.js. */

  /* --- Search overlay: open, close, return focus ------------------------ */
  function initOverlay() {
    var overlay = $('#search-overlay');
    if (!overlay) return;
    var input = $('#overlay-q', overlay);
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
          /* Keyword boxes use the site search engine, so synonyms and
             spelling correction work here too (REQ-043, REQ-045) */
          if (key === 'q') {
            var sid = item.getAttribute('data-sid');
            if (sid && engineHits) return !!engineHits.ids[sid];
            return norm(item.getAttribute('data-text') || item.textContent).indexOf(norm(vals[0])) !== -1;
          }
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

      var engineHits = null;
      function apply() {
        var sel = selected();
        engineHits = sel.q && window.RSSSearch ? window.RSSSearch.matchIds(sel.q[0]) : null;
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
  function money2(n) { return '£' + Number(n).toFixed(2); }

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
        var detail = parts[1] || '';
        var price = parseFloat(parts[2]) || 0;
        /* Non-members pay the non-member price (REQ-087) */
        if (getPersona() !== 'member' && b.hasAttribute('data-price-nonmember')) price = parseFloat(b.getAttribute('data-price-nonmember'));
        /* Course pages: use the date the visitor picked */
        var chosen = $('input[data-date-choice]:checked');
        if (b.hasAttribute('data-uses-date') && chosen) {
          detail = chosen.getAttribute('data-date-choice') + ', ' + chosen.getAttribute('data-format');
          price = parseFloat(getPersona() === 'member' ? chosen.getAttribute('data-member') : chosen.getAttribute('data-nonmember'));
        }
        var items = basket();
        items.push({ title: parts[0], detail: detail, price: price });
        basket(items);
        refreshBasketCount();
        if (b.hasAttribute('data-go-basket')) { window.location.href = 'basket.html'; return; }
        var msg = b.parentElement.querySelector('[data-added]');
        if (msg) msg.hidden = false;
      });
    });
    var host = $('[data-basket-list]');
    if (!host) return;
    function draw() {
      var items = basket();
      var discount = store('rss-promo') === 'MEMBER10' ? 0.1 : 0;
      var summary = $('[data-basket-summary]');
      if (!items.length) {
        host.innerHTML = '<div class="empty-state"><h2>Your basket is empty</h2><p>Add a course, event or conference ticket and it will appear here.</p><p><a class="btn" href="events.html">Find an event or course</a> <a class="btn btn-secondary" href="conference.html#tickets">Conference tickets</a></p></div>';
        if (summary) summary.hidden = true;
        return;
      }
      if (summary) summary.hidden = false;
      var sub = 0;
      host.innerHTML = '<table class="data-table"><thead><tr><th scope="col">Item</th><th scope="col">Price</th><th scope="col"><span class="visually-hidden">Remove</span></th></tr></thead><tbody>' +
        items.map(function (it, i) {
          sub += it.price;
          return '<tr><td><strong>' + esc(it.title) + '</strong><br><span class="wf-meta">' + esc(it.detail) + '</span></td><td>' + money2(it.price) + '</td><td><button class="btn-link" type="button" data-remove-item="' + i + '">Remove</button></td></tr>';
        }).join('') + '</tbody></table>';
      var vat = 0; /* training is VAT-exempt in this example; shown for structure */
      var total = sub * (1 - discount) + vat;
      $$('[data-basket-sub]').forEach(function (el) { el.textContent = money2(sub); });
      $$('[data-basket-discount]').forEach(function (el) { el.textContent = discount ? '−' + money2(sub * discount) : money2(0); });
      $$('[data-basket-vat]').forEach(function (el) { el.textContent = money2(vat); });
      $$('[data-basket-total]').forEach(function (el) { el.textContent = money2(total); });
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
    /* Forms marked data-prefill tick the radio named in the URL, e.g. ?format=online */
    $$('form[data-prefill]').forEach(function (form) {
      params().forEach(function (v, k) {
        $$('input[type="radio"][name="' + k + '"]', form).forEach(function (r) { if (r.value === v) r.checked = true; });
      });
    });
    initCourseDates();
    initBookPage();
    /* Empty listings offer the whole-site search for the same words */
    $$('[data-listing]').forEach(function (listing) {
      listing.addEventListener('listing:updated', function () {
        var q = $('[data-filter="q"]', listing);
        $$('[data-site-search]', listing).forEach(function (a) {
          var term = q ? q.value.trim() : '';
          a.closest('[data-site-search-wrap]').hidden = !term;
          a.setAttribute('href', 'search.html?q=' + encodeURIComponent(term));
          a.textContent = 'search the whole site for \u201c' + term + '\u201d';
        });
      });
      listing.dispatchEvent(new CustomEvent('listing:updated'));
    });
  }

  /* Course page: the chosen date drives the price, the Book link and the
     basket; a full date offers the waiting list instead (REQ-214, REQ-218) */
  function initCourseDates() {
    var radios = $$('input[data-date-choice]');
    if (!radios.length) return;
    var member = getPersona() === 'member';
    function update() {
      var r = $('input[data-date-choice]:checked');
      if (!r) return;
      $$('[data-price-for-viewer]').forEach(function (el) {
        el.textContent = member ? 'You pay the member price: £' + r.getAttribute('data-member') : 'You pay the non-member price: £' + r.getAttribute('data-nonmember') + '. Members pay £' + r.getAttribute('data-member') + '.';
      });
      var full = r.hasAttribute('data-full');
      $$('[data-chosen-date]').forEach(function (el) { el.textContent = r.getAttribute('data-date-choice'); });
      $$('[data-book-actions]').forEach(function (el) { el.hidden = full; });
      $$('[data-waitlist]').forEach(function (el) { el.hidden = !full; });
      var price = member ? r.getAttribute('data-member') : r.getAttribute('data-nonmember');
      $$('[data-book-link]').forEach(function (a) {
        a.setAttribute('href', 'book.html?' + new URLSearchParams({ date: r.getAttribute('data-date-choice'), format: r.getAttribute('data-format'), price: price }).toString());
      });
    }
    radios.forEach(function (r) { r.addEventListener('change', update); });
    update();
  }

  /* Booking page: date and unit price come from the course page; the total
     follows the number of delegates */
  function initBookPage() {
    var form = $('form[data-book-form]');
    if (!form) return;
    var p = params();
    var member = getPersona() === 'member';
    var date = p.get('date') || form.getAttribute('data-default-date');
    var fmt = p.get('format') || form.getAttribute('data-default-format');
    var unit = parseFloat(p.get('price') || (member ? form.getAttribute('data-member') : form.getAttribute('data-nonmember')));
    var title = form.getAttribute('data-course');
    $$('[data-book-date]').forEach(function (el) { el.textContent = date + ', ' + fmt; });
    $$('[data-book-rate]').forEach(function (el) { el.textContent = (member ? 'Member price: ' : 'Non-member price: ') + money(unit) + ' per delegate'; });
    function update() {
      var who = $('input[name="who"]:checked', form);
      var count = who && who.value === 'others' ? parseInt(form.elements.count.value, 10) || 1 : 1;
      var total = unit * count;
      form.setAttribute('data-pay-amount', String(total));
      form.setAttribute('data-pay-desc', title + ', ' + date + ', ' + fmt + (count > 1 ? ' (' + count + ' delegates)' : ''));
      $$('[data-book-total]').forEach(function (el) { el.textContent = money(total); });
      $$('[data-book-count]').forEach(function (el) { el.textContent = count === 1 ? '1 delegate' : count + ' delegates'; });
    }
    form.addEventListener('change', update);
    update();
  }

  document.addEventListener('DOMContentLoaded', function () {
    initNotes();
    initPersona();
    initHeader();
    initOverlay();
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
