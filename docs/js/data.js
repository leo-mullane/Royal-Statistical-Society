/* data.js: search index and search configuration. Generated from tools/content.py and
   tools/search_config.py; pure data, no logic. All people, employers and documents are fictional. */
window.RSS_CONFIG = {
 "tiers": {
  "Expert": 6.0,
  "Group": 6.0,
  "Page": 3.0,
  "Event": 1.2,
  "Course": 1.2,
  "Job": 1.2,
  "News": 1.0,
  "Document": 0.8
 },
 "fieldWeights": {
  "title": 10,
  "tags": 4,
  "summary": 2,
  "body": 1,
  "exactTitle": 60,
  "titlePrefix": 12
 },
 "stopWords": [
  "and",
  "the",
  "of",
  "for",
  "in",
  "a",
  "an",
  "to",
  "on",
  "with",
  "by",
  "at",
  "is",
  "how",
  "do",
  "i",
  "what",
  "my",
  "rss"
 ],
 "synonyms": [
  [
   "chartered statistician",
   "cstat"
  ],
  [
   "graduate statistician",
   "gradstat"
  ],
  [
   "advanced data science professional",
   "advdsp"
  ],
  [
   "artificial intelligence",
   "ai",
   "machine learning",
   "ml",
   "large language models",
   "llm"
  ],
  [
   "course",
   "courses",
   "training",
   "workshop"
  ],
  [
   "fees",
   "fee",
   "price",
   "prices",
   "cost",
   "subscription"
  ],
  [
   "jobs",
   "job",
   "vacancies",
   "vacancy",
   "careers"
  ],
  [
   "excess deaths",
   "covid",
   "pandemic"
  ],
  [
   "office for national statistics",
   "ons"
  ],
  [
   "data visualisation",
   "data visualization",
   "dataviz",
   "charts"
  ],
  [
   "medical",
   "health",
   "clinical"
  ],
  [
   "discussion meeting",
   "read paper"
  ],
  [
   "local group",
   "branch"
  ],
  [
   "statistics",
   "stats"
  ]
 ],
 "correction": {
  "minLength": 4,
  "maxDistance": 2,
  "maxDistanceLong": 3,
  "longFrom": 7,
  "lengthWindow": 2
 },
 "categories": [
  {
   "key": "pages",
   "label": "Pages"
  },
  {
   "key": "events",
   "label": "Events and training"
  },
  {
   "key": "news",
   "label": "News"
  },
  {
   "key": "policy",
   "label": "Policy documents"
  },
  {
   "key": "groups",
   "label": "Sections and groups"
  },
  {
   "key": "experts",
   "label": "Experts"
  },
  {
   "key": "jobs",
   "label": "Jobs"
  }
 ],
 "facets": [
  {
   "key": "ctype",
   "label": "Content type"
  },
  {
   "key": "topic",
   "label": "Topic"
  },
  {
   "key": "audience",
   "label": "Audience"
  },
  {
   "key": "etype",
   "label": "Event type"
  },
  {
   "key": "format",
   "label": "Format"
  },
  {
   "key": "when",
   "label": "Upcoming or past"
  },
  {
   "key": "ptype",
   "label": "Document type"
  },
  {
   "key": "gkind",
   "label": "Group type"
  },
  {
   "key": "region",
   "label": "Region"
  },
  {
   "key": "status",
   "label": "Professional status"
  },
  {
   "key": "directory",
   "label": "Directory"
  },
  {
   "key": "year",
   "label": "Year"
  },
  {
   "key": "access",
   "label": "Access"
  }
 ],
 "facetsFor": {
  "": [
   "ctype",
   "topic",
   "audience",
   "year",
   "access"
  ],
  "pages": [
   "topic",
   "audience"
  ],
  "events": [
   "etype",
   "format",
   "when",
   "topic",
   "audience",
   "year"
  ],
  "news": [
   "ctype",
   "topic",
   "year",
   "access"
  ],
  "policy": [
   "ptype",
   "topic",
   "year"
  ],
  "groups": [
   "gkind",
   "region",
   "topic"
  ],
  "experts": [
   "status",
   "directory",
   "topic"
  ],
  "jobs": [
   "topic"
  ]
 },
 "valueOrder": {
  "status": [
   "CStat",
   "GradStat",
   "Data Analyst",
   "AdvDSP",
   "Fellow"
  ],
  "when": [
   "Upcoming",
   "Past"
  ],
  "gkind": [
   "Section",
   "Local group",
   "Special interest group"
  ]
 },
 "contentTypeAliases": {
  "Statement": "Press release"
 },
 "scopes": {
  "events": {
   "label": "Events and training",
   "type": "events"
  },
  "experts": {
   "label": "Find an expert",
   "type": "experts"
  },
  "policy": {
   "label": "Policy library",
   "type": "policy"
  }
 },
 "bestBets": {
  "renew": "page-renew-your-membership",
  "renewal": "page-renew-your-membership"
 }
};
window.RSS_TOPICS = ["Official statistics", "Data science and AI", "Medical and health statistics", "Methodology", "Statistical education", "Social statistics", "Environmental statistics", "Business and industry", "Statistical computing", "Public understanding of statistics"];
window.RSS_INDEX = [
 {
  "id": "page-chartered-statistician-cstat",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Chartered Statistician (CStat)",
  "url": "chartered-statistician.html",
  "summary": "The Society's highest professional award. Who can apply, what evidence you need and how long it takes.",
  "meta": [
   "Page",
   "Professional development"
  ],
  "tags": "cstat chartered professional status apply Professional development Methodology",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-membership-grades-and-fees",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Membership grades and fees",
  "url": "grades-fees.html",
  "summary": "Every membership grade, what it costs and the concessions available.",
  "meta": [
   "Page",
   "Membership"
  ],
  "tags": "fees price cost subscription grade fellow student concession Membership",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-join-the-rss",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Join the RSS",
  "url": "join.html",
  "summary": "Join online in a few minutes. Choose your grade, add journals and pay by card or Direct Debit.",
  "meta": [
   "Page",
   "Membership"
  ],
  "tags": "join become a member application Membership",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-why-join-the-rss",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Why join the RSS",
  "url": "membership.html",
  "summary": "What membership gives you: professional recognition, journals, events, training discounts and a community.",
  "meta": [
   "Page",
   "Membership"
  ],
  "tags": "benefits membership fellow Membership",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-professional-development",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Professional development",
  "url": "professional-development.html",
  "summary": "Professional status, CPD and accreditation for statisticians and data scientists.",
  "meta": [
   "Page",
   "Professional development"
  ],
  "tags": "gradstat data analyst cpd professional Professional development",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-accreditation-of-degree-programmes",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Accreditation of degree programmes",
  "url": "accreditation.html",
  "summary": "How universities and training providers apply for RSS accreditation.",
  "meta": [
   "Page",
   "Professional development"
  ],
  "tags": "accreditation university afdsp degree Professional development Statistical education",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Statistical education"
   ],
   "audience": [
    "Educators"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-find-an-expert",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Find an expert",
  "url": "find-an-expert.html",
  "summary": "Search the Professional Register and Consultants Directory to find a qualified statistician.",
  "meta": [
   "Page",
   "Resources"
  ],
  "tags": "register consultant directory expert hire verify Resources",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Employers",
    "Journalists"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-rss-conference-2027",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "RSS Conference 2027",
  "url": "conference.html",
  "summary": "Edinburgh, 6 to 9 September 2027. Programme, speakers, prices and how to book.",
  "meta": [
   "Page",
   "Events and training"
  ],
  "tags": "conference annual edinburgh book Events and training Methodology",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-sections-and-groups",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Sections and groups",
  "url": "groups.html",
  "summary": "Find a section, local group or special interest group.",
  "meta": [
   "Page",
   "Get involved"
  ],
  "tags": "section local group sig find a group Get involved",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-donate-to-the-rss",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Donate to the RSS",
  "url": "donate.html",
  "summary": "Support statistical education and the public understanding of statistics. Add Gift Aid.",
  "meta": [
   "Page",
   "Get involved"
  ],
  "tags": "donate gift aid fundraising Get involved",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "The public"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-jobs-and-careers",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Jobs and careers",
  "url": "jobs.html",
  "summary": "Statistics and data science vacancies, and how to advertise a job.",
  "meta": [
   "Page",
   "Resources"
  ],
  "tags": "jobs vacancies careers advertise Resources",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career",
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-for-journalists",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "For journalists",
  "url": "for-journalists.html",
  "summary": "Press office contacts, experts for comment and guides to reporting statistics.",
  "meta": [
   "Page",
   "Resources"
  ],
  "tags": "press media journalist comment Resources Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Journalists"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-policy-and-research",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Policy and research",
  "url": "policy.html",
  "summary": "Our consultation responses, evidence, reports and campaigns.",
  "meta": [
   "Page",
   "Policy and research"
  ],
  "tags": "policy library consultation evidence Policy and research Official statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Official statistics"
   ],
   "audience": [
    "Policymakers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-statistics-and-ai-campaign",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Statistics and AI campaign",
  "url": "campaign.html",
  "summary": "What the public should expect when AI is used to produce statistics.",
  "meta": [
   "Page",
   "Policy and research"
  ],
  "tags": "ai artificial intelligence campaign Policy and research Data science and AI Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Data science and AI",
    "Public understanding of statistics"
   ],
   "audience": [
    "Policymakers",
    "The public"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-journals-and-publications",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Journals and publications",
  "url": "publications.html",
  "summary": "Journal of the Royal Statistical Society Series A, B and C, Significance and Real World Data Science.",
  "meta": [
   "Page",
   "News and publications"
  ],
  "tags": "journal series a b c oup significance News and publications Methodology",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-about-the-rss",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "About the RSS",
  "url": "about.html",
  "summary": "Who we are, our strategy, governance and how to contact us.",
  "meta": [
   "Page",
   "About"
  ],
  "tags": "about contact governance council strategy About",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "The public"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-myrss",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "MyRSS",
  "url": "myrss.html",
  "summary": "Manage your membership, bookings, CPD and preferences.",
  "meta": [
   "Page",
   "MyRSS"
  ],
  "tags": "login sign in account myrss renew MyRSS",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-graduate-statistician-gradstat",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Graduate Statistician (GradStat)",
  "url": "graduate-statistician.html",
  "summary": "Professional status for graduates whose degree meets our academic standard, and the first step towards CStat.",
  "meta": [
   "Page",
   "Professional development"
  ],
  "tags": "gradstat graduate professional status apply Professional development Methodology",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Methodology"
   ],
   "audience": [
    "Students and early career",
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-data-analyst-professional-status",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Data Analyst professional status",
  "url": "data-analyst.html",
  "summary": "Recognition for people who work with data, from apprentices to experienced analysts.",
  "meta": [
   "Page",
   "Professional development"
  ],
  "tags": "data analyst apprentice professional status apply Professional development Data science and AI",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Data science and AI"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-data-science-professional",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Data Science Professional",
  "url": "data-science-professional.html",
  "summary": "The Data Science Professional and Advanced Data Science Professional awards, run with partner societies.",
  "meta": [
   "Page",
   "Professional development"
  ],
  "tags": "dsp advdsp advanced data science professional status Professional development Data science and AI",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Data science and AI"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-events-and-training",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Events and training",
  "url": "events-training.html",
  "summary": "Discussion meetings, section and local group events, public courses, in-house training and the annual conference.",
  "meta": [
   "Page",
   "Events and training"
  ],
  "tags": "events training courses calendar Events and training",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-find-an-event-or-course",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Find an event or course",
  "url": "events.html",
  "summary": "Every event and course in one finder, with list and calendar views.",
  "meta": [
   "Page",
   "Events and training"
  ],
  "tags": "events courses finder calendar Events and training",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-get-involved",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Get involved",
  "url": "get-involved.html",
  "summary": "Sections and groups, volunteering, honours, Statistical Ambassadors and Statisticians for Society.",
  "meta": [
   "Page",
   "Get involved"
  ],
  "tags": "volunteer volunteering get involved Get involved",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals",
    "The public"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-honours-and-awards",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Honours and awards",
  "url": "honours.html",
  "summary": "The Guy Medals and the Society's other honours, with how to nominate.",
  "meta": [
   "Page",
   "Get involved"
  ],
  "tags": "guy medals awards prizes nominate honorary fellowship Get involved Methodology",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-statistical-ambassadors",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Statistical Ambassadors",
  "url": "statistical-ambassadors.html",
  "summary": "Members trained to explain statistics in the media, in schools and in public debate.",
  "meta": [
   "Page",
   "Get involved"
  ],
  "tags": "ambassadors media schools volunteer Get involved Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Journalists",
    "Educators"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-statisticians-for-society",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Statisticians for Society",
  "url": "statisticians-for-society.html",
  "summary": "Free statistical help for charities and community groups, from volunteer members.",
  "meta": [
   "Page",
   "Get involved"
  ],
  "tags": "charity pro bono volunteer help Get involved Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "The public"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-news",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "News",
  "url": "news.html",
  "summary": "News, press releases and statements from the Society.",
  "meta": [
   "Page",
   "News and publications"
  ],
  "tags": "news press releases statements News and publications",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "The public",
    "Journalists"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-resources",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Resources",
  "url": "resources.html",
  "summary": "Resources for journalists, teachers, employers and policymakers.",
  "meta": [
   "Page",
   "Resources"
  ],
  "tags": "resources guides teachers Resources",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "The public",
    "Educators",
    "Journalists"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-advertise-a-job",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Advertise a job",
  "url": "post-job.html",
  "summary": "Post a standard or featured job advert and pay online.",
  "meta": [
   "Page",
   "Resources"
  ],
  "tags": "advertise job advert recruit employer Resources",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "page-renew-your-membership",
  "cat": "pages",
  "tier": "Page",
  "type": "Page",
  "title": "Renew your membership",
  "url": "myrss.html#renew",
  "summary": "Renew online by card or Direct Debit. Sign in to MyRSS to see your renewal fee.",
  "meta": [
   "Page",
   "MyRSS"
  ],
  "tags": "renew renewal subscription myrss MyRSS",
  "body": "",
  "facets": {
   "ctype": [
    "Page"
   ],
   "topic": [],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-dm-llm",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Discussion meeting: Statistical aspects of evaluating large language models",
  "url": "event.html",
  "summary": "A paper read to the Society, followed by an open discussion. Contributions can be made in the room or online.",
  "date": "2026-11-04",
  "meta": [
   "Discussion meeting",
   "4 November 2026",
   "Hybrid",
   "RSS, Errol Street, London, and online"
  ],
  "tags": "Discussion meeting  RSS Hybrid Data science and AI Methodology",
  "body": "RSS, Errol Street, London, and online 17:00 to 19:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Discussion meeting"
   ],
   "format": [
    "Hybrid"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Data science and AI",
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-intro-r",
  "cat": "events",
  "tier": "Course",
  "type": "Course",
  "title": "Introduction to R",
  "url": "course.html",
  "summary": "Import, tidy, summarise and plot data in R, with practical exercises throughout. No previous programming needed.",
  "date": "2026-11-10",
  "meta": [
   "Public course",
   "10 to 11 November 2026",
   "Online",
   "Online (Zoom)"
  ],
  "tags": "Public course Foundation RSS Training Online Statistical computing",
  "body": "Online (Zoom) 09:30 to 16:30 GMT, two days £345 members, £460 non-members",
  "facets": {
   "ctype": [
    "Course"
   ],
   "etype": [
    "Public course"
   ],
   "format": [
    "Online"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Statistical computing"
   ],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-med-estimands",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Medical Section: Estimands in clinical trials, five years on",
  "url": "event.html",
  "summary": "Three speakers from industry and academia on how the ICH E9 addendum has changed trial design and reporting.",
  "date": "2026-11-12",
  "meta": [
   "Section meeting",
   "12 November 2026",
   "Online",
   "Online"
  ],
  "tags": "Section meeting  Medical Section Online Medical and health statistics Methodology",
  "body": "Online 14:00 to 16:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Section meeting"
   ],
   "format": [
    "Online"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Medical and health statistics",
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-bayes-stan",
  "cat": "events",
  "tier": "Course",
  "type": "Course",
  "title": "Bayesian statistics with Stan",
  "url": "course.html",
  "summary": "Build, fit and check Bayesian models in Stan, from simple regressions to hierarchical models.",
  "date": "2026-11-17",
  "meta": [
   "Public course",
   "17 to 18 November 2026",
   "In person",
   "RSS, Errol Street, London"
  ],
  "tags": "Public course Intermediate RSS Training In person Methodology Statistical computing",
  "body": "RSS, Errol Street, London 09:30 to 16:30 GMT, two days £690 members, £920 non-members",
  "facets": {
   "ctype": [
    "Course"
   ],
   "etype": [
    "Public course"
   ],
   "format": [
    "In person"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Methodology",
    "Statistical computing"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-mersey-sport",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Merseyside Local Group: The statistics of sport",
  "url": "event.html",
  "summary": "How clubs use data to recruit players and set tactics, and what the numbers can and cannot tell us.",
  "date": "2026-11-19",
  "meta": [
   "Local group meeting",
   "19 November 2026",
   "In person",
   "University of Liverpool"
  ],
  "tags": "Local group meeting  Merseyside Local Group In person Public understanding of statistics Social statistics",
  "body": "University of Liverpool 18:30 to 20:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Local group meeting"
   ],
   "format": [
    "In person"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Public understanding of statistics",
    "Social statistics"
   ],
   "audience": [
    "The public",
    "Statisticians and data professionals"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-dataviz",
  "cat": "events",
  "tier": "Course",
  "type": "Course",
  "title": "Data visualisation for decision makers",
  "url": "course.html",
  "summary": "Choose the right chart, avoid misleading ones and present uncertainty to people who need to make a decision.",
  "date": "2026-11-24",
  "meta": [
   "Public course",
   "24 November 2026",
   "Online",
   "Online (Zoom)"
  ],
  "tags": "Public course Foundation RSS Training Online Data science and AI Public understanding of statistics",
  "body": "Online (Zoom) 09:30 to 13:00 GMT £295 members, £395 non-members",
  "facets": {
   "ctype": [
    "Course"
   ],
   "etype": [
    "Public course"
   ],
   "format": [
    "Online"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Data science and AI",
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals",
    "Policymakers"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-census-2031",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Official Statistics Section: Census 2031 and the future of population statistics",
  "url": "event.html",
  "summary": "Where the recommendation on the future of the census now stands, and what it means for users of small-area data.",
  "date": "2026-11-26",
  "meta": [
   "Section meeting",
   "26 November 2026",
   "Hybrid",
   "RSS, Errol Street, London, and online"
  ],
  "tags": "Section meeting  Official Statistics Section Hybrid Official statistics Social statistics",
  "body": "RSS, Errol Street, London, and online 16:00 to 18:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Section meeting"
   ],
   "format": [
    "Hybrid"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Official statistics",
    "Social statistics"
   ],
   "audience": [
    "Statisticians and data professionals",
    "Policymakers"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-intro-ml",
  "cat": "events",
  "tier": "Course",
  "type": "Course",
  "title": "Introduction to machine learning",
  "url": "course.html",
  "summary": "Supervised learning, model validation and the trade-offs between interpretability and accuracy, taught by statisticians.",
  "date": "2026-12-01",
  "meta": [
   "Public course",
   "1 to 3 December 2026",
   "Online",
   "Online (Zoom)"
  ],
  "tags": "Public course Intermediate RSS Training Online Data science and AI Statistical computing",
  "body": "Online (Zoom) 09:30 to 13:00 GMT, three mornings £520 members, £690 non-members",
  "facets": {
   "ctype": [
    "Course"
   ],
   "etype": [
    "Public course"
   ],
   "format": [
    "Online"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Data science and AI",
    "Statistical computing"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-ys-careers",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Young Statisticians Section: Careers evening",
  "url": "event.html",
  "summary": "Statisticians from government, health, finance and tech talk about how they got started. Networking afterwards.",
  "date": "2026-12-03",
  "meta": [
   "Section meeting",
   "3 December 2026",
   "In person",
   "Manchester Metropolitan University"
  ],
  "tags": "Section meeting  Young Statisticians Section In person Statistical education",
  "body": "Manchester Metropolitan University 18:00 to 20:30 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Section meeting"
   ],
   "format": [
    "In person"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Statistical education"
   ],
   "audience": [
    "Students and early career"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-schools-lecture",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "RSS lecture for schools: How do we know what we know?",
  "url": "event.html",
  "summary": "A live, interactive lecture for students aged 14 to 18 about evidence, uncertainty and spotting a misleading claim.",
  "date": "2026-12-09",
  "meta": [
   "Public lecture",
   "9 December 2026",
   "Online",
   "Online"
  ],
  "tags": "Public lecture  RSS Online Statistical education Public understanding of statistics",
  "body": "Online 10:00 to 11:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Public lecture"
   ],
   "format": [
    "Online"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Statistical education",
    "Public understanding of statistics"
   ],
   "audience": [
    "Educators",
    "Students and early career",
    "The public"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-survival",
  "cat": "events",
  "tier": "Course",
  "type": "Course",
  "title": "Survival analysis",
  "url": "course.html",
  "summary": "Kaplan-Meier, Cox models and their extensions, with worked examples from clinical and epidemiological studies.",
  "date": "2027-01-14",
  "meta": [
   "Public course",
   "14 to 15 January 2027",
   "In person",
   "RSS, Errol Street, London"
  ],
  "tags": "Public course Intermediate RSS Training In person Medical and health statistics Methodology",
  "body": "RSS, Errol Street, London 09:30 to 16:30 GMT, two days £690 members, £920 non-members",
  "facets": {
   "ctype": [
    "Course"
   ],
   "etype": [
    "Public course"
   ],
   "format": [
    "In person"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Medical and health statistics",
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2027"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-ambassadors",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Statistical Ambassadors training day",
  "url": "event.html",
  "summary": "Media and communication training for members joining the Statistical Ambassadors programme.",
  "date": "2027-01-20",
  "meta": [
   "Training day",
   "20 January 2027",
   "In person",
   "RSS, Errol Street, London"
  ],
  "tags": "Training day  RSS In person Public understanding of statistics",
  "body": "RSS, Errol Street, London 10:00 to 16:00 GMT Free (selected volunteers)",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Training day"
   ],
   "format": [
    "In person"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2027"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-dm-causal",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Discussion meeting: Causal inference from observational data",
  "url": "event.html",
  "summary": "A paper on target trial emulation, read to the Society, with discussion to be published in Series A.",
  "date": "2027-01-27",
  "meta": [
   "Discussion meeting",
   "27 January 2027",
   "Hybrid",
   "RSS, Errol Street, London, and online"
  ],
  "tags": "Discussion meeting  RSS Hybrid Methodology",
  "body": "RSS, Errol Street, London, and online 17:00 to 19:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Discussion meeting"
   ],
   "format": [
    "Hybrid"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2027"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-surveys",
  "cat": "events",
  "tier": "Course",
  "type": "Course",
  "title": "Practical survey design",
  "url": "course.html",
  "summary": "Questionnaire design, sampling and non-response, for people who commission or run surveys.",
  "date": "2027-02-02",
  "meta": [
   "Public course",
   "2 February 2027",
   "Online",
   "Online (Zoom)"
  ],
  "tags": "Public course Foundation RSS Training Online Social statistics Official statistics",
  "body": "Online (Zoom) 09:30 to 16:30 GMT £345 members, £460 non-members",
  "facets": {
   "ctype": [
    "Course"
   ],
   "etype": [
    "Public course"
   ],
   "format": [
    "Online"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Social statistics",
    "Official statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2027"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-gulf-gov",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Gulf Local Group: Data science in government",
  "url": "event.html",
  "summary": "How statistical offices in the region are using administrative data and machine learning.",
  "date": "2027-02-10",
  "meta": [
   "Local group meeting",
   "10 February 2027",
   "Online",
   "Online"
  ],
  "tags": "Local group meeting  Gulf Local Group Online Official statistics Data science and AI",
  "body": "Online 18:00 to 19:30 GST Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Local group meeting"
   ],
   "format": [
    "Online"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Official statistics",
    "Data science and AI"
   ],
   "audience": [
    "Statisticians and data professionals",
    "Policymakers"
   ],
   "year": [
    "2027"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-conference-2027",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "RSS Conference 2027, Edinburgh",
  "url": "conference.html",
  "summary": "The UK's largest annual statistics and data science conference: more than 500 talks, workshops and posters.",
  "date": "2027-09-06",
  "meta": [
   "Conference",
   "6 to 9 September 2027",
   "In person",
   "Edinburgh International Conference Centre"
  ],
  "tags": "Conference  RSS In person Methodology Data science and AI Official statistics Medical and health statistics",
  "body": "Edinburgh International Conference Centre Four days From £295",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Conference"
   ],
   "format": [
    "In person"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Methodology",
    "Data science and AI",
    "Official statistics",
    "Medical and health statistics"
   ],
   "audience": [
    "Statisticians and data professionals",
    "Students and early career"
   ],
   "year": [
    "2027"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-dm-small-area",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Discussion meeting: Small area estimation with administrative data",
  "url": "event.html",
  "summary": "Combining survey and administrative sources to produce reliable estimates for small populations.",
  "date": "2026-12-15",
  "meta": [
   "Discussion meeting",
   "15 December 2026",
   "Hybrid",
   "RSS, Errol Street, London, and online"
  ],
  "tags": "Discussion meeting  RSS Hybrid Official statistics Methodology",
  "body": "RSS, Errol Street, London, and online 17:00 to 19:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Discussion meeting"
   ],
   "format": [
    "Hybrid"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Official statistics",
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals",
    "Policymakers"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-dm-fairness",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Discussion meeting: Measuring fairness in algorithmic decisions",
  "url": "event.html",
  "summary": "A paper comparing statistical definitions of fairness, with case studies from lending and recruitment.",
  "date": "2027-02-24",
  "meta": [
   "Discussion meeting",
   "24 February 2027",
   "Hybrid",
   "RSS, Errol Street, London, and online"
  ],
  "tags": "Discussion meeting  RSS Hybrid Data science and AI Methodology",
  "body": "RSS, Errol Street, London, and online 17:00 to 19:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Discussion meeting"
   ],
   "format": [
    "Hybrid"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Data science and AI",
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals",
    "Policymakers"
   ],
   "year": [
    "2027"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-dm-trials",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Discussion meeting: Adaptive platform trials",
  "url": "event.html",
  "summary": "Design, analysis and regulatory questions for trials that test several treatments under one protocol.",
  "date": "2027-03-17",
  "meta": [
   "Discussion meeting",
   "17 March 2027",
   "Hybrid",
   "RSS, Errol Street, London, and online"
  ],
  "tags": "Discussion meeting  RSS Hybrid Medical and health statistics Methodology",
  "body": "RSS, Errol Street, London, and online 17:00 to 19:00 GMT Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Discussion meeting"
   ],
   "format": [
    "Hybrid"
   ],
   "when": [
    "Upcoming"
   ],
   "topic": [
    "Medical and health statistics",
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2027"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "event-dm-climate",
  "cat": "events",
  "tier": "Event",
  "type": "Event",
  "title": "Discussion meeting: Statistics and the climate emergency",
  "url": "event.html",
  "summary": "Recording now available. The paper and discussion will appear in Series A.",
  "date": "2026-10-14",
  "meta": [
   "Discussion meeting",
   "14 October 2026",
   "Hybrid",
   "RSS, Errol Street, London, and online"
  ],
  "tags": "Discussion meeting  RSS Hybrid Environmental statistics Methodology",
  "body": "RSS, Errol Street, London, and online 17:00 to 19:00 BST Free",
  "facets": {
   "ctype": [
    "Event"
   ],
   "etype": [
    "Discussion meeting"
   ],
   "format": [
    "Hybrid"
   ],
   "when": [
    "Past"
   ],
   "topic": [
    "Environmental statistics",
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "news-stats-commission",
  "cat": "news",
  "tier": "News",
  "type": "Press release",
  "title": "RSS responds to the Statistics Commission report",
  "url": "article.html",
  "summary": "The Society welcomes the report's focus on user needs and sets out three priorities for implementation.",
  "date": "2026-10-28",
  "meta": [
   "Press release",
   "28 October 2026"
  ],
  "tags": " Official statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Press release"
   ],
   "topic": [
    "Official statistics"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "news-guy-medals",
  "cat": "news",
  "tier": "News",
  "type": "News",
  "title": "Nominations open for the 2027 Guy Medals",
  "url": "article.html",
  "summary": "Nominate a colleague for the Society's highest honours. Nominations close on 31 January 2027.",
  "date": "2026-10-22",
  "meta": [
   "News",
   "22 October 2026"
  ],
  "tags": " Methodology",
  "body": "",
  "facets": {
   "ctype": [
    "News"
   ],
   "topic": [
    "Methodology"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "news-extreme-heat",
  "cat": "news",
  "tier": "News",
  "type": "News",
  "title": "From Significance: the statistics of extreme heat",
  "url": "article.html",
  "summary": "How attribution studies estimate the role of climate change in a single heatwave.",
  "date": "2026-10-20",
  "meta": [
   "News",
   "20 October 2026",
   "Significance"
  ],
  "tags": "Significance Environmental statistics",
  "body": "",
  "facets": {
   "ctype": [
    "News"
   ],
   "topic": [
    "Environmental statistics"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "news-ambassadors-call",
  "cat": "news",
  "tier": "News",
  "type": "Member callout",
  "title": "Call for volunteers: Statistical Ambassadors 2027",
  "url": "article.html",
  "summary": "Help journalists and the public understand the numbers. Applications close on 30 November.",
  "date": "2026-10-15",
  "meta": [
   "Member callout",
   "15 October 2026"
  ],
  "tags": " Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Member callout"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Members only"
   ]
  }
 },
 {
  "id": "news-data-analyst",
  "cat": "news",
  "tier": "News",
  "type": "News",
  "title": "Data Analyst professional status: what has changed",
  "url": "article.html",
  "summary": "Simpler evidence requirements and a new route for apprentices, from 1 November.",
  "date": "2026-10-09",
  "meta": [
   "News",
   "9 October 2026"
  ],
  "tags": " Data science and AI",
  "body": "",
  "facets": {
   "ctype": [
    "News"
   ],
   "topic": [
    "Data science and AI"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "news-lfs-statement",
  "cat": "news",
  "tier": "News",
  "type": "Statement",
  "title": "Statement on the Labour Force Survey",
  "url": "article.html",
  "summary": "The Society's response to the latest update on the quality of labour market statistics.",
  "date": "2026-10-02",
  "meta": [
   "Statement",
   "2 October 2026"
  ],
  "tags": " Official statistics Social statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Statement"
   ],
   "topic": [
    "Official statistics",
    "Social statistics"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "news-rwds-validation",
  "cat": "news",
  "tier": "News",
  "type": "News",
  "title": "From Real World Data Science: validating clinical prediction models",
  "url": "article.html",
  "summary": "A practical checklist for anyone building or buying a clinical risk model.",
  "date": "2026-09-25",
  "meta": [
   "News",
   "25 September 2026",
   "Real World Data Science"
  ],
  "tags": "Real World Data Science Medical and health statistics Data science and AI",
  "body": "",
  "facets": {
   "ctype": [
    "News"
   ],
   "topic": [
    "Medical and health statistics",
    "Data science and AI"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "news-keynotes",
  "cat": "news",
  "tier": "News",
  "type": "News",
  "title": "First keynote speakers announced for RSS Conference 2027",
  "url": "article.html",
  "summary": "Three plenary speakers confirmed for Edinburgh, with the call for talks opening in January.",
  "date": "2026-09-18",
  "meta": [
   "News",
   "18 September 2026"
  ],
  "tags": " Methodology",
  "body": "",
  "facets": {
   "ctype": [
    "News"
   ],
   "topic": [
    "Methodology"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "news-medical-committee",
  "cat": "news",
  "tier": "News",
  "type": "Member callout",
  "title": "Medical Section seeks new committee members",
  "url": "article.html",
  "summary": "Two committee places are open for 2027. Members of any grade can stand.",
  "date": "2026-09-10",
  "meta": [
   "Member callout",
   "10 September 2026"
  ],
  "tags": " Medical and health statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Member callout"
   ],
   "topic": [
    "Medical and health statistics"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Members only"
   ]
  }
 },
 {
  "id": "doc-code-consultation",
  "cat": "policy",
  "tier": "Document",
  "type": "Policy document",
  "title": "Response to the consultation on the Code of Practice for Statistics",
  "url": "policy.html",
  "summary": "Our response supports clearer standards for official statistics produced outside government departments.",
  "date": "2026-10-01",
  "meta": [
   "Consultation response",
   "PDF, 1.2 MB",
   "1 October 2026"
  ],
  "tags": "Consultation response Official statistics",
  "body": "Our response supports clearer standards for official statistics produced outside government departments. We recommend that the Code apply to all statistics used to inform public debate, including those produced by arm's-length bodies.",
  "pages": [
   [
    1,
    "Our response supports clearer standards for official statistics produced outside government departments."
   ],
   [
    4,
    "We recommend that the Code apply to all statistics used to inform public debate, including those produced by arm's-length bodies."
   ]
  ],
  "file": "code-consultation.pdf",
  "facets": {
   "ctype": [
    "Policy document"
   ],
   "ptype": [
    "Consultation response"
   ],
   "topic": [
    "Official statistics"
   ],
   "audience": [
    "Policymakers"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "doc-ai-report",
  "cat": "policy",
  "tier": "Document",
  "type": "Policy document",
  "title": "Statistics and AI: what the public should expect",
  "url": "policy.html",
  "summary": "Six principles for using AI in the production and communication of statistics.",
  "date": "2026-09-12",
  "meta": [
   "Report",
   "PDF, 3.4 MB",
   "12 September 2026"
  ],
  "tags": "Report Data science and AI Public understanding of statistics",
  "body": "Six principles for using AI in the production and communication of statistics. Any AI system used to produce official statistics should be documented, tested for bias and subject to the same quality assurance as traditional methods.",
  "pages": [
   [
    1,
    "Six principles for using AI in the production and communication of statistics."
   ],
   [
    11,
    "Any AI system used to produce official statistics should be documented, tested for bias and subject to the same quality assurance as traditional methods."
   ]
  ],
  "file": "ai-report.pdf",
  "facets": {
   "ctype": [
    "Policy document"
   ],
   "ptype": [
    "Report"
   ],
   "topic": [
    "Data science and AI",
    "Public understanding of statistics"
   ],
   "audience": [
    "Policymakers"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "doc-ons-evidence",
  "cat": "policy",
  "tier": "Document",
  "type": "Policy document",
  "title": "Written evidence on ONS data quality",
  "url": "policy.html",
  "summary": "Evidence submitted to the Public Administration and Constitutional Affairs Committee.",
  "date": "2026-07-03",
  "meta": [
   "Written evidence",
   "PDF, 640 KB",
   "3 July 2026"
  ],
  "tags": "Written evidence Official statistics",
  "body": "Evidence submitted to the Public Administration and Constitutional Affairs Committee. Falling response rates to the Labour Force Survey have reduced confidence in labour market statistics.",
  "pages": [
   [
    1,
    "Evidence submitted to the Public Administration and Constitutional Affairs Committee."
   ],
   [
    2,
    "Falling response rates to the Labour Force Survey have reduced confidence in labour market statistics."
   ]
  ],
  "file": "ons-evidence.pdf",
  "facets": {
   "ctype": [
    "Policy document"
   ],
   "ptype": [
    "Written evidence"
   ],
   "topic": [
    "Official statistics"
   ],
   "audience": [
    "Policymakers"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "doc-excess-deaths",
  "cat": "policy",
  "tier": "Document",
  "type": "Policy document",
  "title": "Briefing: understanding excess deaths",
  "url": "policy.html",
  "summary": "What excess death figures measure, how the baseline is chosen and how to report them.",
  "date": "2026-05-20",
  "meta": [
   "Briefing",
   "PDF, 410 KB",
   "20 May 2026"
  ],
  "tags": "Briefing Medical and health statistics Public understanding of statistics",
  "body": "What excess death figures measure, how the baseline is chosen and how to report them. Different choices of baseline can change estimates of excess deaths by tens of thousands.",
  "pages": [
   [
    1,
    "What excess death figures measure, how the baseline is chosen and how to report them."
   ],
   [
    3,
    "Different choices of baseline can change estimates of excess deaths by tens of thousands."
   ]
  ],
  "file": "excess-deaths.pdf",
  "facets": {
   "ctype": [
    "Policy document"
   ],
   "ptype": [
    "Briefing"
   ],
   "topic": [
    "Medical and health statistics",
    "Public understanding of statistics"
   ],
   "audience": [
    "Policymakers"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "doc-census-letter",
  "cat": "policy",
  "tier": "Document",
  "type": "Policy document",
  "title": "Letter on the future of the census",
  "url": "policy.html",
  "summary": "Our letter setting out why a census in 2031 remains the best option for population statistics.",
  "date": "2026-03-14",
  "meta": [
   "Letter",
   "PDF, 220 KB",
   "14 March 2026"
  ],
  "tags": "Letter Official statistics Social statistics",
  "body": "Our letter setting out why a census in 2031 remains the best option for population statistics. Administrative data are not yet able to replace the census for small-area population estimates.",
  "pages": [
   [
    1,
    "Our letter setting out why a census in 2031 remains the best option for population statistics. Administrative data are not yet able to replace the census for small-area population estimates."
   ]
  ],
  "file": "census-letter.pdf",
  "facets": {
   "ctype": [
    "Policy document"
   ],
   "ptype": [
    "Letter"
   ],
   "topic": [
    "Official statistics",
    "Social statistics"
   ],
   "audience": [
    "Policymakers"
   ],
   "year": [
    "2026"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "doc-post16-maths",
  "cat": "policy",
  "tier": "Document",
  "type": "Policy document",
  "title": "Response to the consultation on post-16 maths",
  "url": "policy.html",
  "summary": "Our response calls for data and statistics to be part of every post-16 pathway.",
  "date": "2025-12-02",
  "meta": [
   "Consultation response",
   "PDF, 900 KB",
   "2 December 2025"
  ],
  "tags": "Consultation response Statistical education",
  "body": "Our response calls for data and statistics to be part of every post-16 pathway. Every young person should leave education able to interpret data, risk and uncertainty.",
  "pages": [
   [
    1,
    "Our response calls for data and statistics to be part of every post-16 pathway."
   ],
   [
    5,
    "Every young person should leave education able to interpret data, risk and uncertainty."
   ]
  ],
  "file": "post16-maths.pdf",
  "facets": {
   "ctype": [
    "Policy document"
   ],
   "ptype": [
    "Consultation response"
   ],
   "topic": [
    "Statistical education"
   ],
   "audience": [
    "Policymakers"
   ],
   "year": [
    "2025"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "doc-skills-report",
  "cat": "policy",
  "tier": "Document",
  "type": "Policy document",
  "title": "Data science skills in the UK workforce",
  "url": "policy.html",
  "summary": "Survey findings on skills gaps, training and professional standards for data scientists.",
  "date": "2025-10-10",
  "meta": [
   "Report",
   "PDF, 5.8 MB",
   "10 October 2025"
  ],
  "tags": "Report Data science and AI Business and industry",
  "body": "Survey findings on skills gaps, training and professional standards for data scientists. Two thirds of employers said that statistical skills were the hardest to find in data science applicants.",
  "pages": [
   [
    1,
    "Survey findings on skills gaps, training and professional standards for data scientists."
   ],
   [
    17,
    "Two thirds of employers said that statistical skills were the hardest to find in data science applicants."
   ]
  ],
  "file": "skills-report.pdf",
  "facets": {
   "ctype": [
    "Policy document"
   ],
   "ptype": [
    "Report"
   ],
   "topic": [
    "Data science and AI",
    "Business and industry"
   ],
   "audience": [
    "Policymakers"
   ],
   "year": [
    "2025"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "doc-literacy-briefing",
  "cat": "policy",
  "tier": "Document",
  "type": "Policy document",
  "title": "Briefing: statistical literacy for parliamentarians",
  "url": "policy.html",
  "summary": "A short guide to the questions to ask of any statistic.",
  "date": "2025-06-18",
  "meta": [
   "Briefing",
   "PDF, 350 KB",
   "18 June 2025"
  ],
  "tags": "Briefing Public understanding of statistics",
  "body": "A short guide to the questions to ask of any statistic. Ask where the number came from, what it is being compared with, and how uncertain it is.",
  "pages": [
   [
    1,
    "A short guide to the questions to ask of any statistic."
   ],
   [
    2,
    "Ask where the number came from, what it is being compared with, and how uncertain it is."
   ]
  ],
  "file": "literacy-briefing.pdf",
  "facets": {
   "ctype": [
    "Policy document"
   ],
   "ptype": [
    "Briefing"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Policymakers"
   ],
   "year": [
    "2025"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "job-senior-stat",
  "cat": "jobs",
  "tier": "Job",
  "type": "Job",
  "title": "Senior Statistician",
  "url": "job.html",
  "summary": "Northbridge NHS Foundation Trust. Leeds (hybrid). £52,000 to £60,000.",
  "date": "2026-11-20",
  "meta": [
   "Job",
   "Northbridge NHS Foundation Trust",
   "Leeds (hybrid)",
   "Closes 20 November 2026"
  ],
  "tags": "Northbridge NHS Foundation Trust Permanent Medical and health statistics",
  "body": "Leeds (hybrid)",
  "facets": {
   "ctype": [
    "Job"
   ],
   "topic": [
    "Medical and health statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "job-lead-ds",
  "cat": "jobs",
  "tier": "Job",
  "type": "Job",
  "title": "Lead Data Scientist",
  "url": "job.html",
  "summary": "Halden Insurance. London. £85,000 to £95,000.",
  "date": "2026-11-14",
  "meta": [
   "Job",
   "Halden Insurance",
   "London",
   "Closes 14 November 2026"
  ],
  "tags": "Halden Insurance Permanent Data science and AI Business and industry",
  "body": "London",
  "facets": {
   "ctype": [
    "Job"
   ],
   "topic": [
    "Data science and AI",
    "Business and industry"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "job-lecturer",
  "cat": "jobs",
  "tier": "Job",
  "type": "Job",
  "title": "Lecturer in Statistics",
  "url": "job.html",
  "summary": "University of Eastwick. Norwich. £40,000 to £48,000.",
  "date": "2026-12-01",
  "meta": [
   "Job",
   "University of Eastwick",
   "Norwich",
   "Closes 1 December 2026"
  ],
  "tags": "University of Eastwick Permanent Statistical education Methodology",
  "body": "Norwich",
  "facets": {
   "ctype": [
    "Job"
   ],
   "topic": [
    "Statistical education",
    "Methodology"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "job-survey-method",
  "cat": "jobs",
  "tier": "Job",
  "type": "Job",
  "title": "Survey Methodologist",
  "url": "job.html",
  "summary": "Clearview Research. Remote (UK). £45,000.",
  "date": "2026-11-30",
  "meta": [
   "Job",
   "Clearview Research",
   "Remote (UK)",
   "Closes 30 November 2026"
  ],
  "tags": "Clearview Research Fixed term, 2 years Social statistics Official statistics",
  "body": "Remote (UK)",
  "facets": {
   "ctype": [
    "Job"
   ],
   "topic": [
    "Social statistics",
    "Official statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "job-grad-scheme",
  "cat": "jobs",
  "tier": "Job",
  "type": "Job",
  "title": "Graduate Statistician scheme",
  "url": "job.html",
  "summary": "Morland Water. Bristol. £31,000.",
  "date": "2026-12-12",
  "meta": [
   "Job",
   "Morland Water",
   "Bristol",
   "Closes 12 December 2026"
  ],
  "tags": "Morland Water Graduate scheme Environmental statistics Business and industry",
  "body": "Bristol",
  "facets": {
   "ctype": [
    "Job"
   ],
   "topic": [
    "Environmental statistics",
    "Business and industry"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "job-biostat",
  "cat": "jobs",
  "tier": "Job",
  "type": "Job",
  "title": "Principal Biostatistician",
  "url": "job.html",
  "summary": "Vantor Pharma. Cambridge (hybrid). Competitive.",
  "date": "2026-11-25",
  "meta": [
   "Job",
   "Vantor Pharma",
   "Cambridge (hybrid)",
   "Closes 25 November 2026"
  ],
  "tags": "Vantor Pharma Permanent Medical and health statistics",
  "body": "Cambridge (hybrid)",
  "facets": {
   "ctype": [
    "Job"
   ],
   "topic": [
    "Medical and health statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-medical",
  "cat": "groups",
  "tier": "Group",
  "type": "Section",
  "title": "Medical Section",
  "url": "group.html",
  "summary": "Section, UK-wide. News, events and how to join.",
  "meta": [
   "Section",
   "UK-wide"
  ],
  "tags": "Section UK-wide Medical and health statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Section"
   ],
   "gkind": [
    "Section"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Medical and health statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-official",
  "cat": "groups",
  "tier": "Group",
  "type": "Section",
  "title": "Official Statistics Section",
  "url": "group.html",
  "summary": "Section, UK-wide. News, events and how to join.",
  "meta": [
   "Section",
   "UK-wide"
  ],
  "tags": "Section UK-wide Official statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Section"
   ],
   "gkind": [
    "Section"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Official statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-data-science",
  "cat": "groups",
  "tier": "Group",
  "type": "Section",
  "title": "Data Science and AI Section",
  "url": "group.html",
  "summary": "Section, UK-wide. News, events and how to join.",
  "meta": [
   "Section",
   "UK-wide"
  ],
  "tags": "Section UK-wide Data science and AI",
  "body": "",
  "facets": {
   "ctype": [
    "Section"
   ],
   "gkind": [
    "Section"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Data science and AI"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-social-stats",
  "cat": "groups",
  "tier": "Group",
  "type": "Section",
  "title": "Social Statistics Section",
  "url": "group.html",
  "summary": "Section, UK-wide. News, events and how to join.",
  "meta": [
   "Section",
   "UK-wide"
  ],
  "tags": "Section UK-wide Social statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Section"
   ],
   "gkind": [
    "Section"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Social statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-environmental",
  "cat": "groups",
  "tier": "Group",
  "type": "Section",
  "title": "Environmental Statistics Section",
  "url": "group.html",
  "summary": "Section, UK-wide. News, events and how to join.",
  "meta": [
   "Section",
   "UK-wide"
  ],
  "tags": "Section UK-wide Environmental statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Section"
   ],
   "gkind": [
    "Section"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Environmental statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-education",
  "cat": "groups",
  "tier": "Group",
  "type": "Section",
  "title": "Education and Statistical Literacy Section",
  "url": "group.html",
  "summary": "Section, UK-wide. News, events and how to join.",
  "meta": [
   "Section",
   "UK-wide"
  ],
  "tags": "Section UK-wide Statistical education",
  "body": "",
  "facets": {
   "ctype": [
    "Section"
   ],
   "gkind": [
    "Section"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Statistical education"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-young-stats",
  "cat": "groups",
  "tier": "Group",
  "type": "Section",
  "title": "Young Statisticians Section",
  "url": "group.html",
  "summary": "Section, UK-wide. News, events and how to join.",
  "meta": [
   "Section",
   "UK-wide"
  ],
  "tags": "Section UK-wide Statistical education",
  "body": "",
  "facets": {
   "ctype": [
    "Section"
   ],
   "gkind": [
    "Section"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Statistical education"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-computing",
  "cat": "groups",
  "tier": "Group",
  "type": "Section",
  "title": "Statistical Computing Section",
  "url": "group.html",
  "summary": "Section, UK-wide. News, events and how to join.",
  "meta": [
   "Section",
   "UK-wide"
  ],
  "tags": "Section UK-wide Statistical computing",
  "body": "",
  "facets": {
   "ctype": [
    "Section"
   ],
   "gkind": [
    "Section"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Statistical computing"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-merseyside",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "Merseyside Local Group",
  "url": "group.html",
  "summary": "Local group, North West England. News, events and how to join.",
  "meta": [
   "Local group",
   "North West England"
  ],
  "tags": "Local group North West England Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "North West England"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-manchester",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "Manchester Local Group",
  "url": "group.html",
  "summary": "Local group, North West England. News, events and how to join.",
  "meta": [
   "Local group",
   "North West England"
  ],
  "tags": "Local group North West England Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "North West England"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-edinburgh",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "Edinburgh Local Group",
  "url": "group.html",
  "summary": "Local group, Scotland. News, events and how to join.",
  "meta": [
   "Local group",
   "Scotland"
  ],
  "tags": "Local group Scotland Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "Scotland"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-cardiff",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "Cardiff Local Group",
  "url": "group.html",
  "summary": "Local group, Wales. News, events and how to join.",
  "meta": [
   "Local group",
   "Wales"
  ],
  "tags": "Local group Wales Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "Wales"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-east-midlands",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "East Midlands Local Group",
  "url": "group.html",
  "summary": "Local group, Midlands. News, events and how to join.",
  "meta": [
   "Local group",
   "Midlands"
  ],
  "tags": "Local group Midlands Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "Midlands"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-gulf",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "Gulf Local Group",
  "url": "group.html",
  "summary": "Local group, International. News, events and how to join.",
  "meta": [
   "Local group",
   "International"
  ],
  "tags": "Local group International Official statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "International"
   ],
   "topic": [
    "Official statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-india",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "India Local Group",
  "url": "group.html",
  "summary": "Local group, International. News, events and how to join.",
  "meta": [
   "Local group",
   "International"
  ],
  "tags": "Local group International Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "International"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-nigeria",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "Nigeria Local Group",
  "url": "group.html",
  "summary": "Local group, International. News, events and how to join.",
  "meta": [
   "Local group",
   "International"
  ],
  "tags": "Local group International Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "International"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-singapore",
  "cat": "groups",
  "tier": "Group",
  "type": "Local group",
  "title": "Singapore Local Group",
  "url": "group.html",
  "summary": "Local group, International. News, events and how to join.",
  "meta": [
   "Local group",
   "International"
  ],
  "tags": "Local group International Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Local group"
   ],
   "gkind": [
    "Local group"
   ],
   "region": [
    "International"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-quality",
  "cat": "groups",
  "tier": "Group",
  "type": "Special interest group",
  "title": "Quality Improvement SIG",
  "url": "group.html",
  "summary": "Special interest group, UK-wide. News, events and how to join.",
  "meta": [
   "Special interest group",
   "UK-wide"
  ],
  "tags": "Special interest group UK-wide Business and industry",
  "body": "",
  "facets": {
   "ctype": [
    "Special interest group"
   ],
   "gkind": [
    "Special interest group"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Business and industry"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-sports",
  "cat": "groups",
  "tier": "Group",
  "type": "Special interest group",
  "title": "Statistics in Sport SIG",
  "url": "group.html",
  "summary": "Special interest group, UK-wide. News, events and how to join.",
  "meta": [
   "Special interest group",
   "UK-wide"
  ],
  "tags": "Special interest group UK-wide Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Special interest group"
   ],
   "gkind": [
    "Special interest group"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-history",
  "cat": "groups",
  "tier": "Group",
  "type": "Special interest group",
  "title": "History of Statistics SIG",
  "url": "group.html",
  "summary": "Special interest group, UK-wide. News, events and how to join.",
  "meta": [
   "Special interest group",
   "UK-wide"
  ],
  "tags": "Special interest group UK-wide Public understanding of statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Special interest group"
   ],
   "gkind": [
    "Special interest group"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Public understanding of statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "group-primary-health",
  "cat": "groups",
  "tier": "Group",
  "type": "Special interest group",
  "title": "Primary Health Care SIG",
  "url": "group.html",
  "summary": "Special interest group, UK-wide. News, events and how to join.",
  "meta": [
   "Special interest group",
   "UK-wide"
  ],
  "tags": "Special interest group UK-wide Medical and health statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Special interest group"
   ],
   "gkind": [
    "Special interest group"
   ],
   "region": [
    "UK-wide"
   ],
   "topic": [
    "Medical and health statistics"
   ],
   "audience": [
    "Statisticians and data professionals"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "expert-a-okafor",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "Dr Adaeze Okafor",
  "url": "find-an-expert.html?q=Adaeze%20Okafor",
  "summary": "Clinical trials, Survival analysis.",
  "meta": [
   "CStat",
   "Clinical trials",
   "London"
  ],
  "tags": "CStat London Clinical trials Survival analysis Professional Register Consultants Directory Medical and health statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "CStat"
   ],
   "directory": [
    "Professional Register",
    "Consultants Directory"
   ],
   "topic": [
    "Medical and health statistics"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "expert-j-whitfield",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "James Whitfield",
  "url": "find-an-expert.html?q=James%20Whitfield",
  "summary": "Survey design, Official statistics.",
  "meta": [
   "CStat",
   "Survey design",
   "Edinburgh"
  ],
  "tags": "CStat Edinburgh Survey design Official statistics Professional Register Consultants Directory Official statistics Social statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "CStat"
   ],
   "directory": [
    "Professional Register",
    "Consultants Directory"
   ],
   "topic": [
    "Official statistics",
    "Social statistics"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "expert-p-raman",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "Priya Raman",
  "url": "find-an-expert.html?q=Priya%20Raman",
  "summary": "Data visualisation, R.",
  "meta": [
   "Data Analyst",
   "Data visualisation",
   "Birmingham"
  ],
  "tags": "Data Analyst Birmingham Data visualisation R Professional Register Data science and AI",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "Data Analyst"
   ],
   "directory": [
    "Professional Register"
   ],
   "topic": [
    "Data science and AI"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "expert-t-hughes",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "Tom Hughes",
  "url": "find-an-expert.html?q=Tom%20Hughes",
  "summary": "Environmental modelling.",
  "meta": [
   "GradStat",
   "Environmental modelling",
   "Cardiff"
  ],
  "tags": "GradStat Cardiff Environmental modelling Professional Register Environmental statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "GradStat"
   ],
   "directory": [
    "Professional Register"
   ],
   "topic": [
    "Environmental statistics"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "expert-m-lindqvist",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "Dr Maria Lindqvist",
  "url": "find-an-expert.html?q=Maria%20Lindqvist",
  "summary": "Machine learning, Model validation.",
  "meta": [
   "CStat, AdvDSP",
   "Machine learning",
   "Manchester"
  ],
  "tags": "CStat, AdvDSP Manchester Machine learning Model validation Professional Register Consultants Directory Data science and AI",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "CStat",
    "AdvDSP"
   ],
   "directory": [
    "Professional Register",
    "Consultants Directory"
   ],
   "topic": [
    "Data science and AI"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "expert-s-adeyemi",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "Samuel Adeyemi",
  "url": "find-an-expert.html?q=Samuel%20Adeyemi",
  "summary": "Quality improvement, Six Sigma.",
  "meta": [
   "CStat",
   "Quality improvement",
   "Leeds"
  ],
  "tags": "CStat Leeds Quality improvement Six Sigma Professional Register Consultants Directory Business and industry",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "CStat"
   ],
   "directory": [
    "Professional Register",
    "Consultants Directory"
   ],
   "topic": [
    "Business and industry"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 },
 {
  "id": "expert-h-clarke",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "Professor Helen Clarke",
  "url": "find-an-expert.html?q=Helen%20Clarke&tab=fellows",
  "summary": "Bayesian methods.",
  "meta": [
   "Fellow",
   "Bayesian methods",
   "Oxford"
  ],
  "tags": "Fellow Oxford Bayesian methods Fellows Directory Methodology",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "Fellow"
   ],
   "directory": [
    "Fellows Directory"
   ],
   "topic": [
    "Methodology"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Members only"
   ]
  }
 },
 {
  "id": "expert-r-osei",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "Dr Richard Osei",
  "url": "find-an-expert.html?q=Richard%20Osei&tab=fellows",
  "summary": "Epidemiology.",
  "meta": [
   "Fellow",
   "Epidemiology",
   "Nottingham"
  ],
  "tags": "Fellow Nottingham Epidemiology Fellows Directory Medical and health statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "Fellow"
   ],
   "directory": [
    "Fellows Directory"
   ],
   "topic": [
    "Medical and health statistics"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Members only"
   ]
  }
 },
 {
  "id": "expert-l-macrae",
  "cat": "experts",
  "tier": "Expert",
  "type": "Expert",
  "title": "Lucy MacRae",
  "url": "find-an-expert.html?q=Lucy%20MacRae",
  "summary": "Social research.",
  "meta": [
   "GradStat",
   "Social research",
   "Glasgow"
  ],
  "tags": "GradStat Glasgow Social research Professional Register Social statistics",
  "body": "",
  "facets": {
   "ctype": [
    "Expert"
   ],
   "status": [
    "GradStat"
   ],
   "directory": [
    "Professional Register"
   ],
   "topic": [
    "Social statistics"
   ],
   "audience": [
    "Employers"
   ],
   "access": [
    "Public"
   ]
  }
 }
];
