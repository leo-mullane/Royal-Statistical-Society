# RSS website requirements: prototype trace

Generated from the draft requirements catalogue (ClerksWell review copy). The catalogue is being revised; this trace will be regenerated from the revised set.

Only Must and Should requirements are prototyped. "Shown in" lists the source files whose annotations reference the requirement; "not shown" usually means a platform, CMS or non-functional requirement with no front-end expression.

## Must

| Ref | Type | Area | Requirement | Shown in |
| --- | --- | --- | --- | --- |
| REQ-001 | N | Strategic / Platform | Replicate all existing website functionality (including the MyRSS member portal) as a minimum baseline, with clear proposals for enhancement. | not shown |
| REQ-002 | N | Strategic / Platform | Provide a modern, actively-maintained CMS with Long Term Support, a clear roadmap and the ability to scale with the Society's needs. | not shown |
| REQ-003 | N | Strategic / Platform | .NET-based platform with strong Microsoft ecosystem compatibility to simplify CRM integration. | not shown |
| REQ-004 | N | Strategic / Platform | Robust, comprehensive and well-documented API enabling two-way data flow. | not shown |
| REQ-006 | N | Strategic / Platform | Adhere to core principles: least privilege, security by design, data minimisation, accessibility by default, and configuration over customisation. | not shown |
| REQ-007 | N | Strategic / Platform | Provide sufficient headroom/scalability to support a post-launch marketing campaign and traffic growth. | not shown |
| REQ-008 | F | Strategic / Platform | Support effective income generation and a modern online ecommerce experience. | basket.html |
| REQ-009 | F | CMS core | Admin-level access to CMS UAT and Production environments for the RSS web team. | not shown |
| REQ-010 | F | CMS core | Role-based permissions with granular workflow and versioning (draft, review, approve, schedule, rollback). | not shown |
| REQ-011 | F | CMS core | Structured content types (e.g. articles, events, local groups, sections, taskforces, awards, campaigns, member profiles, press releases). | get-involved.html, library.html |
| REQ-012 | F | CMS core | Bulk operations: move, delete and change permissions across multiple items. | not shown |
| REQ-013 | F | CMS core | Reusable, editable (HTML/CSS) components/widgets: carousel, hero banners, callouts, accordions, tabs, cards, timelines, quote blocks etc. | campaign.html, chartered-statistician.html, home.html, library.html, membership.html |
| REQ-014 | F | CMS core | WYSIWYG editor with semantic HTML controls and accessibility hints (heading levels, alt text, captions). | chartered-statistician.html |
| REQ-015 | F | CMS core | Media library with editing (crop, resize, thumbnails), metadata, and copyright/licence source tracking. | not shown |
| REQ-016 | F | CMS core | Content scheduling and archiving, with automatic redirects generated on URL/slug changes. | get-involved.html |
| REQ-017 | F | CMS core | Taxonomy management (categories, tags, topics, audiences) with bulk retagging. | article.html, events.html, professional-development.html |
| REQ-026 | F | Information architecture | Support a full range of generic and RSS-specific content types (news, blog, case studies, local groups, sections, SIGs, committees, task forces, honours, awards, prizes, campaigns, member profiles, journals, jobs, events, training, conference, policy statements, press releases, accreditation, resources). | library.html |
| REQ-027 | F | Navigation | Clear global navigation with audience pathways, breadcrumbs, footer and contextual wayfinding (related content, popular topics). | article.html, event.html, header.html, home.html, professional-development.html |
| REQ-028 | F | Header / Navigation | Mega menu with keyboard accessibility and logical tab order; top-level items in RSS brand colours with ability to feature a hyperlinked image. | header.html, home.html |
| REQ-029 | F | Navigation | Sub/left-side menus for in-section navigation. | chartered-statistician.html, grades-fees.html |
| REQ-030 | N | Navigation | Navigation works seamlessly and responsively on desktop, tablet and mobile. | not shown |
| REQ-031 | F | Navigation | User-friendly filtering on listing pages (topic/category, tags, date, audience, content type). | events.html, groups.html, search.html |
| REQ-032 | F | Navigation | Menu styling (fonts, colours, hover states) matches RSS brand guidelines; the active item is visually indicated. | home.html |
| REQ-033 | F | Navigation | Clear navigation/signposting to the RSS family of sites: Significance, Real World Data Science and OUP (journals). | header.html, home.html, publications.html |
| REQ-036 | N | Navigation | Users can reach all primary sections within 3 clicks. | not shown |
| REQ-037 | F | Search | All-in-one sitewide search across pages, events, courses, press releases, documents and media (audio, video, images) and metadata. Current search to be completely redeveloped. | header.html, home.html, search.html |
| REQ-038 | F | Search | Display results of different content types together on a single results page. | search.html |
| REQ-039 | F | Search | Comprehensive content filters (document type, category, tag, date, author). | search-advanced.html, search.html |
| REQ-040 | F | Search | Sortable results (date, author, category, tag). | search.html |
| REQ-041 | F | Search / AI | AI-assisted search that understands user intent and returns relevant, well-structured responses. | footer.html, header.html, search.html |
| REQ-048 | N | Search | For under 100k items, 95% of search requests returned in under half a second, with accessible screen-reader announcements for results. | not shown |
| REQ-049 | N | Accessibility | All templates and components meet WCAG 2.2 (alt text, focus indicators, keyboard navigation, colour contrast, error prevention). | not shown |
| REQ-050 | F | Accessibility / Forms | Accessible forms with labels, instructions, validation hints and error summaries. | join.html |
| REQ-051 | N | Accessibility | Manual accessibility audits conducted pre-launch and post-release. | not shown |
| REQ-052 | N | Accessibility | Resolve systemic, template-level accessibility issues: empty/unnamed buttons & links, missing alt text, colour-contrast failures and form labelling. | not shown |
| REQ-055 | N | Accessibility | Zero critical accessibility defects at launch. | not shown |
| REQ-056 | N | Performance | Meet Core Web Vitals targets: LCP <= 2.5s, CLS <= 0.1, INP <= 200ms on target devices. | not shown |
| REQ-057 | F | SEO | Good technical SEO: clean URLs, canonical tags, XML sitemaps, robots rules, schema.org markup, Open Graph/Twitter cards. | event.html, job.html |
| REQ-060 | N | Performance | Core Web Vitals pass rate >= 85% of sessions. | not shown |
| REQ-061 | N | Security & compliance | Pass vulnerability scans required for PCI DSS and Cyber Essentials Plus, adhering to all relevant requirements (e.g. PSD2/SCA). | not shown |
| REQ-062 | N | Security & compliance | HTTPS/TLS everywhere, HSTS, secure cookies, and protection against SQLi, XSS and CSRF with a content security policy (nonce/hash for inline scripts). | not shown |
| REQ-063 | N | Security & compliance | Rate limiting on forms and login pages. | not shown |
| REQ-064 | N | Security & compliance | Full UK GDPR compliance: lawful basis tracking, consent management (cookies, newsletters), separation of necessary vs marketing cookies, retention policies and audit trails. | not shown |
| REQ-065 | N | Security & compliance / Payments | No raw credit card data stored in the CMS or CRM at any point. | not shown |
| REQ-066 | N | Security & compliance | SPF/DKIM/DMARC configured for all emails and newsletters. | not shown |
| REQ-067 | N | Security & compliance | Regular patching strategy; critical/high-risk patches (CVSS 7+) applied within 14 days of release (in line with Cyber Essentials/NCSC guidance). | not shown |
| REQ-068 | F | Security & compliance | Provide data flow diagrams (e.g. CMS <> CRM <> payments), accessible audit logs, developer locations and a list of sub-processors/hosts with country of operation and security credentials. | not shown |
| REQ-069 | F | Security & compliance | Vulnerability/security-issue reporting via a form. | about.html |
| REQ-073 | N | Security & compliance | No high/critical/medium pen-test or PCI findings at go-live. | not shown |
| REQ-074 | F | Identity & access | Secure SSO for staff and key volunteers (with an M365 account in the RSS tenant) via Microsoft Entra ID, with MFA required. | sign-in.html |
| REQ-075 | F | Identity & access / Header | Sign in / out for members and registered users, with app-based MFA support. | header.html, join.html, sign-in.html |
| REQ-076 | F | Identity & access | User registration: a non-member can create a basic account and later upgrade to full membership; includes password resets. | join.html, sign-in.html |
| REQ-077 | F | Identity & access | Ability to impersonate a CMS user (time-limited, audited, requires elevated approval) to replicate their experience for debugging. | not shown |
| REQ-078 | F | Identity & access | Granular role-based permissions in the CMS for staff and key volunteers. | sign-in.html |
| REQ-079 | F | Identity & access | Custom roles (e.g. for trustees/volunteers) definable and updatable by RSS web staff. | not shown |
| REQ-080 | F | Identity & access | Self-service password resets requiring a time-limited confirmation link. | sign-in.html |
| REQ-082 | F | Forms | Accessible form builder: required/optional indicators, roll-over tips, inline instructions, multi-step/multi-page forms, tabs, branching, save-and-resume, restricted-type file uploads, and email notifications to submitter and staff. | about.html, join.html |
| REQ-083 | F | Forms | RSS staff can edit form content (headings, instructions, roll-over tips) without raising a support ticket with the digital agency. | join.html |
| REQ-084 | F | Payments | Direct Debit support via Access Paysuite for mandates, instalments and renewals, with secure webhook processing and CRM write-back. | donate.html, join.html |
| REQ-085 | F | Forms / Security | Spam/bot protection (e.g. reCAPTCHA) and server-side validation on forms. | about.html, accreditation.html |
| REQ-086 | F | Payments | Payment integration via a PCI DSS-compliant gateway (currently Elavon) with secure tokenisation, support for AVS/CVV/3D Secure, redirecting to the processor's secure pages; payments reconciled with CRM (and CMS where appropriate). | donate.html, join.html |
| REQ-087 | F | Payments / Ecommerce | Pricing logic (member grade, early-bird/late, concession, bundles), voucher/promo codes, VAT handling and downloadable HMRC-compliant receipts. | basket.html, book.html, conference.html, grades-fees.html, join.html |
| REQ-088 | F | Jobs | Jobs board with pricing tiers (standard/featured), search, filter, categories/tags, custom fields, featured image, expiry date with auto-unpublish and analytics. | jobs.html |
| REQ-089 | F | Payments / Ecommerce | Payment confirmation pages and email notifications, including dropped-basket and abandoned-application notifications. | book.html, join.html |
| REQ-090 | F | Ecommerce | Donations and fundraising with Gift Aid declarations. | donate.html |
| REQ-091 | F | Payments / Integration | Payment transactions synced with Dynamics CRM; form fields map to equivalent CRM fields. | join.html |
| REQ-092 | F | Forms | Address look-up / validation integration (Loqate). | join.html |
| REQ-093 | F | Advertising | Advertising slots/banners with reporting on impressions and click-through rates. | about.html |
| REQ-100 | F | Templates | Template builder allowing RSS to create and edit templates, clone or create child templates, and define/edit header and footer regions. | library.html |
| REQ-101 | F | Homepage | Highly customisable home page template capable of displaying personalised content blocks. | home.html |
| REQ-102 | F | Sections & Groups | Custom templates for sections, local groups and SIGs that dynamically pull through tagged news and events and link to social profiles (and could link to their newsletters). | get-involved.html, group.html, groups.html, submit-event.html |
| REQ-103 | F | Events / Training / Conference | Events calendar plus distinct custom templates for events, training courses and the annual conference. | event.html |
| REQ-104 | F | Templates | Templates/functionality for campaigns, resource hubs, explainers and FAQs. | campaign.html, membership.html |
| REQ-105 | F | Templates / Social | Share-to-social with auto-generated cards/images/text summaries. | article.html, event.html |
| REQ-106 | F | Templates | Pagination with user-definable values (e.g. show 10 articles). | news.html, search.html |
| REQ-109 | F | Personalisation | Personalised front-end content based on MyRSS preferences, member grade/class, length of membership and country. | chartered-statistician.html, home.html, myrss-profile.html, myrss.html |
| REQ-110 | F | Personalisation / Newsletters | Integrate with email marketing tools (Dynamics Customer Insights or equivalent) for personalised newsletters and preference-based content blocks. | myrss-preferences.html |
| REQ-113 | F | Analytics | Integrate GDPR-compliant analytics (currently GA4) with IP anonymisation and cookie-aware tracking; no tracking before consent (except strictly necessary). | footer.html |
| REQ-114 | F | Analytics | Event tracking for key actions (buy, join/renew, register, donate, download, submit). | donate.html |
| REQ-115 | F | Analytics | RSS able to apply tracking code to templates (header/footer), pages, buttons, banners and widgets. | home.html |
| REQ-116 | F | Analytics / Ecommerce | Ecommerce reporting including dropped baskets, banner adverts and job-board posts. | about.html, basket.html, jobs.html |
| REQ-117 | F | Analytics | Comprehensive reporting/dashboards measuring visits, downloads, drop-off points and conversions. | not shown |
| REQ-120 | F | Governance & workflow | Role-based access for governance (e.g. Admin, Editor, Publisher). | not shown |
| REQ-121 | F | Governance & workflow | Full change history (who changed what, when) with rollback and preview. | not shown |
| REQ-128 | N | Hosting & infrastructure | Scalable cloud hosting with backups and disaster recovery (RPO <= 24h, RTO <= 8h). | not shown |
| REQ-129 | N | Hosting & infrastructure | Hosting and data storage in UK/EU regions with encryption at rest and in transit. | not shown |
| REQ-130 | N | Hosting & infrastructure | Provide fully managed CMS Dev, UAT and Production environments. | not shown |
| REQ-131 | N | Hosting & infrastructure | Strong hosting security: web application firewalls, malware scanning, rapid patching, monitoring, alerting, and DDoS/script-injection protection. | not shown |
| REQ-132 | N | Hosting & infrastructure | Quote at least two tiers of hosting: Standard and Performance. | not shown |
| REQ-138 | F | Data migration | Migration plan from Kentico 12 covering users, navigation structure, content mapping, redirects, link fixes and image/media/document transfer. | not shown |
| REQ-139 | F | Data migration | Migrate required content: static pages, news, training courses, events, jobs, resources, multimedia (images/video/audio), documents (Word/PDF/Excel/CSV), newsletter and email templates. | not shown |
| REQ-140 | F | Data migration | Document library strategy: standardised naming conventions, consistent formats and metadata. | policy.html |
| REQ-141 | F | Data migration | Data cleanse, e.g. duplicate detection and members who haven't logged in for X years. | not shown |
| REQ-142 | F | Data migration / SEO | Implement or advise on a URL redirect strategy to preserve SEO. | not shown |
| REQ-143 | F | Data migration / Governance | Support named content ownership, review dates/lifecycle management, archiving and retention policies, and version control/audit trails. | chartered-statistician.html |
| REQ-144 | F | Data migration / AI | Use AI to optimise content names, tagging and metadata for SEO and AI discoverability. | not shown |
| REQ-147 | N | Data migration | >= 98% content migrated correctly; 100% of legacy URLs handled via redirects; broken links < 1% post-launch. | not shown |
| REQ-148 | F | User migration | Migrate all user accounts into the new CMS (exported from old CMS or resynced from CRM) in the correct security roles, ready for MVP go-live. | sign-in.html |
| REQ-149 | F | Email automation | Migrate/replicate email automation for MVP go-live, including the multi-step onboarding campaign that varies by member type. | join.html |
| REQ-150 | F | Email automation | All standard automated system emails working at launch (password resets, contact confirmations, newsletter subscription confirmations). | about.html, footer.html, sign-in.html |
| REQ-151 | F | Email automation / Membership | Replicate the automated renewals sequence: pre-renewal, renewal notice, prompts, outstanding-payment reminders, suspension and lapse notices (varying by member type and payment method). | myrss.html |
| REQ-152 | F | Email automation | Replicate transactional and staff-notification emails: payment-successful, corporate joining invitation, payment-unsuccessful and abandoned-application alerts. | join.html |
| REQ-153 | F | Integrations | Integrate with the required platforms: Entra (SSO), Copilot (AI), M365/Exchange (email), Dynamics 365 (CRM), Power Automate, Elavon/Opayo (payments), Access Paysuite (Direct Debits), CookieYes, OUP, PushEngage, YouTube, SoundCloud, Meta, Google (ads/analytics/tag manager), LinkedIn, BlueSky, X, Loqate and KnowBot. | search.html |
| REQ-154 | F | Integrations / CRM | Two-way near-real-time sync with Dynamics 365 CRM for users, events, conference, training, publications access, newsletters, directory inclusions and group membership. | grades-fees.html |
| REQ-155 | F | Integrations / CRM | Identify API limitations, where the CMS is source of truth and why, data-synchronisation timeframes, and error handling/retry/fallback scenarios. | not shown |
| REQ-159 | F | Newsletters | Newsletter opt-in/out controlled via MyRSS sign-up options, with an unsubscribe link in every newsletter. | footer.html, myrss-preferences.html |
| REQ-160 | F | Newsletters | Mailing lists sync with CRM, where opt-in/outs are recorded. | footer.html, myrss-groups.html, myrss-preferences.html |
| REQ-161 | F | Newsletters | RSS can develop and edit custom newsletter templates using a drag-and-drop editor. | myrss-preferences.html |
| REQ-162 | F | Newsletters | Newsletter templates pull through upcoming training and events, filterable by category or tag. | myrss-preferences.html |
| REQ-163 | F | Newsletters | Group newsletter templates pull through the group name, tagged/categorised news and events, and the group's social media links. | group.html |
| REQ-164 | F | Newsletters | Newsletter templates pull through tagged/categorised news articles. | myrss-preferences.html |
| REQ-165 | F | Newsletters / Security | Newsletters display only the minimum personal data required for the task (e.g. group users cannot see phone numbers or postal addresses). | group.html |
| REQ-166 | F | Newsletters | Reporting/analytics for all newsletters. | myrss-preferences.html |
| REQ-167 | F | Newsletters | Staff and section/group chairs can create, modify and send newsletters (4 staff newsletters; 35 group newsletters via the portal). | group.html |
| REQ-169 | F | Branding & assets | Shared, reusable and updatable collection of design assets (typography, icons, colours) e.g. a Figma library. | not shown |
| REQ-170 | F | Branding & assets | Direct access to stylesheets or high-level control via the template editor / custom code injection, to style widgets, buttons, forms and block quotes to match evolving brand guidelines. | not shown |
| REQ-173 | F | MyRSS portal | All existing MyRSS self-service functions: profile updates, newsletter preferences, event attendance, fellow/consultant directory inclusion, and payments/receipts. | myrss-profile.html, myrss.html |
| REQ-174 | N | MyRSS portal | Clear, intuitive MyRSS user interface. | not shown |
| REQ-175 | N | MyRSS portal | Fast page loads and filtering in MyRSS. | not shown |
| REQ-176 | F | MyRSS portal / CRM | Two-way sync between MyRSS and Dynamics CRM in near-real-time. | myrss.html |
| REQ-177 | F | MyRSS portal / Personalisation | Page/content-block visibility based on member type (e.g. Data Science Professionals see data-science resources). | chartered-statistician.html, home.html, myrss.html |
| REQ-178 | F | MyRSS portal / Personalisation | Page/content-block visibility based on membership status (e.g. a lapsed member loses access until they have paid). | find-an-expert.html, home.html, myrss-bookings.html, myrss-cpd.html, myrss-groups.html, myrss-preferences.html, myrss-profile.html, myrss.html, resources.html |
| REQ-179 | F | MyRSS portal | Member banner displaying name, type, category and number, with quick links to edit profile and apply for memberships, plus e-certificate download. | myrss.html |
| REQ-180 | F | MyRSS portal / Events / Training | My Events and My Training areas displaying booked, past and related items. | myrss-bookings.html, myrss.html |
| REQ-181 | F | MyRSS portal / Payments | Outstanding-balance dynamic area with a 'Pay now' pathway and clear payment-status indicators. | myrss.html |
| REQ-182 | F | MyRSS portal / Sections & Groups | Sections and groups page where members view subscriptions and select group mailing lists (tabs for Sections, SIGs, LGs). | myrss-groups.html |
| REQ-186 | F | Membership / Join | Online joining: multi-part form capturing member type, payment type, journal subscriptions and newsletter subscriptions, directing to the payment gateway then MyRSS on success. | join.html |
| REQ-187 | F | Membership / Join | Support 6 membership classes (Fellow, CStat, GradStat, Data Analyst, FIS/MIS, e-Student) and their grades, with correct joining and renewal fees, concessions, VAT codes and payment methods. | grades-fees.html, join.html, membership.html, professional-development.html |
| REQ-188 | F | Membership / Renewal | Membership renewals via credit/debit card or Direct Debit, with invoice/receipt provided to the user. | myrss.html |
| REQ-189 | F | Membership / Payments | Pricing logic reflecting member grade/class including concessions (career break, EDA, new graduate, retired, student), 60+, honorary, compounder and staff rates. | grades-fees.html, join.html, membership.html |
| REQ-190 | F | Accreditation | Accreditation applications (University and AfDSP) with admin management pages, past-applications views and PAC review workflow (in-progress, submitted, pending, awarded, rejected, filterable). | accreditation.html |
| REQ-192 | F | Professional services | Professional Register listing CStat, GradStat and Data Analyst holders, with search; able to show AdvDSP/ADSP and accommodate the AdvDSP -> CDSP (Chartered Data Science Professional) rename. | find-an-expert.html, professional-development.html |
| REQ-193 | F | Professional services | Fellows Directory with filtering menu. | find-an-expert.html |
| REQ-196 | F | Professional services | Directory listing management (consultant/fellow directory inclusion) by members. | find-an-expert.html, myrss-profile.html |
| REQ-198 | F | Publications | Access to journal subscriptions via SSO with the publisher OUP, unlocking content based on member type or paid subscription. | publications.html |
| REQ-199 | F | Publications / MyRSS portal | Publications area in MyRSS displaying active journal subscriptions. | myrss.html, publications.html |
| REQ-201 | F | Events | A single event listing page per event regardless of format, displayed once in listings and search, with a clear 'Hybrid event' indicator/tag. | event.html, events.html |
| REQ-202 | F | Events | Support multiple booking options/buttons per event, linking one event to multiple CRM booking endpoints (e.g. 'Attend in person', 'Join online'). | event.html |
| REQ-203 | F | Events | Sections, SIGs and Local Groups can submit events (free and charged); once approved they appear on the calendar. | submit-event.html |
| REQ-204 | F | Events / Forms | Modular, template-based registration forms supporting event-specific custom fields without bespoke builds (e.g. standard, conference, free, catering templates). | book.html |
| REQ-205 | F | Events | CMS-level data capture for additional fields outside CRM (stored temporarily or emailed to organisers). | book.html, submit-event.html |
| REQ-206 | F | Events | Streamlined booking journey, particularly for free events, with clear pre-booking information (format, location, joining details). | event.html |
| REQ-209 | F | Events | Event booking page displaying information in tabs (speakers, organiser, costs) with a 'Book now' button. | event.html |
| REQ-213 | F | Training | Course listings dynamically driven from CRM, with teaser descriptions, tags, optional tutor highlights, and filters for topic, date, format and price plus keyword search. | course.html, events.html, home.html |
| REQ-214 | F | Training | Course detail pages with full descriptions, learning outcomes, pricing, all available dates on one page, testimonials and tutor information, with direct booking. | course.html |
| REQ-215 | F | Training | Streamlined booking supporting booking for self or others, clearly differentiating booker and attendee roles and explaining delegate account creation. | book.html |
| REQ-216 | F | Training / Forms | Training forms capture delegate details, organisation, special requirements, communication preferences and marketing attribution (referral source), with clear newsletter opt-in. | book.html |
| REQ-219 | F | Training / MyRSS portal | My Training area pulling training history from CRM, so unpublished courses still appear historically. | myrss-bookings.html |
| REQ-222 | F | Training / CRM | Courses can be unpublished in the CMS without losing historical data; support multiple course dates with booking/attendance syncing. | course.html |
| REQ-224 | F | Conference | Conference landing page acting as the primary information hub with sections for overview, programme, speakers, attendee information, sponsors and a booking CTA. | conference.html |
| REQ-225 | F | Conference | Prominent 'Book Now' primary CTA (replacing 'Register Now'), high-contrast and WCAG-compliant, visually dominant and repeated at key scroll points. | conference.html |
| REQ-226 | F | Conference | Surface key content near the top of the conference homepage: programme summary, keynote speakers and key dates (card/highlight/image layouts). | conference.html |
| REQ-235 | F | News | News landing page filtering stories by relevance, recency, featured status and category; single page with filters covering featured stories, group news, call-outs and press/media. | home.html, news.html |
| REQ-236 | F | News | News/article page with social-media share buttons, thumbnail and categorisation, organised by category and date. | article.html |
| REQ-238 | F | Homepage | Home page featuring About, Join, News, featured tiles, Events & training, Publications, Jobs, Volunteering opportunities, Find an expert and Subscribe-to-newsletter entry points. | home.html, membership.html |
| REQ-246 | F | Footer | Footer secondary menu with options independent of the top menu. | footer.html |
| REQ-247 | F | Footer | Copyright notice in the footer showing the current year and registered charity number. | footer.html |
| REQ-248 | F | Footer / Compliance | Cookie consent management with granular preferences and audit logs (currently CookieYes). | footer.html |
| REQ-249 | F | Jobs | Jobs board landing page listing recent posts with salary, location and employer. | jobs.html |
| REQ-250 | F | Jobs | Job post detail page including the job description and an 'Apply now' button. | job.html |
| REQ-252 | F | Policy / Resources | Searchable, filterable policy documents listing (by category, subcategory, date, file type and size) with per-item title, description and download button. | policy.html |
| REQ-254 | F | File uploads | Restrict uploads to accepted file types (PDF, DOCX, XLSX, JPG/PNG, CSV) and reject ZIP/compressed, executable/script, legacy Office (.doc/.xls) and password-protected/encrypted files. | submit-event.html |
| REQ-255 | F | File uploads | Enforce file size limits (max 25 MB per file, 100 MB per application) with admin ability to control/override limits. | submit-event.html |
| REQ-256 | F | File uploads | Allow RSS admins to control the allowed/blocked list of file types. | not shown |
| REQ-257 | F | File uploads | Normalise file names on upload (replace spaces/special characters), reject double extensions (e.g. cv.pdf.exe) and apply a consistent internal naming pattern (e.g. ApplicationID_Surname_Firstname_DocumentType_YYYYMMDD.ext). | submit-event.html |
| REQ-258 | N | File uploads / Security | Validate MIME type and file signature (not just extension) and scan all uploads for malware before storage or access. | not shown |
| REQ-259 | N | File uploads / Compliance | Treat file names as personal data (include in access logs); define retention periods and auto-delete unsuccessful applications after the retention period. | not shown |
| REQ-266 | N | Testing & QA | Test plans covering unit, integration, UAT, cross-browser/device, accessibility, performance and security testing, with zero 'blocker' defects at launch. | not shown |
| REQ-268 | N | Support & documentation | Support SLA covering incidents (P1 response <= 1h, resolution targets), security and maintenance patching, and feature requests. | not shown |
| REQ-269 | N | Support & documentation | Detailed documentation, user guides and videos. | not shown |
| REQ-270 | N | Support & documentation | Training sessions for CMS administrators. | not shown |
| REQ-271 | N | Support & documentation | Incident management process with defined severity levels, immediate notification of security incidents, status updates and root-cause analysis for P1/P2, and a clear escalation process. | not shown |
| REQ-272 | N | Support & documentation / DevOps | Structured change and release management: clear release schedule/versioning, pre-release testing in Dev/UAT, formal production approval and rollback capability. | not shown |
| REQ-273 | N | Support & documentation / Hosting | Backup and disaster recovery with defined RPO/RTO, storage location, backup frequency/generations and failover capability. | not shown |
| REQ-274 | N | Support & documentation | Regular service reporting: monthly service report and quarterly service review, covering incidents/trends, security & patching, performance metrics and SLA performance. | not shown |

