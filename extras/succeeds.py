"""
Succeed text handler.

For more information about succeeds file, check out
https://docs...
"""
from .textstyle import Alert, Style

DOCKER_EXCEPTION = '%sDBMQ Connected to Docker!%s' % (
    Alert.succeed, Style.clear)
