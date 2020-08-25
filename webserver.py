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
        'NAME': 'container-name',
    },
    'NAME': 'database-name',
    'SERVER': settings.Database.postgres,
    'USERNAME': 'user',
    'PASSWORD': 'pass',
}
