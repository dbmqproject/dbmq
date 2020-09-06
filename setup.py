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
    root_configs = {
        'path': path.join(configs['DOCKER_FILES_DIR'],
                          webserver.SERVER_CONFIGS['CONTAINER']['IMAGE']),
        'tag': webserver.SERVER_CONFIGS['CONTAINER']['NAME'],
        'buildargs': {
            'PROJECT_NAME': webserver.SERVER_CONFIGS['NAME'],
        },
        'nocache': webserver.SERVER_CONFIGS['CONTAINER']['NOCACHE'],
    }

    beautified_root_configs = json.dumps(
        root_configs, sort_keys=True, indent=3)
    print(beautified_configs)

    # Building process starts
    try:
        client.images.build(**root_configs)
        print(exceptions.IMAGE_BUILT)
        print(beautified_root_configs)
    except:
        print(exceptions.CONNECTION_REFUSED)
        return

    # TODO: Running the images (with exceptional conditions)
    # TODO: Ending up the program "Press any key to exit.."-like


if __name__ == '__main__':
    try:
        client = docker.from_env()
        print(exceptions.DOCKER_EXCEPTION_SUCCESS)
        main(client)
    except docker.errors.DockerException:
        print(exceptions.DOCKER_EXCEPTION_FAILED)
