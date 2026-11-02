"""Search configuration for the prototype (written to data.js as RSS_CONFIG).

Everything that decides how search behaves lives here: ranking tiers, field
weights, synonym groups, facets and the order of their values, categories,
content-type aliases and promoted results. The engine (src/js/search-engine.js)
reads this object and hard-codes none of it. pages/search-configuration.html
renders it, so RSS can see that changing search means editing data.
"""

CONFIG = {
    # Score multiplier by page type: people and groups first, documents last (REQ-037, REQ-038)
    'tiers': {
        'Expert': 6.0,
        'Group': 6.0,
        'Page': 3.0,
        'Event': 1.2,
        'Course': 1.2,
        'Job': 1.2,
        'News': 1.0,
        'Document': 0.8,
    },
    # Points for a match in each field, plus bonuses for the whole title
    'fieldWeights': {'title': 10, 'tags': 4, 'summary': 2, 'body': 1, 'exactTitle': 60, 'titlePrefix': 12},
    'stopWords': ['and', 'the', 'of', 'for', 'in', 'a', 'an', 'to', 'on', 'with', 'by', 'at', 'is', 'how', 'do', 'i', 'what', 'my', 'rss'],
    # Each group: any member finds the others (REQ-045). Longest phrases are read first.
    'synonyms': [
        ['chartered statistician', 'cstat'],
        ['graduate statistician', 'gradstat'],
        ['advanced data science professional', 'advdsp'],
        ['artificial intelligence', 'ai', 'machine learning', 'ml', 'large language models', 'llm'],
        ['course', 'courses', 'training', 'workshop'],
        ['fees', 'fee', 'price', 'prices', 'cost', 'subscription'],
        ['jobs', 'job', 'vacancies', 'vacancy', 'careers'],
        ['excess deaths', 'covid', 'pandemic'],
        ['office for national statistics', 'ons'],
        ['data visualisation', 'data visualization', 'dataviz', 'charts'],
        ['medical', 'health', 'clinical'],
        ['discussion meeting', 'read paper'],
        ['local group', 'branch'],
        ['statistics', 'stats'],
    ],
    # Spelling correction: only when a search finds nothing (REQ-043)
    'correction': {'minLength': 4, 'maxDistance': 2, 'maxDistanceLong': 3, 'longFrom': 7, 'lengthWindow': 2},
    'categories': [
        {'key': 'pages', 'label': 'Pages'},
        {'key': 'events', 'label': 'Events and training'},
        {'key': 'news', 'label': 'News'},
        {'key': 'policy', 'label': 'Policy documents'},
        {'key': 'groups', 'label': 'Sections and groups'},
        {'key': 'experts', 'label': 'Experts'},
        {'key': 'jobs', 'label': 'Jobs'},
    ],
    # Facets over RSS's own taxonomies (REQ-039). OR within a facet, AND across facets.
    'facets': [
        {'key': 'ctype', 'label': 'Content type'},
        {'key': 'topic', 'label': 'Topic'},
        {'key': 'audience', 'label': 'Audience'},
        {'key': 'etype', 'label': 'Event type'},
        {'key': 'format', 'label': 'Format'},
        {'key': 'when', 'label': 'Upcoming or past'},
        {'key': 'ptype', 'label': 'Document type'},
        {'key': 'gkind', 'label': 'Group type'},
        {'key': 'region', 'label': 'Region'},
        {'key': 'status', 'label': 'Professional status'},
        {'key': 'directory', 'label': 'Directory'},
        {'key': 'year', 'label': 'Year'},
        {'key': 'access', 'label': 'Access'},
    ],
    # Which facets are offered for each tab ('' is All)
    'facetsFor': {
        '': ['ctype', 'topic', 'audience', 'year', 'access'],
        'pages': ['topic', 'audience'],
        'events': ['etype', 'format', 'when', 'topic', 'audience', 'year'],
        'news': ['ctype', 'topic', 'year', 'access'],
        'policy': ['ptype', 'topic', 'year'],
        'groups': ['gkind', 'region', 'topic'],
        'experts': ['status', 'directory', 'topic'],
        'jobs': ['topic'],
    },
    # Values sorted in a set order rather than by count (years always newest first)
    'valueOrder': {
        'status': ['CStat', 'GradStat', 'Data Analyst', 'AdvDSP', 'Fellow'],
        'when': ['Upcoming', 'Past'],
        'gkind': ['Section', 'Local group', 'Special interest group'],
    },
    # Merge loose internal distinctions. For RSS sign-off.
    'contentTypeAliases': {'Statement': 'Press release'},
    # Section searches: the same engine with a scope applied (header Events and Resources panels)
    'scopes': {
        'events': {'label': 'Events and training', 'type': 'events'},
        'experts': {'label': 'Find an expert', 'type': 'experts'},
        'policy': {'label': 'Policy library', 'type': 'policy'},
    },
    # Promoted results for named queries: later phase (REQ-278, a Could). One example.
    'bestBets': {'renew': 'page-renew-your-membership', 'renewal': 'page-renew-your-membership'},
}
