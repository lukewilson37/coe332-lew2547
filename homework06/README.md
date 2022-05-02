# COE332 HW6: Using Kubernetes to Create a Meteorite Landing Data Service

By: Luke Wilson
Due: 04/19/2022

The following homework uses kubernetes, a distributed system, to create a [Meteorite landing Data](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json) Service whose information persisst throughout time. 

## Contents

- app.py - contains the flask app used to post and get Meteorite Landing Data
- requirements.txt - file containing python packages used in flask api
- Dockerfile - file used to generate docker image
- Makefile - file used to expidite development of docker images
- lew2547-test-redis-deployment.yml - file describing the pod used as redis database
- lew2547-test-redis-pvc.yml - file descibing the persistant volume claim used by redis to store meteorite landing data
- lew2547-test-redis-service.yml - file describing the service used to direct calls from flask app to the most recent redis deployment
- lew2547-test-flask-deployment.yml - file describing the pod used as a flask application
- lew2547-test-flask-service.yml - file describing the service used to direct flask api call to most recent flask app deployment

## Deploying the Service System

Here I will describe the process by which the Meteorite Landing Data Service system is deployed

#### Enviorment

We begin by entering the kubernetes cluster generated for this class with 
```bash
$ ssh <tacc_username>@isp02.tacc.utexas.edu
$ ssh <tacc_username>@coe332-k8s.tacc.cloud
```
Once here we can begin to build out kubernetes system.

#### Flask Application

We copy the flask app and dockerfile from homework 5. The only changes that will need to be made involve the ip address of the redis server accessed in the flask application. we have not generated a redis servive so we will come back to this later.

#### Persistant Value Claim

We begin with the persistant value claim for our redis data. We create this PVC with the following command:
```bash
$ kubectl apply -f lew2547-test-redis-pvc.yml
```
Note the contents of this file are fairly simple but the user must change any username/name data to match the users name.

#### Redis Database

Now we move on to deploying the Redis Database which will operate on the persisting data stored in the claim above. The command used to deploy the database is
```bash
$ kubectl apply -f lew2547-test-redis-deployment.yml
```
Similar to the PVC, the contents of the file must be altered to match the users username. We must also be aware of how redis interacts with the PVC. We may need to alter the name of the ```volumeMounts:``` as well as its ```mountPath```. for this system we simply have ```mountPath: "/data"```.

#### Redis Service

The redis service is created with:
```bash
$ kubectl apply -f lew2547-test-redis-service.yml
```
This generates the service which will redirect any call to the most recent deployment of the redis database. We will take note of the servers IP address and port as it will be needed for our flask application to access the database. We find the address and port by calling
```
$ kubectl get service -o wide
```
Once we find the IP address and port of the redis service, we update out flask app to access the database with
```python
return redis.Redis(host='<redis_ip_address>', port=<redis_port>, db =0)
```
we then rebuild and push the docker image conatining the flask application.

#### Flask Application

To deploy the flask application, we first obtain the docker image tag of the flask app we will use. This will be the associated value with the ```image:``` key in the YAML file. For this system we want ```replicas: 2```. We then deploy the app with 
```bash
$ kubectl apply -f lew2547-test-flask-deployment.yml
```

#### Flask Service

This flask service is similar ot the redis service in that it redirects any service call to the most recent deployment of the flask api. It is created with
```bash
$ kubectl apply -f lew2547-test-flask-service.yml
```

#### Interacting with the System

To interact with the system, the flask sercive is key. In a similar way to the redis service, we must know the flaks IP address. we use this service IP address to interact with the database in the same way as in homework 5.

