"""Professional development, events and training."""
from common import *


QUALS = [
    dict(file='chartered-statistician.html', title='Chartered Statistician (CStat)', short='Chartered Statistician', grade='cstat',
         lead="CStat is the Society's highest professional award. It shows employers and clients that you have the qualifications, experience and commitment to professional development of a senior statistician.",
         who='Statisticians with an approved degree and at least five years of professional experience', fee='£[fee] application fee, then the CStat annual fee',
         time='Usually 8 to 12 weeks from a complete application', need='Degree certificate, CV, two referees, CPD record',
         faqs=[("My degree is not in statistics. Can I still apply?", "Yes, if your degree has enough statistical content. We assess each case."),
               ("What counts as professional experience?", "Work in which you apply statistical methods and take responsibility for the results."),
               ("How much CPD do I need to keep CStat?", "At least 30 hours a year, recorded in MyRSS.")]),
    dict(file='graduate-statistician.html', title='Graduate Statistician (GradStat)', short='Graduate Statistician', grade='gradstat',
         lead='GradStat recognises a degree that meets our academic standard. It is the usual first step towards becoming a Chartered Statistician.',
         who='Graduates of an accredited degree, or a degree with enough statistical content', fee='£[fee] application fee, then the GradStat annual fee',
         time='Usually 4 to 6 weeks', need='Degree certificate and transcript',
         faqs=[("Is my degree accredited?", "Check the list of accredited degrees. If yours is not on it, we can still assess your transcript."),
               ("How do I move from GradStat to CStat?", "Once you have five years of experience, apply for CStat from MyRSS.")]),
    dict(file='data-analyst.html', title='Data Analyst', short='Data Analyst', grade='analyst',
         lead='Data Analyst status recognises people who work with data professionally, whatever their route in, including apprenticeships.',
         who='Analysts with relevant experience, or who have completed a Level 4 data analyst apprenticeship', fee='£[fee] application fee, then the Data Analyst annual fee',
         time='Usually 4 to 6 weeks', need='CV, a short statement of your work, and one referee or your apprenticeship certificate',
         faqs=[("Do I need a degree?", "No. Experience or an apprenticeship is enough."),
               ("Can I go on to GradStat or CStat later?", "Yes. Your Data Analyst status and CPD count towards it.")]),
    dict(file='data-science-professional.html', title='Data Science Professional', short='Data Science Professional', grade='dsp',
         lead='Data Science Professional (DSP) and Advanced Data Science Professional (AdvDSP) are awarded with the Alliance for Data Science Professionals, to a shared standard.',
         who='Data scientists who meet the Alliance standard, at practitioner (DSP) or advanced (AdvDSP) level', fee='£[fee] application fee',
         time='Usually 8 to 12 weeks', need='CV, evidence against the Alliance standard, two referees',
         faqs=[("What is the difference between DSP and AdvDSP?", "AdvDSP is for senior practitioners who lead data science work and set direction."),
               ("Is AdvDSP being renamed?", "A change from AdvDSP to Chartered Data Science Professional (CDSP) is under discussion.")]),
]

PD_NAV = [('professional-development.html', 'Overview')] + [(q['file'], q['title']) for q in QUALS] + [('professional-development.html#cpd', 'CPD'), ('accreditation.html', 'Accreditation')]


def pd_sidenav(current):
    cur = ' aria-current="page"'
    lis = ''.join(f'<li><a href="~/pages/{f}"{cur if f == current else ""}>{e(t)}</a></li>' for f, t in PD_NAV)
    return f'<nav class="sidenav" aria-label="Professional development"><h2>Professional development</h2><ul>{lis}</ul></nav>'


