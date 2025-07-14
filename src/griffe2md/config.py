"""Load configuration."""

import logging
from pathlib import Path
from typing import Any

import tomllib

logger = logging.getLogger(__name__)

PATHS = (
    Path(".config/griffe2md.toml"),
    Path("config/griffe2md.toml"),
    Path("pyproject.toml"),
)


def _locate_config_file() -> Path | None:
    for path in PATHS:
        if path.is_file():
            return path
    return None


def load_config() -> dict[str, Any] | None:
    """Load the configuration if config file or config entry in pyproject.toml exists.

    If neither config file was found or pyproject.toml file doesn't have
    a `[tool.griffe2md]` section, None is returned.
    """
    if not (config_path := _locate_config_file()):
        return None

    logger.debug("Loading config from %s", config_path)

    with config_path.open("rb") as f:
        config = tomllib.load(f)

    if config_path.name == "pyproject.toml":
        return config.get("tool", {}).get("griffe2md", None)
    return config
