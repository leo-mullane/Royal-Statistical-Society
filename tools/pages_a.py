"""Home, search, membership and joining."""
from common import *


def event_card(ev, featured=False):
    img = '<div class="wf-placeholder ratio-16-9">Image 16:9</div>' if featured else ''
    places = f'<p class="wf-meta"><strong>{e(ev["places"])}</strong></p>' if ev.get('places') else ''
    return f'''<article class="card">
          {img}<p class="meta-row"><span class="tag">{e(ev.get("sub", ""))}</span><span class="tag">{fmt_label(ev["fmt"])}</span></p>
          <h3 class="card-title"><a href="~/pages/{event_url(ev)}">{e(ev["title"])}</a></h3>
          <p class="card-text">{drange(ev["date"], ev["end"])}<br>{e(ev["place"])}</p>{places}
        </article>'''


def home():
    n = Notes()
    up_events = [x for x in EVENTS if x['kind'] == 'event' and x['date'] >= TODAY]
    feat = [x for x in up_events if x.get('featured')][:2]
    rest = [x for x in up_events if x not in feat][:4]
    courses = [x for x in EVENTS if x['kind'] == 'course' and x['date'] >= TODAY][:6]
    news = sorted(NEWS, key=lambda x: (not x.get('featured'), x['date']), reverse=False)[:4]
    news = [x for x in NEWS if x.get('featured')] + [x for x in NEWS if not x.get('featured')][:3]
    slides = ''.join(f'''<div class="carousel-item">
            <div class="wf-placeholder ratio-16-9">Image 16:9</div>
            <div><p class="meta-row"><span>{d(x["date"])}</span><a href="~/pages/news.html">{e(TOPICS[x["topics"][0]])}</a></p>
            <h3><a href="~/pages/article.html">{e(x["title"])}</a></h3><p>{e(x["summary"])}</p></div>
          </div>''' for x in news)
    body = f'''
      <!-- Home page hero with site search (REQ-101, REQ-238, REQ-037) -->
      <section class="hub-hero">
        <div>
          <h1>Statistics and data for the public good</h1>
          <p class="lead">The Royal Statistical Society is the professional body for statisticians and data scientists, and a charity that promotes the use of statistics for the benefit of society.</p>
          <form class="big-search" action="~/pages/search.html" role="search">
            <label for="home-q" class="visually-hidden">Search the RSS website</label>
            <input type="search" id="home-q" name="q" placeholder="Search events, courses, policy and more">
            <button class="btn" type="submit">Search</button>
          </form>
          <p data-show-for="guest registered"><a class="btn" href="~/pages/join.html">Join the RSS</a> <a class="btn btn-secondary" href="~/pages/events.html">Find an event or course</a></p>
          <div class="panel surface" data-show-for="member" hidden>
            <p><strong>Welcome back, Dr Alex Morgan.</strong> Your membership renews on 1 January 2027. You have 1 booking coming up.</p>
            <a href="~/pages/myrss.html">Go to MyRSS</a>
          </div>
          <div class="panel surface" data-show-for="lapsed" hidden>
            <p><strong>Your membership lapsed on 30 September 2026.</strong> Renew to keep your Fellowship, CPD record and journal access.</p>
            <a class="btn" href="~/pages/myrss.html#renew">Renew now</a>
          </div>
          {n("The welcome panel changes with the viewer. Use <strong>View as</strong> in the grey bar to see the signed-out, member and lapsed versions.", "REQ-101, REQ-109, REQ-178")}
        </div>
        <div class="wf-placeholder ratio-4-3">Image or short muted video 4:3</div>
      </section>
      {n("The section you are in is marked in the main menu, and menu labels, order and promo slots are edited in the CMS.", "REQ-032, REQ-028", "CMS")}
      {n("Editors can A/B test key blocks and calls to action on this page, and add tracking to any block, button or banner without a developer.", "REQ-023, REQ-115", "CMS")}
      {n("Multilingual content is a Should. Which languages, and which parts of the site? A language switch would sit in the utility bar.", "REQ-125, REQ-127", "Open question")}
      {n("The hero can carry a short looping video (RSS wishlist). It must have a pause control, captions where there is speech, and a still-image fallback on slow connections.", "REQ-013", "Proposed")}

      <!-- Task-led entry points (REQ-238, REQ-027) -->
      <section aria-labelledby="tasks-title">
        <h2 class="section-title" id="tasks-title">What would you like to do?</h2>
        <div class="task-grid">
          <a class="task" href="~/pages/join.html">Join the RSS<span>Grades, fees and how to apply</span></a>
          <a class="task" href="~/pages/events.html">Find an event or course<span>Discussion meetings, section events and training</span></a>
          <a class="task" href="~/pages/chartered-statistician.html">Become a Chartered Statistician<span>Professional status and CPD</span></a>
          <a class="task" href="~/pages/find-an-expert.html">Find an expert<span>Search the Professional Register</span></a>
          <a class="task" href="~/pages/groups.html">Find a group near you<span>Sections, local groups and SIGs</span></a>
          <a class="task" href="~/pages/publications.html">Read our journals<span>Series A, B and C, and Significance</span></a>
          <a class="task" href="~/pages/policy.html">Read our policy work<span>Responses, evidence and reports</span></a>
          <a class="task" href="~/pages/jobs.html">Find a job<span>Statistics and data science vacancies</span></a>
        </div>
        {n("Editors choose the eight tasks and their order. Tiles are a reusable component, so a hub page can use the same block.", "REQ-238, REQ-018, REQ-019", "CMS")}
      </section>

      <!-- Audience shortcuts (REQ-027, REQ-253) -->
      <section class="audience-strip" aria-label="Shortcuts by audience">
        <strong>I am a&hellip;</strong>
        <a href="~/pages/resources.html#students">Student or early-career statistician</a>
        <a href="~/pages/find-an-expert.html">Employer</a>
        <a href="~/pages/for-journalists.html">Journalist</a>
        <a href="~/pages/resources.html#educators">Educator</a>
        <a href="~/pages/policy.html">Policymaker</a>
      </section>
      {n("Audience shortcuts link to the audience resource hubs. The same shortcuts appear in the footer.", "REQ-027, REQ-253")}

      <!-- Personalised block (REQ-109, REQ-111, REQ-177) -->
      <section data-show-for="member" hidden aria-labelledby="foryou-title">
        <h2 class="section-title" id="foryou-title">Recommended for you</h2>
        <p class="wf-meta">Based on your interests: Medical and health statistics, Methodology</p>
        <div class="grid grid-3">
          {event_card(EVENTS[2])}
          {event_card(EVENTS[10])}
          <article class="card"><p class="meta-row"><span class="tag">Policy document</span></p><h3 class="card-title"><a href="~/pages/policy.html">Briefing: understanding excess deaths</a></h3><p class="card-text">What excess death figures measure and how to report them.</p></article>
        </div>
        {n("Recommendations use the interests in the member's MyRSS profile, drawn from the same topic list that content is tagged with, plus member grade and country.", "REQ-109, REQ-111, REQ-177")}
      </section>
      <section data-show-for="guest registered" aria-labelledby="whyjoin-title">
        <div class="content-highlight">
          <div class="wf-placeholder ratio-16-9">Image 16:9</div>
          <div>
            <h2 id="whyjoin-title">Join 10,000 statisticians and data scientists</h2>
            <p>Professional recognition, four journals, discounted training and a network of sections and local groups across the UK and beyond.</p>
            <a class="btn" href="~/pages/membership.html">Why join</a> <a href="~/pages/grades-fees.html">See grades and fees</a>
          </div>
        </div>
      </section>

      <!-- Latest events and training (REQ-239, REQ-240) -->
      <section aria-labelledby="events-title">
        <h2 class="section-title" id="events-title">Events and training</h2>
        <div class="tabs" role="tablist">
          <button class="tab active" type="button" data-tab="home-events">Events</button>
          <button class="tab" type="button" data-tab="home-courses">Training courses</button>
        </div>
        <div>
          <div class="tab-panel active" id="home-events">
            <div class="grid grid-2">{"".join(event_card(x, True) for x in feat)}</div>
            <div class="grid grid-4" style="margin-top:1.5rem">{"".join(event_card(x) for x in rest)}</div>
            <p><a href="~/pages/events.html?type=event">All events &rarr;</a></p>
          </div>
          <div class="tab-panel" id="home-courses">
            <div class="grid grid-3">{"".join(event_card(x) for x in courses)}</div>
            <p><a href="~/pages/events.html?type=course">All training courses &rarr;</a></p>
          </div>
        </div>
        {n("Pulled automatically from the events and training data (Dynamics), soonest first. Editors can pin featured items. Events: 2 featured plus 4 standard. Training: 6 public courses.", "REQ-239, REQ-240, REQ-213")}
      </section>

      <!-- News carousel (REQ-237) -->
      <section aria-labelledby="news-title">
        <h2 class="section-title" id="news-title">Latest news</h2>
        <div class="carousel" aria-roledescription="carousel">
          <div class="carousel-track">{slides}</div>
          <div class="carousel-controls">
            <button class="carousel-arrow" type="button" data-dir="prev" aria-label="Previous story">&lsaquo;</button>
            <button class="carousel-arrow" type="button" data-dir="next" aria-label="Next story">&rsaquo;</button>
          </div>
          <div class="carousel-indicators"></div>
        </div>
        <p><a href="~/pages/news.html">All news &rarr;</a></p>
        {n("Four stories, featured first, each with its date and a linked category. Does not auto-advance, so nobody has to chase it.", "REQ-237, REQ-235")}
      </section>

      <!-- From the RSS family of sites (REQ-020, REQ-033) -->
      <section aria-labelledby="family-title">
        <h2 class="section-title" id="family-title">From the RSS family</h2>
        <div class="grid grid-3">
          <article class="card"><div class="wf-placeholder ratio-16-9">Image 16:9</div><p class="meta-row"><span class="tag">Significance</span></p><h3 class="card-title"><a href="#">The statistics of extreme heat</a></h3><p class="card-text">How attribution studies estimate the role of climate change in a single heatwave.</p></article>
          <article class="card"><div class="wf-placeholder ratio-16-9">Image 16:9</div><p class="meta-row"><span class="tag">Real World Data Science</span></p><h3 class="card-title"><a href="#">Validating clinical prediction models</a></h3><p class="card-text">A practical checklist for anyone building or buying a clinical risk model.</p></article>
          <article class="card"><div class="wf-placeholder ratio-16-9">Image 16:9</div><p class="meta-row"><span class="tag">Series A</span></p><h3 class="card-title"><a href="~/pages/publications.html">Latest issue: Statistics in Society</a></h3><p class="card-text">Read the latest papers. Members sign in once for full access.</p></article>
        </div>
        {n("Latest articles pulled from the Significance and Real World Data Science feeds and restyled to sit natively on rss.org.uk. Links go to the source site.", "REQ-020, REQ-033")}
        {n("What do Significance (WordPress) and Real World Data Science publish as feeds or APIs, and who owns Real World Data Science's content?", "REQ-020", "Open question")}
      </section>

      <!-- Featured tiles: get involved, experts, jobs (REQ-238) -->
      <section aria-labelledby="involved-title">
        <h2 class="section-title" id="involved-title">Get involved</h2>
        <div class="grid grid-3">
          <article class="card"><h3 class="card-title">Volunteering opportunities</h3>
            <ul class="stack">
              <li><a href="~/pages/article.html">Statistical Ambassadors 2027</a><br><span class="wf-meta">Closes 30 November</span></li>
              <li><a href="~/pages/article.html">Medical Section committee places</a><br><span class="wf-meta">Two places for 2027</span></li>
              <li><a href="~/pages/get-involved.html#s4s">Statisticians for Society: pro bono projects</a><br><span class="wf-meta">Ongoing</span></li>
            </ul>
            <a class="card-link" href="~/pages/get-involved.html#volunteering">All volunteering &rarr;</a>
          </article>
          <article class="card"><h3 class="card-title">Find an expert</h3><p class="card-text">Need a qualified statistician? Search the Professional Register and Consultants Directory.</p>
            <form action="~/pages/find-an-expert.html" role="search"><label for="home-expert">Name, skill or area</label><div class="inline-field"><input type="search" id="home-expert" name="q"><button class="btn btn-small" type="submit">Search</button></div></form>
          </article>
          <article class="card"><h3 class="card-title">Latest jobs</h3>
            <ul class="stack">{"".join(f'<li><a href="~/pages/job.html">{e(j["title"])}</a><br><span class="wf-meta">{e(j["employer"])}, {e(j["place"])}</span></li>' for j in JOBS[:3])}</ul>
            <a class="card-link" href="~/pages/jobs.html">All jobs &rarr;</a>
          </article>
        </div>
      </section>

      <section class="statistics" aria-label="The RSS in numbers">
        <div class="stat-item"><div class="stat-value">1834</div><div class="stat-title">Founded</div><div class="stat-description">Royal charter society</div></div>
        <div class="stat-item"><div class="stat-value">10,000+</div><div class="stat-title">Members</div><div class="stat-description">In more than 50 countries</div></div>
        <div class="stat-item"><div class="stat-value">42</div><div class="stat-title">Sections and local groups</div><div class="stat-description">UK and international</div></div>
        <div class="stat-item"><div class="stat-value">4</div><div class="stat-title">Journals</div><div class="stat-description">Series A, B, C and Significance</div></div>
      </section>
      {n("Figures are placeholders to check with RSS. Every block on this page is optional and reorderable in the CMS.", "REQ-101, REQ-018", "CMS")}
'''
    page('home.html', 'Home', body, '', None)


