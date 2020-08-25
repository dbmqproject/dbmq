"""
DBMQ settings.

For more information about webserver_configs file, check out
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