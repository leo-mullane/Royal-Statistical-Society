"""Get involved, policy, news and publications."""
from common import *


def get_involved():
    n = Notes()
    body = f'''
      <section class="hub-hero">
        <div>
          <h1>Get involved</h1>
          <p class="lead">Join a section or local group, volunteer your skills, and help us recognise the work of statisticians.</p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>
      {n("Use-based hub for getting involved. Volunteering sits here, with groups, honours and ambassadors.", "REQ-034")}
      <section aria-labelledby="gi-groups">
        <h2 class="section-title" id="gi-groups">Sections and groups</h2>
        <div class="grid grid-3">
          <article class="card"><h3 class="card-title"><a href="~/pages/groups.html">20 sections</a></h3><p class="card-text">Organised by subject, from medical statistics to statistical computing.</p></article>
          <article class="card"><h3 class="card-title"><a href="~/pages/groups.html?tab=local">22 local groups</a></h3><p class="card-text">Across the UK, and in the Gulf, India, Nigeria and Singapore.</p></article>
          <article class="card"><h3 class="card-title"><a href="~/pages/groups.html?tab=sigs">Special interest groups</a></h3><p class="card-text">Smaller groups around a shared interest.</p></article>
        </div>
        {n("How many sections and local groups are there? The RFP gives 16 and 15; the site lists 20 and 22.", "REQ-102", "Open question")}
      </section>
      <section id="volunteering" aria-labelledby="gi-vol">
        <h2 class="section-title" id="gi-vol">Volunteering opportunities</h2>
        <div class="list-item no-thumb"><div><h3><a href="~/pages/article.html">Statistical Ambassadors 2027</a></h3><p>Help journalists and the public understand the numbers. Training provided.</p><p class="meta-row"><span>Closes 30 November 2026</span><span>About 2 days a year</span></p></div><div class="list-actions"><a class="btn btn-small" href="~/pages/article.html">Find out more</a></div></div>
        <div class="list-item no-thumb"><div><h3><a href="~/pages/article.html">Medical Section committee</a></h3><p>Two places on the committee for 2027.</p><p class="meta-row"><span>Closes 15 December 2026</span><span>Four meetings a year</span></p></div><div class="list-actions"><a class="btn btn-small" href="~/pages/article.html">Find out more</a></div></div>
        <div class="list-item no-thumb" id="s4s"><div><h3><a href="#">Statisticians for Society</a></h3><p>Pro bono statistical help for charities and community groups.</p><p class="meta-row"><span>Ongoing</span><span>Project by project</span></p></div><div class="list-actions"><a class="btn btn-small" href="#">Volunteer</a></div></div>
        {n("Volunteering opportunities are their own content type, with a closing date that removes them from listings automatically.", "REQ-011, REQ-016")}
      </section>
      <section class="grid grid-2">
        <article class="card" id="honours"><h2 class="card-title">Honours and awards</h2><p class="card-text">The Guy Medals, the Florence Nightingale Award and more. Nominations for 2027 are open.</p><a class="card-link" href="#">Honours and awards</a></article>
        <article class="card" id="ambassadors"><h2 class="card-title">Statistical Ambassadors</h2><p class="card-text">Members who explain statistics in the media and in schools.</p><a class="card-link" href="#">About the programme</a></article>
      </section>
      <section class="content-highlight">
        <div><h2>Support our work</h2><p>Donations fund statistical education and our work on the public understanding of statistics.</p><a class="btn" href="~/pages/donate.html">Donate</a></div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>
'''
    page('get-involved.html', 'Get involved', body, 'get-involved', [('Get involved', None)])


