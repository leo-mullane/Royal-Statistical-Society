"""Professional development, events and training."""
from common import *


def pd_hub():
    n = Notes()
    body = f'''
      <section class="hub-hero">
        <div>
          <h1>Professional development</h1>
          <p class="lead">Professional status, CPD and accreditation for statisticians and data scientists, whether or not you are a member yet.</p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>
      {n("A use-based hub: a secondary home page for professional development, assembled from components. It sits at the top level rather than under Membership, because people look for CPD and status before they join.", "REQ-034, REQ-027")}

      <!-- Professional status (REQ-187, REQ-192) -->
      <section aria-labelledby="status">
        <h2 class="section-title" id="status">Professional status</h2>
        <div class="grid grid-4">
          <article class="card"><h3 class="card-title"><a href="~/pages/chartered-statistician.html">Chartered Statistician (CStat)</a></h3><p class="card-text">Qualifications plus five years' experience.</p></article>
          <article class="card"><h3 class="card-title"><a href="~/pages/chartered-statistician.html">Graduate Statistician (GradStat)</a></h3><p class="card-text">For graduates with a degree that meets our standard.</p></article>
          <article class="card"><h3 class="card-title"><a href="~/pages/chartered-statistician.html">Data Analyst</a></h3><p class="card-text">For people working with data, including apprentices.</p></article>
          <article class="card"><h3 class="card-title"><a href="~/pages/chartered-statistician.html">Data Science Professional</a></h3><p class="card-text">AdvDSP and DSP, awarded with the Alliance for Data Science Professionals.</p></article>
        </div>
      </section>

      <section class="grid grid-3" aria-label="CPD, accreditation and the register">
        <article class="card"><h2 class="card-title">CPD</h2><p class="card-text">Plan and record your continuing professional development in MyRSS, and download your record for any period.</p><a class="card-link" href="~/pages/myrss-cpd.html">Your CPD record</a></article>
        <article class="card"><h2 class="card-title">Accreditation</h2><p class="card-text">How universities and training providers get their programmes accredited.</p><a class="card-link" href="~/pages/accreditation.html">About accreditation</a></article>
        <article class="card"><h2 class="card-title">Professional Register</h2><p class="card-text">Check whether someone holds CStat, GradStat or Data Analyst status.</p><a class="card-link" href="~/pages/find-an-expert.html">Search the register</a></article>
      </section>

      <!-- Training cross-promotion (REQ-220) -->
      <section aria-labelledby="pd-courses">
        <h2 class="section-title" id="pd-courses">Courses that count towards CPD</h2>
        <ul class="stack">{"".join(f'<li><a href="~/pages/course.html">{e(x["title"])}</a> <span class="wf-meta">{drange(x["date"], x["end"])}, {fmt_label(x["fmt"])}, {e(x.get("level", ""))}</span></li>' for x in EVENTS if x["kind"] == "course" and x["date"] >= TODAY)}</ul>
        <p><a href="~/pages/events.html?type=course">All training courses &rarr;</a></p>
        {n("Pulled from the shared tags, so the hub stays current without editing.", "REQ-220, REQ-017")}
      </section>
'''
    page('professional-development.html', 'Professional development', body, 'professional-development', [('Professional development', None)])


def cstat():
    n = Notes()
    body = f'''
      <div class="with-sidenav">
        <nav class="sidenav" aria-label="Professional development">
          <h2>Professional development</h2>
          <ul>
            <li><a href="~/pages/professional-development.html">Overview</a></li>
            <li><a href="~/pages/chartered-statistician.html" aria-current="page">Chartered Statistician (CStat)</a></li>
            <li><a href="#">Graduate Statistician (GradStat)</a></li>
            <li><a href="#">Data Analyst</a></li>
            <li><a href="#">Data Science Professional</a></li>
            <li><a href="~/pages/myrss-cpd.html">CPD</a></li>
            <li><a href="~/pages/accreditation.html">Accreditation</a></li>
          </ul>
        </nav>
        <article>
          <h1>Chartered Statistician (CStat)</h1>
          <p class="lead">CStat is the Society's highest professional award. It shows employers and clients that you have the qualifications, experience and commitment to professional development of a senior statistician.</p>
          {n("Standard content page: left-hand section menu, rich text with headings, and reusable components (key facts, steps, accordion, call to action) placed by editors.", "REQ-029, REQ-013, REQ-014", "CMS")}
          <section class="panel surface">
            <h2 class="h4">At a glance</h2>
            <dl class="summary-list">
              <dt>Who it is for</dt><dd>Statisticians with an approved degree and at least five years of professional experience</dd>
              <dt>Fee</dt><dd>£[fee] application fee, then the CStat annual fee</dd>
              <dt>How long it takes</dt><dd>Usually 8 to 12 weeks from a complete application</dd>
              <dt>You will need</dt><dd>Degree certificate, CV, two referees, CPD record</dd>
            </dl>
          </section>
          <h2>How to apply</h2>
          <ol class="steps" aria-label="Steps to CStat"><li>Join as a Fellow</li><li>Apply in MyRSS</li><li>Assessment</li><li>Award</li></ol>
          <div class="prose">
            <p>You apply from MyRSS once you are a member. Your application is assessed by the Professional Affairs Committee, which may ask for more evidence.</p>
            <p>Once awarded, you will appear on the public Professional Register unless you choose not to.</p>
          </div>
          <p data-show-for="guest registered"><a class="btn" href="~/pages/join.html">Join, then apply</a></p>
          <p data-show-for="member lapsed" hidden><a class="btn" href="~/pages/myrss.html#applications">Start your application in MyRSS</a></p>
          {n("The button changes with the viewer: non-members are sent to join first; members go straight to the application in MyRSS.", "REQ-109, REQ-177")}
          <h2>Frequently asked questions</h2>
          <div class="accordion">
            <div class="accordion-item"><button class="accordion-title" type="button">My degree is not in statistics. Can I still apply? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>Yes, if your degree has enough statistical content. We assess each case.</p></div></div>
            <div class="accordion-item"><button class="accordion-title" type="button">What counts as professional experience? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>Work in which you apply statistical methods and take responsibility for the results.</p></div></div>
            <div class="accordion-item"><button class="accordion-title" type="button">How much CPD do I need to keep CStat? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>At least 30 hours a year, recorded in MyRSS.</p></div></div>
          </div>
          <div class="share-row" style="margin-top:2rem"><span class="wf-meta">Last reviewed 12 September 2026 by Professional Affairs</span></div>
          {n("Every page has a named owner and a review date; the owner is reminded when it falls due.", "REQ-143, REQ-122", "CMS")}
        </article>
      </div>
'''
    page('chartered-statistician.html', 'Chartered Statistician (CStat)', body, 'professional-development',
         [('Professional development', '~/pages/professional-development.html'), ('Chartered Statistician', None)])


