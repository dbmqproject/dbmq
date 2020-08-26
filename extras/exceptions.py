"""
Exception text handler.

For more information about exceptions file, check out
https://docs...
"""
from .textstyle import Alert, Style

DOCKER_EXCEPTION = """
%sDBMQ Could Not Connect to Docker!%s

- Make sure your Docker service is running.
- Check your permission. Try again with the highest previlages.
- Check the status of your Docker service.
- Restart the Docker and try again.
""" % (Alert.failed, Style.clear)