def groups():
    n = Notes()

    def items(kind):
        out = ''
        for g in [x for x in GROUPS if x['kind'] == kind]:
            out += f'''<article class="list-item no-thumb" data-item data-region="{e(g['region'].lower().replace(' ', '-'))}" data-topic="{' '.join(g['topics'])}" data-title="{e(g['title'])}" data-text="{e(g['title'] + ' ' + g['region'])}">
              <div><h3><a href="~/pages/group.html">{e(g['title'])}</a></h3><p class="meta-row"><span>{e(GROUP_KINDS[g['kind']])}</span><span>{e(g['region'])}</span></p></div>
              <div class="list-actions"><a class="btn btn-small btn-secondary" href="~/pages/group.html">View group</a></div>
            </article>'''
        return out

    regions = sorted({g['region'] for g in GROUPS})
    region_opts = ''.join(f'<option value="{e(r.lower().replace(" ", "-"))}">{e(r)}</option>' for r in regions)

    def panel(kind, pid, active=False):
        return f'''<div class="tab-panel{' active' if active else ''}" id="{pid}">
            <section data-listing>
              <div class="filter-bar">
                <div class="field"><label for="{pid}-q">Search</label><input type="search" id="{pid}-q" data-filter="q" placeholder="Group name or place"></div>
                <div class="field"><label for="{pid}-r">Region</label><select id="{pid}-r" data-filter="region"><option value="">All regions</option>{region_opts}</select></div>
              </div>
              <p class="result-count" data-count aria-live="polite"></p>
              <div>{items(kind)}</div>
              <p class="empty-state" data-empty hidden>No groups match.</p>
            </section>
          </div>'''

    body = f'''
      <h1>Sections and groups</h1>
      <p class="lead">Members can join as many sections and groups as they like, free of charge, from MyRSS.</p>
      <div class="tabs" role="tablist">
        <button class="tab active" type="button" data-tab="g-sections" data-tab-key="sections">Sections</button>
        <button class="tab" type="button" data-tab="g-local" data-tab-key="local">Local groups</button>
        <button class="tab" type="button" data-tab="g-sigs" data-tab-key="sigs">Special interest groups</button>
      </div>
      <div>
        {panel('section', 'g-sections', True)}
        {panel('local', 'g-local')}
        {panel('sig', 'g-sigs')}
      </div>
      <div class="wf-placeholder embed">Map of local groups</div>
      {n("Groups listed by type, with a region field so international and UK local groups can be found by place. A map view is shown as a placeholder.", "REQ-102, REQ-031")}
      {n("A full 'Find a group' finder with map is ClerksWell's suggestion REQ-285 (a Could); this page shows the basic listing.", "REQ-285", "Proposed")}
'''
    page('groups.html', 'Sections and groups', body, 'get-involved', [('Get involved', '~/pages/get-involved.html'), ('Sections and groups', None)])


def group():
    n = Notes()
    evs = [x for x in EVENTS if 'health' in x['topics'] and x['date'] >= TODAY]
    body = f'''
      <section class="hub-hero">
        <div>
          <p class="meta-row"><span class="tag">Section</span></p>
          <h1>Medical Section</h1>
          <p class="lead">For statisticians working in clinical trials, epidemiology and health services research.</p>
          <p data-show-for="member" hidden><button class="btn" type="button">Join this section</button> <span class="wf-meta">Free for members. You'll get the section newsletter.</span></p>
          <p data-show-for="guest registered lapsed"><a class="btn" href="~/pages/join.html">Join the RSS to join this section</a></p>
          <p class="share-row"><a href="#">LinkedIn</a><a href="#">Bluesky</a><a href="#">YouTube</a></p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>
      {n("Section, SIG and local group template. News and events tagged with the group are pulled through automatically, with the group's social links.", "REQ-102")}
      <div class="split">
        <div>
          <section aria-labelledby="g-events"><h2 class="section-title" id="g-events">Upcoming events</h2>
            {"".join(f'<div class="list-item no-thumb"><div><h3><a href="~/pages/{event_url(x)}">{e(x["title"])}</a></h3><p class="meta-row"><span>{drange(x["date"], x["end"])}</span><span>{fmt_label(x["fmt"])}</span></p></div></div>' for x in evs)}
            <p><a href="~/pages/events.html?topic=health">All health statistics events &rarr;</a></p></section>
          <section aria-labelledby="g-news"><h2 class="section-title" id="g-news">News</h2>
            <div class="list-item no-thumb"><div><h3><a href="~/pages/article.html">Medical Section seeks new committee members</a></h3><p class="meta-row"><span>10 September 2026</span></p></div></div>
            <div class="list-item no-thumb"><div><h3><a href="~/pages/article.html">From Real World Data Science: validating clinical prediction models</a></h3><p class="meta-row"><span>25 September 2026</span></p></div></div>
          </section>
        </div>
        <aside class="stack">
          <div class="panel"><h2 class="h4">Committee</h2><ul class="stack"><li>Chair: Dr [Name]</li><li>Secretary: [Name]</li><li>Treasurer: [Name]</li></ul><p><a href="#">Contact the committee</a></p></div>
          <div class="panel"><h2 class="h4">Section newsletter</h2><p>Sent four times a year to section members.</p></div>
          {n("Group officers write and send their newsletter from the portal using a template that pulls in the group's news and events. Officers see only the minimum personal data about recipients.", "REQ-163, REQ-165, REQ-167")}
        </aside>
      </div>
'''
    page('group.html', 'Medical Section', body, 'get-involved', [('Get involved', '~/pages/get-involved.html'), ('Sections and groups', '~/pages/groups.html'), ('Medical Section', None)])


