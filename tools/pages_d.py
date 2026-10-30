"""Resources, about, sign-in and MyRSS."""
from common import *


def resources():
    n = Notes()
    body = f'''
      <section class="hub-hero">
        <div>
          <h1>Resources</h1>
          <p class="lead">Find a qualified statistician, a job, or the resources we provide for students, educators, journalists and the public.</p>
          <form class="big-search" action="~/pages/find-an-expert.html" role="search"><label for="res-q" class="visually-hidden">Find an expert</label><input type="search" id="res-q" name="q" placeholder="Find an expert by name, skill or place"><button class="btn" type="submit">Find an expert</button></form>
        </div>
        <div class="wf-placeholder ratio-16-9">Image 16:9</div>
      </section>
      {n("Resources hub with audience hubs for journalists, educators and the public, and Find an expert.", "REQ-034, REQ-253")}
      <section class="grid grid-3" aria-label="Audience resources">
        <article class="card" id="students"><h2 class="card-title">Students and early career</h2><p class="card-text">e-Student membership, the Young Statisticians Section, careers advice and accredited degrees.</p><a class="card-link" href="#">Resources for students</a></article>
        <article class="card" id="educators"><h2 class="card-title">Educators</h2><p class="card-text">Teaching resources, the schools lecture and accreditation for universities.</p><a class="card-link" href="#">Resources for educators</a></article>
        <article class="card"><h2 class="card-title">Journalists</h2><p class="card-text">Press office, experts for comment and guides to reporting numbers.</p><a class="card-link" href="~/pages/for-journalists.html">Resources for journalists</a></article>
        <article class="card" id="public"><h2 class="card-title">The public</h2><p class="card-text">Explainers on the statistics in the news, and how to spot a misleading claim.</p><a class="card-link" href="#">Understanding statistics</a></article>
        <article class="card"><h2 class="card-title">Employers</h2><p class="card-text">Verify a professional qualification, hire a consultant or advertise a job.</p><a class="card-link" href="~/pages/find-an-expert.html">Find an expert</a></article>
        <article class="card"><h2 class="card-title">Jobs and careers</h2><p class="card-text">Vacancies in statistics and data science, and career profiles.</p><a class="card-link" href="~/pages/jobs.html">Browse jobs</a></article>
      </section>
      <section class="panel surface">
        <h2>Information centre</h2>
        <p data-show-for="member">Member documents: guidance, templates and past committee papers. <a href="~/pages/myrss.html#information-centre">Open the information centre</a></p>
        <p data-show-for="guest registered lapsed">A searchable library of documents for members. <a href="~/pages/sign-in.html">Sign in</a> to use it.</p>
        {n("Searchable, filterable repository of downloadable documents for members.", "REQ-185, REQ-178")}
      </section>
'''
    page('resources.html', 'Resources', body, 'resources', [('Resources', None)])


def journalists():
    n = Notes()
    press = [x for x in NEWS if x['kind'] == 'press']
    body = f'''
      <div class="split">
        <div>
          <h1>For journalists</h1>
          <p class="lead">We can help you understand and report the numbers, and put you in touch with an expert for comment.</p>
          {n("An audience resource hub, built from the same components as other hubs.", "REQ-253, REQ-034")}
          <section aria-labelledby="pr"><h2 class="section-title" id="pr">Latest press releases</h2>
            {"".join(f'<div class="list-item no-thumb"><div><h3><a href="~/pages/article.html">{e(x["title"])}</a></h3><p class="meta-row"><span>{d(x["date"])}</span></p></div></div>' for x in press)}
            <p><a href="~/pages/news.html?type=press">All press releases &rarr;</a></p></section>
          <section aria-labelledby="guides"><h2 class="section-title" id="guides">Guides to reporting statistics</h2>
            <ul class="stack"><li><a href="~/pages/policy.html">Briefing: understanding excess deaths</a></li><li><a href="#">A journalist's guide to risk</a></li><li><a href="#">Ten questions to ask of any statistic</a></li></ul></section>
        </div>
        <aside class="stack">
          <div class="panel surface"><h2 class="h4">Press office</h2><p><a href="#">press@rss.org.uk</a><br>020 7638 8998 (placeholder)<br>Out of hours: 07700 900000 (placeholder)</p></div>
          <div class="panel"><h2 class="h4">Find an expert for comment</h2><p>Our Statistical Ambassadors are trained to work with the media.</p><a href="~/pages/find-an-expert.html">Search experts</a></div>
        </aside>
      </div>
'''
    page('for-journalists.html', 'For journalists', body, 'resources', [('Resources', '~/pages/resources.html'), ('For journalists', None)])


