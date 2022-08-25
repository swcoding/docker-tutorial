.PHONY: help
help:
        @grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Upgrade the pip and then install poetry
		pip install --upgrade pip
		pip install poetry

.PHONY: deploy
deploy: ## deploys backend at port 8000
		uvicorn backend.backend.app:app --reload