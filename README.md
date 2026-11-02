# RSS website prototype

A clickable greyscale prototype of the new rss.org.uk (Royal Statistical Society), built by ClerksWell to agree structure, navigation and journeys before design.

- **Phase:** v0.1, first draft (30 October 2026). Not yet reviewed with RSS.
- **Scope:** Must and Should requirements from the draft requirements catalogue. Could requirements (including ClerksWell's REQ-276 to REQ-291) are flagged as "Proposed" notes where they would change a page, but are not built. The catalogue is being revised; regenerate the trace when it is.
- **Fidelity:** greyscale, system fonts, labelled placeholders for all media. Visual design belongs in `src/css/theme.css`, which is deliberately empty.

## Viewing it

GitHub Pages serves the built site from `docs/` on `main`:

1. Push this repository to GitHub.
2. Settings → Pages → Build and deployment → Source: **Deploy from a branch**; Branch: **main**, folder **/docs**.
3. Open `https://<account>.github.io/<repository>/`. The first page is the contents hub; send that link to reviewers.

All links are relative, so it works under any repository name, and locally by opening `docs/index.html` in a browser.

Annotations are **off** by default. Reviewers switch them on in the dark bar at the top of each page. "View as" in the same bar switches between signed out, registered non-member, member and lapsed member.

## Structure

```
README.md
requirements/requirements.md   Must and Should requirements, and the pages that show each one
tools/                         Python page generator (content.py, common.py, pages_*.py, gen.py)
src/                           Source: pages, includes (header, footer), css, js
  includes/header.html         Navigation, mega menus, search overlay (edit once, applies everywhere)
  includes/footer.html         Footer, newsletter sign-up, cookie banner
  js/search-engine.js          Search engine: one index, ranking, synonyms, correction, facets, suggestions
  js/search-ui.js              Type-ahead, results page, advanced search builder, configuration page
  js/rss.js                    Listing filters, calendar, forms, basket, persona, annotations
  js/wireframe.js              Shared ClerksWell wireframe behaviour (menus, tabs, accordions, modals)
  js/data.js                   Search index and search configuration (generated from tools/content.py and tools/search_config.py)
  css/                         base, components, rss (structure); theme (design layer, empty)
build-includes.js              Builds src/ into docs/, resolving includes and ~/ paths
validate.js                    Checks tag balance, handlers and every internal link
docs/                          Built site served by GitHub Pages. Do not edit by hand.
```

## Making changes

Requires Python 3 (with `openpyxl` for the requirements trace) and Node.js. From the repository root:

```
python3 tools/gen.py && node build-includes.js && node validate.js
```

- Page content lives in `tools/pages_*.py`; sample events, news, policy documents, jobs, groups and experts in `tools/content.py`; search settings in `tools/search_config.py`. Running `gen.py` **overwrites** `src/pages/`, `src/index.html`, `src/modules/library.html` and `src/js/data.js`, so make page changes in `tools/`, not in `src/pages/`.
- The header, footer, CSS and the JavaScript files (other than `data.js`) are edited directly in `src/`.
- The requirements trace reads the catalogue from the path in `RSS_REQS` (default: the ClerksWell review copy). Set it to the revised catalogue when that is ready.
- `validate.js` must report 0 errors before pushing.

## Annotation conventions

- Every note names the requirement(s) it answers, e.g. `REQ-201`.
- Yellow notes: **Behaviour**, **CMS**, **Integration**, **Proposed** (a Could requirement, not built).
- Red notes: **Open question** for RSS.
- Each section of a page also carries an HTML comment naming its module and requirements, so coverage can be checked with a search.

## Search

All the people, employers and documents in the search data are fictional.

**Core, built and working**

- One index across pages, events and courses, news, policy documents, sections and groups, experts and jobs. Every search box calls the same `search()`: the header overlay, the home page, the results page, the section searches in the Events and training and Resources menus, and the keyword boxes on the listing pages (`matchIds()`).
- Ranking by page type as a multiplier (experts and groups 6.0, pages 3.0, events, courses and jobs 1.2, news 1.0, documents 0.8), field weights (title 10, tags 4, summary 2, body 1), +60 for an exact title and +12 for a title that starts with the search. Every word must match (AND); any synonym will do (OR).
- Normalisation (case, accents, apostrophes, punctuation, stop words). Words of three letters or fewer match whole words; longer words match word starts.
- Type-ahead from two characters: topics, sections and groups, then experts, then pages, events and documents. Synonym matches say what they matched. ARIA combobox; Up, Down, Enter, Escape.
- Synonym groups, with a notice when one was used. Spelling correction only when nothing matches, with "search for … exactly" (`raw=1`).
- Tabs with counts that stay accurate; filters with live counts (each counted with every other filter except its own), hidden when they would return nothing or offer one option, show all and filter within, chips and Clear all; filters at the side or across the top.
- All state in the URL (query, tab, scope, filters, sort, page, page size, layout, letter) with Back and Forward, and a copy-link control.
- Section searches (`scope=events`, `scope=experts`, `scope=policy`) shown as a chip that widens to the whole site.
- Browse everything with nothing typed; sort by relevance, newest, oldest, year, type and A to Z (undated items last); experts by surname A to Z.
- Advanced search builder with a live count, a plain-English readout and a preview, opening from the current results.
- Text inside documents, with the page that matched.
- `pages/search-configuration.html` renders the live configuration from `tools/search_config.py`.
- The AI-assisted summary (REQ-041) sits above the results and is never shown for experts.

**Later phase, not built**

- Promoted results (REQ-278, a Could): one working example, for "renew".
- Editor-maintained synonyms (REQ-047, a Could); search across the RSS family of sites (REQ-291, a Could); search analytics dashboards (REQ-118); saved searches and alerts; Word and PowerPoint text; location-aware search; reference-number matching.
