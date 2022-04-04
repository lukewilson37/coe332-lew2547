ME ?= lukewilson37

test: py_test build run clean

init: build run gather

images:
	docker images | grep ${NAME}

ps:
	docker ps -a | grep ${NAME}

logs:
	docker logs "lw5"

py_test:
	pytest

clean:
	docker stop "lw5"
	docker rm "lw5"

build:
	 docker build -t lukewilson37/lew2547-hw5-flask-redis:latest .

run:
	docker run --name "lw5" -d -p 5037:5000 lukewilson37/lew2547-hw5-flask-redis:latest

postdata:
	curl -X POST localhost:5037/data

getdata:
	curl localhost:5037/data

test:
	curl localhost:5037/

run_flask:
	 docker run --name "${NAME}-flask" -d -p 5037:5000 ${NAME}/whereisiss-flask:latest
	
push:
	docker push ${NAME}/whereisiss-flask:latest

gather:
	curl -X POST localhost:5037/init


