.DEFAULT_GOAL := help

.PHONY: deps test test_coverage help

deps:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements.dev.txt

test:
	python -m unittest discover tests/

test_coverage:
	coverage run -m unittest discover tests/
	coverage html

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