def accreditation():
    n = Notes()
    body = f'''
      <div class="split">
        <article>
          <h1>Accreditation</h1>
          <p class="lead">We accredit university degrees and data science programmes that meet our standards, so that graduates can apply for GradStat or DSP status more easily.</p>
          <h2>Routes to accreditation</h2>
          <div class="grid grid-2">
            <article class="card"><h3 class="card-title">University accreditation</h3><p class="card-text">For undergraduate and master's degrees with substantial statistical content.</p></article>
            <article class="card"><h3 class="card-title">Alliance for Data Science Professionals (AfDSP)</h3><p class="card-text">For programmes that lead to Data Science Professional status.</p></article>
          </div>
          <h2>How it works</h2>
          <p>Tell us about your programme using the form. If it looks eligible, we will invite you to apply in the accreditation portal, where you can track your application and see past ones.</p>
          {n("Applications are made in a signed-in portal with admin pages for RSS staff and a review workflow for the Professional Affairs Committee: in progress, submitted, under review, approved. The portal is outside this first draft.", "REQ-190", "Behaviour")}
        </article>
        <!-- Expression of interest (REQ-191) -->
        <form class="panel" data-validate novalidate>
          <h2>Register your interest</h2>
          <div class="field"><label for="ac-name">Your name</label><input type="text" id="ac-name" name="name" required></div>
          <div class="field"><label for="ac-email">Work email</label><input type="email" id="ac-email" name="email" required></div>
          <div class="field"><label for="ac-org">University or provider</label><input type="text" id="ac-org" name="org" required></div>
          <div class="field"><label for="ac-route">Route</label><select id="ac-route" name="route" required><option value="">Choose a route</option><option>University accreditation</option><option>AfDSP</option><option>Not sure</option></select></div>
          <div class="field"><label for="ac-prog">Programme name and level (optional)</label><textarea id="ac-prog" name="programme" rows="3"></textarea></div>
          <button class="btn" type="submit">Send</button>
          <p class="form-success" hidden>Thank you. The accreditation team will reply within 10 working days.</p>
          {n("Spam protection and server-side validation on every public form.", "REQ-191, REQ-085")}
        </form>
      </div>
'''
    page('accreditation.html', 'Accreditation', body, 'professional-development',
         [('Professional development', '~/pages/professional-development.html'), ('Accreditation', None)])


def events_hub():
    n = Notes()
    up = [x for x in EVENTS if x['date'] >= TODAY and x['id'] != 'conference-2027']
    feat = [x for x in up if x.get('featured')][:3]
    body = f'''
      <section class="hub-hero">
        <div>
          <h1>Events and training</h1>
          <p class="lead">Discussion meetings, section and local group events, public courses and the annual conference, all in one place.</p>
          <form class="big-search" action="~/pages/events.html" role="search">
            <label for="hub-ev-q" class="visually-hidden">Find an event or course</label>
            <input type="search" id="hub-ev-q" name="q" placeholder="Find an event or course">
            <button class="btn" type="submit">Find</button>
          </form>
          <p class="chips"><a class="chip" href="~/pages/events.html?type=event">Events</a> <a class="chip" href="~/pages/events.html?type=course">Training courses</a> <a class="chip" href="~/pages/events.html?sub=discussion-meeting">Discussion meetings</a> <a class="chip" href="~/pages/events.html?fmt=online">Online</a> <a class="chip" href="~/pages/events.html?when=month">This month</a></p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>
      {n("Hub page for events and training. The chips open the finder already filtered, so a training newsletter can link straight to courses only.", "REQ-034, REQ-211")}

      <section aria-labelledby="ev-feat">
        <h2 class="section-title" id="ev-feat">Coming up</h2>
        <div class="grid grid-3">{"".join(f'<article class="card"><div class="wf-placeholder ratio-16-9">Image 16:9</div><p class="meta-row"><span class="tag">{e(x["sub"])}</span><span class="tag">{fmt_label(x["fmt"])}</span></p><h3 class="card-title"><a href="~/pages/{event_url(x)}">{e(x["title"])}</a></h3><p class="card-text">{drange(x["date"], x["end"])}</p></article>' for x in feat)}</div>
        <p><a href="~/pages/events.html">See all events and courses &rarr;</a></p>
      </section>

      <section class="content-highlight">
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
        <div><p class="meta-row"><span class="tag tag-strong">Conference</span></p><h2>RSS Conference 2027, Edinburgh</h2><p>6 to 9 September 2027. Early-bird booking is open.</p><a class="btn" href="~/pages/conference.html">Conference programme and booking</a></div>
      </section>

      <section id="recordings" aria-labelledby="rec-title">
        <h2 class="section-title" id="rec-title">Recordings</h2>
        <div class="grid grid-3">
          <article class="card"><div class="wf-placeholder ratio-16-9">Video 16:9</div><h3 class="card-title"><a href="~/pages/event.html">Statistics and the climate emergency</a></h3><p class="card-text">Discussion meeting, 14 October 2026</p></article>
          <article class="card"><div class="wf-placeholder ratio-16-9">Video 16:9</div><h3 class="card-title"><a href="#">Presidential address 2026</a></h3><p class="card-text">RSS Conference, Brighton</p></article>
          <article class="card"><div class="wf-placeholder ratio-16-9">Video 16:9</div><h3 class="card-title"><a href="#">Careers in official statistics</a></h3><p class="card-text">Young Statisticians Section</p></article>
        </div>
        {n("Pulled from the RSS YouTube channel and played on the site, with captions. Some recordings are members only.", "REQ-107, REQ-183")}
      </section>

      <section class="grid grid-2" id="in-house">
        <article class="card"><h2 class="card-title">In-house training</h2><p class="card-text">Any of our courses can be run for your team, online or at your offices.</p><a class="card-link" href="~/pages/about.html#contact">Ask about in-house training</a></article>
        <article class="card"><h2 class="card-title">Running a section or group event?</h2><p class="card-text">Submit it for the calendar. Free and charged events are both welcome.</p><a class="card-link" href="~/pages/submit-event.html">Submit an event</a></article>
      </section>
'''
    page('events-training.html', 'Events and training', body, 'events-training', [('Events and training', None)])


