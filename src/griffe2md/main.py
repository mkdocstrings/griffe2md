"""Deprecated. Import from `griffe2md` directly."""

# YORE: Bump 2: Remove file.

import warnings
from typing import Any

from griffe2md._internal import main


def __getattr__(name: str) -> Any:
    warnings.warn(
        "Importing from `griffe2md.main` is deprecated. Import from `griffe2md` directly.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(main, name)
