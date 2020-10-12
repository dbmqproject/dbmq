"""
DBMQ handlers.

For more information about handlers file, check out
https://docs...
"""

import logging
import logging.config
import pathlib


def create_logger(base):
    # base logging configuration
    logging.config.fileConfig(
        fname=base / 'logs/logging_config.ini',
        disable_existing_loggers=False,
    )

    logger = logging.getLogger('DBMQ-LOGGER')
    return logger
