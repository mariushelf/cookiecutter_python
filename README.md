# Cookiecutter Python

A simple [cookiecutter](https://github.com/cookiecutter/cookiecutter)
for any Python package.

Easily publish to PyPI from your local machine or automated via Github actions.

Automated linting and testing, locally and on Github.

Ready-to-use documentation and api-docs pipeline.


# Features

* Ready-to-release:
  * Extensive documentation on how to release your package
  * Github actions to run tests and release to PyPI
  * Makefile targets to test, build and release your code from your local machine
* Easy documentation: ready-to-rumble, [Read the Docs](https://readthedocs.org) compatible
  [sphinx](https://www.sphinx-doc.org/) configuration with Markdown support
  ((almost) no more Restructured Text)
* [Poetry](https://poetry.eustace.io/) dependency management
* Test pipeline with [pytest](https://docs.pytest.org/en/latest/) 
  and [tox](https://tox.wiki/)
* Linting and code check pipeline with [pre-commit](https://pre-commit.com), including:
  * [isort](https://github.com/timothycrosley/isort) - sorts your imports for you, so you don't have to
  * [black](https://github.com/psf/black) - the uncompromising code formatter
  * [flake8](https://gitlab.com/pycqa/flake8) - checking code formatting and style
  * [mypy](http://mypy-lang.org/) - check code, find type errors
  * [yamllint](http://www.yamllint.com/) - print warnings about
    badly formatted yaml files
  * [pydocstyle](http://www.pydocstyle.org/en/stable/index.html) - check
    docstrings for syntax and consistency

Inspired by [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

# Requirements

- This cookiecutter makes use of new features from Poetry 1.2.0 released on
  2022-08-31. Make sure to follow the
  [upgrade process](https://python-poetry.org/blog/announcing-poetry-1.2.0/)
  if you are still running an older version of poetry.


# Usage

```bash
# install cookiecutter and poetry into the current environment for the current user
pip install --user cookiecutter poetry

cookiecutter gh:mariushelf/cookiecutter_python
cd <your_project_slug>

# Write your code and tests now.
# Document everything in Markdown.

# Then run your tests with different Python versions (using tox):
make test

# Generate documentation
make docs

# and publish your code
make publish

# Or push to Github and create a Github release which gets automatically published
# to PyPI.
```

# Troubleshooting

* mypy checking can find a lot of bugs without even running the code, but sometimes it is too strict. There are a lot of [things you can configure](https://mypy.readthedocs.io/en/latest/config_file.html), but if it's a one of on just one or two lines of your code, you can tell mypy to ignore that specific line by appending `#  type: ignore` to it.
* The required version of poetry is 1.2.0. If you get problems regarding
  poetry or the `pyproject.toml`, make sure to check your poetry version
  and [update](https://python-poetry.org/blog/announcing-poetry-1.2.0/)
  it if necessary.
 