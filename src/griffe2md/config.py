"""Load configuration."""

from __future__ import annotations

import logging
import sys
import typing
from pathlib import Path

if typing.TYPE_CHECKING:
    from griffe2md import rendering

# YORE: EOL 3.10: Replace block with line 2.
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

logger = logging.getLogger(__name__)

CONFIG_FILE_PATHS = (
    Path(".config/griffe2md.toml"),
    Path("config/griffe2md.toml"),
    Path("pyproject.toml"),
)


def _locate_config_file() -> Path | None:
    for path in CONFIG_FILE_PATHS:
        if path.is_file():
            return path
    return None


def load_config() -> rendering.ConfigDict | None:
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
    return typing.cast("rendering.ConfigDict", config)