def pd_hub():
    n = Notes()
    cards = ''.join(f'<article class="card"><h3 class="card-title"><a href="~/pages/{q["file"]}">{e(q["title"])}</a></h3><p class="card-text">{e(q["who"])}.</p></article>' for q in QUALS)
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
        <div class="grid grid-4">{cards}</div>
      </section>

      <!-- CPD explained publicly; the record itself is in MyRSS (REQ-195) -->
      <section id="cpd" aria-labelledby="cpd-title" class="content-highlight">
        <div>
          <h2 id="cpd-title">Continuing professional development (CPD)</h2>
          <p>Holders of professional status record at least 30 hours of CPD a year. Courses, conferences, reviewing, mentoring and self-directed study all count. RSS courses and events are added to your record automatically.</p>
          <p data-show-for="member lapsed" hidden><a class="btn" href="~/pages/myrss-cpd.html">Open your CPD record</a></p>
          <p data-show-for="guest registered">Members keep their CPD record in MyRSS. <a href="~/pages/sign-in.html">Sign in</a> or <a href="~/pages/join.html">join</a>.</p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>
      {n("CPD is explained to everyone; only the record itself is behind sign-in.", "REQ-195, REQ-178")}

      <section class="grid grid-2" aria-label="Accreditation and the register">
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


def qual_page(q):
    n = Notes()
    faqs = ''.join(f'<div class="accordion-item"><button class="accordion-title" type="button">{e(a)} <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>{e(b)}</p></div></div>' for a, b in q['faqs'])
    member_cta = ('<p data-show-for="member" hidden><span class="status-pill">You hold CStat</span> <a href="~/pages/myrss.html">Download your certificate</a></p>'
                  '<p data-show-for="lapsed" hidden><a class="btn" href="~/pages/myrss.html#renew">Renew to keep your status</a></p>') if q['grade'] == 'cstat' else \
                 '<p data-show-for="member lapsed" hidden><a class="btn" href="~/pages/myrss.html#applications">Start your application in MyRSS</a></p>'
    body = f'''
      <div class="with-sidenav">
        {pd_sidenav(q['file'])}
        <article>
          <h1>{e(q['title'])}</h1>
          <p class="lead">{e(q['lead'])}</p>
          {n("Standard content page: left-hand section menu, rich text with headings, and reusable components (key facts, steps, accordion, call to action) placed by editors.", "REQ-029, REQ-013, REQ-014", "CMS")}
          <section class="panel surface">
            <h2 class="h4">At a glance</h2>
            <dl class="summary-list">
              <dt>Who it is for</dt><dd>{e(q['who'])}</dd>
              <dt>Fee</dt><dd>{e(q['fee'])}</dd>
              <dt>How long it takes</dt><dd>{e(q['time'])}</dd>
              <dt>You will need</dt><dd>{e(q['need'])}</dd>
            </dl>
          </section>
          <h2>How to apply</h2>
          <ol class="steps" aria-label="Steps to {e(q['short'])}"><li>Join as a Fellow</li><li>Apply in MyRSS</li><li>Assessment</li><li>Award</li></ol>
          <div class="prose">
            <p>You apply from MyRSS once you are a member. Your application is assessed by the Professional Affairs Committee, which may ask for more evidence.</p>
            <p>Once awarded, you will appear on the public Professional Register unless you choose not to.</p>
          </div>
          <p data-show-for="guest registered"><a class="btn" href="~/pages/join.html">Join, then apply</a></p>
          {member_cta}
          {n("The call to action changes with the viewer: non-members are sent to join first; members go to the application in MyRSS, or are told they already hold the status.", "REQ-109, REQ-177")}
          <h2>Frequently asked questions</h2>
          <div class="accordion">{faqs}</div>
          <div class="share-row" style="margin-top:2rem"><span class="wf-meta">Last reviewed 12 September 2026 by Professional Affairs</span></div>
          {n("Every page has a named owner and a review date; the owner is reminded when it falls due.", "REQ-143, REQ-122", "CMS")}
        </article>
      </div>
'''
    page(q['file'], q['title'], body, 'professional-development',
         [('Professional development', '~/pages/professional-development.html'), (q['short'], None)])


