"""
DBMQ setup.

For more information about setup file, check out
https://docs...
"""

import json
import logging
from os import path

import docker
from requests.exceptions import ConnectionError

import webserver
from extras import exceptions, flow
from extras.validator import ServerConfigsValidator


def main():
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
        raise SystemExit

    print(beautified_configs)
    print(beautified_root_configs)

    # Building process starts
    build(root_configs)


def build(root_configs):
    print(exceptions.BUILDING_IMAGE)
    try:
        client.images.build(**root_configs)
        print(exceptions.IMAGE_BUILT)
    except ConnectionError:
        print(exceptions.CONNECTION_REFUSED)
        raise SystemExit

    # Running process starts
    run(root_configs['tag'])


def run(tag):
    try:
        print(exceptions.RUNNING_CORE_CONTAINER)
        running = client.containers.run(image=tag, detach=True)
        print(exceptions.CONTAINER_IS_RUNNING)
    except ConnectionError:
        print(exceptions.CONTAINER_FAILED_IN_RUNNING)
        raise SystemExit

    container = client.containers.get(running.name)
    basic_configs = flow.ContainerConfigs(container.attrs)
    print(basic_configs)
    print(exceptions.STREAM_LOGGING_STARTED)

    # Stream logging
    process = running.logs(follow=True, stream=True)

    try:
        for line in process:
            print(line.decode('UTF-8'), end='')
    except KeyboardInterrupt:
        print(exceptions.EXIT_INTERRUPT)
        raise SystemExit


if __name__ == '__main__':
    try:
        client = docker.from_env()
        print(exceptions.DOCKER_EXCEPTION_SUCCESS)
        main()
    except docker.errors.DockerException:
        print(exceptions.DOCKER_EXCEPTION_FAILED)
        raise SystemExit
