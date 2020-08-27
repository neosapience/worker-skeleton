name := neosapience/appname-worker
tag := dev
pwd := $(shell pwd)

default: build

test:
	@docker-compose -f docker-compose.yml -f docker-compose.test.yml up -d

test-queue:
	@docker-compose stop worker
	@docker-compose -f docker-compose.yml -f docker-compose.test.queue.yml up -d

build:
	@docker build . -f docker/Dockerfile -t ${name}:${tag}

build-base:
	@docker build . -f docker/Dockerfile.base -t ${name}:base

ls:
	@docker images ${name}

history:
	@docker history ${name}:${tag}

up:
	@docker-compose up -d

down:
	@docker-compose down

ps:
	@docker-compose ps

logs:
	@docker-compose logs -f worker-test

sh:
	@docker run --rm -it -v ${pwd}/worker:/opt/code ${name}:${tag} sh