def finder():
    n = Notes()
    items = ''
    for x in sorted(EVENTS, key=lambda v: v['date']):
        dt = x['date']
        y, m, dd = dt.split('-')
        text = f"{x['title']} {x['summary']} {x['org']} {x.get('sub', '')} {x.get('level', '')} {' '.join(TOPICS[t] for t in x['topics'])}"
        places = f'<p><strong>{e(x["places"])}</strong></p>' if x.get('places') else ''
        rec = '<p><span class="tag">Recording available</span></p>' if x.get('recording') else ''
        level = f'<span class="tag">{e(x["level"])}</span>' if x.get('level') else ''
        short = trunc(x['title'].split(':')[-1].strip(), 34)
        snapshot = f"{x['title']}. {drange(x['date'], x['end'])}. {x['time']}. {fmt_label(x['fmt'])}. {x['price']}"
        items += f'''
            <article class="list-item" data-item data-kind="{x['kind']}" data-type="{x['kind']}" data-topic="{' '.join(x['topics'])}" data-fmt="{x['fmt']}" data-sub="{slug(x.get('sub', ''))}" data-audience="{' '.join(x['aud'])}"
              data-date="{x['date']}" data-end="{x['end']}" data-title="{e(x['title'])}" data-text="{e(text)}" data-short="{e(short)}" data-snapshot="{e(snapshot)}">
              <div class="date-block" aria-hidden="true"><span class="d">{int(dd)}</span><span class="m">{MONTHS[int(m)-1][:3]} {y}</span></div>
              <div>
                <p class="meta-row"><span class="tag">{'Training course' if x['kind'] == 'course' else e(x['sub'])}</span><span class="tag">{fmt_label(x['fmt'])}</span>{level}</p>
                <h3><a href="~/pages/{event_url(x)}">{e(x['title'])}</a></h3>
                <p>{e(x['summary'])}</p>
                <p class="meta-row"><span>{drange(x['date'], x['end'])}, {e(x['time'])}</span><span>{e(x['place'])}</span><span>{e(x['price'])}</span><span>Organised by {e(x['org'])}</span></p>
                {places}{rec}
              </div>
              <div class="list-actions"><a class="btn btn-small" href="~/pages/{event_url(x)}">{'Book' if x['end'] >= TODAY else 'View'}</a></div>
            </article>'''
    topic_checks = ''.join(f'<label class="check"><input type="checkbox" data-filter="topic" value="{k}"> {e(v)}</label>' for k, v in TOPICS.items())
    subs = sorted({x['sub'] for x in EVENTS})
    sub_checks = ''.join(f'<label class="check"><input type="checkbox" data-filter="sub" value="{slug(s)}"> {e(s)}</label>' for s in subs)
    aud_checks = ''.join(f'<label class="check"><input type="checkbox" data-filter="audience" value="{k}"> {e(v)}</label>' for k, v in AUDIENCES.items() if k in ('professionals', 'students', 'educators', 'policymakers', 'public'))
    body = f'''
      <h1>Find an event or course</h1>
      <p class="lead">Events, discussion meetings and training courses in one list.</p>
      <!-- Combined events and training finder (REQ-211, REQ-031, REQ-210) -->
      <section data-listing data-page-size="8">
        <form class="big-search" role="search">
          <label for="ev-q" class="visually-hidden">Search events and courses</label>
          <input type="search" id="ev-q" data-filter="q" placeholder="Search by keyword, speaker or organiser">
          <button class="btn" type="submit">Search</button>
        </form>
        {n("Event type separates discussion meetings, section and local group meetings, public lectures and courses, so the menu can link straight to <a href=\'?sub=discussion-meeting\'>discussion meetings</a>. It comes from the event record, not the CRM category.", "REQ-211, REQ-031")}
        {n("One finder for events and training. Filters are topic, format, audience, type and date, using the shared taxonomy. CRM categories ('Section Group Meeting', 'Other Event (non-RSS)') are kept behind the scenes as an 'organiser' field.", "REQ-211, REQ-031, REQ-213, REQ-017")}
        <div class="finder">
          <aside class="facets" aria-label="Filter events and courses">
            <fieldset class="facet"><legend>Type</legend>
              <label class="check"><input type="checkbox" data-filter="type" value="event"> Events</label>
              <label class="check"><input type="checkbox" data-filter="type" value="course"> Training courses</label>
            </fieldset>
            <fieldset class="facet"><legend>Event type</legend>{sub_checks}</fieldset>
            <div class="facet field"><label for="ev-when" class="facet-title">When</label>
              <select id="ev-when" data-filter="when"><option value="upcoming">Upcoming</option><option value="month">Next 30 days</option><option value="quarter">Next three months</option><option value="past">Past events</option><option value="">Any time</option></select></div>
            <fieldset class="facet"><legend>Format</legend>
              <label class="check"><input type="checkbox" data-filter="fmt" value="in-person"> In person</label>
              <label class="check"><input type="checkbox" data-filter="fmt" value="online"> Online</label>
              <label class="check"><input type="checkbox" data-filter="fmt" value="hybrid"> Hybrid</label>
            </fieldset>
            <fieldset class="facet"><legend>Topic</legend>{topic_checks}</fieldset>
            <fieldset class="facet"><legend>Who it is for</legend>{aud_checks}</fieldset>
          </aside>
          <div>
            <div class="results-bar">
              <p class="result-count" data-count aria-live="polite"></p>
              <button class="btn btn-secondary btn-small facets-toggle" type="button" data-facets-toggle aria-expanded="false">Filters</button>
              <div class="field"><label for="ev-sort">Sort</label><select id="ev-sort" data-list-sort><option value="soonest">Soonest first</option><option value="latest">Latest first</option><option value="title">Title A to Z</option></select></div>
              <div class="view-switch" role="group" aria-label="View"><button type="button" data-view="list" aria-pressed="true">List</button><button type="button" data-view="calendar" aria-pressed="false">Calendar</button></div>
            </div>
            <div class="active-filters" data-chips></div>
            <div data-list-view>
              <div>{items}
              </div>
              <p class="empty-state" data-empty hidden>No events or courses match. Try removing a filter, or <a href="~/pages/events.html?when=past">look at past events</a>.</p>
              <p style="text-align:center;margin-top:1.5rem"><button class="btn btn-secondary" type="button" data-more>Show more</button></p>
            </div>
            <div data-calendar hidden>
              <div class="calendar-head"><button class="btn btn-secondary btn-small" type="button" data-cal-step="-1">&lsaquo; Previous</button><h2 data-cal-label>November 2026</h2><button class="btn btn-secondary btn-small" type="button" data-cal-step="1">Next &rsaquo;</button></div>
              <div class="calendar-grid" data-cal-grid></div>
              <p class="cal-legend"><span class="cal-item event">Event</span><span class="cal-item course">Training course</span></p>
              {n("Month view with the same filters. Each item shows a quick snapshot on hover or focus and links to the full listing. Events and courses are told apart by a pattern here; in design, by colour.", "REQ-210, REQ-212")}
            </div>
            {n("Each event appears once whatever its format, tagged Hybrid where it is. Multi-day courses appear once, not on every day. Fully booked courses stay listed with a waiting list.", "REQ-201, REQ-218, REQ-223")}
          </div>
        </div>
      </section>
'''
    page('events.html', 'Find an event or course', body, 'events-training', [('Events and training', '~/pages/events-training.html'), ('Find an event or course', None)])


