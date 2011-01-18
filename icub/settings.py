# -*- coding: utf-8 -*-
# settings.py by gonz
from os.path import abspath, dirname, basename, join
import sys

PROJECT_ABSOLUTE_DIR = dirname(abspath(__file__))
PROJECT_NAME = basename(PROJECT_ABSOLUTE_DIR)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',

    'home',
    'menu',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'context_processors.urls',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

LANGUAGES = (
  ('es', 'Español'),
  ('en', 'English'),
)
LANGUAGE_CODE = 'es-uy'
DEFAULT_LANGUAGE = 1

DEFAULT_CHARSET = 'utf-8'

SITE_ID = 1

SECRET_KEY = ''

ROOT_URLCONF = '%s.urls' % PROJECT_NAME


# MEDIA
MEDIA_ROOT = PROJECT_ABSOLUTE_DIR + "/media/"
MEDIA_URL = 'http://media.icub.edu.uy/'
ADMIN_MEDIA_PREFIX = 'http://media.icub.edu.uy/admin/'

CSS_PATH = '%scss/' % MEDIA_URL
JS_PATH = '%sjs/' % MEDIA_URL

# TEMPLATES
TEMPLATE_DIRS = (
    join(PROJECT_ABSOLUTE_DIR, "templates"),
)
ADMIN_TEMPLATE_DIRS = (
    join(PROJECT_ABSOLUTE_DIR, "templates"),
)

# Add apps/ dir to python path.
sys.path.append(join(PROJECT_ABSOLUTE_DIR, "apps"))

# Override previous settings with values in local_settings.py settings file.
try:
    from local_settings import *
except ImportError:
    debug_msg ="Can't find local_settings.py, using default settings."
    try:
        from mod_python import apache
        apache.log_error("%s" % debug_msg, apache.APLOG_NOTICE)
    except ImportError:
        import sys
        sys.stderr.write("%s\n" % debug_msg)
