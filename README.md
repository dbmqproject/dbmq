<p align="center">
  <img src=".git_components/images/logo.png" width="130"><br />
  Docker-based Message Queuing<br />
  <a href="https://docker-py.readthedocs.io">Docker SDK</a> - <a href="https://medium.com/@lnxpy/sample-project-in-dbmq-v2-1-d4f8cb41108c">Article on Medium</a> - <a href="https://dbmq.readthedocs.io">Read the Docs here ➤</a><br />
  Build and ship your Dockerized Django applications and feel free to use MBs<br />
  
  <img src="https://img.shields.io/badge/base%20package-Docker SDK 4.3.1-blue?logo=docker">
  <img src="https://img.shields.io/github/license/lnxpy/DBMQ?color=blue&logo=gnu">
  <img src="https://img.shields.io/badge/webserver-Django-blue?logo=django"><br />
  <a href='https://dbmq.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/dbmq/badge/?version=latest' alt='Documentation Status' />
  </a><br />
</p>

### Introduction
Docker-based Message Queuing (DBMQ) is an efficient way to run the pre-built configurations on the build process of [Dockerfiles](https://docs.docker.com/engine/reference/builder/). Once you have finished configuring, you will be able to create your images based on your configurations. DBMQ is very flexible with [Django](djangoproject.com) projects and you might stay away from troubles with creating a Dockerized Django project. After the building process, your image will be ready to get started. Use a text editor to step through your container and make changes. (the pre-installed editor is [Vim](https://www.vim.org/))

### Why DBMQ is Needed?
This system locates between the user and the Docker service. You config your requirements and let this automated system to provide them to you. You don't need to be a genius in Docker, just keep configuring. There is a channel between Docker and DBMQ called SDK. There are several services, but there is only one service that allows DBMQ to interact with Docker, which called [Docker Engine API](https://docs.docker.com/engine/api/). Docker is a distributed computing platform that allows you to decrease the latency and to cheap your project. You can keep up your project with distributed resources. (brokers, databases, etc)

### Installation
Before you clone DBMQ, you better make sure your Docker service is installed successfully. If there is something wrong, you can start browsing on the [Docker Installation Guide on Linux](https://runnable.com/docker/install-docker-on-linux). Make sure your Docker is running.

```shell
$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; vendor p>
     Active: active (running) since Mon 2020-09-07 23:47:00 +0430; 1s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 5644 (dockerd)
      Tasks: 25 (limit: 4502)
     Memory: 184.1M
     CGroup: /system.slice/docker.service
             ├─5644 /usr/bin/dockerd -H fd://
             └─5652 containerd --config /var/run/docker/containerd/containerd.t>
```
Clone the repository with the following command and either create a new virtualenv or, just keep installing the libraries on your real machine.
```shell
$ git clone https://github.com/lnxpy/DBMQ.git
...
$ cd ./DBMQ
```

- Using virtualenv (for more information about the venv installation, check out [virtualenv Installation](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b))
```shell
$ virtualenv .venv
...
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
```

- Without virtualenv
```shell
$ pip3 install -r requirements.txt
```
Installation has been completed. For the further steps, check out the [documents](https://dbmq.readthedocs.io).

### To-Do
The following to-do task list should be followed in order. If you are experienced enough in these tasks, you can start contributing to DBMQ. Fork the project, create PRs and I'll review them. If you've done any further task, change your task context grammatically in the following list.

- [x] **version 2.1 is being released**
- [x] `Docker_images` removed from the whole project
- [x] New logo represented for DBMQ v2.1
- [ ] Start writing documentations (Sphinx)
- [ ] Using python docker images instead of linux distros
- [ ] Tests
- [ ] New feature -> streaming the running containers
- [ ] Updating the links in the exceptions and repo 
- [ ] Database implementation process
- [ ] Broker implementation process
- [ ] **version 2.2 is being released**

### License & Contribution
DBMQ is licensed by [GPL-v3 (quick guide reference)](./LICENSE).
