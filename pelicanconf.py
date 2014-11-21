#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from collections import namedtuple
import time

AUTHOR = u'John Vrbanac'
SITENAME = u'Flux.Ninja'
SITESUBTITLE = u'The opinionated comments of a software engineer'
SITEURL = 'http://flux.ninja'
COPYRIGHT = '&copy; 2012-{0} John Vrbanac'.format(time.strftime('%Y'))

PATH = 'content'
THEME = 'themes/flux'

MD_EXTENSIONS = ['codehilite(linenums=True, css_class=codehilite)', 'extra']

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

STATIC_PATHS = ['images']
PROFILE_PICTURE = ('https://22ec0acdb748a8b4898b-a208547a665e9daef6b0974a'
                   'b1daf34d.ssl.cf2.rackcdn.com/profile_picture.jpg')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

Link = namedtuple('Link', ['name', 'icon', 'href'])
LINKS = [
    Link('GitHub', 'fa-github', 'https://github.com/jmvrbanac'),
    Link('Google+', 'fa-google-plus-square',
         'https://plus.google.com/+JohnVrbanac'),
    Link('LinkedIn', 'fa-linkedin',
         'https://www.linkedin.com/pub/john-vrbanac/'),
    Link('jvrbanac', 'fa-slack', 'http://webchat.freenode.net/')
]

# Custom Menu Items
MENUITEMS = (('Home', '/'),)

DEFAULT_PAGINATION = 4
USE_FOLDER_AS_CATEGORY = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

DISQUS_SITENAME = 'flux-ninja-blog'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