def experts():
    n = Notes()

    def items(dirname):
        out = ''
        for x in [p for p in EXPERTS if dirname in p['dirs']]:
            out += f'''<article class="list-item" data-item data-status="{e(x['status'].split(',')[0].lower().replace(' ', '-'))}" data-topic="{' '.join(x['topics'])}" data-title="{e(x['name'])}" data-text="{e(x['name'] + ' ' + x['place'] + ' ' + ' '.join(x['areas']) + ' ' + x['status'])}">
              <div class="wf-placeholder avatar">Photo</div>
              <div><h3><a href="#">{e(x['name'])}</a></h3><p class="meta-row"><span class="tag">{e(x['status'])}</span><span>{e(x['place'])}</span></p><p>{e(', '.join(x['areas']))}</p></div>
              <div class="list-actions"><a class="btn btn-small btn-secondary" href="#">{'Contact' if dirname == 'consultants' else 'View'}</a></div>
            </article>'''
        return out

    topic_opts = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in TOPICS.items())

    def listing(dirname, extra=''):
        return f'''<section data-listing>
              <form class="filter-bar" role="search">
                <div class="field"><label for="{dirname}-q">Name, skill or place</label><input type="search" id="{dirname}-q" data-filter="q" name="q"></div>
                {extra}
                <div class="field"><label for="{dirname}-t">Area of work</label><select id="{dirname}-t" data-filter="topic"><option value="">Any area</option>{topic_opts}</select></div>
              </form>
              <p class="result-count" data-count aria-live="polite"></p>
              <div>{items(dirname)}</div>
              <p class="empty-state" data-empty hidden>Nobody matches. Try a broader search.</p>
            </section>'''

    status_sel = '''<div class="field"><label for="register-s">Professional status</label><select id="register-s" data-filter="status"><option value="">Any status</option><option value="cstat">Chartered Statistician (CStat)</option><option value="gradstat">Graduate Statistician (GradStat)</option><option value="data-analyst">Data Analyst</option></select></div>'''
    body = f'''
      <h1>Find an expert</h1>
      <p class="lead">Check someone's professional status, or find a qualified statistician to work with.</p>
      <div class="tabs" role="tablist">
        <button class="tab active" type="button" data-tab="d-register" data-tab-key="register">Professional Register</button>
        <button class="tab" type="button" data-tab="d-consultants" data-tab-key="consultants">Consultants Directory</button>
        <button class="tab" type="button" data-tab="d-fellows" data-tab-key="fellows">Fellows Directory (members)</button>
      </div>
      <div>
        <div class="tab-panel active" id="d-register">
          {listing('register', status_sel)}
          {n("Public register of CStat, GradStat and Data Analyst holders, searchable, showing AdvDSP and DSP. Ready for the AdvDSP to CDSP rename.", "REQ-192")}
        </div>
        <div class="tab-panel" id="d-consultants">
          {listing('consultants')}
          {n("Members offering statistical consultancy, searchable by area of work, name and place. Members manage their own listing in MyRSS; staff approve it.", "REQ-194, REQ-196")}
        </div>
        <div class="tab-panel" id="d-fellows">
          <div data-show-for="guest registered lapsed" class="locked"><h2>For members only</h2><p>The Fellows Directory lists members who have chosen to be included. <a href="~/pages/sign-in.html">Sign in</a> or <a href="~/pages/join.html">join</a> to search it.</p></div>
          <div data-show-for="member" hidden>{listing('fellows')}</div>
          {n("Visible only to signed-in members. Non-members see what it is and how to get access, instead of being sent back to the home page. Switch View as to Member to see it.", "REQ-193, REQ-178")}
        </div>
      </div>
      {n("A single 'Find an expert' search across all directories is ClerksWell's suggestion REQ-284 (a Could). Here the directories share one page and one search pattern.", "REQ-284", "Proposed")}
'''
    page('find-an-expert.html', 'Find an expert', body, 'resources', [('Resources', '~/pages/resources.html'), ('Find an expert', None)])


def jobs():
    n = Notes()
    items = ''
    for j in sorted(JOBS, key=lambda x: (not x.get('featured'), x['closes'])):
        feat = '<span class="tag tag-strong">Featured</span>' if j.get('featured') else ''
        items += f'''<article class="list-item" data-item data-topic="{' '.join(j['topics'])}" data-contract="{e(j['contract'].split(',')[0].lower().replace(' ', '-'))}" data-date="{j['closes']}" data-title="{e(j['title'])}" data-text="{e(j['title'] + ' ' + j['employer'] + ' ' + j['place'])}">
              <div class="wf-placeholder logo">Employer logo</div>
              <div><p class="meta-row">{feat}{tags(j['topics'])}</p><h3><a href="~/pages/job.html">{e(j['title'])}</a></h3>
                <p class="meta-row"><span><strong>{e(j['employer'])}</strong></span><span>{e(j['place'])}</span><span>{e(j['salary'])}</span><span>{e(j['contract'])}</span></p>
                <p class="wf-meta">Closes {d(j['closes'])}</p></div>
              <div class="list-actions"><a class="btn btn-small btn-secondary" href="~/pages/job.html">View job</a></div>
            </article>'''
    topic_opts = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in TOPICS.items())
    body = f'''
      <h1>Jobs</h1>
      <div class="split">
        <section data-listing>
          <form class="filter-bar" role="search">
            <div class="field"><label for="j-q">Keyword or employer</label><input type="search" id="j-q" data-filter="q"></div>
            <div class="field"><label for="j-t">Sector</label><select id="j-t" data-filter="topic"><option value="">All sectors</option>{topic_opts}</select></div>
            <div class="field"><label for="j-c">Contract</label><select id="j-c" data-filter="contract"><option value="">Any</option><option value="permanent">Permanent</option><option value="fixed-term">Fixed term</option><option value="graduate-scheme">Graduate scheme</option></select></div>
          </form>
          <p class="result-count" data-count aria-live="polite"></p>
          <div>{items}</div>
          <p class="empty-state" data-empty hidden>No jobs match. <a href="#">Set up a job alert</a>.</p>
          {n("Recent posts with salary, location and employer. Featured (paid) posts come first. Each job unpublishes itself on its closing date.", "REQ-249, REQ-088")}
        </section>
        <aside class="stack" id="advertise">
          <div class="panel surface"><h2 class="h4">Advertise a job</h2>
            <dl class="summary-list"><dt>Standard</dt><dd>£[price], 30 days</dd><dt>Featured</dt><dd>£[price], top of the list and in the newsletter</dd></dl>
            <a class="btn btn-block" href="#">Post a job</a></div>
          {n("Employers submit and pay online; staff review before publishing. Prices are placeholders.", "REQ-095, REQ-088, REQ-116")}
          <div class="panel"><h2 class="h4">Careers advice</h2><ul class="stack"><li><a href="#">Careers in statistics</a></li><li><a href="#">Career profiles</a></li></ul></div>
          {n("'Advertise with us' and careers content sit within the Jobs section.", "REQ-251")}
        </aside>
      </div>
'''
    page('jobs.html', 'Jobs', body, 'resources', [('Resources', '~/pages/resources.html'), ('Jobs', None)])


