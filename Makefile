.PHONY: test

test:
	./tests/test.sh

test-all:
	tox p
