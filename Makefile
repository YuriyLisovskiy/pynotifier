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
	PLATFORM=$$(python -c 'import sys; print(sys.platform)') $(VENV)/tox -e py

lint: venv ## Lint source
	@echo "+ $@"
	$(VENV)/tox -e lint

ci: venv ## Lint and Test
	@echo "+ $@"
	PLATFORM=$$(python -c 'import sys; print(sys.platform)') $(VENV)/tox -e lint,py

bump-version-major:
	bump2version major

bump-version-minor:
	bump2version minor

bump-version-patch:
	bump2version patch

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
