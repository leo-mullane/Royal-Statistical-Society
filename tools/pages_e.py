"""Payment: hosted payment page, confirmation, and posting a job."""
import os
from urllib.parse import urlencode

from common import *


def pay_url(what, amount, desc, method='card'):
    return '~/pages/pay.html?' + e(urlencode({'for': what, 'amount': f'{amount:.2f}', 'desc': desc, 'method': method}))


def pay_page():
    n = Notes()
    out = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Secure payment | Royal Statistical Society (prototype)</title>
  <link rel="stylesheet" href="~/css/base.css">
  <link rel="stylesheet" href="~/css/components.css">
  <link rel="stylesheet" href="~/css/rss.css">
  <link rel="stylesheet" href="~/css/theme.css">
</head>
<body>
  <!-- @@include protobar.html -->
  <!-- Hosted payment page: belongs to the payment provider, not rss.org.uk (REQ-086, REQ-084) -->
  <div class="provider-bar">
    <div class="container provider-bar-inner">
      <span class="wf-placeholder logo">RSS logo</span>
      <span class="provider-name">Secure payment provided by [payment provider]</span>
    </div>
  </div>
  <main id="main" data-pay-page>
    <div class="container">
      <h1>Pay the Royal Statistical Society</h1>
      {n("This page is hosted by the payment provider (currently Elavon for cards, Access Paysuite for Direct Debit). RSS's site never handles card or bank details; it hands over the amount and reference, and the provider returns the result. Card payments use tokenisation, AVS, CVV and 3-D Secure.", "REQ-086, REQ-084, REQ-091", "Integration")}
      {n("Confirm the card provider and product (Elavon bought Opayo) and whether the hosted page can carry RSS branding.", "REQ-086, REQ-153", "Open question")}
      <div class="pay-layout">
        <div>
          <div class="tabs" role="tablist">
            <button class="tab active" type="button" data-tab="pay-card" data-tab-key="card">Card</button>
            <button class="tab" type="button" data-tab="pay-dd" data-tab-key="dd">Direct Debit</button>
          </div>
          <div>
            <div class="tab-panel active" id="pay-card">
              <div class="error-summary" data-declined hidden role="alert">
                <h2>Your payment was declined</h2>
                <p>Your bank did not authorise this payment, and you have not been charged. Check your card details or try another card.</p>
              </div>
              <form data-card-form novalidate>
                <div class="field"><label for="cc-name">Name on card</label><input type="text" id="cc-name" name="ccname" required autocomplete="cc-name"></div>
                <div class="field"><label for="cc-num">Card number</label><input type="text" id="cc-num" name="cardnumber" required inputmode="numeric" autocomplete="cc-number" placeholder="1234 5678 9012 3456"></div>
                <div class="card-row">
                  <div class="field"><label for="cc-exp">Expiry date (MM/YY)</label><input type="text" id="cc-exp" name="exp" required autocomplete="cc-exp" placeholder="MM/YY"></div>
                  <div class="field"><label for="cc-cvc">Security code</label><input type="text" id="cc-cvc" name="cvc" required inputmode="numeric" autocomplete="cc-csc"><p class="field-hint">The last 3 digits on the back</p></div>
                </div>
                <div class="field"><label for="cc-post">Billing postcode</label><input type="text" id="cc-post" name="postcode" required autocomplete="postal-code"></div>
                <p><button class="btn" type="submit">Pay <span data-pay-amount></span></button> <a href="#" data-pay-back>Cancel and go back</a></p>
              </form>
              {n("Try any card number to see 3-D Secure and a successful payment, or one ending 0002 to see a decline. A declined or abandoned payment triggers the payment-unsuccessful or abandoned-application email.", "REQ-089, REQ-152")}
            </div>
            <div class="tab-panel" id="pay-dd">
              <form data-dd-form novalidate>
                <div class="field"><label for="dd-name">Account holder name</label><input type="text" id="dd-name" name="ddname" required></div>
                <div class="card-row">
                  <div class="field"><label for="dd-sort">Sort code</label><input type="text" id="dd-sort" name="sort" required inputmode="numeric" placeholder="00-00-00"></div>
                  <div class="field"><label for="dd-acc">Account number</label><input type="text" id="dd-acc" name="account" required inputmode="numeric"></div>
                </div>
                <div class="field"><label for="dd-sched">Collection</label><select id="dd-sched" name="schedule"><option>Annually, on 1 January</option><option>Quarterly instalments</option><option>Monthly</option></select></div>
                <div class="field"><label class="check"><input type="checkbox" name="sole" required data-error="Confirm you can authorise Direct Debits on this account"> I am the account holder and the only person needed to authorise Direct Debits from this account</label></div>
                <div class="dd-guarantee"><strong>The Direct Debit Guarantee</strong><p>This Guarantee is offered by all banks and building societies that accept instructions to pay Direct Debits. You will be told in advance of any change to the amount, date or frequency. You can cancel at any time by contacting your bank.</p></div>
                <p style="margin-top:1rem"><button class="btn" type="submit">Set up Direct Debit</button> <a href="#" data-pay-back>Cancel and go back</a></p>
              </form>
              {n("Mandate set up through Access Paysuite, with instalments where offered. Confirmation of the mandate is emailed within three working days, as the scheme requires. Webhooks update Dynamics.", "REQ-084, REQ-091, REQ-188", "Integration")}
            </div>
          </div>
        </div>
        <aside class="panel surface order-summary">
          <h2 class="h4">You are paying</h2>
          <p data-pay-desc></p>
          <p class="amount" data-pay-amount></p>
          <p class="wf-meta">Royal Statistical Society, 12 Errol Street, London</p>
        </aside>
      </div>
    </div>
  </main>
  <div class="wf-modal" id="three-ds" role="dialog" aria-modal="true" aria-labelledby="tds-title">
    <div class="wf-modal-panel">
      <h2 id="tds-title">Verify it's you</h2>
      <p>Your bank needs to confirm this payment. Approve it in your banking app, or enter the code we sent to your phone.</p>
      <div class="wf-placeholder embed">Your bank's 3-D Secure screen</div>
      <p style="margin-top:1rem"><button class="btn" type="button" data-3ds-approve>Approve payment</button></p>
    </div>
  </div>
  <script src="~/js/data.js"></script>
  <script src="~/js/wireframe.js"></script>
  <script src="~/js/rss.js"></script>
