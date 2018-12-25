#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Eric Chan'
SITENAME = 'Eric Chan @ Clarity Insights'
# SITEURL = 'https://eChanClarityInsights.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
LOAD_CONTENT_CACHE = False
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
TAGLINE = '''Eric Chan is a Senior Associate Consultant at Clarity Insights.'''
DISQUS_SITENAME = "echanclarityinsights-github-io-1"
THEME = "pelican-svbhack"
FAVICON = '/images/favicon.ico'
USER_LOGO_URL = '/images/eric.jpg'


LINKS = (('Clarity Insights', 'https://www.clarityinsights.com'),
         ('GitHub', 'https://github.com/eChanClarityInsights'),
         ('Email', 'mailto:echan@clarityinsights.com')
         )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