def job():
    n = Notes()
    j = JOBS[0]
    body = f'''
      <article class="split">
        <div>
          <p class="meta-row"><span class="tag tag-strong">Featured</span>{tags(j['topics'])}</p>
          <h1>{e(j['title'])}</h1>
          <p class="lead">{e(j['employer'])}</p>
          <div class="prose">
            <h2>About the role</h2>
            <p>You will lead the statistical analysis for the Trust's clinical audit programme and advise clinicians on study design. You will supervise two analysts and work closely with the research and development team.</p>
            <h2>What we are looking for</h2>
            <ul><li>A degree in statistics or a related subject</li><li>Experience of R or Stata</li><li>GradStat or CStat, or working towards it</li></ul>
          </div>
        </div>
        <aside class="panel surface">
          <dl class="summary-list"><dt>Location</dt><dd>{e(j['place'])}</dd><dt>Salary</dt><dd>{e(j['salary'])}</dd><dt>Contract</dt><dd>{e(j['contract'])}</dd><dt>Closes</dt><dd>{d(j['closes'])}</dd></dl>
          <a class="btn btn-block" href="#">Apply now</a>
          <p class="wf-meta">Applications are made on the employer's website.</p>
          {n("Job detail with description and Apply now. Search engines are notified when the job is posted and removed.", "REQ-250, REQ-156, REQ-057")}
        </aside>
      </article>
'''
    page('job.html', j['title'], body, 'resources', [('Resources', '~/pages/resources.html'), ('Jobs', '~/pages/jobs.html'), (j['title'], None)])


def about():
    n = Notes()
    body = f'''
      <div class="with-sidenav">
        <nav class="sidenav" aria-label="About">
          <h2>About</h2>
          <ul>
            <li><a href="~/pages/about.html" aria-current="page">Who we are</a></li>
            <li><a href="#strategy">Strategy</a></li>
            <li><a href="#governance">Governance</a></li>
            <li><a href="#reports">Annual reports</a></li>
            <li><a href="#advertise">Advertise with us</a></li>
            <li><a href="#contact">Contact us</a></li>
          </ul>
        </nav>
        <div class="prose">
          <h1>About the Royal Statistical Society</h1>
          <p class="lead">We are a professional body for statisticians and data scientists, and a charity that promotes statistics for the public good. We were founded in 1834 and received our royal charter in 1887.</p>
          <h2 id="strategy">Our strategy</h2>
          <p>Our strategy has four aims: to support statisticians and data scientists throughout their careers, to advance the discipline, to promote statistical literacy, and to influence policy.</p>
          <h2 id="governance">Governance</h2>
          <p>The Society is governed by its Council, elected by the membership, and supported by committees and staff.</p>
          <div class="accordion"><div class="accordion-item"><button class="accordion-title" type="button">Council and trustees <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>List of trustees with roles and terms.</p></div></div><div class="accordion-item"><button class="accordion-title" type="button">Committees <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>Committees and their terms of reference.</p></div></div></div>
          <h2 id="reports">Annual reports</h2>
          <ul><li><a href="#">Annual report and accounts 2025 (PDF, 2.1 MB)</a></li><li><a href="#">Annual report and accounts 2024 (PDF, 1.9 MB)</a></li></ul>
          <h2 id="advertise">Advertise with us</h2>
          <p>Banner and sponsored placements on the website and in newsletters.</p>
          {n("Advertising slots with impression and click-through reporting.", "REQ-093, REQ-116")}
          <h2 id="contact">Contact us</h2>
          <form class="panel" data-validate novalidate>
            <div class="field"><label for="c-topic">What is it about?</label><select id="c-topic" name="topic" required><option value="">Choose a topic</option><option>Membership</option><option>Events and training</option><option>Professional status</option><option>Media enquiry</option><option>Something else</option></select></div>
            <div class="field"><label for="c-name">Name</label><input type="text" id="c-name" name="name" required></div>
            <div class="field"><label for="c-email">Email</label><input type="email" id="c-email" name="email" required></div>
            <div class="field"><label for="c-msg">Message</label><textarea id="c-msg" name="msg" rows="5" required></textarea></div>
            <button class="btn" type="submit">Send</button>
            <p class="form-success" hidden>Thank you. We have emailed you a copy and will reply within three working days.</p>
          </form>
          {n("Each topic goes to the right team. A confirmation email is sent automatically.", "REQ-150, REQ-082, REQ-085")}
          <h2 id="security">Report a security issue</h2>
          <p>If you think you have found a vulnerability in our website, <a href="#">report it using this form</a>. Please do not disclose it publicly until we have responded.</p>
          {n("Vulnerability reporting form, linked from the footer.", "REQ-069")}
        </div>
      </div>
'''
    page('about.html', 'About the RSS', body, 'about', [('About', None)])


def sign_in():
    n = Notes()
    body = f'''
      <div class="split">
        <div>
          <h1>Sign in to MyRSS</h1>
          <div class="tabs" role="tablist">
            <button class="tab active" type="button" data-tab="si-signin">Sign in</button>
            <button class="tab" type="button" data-tab="si-register">Create an account</button>
          </div>
          <div>
            <div class="tab-panel active" id="si-signin">
              <form class="form-step" data-validate novalidate>
                <div class="field"><label for="si-email">Email address</label><input type="email" id="si-email" name="email" required autocomplete="username"></div>
                <div class="field"><label for="si-pass">Password</label><input type="password" id="si-pass" name="password" required autocomplete="current-password"><p class="field-hint"><a href="#" data-modal-open="reset-modal">Forgotten your password?</a></p></div>
                <button class="btn" type="submit">Sign in</button>
                <p class="form-success" hidden>Enter the 6-digit code from your authenticator app. <span class="wf-meta">(prototype: use the demo links instead)</span></p>
              </form>
              {n("Members and registered users sign in with email and password, with app-based MFA. The identity provider is still to be decided.", "REQ-075, REQ-081")}
              {n("Which identity provider (Entra External ID or another), is MFA required or optional for members, and are existing passwords migrated or reset?", "REQ-075, REQ-148", "Open question")}
            </div>
            <div class="tab-panel" id="si-register">
              <form class="form-step" data-validate novalidate>
                <p>Create a free account to book events and courses. You can upgrade to membership at any time.</p>
                <div class="field-row"><div class="field"><label for="r-first">First name</label><input type="text" id="r-first" name="first" required></div><div class="field"><label for="r-last">Last name</label><input type="text" id="r-last" name="last" required></div></div>
                <div class="field"><label for="r-email">Email address</label><input type="email" id="r-email" name="email" required></div>
                <div class="field"><label for="r-pass">Password</label><input type="password" id="r-pass" name="password" required></div>
                <button class="btn" type="submit">Create account</button>
                <p class="form-success" hidden>Check your email to confirm your account.</p>
              </form>
              {n("A non-member can create a basic account and later upgrade to full membership without re-entering details.", "REQ-076")}
            </div>
          </div>
        </div>
        <aside class="panel surface">
          <h2 class="h4">Prototype: sign in as</h2>
          <ul class="stack">
            <li><a href="~/pages/myrss.html" data-sign-in-as="member">A member (CStat)</a></li>
            <li><a href="~/pages/myrss.html" data-sign-in-as="registered">A registered non-member</a></li>
            <li><a href="~/pages/myrss.html" data-sign-in-as="lapsed">A lapsed member</a></li>
          </ul>
          <hr>
          <p><a href="#">RSS staff and volunteers: sign in with Microsoft</a></p>
          {n("Staff and key volunteers sign in to the CMS and portal with their RSS Microsoft 365 account (Entra ID), with MFA.", "REQ-074, REQ-078")}
        </aside>
      </div>
      <div class="wf-modal" id="reset-modal" role="dialog" aria-modal="true" aria-labelledby="reset-title">
        <div class="wf-modal-panel">
          <button class="wf-modal-close" type="button" aria-label="Close">&times;</button>
          <h2 id="reset-title">Reset your password</h2>
          <form data-validate novalidate>
            <div class="field"><label for="reset-email">Email address</label><input type="email" id="reset-email" name="email" required></div>
            <button class="btn" type="submit">Send reset link</button>
            <p class="form-success" hidden>If an account exists for that address, we have sent a link. It expires in 30 minutes.</p>
          </form>
          {n("Self-service reset with a time-limited link.", "REQ-080, REQ-150")}
        </div>
      </div>
'''
    page('sign-in.html', 'Sign in', body, '', [('Sign in', None)])


