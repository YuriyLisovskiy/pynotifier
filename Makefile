.DEFAULT_GOAL := help

.PHONY: bump-version-major bump-version-minor bump-version-patch help

bump-version-major:
	bump2version major

bump-version-minor:
	bump2version minor

bump-version-patch:
	bump2version patch

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