def event():
    n = Notes()
    ev = EVENTS[0]
    body = f'''
      <article>
        <p class="meta-row"><span class="tag">{e(ev["sub"])}</span><span class="tag tag-strong">Hybrid event</span>{tags(ev["topics"])}</p>
        <h1>{e(ev["title"])}</h1>
        <div class="split">
          <div>
            <p class="lead">{e(ev["summary"])}</p>
            <!-- Event details in tabs (REQ-209) -->
            <div class="tabs" role="tablist">
              <button class="tab active" type="button" data-tab="ev-about">About</button>
              <button class="tab" type="button" data-tab="ev-speakers">Speakers</button>
              <button class="tab" type="button" data-tab="ev-organiser">Organiser</button>
              <button class="tab" type="button" data-tab="ev-costs">Costs</button>
            </div>
            <div>
              <div class="tab-panel active" id="ev-about">
                <div class="prose">
                  <p>Large language models are increasingly evaluated on benchmark datasets, often with little attention to sampling, uncertainty or the dependence between test items. The paper proposes a statistical framework for evaluation and shows how conclusions change when uncertainty is taken into account.</p>
                  <p>The paper will be published in Series A with the discussion. Written contributions can be submitted for two weeks after the meeting.</p>
                </div>
                <div class="wf-placeholder embed">Embedded map: Errol Street, London</div>
              </div>
              <div class="tab-panel" id="ev-speakers"><div class="grid grid-2">
                <div class="card"><div class="wf-placeholder avatar">Photo</div><h3 class="card-title">Dr Imogen Hale</h3><p class="card-text">Author, University of Eastwick</p></div>
                <div class="card"><div class="wf-placeholder avatar">Photo</div><h3 class="card-title">Professor Daniel Mensah</h3><p class="card-text">Proposer of the vote of thanks</p></div>
              </div></div>
              <div class="tab-panel" id="ev-organiser"><p>Organised by the Royal Statistical Society. Questions: <a href="#">events@rss.org.uk</a></p></div>
              <div class="tab-panel" id="ev-costs"><p>Free for everyone. Booking is required for both in-person and online places.</p></div>
            </div>
            {n("Tabbed detail for speakers, organiser and costs, as asked for in the events specification. Tabs stack as sections on mobile.", "REQ-209, REQ-103")}
            <div class="share-row"><span class="wf-meta">Share:</span><a href="#">LinkedIn</a><a href="#">Bluesky</a><a href="#">Email</a><button class="btn-link" type="button" data-copy-link>Copy link</button></div>
            {n("Share links use an automatically generated card: title, date and image.", "REQ-105, REQ-057")}
          </div>
          <!-- Booking panel with one button per format (REQ-201, REQ-202, REQ-206) -->
          <aside class="panel surface" aria-label="Book a place">
            <dl class="summary-list">
              <dt>Date</dt><dd>{weekday(ev["date"])} {d(ev["date"])}</dd>
              <dt>Time</dt><dd>{e(ev["time"])}</dd>
              <dt>Where</dt><dd>{e(ev["place"])}</dd>
              <dt>Cost</dt><dd>{e(ev["price"])}</dd>
            </dl>
            <p><a class="btn btn-block" href="~/pages/book.html?format=in-person">Attend in person</a></p>
            <p><a class="btn btn-block btn-secondary" href="~/pages/book.html?format=online">Join online</a></p>
            <p class="wf-meta">Online joining details are emailed the day before.</p>
            <p><a href="#">Add to calendar</a></p>
            {n("One event page whatever the format, with a booking button per option. Each button links to its own booking endpoint in Dynamics. For free events the confirmation email leaves out payment wording.", "REQ-201, REQ-202, REQ-206, REQ-207")}
          </aside>
        </div>
      </article>
      <section aria-labelledby="related">
        <h2 class="section-title" id="related">You might also like</h2>
        <div class="grid grid-3">
          <article class="card"><p class="meta-row"><span class="tag">Discussion meeting</span></p><h3 class="card-title"><a href="~/pages/event.html">Causal inference from observational data</a></h3><p class="card-text">27 January 2027</p></article>
          <article class="card"><p class="meta-row"><span class="tag">Training course</span></p><h3 class="card-title"><a href="~/pages/course.html">Introduction to machine learning</a></h3><p class="card-text">1 to 3 December 2026</p></article>
          <article class="card"><p class="meta-row"><span class="tag">Policy</span></p><h3 class="card-title"><a href="~/pages/campaign.html">Statistics and AI: what the public should expect</a></h3><p class="card-text">Report, September 2026</p></article>
        </div>
        {n("Related events, courses and articles come from the shared tags.", "REQ-220, REQ-027")}
      </section>
'''
    page('event.html', ev['title'], body, 'events-training', [('Events and training', '~/pages/events-training.html'), ('Events', '~/pages/events.html?type=event'), ('Discussion meeting', None)])


