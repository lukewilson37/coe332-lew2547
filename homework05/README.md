 # COE 332 Homework 5
 By Luke Wilson\
 Due: 04/05/2022\

The following homework uses a redis database and flask server to create an application that can access the [meteorite landing data](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json) through a database without having to remount the data or refetch the data from the internet.

## Accessing the Containerized Flask Application
  
You can pull the docker image with the following command:                                                                  

```bash
$ docker pull docker.io/lukewilson37/lew2547-hw5-flask-redis:latest
```

And you can run the container with:

```bash
$ docker run --name "lw5" -d -p 5037:5000 lukewilson37/lew2547-hw5-flask-redis:latest
```

## Interacting with the Flask Application

To interact with the flask application running in the container mentioned above we will us the ```curl``` command. Our application has 1 route with two method options described below.

```bash
$ curl -X POST localhost:5037/data			# Instructs server to gather meteorite landing data from web
$ curl localhost:5037/data					# gets meteorite landind data in json
```

## Dockerfile, Requirements and Makefile

The ```Dockerfile``` contains the instructions to run the flask application. ```Requirements.txt``` contains the python packages used in the app. If app is to be further developed, this file should be expanded. ```Makefile``` was used and can be used in the development process. It is mostly hard coded so any further use will require updating the file. 


