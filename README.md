# Cookiecutter Python

A simple [cookiecutter](https://github.com/cookiecutter/cookiecutter)
for any Python package.

Easily publish to PyPI from your local machine or automated via Github actions.

Automated linting and testing, locally and on Github.


# Features

* [Poetry](https://poetry.eustace.io/) dependency management
* [pre-commit](https://pre-commit.com) hooks for:
  * [isort](https://github.com/timothycrosley/isort) - sorts your imports for you, so you don't have to
  * [black](https://github.com/psf/black) - the uncompromising code formatter
  * [flake8](https://gitlab.com/pycqa/flake8) - checking code formatting and style
  * [mypy](http://mypy-lang.org/) - check code, find type errors
    * mypy checking can find a lot of bugs without even running the code, but sometimes it is too strict. There are a lot of [things you can configure](https://mypy.readthedocs.io/en/latest/config_file.html), but if it's a one of on just one or two lines of your code, you can tell mypy to ignore that specific line by appending `#  type: ignore` to it. E.g.,
    
      `reduce(lambda x, y: x & y, filters)  # type: ignore`
* [pytest](https://docs.pytest.org/en/latest/) dependency.
* Github actions to run tests and release to PyPI
* Makefile targets to test, build and release your code from your local machine
* Extensive documentation on how to release your package to PyPI

Inspired by [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).


# Usage

```bash
# install cookiecutter and poetry into the current environment for the current user
pip install --user cookiecutter poetry

cookiecutter gh:mariushelf/cookiecutter_python
cd <your_project_slug>
# write your code and tests now

# Then run your tests with different Python versions (using tox):
make test

# and publish your code
make publish

# Or push to Github and create a Github release which gets automatically published
# to PyPI.
```

# License

[MIT](https://choosealicense.com/licenses/mit/)

