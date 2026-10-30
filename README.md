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
  js/rss.js                    Search, filters, calendar, forms, basket, persona, annotations
  js/wireframe.js              Shared ClerksWell wireframe behaviour (menus, tabs, accordions, modals)
  js/data.js                   Sample search index (generated from tools/content.py)
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

- Page content lives in `tools/pages_*.py`; sample events, news, policy documents, jobs, groups and experts in `tools/content.py`. Running `gen.py` **overwrites** `src/pages/`, `src/index.html`, `src/modules/library.html` and `src/js/data.js`, so make page changes in `tools/`, not in `src/pages/`.
- The header, footer, CSS and `rss.js` are edited directly in `src/`.
- The requirements trace reads the catalogue from the path in `RSS_REQS` (default: the ClerksWell review copy). Set it to the revised catalogue when that is ready.
- `validate.js` must report 0 errors before pushing.

## Annotation conventions

- Every note names the requirement(s) it answers, e.g. `REQ-201`.
- Yellow notes: **Behaviour**, **CMS**, **Integration**, **Proposed** (a Could requirement, not built).
- Red notes: **Open question** for RSS.
- Each section of a page also carries an HTML comment naming its module and requirements, so coverage can be checked with a search.

## Search

Search follows the model agreed for Travers Smith: an overlay with type-ahead grouped by content type, curated quick links and suggested searches; one results page for every content type with faceted filters and counts (hiding a filter with one option or none), synonyms, typo tolerance, matches inside documents, highlighted terms, sorting, results per page, zero-results help, and "Refine in advanced search" that carries the current query. An AI-assisted summary (REQ-041) sits above the results.