def myrss_shell(current, inner, n, title):
    links = [('myrss.html', 'Dashboard'), ('myrss-profile.html', 'Profile and directory listings'), ('myrss-bookings.html', 'My events and training'),
             ('myrss-cpd.html', 'CPD record'), ('myrss-groups.html', 'Sections and groups'), ('myrss-preferences.html', 'Newsletters and preferences')]
    cur = ' aria-current="page"'
    lis = ''.join(f'<li><a href="~/pages/{f}"{cur if f == current else ""}>{e(t)}</a></li>' for f, t in links)
    return f'''
      <div data-show-for="guest" class="locked">
        <h1>MyRSS</h1>
        <p>Sign in to manage your membership, bookings, CPD and preferences.</p>
        <p><a class="btn" href="~/pages/sign-in.html">Sign in</a> <a href="~/pages/sign-in.html">Create an account</a></p>
        {n("Signed-out visitors see what MyRSS is and how to get in, rather than being redirected. Use View as in the grey bar to see the signed-in versions.", "REQ-178")}
      </div>
      <div class="myrss-layout" data-show-for="registered member lapsed" hidden>
        <nav class="sidenav" aria-label="MyRSS">
          <h2>MyRSS</h2>
          <ul>{lis}<li><a href="~/pages/home.html" data-sign-out>Sign out</a></li></ul>
        </nav>
        <div>
          <h1>{e(title)}</h1>
{inner}
        </div>
      </div>
'''


def myrss():
    n = Notes()
    inner = f'''
          <!-- Member banner (REQ-179) -->
          <div class="member-banner" data-show-for="member" hidden>
            <div class="wf-placeholder avatar">Photo</div>
            <div><p><strong>Dr Alex Morgan</strong> <span class="status-pill">Active</span></p><p class="meta-row"><span>Fellow, Chartered Statistician (CStat)</span><span>Full rate</span><span>Membership no. 01234567</span></p><p class="wf-meta">Renews 1 January 2027 by Direct Debit</p></div>
            <div class="stack"><a href="~/pages/myrss-profile.html">Edit profile</a><a href="#applications">Apply for professional status</a><a href="#">Download e-certificate</a></div>
          </div>
          <div class="member-banner" data-show-for="lapsed" hidden>
            <div class="wf-placeholder avatar">Photo</div>
            <div><p><strong>Chris Patel</strong> <span class="status-pill warn">Lapsed</span></p><p class="meta-row"><span>Fellow</span><span>Membership no. 07654321</span></p><p class="wf-meta">Lapsed on 30 September 2026</p></div>
            <div class="stack"><a href="~/pages/myrss-profile.html">Edit profile</a></div>
          </div>
          <div class="member-banner" data-show-for="registered" hidden>
            <div class="wf-placeholder avatar">Photo</div>
            <div><p><strong>Sam Green</strong> <span class="status-pill">Registered account</span></p><p class="wf-meta">You can book events and courses. Membership adds journals, member prices and professional status.</p></div>
            <div><a class="btn" href="~/pages/join.html">Become a member</a></div>
          </div>
          {n("Banner with name, membership type, category and number, quick links and the e-certificate. Content changes by membership status.", "REQ-179, REQ-177, REQ-178")}

          <!-- Outstanding balance and renewal (REQ-181, REQ-188) -->
          <section id="renew" class="panel" data-show-for="lapsed" hidden>
            <h2>Renew your membership</h2>
            <p>Outstanding: <strong>£165.00</strong> for 2026 to 2027 <span class="status-pill warn">Unpaid</span></p>
            <p><a class="btn" href="~/pages/basket.html">Pay now by card</a> <a class="btn btn-secondary" href="#">Set up Direct Debit</a></p>
            <p class="wf-meta">An invoice and receipt are emailed once paid. Journal access returns immediately.</p>
          </section>
          <section class="panel" data-show-for="member" hidden><p>No outstanding balance <span class="status-pill">Paid</span></p></section>
          {n("A dynamic balance area with a Pay now route and clear payment status. Renewal by card or Direct Debit, with the renewals email sequence running in the background.", "REQ-181, REQ-188, REQ-151")}

          <div class="dash-grid" style="margin-top:1.5rem">
            <article class="card"><h2 class="card-title">My bookings</h2><p class="card-text">Introduction to R, 10 to 11 November 2026, online <span class="status-pill">Paid</span></p><a class="card-link" href="~/pages/myrss-bookings.html">All bookings</a></article>
            <article class="card" data-show-for="member lapsed"><h2 class="card-title">My publications</h2><p class="card-text" data-show-for="member">Series A, B and C online <span class="status-pill">Active</span></p><p class="card-text" data-show-for="lapsed" hidden>Access paused until you renew</p><a class="card-link" href="~/pages/publications.html">Read journals</a></article>
            <article class="card" data-show-for="member lapsed"><h2 class="card-title">CPD this year</h2><p class="card-text">18 of 30 hours recorded</p><a class="card-link" href="~/pages/myrss-cpd.html">Your CPD record</a></article>
            <article class="card" data-show-for="member lapsed"><h2 class="card-title">My sections and groups</h2><p class="card-text">Medical Section, Merseyside Local Group</p><a class="card-link" href="~/pages/myrss-groups.html">Manage</a></article>
            <article class="card"><h2 class="card-title">Newsletters</h2><p class="card-text">2 newsletters</p><a class="card-link" href="~/pages/myrss-preferences.html">Preferences</a></article>
            <article class="card" data-show-for="member" hidden id="applications"><h2 class="card-title">Applications</h2><p class="card-text">No applications in progress.</p><a class="card-link" href="#">Apply for GradStat, CStat or Data Analyst</a></article>
          </div>
          {n("Existing MyRSS self-service functions, regrouped as a dashboard: profile, newsletter preferences, bookings, directory inclusion and payments. All read and write Dynamics in near real time.", "REQ-173, REQ-176, REQ-180, REQ-199")}

          <section style="margin-top:2rem" data-show-for="member" hidden aria-labelledby="rec">
            <h2 class="section-title" id="rec">For you</h2>
            <div class="grid grid-3">
              <article class="card"><div class="wf-placeholder ratio-16-9">Video 16:9</div><p class="meta-row"><span class="tag">Members only</span></p><h3 class="card-title"><a href="#">Recording: Statistics and the climate emergency</a></h3></article>
              <article class="card"><p class="meta-row"><span class="tag">Event</span></p><h3 class="card-title"><a href="~/pages/event.html">Medical Section: Estimands in clinical trials</a></h3><p class="card-text">12 November 2026, online</p></article>
              <article class="card"><p class="meta-row"><span class="tag">Course</span></p><h3 class="card-title"><a href="~/pages/course.html">Survival analysis</a></h3><p class="card-text">14 to 15 January 2027</p></article>
            </div>
            {n("Restricted content (recordings, training resources) and recommendations based on membership type and interests.", "REQ-183, REQ-109, REQ-111")}
          </section>

          <section id="information-centre" style="margin-top:2rem" data-show-for="member" hidden aria-labelledby="ic">
            <h2 class="section-title" id="ic">Information centre</h2>
            <form class="filter-bar" role="search"><div class="field"><label for="ic-q">Search documents</label><input type="search" id="ic-q"></div><div class="field"><label for="ic-d">Date</label><select id="ic-d"><option>Any time</option><option>Past year</option></select></div></form>
            <ul class="stack" style="margin-top:1rem"><li><a href="#">CPD guidance for CStat holders (PDF)</a> <span class="wf-meta">March 2026</span></li><li><a href="#">Code of conduct (PDF)</a> <span class="wf-meta">January 2026</span></li></ul>
            {n("Searchable repository of member documents.", "REQ-185")}
          </section>

          <section class="panel" style="margin-top:2rem" data-show-for="member" hidden>
            <h2 class="h4">Member community</h2><p>Profiles, discussion forum and messaging between members.</p>
            {n("Community features are a large piece of work in their own right. Agree scope or phasing in Define before this is designed.", "REQ-184", "Open question")}
          </section>
'''
    page('myrss.html', 'MyRSS', myrss_shell('myrss.html', inner, n, 'Dashboard'), '', [('MyRSS', None)])


