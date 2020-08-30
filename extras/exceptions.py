"""
Exception text handler.

For more information about exceptions file, check out
https://docs...
"""
from .textstyle import Failure


DOCKER_EXCEPTION = Failure('DBMQ Could Not Connect to Docker!',
                           [
                               'Make sure Docker service is running properly.',
                               'Use an un-staff user.',
                               'Either run up with the root user or, make sure your user is a member of Docker group.'
                           ], 'https://docs...').text()
