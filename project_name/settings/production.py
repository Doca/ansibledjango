from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))
STATIC_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'media'))
TEMPLATE_LOADERS = (
    (
        'django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )
    ),
)

PREPEND_WWW = True

ADMINS = (
    ('Dorian Cantzen', 'cantzen@extrument.com'),
)



DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'project_name',
        'PASSWORD': 'DATABASE_PW',
        'USER':'root'
    }
}
