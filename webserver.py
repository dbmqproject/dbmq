"""
DBMQ webserver configurations.

For more information about webserver file, check out
https://docs..
"""

from extras import settings

SERVER_CONFIGS = {
    'CONTAINER': {
        'IMAGE': settings.Image.ubuntu,
        'NAME': 'django_app',
    },
    'NAME': 'djangotest',
    'SERVER': settings.Server.django,
}

DATABASES = {
    'CONTAINER': {
        'NAME': 'django_db',
    },
    'NAME': 'django',
    'SERVER': settings.Database.postgres,
    'USERNAME': 'test',
    'PASSWORD': 'test123',
}
