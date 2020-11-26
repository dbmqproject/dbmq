``SERVER_CONFIGS`` configurations
=================================

Server configurations take three parameter in a variable name ``SERVER_CONFIGS`` in the ``webserver.py`` file. 
This variable has to be filled with the proper values. It's kind of an essential argument to the main process. 

CONTAINER
    It refers to the container that contains the core distribution. Mostly it's ``settings.Image.centos_8`` as 
    ``IMAGE`` by default. ``NAME`` parameter is equal to tag in the Docker concepts. Use this parameter in order 
    to pick a name for your core container.

    * ``IMAGE`` : The image you want to serve your core container on.
    * ``NAME`` : Tag name you want to name your container to.
    * ``NOCACHE`` : It allows you to specify whether you want to use caches or not. It's set to ``False`` by default which means it does use the caches.

    .. code-block:: python

        SERVER_CONFIGS = {
            ...
            'CONTAINER': {
                'IMAGE': settings.Image.centos_8,
                'NAME': 'django_core',
            },
            ...
        }

NAME
    You can specify your Django core project name with the ``NAME`` parameter. It only inputs a name as follows.

    .. code-block:: python

        SERVER_CONFIGS = {
            ...
            'NAME': 'sample',
            ...
        }
    
    This parameter will be executed in the following way so make sure you will never need to change this name.

    .. code-block:: shell

        $ django-admin startproject sample .

SERVER
    This parameter refers to the server you are building in your containers. Only ``settings.Server.django`` is available by now. 
    It's like the webserver you are going to setup within your Docker containers.
    
    .. code-block:: python

        SERVER_CONFIGS = {
            ...
            'SERVER': settings.Server.django,
            ...
        }

.. warning::
    Make sure the keys in the ``SERVER_CONFIGS`` are all uppercase. All validators are case-sensitive. For example, we have 
    the ``SERVER_CONFIGS.CONTAINER`` validator right below. 

    .. code-block:: python
    
        class Container(BaseModel):
            IMAGE: str
            NAME: str
            NOCACHE: bool = False