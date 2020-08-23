#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyCon ID 2020'
SITENAME = 'Python Conference Indonesia 2020'
SITEURL = ''
SITESUBTITLE = 'Python Indonesia'
DESCRIPTION = 'Python Indonesia'
SITEIMAGE = '/images/logo.png'

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

THEME = 'themes/eventalk'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATH = ['images', 'pdfs']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Page Config
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
SCHEDULE_URL = '/schedule'


# Articel Config
ARTICEL_PATHS = ['articles']
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

# Menu Item Config
MENUITEMS = (
    # ('About', 'about'),
    ('Our Speakers', 'speaker'),
    ('Schedule & Layout', 'schedule-layout'),
    # ('Speakers', 'speakers'),
    ('Sponsorship Opportunity', 'sponsor'),
    # ('Participant', 'participant-mail-list'),
    # ('Speak at Pycon ID', 'call-for-paper'),
    ('Code of Conduct', 'code-of-conduct'),
    ('Our Patrons', 'patron')
    # ('Blog', 'blog'),
    # ('Contact', 'contact'),
)