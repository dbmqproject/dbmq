"""
DBMQ webserver configurations.

For more information about webserver file, check out
https://docs..
"""

from extras import settings

# Core configurations
SERVER_CONFIGS = {
    'CONTAINER': {
        'IMAGE': settings.Image.centos,
        'NAME': 'django_app',
        'NOCACHE': False,
    },
    'NAME': 'djangotest',
    'SERVER': settings.Server.django,
}

# Database configurations
DATABASES = {
    'CONTAINER': {
        'NAME': 'django_db',
    },
    'NAME': 'django',
    'SERVER': settings.Database.postgres,
    'USERNAME': 'test',
    'PASSWORD': 'test123',
}

# DBMQ network configurations
DBMQ_NETWORK = {}
