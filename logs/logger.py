"""
DBMQ logger.

For more information about logger file, check out
https://docs...
"""


def logging(logger, level, exception, siw=''):
    if siw:
        title = exception.title % siw
    else:
        title = exception.title

    if level == 10:
        logger.debug(title)
    elif level == 20:
        logger.info(title)
    elif level == 30:
        logger.warning(title)
    elif level == 40:
        logger.error(title)
    elif level == 50:
        logger.critical(title)

    print(exception.text())