def myrss_profile():
    n = Notes()
    topic_checks = ''.join(f'<label class="check"><input type="checkbox" name="interests" value="{k}"{" checked" if k in ("health", "methods") else ""}> {e(v)}</label>' for k, v in TOPICS.items())
    inner = f'''
          <p class="lead">Keep your details up to date. Each section saves on its own.</p>
          {n("The current single page of 102 fields with five Submit buttons is split into short sections, each with its own save. This layout is ClerksWell's suggestion REQ-282; the functions are the existing ones.", "REQ-173, REQ-282")}
          <div class="accordion">
            <div class="accordion-item open"><button class="accordion-title" type="button">Personal details <span class="accordion-icon" aria-hidden="true">&#9662;</span></button>
              <div class="accordion-content"><form data-validate novalidate>
                <div class="field-row"><div class="field"><label for="p-first">First name</label><input type="text" id="p-first" name="first" value="Alex" required></div><div class="field"><label for="p-last">Last name</label><input type="text" id="p-last" name="last" value="Morgan" required></div></div>
                <div class="field"><label for="p-email">Email</label><input type="email" id="p-email" name="email" value="alex.morgan@example.org" required></div>
                <button class="btn btn-small" type="submit">Save personal details</button><p class="form-success" hidden>Saved.</p></form></div></div>
            <div class="accordion-item"><button class="accordion-title" type="button">Address <span class="accordion-icon" aria-hidden="true">&#9662;</span></button>
              <div class="accordion-content"><form data-validate novalidate><div class="field"><label for="p-post">Postcode</label><div class="inline-field"><input type="text" id="p-post" name="postcode" value="EC1Y 8LX" required><button class="btn btn-secondary btn-small" type="button">Find address</button></div></div><button class="btn btn-small" type="submit">Save address</button><p class="form-success" hidden>Saved.</p></form></div></div>
            <div class="accordion-item"><button class="accordion-title" type="button">Employment <span class="accordion-icon" aria-hidden="true">&#9662;</span></button>
              <div class="accordion-content"><form data-validate novalidate><div class="field"><label for="p-emp">Employer</label><input type="text" id="p-emp" name="employer" value="Northbridge NHS Foundation Trust"></div><div class="field"><label for="p-role">Job title</label><input type="text" id="p-role" name="role" value="Head of Statistics"></div><button class="btn btn-small" type="submit">Save employment</button><p class="form-success" hidden>Saved.</p></form></div></div>
            <div class="accordion-item"><button class="accordion-title" type="button">Interests <span class="accordion-icon" aria-hidden="true">&#9662;</span></button>
              <div class="accordion-content"><form data-validate novalidate><fieldset class="field"><legend>Topics you are interested in</legend>{topic_checks}</fieldset><button class="btn btn-small" type="submit">Save interests</button><p class="form-success" hidden>Saved. Your recommendations will update.</p></form>
              {n("Interests use the same topic list as site content, so they can drive personalisation and newsletters.", "REQ-109, REQ-282")}
              {n("Can the 29 areas of specialisation in Dynamics be replaced by the shared topic list, and what happens to existing data?", "REQ-109", "Open question")}</div></div>
            <div class="accordion-item"><button class="accordion-title" type="button">Directory listings <span class="accordion-icon" aria-hidden="true">&#9662;</span></button>
              <div class="accordion-content"><form data-validate novalidate>
                <label class="check"><input type="checkbox" name="dir" value="fellows" checked> Include me in the Fellows Directory (members only)</label>
                <label class="check"><input type="checkbox" name="dir" value="register" checked> Show me on the public Professional Register</label>
                <label class="check"><input type="checkbox" name="dir" value="consultants" data-reveal="consultant-detail"> List me in the Consultants Directory</label>
                <div class="reveal" id="consultant-detail" hidden><div class="field"><label for="p-cons">Areas of consultancy</label><textarea id="p-cons" name="cons" rows="3"></textarea></div><p class="wf-meta">Listings are checked by staff before they appear.</p></div>
                <button class="btn btn-small" type="submit">Save listings</button><p class="form-success" hidden>Saved.</p></form>
              {n("Members manage their own directory listings.", "REQ-196, REQ-194")}</div></div>
          </div>
'''
    page('myrss-profile.html', 'Profile', myrss_shell('myrss-profile.html', inner, n, 'Profile and directory listings'), '', [('MyRSS', '~/pages/myrss.html'), ('Profile', None)])


