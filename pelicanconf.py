#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lucas Magnum'
SITENAME = u'Lucas Magnum'
SITEURL = 'http://lucasmagnum.github.io'
SITEDESCRIPTION = 'Lucas Magnum'

SITETITLE = AUTHOR
SITESUBTITLE = u'Software Developer'
SITEDESCRIPTION = u'{} - Software Developer'.format(AUTHOR)
SITELOGO = '{}/theme/img/avatar.jpg'.format(SITEURL)

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ROBOTS = 'index, follow'

LINKS = ()

DISQUS_SITENAME = 'lucasmagnumgithubio'


CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}


# Social widget
SOCIAL = (
    ('github', 'https://github.com/lucasmagnum'),
    ('linkedin', 'https://br.linkedin.com/in/lucasmagnum'),
    ('facebook', 'https://www.facebook.com/lmloliveira'),
    ('twitter', 'http://twitter.com/lucasmagn'),
)

THEME = 'theme'

GOOGLE_ANALYTICS = 'UA-69554514-1'

DEFAULT_PAGINATION = 5
