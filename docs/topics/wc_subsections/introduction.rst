Introduction
============

All essential configurations are stored in a file named ``webserver.py`` in the root directory of the project. 
Make sure you have already switched into the root directory of the project. Use a `text editor
<https://en.wikipedia.org/wiki/List_of_text_editors>`_ in order to make changes.

You configure your images, containers, tags, environment variables, and etc in your ``webserver.py`` file. These 
configurations you write in the file will be authorized in the running process. The authorizer is an instance from 
the ``BaseModel`` class in the `pydantic
<https://pypi.org/project/pydantic/>`_ module.