def donate():
    n = Notes()
    body = f'''
      <div class="split">
        <div>
          <h1>Donate</h1>
          <p class="lead">Your gift helps more people understand and use statistics, from school classrooms to Parliament.</p>
          <!-- Donations with Gift Aid (REQ-090) -->
          <form class="form-step" data-validate novalidate>
            <fieldset class="field"><legend>Amount</legend>
              <div class="radio-cards">
                <label class="radio-card"><input type="radio" name="amount" value="10" data-price="10" required data-error="Choose an amount"> <strong>£10</strong>Buys a classroom resource pack</label>
                <label class="radio-card"><input type="radio" name="amount" value="25" data-price="25"> <strong>£25</strong>Supports a schools lecture</label>
                <label class="radio-card"><input type="radio" name="amount" value="50" data-price="50"> <strong>£50</strong>Trains a Statistical Ambassador</label>
                <label class="radio-card"><input type="radio" name="amount" value="other" data-reveal="other-amount"> <strong>Other amount</strong></label>
              </div>
            </fieldset>
            <div class="reveal field" id="other-amount" hidden><label for="d-other">Amount in pounds</label><input type="number" id="d-other" name="other" min="1"></div>
            <fieldset class="field"><legend>How often</legend>
              <label class="check"><input type="radio" name="freq" value="once" checked> Once</label>
              <label class="check"><input type="radio" name="freq" value="monthly"> Monthly by Direct Debit</label>
            </fieldset>
            <div class="field-row">
              <div class="field"><label for="d-name">Full name</label><input type="text" id="d-name" name="name" required></div>
              <div class="field"><label for="d-email">Email</label><input type="email" id="d-email" name="email" required></div>
            </div>
            <div class="field"><label class="check"><input type="checkbox" name="giftaid" data-reveal="giftaid-detail"> Yes, I am a UK taxpayer and want to Gift Aid this donation</label>
              <p class="field-hint">Gift Aid adds 25p to every £1 at no cost to you.</p></div>
            <div class="reveal" id="giftaid-detail" hidden>
              <div class="field"><label for="d-addr">Home address and postcode</label><input type="text" id="d-addr" name="address"></div>
              <p class="wf-meta">I understand that if I pay less Income Tax or Capital Gains Tax than the Gift Aid claimed on all my donations in that tax year, it is my responsibility to pay the difference.</p>
            </div>
            <p>Your donation: <strong data-total>£0</strong></p>
            <button class="btn" type="submit">Continue to payment</button>
            <p class="form-success" hidden>Thank you. We have emailed your receipt and Gift Aid declaration.</p>
          </form>
          {n("Gift Aid declaration recorded against the donor in Dynamics; card or Direct Debit through the same payment gateway as membership. There is no online donation function today, so this is new build.", "REQ-090, REQ-084, REQ-086, REQ-114")}
        </div>
        <div class="wf-placeholder ratio-4-3">Image 4:3</div>
      </div>
'''
    page('donate.html', 'Donate', body, 'get-involved', [('Get involved', '~/pages/get-involved.html'), ('Donate', None)])


