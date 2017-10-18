#!/bin/bash



echo """
Cheatsheet
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