def course():
    n = Notes()
    dates = [('2026-11-10', '2026-11-11', 'Online', 'Places available'), ('2027-02-16', '2027-02-17', 'Online', 'Places available'), ('2027-04-20', '2027-04-21', 'In person, London', 'Few places left')]
    radios = ''.join(f'<label class="radio-card"><input type="radio" name="date" value="{a}" data-date-choice="{drange(a, b)}"{" checked" if i == 0 else ""}> <strong>{drange(a, b)}</strong>{fmt} &middot; {st}</label>' for i, (a, b, fmt, st) in enumerate(dates))
    body = f'''
      <article>
        <p class="meta-row"><span class="tag">Training course</span><span class="tag">Foundation</span><span class="tag">Online and in person</span><span class="tag">12 CPD hours</span><span class="tag">Quality Mark</span></p>
        <h1>Introduction to R</h1>
        <div class="split">
          <div class="prose">
            <p class="lead">Import, tidy, summarise and plot data in R, with practical exercises throughout. No previous programming needed.</p>
            <h2>What you will learn</h2>
            <ul><li>Read data from spreadsheets and databases</li><li>Reshape and summarise data with the tidyverse</li><li>Make clear, reproducible charts</li><li>Write simple functions and scripts</li></ul>
            <h2>Who it is for</h2>
            <p>Analysts and researchers who use spreadsheets or point-and-click software and want to move to code.</p>
            <h2>Your tutor</h2>
            <div class="content-highlight"><div class="wf-placeholder avatar">Photo</div><p><strong>Dr Ruth Kamara</strong> has taught R to more than 2,000 analysts in government and the NHS.</p></div>
            <h2>What past delegates said</h2>
            <blockquote class="wf-quote"><p>"Practical and well paced. I used it at work the following Monday."</p><cite>Delegate, March 2026</cite></blockquote>
            {n("Course content comes from Dynamics: description, outcomes, tutor, price and every date. Unpublishing a course in the CMS keeps its history for delegates' records.", "REQ-213, REQ-214, REQ-222", "Integration")}
          </div>
          <!-- All dates and prices on one page (REQ-214) -->
          <aside class="panel surface" aria-label="Choose a date">
            <h2 class="h4">Choose a date</h2>
            <form><fieldset class="field"><legend class="visually-hidden">Course dates</legend><div class="stack">{radios}</div></fieldset></form>
            <dl class="summary-list"><dt>Members</dt><dd>£345</dd><dt>Non-members</dt><dd>£460</dd></dl>
            <p data-show-for="member" hidden class="wf-meta">You will pay the member rate.</p>
            <p><a class="btn btn-block" href="~/pages/book.html">Book <span data-chosen-date>10 to 11 November 2026</span></a></p>
            <p><button class="btn btn-block btn-secondary" type="button" data-add-basket="Introduction to R|10 to 11 November 2026, online|345">Add to basket</button><span class="wf-meta" data-added hidden>Added. <a href="~/pages/basket.html">View basket</a></span></p>
            <p><a href="#">Join the waiting list for a full date</a></p>
            {n("Every date and price on one page, so nobody has to move between pages to compare. A full date offers a waiting list, synced with Dynamics.", "REQ-214, REQ-218, REQ-094")}
          </aside>
        </div>
      </article>
      <section aria-labelledby="also">
        <h2 class="section-title" id="also">Related courses</h2>
        <div class="grid grid-3">{"".join(f'<article class="card"><p class="meta-row"><span class="tag">{e(x.get("level", ""))}</span><span class="tag">{fmt_label(x["fmt"])}</span></p><h3 class="card-title"><a href="~/pages/course.html">{e(x["title"])}</a></h3><p class="card-text">{drange(x["date"], x["end"])}</p></article>' for x in EVENTS if x["kind"] == "course" and x["id"] in ("dataviz", "bayes-stan", "intro-ml"))}</div>
        {n("Cross-sell from shared tags across CMS and CRM.", "REQ-220")}
      </section>
'''
    page('course.html', 'Introduction to R', body, 'events-training', [('Events and training', '~/pages/events-training.html'), ('Training courses', '~/pages/events.html?type=course'), ('Introduction to R', None)])


