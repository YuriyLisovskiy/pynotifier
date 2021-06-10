VENV = .venv/bin

.DEFAULT_GOAL := help

.PHONY: clean help
clean: ## Remove Python file artifacts and virtualenv
	@echo "+ $@"
	@rm -rf .venv

${VENV}/python:
	@echo "+ $@"
	python -m venv .venv

venv: ${VENV}/python ## Creates the virtualenv and installs tox
	@echo "+ $@"
	$(VENV)/pip install tox

test: venv ## Run tests
	@echo "+ $@"
	$(VENV)/tox -e py

lint: venv ## Lint source
	@echo "+ $@"
	$(VENV)/tox -e lint

ci: venv ## Lint and Test
	@echo "+ $@"
	$(VENV)/tox

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