def cstat():
    for q in QUALS:
        qual_page(q)


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
          <p>Tell us about your programme using the form. If it looks eligible, we will invite you to apply online, where you can save your application as you go, track it and see past ones.</p>
          <p><a class="btn btn-secondary" href="~/pages/accreditation-apply.html">Start or continue an application</a> <a href="~/pages/myrss-accreditation.html">Your applications</a></p>
          {n("Applications are made online by a signed-in contact at the university or provider, with save and return, document upload and a status they can follow. Staff and the Professional Affairs Committee review them in the CMS.", "REQ-190")}
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
            <article class="list-item" data-item data-sid="event-{x['id']}" data-kind="{x['kind']}" data-type="{x['kind']}" data-topic="{' '.join(x['topics'])}" data-fmt="{x['fmt']}" data-sub="{slug(x.get('sub', ''))}" data-audience="{' '.join(x['aud'])}"
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
              <p class="empty-state" data-empty hidden>No events or courses match. Try removing a filter, or <a href="~/pages/events.html?when=past">look at past events</a>.<span data-site-search-wrap hidden> Or <a data-site-search href="search.html">search the whole site</a>.</span></p>
              <p style="text-align:center;margin-top:1.5rem"><button class="btn btn-secondary" type="button" data-more>Show more</button></p>
            </div>
            <div data-calendar hidden>
              <div class="calendar-head"><button class="btn btn-secondary btn-small" type="button" data-cal-step="-1">&lsaquo; Previous</button><h2 data-cal-label>November 2026</h2><button class="btn btn-secondary btn-small" type="button" data-cal-step="1">Next &rsaquo;</button></div>
              <div class="calendar-grid" data-cal-grid></div>
              <p class="cal-legend"><span class="cal-item event">Event</span><span class="cal-item course">Training course</span></p>
              {n("Month view with the same filters. Each item shows a quick snapshot on hover or focus and links to the full listing. Events and courses are told apart by a pattern here; in design, by colour.", "REQ-210, REQ-212")}
            </div>
            {n("Each event appears once whatever its format, tagged Hybrid where it is. Multi-day courses appear once, not on every day. Fully booked courses stay listed with a waiting list.", "REQ-201, REQ-218, REQ-223")}
            {n("Availability labels on listings ('Few places left', 'Fully booked') are ClerksWell's suggestion REQ-289 (a Could). They are shown on two courses only to illustrate it.", "REQ-289", "Proposed")}
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
            <p><a class="btn btn-block" href="~/pages/book-event.html?format=in-person">Attend in person</a></p>
            <p><a class="btn btn-block btn-secondary" href="~/pages/book-event.html?format=online">Join online</a></p>
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
    dates = [('2026-11-10', '2026-11-11', 'online', 'Places available', 345, 460, False),
             ('2027-02-16', '2027-02-17', 'online', 'Fully booked: waiting list', 345, 460, True),
             ('2027-04-20', '2027-04-21', 'in person, London', 'Places available', 395, 520, False)]
    radios = ''.join(f'<label class="radio-card"><input type="radio" name="date" value="{a}" data-date-choice="{drange(a, b)}" data-format="{fmt}" data-member="{m}" data-nonmember="{nm}"{" data-full" if full else ""}{" checked" if i == 0 else ""}> <strong>{drange(a, b)}</strong>{fmt[0].upper() + fmt[1:]} &middot; £{m} members, £{nm} non-members &middot; {st}</label>' for i, (a, b, fmt, st, m, nm, full) in enumerate(dates))
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
            <p class="wf-meta" data-price-for-viewer data-member="345" data-nonmember="460"></p>
            <div data-book-actions>
              <p><a class="btn btn-block" href="~/pages/book.html" data-book-link>Book <span data-chosen-date>10 to 11 November 2026</span></a></p>
              <p><button class="btn btn-block btn-secondary" type="button" data-add-basket="Introduction to R||345" data-price-nonmember="460" data-uses-date>Add to basket</button><span class="wf-meta" data-added hidden>Added. <a href="~/pages/basket.html">View basket</a></span></p>
            </div>
            <div data-waitlist hidden>
              <p>This date is full. Join the waiting list and we'll email you if a place comes up.</p>
              <p><button class="btn btn-block btn-secondary" type="button" data-modal-open="waitlist-modal">Join the waiting list</button></p>
            </div>
            {n("Every date and price on one page, so nobody has to move between pages to compare. The date chosen and the viewer's price carry through to booking and the basket. A full date (February here) swaps booking for the waiting list, synced with Dynamics.", "REQ-214, REQ-218, REQ-094, REQ-087")}
          </aside>
        </div>
      </article>
      <section aria-labelledby="also">
        <h2 class="section-title" id="also">Related courses</h2>
        <div class="grid grid-3">{"".join(f'<article class="card"><p class="meta-row"><span class="tag">{e(x.get("level", ""))}</span><span class="tag">{fmt_label(x["fmt"])}</span></p><h3 class="card-title"><a href="~/pages/course.html">{e(x["title"])}</a></h3><p class="card-text">{drange(x["date"], x["end"])}</p></article>' for x in EVENTS if x["kind"] == "course" and x["id"] in ("dataviz", "bayes-stan", "intro-ml"))}</div>
        {n("Cross-sell from shared tags across CMS and CRM.", "REQ-220")}
      </section>
      <div class="wf-modal" id="waitlist-modal" role="dialog" aria-modal="true" aria-labelledby="wl-title">
        <div class="wf-modal-panel">
          <button class="wf-modal-close" type="button" aria-label="Close">&times;</button>
          <h2 id="wl-title">Join the waiting list</h2>
          <form data-validate novalidate>
            <div class="field"><label for="wl-email">Email address</label><input type="email" id="wl-email" name="email" required></div>
            <button class="btn" type="submit">Join the waiting list</button>
            <p class="form-success" hidden>You're on the list for 16 to 17 February 2027. We'll email you if a place comes up.</p>
          </form>
        </div>
      </div>
