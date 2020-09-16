"""
DBMQ setup.

For more information about setup file, check out
https://docs...
"""

import docker
import webserver
import json
import sys
from os import path
from extras import exceptions
from extras.validator import ServerConfigsValidator


def main(client):
    # Reading local_configs for the paths
    with open('workdir.json', 'r') as f:
        configs = json.load(f)
        beautified_configs = json.dumps(
            configs, sort_keys=True, indent=3)

    process = ServerConfigsValidator(webserver.SERVER_CONFIGS)

    if process['status']:
        main_data = process['data']

        # Main Docker configurations are stored in root_configs
        root_configs = {
            'path': path.join(configs['DOCKER_FILES_DIR'],
                              main_data['CONTAINER']['IMAGE']),
            'tag': main_data['CONTAINER']['NAME'],
            'buildargs': {
                'PROJECT_NAME': main_data['NAME'],
            },
            'nocache': main_data['CONTAINER']['NOCACHE'],
        }
        beautified_root_configs = json.dumps(
            main_data, sort_keys=True, indent=3)
    else:
        print(process['data'])
        return

    print(beautified_configs)
    print(beautified_root_configs)

    # Building process starts
    build(root_configs)


def build(root_configs):
    print(exceptions.BUILDING_IMAGE)
    try:
        client.images.build(**root_configs)
        print(exceptions.IMAGE_BUILT)
    except:
        print(exceptions.CONNECTION_REFUSED)
        return

    # Running process starts
    try:
        print(exceptions.RUNNING_CONTAINER)
        running = client.containers.run(image=root_configs['tag'], detach=True)
        print(exceptions.CONTAINER_IS_RUNNING)
    except Exception as e:
        print(exceptions.CONTAINER_FAILED_IN_RUNNING)
        return

    # TODO: Attributes filtering on the executed container
    # TODO: Showing an inspect of the Core container

    # Stream logging
    process = running.logs(follow=True, stream=True)
    for line in process:
        print(line.decode('UTF-8'), end='')

    # TODO: Solving some conflicts on styling file


if __name__ == '__main__':
    try:
        client = docker.from_env()
        print(exceptions.DOCKER_EXCEPTION_SUCCESS)
        main(client)
    except docker.errors.DockerException:
        print(exceptions.DOCKER_EXCEPTION_FAILED)