def policy():
    n = Notes()
    items = ''
    for p in sorted(POLICY, key=lambda x: x['date'], reverse=True):
        items += f'''<article class="list-item no-thumb" data-item data-ptype="{p['ptype']}" data-topic="{' '.join(p['topics'])}" data-date="{p['date']}" data-year="{p['date'][:4]}" data-title="{e(p['title'])}" data-text="{e(p['title'] + ' ' + p['summary'])}">
              <div>
                <p class="meta-row"><span class="tag">{e(PTYPES[p['ptype']])}</span>{tags(p['topics'])}</p>
                <h3>{e(p['title'])}</h3>
                <p>{e(p['summary'])}</p>
                <p class="meta-row"><span>{d(p['date'])}</span><span>PDF, {e(p['size'])}</span></p>
              </div>
              <div class="list-actions"><a class="btn btn-small" href="#">Download PDF</a></div>
            </article>'''
    ptype_checks = ''.join(f'<label class="check"><input type="checkbox" data-filter="ptype" value="{k}"> {e(v)}</label>' for k, v in PTYPES.items())
    topic_opts = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in TOPICS.items())
    body = f'''
      <section class="hub-hero">
        <div>
          <h1>Policy and research</h1>
          <p class="lead">We use evidence and our members' expertise to improve how statistics are produced and used in public life.</p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>
      <section class="grid grid-3" id="areas" aria-label="Policy areas">
        <article class="card"><h2 class="card-title">Official statistics</h2><p class="card-text">The quality and independence of national statistics.</p></article>
        <article class="card"><h2 class="card-title">Statistics and AI</h2><p class="card-text"><a href="~/pages/campaign.html">Our campaign</a> on AI in the production of statistics.</p></article>
        <article class="card"><h2 class="card-title">Data skills and education</h2><p class="card-text">Statistics in schools, universities and the workforce.</p></article>
      </section>

      <!-- Policy library (REQ-252) -->
      <section id="library" data-listing data-page-size="6" aria-labelledby="lib-title">
        <h2 class="section-title" id="lib-title">Policy library</h2>
        <form class="filter-bar" role="search">
          <div class="field"><label for="pl-q">Search the library</label><input type="search" id="pl-q" data-filter="q"></div>
          <div class="field"><label for="pl-topic">Topic</label><select id="pl-topic" data-filter="topic"><option value="">All topics</option>{topic_opts}</select></div>
          <div class="field"><label for="pl-year">Year</label><select id="pl-year" data-filter="year"><option value="">Any year</option><option>2026</option><option>2025</option></select></div>
          <div class="field"><label for="pl-sort">Sort</label><select id="pl-sort" data-list-sort><option value="latest">Newest first</option><option value="oldest">Oldest first</option><option value="title">Title A to Z</option></select></div>
        </form>
        <fieldset class="chips" style="margin:1rem 0"><legend class="visually-hidden">Document type</legend>{ptype_checks}</fieldset>
        <div class="active-filters" data-chips></div>
        <p class="result-count" data-count aria-live="polite"></p>
        <div>{items}</div>
        <p class="empty-state" data-empty hidden>No documents match. Try another topic or year.</p>
        <p style="text-align:center"><button class="btn btn-secondary" type="button" data-more>Show more</button></p>
        {n("One library replaces the six category pages. Each item shows title, description, date, type, file type and size, with a download button. Text inside the PDFs is searchable from site search.", "REQ-252, REQ-044, REQ-140")}
        {n("Publishing each output as a short HTML summary page with the PDF attached is ClerksWell's suggestion REQ-286 (a Could).", "REQ-286", "Proposed")}
      </section>

      <section id="taskforces" class="grid grid-2">
        <article class="card"><h2 class="card-title">Task forces</h2><p class="card-text">Time-limited groups on a single issue, such as the Covid-19 Task Force and the AI Task Force.</p><a class="card-link" href="#">Current task forces</a></article>
        <article class="card" id="contact"><h2 class="card-title">Contact the policy team</h2><p class="card-text">For evidence requests, briefings and consultations.</p><a class="card-link" href="#">policy@rss.org.uk</a></article>
      </section>
'''
    page('policy.html', 'Policy and research', body, 'policy', [('Policy and research', None)])


def campaign():
    n = Notes()
    body = f'''
      <!-- Campaign / explainer template (REQ-104) -->
      <section class="hub-hero">
        <div>
          <p class="meta-row"><span class="tag">Campaign</span>{tags(['datasci', 'public'])}</p>
          <h1>Statistics and AI: what the public should expect</h1>
          <p class="lead">Six principles for using AI to produce and communicate statistics, and what we are asking government to do.</p>
          <p><a class="btn" href="#">Read the report (PDF, 3.4 MB)</a> <a class="btn btn-secondary" href="#act">Support the campaign</a></p>
        </div>
        <div class="wf-placeholder ratio-16-9">Image or video 16:9</div>
      </section>
      {n("Campaign and explainer template: hero, key messages, timeline, FAQs and a call to action, all as reusable components.", "REQ-104, REQ-013")}
      <section aria-labelledby="six">
        <h2 class="section-title" id="six">The six principles</h2>
        <ol class="grid grid-3">
          <li class="card"><h3 class="card-title">Transparent</h3><p class="card-text">Say when and how AI was used.</p></li>
          <li class="card"><h3 class="card-title">Tested</h3><p class="card-text">Check for bias and error before use.</p></li>
          <li class="card"><h3 class="card-title">Accountable</h3><p class="card-text">A named person is responsible.</p></li>
          <li class="card"><h3 class="card-title">Quality assured</h3><p class="card-text">The same standards as any other method.</p></li>
          <li class="card"><h3 class="card-title">Explained</h3><p class="card-text">Uncertainty is communicated clearly.</p></li>
          <li class="card"><h3 class="card-title">Open to challenge</h3><p class="card-text">Users can question the results.</p></li>
        </ol>
      </section>
      <section aria-labelledby="chart-title">
        <h2 class="section-title" id="chart-title">What the public told us</h2>
        <div class="wf-placeholder embed">Interactive chart (Flourish or Power BI) with a data table alternative</div>
        {n("Interactive data visuals can be embedded, each with an accessible table and a download.", "REQ-108, REQ-157")}
      </section>
      <section aria-labelledby="timeline">
        <h2 class="section-title" id="timeline">Timeline</h2>
        <ul class="stack"><li><strong>September 2026</strong> Report published</li><li><strong>October 2026</strong> Evidence to the Science, Innovation and Technology Committee</li><li><strong>Spring 2027</strong> Follow-up survey</li></ul>
      </section>
      <section aria-labelledby="cfaq">
        <h2 class="section-title" id="cfaq">Questions and answers</h2>
        <div class="accordion" data-single>
          <div class="accordion-item"><button class="accordion-title" type="button">Is the RSS against using AI? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>No. We want it used well, and openly.</p></div></div>
          <div class="accordion-item"><button class="accordion-title" type="button">Who did you consult? <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>Members, statistical producers and a representative public survey.</p></div></div>
        </div>
      </section>
      <section id="act" class="panel surface"><h2>Support the campaign</h2><p>Share the principles with your organisation, or tell us how AI is being used where you work.</p><div class="share-row"><a href="#">LinkedIn</a><a href="#">Bluesky</a><a href="#">Email</a><button class="btn-link" type="button" data-copy-link>Copy link</button></div></section>
'''
    page('campaign.html', 'Statistics and AI', body, 'policy', [('Policy and research', '~/pages/policy.html'), ('Statistics and AI', None)])