def search_page():
    n = Notes()
    body = f'''
      <!-- Site search results (REQ-037 to REQ-046) -->
      <section data-search-results>
        <h1>Search</h1>
        <form class="big-search" role="search" data-results-form>
          <label for="results-q" class="visually-hidden">Search the RSS website</label>
          <input type="search" id="results-q" name="q" placeholder="Search the RSS website">
          <button class="btn" type="submit">Search</button>
        </form>
        <p><a href="~/pages/search-advanced.html" data-advanced-link>Refine in advanced search</a></p>
        {n("One results page for every content type: pages, events, courses, news, policy documents (including text inside PDFs and Office files), jobs, groups and experts. Try <a href=\'?q=CStat\'>CStat</a>, <a href=\'?q=bayseian\'>bayseian</a> (typo), <a href=\'?q=census\'>census</a> (matches inside documents) or <a href=\'?q=qwertyuiop\'>a search with no results</a>.", "REQ-037, REQ-038, REQ-044")}
        <div class="finder">
          <aside class="facets" aria-label="Filter results">
            <div class="facets-head"><h2 class="facet-title">Filter by</h2></div>
            <div data-facet-host></div>
            {n("Counts update as you filter. A filter group with only one option is hidden, as agreed for Travers Smith.", "REQ-039, REQ-031")}
          </aside>
          <div>
            <div class="ai-answer" data-ai-answer hidden>
              <h2>Summary</h2>
              <p data-ai-text></p>
              <ol class="chips" data-ai-sources></ol>
              <p class="wf-meta">AI-generated from pages on this site. Check the sources.</p>
            </div>
            {n("AI-assisted answer drawn only from rss.org.uk content, with numbered sources. Shown for questions and high-confidence queries; never for people. Model and provider (Copilot or other) to agree with the tech lead.", "REQ-041, REQ-153")}
            {n("Should the AI summary appear by default, or behind an \'Ask a question\' control?", "REQ-041", "Open question")}
            <div data-search-notices></div>
            <div class="active-filters" data-active-filters></div>
            <div class="results-bar">
              <p class="result-count" data-result-count aria-live="polite"></p>
              <button class="btn btn-secondary btn-small facets-toggle" type="button" data-facets-toggle aria-expanded="false">Filters</button>
              <div class="field"><label for="sort">Sort by</label>
                <select id="sort" data-sort>
                  <option value="relevance">Relevance</option>
                  <option value="newest">Date, newest first</option>
                  <option value="oldest">Date, oldest first</option>
                  <option value="type">Content type</option>
                  <option value="title">Title A to Z</option>
                </select></div>
              <div class="field"><label for="per">Show</label>
                <select id="per" data-per><option value="10">10</option><option value="20">20</option><option value="50">50</option></select></div>
            </div>
            {n("Sort by relevance, date, type or title. Results per page can be changed by the user; editors set the default.", "REQ-040, REQ-106")}
            <div data-result-list></div>
            <div class="empty-state" data-zero hidden>
              <h2>No results found</h2>
              <ul class="prose" style="text-align:left;margin:0 auto 1rem;max-width:30rem">
                <li>Check the spelling, or try fewer or more general words</li>
                <li>Remove some filters</li>
                <li>Browse <a href="~/pages/events.html">events and courses</a>, <a href="~/pages/policy.html">policy</a> or <a href="~/pages/news.html">news</a></li>
              </ul>
              <p>Still stuck? <a href="~/pages/about.html#contact">Contact us</a> and we'll help.</p>
            </div>
            <ul class="pagination" data-pagination></ul>
            {n("Search terms are highlighted in titles and summaries. Spelling is corrected automatically and synonyms are included (for example CStat and Chartered Statistician), with a notice and a way back to the exact search.", "REQ-042, REQ-043, REQ-045, REQ-046")}
          </div>
        </div>
      </section>
'''
    page('search.html', 'Search', body, '', [('Search', None)])


