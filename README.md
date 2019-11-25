# About

A simple cookiecutter to create a python package with

* [Poetry](https://poetry.eustace.io/) dependency management
* [pre-commit](https://pre-commit.com) hooks for black and flake8
* pytest dependency

# Usage

```bash
# install cookiecutter and poetry into the current environment for the current user
pip install --user cookiecutter poetry

cookiecutter gh:mariushelf/cookiecutter_python
cd <your_project_slug>
git init
poetry install
poetry run pre-commit install
```

