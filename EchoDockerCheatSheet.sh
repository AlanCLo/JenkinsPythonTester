#!/bin/bash



echo """
Cheatsheet
=====
#Install docker on 14.04 ubuntu
wget -qO- https://get.docker.com/ | sh

#Install java 8 on 14.04 ubuntu
sudo apt-add-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
=====
docker run -d -it --expose 8000 -P --name=jt python:2.7.10 python

docker ps
docker exec -it <id> /bin/bash


cd home
git clone https://github.com/AlanCLo/JenkinsPythonTester.git
cd JenkinsPythonTester
sh JenkinsBuild.sh
python manage.py runserver 0.0.0.0:8000
"""