def advanced():
    n = Notes()
    topic_opts = ''.join(f'<option value="{e(v)}">{e(v)}</option>' for v in TOPICS.values())
    types = ['Page', 'Event', 'Course', 'News', 'Press release', 'Policy document', 'Job', 'Group', 'Expert']
    tchecks = ''.join(f'<label class="check"><input type="checkbox" name="type" value="{t}"> {t}</label>' for t in types)
    body = f'''
      <!-- Advanced search (REQ-039) -->
      <h1>Advanced search</h1>
      <p class="lead">Opens on the search you came from, so you can refine it.</p>
      {n("Opens pre-filled from the results page ('Refine in advanced search'), or empty if opened from the menu. Fixed for Travers Smith: it never keeps a stale earlier search.", "REQ-039")}
      <form class="form-step" data-advanced-form>
        <div class="field"><label for="adv-all">All of these words</label><input type="text" id="adv-all" name="all"></div>
        <div class="field"><label for="adv-phrase">This exact phrase</label><input type="text" id="adv-phrase" name="phrase"></div>
        <div class="field"><label for="adv-none">None of these words</label><input type="text" id="adv-none" name="none"><p class="field-hint">Separate words with spaces</p></div>
        <fieldset class="field"><legend>Content type</legend>{tchecks}</fieldset>
        <div class="field"><label for="adv-topic">Topic</label><select id="adv-topic" name="topic"><option value="">Any topic</option>{topic_opts}</select></div>
        <div class="field-row">
          <div class="field"><label for="adv-from">From date</label><input type="date" id="adv-from" name="from"></div>
          <div class="field"><label for="adv-to">To date</label><input type="date" id="adv-to" name="to"></div>
        </div>
        <p><button class="btn" type="submit">Search</button> <button class="btn btn-secondary" type="button" data-advanced-reset>Clear</button></p>
      </form>
'''
    page('search-advanced.html', 'Advanced search', body, '', [('Search', '~/pages/search.html'), ('Advanced search', None)])


