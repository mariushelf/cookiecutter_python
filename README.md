# About

A simple [cookiecutter](https://github.com/cookiecutter/cookiecutter)
to create a python package with

* [Poetry](https://poetry.eustace.io/) dependency management
* [pre-commit](https://pre-commit.com) hooks for black, flake8 and mypy
* pytest dependency.

Inspired by [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).


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

# License

[MIT](https://choosealicense.com/licenses/mit/)

