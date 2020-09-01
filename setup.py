"""
DBMQ setup.

For more information about setup file, check out
https://docs...
"""

import docker
import webserver
import json
from os import path
from extras import exceptions


def main(client):
    # TODO: Start managing containers

    # Reading local_configs for the paths
    with open('local_configs.json', 'r') as f:
        configs = json.load(f)
        beautified_configs = json.dumps(configs, sort_keys=True, indent=3)

    # Main Docker configurations are stored in root_config
    root_config = {
        'path': path.join(configs['DOCKER_FILES_DIR'],
                          webserver.SERVER_CONFIGS['CONTAINER']['IMAGE']),
        'tag': webserver.SERVER_CONFIGS['CONTAINER']['NAME'],
        'buildargs': {
            'PROJECT_NAME': webserver.SERVER_CONFIGS['NAME'],
        },
    }
    print(beautified_configs)

    # Building process starts
    try:
        client.images.build(**root_config)
        print(exceptions.IMAGE_BUILT)
    except:
        print(exceptions.CONNECTION_REFUSED)
        return

    # TODO: Running the images (with exceptional conditions)
    # TODO: Ending up the program "Press any key to exit.."-like
    # TODO: ++ Adding cache-usage feature in webserver configs


if __name__ == '__main__':
    try:
        client = docker.from_env()
        print(exceptions.DOCKER_EXCEPTION_SUCCESS)
        main(client)
    except docker.errors.DockerException:
        print(exceptions.DOCKER_EXCEPTION_FAILED)
