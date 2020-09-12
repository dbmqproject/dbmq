"""
This module includes all pre-build utilities you might need.
Use the imported `settings` module in the webserver configs from the extras dir.

For more information about settings file, check out
https://docs...
"""


class Image:
    """
    Available images are stored here.
    Example script: `settings.Images.centos_8`
    """

    centos_8 = 'centos_8'


class Server:
    """
    Available web servers are stored here.
    Example script: `settings.Server.django`"""

    django = 'django'


class Database:
    """
    Available databases are stored here.
    Example script: `settings.Database.postgres`
    """

    postgres = 'postgres'


class Broker:
    """
    Available brokers are stored here.
    Example script: `settings.Broker.rabbitmq`
    """

    rabbitmq = 'rabbitmq'
