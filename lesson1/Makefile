HOST_FOLDER=backend

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Upgrade the pip and then install poetry
	pip install --upgrade pip
	pip install poetry

.PHONY: build
build: ## build
	docker build . -t "$(HOST_FOLDER):$$(poetry version -s)"

.PHONY: start-db
start-db: ## start-db
	docker run --name mongo -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongo-admin -e MONGO_INITDB_ROOT_PASSWORD=mongo-password -v mongo-volume:/data/db -d mongo:latest

.PHONY: deploy
deploy: start-db ## deploys $(HOST_FOLDER) at port 8000
	docker run -d --rm -p 8000:8000 -v "$${PWD}/$(HOST_FOLDER):/app:ro" --name $(HOST_FOLDER) "$(HOST_FOLDER):$$(poetry version -s)" 

.PHONY: stop-db
stop-db: ## stop-db
	docker rm -f mongo

.PHONY: stop
stop: stop-db ## stopdb & stop deploy
	docker rm -f $(HOST_FOLDER)

.PHONY: check-inner-file
check-inner-file:
	docker exec $(HOST_FOLDER) ls

