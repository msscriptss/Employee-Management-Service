# Employee Management Service

## Technologies
- Python
- Flask
- SQLAlchemy
- SQLite
- Docker

## Required Dependencies 
- pip3 `sudo apt-get -y install python3-pip`
- virtualenv  `pip3 install virtualenv`
- pre-commit `pip3 install pre-commit`


## Base Setup
- Install setup `. install.sh`


## Installation of the necessary “packages”.
- Docker → [Docker Installation Tutorial](https://docs.docker.com/engine/install/ubuntu/)
- Docker compose → [docker-compose Installation Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-pt)


## Environment variables
_You need create **.env** file, use ``.env.example`` file for template_
```
APPLICATION_PORT=3008
```

## Start Project
cd database
sqlite3 testDB.db
Run the migration scripts inside database folder. 
_Docker is configured to raise two containers, the flask application image and the postgres database. For more details see the **docker-compose.yml** configuration file_
```
docker-compose up --build
```
_If everything went well, you will be able to access the **web api** on localhost and the port chosen in your ``.env``
by default:_
[http://127.0.0.1:3008/](http://127.0.0.1:3008/)