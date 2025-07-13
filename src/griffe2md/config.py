"""Load configuration."""

import logging
import pathlib
from typing import Optional

import tomllib

logger = logging.getLogger(__name__)

PATHS = (
    ".config/griffe2md.toml",
    "config/griffe2md.toml",
)

PYPROJECT = "pyproject.toml"


def _locate_config_file() -> Optional[pathlib.Path]:
    for path in PATHS:
        path_ = pathlib.Path(path)
        if path_.is_file():
            return path_

    pyproj_path = pathlib.Path(PYPROJECT)
    if pyproj_path.is_file():
        return pyproj_path

    return None


def load_config() -> Optional[dict]:
    """Load the configuration if config file or config entry in pyproject.toml exists. If neither config file was found or pyproject.toml file doesn't have [tool.griffe2md] section, returns None."""
    config_path = _locate_config_file()
    if config_path is None:
        return None

    logger.debug("Loading config from %s", config_path)

    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    if str(config_path) == PYPROJECT:
        return (config.get("tool") or {}).get("griffe2md")
    return config
