FROM centos:centos8

# Start django project
# Configuration file exists at webserver.py

ARG PROJECT_NAME
ENV PROJECT_NAME ${PROJECT_NAME}

RUN yum -y install epel-release && yum clean all
RUN yum -y install python3-pip && yum clean all
RUN yum install vim-enhanced -y
RUN mkdir /$PROJECT_NAME

WORKDIR /$PROJECT_NAME

RUN pip3 install django
RUN django-admin startproject $PROJECT_NAME .

CMD python3 manage.py runserver 0.0.0.0:8000