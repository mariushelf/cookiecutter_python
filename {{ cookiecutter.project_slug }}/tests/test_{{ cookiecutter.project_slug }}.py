import re

import {{ cookiecutter.project_slug }}


# TODO: implement your tests here!

def test_reminder():
    assert False, "If this test runs it probably means that you have not written your own tests yet. Do it now!"

def test_version_is_semver_string():
    semver_pattern = r'^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'
    version = {{ cookiecutter.project_slug }}.__version__
    print(f"Version is {version}")
    assert re.match(semver_pattern, version)
