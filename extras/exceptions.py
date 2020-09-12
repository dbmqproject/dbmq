"""
Exception text handler.

For more information about exceptions file, check out
https://docs...
"""
from .textstyle import Failure, Succeed, Notification


DOCKER_EXCEPTION_FAILED = Failure('DBMQ Could Not Connect to Docker!',
                                  [
                                      'Make sure Docker service is running properly.',
                                      'Use an un-staff user.',
                                      'Either run up with the root user or, make sure your user is a member of Docker group.'
                                  ], 'https://docs...').text()

DOCKER_EXCEPTION_SUCCESS = Succeed('DBMQ Connected to Docker!',
                                   [
                                       'Reading the configurations..',
                                       'Checking the images existence..',
                                   ]).text()

IMAGE_BUILT = Succeed('Core image has been built successfully.').text()

CONNECTION_REFUSED = Failure('The Connection Between DBMQ and Docker Server Refused!',
                             [
                                 'Please check your connection and try again.',
                                 'Boot up the Docker service with no latency or duration.'
                             ], 'https://docs...').text()

BUILDING_IMAGE = Notification([
    'Sending the arguments to Dockerfile..',
    'Environment variables are setting..',
    'Building the core image and installing the packages.. (it might take a few minutes)',
]).text()
