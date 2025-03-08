import re

import {{ cookiecutter.project_slug }}


def test_version_is_semver_string():
    """Test that the version in pyproject.toml is a proper semantic version."""
    semver_pattern = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
    version = {{ cookiecutter.project_slug }}.__version__
    assert re.match(semver_pattern, version), (
        f'"{version}" is not a valid semver version'
    )
