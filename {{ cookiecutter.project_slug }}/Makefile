SHELL := /bin/bash

.PHONY: docs

install:
	poetry install

clean: clean_docs
	rm -rf dist

clean_docs:
	cd docs && make clean

test: install
	poetry run pytest tests

docs:
	cd docs && poetry run make html
	echo You can now browse the documentation at ./docs/build/index.html

build: docs
	poetry build
