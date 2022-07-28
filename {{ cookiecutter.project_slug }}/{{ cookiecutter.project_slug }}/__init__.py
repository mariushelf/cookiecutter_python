import {{ cookiecutter.project_slug }}

try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from importlib_metadata import version

__version__ = version("{{ cookiecutter.project_slug }}")
