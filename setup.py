"""
DBMQ setup.

For more information about setup file, check out
https://docs...
"""

import json
from os import path

import docker
from requests.exceptions import (ConnectionError,)
from logs.handlers import create_logger
import pathlib
from logging import (DEBUG, INFO, WARNING, ERROR, CRITICAL)


import webserver
from extras import exceptions, flow
from extras.validator import ServerConfigsValidator
from logs.logger import logging


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
        logging(logger, ERROR, process['data'])
        raise SystemExit

    print(beautified_configs)
    print(beautified_root_configs)

    # Building process starts
    build(root_configs)


def build(root_configs):
    logging(logger, INFO, exceptions.BUILDING_IMAGE)
    try:
        client.images.build(**root_configs)
        logging(logger, INFO, exceptions.IMAGE_BUILT)
    except ConnectionError:
        logging(logger, ERROR, exceptions.CONNECTION_REFUSED)
        raise SystemExit
    except:
        logging(logger, ERROR, exceptions.SOMETHING_IS_WRONG, siw='Building')
        raise SystemExit

    # Running process starts
    run(root_configs['tag'])


def run(tag):
    try:
        logging(logger, INFO, exceptions.RUNNING_CORE_CONTAINER)
        running = client.containers.run(image=tag, detach=True)
        logging(logger, INFO, exceptions.CONTAINER_IS_RUNNING)
    except ConnectionError:
        logging(logger, ERROR, exceptions.CONTAINER_FAILED_IN_RUNNING)
        raise SystemExit
    except:
        logging(logger, ERROR, exceptions.SOMETHING_IS_WRONG % 'Running')
        raise SystemExit

    container = client.containers.get(running.name)
    basic_configs = flow.ContainerConfigs(container.attrs)
    print(basic_configs)
    logging(logger, INFO, exceptions.STREAM_LOGGING_STARTED)

    # Stream logging
    process = running.logs(follow=True, stream=True)

    try:
        for line in process:
            print(line.decode('UTF-8'), end='')
    except KeyboardInterrupt:
        logging(logger, INFO, exceptions.EXIT_INTERRUPT)
        raise SystemExit
    except:
        logging(logger, ERROR, exceptions.SOMETHING_IS_WRONG %
                'Stream Logging')
        raise SystemExit


if __name__ == '__main__':
    BASE_DIR = pathlib.Path().absolute()
    logger = create_logger(BASE_DIR)

    try:
        client = docker.from_env()
        logging(logger, INFO, exceptions.DOCKER_EXCEPTION_SUCCESS)
        main()
    except docker.errors.DockerException:
        logging(logger, ERROR, exceptions.DOCKER_EXCEPTION_FAILED)
        raise SystemExit
