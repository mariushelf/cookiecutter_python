import logging
import os


def get_logger() -> logging.Logger:
    """Create a logger instance that can be imported in other modules.

    Returns
    -------
    logger : logging.Logger
        Logger instance.
    """
    logger = logging.getLogger("src")
    logger.setLevel(logging.DEBUG)

    loglevel = os.environ.get("LOGLEVEL", "INFO")

    sh = logging.StreamHandler()
    sh.setLevel(logging.getLevelName(loglevel))

    formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s")
    sh.setFormatter(formatter)

    logger.addHandler(sh)

    return logger


logger = get_logger()