def myrss_bookings():
    n = Notes()
    inner = f'''
          <div class="tabs" role="tablist">
            <button class="tab active" type="button" data-tab="b-up">Upcoming</button>
            <button class="tab" type="button" data-tab="b-past">Past</button>
          </div>
          <div>
            <div class="tab-panel active" id="b-up">
              <table class="data-table"><thead><tr><th scope="col">Event or course</th><th scope="col">Date</th><th scope="col">Status</th><th scope="col"></th></tr></thead><tbody>
                <tr><td><a href="~/pages/course.html">Introduction to R</a><br><span class="wf-meta">Online. Joining link emailed 9 November</span></td><td>10 to 11 Nov 2026</td><td><span class="status-pill">Paid</span></td><td><a href="#">Add to calendar</a></td></tr>
                <tr><td><a href="~/pages/event.html">Discussion meeting: evaluating large language models</a><br><span class="wf-meta">In person</span></td><td>4 Nov 2026</td><td><span class="status-pill">Free</span></td><td><a href="#">Cancel</a></td></tr>
                <tr><td><a href="~/pages/conference.html">RSS Conference 2027: full</a></td><td>6 to 9 Sep 2027</td><td><span class="status-pill warn">Invoice unpaid</span></td><td><a class="btn btn-small" href="~/pages/basket.html">Pay invoice</a></td></tr>
              </tbody></table>
            </div>
            <div class="tab-panel" id="b-past">
              <table class="data-table"><thead><tr><th scope="col">Event or course</th><th scope="col">Date</th><th scope="col">CPD</th><th scope="col"></th></tr></thead><tbody>
                <tr><td>Statistics and the climate emergency</td><td>14 Oct 2026</td><td>2 hours</td><td><a href="#">Watch recording</a></td></tr>
                <tr><td>Practical survey design (course no longer offered)</td><td>3 Jun 2025</td><td>6 hours</td><td><a href="#">Certificate</a></td></tr>
              </tbody></table>
            </div>
          </div>
          {n("My Events and My Training in one place: booked, past and related items, with clear payment status and a prominent route to pay an outstanding invoice. Training history comes from Dynamics, so courses that are no longer published still appear.", "REQ-180, REQ-208, REQ-219")}
'''
    page('myrss-bookings.html', 'My events and training', myrss_shell('myrss-bookings.html', inner, n, 'My events and training'), '', [('MyRSS', '~/pages/myrss.html'), ('My events and training', None)])


def myrss_cpd():
    n = Notes()
    inner = f'''
          <div class="results-bar"><p><strong>18 of 30 hours</strong> recorded for 2026</p><button class="btn" type="button" data-modal-open="cpd-modal">Add an activity</button></div>
          <table class="data-table"><thead><tr><th scope="col">Date</th><th scope="col">Activity</th><th scope="col">Type</th><th scope="col">Hours</th><th scope="col"></th></tr></thead><tbody>
            <tr><td>14 Oct 2026</td><td>Discussion meeting: Statistics and the climate emergency</td><td>Event</td><td>2</td><td><a href="#">Edit</a> &middot; <a href="#">Delete</a></td></tr>
            <tr><td>2 Sep 2026</td><td>Reviewed a paper for Series C</td><td>Professional activity</td><td>6</td><td><a href="#">Edit</a> &middot; <a href="#">Delete</a></td></tr>
            <tr><td>12 May 2026</td><td>Bayesian statistics with Stan</td><td>RSS course</td><td>10</td><td><a href="#">Edit</a> &middot; <a href="#">Delete</a></td></tr>
          </tbody></table>
          <form class="filter-bar" style="margin-top:1.5rem"><div class="field"><label for="cpd-from">From</label><input type="date" id="cpd-from" value="2026-01-01"></div><div class="field"><label for="cpd-to">To</label><input type="date" id="cpd-to" value="2026-12-31"></div><button class="btn btn-secondary" type="button">Download record (PDF)</button></form>
          {n("Add, edit and delete CPD activities, and download a record for any period. RSS courses and events are added automatically when attended.", "REQ-195")}
          <div class="wf-modal" id="cpd-modal" role="dialog" aria-modal="true" aria-labelledby="cpd-title">
            <div class="wf-modal-panel">
              <button class="wf-modal-close" type="button" aria-label="Close">&times;</button>
              <h2 id="cpd-title">Add a CPD activity</h2>
              <form data-validate novalidate>
                <div class="field"><label for="cpd-act">Activity</label><input type="text" id="cpd-act" name="act" required></div>
                <div class="field-row"><div class="field"><label for="cpd-date">Date</label><input type="date" id="cpd-date" name="date" required></div><div class="field"><label for="cpd-hrs">Hours</label><input type="number" id="cpd-hrs" name="hours" min="0.5" step="0.5" required></div></div>
                <div class="field"><label for="cpd-type">Type</label><select id="cpd-type" name="type"><option>Course or event</option><option>Professional activity</option><option>Self-directed learning</option></select></div>
                <button class="btn" type="submit">Add activity</button><p class="form-success" hidden>Added to your record.</p>
              </form>
            </div>
          </div>
'''
    page('myrss-cpd.html', 'CPD record', myrss_shell('myrss-cpd.html', inner, n, 'CPD record'), '', [('MyRSS', '~/pages/myrss.html'), ('CPD record', None)])


def myrss_groups():
    n = Notes()

    def rows(kind):
        return ''.join(f'<tr><td>{e(g["title"])}</td><td><label class="check"><input type="checkbox"{" checked" if g["id"] in ("medical", "merseyside") else ""}> Member</label></td><td><label class="check"><input type="checkbox"{" checked" if g["id"] == "medical" else ""}> Mailing list</label></td></tr>' for g in GROUPS if g['kind'] == kind)

    def table(kind):
        return f'<table class="data-table"><thead><tr><th scope="col">Group</th><th scope="col">Membership</th><th scope="col">Email</th></tr></thead><tbody>{rows(kind)}</tbody></table>'

    inner = f'''
          <div data-show-for="registered" class="locked">Sections and groups are free for members. <a href="~/pages/join.html">Become a member</a>.</div>
          <div data-show-for="member lapsed">
            <div class="tabs" role="tablist">
              <button class="tab active" type="button" data-tab="mg-s">Sections</button>
              <button class="tab" type="button" data-tab="mg-sig">Special interest groups</button>
              <button class="tab" type="button" data-tab="mg-l">Local groups</button>
            </div>
            <div>
              <div class="tab-panel active" id="mg-s">{table('section')}</div>
              <div class="tab-panel" id="mg-sig">{table('sig')}</div>
              <div class="tab-panel" id="mg-l">{table('local')}</div>
            </div>
            <p><button class="btn" type="button">Save changes</button></p>
          </div>
          {n("Members see their subscriptions and choose group mailing lists, in tabs for sections, SIGs and local groups.", "REQ-182, REQ-160")}
'''
    page('myrss-groups.html', 'Sections and groups', myrss_shell('myrss-groups.html', inner, n, 'Sections and groups'), '', [('MyRSS', '~/pages/myrss.html'), ('Sections and groups', None)])


def myrss_prefs():
    n = Notes()
    inner = f'''
          <form data-validate novalidate>
            <fieldset class="field"><legend>Newsletters</legend>
              <label class="check"><input type="checkbox" name="nl" checked> RSS monthly news</label>
              <label class="check"><input type="checkbox" name="nl" checked> Training and events</label>
              <label class="check"><input type="checkbox" name="nl"> Policy updates</label>
              <label class="check"><input type="checkbox" name="nl"> Careers and jobs</label>
            </fieldset>
            <fieldset class="field"><legend>Other communications</legend>
              <label class="check"><input type="checkbox" name="other"> Offers from partners</label>
              <label class="check"><input type="checkbox" name="other" checked> Requests to take part in research</label>
            </fieldset>
            <button class="btn" type="submit">Save preferences</button> <button class="btn-link" type="button">Unsubscribe from everything</button>
            <p class="form-success" hidden>Saved. Changes can take up to an hour to reach our mailing lists.</p>
          </form>
          {n("Opt-in and opt-out for every newsletter, recorded in Dynamics. Every newsletter carries an unsubscribe link back here.", "REQ-159, REQ-160, REQ-110")}
          {n("Newsletters are built in a drag-and-drop editor with templates that pull in upcoming events, training and tagged news, with reporting on every send.", "REQ-161, REQ-162, REQ-164, REQ-166", "CMS")}
          {n("Which platform sends the staff and group newsletters (Customer Insights or a dedicated tool)?", "REQ-110, REQ-158", "Open question")}
'''
    page('myrss-preferences.html', 'Newsletters and preferences', myrss_shell('myrss-preferences.html', inner, n, 'Newsletters and preferences'), '', [('MyRSS', '~/pages/myrss.html'), ('Preferences', None)])


def build():
    resources()
    journalists()
    experts()
    jobs()
    job()
    about()
    sign_in()
    myrss()
    myrss_profile()
    myrss_bookings()
    myrss_cpd()
    myrss_groups()
    myrss_prefs()
