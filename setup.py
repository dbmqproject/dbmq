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
    pass


if __name__ == '__main__':
    try:
        client = docker.from_env()
        print(succeeds.DOCKER_EXCEPTION)
        main(client, sys.argv[1:])
    except docker.errors.DockerException:
        print(exceptions.DOCKER_EXCEPTION)
