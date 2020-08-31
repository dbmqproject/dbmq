"""
DBMQ setup.

For more information about setup file, check out
https://docs...
"""

import docker
import sys
import webserver
from extras import exceptions, succeeds


def main(client, args):
    # TODO: Manage args & start managing containers
    try:
        client.images.build(
            path='docker_files/centos/',
            buildargs={'PROJECT_NAME': webserver.SERVER_CONFIGS['NAME']},
            tag=webserver.SERVER_CONFIGS['CONTAINER']['NAME'],
        )
        print('Done.')
    except Exception as e:
        print('Something went wrong!')
        print(e)


if __name__ == '__main__':
    try:
        client = docker.from_env()
        print(succeeds.DOCKER_EXCEPTION)
        main(client, sys.argv[1:])
    except docker.errors.DockerException:
        print(exceptions.DOCKER_EXCEPTION)
