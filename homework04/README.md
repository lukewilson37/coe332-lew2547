# Containerizing the Moon Landing Analysis
Luke Wilson
lew2547
3/1/2022

## CONTENTS

- Dockerfile
- ml_data_analysis.py
- test_ml_data_analysis.py
- Meteorite_Landings.json

### Dockerfile

This file contains the build steps necessary for the computer to build a docker image.

### ml_data_analysis.py

This python script preforms alanysis on a given meteorite landing data set. It will return each sites longitude and latitude as well as the hemisphere it is in

### test_ml_data_analysis.py

This script is a test script for ml_data_analysis.py. Using pytest it feeds dummy code ensuring the algorithms run properly.

### Meteorite_Landing.json

This is the data on which we preformed our analysis. Use this as example data format. Instructions will be provided on how to use other data


## How to run Docker File

To pull container:
```bash
$ docker pull lukewilson37/ml_data_analysis:1.0
```

To build docker file image:
```bash
$ docker build -t your_username/ml_data_analysis:1.0 .
```
To access sample data:
Go to /data file in container:
```bash
$ docker run --rm -it -v $PWD:/data username/ml_data_analysis:1.0 /bin/bash
```
To fetch sample data:
```bash 
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```
Or append your own data here

To Run with data:
```bash
$ docker run --rm -v $PWD:/data username/ml_data_analysis:1.0 ml_data_analysis.py /data/yourdata.json
```

To Run pytest:
``bash 
$ docker run --rm -v $PWD:/data username/ml_data_analysis:1.0 pytest
```