'''
    page('course.html', 'Introduction to R', body, 'events-training', [('Events and training', '~/pages/events-training.html'), ('Training courses', '~/pages/events.html?type=course'), ('Introduction to R', None)])


def book():
    n = Notes()
    body = f'''
      <h1>Book: Introduction to R</h1>
      <p class="lead" data-book-date>10 to 11 November 2026, online</p>
      <ol class="steps" aria-label="Booking progress"><li>Who is attending</li><li>Delegate details</li><li>Your organisation</li><li>Check and pay</li></ol>
      {n("Booking for yourself or for others, with the booker and each delegate kept separate. Delegates get their own account so the course appears in their MyRSS.", "REQ-215, REQ-216")}
      <div class="split">
        <form data-steps data-book-form data-course="Introduction to R" data-default-date="10 to 11 November 2026" data-default-format="online" data-member="345" data-nonmember="460" data-pay-for="course" data-pay-amount="345" data-pay-desc="Introduction to R" novalidate>
          <section class="form-step">
            <h2>Who is attending?</h2>
            <fieldset class="field"><legend>I am booking for</legend>
              <label class="radio-card"><input type="radio" name="who" value="me" required data-error="Choose who you are booking for"> <strong>Myself</strong>We will use your MyRSS details</label>
              <label class="radio-card"><input type="radio" name="who" value="others" data-reveal="others-note"> <strong>Someone else, or a group</strong>You pay; each delegate gets the joining details</label>
            </fieldset>
            <div class="reveal" id="others-note" hidden><p>You will add each delegate on the next step. We will create a basic account for each delegate and tell them why.</p>
              <div class="field"><label for="b-count">Number of delegates</label><select id="b-count" name="count"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option></select><p class="field-hint">Booking six or more? <a href="~/pages/about.html#contact">Ask us about a group rate or in-house course</a>.</p></div></div>
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
            <p>Payment is by card on the next step.</p>
            {n("Paying by invoice or purchase order is ClerksWell's suggestion REQ-290 (a Could), so it is not built. Is it offered today?", "REQ-290", "Open question")}
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue</button></div>
          </section>
          <section class="form-step" hidden data-review>
            <h2>Check and pay</h2>
            <div data-summary></div>
            <div class="field"><label for="b-code">Discount code (optional)</label><div class="inline-field"><input type="text" id="b-code" name="code"><button class="btn btn-secondary btn-small" type="button">Apply</button></div></div>
            {n("Discount codes are entered here and validated with the payment provider. Member and early-bird prices are applied automatically.", "REQ-217, REQ-087")}
            <div class="field"><label class="check"><input type="checkbox" name="terms" required data-error="Accept the booking terms"> I accept the <a href="#">booking terms and cancellation policy</a></label></div>
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="submit">Continue to payment: <span data-book-total>£345</span></button></div>
          </section>
          <section class="form-success" data-complete hidden>
            <h2>Booking confirmed</h2>
            <p>We have emailed a receipt to you and joining instructions to the delegate. The course now appears in My events and training.</p>
            <p><a class="btn" href="~/pages/myrss-bookings.html">View in MyRSS</a></p>
            {n("If the booker leaves before paying, an abandoned-booking reminder is sent.", "REQ-221, REQ-089")}
          </section>
        </form>
        <aside class="panel surface"><h2 class="h4">Your booking</h2><p><strong>Introduction to R</strong><br><span data-book-date>10 to 11 November 2026, online</span></p><p data-book-rate>Member price: £345 per delegate</p><p><span data-book-count>1 delegate</span>: <strong data-book-total>£345</strong></p>
          {n("The date, the viewer's price (member or non-member) and the number of delegates all come through from the course page and set the amount paid.", "REQ-087, REQ-215")}</aside>
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
        <aside class="panel surface" data-basket-summary hidden>
          <dl class="summary-list"><dt>Subtotal</dt><dd data-basket-sub>£0.00</dd><dt>Discount</dt><dd data-basket-discount>£0.00</dd><dt>VAT</dt><dd data-basket-vat>£0.00</dd><dt>Total</dt><dd><strong data-basket-total>£0.00</strong></dd></dl>
          <form data-promo-form>
            <div class="field"><label for="promo">Voucher or promo code</label><div class="inline-field"><input type="text" id="promo" name="code"><button class="btn btn-secondary btn-small" type="submit">Apply</button></div><p class="field-hint" data-promo-msg aria-live="polite">Try MEMBER10</p></div>
          </form>
          <p><button class="btn btn-block" type="button" data-checkout>Checkout and pay</button></p>
          {n("Pricing logic covers member grade, early-bird and late rates, concessions, bundles, codes and VAT. A downloadable receipt follows payment.", "REQ-087")}
          {n("Baskets left without paying prompt a reminder email and appear in ecommerce reporting.", "REQ-089, REQ-116")}
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
            <tr><th scope="row">Full conference</th><td>All sessions, lunches, refreshments, welcome reception</td><td>£595</td><td>£795</td><td><button class="btn btn-small" type="button" data-add-basket="RSS Conference 2027: full|6 to 9 September 2027|595" data-price-nonmember="795" aria-label="Add full to basket">Add</button><span class="wf-meta" data-added hidden> Added</span></td></tr>
            <tr><th scope="row">Day ticket</th><td>One day, lunch and refreshments</td><td>£225</td><td>£295</td><td><button class="btn btn-small" type="button" data-add-basket="RSS Conference 2027: day ticket|Choose your day at checkout|225" data-price-nonmember="295" aria-label="Add day ticket to basket">Add</button><span class="wf-meta" data-added hidden> Added</span></td></tr>
            <tr><th scope="row">Student</th><td>All sessions and lunches</td><td>£295</td><td>£345</td><td><button class="btn btn-small" type="button" data-add-basket="RSS Conference 2027: student|6 to 9 September 2027|295" data-price-nonmember="345" aria-label="Add student to basket">Add</button><span class="wf-meta" data-added hidden> Added</span></td></tr>
            <tr><th scope="row">Optional: conference dinner</th><td>Tuesday evening</td><td>£85</td><td>£85</td><td><button class="btn btn-small" type="button" data-add-basket="Conference dinner|7 September 2027|85" data-price-nonmember="85" aria-label="Add Conference dinner to basket">Add</button><span class="wf-meta" data-added hidden> Added</span></td></tr>
          </tbody></table></div>
        <p><button class="btn" type="button" data-add-basket="RSS Conference 2027: full|6 to 9 September 2027|595" data-price-nonmember="795" data-go-basket>Book now: full conference</button> <a href="~/pages/basket.html">View basket</a></p>
        {n("What each ticket includes and the price of every extra are shown before checkout. Tickets go into the basket at the viewer's price: member or non-member.", "REQ-230, REQ-087, REQ-094")}
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