GRADES = [
    ('fellow', 'Fellow', 'The standard grade, for anyone with an interest in statistics or data. No qualifications needed.', 165),
    ('gradstat', 'Graduate Statistician (GradStat)', 'For graduates with a degree that meets our academic standard.', 185),
    ('cstat', 'Chartered Statistician (CStat)', 'Our highest professional award: qualifications plus at least five years of experience.', 230),
    ('analyst', 'Data Analyst', 'For people working with data, from apprentices to experienced analysts.', 165),
    ('fis', 'Fellow or Member of an International Society (FIS/MIS)', 'For members of partner societies outside the UK.', 95),
    ('student', 'e-Student', 'For full-time students. Digital journals and events at student rates.', 25),
]


def membership():
    n = Notes()
    cards = ''.join(f'<article class="card"><h3 class="card-title">{e(t)}</h3><p class="card-text">{e(s)}</p><p><strong>From £{p} a year</strong></p></article>' for _, t, s, p in GRADES)
    body = f'''
      <section class="hub-hero">
        <div>
          <h1>Membership</h1>
          <p class="lead">Join a community of 10,000 statisticians and data scientists in more than 50 countries.</p>
          <p data-show-for="guest registered"><a class="btn" href="~/pages/join.html">Join now</a> <a class="btn btn-secondary" href="~/pages/grades-fees.html">Grades and fees</a></p>
          <p data-show-for="member" hidden><span class="status-pill">You are a member: CStat</span> <a href="~/pages/myrss.html">Manage your membership</a></p>
          <p data-show-for="lapsed" hidden><a class="btn" href="~/pages/myrss.html#renew">Renew your membership</a></p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>

      <!-- Benefits (REQ-238) -->
      <section aria-labelledby="benefits">
        <h2 class="section-title" id="benefits">What membership gives you</h2>
        <div class="grid grid-3">
          <article class="card"><h3 class="card-title">Professional recognition</h3><p class="card-text">Use the letters after your name and work towards GradStat, CStat or Data Analyst status.</p></article>
          <article class="card"><h3 class="card-title">Journals and Significance</h3><p class="card-text">Online access to Series A, B and C, and Significance in print and online.</p></article>
          <article class="card"><h3 class="card-title">Training at member rates</h3><p class="card-text">Around 25% off public courses, and CPD you can record in MyRSS.</p></article>
          <article class="card"><h3 class="card-title">Sections and local groups</h3><p class="card-text">Meetings, newsletters and networks in your field and near you.</p></article>
          <article class="card"><h3 class="card-title">A voice in policy</h3><p class="card-text">Contribute to consultation responses and campaigns.</p></article>
          <article class="card"><h3 class="card-title">Directories</h3><p class="card-text">Be listed in the Fellows Directory, and in the Consultants Directory if you offer consultancy.</p></article>
        </div>
      </section>

      <!-- Membership grades (REQ-187) -->
      <section aria-labelledby="grades">
        <h2 class="section-title" id="grades">Membership grades</h2>
        <div class="grid grid-3">{cards}</div>
        <p><a href="~/pages/grades-fees.html">Compare grades, fees and concessions &rarr;</a></p>
        {n("Six membership classes, each with its own joining and renewal fees and concessions, held in Dynamics. Fees on this page are placeholders.", "REQ-187, REQ-189")}
        {n("Does 'Fellow' stay as the name of the standard grade? Many visitors read it as an honour.", "REQ-187", "Open question")}
      </section>

      <section class="content-highlight">
        <blockquote class="wf-quote"><p>"Becoming chartered gave me the credibility to lead our analytics team, and the Society's courses filled the gaps."</p><cite>Member, CStat, NHS analyst</cite></blockquote>
        <div><h2>How professional status works</h2><p>Join as a Fellow, then apply for GradStat, CStat or Data Analyst status from MyRSS when you are ready.</p><a href="~/pages/chartered-statistician.html">How to become a Chartered Statistician</a></div>
      </section>
      {n("Applying for professional status within the joining journey is ClerksWell's suggestion REQ-277 (a Could), so it is not prototyped here.", "REQ-277", "Proposed")}

      <!-- FAQs (REQ-104) -->
      <section aria-labelledby="faqs">
        <h2 class="section-title" id="faqs">Membership FAQs</h2>
        <div class="accordion">
          <div class="accordion-item"><button class="accordion-title" type="button">Do I need a statistics degree to join? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>No. Fellowship is open to anyone with an interest in statistics or data. Professional grades have their own requirements.</p></div></div>
          <div class="accordion-item"><button class="accordion-title" type="button">Can I pay by Direct Debit? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>Yes. You can pay annually by card or Direct Debit, or in instalments by Direct Debit.</p></div></div>
          <div class="accordion-item"><button class="accordion-title" type="button">Is there a cooling-off period? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>Yes, 14 days from the date you join.</p></div></div>
          <div class="accordion-item"><button class="accordion-title" type="button">My employer pays for my membership. What do I do? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>Choose 'Invoice my organisation' at the payment step and give us their details.</p></div></div>
        </div>
        {n("FAQs are a reusable accordion component; editors add, reorder and remove questions.", "REQ-104, REQ-013", "CMS")}
      </section>
'''
    page('membership.html', 'Membership', body, 'membership', [('Membership', None)])