def news():
    n = Notes()
    kinds = {'news': 'News', 'press': 'Press release', 'callout': 'Member callout'}
    feat = [x for x in NEWS if x.get('featured')][0]
    items = ''
    for x in NEWS:
        src = f'<span class="tag">From {e(x["source"])}</span>' if x.get('source') else ''
        lock = '<span class="tag">Members</span>' if x['kind'] == 'callout' else ''
        items += f'''<article class="list-item" data-item data-type="{x['kind']}" data-topic="{' '.join(x['topics'])}" data-date="{x['date']}" data-title="{e(x['title'])}" data-text="{e(x['title'] + ' ' + x['summary'])}">
              <div class="wf-placeholder ratio-4-3">Image</div>
              <div><p class="meta-row"><span class="tag">{kinds[x['kind']]}</span>{src}{lock}{tags(x['topics'])}</p>
                <h3><a href="~/pages/article.html">{e(x['title'])}</a></h3><p>{e(x['summary'])}</p><p class="meta-row"><span>{d(x['date'])}</span></p></div>
              <div></div>
            </article>'''
    topic_opts = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in TOPICS.items())
    body = f'''
      <h1>News</h1>
      <!-- News landing with featured story and filters (REQ-235) -->
      <section class="content-highlight" aria-label="Featured story">
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
        <div><p class="meta-row"><span class="tag tag-strong">Featured</span><span class="tag">Press release</span></p><h2><a href="~/pages/article.html">{e(feat['title'])}</a></h2><p>{e(feat['summary'])}</p><p class="wf-meta">{d(feat['date'])}</p></div>
      </section>
      <section data-listing data-page-size="6">
        <form class="filter-bar" role="search">
          <div class="field"><label for="n-q">Search news</label><input type="search" id="n-q" data-filter="q"></div>
          <div class="field"><label for="n-type">Type</label><select id="n-type" data-filter="type"><option value="">All types</option><option value="news">News</option><option value="press">Press releases</option><option value="callout">Member callouts</option></select></div>
          <div class="field"><label for="n-topic">Topic</label><select id="n-topic" data-filter="topic"><option value="">All topics</option>{topic_opts}</select></div>
          <div class="field"><label for="n-sort">Sort</label><select id="n-sort" data-list-sort><option value="latest">Most recent</option><option value="oldest">Oldest</option><option value="title">Title A to Z</option></select></div>
        </form>
        <div class="active-filters" data-chips style="margin-top:1rem"></div>
        <p class="result-count" data-count aria-live="polite"></p>
        <div>{items}</div>
        <p class="empty-state" data-empty hidden>No stories match these filters.</p>
        <p style="text-align:center"><button class="btn btn-secondary" type="button" data-more>Show more</button></p>
        {n("One news page with filters for type and topic, covering featured stories, group news, press releases and member callouts. Stories from Significance and Real World Data Science are pulled in and labelled with their source.", "REQ-235, REQ-020, REQ-106")}
      </section>
'''
    page('news.html', 'News', body, 'news', [('News', None)])


def article():
    n = Notes()
    body = f'''
      <article class="split">
        <div>
          <p class="meta-row"><span class="tag">Press release</span>{tags(['official'])}</p>
          <h1>RSS responds to the Statistics Commission report</h1>
          <p class="meta-row"><span>28 October 2026</span><span>Policy team</span><span>4 minute read</span></p>
          <div class="share-row"><span class="wf-meta">Share:</span><a href="#">LinkedIn</a><a href="#">Bluesky</a><a href="#">Facebook</a><a href="#">Email</a><button class="btn-link" type="button" data-copy-link>Copy link</button></div>
          {n("Share buttons on every article, with an automatically generated card (title, summary, image).", "REQ-236, REQ-105")}
          <div class="wf-placeholder ratio-16-9" style="margin:1rem 0">Image 16:9, with caption and credit</div>
          <div class="prose">
            <p class="lead">The Society welcomes the report's focus on user needs and sets out three priorities for implementation.</p>
            <p>The Royal Statistical Society has responded to the Statistics Commission's final report, welcoming its recommendation that the needs of users should drive what official statistics are produced and how.</p>
            <h2>Three priorities</h2>
            <ol><li>Restore confidence in labour market statistics.</li><li>Give the statistical system the funding to modernise.</li><li>Make the independence of statistics clearer in law.</li></ol>
            <blockquote class="wf-quote"><p>"Good statistics are a public good. This report is a chance to put users first."</p><cite>RSS spokesperson</cite></blockquote>
            <h2>Notes to editors</h2>
            <p>For interviews, contact the press office on <a href="#">press@rss.org.uk</a>.</p>
          </div>
        </div>
        <aside class="stack">
          <div class="panel"><h2 class="h4">Related</h2><ul class="stack"><li><a href="~/pages/policy.html">Written evidence on ONS data quality</a></li><li><a href="~/pages/event.html">Census 2031 and the future of population statistics</a></li><li><a href="~/pages/group.html">Official Statistics Section</a></li></ul></div>
          <div class="panel"><h2 class="h4">Topics</h2><p class="chips"><a class="chip" href="~/pages/news.html?topic=official">Official statistics</a></p></div>
          {n("Related content and topic links come from the shared taxonomy.", "REQ-027, REQ-017")}
        </aside>
      </article>
'''
    page('article.html', 'RSS responds to the Statistics Commission report', body, 'news', [('News and publications', '~/pages/news.html'), ('News', '~/pages/news.html'), ('Article', None)])