def accreditation_apply():
    n = Notes()
    body = f'''
      <h1>Apply for accreditation</h1>
      <p class="lead">Your application saves as you go. You can leave and come back to it from MyRSS.</p>
      <ol class="steps" aria-label="Application progress"><li>Route</li><li>Your organisation</li><li>The programme</li><li>Evidence</li><li>Check and submit</li></ol>
      {n("Online application for University and AfDSP accreditation by a signed-in contact. Each step saves to a draft, so an applicant can leave and return.", "REQ-190, REQ-082")}
      <div class="split">
        <form data-steps novalidate>
          <section class="form-step">
            <h2>Which route are you applying for?</h2>
            <fieldset class="field"><legend>Route</legend>
              <label class="radio-card"><input type="radio" name="route" value="University accreditation" required data-error="Choose a route"> <strong>University accreditation</strong>Undergraduate and master's degrees with substantial statistical content</label>
              <label class="radio-card"><input type="radio" name="route" value="AfDSP"> <strong>Alliance for Data Science Professionals (AfDSP)</strong>Programmes that lead to Data Science Professional status</label>
            </fieldset>
            <div class="form-nav"><span></span><button class="btn" type="button" data-next>Continue</button></div>
          </section>
          <section class="form-step" hidden>
            <h2>Your organisation</h2>
            <div class="field"><label for="aa-org">University or provider</label><input type="text" id="aa-org" name="org" value="University of Eastwick" required></div>
            <div class="field"><label for="aa-dept">Department or school</label><input type="text" id="aa-dept" name="dept" required></div>
            <div class="field-row"><div class="field"><label for="aa-contact">Main contact</label><input type="text" id="aa-contact" name="contact" value="Sam Green" required></div><div class="field"><label for="aa-email">Contact email</label><input type="email" id="aa-email" name="cemail" value="s.green@eastwick.example.ac.uk" required></div></div>
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Save and continue</button></div>
          </section>
          <section class="form-step" hidden>
            <h2>The programme</h2>
            <div class="field"><label for="aa-prog">Programme title</label><input type="text" id="aa-prog" name="programme" required></div>
            <div class="field-row"><div class="field"><label for="aa-level">Level</label><select id="aa-level" name="level" required><option value="">Choose</option><option>Undergraduate</option><option>Master's</option><option>Other</option></select></div><div class="field"><label for="aa-start">First intake</label><input type="text" id="aa-start" name="start" placeholder="e.g. September 2027"></div></div>
            <div class="field"><label for="aa-mode">Mode of study</label><select id="aa-mode" name="mode"><option>Full time</option><option>Part time</option><option>Both</option></select></div>
            <div class="field"><label for="aa-out">How does the programme meet the learning outcomes?</label><textarea id="aa-out" name="outcomes" rows="5" required></textarea><p class="field-hint">Summarise here; the full mapping goes in the evidence step.</p></div>
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Save and continue</button></div>
          </section>
          <section class="form-step" hidden>
            <h2>Evidence</h2>
            <div class="field"><label for="aa-map">Learning outcomes mapping</label><input type="file" id="aa-map" name="mapping" accept=".pdf,.docx,.xlsx" required data-error="Upload the learning outcomes mapping"><p class="field-hint">PDF, Word or Excel, up to 20 MB. <a href="#">Download the mapping template</a></p></div>
            <div class="field"><label for="aa-hand">Programme handbook and module descriptors</label><input type="file" id="aa-hand" name="handbook" accept=".pdf,.docx" multiple></div>
            {n("Uploads are restricted to accepted file types, checked by file signature and scanned for malware before they are stored.", "REQ-254, REQ-258, REQ-259")}
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="button" data-next>Save and continue</button></div>
          </section>
          <section class="form-step" hidden data-review>
            <h2>Check and submit</h2>
            <div data-summary></div>
            <div class="field"><label class="check"><input type="checkbox" name="declare" required data-error="Confirm the declaration"> I confirm the information is accurate and I am authorised to apply on behalf of the organisation</label></div>
            <div class="form-nav"><button class="btn btn-secondary" type="button" data-back>Back</button><button class="btn" type="submit">Submit application</button></div>
          </section>
          <section class="form-success" data-complete hidden>
            <h2>Application submitted</h2>
            <p>Your reference is <strong>ACC-2026-118</strong>. We have emailed a copy. The accreditation team will acknowledge it within 10 working days, and you can follow its progress in MyRSS.</p>
            <p><a class="btn" href="~/pages/myrss-accreditation.html">Your applications</a></p>
          </section>
        </form>
        <aside class="panel surface">
          <h2 class="h4">Before you start</h2>
          <p>You will need the programme handbook, module descriptors and a learning outcomes mapping.</p>
          <p class="wf-meta">Draft saved 2 November 2026, 14:32</p>
          {n("Is there an application fee? If so, it is paid on the submit step through the same payment page as every other purchase.", "REQ-190, REQ-086", "Open question")}
        </aside>
      </div>
'''
    page('accreditation-apply.html', 'Apply for accreditation', body, 'professional-development',
         [('Professional development', '~/pages/professional-development.html'), ('Accreditation', '~/pages/accreditation.html'), ('Apply', None)])


