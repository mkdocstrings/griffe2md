"""griffe2md package.

Output API docs to Markdown using Griffe.
"""

from __future__ import annotations

from griffe2md._internal.cli import get_parser, main

__all__: list[str] = ["get_parser", "main"]
