HOST_FOLDER=backend

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Upgrade the pip and then install poetry
	pip install --upgrade pip
	pip install poetry

.PHONY: build
build:
	docker build . -t "$(HOST_FOLDER):$$(poetry version -s)"

.PHONY: deploy
deploy: ## deploys $(HOST_FOLDER) at port 8000
	docker run -d --rm -p 8000:8000 -v "$${PWD}/$(HOST_FOLDER):/app:ro" --name $(HOST_FOLDER) "$(HOST_FOLDER):$$(poetry version -s)" 

.PHONY: stop
stop:
	docker rm -f $(HOST_FOLDER)

.PHONY: check-inner-file
check-inner-file:
	docker exec $(HOST_FOLDER) ls