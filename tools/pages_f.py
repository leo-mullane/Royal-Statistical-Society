"""Get involved: honours, Statistical Ambassadors, Statisticians for Society."""
from common import *

GI_NAV = [('get-involved.html', 'Overview'), ('groups.html', 'Sections and groups'), ('get-involved.html#volunteering', 'Volunteering'),
          ('honours.html', 'Honours and awards'), ('statistical-ambassadors.html', 'Statistical Ambassadors'),
          ('statisticians-for-society.html', 'Statisticians for Society'), ('donate.html', 'Donate')]


def gi_sidenav(current):
    cur = ' aria-current="page"'
    lis = ''.join(f'<li><a href="~/pages/{f}"{cur if f == current else ""}>{e(t)}</a></li>' for f, t in GI_NAV)
    return f'<nav class="sidenav" aria-label="Get involved"><h2>Get involved</h2><ul>{lis}</ul></nav>'


def honours():
    n = Notes()
    body = f'''
      <div class="with-sidenav">
        {gi_sidenav('honours.html')}
        <article>
          <h1>Honours and awards</h1>
          <p class="lead">Each year the Society recognises outstanding contributions to statistics and data science, from lifetime achievement to early-career research.</p>
          {n("Standard content page in the Get involved section. The list of honours and their criteria is to be supplied by RSS.", "REQ-029, REQ-011", "CMS")}
          <section class="panel surface"><h2 class="h4">Nominations for 2027</h2><p>Nominations are open until 31 January 2027. Anyone may nominate a member; self-nominations are not accepted.</p>
            <p><a class="btn" href="#">Download the nomination form (Word)</a></p></section>
          {n("Online nomination and entry forms, replacing the Word download, are ClerksWell's suggestion REQ-287 (a Could), so they are not built.", "REQ-287", "Proposed")}
          <h2>Our honours</h2>
          <div class="accordion">
            <div class="accordion-item"><button class="accordion-title" type="button">The Guy Medals (Gold, Silver and Bronze) <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>The Society's highest honours, for contributions to statistics. Criteria and past winners to be supplied by RSS.</p></div></div>
            <div class="accordion-item"><button class="accordion-title" type="button">Other medals and prizes <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>The full list, with criteria and past winners, to be supplied by RSS.</p></div></div>
            <div class="accordion-item"><button class="accordion-title" type="button">Honorary Fellowship <span class="accordion-icon" aria-hidden="true">&#9662;</span></button><div class="accordion-content"><p>Placeholder text to be supplied by RSS.</p></div></div>
          </div>
          <h2>Past winners</h2>
          <p>An archive of past winners, searchable by year and award, will sit here.</p>
        </article>
      </div>
'''
    page('honours.html', 'Honours and awards', body, 'get-involved', [('Get involved', '~/pages/get-involved.html'), ('Honours and awards', None)])


def ambassadors():
    n = Notes()
    body = f'''
      <div class="with-sidenav">
        {gi_sidenav('statistical-ambassadors.html')}
        <article>
          <h1>Statistical Ambassadors</h1>
          <p class="lead">Members trained to explain statistics in the media, in schools and in public debate.</p>
          <div class="grid grid-3">
            <article class="card"><h2 class="card-title">For journalists</h2><p class="card-text">Need someone to explain the numbers? Our press office will put you in touch.</p><a class="card-link" href="~/pages/for-journalists.html">Media enquiries</a></article>
            <article class="card"><h2 class="card-title">For schools</h2><p class="card-text">Invite an ambassador to talk to students about careers and data.</p><a class="card-link" href="~/pages/about.html#contact">Request a visit</a></article>
            <article class="card"><h2 class="card-title">Become an ambassador</h2><p class="card-text">Applications for 2027 close on 30 November 2026. Training is provided.</p><a class="card-link" href="~/pages/article.html">How to apply</a></article>
          </div>
          <h2>Next training day</h2>
          <p><a href="~/pages/event.html">Statistical Ambassadors training day</a>, 20 January 2027, London.</p>
          {n("Programme page built from standard components; the call for volunteers is a news item with a closing date.", "REQ-013, REQ-016")}
        </article>
      </div>
'''
    page('statistical-ambassadors.html', 'Statistical Ambassadors', body, 'get-involved', [('Get involved', '~/pages/get-involved.html'), ('Statistical Ambassadors', None)])


def s4s():
    n = Notes()
    body = f'''
      <div class="with-sidenav">
        {gi_sidenav('statisticians-for-society.html')}
        <article>
          <h1>Statisticians for Society</h1>
          <p class="lead">Free statistical help for charities and community groups, from volunteer members.</p>
          <div class="grid grid-2">
            <article class="card"><h2 class="card-title">Charities: ask for help</h2><p class="card-text">Tell us about your project and the help you need. We match you with a volunteer.</p>
              <form data-validate novalidate>
                <div class="field"><label for="s4s-org">Organisation</label><input type="text" id="s4s-org" name="org" required></div>
                <div class="field"><label for="s4s-email">Email</label><input type="email" id="s4s-email" name="email" required></div>
                <div class="field"><label for="s4s-need">What do you need help with?</label><textarea id="s4s-need" name="need" rows="4" required></textarea></div>
                <button class="btn" type="submit">Send request</button>
                <p class="form-success" hidden>Thank you. We'll be in touch within ten working days.</p>
              </form></article>
            <article class="card"><h2 class="card-title">Members: volunteer</h2><p class="card-text">Give a few hours to a project that matches your skills. Volunteering counts towards CPD.</p>
              <p data-show-for="member" hidden><a class="btn" href="#">Register as a volunteer</a></p>
              <p data-show-for="guest registered lapsed"><a href="~/pages/sign-in.html">Sign in</a> as a member to volunteer.</p></article>
          </div>
          {n("Requests go to the programme team through the form builder, with spam protection.", "REQ-082, REQ-085")}
        </article>
      </div>
'''
    page('statisticians-for-society.html', 'Statisticians for Society', body, 'get-involved', [('Get involved', '~/pages/get-involved.html'), ('Statisticians for Society', None)])


def build():
    honours()
    ambassadors()
    s4s()