def book_event():
    n = Notes()
    ev = EVENTS[0]
    body = f'''
      <h1>Book: {e(ev["title"])}</h1>
      <p class="lead">{weekday(ev["date"])} {d(ev["date"])}, {e(ev["time"])}. Free.</p>
      {n("Free events have a short booking: no payment step, and a confirmation email without payment wording. Signed-in users' details are filled in from MyRSS.", "REQ-206, REQ-207")}
      <div class="split">
        <form data-validate data-prefill novalidate>
          <div data-show-for="guest" class="panel">
            <p><a href="~/pages/sign-in.html">Sign in</a> to book faster, or continue as a guest. We will create a free account so the booking appears in MyRSS.</p>
            {n("Booking creates a basic account for anyone without one, so every booking sits against a contact in Dynamics. Should guests be asked to create a password now, or later?", "REQ-076, REQ-154", "Open question")}
          </div>
          <fieldset class="field"><legend>How will you attend?</legend>
            <label class="radio-card"><input type="radio" name="format" value="in-person" required data-error="Choose how you will attend"> <strong>In person</strong>{e(ev["place"].split(",")[0])}, Errol Street, London</label>
            <label class="radio-card"><input type="radio" name="format" value="online"> <strong>Online</strong>Joining link emailed the day before</label>
          </fieldset>
          <div class="field-row"><div class="field"><label for="be-first">First name</label><input type="text" id="be-first" name="first" required></div><div class="field"><label for="be-last">Last name</label><input type="text" id="be-last" name="last" required></div></div>
          <div class="field"><label for="be-email">Email</label><input type="email" id="be-email" name="email" required></div>
          <div class="field"><label for="be-needs">Access requirements (optional)</label><textarea id="be-needs" name="needs" rows="2"></textarea></div>
          <button class="btn" type="submit">Book my free place</button>
          <div class="form-success panel" hidden>
            <h2 class="h4">You're booked</h2>
            <p>We have emailed your confirmation. The event is in My events and training.</p>
            <p><a class="btn btn-small" href="~/pages/myrss-bookings.html">View my bookings</a> <a href="#">Add to calendar</a></p>
          </div>
        </form>
        <aside class="panel surface"><h2 class="h4">Your booking</h2><p><strong>{e(ev["title"])}</strong><br>{d(ev["date"])}</p><p>Cost: Free</p></aside>
      </div>
'''
    page('book-event.html', 'Book a free event', body, 'events-training', [('Events and training', '~/pages/events-training.html'), ('Event', '~/pages/event.html'), ('Book', None)])

def build():
    pd_hub()
    cstat()
    accreditation()
    events_hub()
    finder()
    event()
    course()
    book()
    book_event()
    accreditation_apply()
    basket_page()
    conference()
    submit_event()