def book():
    n = Notes()
    body = f'''
      <h1>Book: Introduction to R</h1>
      <p class="lead">10 to 11 November 2026, online</p>
      <ol class="steps" aria-label="Booking progress"><li>Who is attending</li><li>Delegate details</li><li>Your organisation</li><li>Check and pay</li></ol>
      {n("Booking for yourself or for others, with the booker and each delegate kept separate. Delegates get their own account so the course appears in their MyRSS.", "REQ-215, REQ-216, REQ-204")}
      <div class="split">
        <form data-steps data-pay-for="course" data-pay-amount="345" data-pay-desc="Introduction to R, 10 to 11 November 2026, online" novalidate>
          <section class="form-step">
            <h2>Who is attending?</h2>
            <fieldset class="field"><legend>I am booking for</legend>
              <label class="radio-card"><input type="radio" name="who" value="me" required data-error="Choose who you are booking for"> <strong>Myself</strong>We will use your MyRSS details</label>
              <label class="radio-card"><input type="radio" name="who" value="others" data-reveal="others-note"> <strong>Someone else, or a group</strong>You pay; each delegate gets the joining details</label>
            </fieldset>
            <div class="reveal" id="others-note" hidden><p>You will add each delegate on the next step. We will create a basic account for each delegate and tell them why.</p>
              <div class="field"><label for="b-count">Number of delegates</label><select id="b-count" name="count"><option>1</option><option>2</option><option>3</option><option>4</option><option>5 or more</option></select></div></div>
            <div class="form-nav"><span></span><button class="btn" type="button" data-next>Continue</button></div>
          </section>
          <section class="form-step" hidden>
            <h2>Delegate details</h2>
            <div class="field-row">
              <div class="field"><label for="b-first">Delegate first name</label><input type="text" id="b-first" name="dfirst" required></div>
              <div class="field"><label for="b-last">Delegate last name</label><input type="text" id="b-last" name="dlast" required></div>
            </div>
            <div class="field"><label for="b-email">Delegate email</label><input type="email" id="b-email" name="demail" required></div>
            <div class="field"><label for="b-needs">Access or dietary requirements (optional)</label><textarea id="b-needs" name="needs" rows="3"></textarea></div>
            <div class="field"><label for="b-heard">How did you hear about this course? (optional)</label><select id="b-heard" name="heard"><option value="">Choose one</option><option>RSS newsletter</option><option>Colleague</option><option>Search engine</option><option>Social media</option><option>Employer</option></select></div>
            {n("Fields come from a reusable registration template with event-specific extras (catering, accessibility). Extra fields not held in Dynamics are stored for the organiser or emailed to them.", "REQ-204, REQ-205, REQ-216")}
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue</button></div>
          </section>
          <section class="form-step" hidden>
            <h2>Your organisation</h2>
            <div class="field"><label for="b-org">Organisation (optional)</label><input type="text" id="b-org" name="org"></div>
            <fieldset class="field"><legend>Payment</legend>
              <label class="check"><input type="radio" name="pay" value="card" required data-error="Choose how to pay"> Card</label>
              <label class="check"><input type="radio" name="pay" value="invoice" data-reveal="po-field"> Invoice or purchase order</label>
            </fieldset>
            <div class="reveal" id="po-field" hidden><div class="field"><label for="b-po">Purchase order number</label><input type="text" id="b-po" name="po"></div></div>
            {n("Is booking by invoice or purchase order offered today? ClerksWell has suggested it (REQ-290, a Could).", "REQ-290", "Open question")}
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue</button></div>
          </section>
          <section class="form-step" hidden data-review>
            <h2>Check and pay</h2>
            <div data-summary></div>
            <div class="field"><label for="b-code">Discount code (optional)</label><div class="inline-field"><input type="text" id="b-code" name="code"><button class="btn btn-secondary btn-small" type="button">Apply</button></div></div>
            {n("Discount codes are entered here and validated with the payment provider. Member and early-bird prices are applied automatically.", "REQ-217, REQ-087")}
            <div class="field"><label class="check"><input type="checkbox" name="terms" required data-error="Accept the booking terms"> I accept the <a href="#">booking terms and cancellation policy</a></label></div>
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="submit">Continue to payment: £345</button></div>
          </section>
          <section class="form-success" data-complete hidden>
            <h2>Booking confirmed</h2>
            <p>We have emailed a receipt to you and joining instructions to the delegate. The course now appears in My Training.</p>
            <p><a class="btn" href="~/pages/myrss-bookings.html">View in MyRSS</a></p>
            {n("If the booker leaves before paying, an abandoned-booking reminder is sent.", "REQ-221, REQ-089")}
          </section>
        </form>
        <aside class="panel surface"><h2 class="h4">Your booking</h2><p><strong>Introduction to R</strong><br>10 to 11 November 2026, online</p><p>Member price: £345</p></aside>
      </div>
'''
    page('book.html', 'Book a course', body, 'events-training', [('Events and training', '~/pages/events-training.html'), ('Introduction to R', '~/pages/course.html'), ('Book', None)])


def basket_page():
    n = Notes()
    body = f'''
      <h1>Your basket</h1>
      {n("A persistent basket so several courses, events and conference add-ons can be bought in one payment. It is kept for signed-in users across visits. Add a course from the <a href=\'course.html\'>course page</a> to try it.", "REQ-094, REQ-008")}
      <div class="split">
        <div data-basket-list></div>
        <aside class="panel surface">
          <dl class="summary-list"><dt>Subtotal</dt><dd data-basket-sub>£0.00</dd><dt>Discount</dt><dd data-basket-discount>£0.00</dd><dt>VAT</dt><dd>£0.00</dd><dt>Total</dt><dd><strong data-basket-total>£0</strong></dd></dl>
          <form data-promo-form>
            <div class="field"><label for="promo">Voucher or promo code</label><div class="inline-field"><input type="text" id="promo" name="code"><button class="btn btn-secondary btn-small" type="submit">Apply</button></div><p class="field-hint" data-promo-msg aria-live="polite">Try MEMBER10</p></div>
          </form>
          <p><button class="btn btn-block" type="button" data-checkout>Checkout and pay</button></p>
          {n("Pricing logic covers member grade, early-bird and late rates, concessions, bundles, codes and VAT. A downloadable receipt follows payment.", "REQ-087, REQ-116")}
        </aside>
      </div>
'''
    page('basket.html', 'Your basket', body, '', [('Basket', None)])


