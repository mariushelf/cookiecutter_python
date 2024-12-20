#!/usr/bin/env sh
# Integration test for the cookiecutter.
# Creates a project with the cookiecutter and tests that:
# * The documentation builds
# * The test_reminder test fails as expected
# * All other tests pass
# * The main.py script executes successfully

set -xe

CURRENT_DIR=$(pwd)

rm -rf test_project

cookiecutter --no-input --default-config \
  -o test_project \
   . \
  author_name="Joe Doe" \
    author_email="joe@example.com" \
    github_username="jdoe" \
    project_name="My Project" \
    project_short_description="This is a test project." \
    version="1.2.3" \
    license="MIT"
echo "✅ Cookiecutter executes successfully."

cd test_project/my_project

poetry install

git add .
poetry run pre-commit run --all-files
echo "✅ Commit hooks installed and working."

# check that we can run the project
poetry run python -m my_project.main
echo "✅ main.py script executes successfully."

# check that the documentation builds without warnings
make docs
echo "✅ Documentation builds."

# check that the tests pass (apart from the test_reminder which always fails)
TOX_ARGS="-k 'not test_reminder'" make test

# check that the test_reminder fails
if TOX_ARGS="-k test_reminder" make test ; then
    echo 'test_reminder test does not fail.' >&2
    exit 1
fi
echo "✅ test_reminder test failed as expected."

cd "${CURRENT_DIR}"
#rm -rf test_project

echo "✅ Cookiecutter project tested successfully. All good 🤩"
