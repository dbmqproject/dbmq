"""
Exception text handler.

For more information about exceptions file, check out
https://docs...
"""
from .textstyle import Failure, Notification, Succeed

DOCKER_EXCEPTION_FAILED = Failure(
    'DBMQ Could Not Connect to Docker!',
    [
        'Make sure Docker service is running properly.',
        'Use an un-staff user.',
        'Either run up with the root user or, make sure your user is a member of Docker group.'
    ], 'https://docs...'
).text()

DOCKER_EXCEPTION_SUCCESS = Succeed(
    'DBMQ Connected to Docker!',
    [
        'Reading the configurations..',
        'Checking the images existence..',
    ]
).text()

IMAGE_BUILT = Succeed('Core Image Has Been Built Successfully.').text()

CONNECTION_REFUSED = Failure(
    'The Connection Between DBMQ and Docker Server Refused!',
    [
        'Please check your connection and try again.',
        'Boot up the Docker service with no latency or duration.',
        'Make sure you have stored your images and Dockerfiles on DOCKER_FILES_DIR.',
    ], 'https://docs...'
).text()

BUILDING_IMAGE = Notification(
    [
        'Sending the arguments to Dockerfile..',
        'Setting the environment variables..',
        'Building the core image and installing the packages.. (It might take a few minutes)',
    ]
).text()

RUNNING_CORE_CONTAINER = Notification(
    [
        'Running your core container..'
    ]
).text()

CONTAINER_IS_RUNNING = Succeed(
    'Core Container is Running in the Background.'
).text()

CONTAINER_FAILED_IN_RUNNING = Failure(
    'Could Not Run the Core Image',
    [
        'Make sure if there is any conflict with tags and solve them.',
        'Check your Docker stability.'
    ]
).text()

STREAM_LOGGING_STARTED = Notification(
    [
        'Stream logger is processing the console..',
    ]
).text()

EXIT_INTERRUPT = Failure(
    'This Session is About to Die.',
    [
        'Core container is still running.',
        'All other services are still available.',
        'View logs and keep developing on your containers manually.'
    ]
).text()

SOMETHING_IS_WRONG = Failure(
    'Something Went Wrong in the %s Process.'
).text()