def conference():
    n = Notes()
    days = [
        ('Monday 6 September', [('09:00', 'Registration and welcome'), ('10:00', 'Plenary: The future of official statistics'), ('11:30', 'Parallel sessions: methods, health, data science')]),
        ('Tuesday 7 September', [('09:00', 'Plenary: Statistics and AI'), ('11:00', 'Workshops'), ('19:00', 'Conference dinner')]),
        ('Wednesday 8 September', [('09:00', 'Presidential address'), ('11:00', 'Poster session'), ('14:00', 'Parallel sessions')]),
        ('Thursday 9 September', [('09:00', 'Plenary: Statistics in public health'), ('12:30', 'Close')]),
    ]
    acc = ''.join(f'<div class="accordion-item"><button class="accordion-title" type="button">{day} <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><table class="data-table"><tbody>{"".join(f"<tr><th scope=row>{t}</th><td>{e(s)}</td></tr>" for t, s in sess)}</tbody></table></div></div>' for day, sess in days)
    body = f'''
      <!-- Conference landing page (REQ-224, REQ-225, REQ-226) -->
      <section class="hub-hero">
        <div>
          <p class="meta-row"><span class="tag tag-strong">Conference</span></p>
          <h1>RSS Conference 2027</h1>
          <p class="lead">Edinburgh International Conference Centre, 6 to 9 September 2027. More than 500 talks, workshops and posters.</p>
          <p><a class="btn" href="#tickets">Book now</a> <a class="btn btn-secondary" href="#programme">See the programme</a></p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image or video 16:9</div>
      </section>
      {n("'Book now' is the primary call to action, high contrast and repeated at key points down the page.", "REQ-225")}
      <nav class="audience-strip" aria-label="On this page"><a href="#key-dates">Key dates</a><a href="#speakers">Speakers</a><a href="#programme">Programme</a><a href="#tickets">Tickets</a><a href="#attending">Attending</a><a href="#sponsors">Sponsors</a><a href="#future">Future conferences</a></nav>

      <section class="grid grid-3" id="key-dates" aria-label="Key dates">
        <div class="stat-item"><div class="stat-value">15 Jan</div><div class="stat-title">Call for talks opens</div></div>
        <div class="stat-item"><div class="stat-value">31 Mar</div><div class="stat-title">Early-bird booking closes</div></div>
        <div class="stat-item"><div class="stat-value">6 Sep</div><div class="stat-title">Conference opens</div></div>
      </section>
      {n("Programme summary, keynote speakers and key dates sit near the top.", "REQ-226")}

      <section class="panel" aria-labelledby="updates-title">
        <h2 class="h4" id="updates-title">Conference updates</h2>
        <ul class="stack"><li><strong>18 September 2026</strong> First three keynote speakers confirmed.</li><li><strong>1 September 2026</strong> Dates and venue announced.</li></ul>
        {n("A light updates block editors change in place, without writing a news article.", "REQ-229", "CMS")}
      </section>

      <section id="speakers" aria-labelledby="sp-title">
        <h2 class="section-title" id="sp-title">Keynote speakers</h2>
        <div class="grid grid-3">
          <div class="card"><div class="wf-placeholder avatar">Photo</div><h3 class="card-title">Keynote speaker 1</h3><p class="card-text">Official statistics</p></div>
          <div class="card"><div class="wf-placeholder avatar">Photo</div><h3 class="card-title">Keynote speaker 2</h3><p class="card-text">Statistics and AI</p></div>
          <div class="card"><div class="wf-placeholder avatar">Photo</div><h3 class="card-title">Keynote speaker 3</h3><p class="card-text">Public health</p></div>
        </div>
      </section>

      <section id="programme" aria-labelledby="prog-title">
        <h2 class="section-title" id="prog-title">Programme</h2>
        <div class="accordion">{acc}</div>
        {n("Programme by day, session and detail in an accordion. The embedded programme tool is Phase 2 in the SoW, so the accordion is the launch option.", "REQ-228")}
      </section>

      <section id="tickets" aria-labelledby="t-title">
        <h2 class="section-title" id="t-title">Tickets</h2>
        <div class="table-wrap"><table class="data-table">
          <thead><tr><th scope="col">Ticket</th><th scope="col">Includes</th><th scope="col">Member</th><th scope="col">Non-member</th><th scope="col"></th></tr></thead>
          <tbody>
            <tr><th scope="row">Full conference</th><td>All sessions, lunches, refreshments, welcome reception</td><td>£595</td><td>£795</td><td><button class="btn btn-small" type="button" data-add-basket="RSS Conference 2027: full|6 to 9 September 2027|595">Add</button></td></tr>
            <tr><th scope="row">Day ticket</th><td>One day, lunch and refreshments</td><td>£225</td><td>£295</td><td><button class="btn btn-small" type="button" data-add-basket="RSS Conference 2027: day ticket|Choose your day at checkout|225">Add</button></td></tr>
            <tr><th scope="row">Student</th><td>All sessions and lunches</td><td>£295</td><td>£345</td><td><button class="btn btn-small" type="button" data-add-basket="RSS Conference 2027: student|6 to 9 September 2027|295">Add</button></td></tr>
            <tr><th scope="row">Optional: conference dinner</th><td>Tuesday evening</td><td>£85</td><td>£85</td><td><button class="btn btn-small" type="button" data-add-basket="Conference dinner|7 September 2027|85">Add</button></td></tr>
          </tbody></table></div>
        <p><span data-added hidden></span><a class="btn" href="~/pages/basket.html">Book now</a></p>
        {n("What each ticket includes and the price of every extra are shown before checkout.", "REQ-230, REQ-087")}
      </section>

      <section id="attending" aria-labelledby="att-title">
        <h2 class="section-title" id="att-title">Attending</h2>
        <div class="grid grid-3">
          <article class="card"><h3 class="card-title">Venue and travel</h3><p class="card-text">Getting to the EICC, accessibility and accommodation.</p></article>
          <article class="card"><h3 class="card-title">Conference app</h3><p class="card-text">Download the app for your personal timetable. <a href="#">App Store</a> &middot; <a href="#">Google Play</a></p></article>
          <article class="card"><h3 class="card-title">FAQs</h3><p class="card-text">Childcare, quiet room, dietary needs, refunds.</p></article>
        </div>
        {n("Attendee information: the app, logistics and FAQs.", "REQ-227")}
      </section>

      <section id="sponsors" aria-labelledby="spn-title">
        <h2 class="section-title" id="spn-title">Sponsors and exhibitors</h2>
        <div class="grid grid-4">{"".join('<div class="wf-placeholder logo">Sponsor logo</div>' for _ in range(8))}</div>
        <p><a href="#">Committee and organisers</a></p>
        {n("Named non-developer owners upload sponsor logos, with size guidance and automatic optimisation. The Conference Board is listed on its own page.", "REQ-231, REQ-232", "CMS")}
      </section>

      <section id="future" aria-labelledby="fut-title">
        <h2 class="section-title" id="fut-title">Future and past conferences</h2>
        <table class="data-table"><thead><tr><th scope="col">Year</th><th scope="col">Where</th><th scope="col">When</th></tr></thead>
          <tbody><tr><td>2027</td><td>Edinburgh</td><td>6 to 9 September</td></tr><tr><td>2028</td><td>Venue to be announced</td><td>September</td></tr><tr><td>2029</td><td>Venue to be announced</td><td>September</td></tr><tr><td>2030</td><td>Venue to be announced</td><td>September</td></tr></tbody></table>
        <p><a href="#">Past conferences archive</a></p>
        {n("The next four years, plus an archive of past conferences.", "REQ-233")}
      </section>
'''
    page('conference.html', 'RSS Conference 2027', body, 'events-training', [('Events and training', '~/pages/events-training.html'), ('RSS Conference 2027', None)])


