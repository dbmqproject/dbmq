"""
Exception text handler.

For more information about exceptions file, check out
https://docs...
"""
from .textstyle import Alert, Style

DOCKER_EXCEPTION = '%sDBMQ Could Not Connect to Docker!%s' % (
    Alert.failed, Style.clear)
