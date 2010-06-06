try:
    from djangoappengine.settings_base import *
    has_djangoappengine = True
except ImportError:
    has_djangoappengine = False
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

import os

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'djangotoolbox',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'artists',
    'jamfu_facebook',
    'socialregistration',
)

if has_djangoappengine:
    INSTALLED_APPS = ('djangoappengine',) + INSTALLED_APPS

ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

FACEBOOK_API_KEY='32e800dec1c23f116038e0bc8641ee88'
FACEBOOK_SECRET_KEY='8225f22b8c9e5fa3af75c0d85280adbb'
FACEBOOK_APP_ID='119681858044432'

AUTHENTICATION_BACKENDS=('socialregistration.auth.FacebookAuth',)
MIDDLEWARE_CLASSES=('socialregistration.middleware.FacebookMiddleware',)
