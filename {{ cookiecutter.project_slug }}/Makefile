SHELL := /bin/bash

install:
	poetry install

clean:
	rm -rf dist

test: install
	poetry run tox -p -o -r

build:
	poetry build

# deactivated by default to prevent accidental uploads
publish: test clean build
	echo "NOT uploading to PyPI. You need to uncomment the command in the Makefile."
#	poetry run python -mtwine upload dist/* --verbose
