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

=====
#Local docker registry
#https://docs.docker.com/registry/deploying/#copy-an-image-from-docker-hub-to-your-registry

docker run -d -p 5000:5000 --restart=always --name registry registry:2


#get an image and push it to loca. The image removes makes sure the external refs are gone:ew
docker pull python:2.7.10
docker tag python:2.7.10 localhost:5000/python:2.7.10
docker push localhost:5000/python.2.7.10
docker image remove python:2.7.10 localhost:5000/python.2.7.10
docker pull localhost:5000/python:2.7.10


=====
#Clean up
docker rmi $(docker images -q -f dangling=true)

docker volume rm $(docker volume ls -qf dangling=true)



====
# Volumes, backup and restore

docker volume create --name pgdata

# mounting a postgres
docker run --name postgres -v pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=admin123 -d postgres

# back it up
docker run -it -v pgdata:/volume -v `pwd`/bak:/backup alpine tar -cjf /backup/some_archive.tar.bz2 -C /volume ./

# restore to new volume
docker volume create --name another
docker run -it -v another:/volume -v `pwd`/bak:/backup alpine sh -c "rm -rf /volume/*; tar -C /volume/ -xjf /backup/some_archive.tar.bz2"





"""
