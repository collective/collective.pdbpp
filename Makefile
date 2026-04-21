TWINE_REPOSITORY ?= pypi

.PHONY: config-package
config-package:
	uvx --from plone.meta config-package . --no-commit

.PHONY: release
release:
	@echo "Releasing to repository: $(TWINE_REPOSITORY)"
	@echo "To release to a different repository, run \`make release TWINE_REPOSITORY=<repository>\`"
	TWINE_REPOSITORY="$(TWINE_REPOSITORY)" uvx \
		--from zest-releaser \
		--with zest-releaser\[recommended\] \
		--with zestreleaser-towncrier \
		fullrelease
