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
        # Main Docker configurations are stored in root_config
        root_configs = {
            'path': path.join(configs['DOCKER_FILES_DIR'],
                              main_data['CONTAINER']['IMAGE']),
            'tag': main_data['CONTAINER']['NAME'],
            'buildargs': {
                'PROJECT_NAME': main_data['NAME'],
            },
            'nocache': main_data['CONTAINER']['NOCACHE'],
        }
        beautified_root_configs = json.dumps(process, sort_keys=True, indent=3)
    else:
        print(process['data'])
        return

    print(beautified_configs)
    print(beautified_root_configs)

    # Building process starts
    build(root_configs)


def build(root_configs):
    toolbar_width = 30

    # setup toolbar
    sys.stdout.write("Building Your Core Image.. [%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    # return to start of line, after '['
    sys.stdout.write("\b" * (toolbar_width+1))

    for i in range(toolbar_width):
        client.images.build(**root_configs)
        # update the bar
        sys.stdout.write('-')
        sys.stdout.flush()

    sys.stdout.write("]\n")  # this ends the progress bar
    print(exceptions.IMAGE_BUILT)


if __name__ == '__main__':
    try:
        client = docker.from_env()
        print(exceptions.DOCKER_EXCEPTION_SUCCESS)
        main(client)
    except docker.errors.DockerException:
        print(exceptions.DOCKER_EXCEPTION_FAILED)
