DBMQ (Docker-based Message Queuing)
===================================

Docker-based Message Queuing (DBMQ) is an efficient way to run the pre-built configurations on the build process of Dockerfiles.
Once you have finished configuring, you will be able to create your images based on your configurations.

.. warning::
   DBMQ is fully stable on Linux-based distributions and there is no guarantee that this tool works as properly
   as what it does on the Linux machines on Windows machines.

Why DBMQ is Needed
------------------

This system locates between the user and the Docker service. You config your requirements and let this automated system to provide them to you.
You don't need to be a genius in Docker, just keep configuring.

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents:

   topics/webserver_configurations.rst

Installation
------------

This installation process is valid on the Linux-based distributions so that you better to find the equivalent commands on other machines.
The things you need to do is to install ``Docker`` engine on your machine and make sure you have ``python>=3.8`` available on your machine.
We will catch all steps one by one. Let's have a general view on the way that we want to get through. First of all, we will install Docker and then,
we will take a closer look on python and ``virtualenvs``.

.. note::
   We are going to install all dependencies through an isolated environment called ``env``.

Docker Installation
~~~~~~~~~~~~~~~~~~~

Depending on your distribution, you need to find the way that you can install Docker on your machine. Here is the `Official Docker Installation Guide
<https://docs.docker.com/engine/install/ubuntu/>`_ that will help you to setup Docker on your distribution. The focuses are more on DBMQ and all its
dependencies.

DBMQ Installation
~~~~~~~~~~~~~~~~~

In this section, you need to clone the project on your local machine and start installing the dependencies. Use the following command in order to 
clone the repository.

.. code-block:: shell

  $ git clone https://github.com/dbmqproject/dbmq.git/

Once it's done, everything would be ready for the virtual environment. We are keeping up with ``virtualenv`` package
which is available on 
`PyPi
<https://pypi.org/>`_.