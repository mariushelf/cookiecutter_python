import logging
from typing import Any

from pydantic import field_validator
from pydantic_settings import BaseSettings


class LogSettings(BaseSettings):
    """Define settings for the logger."""

    loglevel: int = logging.DEBUG  # loglevel for "our" packages
    loglevel_3rdparty: int = logging.WARNING  # loglevel for 3rdparty packages
    our_packages: list[str] = [
        # list of "our" packages
        "__main__",
        "the_next_iteration",
    ]
    basicConfig: dict[str, Any] = {
        # "basicConfig" of the logging module.
        # Do not include the level parameter here since it's being controlled
        # by the loglevel... parameters above.
        "format": "%(asctime)s:%(levelname)s:%(name)s:%(message)s",
    }

    @field_validator("loglevel", "loglevel_3rdparty")
    def string_to_loglevel(cls, v: str) -> int:
        """Convert a string to a loglevel."""
        try:
            return int(v)
        except TypeError:
            v = v.lower()
            if v == "debug":
                return logging.DEBUG
            elif v == "info":
                return logging.INFO
            elif v == "warning":
                return logging.WARNING
            elif v == "error":
                return logging.ERROR
            elif v == "critical":
                return logging.CRITICAL
            else:
                raise ValueError(f"invalid loglevel {v}")