def publications():
    n = Notes()
    body = f'''
      <h1>Journals and publications</h1>
      <p class="lead">Four journals, published for the Society by Oxford University Press, plus Significance magazine and Real World Data Science.</p>
      <!-- Journals with member access via SSO (REQ-198, REQ-033) -->
      <section class="grid grid-3" aria-label="Journals">
        <article class="card"><div class="wf-placeholder ratio-4-3">Journal cover</div><h2 class="card-title">Series A: Statistics in Society</h2><p class="card-text">Papers on statistics in public life, policy and society.</p><a class="card-link" href="#">Read Series A</a></article>
        <article class="card"><div class="wf-placeholder ratio-4-3">Journal cover</div><h2 class="card-title">Series B: Statistical Methodology</h2><p class="card-text">New statistical methods and theory.</p><a class="card-link" href="#">Read Series B</a></article>
        <article class="card"><div class="wf-placeholder ratio-4-3">Journal cover</div><h2 class="card-title">Series C: Applied Statistics</h2><p class="card-text">Statistics applied to real problems.</p><a class="card-link" href="#">Read Series C</a></article>
      </section>
      <div class="panel surface" data-show-for="member" hidden><p><strong>You have online access to Series A, B and C.</strong> Use 'Read' and you will be signed in at OUP automatically.</p></div>
      <div class="panel surface" data-show-for="guest registered lapsed"><p>Members read every journal online free. <a href="~/pages/sign-in.html">Sign in</a> or <a href="~/pages/join.html">join</a>.</p></div>
      {n("Members are signed in to the publisher (OUP) automatically, and content unlocks according to member type or paid subscription. Active subscriptions show in MyRSS.", "REQ-198, REQ-199", "Integration")}
      <section id="significance" class="content-highlight">
        <div class="wf-placeholder ratio-16-9">Significance cover</div>
        <div><h2>Significance</h2><p>Our magazine for anyone interested in statistics and data, published with the American Statistical Association.</p><ul class="stack"><li><a href="#">The statistics of extreme heat</a></li><li><a href="#">How many people really live in London?</a></li></ul><a href="#">Go to significancemagazine.com</a></div>
      </section>
      <section id="rwds" class="content-highlight image-right">
        <div class="wf-placeholder ratio-16-9">Real World Data Science</div>
        <div><h2>Real World Data Science</h2><p>Case studies and tutorials for data science practitioners.</p><ul class="stack"><li><a href="#">Validating clinical prediction models</a></li><li><a href="#">A field guide to synthetic data</a></li></ul><a href="#">Go to realworlddatascience.net</a></div>
      </section>
      {n("Latest items from each site are pulled through and styled as native content.", "REQ-020, REQ-033")}
'''
    page('publications.html', 'Journals and publications', body, 'news', [('News and publications', '~/pages/news.html'), ('Journals and publications', None)])


def build():
    get_involved()
    groups()
    group()
    donate()
    policy()
    campaign()
    news()
    article()
    publications()
