"""
DBMQ webserver configurations.

For more information about webserver file, check out
https://docs..
"""

from extras import settings

SERVER_CONFIGS = {
    # Core configurations
}

DATABASES = {
    # Database configurations
}

DBMQ_NETWORK = {
    # DBMQ network configurations
}

# Importing all configurations from the local file
try:
    from .local_webserver import *
except:
    pass