</body>
</html>
'''
    with open(os.path.join(SRC, 'pages', 'pay.html'), 'w', encoding='utf-8') as fh:
        fh.write(out)
    PAGES_BUILT.append('pay.html')


def complete_page():
    n = Notes()
    body = f'''
      <!-- Payment confirmation page (REQ-089, REQ-087) -->
      <section data-pay-complete class="split">
        <div>
          <div data-pay-method-block="card dd">
            <h1>Payment successful</h1>
            <p class="lead">Thank you. We have emailed your receipt.</p>
          </div>
          <div data-pay-method-block="invoice" hidden>
            <h1>Application received</h1>
            <p class="lead">We will email an invoice to your organisation. Your membership starts when it is paid.</p>
          </div>

          <div data-pay-for-block="join" hidden class="stack">
            <h2>Welcome to the Royal Statistical Society</h2>
            <p>Your membership number is <strong>01234567</strong>. Your welcome pack is on its way, and you can sign in to MyRSS now.</p>
            <p><a class="btn" href="~/pages/myrss.html">Go to MyRSS</a> <a href="~/pages/groups.html">Join a section or local group</a></p>
            {n("The onboarding email sequence starts, varying by member type.", "REQ-149")}
          </div>
          <div data-pay-for-block="renewal" hidden class="stack">
            <h2>Your membership is renewed</h2>
            <p>Thank you for staying with us. Your journal access and professional status continue without a break.</p>
            <p><a class="btn" href="~/pages/myrss.html">Back to MyRSS</a></p>
          </div>
          <div data-pay-for-block="course" hidden class="stack">
            <h2>Your place is booked</h2>
            <p>Joining instructions are on their way to the delegate. The course now appears in My Training.</p>
            <p><a class="btn" href="~/pages/myrss-bookings.html">View my bookings</a> <a href="#">Add to calendar</a></p>
          </div>
          <div data-pay-for-block="basket" hidden class="stack">
            <h2>Your order is confirmed</h2>
            <p>Your tickets and bookings are in MyRSS, with confirmation emails for each.</p>
            <p><a class="btn" href="~/pages/myrss-bookings.html">View my bookings</a></p>
          </div>
          <div data-pay-for-block="invoice" hidden class="stack">
            <h2>Invoice paid</h2>
            <p>Your booking status is now Paid.</p>
            <p><a class="btn" href="~/pages/myrss-bookings.html">Back to my bookings</a></p>
          </div>
          <div data-pay-for-block="donation" hidden class="stack">
            <h2>Thank you for your gift</h2>
            <p>Your donation supports statistical education and the public understanding of statistics. If you added Gift Aid, we have emailed a copy of your declaration.</p>
            <div class="share-row"><span class="wf-meta">Tell others:</span><a href="#">LinkedIn</a><a href="#">Bluesky</a><a href="#">Email</a></div>
          </div>
          <div data-pay-for-block="job" hidden class="stack">
            <h2>Your job advert is with us</h2>
            <p>We check every advert before it goes live, usually within one working day. We will email you when it is published.</p>
            <p><a class="btn" href="~/pages/jobs.html">Back to jobs</a></p>
          </div>
          {n("Every payment ends here, back on rss.org.uk: what happens next depends on what was bought. A confirmation email follows; free events have their own wording without payment language.", "REQ-089, REQ-150, REQ-152, REQ-207")}
        </div>
        <aside class="panel surface" aria-label="Receipt">
          <h2 class="h4">Receipt</h2>
          <dl class="summary-list">
            <dt>Item</dt><dd data-pay-desc></dd>
            <dt>Amount</dt><dd data-pay-amount></dd>
            <dt>Paid by</dt><dd data-pay-method></dd>
            <dt>Reference</dt><dd data-pay-ref></dd>
            <dt>Date</dt><dd>30 October 2026</dd>
          </dl>
          <p><a href="#">Download receipt (PDF)</a></p>
          {n("Downloadable receipt that meets HMRC requirements, with VAT shown where it applies. The transaction is written to Dynamics and the purchase is tracked in analytics.", "REQ-087, REQ-091, REQ-114, REQ-116")}
        </aside>
      </section>
