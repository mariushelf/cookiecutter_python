# About

A simple [cookiecutter](https://github.com/cookiecutter/cookiecutter)
to create a python package with

* [Poetry](https://poetry.eustace.io/) dependency management
* [pre-commit](https://pre-commit.com) hooks for:
  * [isort](https://github.com/timothycrosley/isort) - sorts your imports for you, so you don't have to
  * [black](https://github.com/psf/black) - the uncompromising code formatter
  * [flake8](https://gitlab.com/pycqa/flake8) - checking code formatting and style
  * [mypy](http://mypy-lang.org/) - check code, find type errors
    * mypy checking can find a lot of bugs without even running the code, but sometimes it is too strict. There are a lot of [things you can configure](https://mypy.readthedocs.io/en/latest/config_file.html), but if it's a one of on just one or two lines of your code, you can tell mypy to ignore that specific line by appending `#  type: ignore` to it. E.g.,
    
      `reduce(lambda x, y: x & y, filters)  # type: ignore`
* [pytest](https://docs.pytest.org/en/latest/) dependency.

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

