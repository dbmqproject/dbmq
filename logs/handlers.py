"""
DBMQ handlers.

For more information about handlers file, check out
https://docs...
"""

import logging


# custom stream handler
class MyStreamHandler(logging.StreamHandler):
    def emit(self, record):
        if record.levelno == self.level:
            super().emit(record)


def logger_handler():
    # base logging configuration
    logger = logging.getLogger('DBMQ')
    logger.setLevel(logging.DEBUG)

    # stream handler
    stream_handler = MyStreamHandler()
    stream_handler.setLevel(logging.INFO)

    # file handler
    file_handler = logging.FileHandler(
        './data/file.log',
        mode='a',
        encoding='UTF-8',
    )
    file_handler.setLevel(logging.WARNING)

    # formatters
    stream_formatter = logging.Formatter(
        '%(message)s',
    )
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
    )
    stream_handler.setFormatter(stream_formatter)
    file_handler.setFormatter(file_formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger
