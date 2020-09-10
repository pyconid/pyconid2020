#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyCon ID 2020'
SITENAME = 'Python Conference Indonesia 2020'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

THEME = 'themes/eventalk'

TICKETING_SITE_URL = 'https://ticket.pycon.id'

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

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
SCHEDULE_URL = '/schedule'
# BLOG_URL = '/blog'


# Articel Config
ARTICEL_PATHS = ['articles']
# ARTICLE_URL = '{category}/{slug}'
# ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = 'blog/'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

# Menu Item Config
MENUITEMS = (
    # ('Our Speakers', 'speakers'),
    ('Call for Paper', 'call-for-paper'),
    #('Buy Ticket', 'ticket'),
    # ('Schedule', 'schedule'),
    # ('Speakers', 'speakers'),
    ('Sponsorship Opportunity', 'sponsor'),
    # ('Participant', 'participant-mail-list'),
    # ('Speak at Pycon ID', 'call-for-paper'),
    ('Code of Conduct', 'code-of-conduct'),
    ('Blog', 'blog'),
    ('Our Patrons', 'patron')
    # ('Contact', 'contact'),
)