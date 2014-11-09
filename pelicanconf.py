#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'John Vrbanac'
SITENAME = u'Flux.Ninja'
SITESUBTITLE = u'The opinionated comments of a software engineer'
SITEURL = ''

PATH = 'content'
THEME = 'themes/bootstrap3'
BOOTSTRAP_THEME = 'yeti'

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

STATIC_PATHS = ['images']
PROFILE_PICTURE = "profile_picture.jpg"

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

DEFAULT_PAGINATION = False
USE_FOLDER_AS_CATEGORY = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
