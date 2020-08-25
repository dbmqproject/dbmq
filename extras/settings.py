class Image:
    """
    Available images are stored here.
    Example script: `settings.Images.ubuntu`
    """
    
    ubuntu = 'ubuntu'
    centos = 'centos'

class Server:
    """
    Available servers are stored here.
    Example script: `settings.Server.django`"""
    
    django = 'django'
    flask = 'flask'

class Database:
    """
    Available databases are stored here.
    Example script: `settings.Database.postgres`
    """
    
    postgres = 'postgres'
    mysql = 'mysql'

class Broker:
    """
    Available brokers are stored here.
    Example script: `settings.Broker.rabbitmq`
    """
    
    rabbitmq = 'rabbitmq'
    redis = 'redis'