'''
    page('payment-complete.html', 'Payment complete', body, '', [('Payment complete', None)])


def post_job():
    n = Notes()
    body = f'''
      <div class="split">
        <div>
          <h1>Advertise a job</h1>
          <p class="lead">Reach 10,000 statisticians and data scientists. Adverts run for 30 days.</p>
          <form class="form-step" data-validate data-pay-for="job" data-pay-desc="Job advert" novalidate>
            <fieldset class="field"><legend>Advert type</legend>
              <label class="radio-card"><input type="radio" name="tier" value="standard" data-price="250" required data-error="Choose an advert type"> <strong>Standard</strong>Listed for 30 days. £250</label>
              <label class="radio-card"><input type="radio" name="tier" value="featured" data-price="450"> <strong>Featured</strong>Top of the list, with your logo, and in the monthly newsletter. £450</label>
            </fieldset>
            <div class="field"><label for="pj-title">Job title</label><input type="text" id="pj-title" name="title" required></div>
            <div class="field-row">
              <div class="field"><label for="pj-emp">Employer</label><input type="text" id="pj-emp" name="employer" required></div>
              <div class="field"><label for="pj-loc">Location</label><input type="text" id="pj-loc" name="location" required></div>
            </div>
            <div class="field-row">
              <div class="field"><label for="pj-sal">Salary</label><input type="text" id="pj-sal" name="salary" required></div>
              <div class="field"><label for="pj-close">Closing date</label><input type="date" id="pj-close" name="closes" required></div>
            </div>
            <div class="field"><label for="pj-desc">Description</label><textarea id="pj-desc" name="desc" rows="6" required></textarea></div>
            <div class="field"><label for="pj-url">Link to apply</label><input type="url" id="pj-url" name="url" required></div>
            <div class="field"><label for="pj-logo">Logo (optional, featured adverts)</label><input type="file" id="pj-logo" name="logo" accept=".jpg,.png"></div>
            <p>Total: <strong data-total>£0</strong> (plus VAT)</p>
            <button class="btn" type="submit">Continue to payment</button>
          </form>
          {n("Employers submit and pay online; staff review before the advert is published. It unpublishes itself on the closing date. Prices are placeholders.", "REQ-088, REQ-095, REQ-116")}
        </div>
        <aside class="panel surface"><h2 class="h4">Need an invoice?</h2><p>Recruitment agencies and employers with an account can pay by invoice. <a href="~/pages/about.html#contact">Contact us</a>.</p></aside>
      </div>
'''
    page('post-job.html', 'Advertise a job', body, 'resources', [('Resources', '~/pages/resources.html'), ('Jobs', '~/pages/jobs.html'), ('Advertise a job', None)])


def build():
    pay_page()
    complete_page()
    post_job()