## Should

| Ref | Type | Area | Requirement | Shown in |
| --- | --- | --- | --- | --- |
| REQ-018 | F | CMS core | Drag-and-drop placement of components/widgets, each instance able to display different content and link to different pages. | home.html, library.html |
| REQ-019 | F | CMS core | High level of customisation of components/widgets (e.g. 2 large featured stories followed by 4 standard articles). | home.html, library.html |
| REQ-020 | F | CMS core / Content syndication | Pull through and re-style content from the Significance and Real World Data Science sites so it appears native to rss.org.uk. | home.html, news.html, publications.html |
| REQ-021 | F | CMS core | Editorial dashboards showing analytics, workflow queues and content freshness. | not shown |
| REQ-022 | F | CMS core | Inline content quality checks (readability, broken links, metadata completeness). | not shown |
| REQ-023 | F | CMS core | A/B testing for key pages, CTAs and newsletters. | home.html |
| REQ-024 | F | CMS core / AI | AI-assisted content suggestions (headlines, summaries, related content, SEO). | not shown |
| REQ-034 | F | Information architecture | Implement 'use-based hubs' (e.g. Volunteering, Professional Development, Training, Resources) acting as interactive secondary home pages. | events-training.html, for-journalists.html, get-involved.html, header.html, professional-development.html, resources.html |
| REQ-042 | F | Search | Highlight the search term within results. | search.html |
| REQ-043 | F | Search | Typo tolerance in search. | header.html, search.html |
| REQ-044 | F | Search | Search and index content within documents (PDF, Word, Excel, PowerPoint). | policy.html, search.html |
| REQ-045 | F | Search | Semantic search that understands the root of a term to deliver related results. | header.html, search.html |
| REQ-046 | F | Search | Helpful zero-results messaging when no matches are found. | search.html |
| REQ-053 | N | Accessibility | Automated CI checks to detect common accessibility issues before they reach Production. | not shown |
| REQ-054 | N | Accessibility | Accessibility statements and quarterly accessibility reports. | not shown |
| REQ-058 | N | Performance | Image optimisation (responsive images, modern formats), client-side caching and server-side/edge caching via CDN. | not shown |
| REQ-059 | F | SEO | Automatic metadata suggestions and broken-link monitoring. | not shown |
| REQ-070 | N | Security & compliance / Hosting | DDoS protection, Web Application Firewall / edge rules and IP reputation filtering. | not shown |
| REQ-071 | F | Security & compliance | Data Subject Access Request (DSAR) support. | not shown |
| REQ-081 | F | Identity & access | Log in/out support for third-party identity providers. | sign-in.html |
| REQ-094 | F | Ecommerce | Persistent shopping basket to facilitate multiple purchases. | basket.html, course.html, header.html |
| REQ-095 | F | Jobs | Submission, review and billing process for the job board. | jobs.html |
| REQ-096 | N | Forms / Security | Virus scanning on all file uploads. | not shown |
| REQ-097 | F | Forms | Progressive disclosure on forms (e.g. 'show more'). | join.html |
| REQ-098 | F | Forms | Reusable form templates that RSS can create and save. | join.html |
| REQ-099 | F | Forms / Branding | Branding of all form elements (fonts, colours). | not shown |
| REQ-107 | F | Templates / Media | Template to display content from the RSS YouTube channel. | events-training.html |
| REQ-108 | F | Templates / Media | Embed interactive data visuals (e.g. Power BI, Flourish) with accessible fallbacks. | campaign.html |
| REQ-111 | F | Personalisation | Personalised recommendations based on pages viewed, traffic source and search history. | home.html, myrss.html |
| REQ-118 | F | Analytics | Editorial dashboards (content performance, search queries, top pages). | header.html |
| REQ-122 | F | Governance & workflow | Content lifecycle policies: review reminders and retention/auto-archive. | chartered-statistician.html |
| REQ-123 | F | Governance & workflow | Bulk labelling (tags, categories, sensitivity). | not shown |
| REQ-125 | F | Internationalisation | Multilingual content support (defaulting to GB). | home.html |
| REQ-126 | N | Internationalisation | Inclusive imagery and language. | not shown |
| REQ-127 | F | Internationalisation | Date/time/number formatting localisation. | home.html |
| REQ-133 | N | DevOps | CI/CD pipeline with automated tests (accessibility, performance, security). | not shown |
| REQ-134 | N | DevOps | Zero-downtime deployments to Production. | not shown |
| REQ-135 | N | DevOps / Security | Secrets management for keys and credentials. | not shown |
| REQ-136 | N | Hosting & infrastructure | Monitoring/alerting with 99.9% uptime SLA. | not shown |
| REQ-137 | N | DevOps | Deployment rollback achievable in under 15 minutes. | not shown |
| REQ-145 | F | Data migration | Automated migration tooling with QA checks and sample test batches. | not shown |
| REQ-156 | F | Integrations / SEO | Search-indexing API (e.g. notify Google when a job posting is added or removed). | job.html |
| REQ-157 | F | Integrations / Analytics | Power BI integration for data visualisations. | campaign.html |
| REQ-158 | F | Integrations / Newsletters | Dedicated newsletter tool integration (e.g. Customer Insights). | myrss-preferences.html |
| REQ-168 | F | Newsletters | Detailed reporting dashboard with drill-down for newsletters. | not shown |
| REQ-171 | N | Branding & assets / Design | Replace text-heavy pages with infographics and iconography where possible, without reducing perceived brand authority. | not shown |
| REQ-183 | F | MyRSS portal / Personalisation | Restricted content (videos, training resources) and personalised content blocks based on membership type and interests. | events-training.html, myrss.html |
| REQ-184 | F | MyRSS portal | Community/interactivity features for logged-in members (profiles, forum, direct messaging). | myrss.html |
| REQ-185 | F | MyRSS portal / Resources | Information centre: searchable repository of downloadable documents, filterable by date/search term. | myrss.html, resources.html |
| REQ-191 | F | Accreditation | Expression-of-interest form for accreditation (University Accreditation / AfDSP). | accreditation.html |
| REQ-194 | F | Professional services | Consultants Directory: searchable, filterable listing of qualified members offering statistical consultancy, with back-office management. | find-an-expert.html, myrss-profile.html |
| REQ-195 | F | CPD / Professional services | CPD management: add CPD activities and view/edit/delete a dynamic CPD record, with downloadable activity records for a selected period. | myrss-cpd.html |
| REQ-207 | F | Events / Email automation | Suppress or customise payment-confirmation emails for free events and supplement CRM emails with clearer CMS-triggered or reminder emails. | event.html |
| REQ-208 | F | Events / MyRSS portal | Improve My RSSEvents: clear payment-status indicators, prominent 'Pay outstanding invoice' pathways, and profile management for members and non-members. | myrss-bookings.html |
| REQ-210 | F | Events calendar | Fast events calendar offering both list and calendar views, showing upcoming and previous events, with different colours per event type. | events.html |
| REQ-211 | F | Events calendar | Combined, filterable display of events and training (by type, topic, date) with the ability to create pre-filtered views (e.g. training-only from a training newsletter). | events-training.html, events.html |
| REQ-212 | F | Events calendar | Calendar items provide a quick snapshot of event/training info that links through to the full listing. | events.html |
| REQ-217 | F | Training / Payments | Discount codes entered at the summary/payment stage, integrated with the payment provider. | book.html |
| REQ-218 | F | Training | Automated waiting list for full courses, ideally integrated with CRM. | course.html, events.html |
| REQ-220 | F | Training | Cross-sell recommendations for related courses, events and articles via a global tagging system shared across CMS and CRM. | course.html, event.html, professional-development.html |
| REQ-221 | F | Training / Email automation | Marketing automation for training: abandoned-booking reminders and trigger-based course notifications. | book.html |
| REQ-223 | F | Training | Visual cues (icons/labels) clearly distinguishing online vs in-person course formats; promote featured, popular and upcoming courses. | events.html |
| REQ-227 | F | Conference | Dedicated Attendee Information section/page covering the conference app (download links/instructions), event logistics (dates, venue access) and FAQs. | conference.html |
| REQ-228 | F | Conference | Improved programme presentation via embedded programme (API/iframe), accordion (day/session/detail) or structured filtered pages. | conference.html |
| REQ-229 | F | Conference | Lightweight 'Conference Updates' dynamic content block, editable in the CMS without creating full news articles. | conference.html |
| REQ-230 | F | Conference / Payments | Clear pricing transparency: show what each ticket includes vs optional extras, and display add-on pricing before final checkout. | conference.html |
| REQ-231 | F | Conference / Sponsors | Sponsor/exhibitor logo display with CMS upload (image size constraints/optimisation guidance), delegated to named non-developer content owners. | conference.html |
| REQ-232 | F | Conference | Conference Board / Organising Committee listing page. | conference.html |
| REQ-233 | F | Conference | Future Conferences page listing the next 4 years (location and dates), plus a maintained past-conferences archive and multi-year calendar view. | conference.html |
| REQ-237 | F | Homepage / News | News carousel on the home page (e.g. 4 articles with published date and hyperlinked category, featured first, scrollable). | home.html |
| REQ-239 | F | Homepage / Events | Latest Events block on the home page (e.g. 2 featured + 4 standard) with title, date, location (incl. 'online'), type and optional image. | home.html |
| REQ-240 | F | Homepage / Training | Latest Training block on the home page (e.g. 6 public courses) with title, date and location, with hover for more info/alternate dates and optional image. | home.html |
| REQ-243 | F | Header | Social media links in the header to Bluesky, LinkedIn, Facebook, X and YouTube. | header.html |
| REQ-244 | F | Header / AI | AI assistant / chatbot on the front end (currently KnowBot, on evaluation) able to answer questions and support members, tailoring responses to user interests/knowledge level. | footer.html |
| REQ-245 | F | Header / Newsletters | Newsletter sign-up for non-members without requiring login. | footer.html |
| REQ-251 | F | Jobs | 'Advertise with us' and career advice/profiles content within the Jobs section. | jobs.html |
| REQ-253 | F | Resources | Resource hubs for distinct audiences (Journalists, Educators, Public) and a 'Find an Expert' facility. | for-journalists.html, home.html, resources.html |
| REQ-260 | F | AI | Automatic, highly-optimised classification, tagging and metadata for SEO and enhanced discoverability. | not shown |
| REQ-261 | F | AI / Personalisation | AI-driven personalised content, user journeys and recommendations. | not shown |
| REQ-262 | F | AI / Newsletters | AI content production and repurposing (e.g. generate a newsletter from the latest news articles). | not shown |
| REQ-263 | N | AI / Security | AI-assisted cyber security to complement (not replace) other security layers. | not shown |
| REQ-267 | N | Testing & QA | User testing with representative audiences (members, trustees, volunteers). | not shown |
| REQ-275 | N | Support & documentation | Quarterly reviews, a clear roadmap and capacity planning. | not shown |

## Could requirements referenced as "Proposed"

- REQ-276: Membership pathway finder: a short set of questions (career stage, qualifications, experience, data science focus) that recommends a membership grade and add-ons, shows the price including concessions, and starts the join form pre-filled. (grades-fees.html)
- REQ-277: Allow applicants to start a GradStat, CStat or Data Analyst application within the joining journey, rather than joining then upgrading in MyRSS. (membership.html)
- REQ-282: One shared interests taxonomy used by the profile, newsletter preferences, personalisation and recommendations; profile split into short sections each with its own save. (myrss-profile.html)
- REQ-284: Unified 'Find an expert' search across the Professional Register, Consultants Directory, Statistical Ambassadors and Statisticians for Society, with credential verification for employers. (find-an-expert.html)
- REQ-285: Filterable 'Find a group' list and map of sections, local groups (including international groups) and SIGs. (groups.html)
- REQ-286: Policy outputs published as HTML summary pages (key points, date, topic) with the full document attached, to improve search and AI discoverability. (policy.html)
- REQ-290: Pay by invoice or purchase order for organisations booking training or events for staff. (book.html)