def grades_fees():
    n = Notes()
    rows = ''.join(f'<tr><th scope="row">{e(t)}</th><td>{e(s)}</td><td>£{p}</td><td>£{round(p*0.75)}</td></tr>' for _, t, s, p in GRADES)
    body = f'''
      <div class="with-sidenav">
        <nav class="sidenav" aria-label="Membership">
          <h2>Membership</h2>
          <ul>
            <li><a href="~/pages/membership.html">Why join</a></li>
            <li><a href="~/pages/grades-fees.html" aria-current="page">Grades and fees</a>
              <ul><li><a href="#concessions">Concessions</a></li><li><a href="#students">Students</a></li></ul></li>
            <li><a href="~/pages/join.html">Join now</a></li>
            <li><a href="~/pages/membership.html#faqs">FAQs</a></li>
          </ul>
        </nav>
        <div>
          <h1>Membership grades and fees</h1>
          <p class="lead">Fees for 2027. Prices include journal access for your grade.</p>
          {n("Section navigation in the left column, generated from the page tree. On mobile it moves above the content.", "REQ-029")}
          <!-- Fees table (REQ-187, REQ-189) -->
          <div class="table-wrap"><table class="data-table">
            <thead><tr><th scope="col">Grade</th><th scope="col">Who it is for</th><th scope="col">Annual fee</th><th scope="col">With a concession</th></tr></thead>
            <tbody>{rows}</tbody>
          </table></div>
          {n("Fees come from Dynamics, so they are never typed into a page. Figures shown are placeholders.", "REQ-087, REQ-189, REQ-154", "Integration")}
          <h2 id="concessions" style="margin-top:2rem">Concessions</h2>
          <p>We offer 25% off for members who are:</p>
          <ul class="prose"><li>on a career break or parental leave</li><li>in their first two years after graduating</li><li>retired, or aged 60 or over</li><li>in an eligible developing country (EDA)</li></ul>
          <p>Honorary and compounder members pay no annual fee. Students should choose e-Student membership.</p>
          <h2 id="students">Students</h2>
          <p>e-Student membership costs £25 a year and includes digital journals, events at student rates and the Young Statisticians Section.</p>
          <p><a class="btn" href="~/pages/join.html">Join now</a></p>
          {n("A membership pathway finder (questions that recommend a grade) is ClerksWell's suggestion REQ-276 (a Could), so this page uses a comparison table instead.", "REQ-276", "Proposed")}
        </div>
      </div>
'''
    page('grades-fees.html', 'Membership grades and fees', body, 'membership', [('Membership', '~/pages/membership.html'), ('Grades and fees', None)])


