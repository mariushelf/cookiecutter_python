# {{ cookiecutter.project_name }}

[![Tests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/tests.yml/badge.svg)](https://github.com/mariushelf/bcdict/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)


{{ cookiecutter.project_short_description }}

Original repository: [https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})


# Linting and Testing

## Locally on every commit

On every commit, some code formatting and checking tools are run by
[pre-commit](https://pre-commit.com/).

The test pipeline is configured in the
[.pre-commit-config.yaml](.pre-commit-config.yaml).


## Running tests locally

On your local machine, you can run tests by running `make test`.

This uses [Tox](https://tox.wiki/en/latest/) to run tests for a variety
of Python versions.

As a prerequisite you need to install all those Python version, e.g., with
[pyenv](https://github.com/pyenv/pyenv).

To configure the Python versions under test, edit the [tox.ini](tox.ini).


## With Github actions

After every push to Github, the [tests.yml](.github/workflows/tests.yml)
workflow is run. It runs the tests in the [tests](tests) folder for a bunch
of Python versions.

It also uploads the code coverage report to [codecov](https://codecov.io).

**Note:** for private repositories you need to acquire a token from codecov
and configure in in the `tests.yaml` workflow file and in Github secrets.

To configure which Python versions are tested, edit the `python-version`
list in the `tests.yml` workflow file.


# How to release to PyPI

You can upload the package either from your local machine via twine, or
by using Github actions.


## Release with Github actions

To make a release via Github actions, you need to create a release in
Github. When the release is published, the
[publish-to-pypi.yaml](.github/workflows/publish-to-pypi.yaml) workflow
is run.

To create a release in Github you need to create a tag.

For this project it is necessary that the tag matches the version number.
E.g., for version `1.2.3` the tag must be `v1.2.3` (note the `v`).

### Prerequisites

1. Create an API token in the
   [PyPI account settings](https://pypi.org/manage/account/).
   If you don't have a PyPI account yet, create one. *Do not close the
   page right away, you will never see the token again!*
   
   **Note:** before you upload the package for the first time, you can
   only create a global api token with access to all your packages. It is
   *highly* recommended to replace it with a package-specific token after
   you have published your package for the first time.
3. In the [Github repository settings](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/environments),
   create a new environment named `production`. If you are the only
   contributor, you can leave all settings at the default.
4. Under [Secrets -> actions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets/actions),
   create a new secret named `PYPI_API_TOKEN` and copy the token from PyPI
   as value.


### Create a release and publish the package to PyPI

1. update the version number in the [pyproject.toml](pyproject.toml)
2. create a matching tag on your local machine and push it to the
   Github repository:
   ```bash
   git tag v1.2.3
   git push --tags
   ```
3. In [Github actions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
   make sure that the test workflow succeeds.
4. In the Github [release tab](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases)
   click "Draft a new release". Fill in the form. When you click publish,
   the `publish-to-pypi` workflow is run.
   
   It checks that the tag matches the version number and then builds and
   publishes the package to
   [PyPI](https://pypi.org/project/{{ cookiecutter.project_slug }}/).

## Upload from the local machine

[twine](https://twine.readthedocs.io/en/stable/) allows to upload a package
from your local machine to PyPI.

### Prerequisites

You need a PyPI API token. See prerequisites for the Github actions above
(you don't need to perform any actions on Github when using twine, so you
only need to perform step 1).

### Configuration

The PyPI credentials must be configured either via a configuration file
or via environment variables.
See the [twine documentation](https://twine.readthedocs.io/en/stable/#configuration)
for details.

Since we are using an api token to authenticate with PyPI, the username
must be set to `__token__`, and the password is the actual token.

When using the PyPI test server, the repository url must be set to
`https://test.pypi.org/legacy/`.

### Usage

The `publish` target in the [Makefile](Makefile) calls twine to upload
a package to PyPI.

**Note:** the upload command is deactivated by default to prevent accidental
uploads. You need to manually uncomment it before the first release.

Here are the necessary steps:

1. update the version number in the [pyproject.toml](pyproject.toml)
2. run `make publish`.

# Contact

{{ cookiecutter.full_name }} 
  ([{{ cookiecutter.email }}](mailto:{{ cookiecutter.email }}))


# License
{% set is_open_source = cookiecutter.license != 'Not open source' -%}
{% if is_open_source %}
{{ cookiecutter.license }} -- see [LICENSE](LICENSE)
{% else %}
Not open source -- see [LICENSE](LICENSE)
{% endif %}
