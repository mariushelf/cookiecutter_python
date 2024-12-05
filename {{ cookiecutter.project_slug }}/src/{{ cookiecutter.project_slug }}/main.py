import logging

from {{cookiecutter.project_slug}}.utils import setup_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the project pipeline."""
    setup_logging()
    logger.info("Running the project")


if __name__ == "__main__":
    main()
