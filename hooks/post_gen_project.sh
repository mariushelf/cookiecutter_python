#!/bin/bash
git init
git config --local user.name "{{cookiecutter.full_name}}"
git config --local user.email {{cookiecutter.email}}
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