def submit_event():
    n = Notes()
    groups = ''.join(f'<option>{e(g["title"])}</option>' for g in GROUPS)
    topic_checks = ''.join(f'<label class="check"><input type="checkbox" name="topics" value="{k}"> {e(v)}</label>' for k, v in TOPICS.items())
    body = f'''
      <h1>Submit a group event</h1>
      <p class="lead">For sections, special interest groups and local groups. Events appear on the calendar once approved.</p>
      <p data-show-for="guest" class="locked">You need to <a href="~/pages/sign-in.html">sign in</a> as a group officer to submit an event. Use <strong>View as</strong> to see the form.</p>
      {n("Only group officers can submit. Approved events appear in the events finder and on the group's own page.", "REQ-203, REQ-102")}
      <form class="form-step" data-validate novalidate data-show-for="registered member lapsed" hidden>
        <div class="field"><label for="se-group">Group</label><select id="se-group" name="group" required><option value="">Choose your group</option>{groups}</select></div>
        <div class="field"><label for="se-title">Event title</label><input type="text" id="se-title" name="title" required></div>
        <div class="field-row">
          <div class="field"><label for="se-date">Date</label><input type="date" id="se-date" name="date" required></div>
          <div class="field"><label for="se-time">Start and end time</label><input type="text" id="se-time" name="time" required placeholder="18:30 to 20:00"></div>
        </div>
        <fieldset class="field"><legend>Format</legend>
          <label class="check"><input type="radio" name="fmt" value="in-person" required data-error="Choose a format"> In person</label>
          <label class="check"><input type="radio" name="fmt" value="online"> Online</label>
          <label class="check"><input type="radio" name="fmt" value="hybrid"> Hybrid</label>
        </fieldset>
        <fieldset class="field"><legend>Is there a charge?</legend>
          <label class="check"><input type="radio" name="charge" value="free" required data-error="Tell us whether the event is free"> Free</label>
          <label class="check"><input type="radio" name="charge" value="paid" data-reveal="charge-detail"> Charged</label>
        </fieldset>
        <div class="reveal" id="charge-detail" hidden>
          <div class="field"><label for="se-price">Prices (member and non-member)</label><input type="text" id="se-price" name="price"></div>
          {n("How are charged group events paid for, and where is extra registration information stored?", "REQ-203, REQ-205", "Open question")}
        </div>
        <fieldset class="field"><legend>Topics</legend>{topic_checks}</fieldset>
        <div class="field"><label for="se-desc">Description</label><textarea id="se-desc" name="desc" rows="5" required></textarea></div>
        <div class="field"><label for="se-file">Flyer or programme (optional)</label><input type="file" id="se-file" name="file" accept=".pdf,.docx,.jpg,.png"><p class="field-hint">PDF, DOCX, JPG or PNG, up to 25 MB.</p></div>
        {n("Uploads accept only approved file types and sizes; names are normalised and double extensions rejected.", "REQ-254, REQ-255, REQ-257")}
        <button class="btn" type="submit">Submit for approval</button>
        <p class="form-success" hidden>Thank you. The events team will review your event within three working days.</p>
      </form>
'''
    page('submit-event.html', 'Submit a group event', body, 'events-training', [('Events and training', '~/pages/events-training.html'), ('Submit a group event', None)])


def build():
    pd_hub()
    cstat()
    accreditation()
    events_hub()
    finder()
    event()
    course()
    book()
    basket_page()
    conference()
    submit_event()
