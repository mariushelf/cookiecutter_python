#!/bin/bash
set -e
echo Initializing and configuring git...
git init
git config --local user.name "{{cookiecutter.full_name}}"
git config --local user.email {{cookiecutter.email}}
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
echo Installing package dependencies locally...
poetry install
echo Installing pre-commit hooks...
poetry run pre-commit install
echo "Done. Happy coding! It's gonna be great 🤩"