def join():
    n = Notes()
    grade_radios = ''.join(f'<label class="radio-card"><input type="radio" name="grade" value="{k}" data-price="{p}" required data-error="Choose a membership grade"> <strong>{e(t)}</strong>{e(s)} <span class="wf-meta">£{p} a year</span></label>' for k, t, s, p in GRADES)
    body = f'''
      <h1>Join the RSS</h1>
      <p class="lead">It takes about 10 minutes. You can save your application and come back to it.</p>
      <ol class="steps" aria-label="Application progress">
        <li>Membership</li><li>Your details</li><li>Journals and newsletters</li><li>Payment</li><li>Check and confirm</li>
      </ol>
      {n("Multi-step form built with the form builder: required fields marked, hints inline, an error summary at the top of each step, and save-and-resume. Try continuing without choosing a grade.", "REQ-186, REQ-082, REQ-050, REQ-097")}
      <div class="split">
        <!-- Online joining form (REQ-186) -->
        <form data-steps novalidate>
          <section class="form-step">
            <h2>Choose your membership</h2>
            <fieldset class="field"><legend>Membership grade</legend><div class="radio-cards">{grade_radios}</div></fieldset>
            <div class="field"><label for="concession">Concession (optional)</label>
              <select id="concession" name="concession">
                <option value="">None</option>
                <option value="career-break" data-price="-40">Career break or parental leave</option>
                <option value="new-grad" data-price="-40">New graduate (first two years)</option>
                <option value="retired" data-price="-40">Retired, or aged 60 or over</option>
                <option value="eda" data-price="-40">Eligible developing country</option>
              </select>
              <p class="field-hint">We may ask for evidence later.</p></div>
            <div class="form-nav"><span></span><button class="btn" type="button" data-next>Continue</button></div>
          </section>

          <section class="form-step" hidden>
            <h2>Your details</h2>
            <div class="field-row">
              <div class="field"><label for="j-first">First name</label><input type="text" id="j-first" name="first" required autocomplete="given-name"></div>
              <div class="field"><label for="j-last">Last name</label><input type="text" id="j-last" name="last" required autocomplete="family-name"></div>
            </div>
            <div class="field"><label for="j-email">Email address</label><input type="email" id="j-email" name="email" required autocomplete="email" data-error="Enter an email address in the correct format, like name@example.com"></div>
            <div class="field"><label for="j-postcode">Postcode</label>
              <div class="inline-field"><input type="text" id="j-postcode" name="postcode" required autocomplete="postal-code"><button class="btn btn-secondary btn-small" type="button" data-dismiss="address-pick-hint">Find address</button></div>
              <p class="field-hint" id="address-pick-hint">Or <a href="#">enter your address manually</a></p>
            </div>
            {n("Address look-up as you type the postcode (Loqate), with a manual option for addresses outside the UK.", "REQ-092", "Integration")}
            <div class="field"><label for="j-employer">Employer or university (optional)</label><input type="text" id="j-employer" name="employer"></div>
            <div class="field"><label for="j-pass">Create a password</label><input type="password" id="j-pass" name="password" required autocomplete="new-password"><p class="field-hint">At least 12 characters. You will use this to sign in to MyRSS.</p></div>
            {n("This creates the MyRSS account at the same time. Someone who already has a registered account signs in first and their details are filled in.", "REQ-076, REQ-075")}
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue</button></div>
          </section>

          <section class="form-step" hidden>
            <h2>Journals and newsletters</h2>
            <fieldset class="field"><legend>Print journals (optional)</legend>
              <p class="field-hint">Online access to Series A, B and C is included. Add print copies if you want them.</p>
              <label class="check"><input type="checkbox" name="journals" value="a" data-price="45"> Series A: Statistics in Society, print (£45)</label>
              <label class="check"><input type="checkbox" name="journals" value="b" data-price="45"> Series B: Statistical Methodology, print (£45)</label>
              <label class="check"><input type="checkbox" name="journals" value="c" data-price="45"> Series C: Applied Statistics, print (£45)</label>
            </fieldset>
            <fieldset class="field"><legend>Newsletters (optional)</legend>
              <label class="check"><input type="checkbox" name="news" value="monthly" checked> RSS monthly news</label>
              <label class="check"><input type="checkbox" name="news" value="training"> Training and events</label>
              <label class="check"><input type="checkbox" name="news" value="policy"> Policy updates</label>
            </fieldset>
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue</button></div>
          </section>

          <section class="form-step" hidden>
            <h2>Payment</h2>
            <fieldset class="field"><legend>How would you like to pay?</legend>
              <label class="radio-card"><input type="radio" name="pay" value="card" required data-error="Choose how you would like to pay"> <strong>Card</strong>Pay the full year now</label>
              <label class="radio-card"><input type="radio" name="pay" value="dd" data-reveal="dd-options"> <strong>Direct Debit</strong>Annually or in instalments</label>
              <label class="radio-card"><input type="radio" name="pay" value="invoice" data-reveal="invoice-options"> <strong>Invoice my organisation</strong>We will send an invoice</label>
            </fieldset>
            <div class="reveal" id="dd-options" hidden>
              <fieldset class="field"><legend>Direct Debit schedule</legend>
                <label class="check"><input type="radio" name="dd" value="annual"> Annually</label>
                <label class="check"><input type="radio" name="dd" value="quarterly"> Quarterly instalments</label>
              </fieldset>
            </div>
            <div class="reveal" id="invoice-options" hidden>
              <div class="field"><label for="po">Purchase order number (optional)</label><input type="text" id="po" name="po"></div>
            </div>
            {n("Card payments redirect to the PCI DSS gateway (Elavon) and back. Direct Debit mandates and instalments are set up through Access Paysuite. Both write back to Dynamics.", "REQ-084, REQ-086, REQ-091", "Integration")}
            {n("Is joining by organisation invoice offered today? It is included here as an option to confirm.", "REQ-186", "Open question")}
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue</button></div>
          </section>

          <section class="form-step" hidden data-review>
            <h2>Check your answers</h2>
            <dl class="summary-list" data-summary></dl>
            <p><button class="btn-link" type="button" data-goto="0">Change membership</button> &middot; <button class="btn-link" type="button" data-goto="1">Change details</button></p>
            <div class="field"><label class="check"><input type="checkbox" name="declare" required data-error="Confirm that you agree to the Society's charter and code of conduct"> I agree to abide by the Society's charter, bylaws and code of conduct</label></div>
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="submit">Confirm and pay</button></div>
          </section>

          <section class="form-success" data-complete hidden>
            <h2>Welcome to the Royal Statistical Society</h2>
            <p>Your membership number is <strong>01234567</strong>. We have emailed your receipt and a welcome pack.</p>
            <p><a class="btn" href="~/pages/myrss.html">Go to MyRSS</a></p>
            {n("Payment confirmation page and email with an HMRC-compliant receipt. The onboarding email sequence starts, varying by member type. If someone leaves mid-application, an abandoned-application email follows.", "REQ-089, REQ-149, REQ-152, REQ-087")}
          </section>
        </form>

        <aside class="panel surface" aria-label="Your membership">
          <h2 class="h4">Your membership</h2>
          <p>Total to pay today: <strong data-total>£0</strong></p>
          <p class="wf-meta">Prices update as you choose. Annual fee for 2027.</p>
          <p><button class="btn-link" type="button">Save and finish later</button></p>
          {n("Save and resume emails a link to the saved application.", "REQ-082")}
          {n("RSS staff edit headings, hints and help text in the form builder without a developer, and can save forms as templates.", "REQ-083, REQ-098", "CMS")}
        </aside>
      </div>
'''
    page('join.html', 'Join the RSS', body, 'membership', [('Membership', '~/pages/membership.html'), ('Join', None)])


def build():
    home()
    search_page()
    advanced()
    membership()
    grades_fees()
    join()
