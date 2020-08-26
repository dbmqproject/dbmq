"""
DBMQ setup.

For more information about setup file, check out
https://docs...
"""

import docker
import webserver
from extras import exceptions, succeeds


def main(client):
    # TODO: Managing the containers
    pass


if __name__ == '__main__':
    try:
        client = docker.from_env()
        print(succeeds.DOCKER_EXCEPTION)
        main(client)
    except docker.errors.DockerException:
        print(exceptions.DOCKER_EXCEPTION)
