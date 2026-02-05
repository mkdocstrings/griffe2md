"""Test config loading."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import Mock, patch

import pytest

import griffe2md

if TYPE_CHECKING:
    import py


@pytest.mark.parametrize("rel_path", griffe2md.CONFIG_FILE_PATHS)
def test_load_config(tmpdir: py.path.local, rel_path: Path) -> None:
    """Test that config is loaded."""
    expected_config = {"dummy": True}
    config_text = "dummy=true"

    mock_write = Mock()

    with tmpdir.as_cwd(), patch("griffe2md._internal.cli.write_package_docs", mock_write):
        text = f"[tool.griffe2md]\n{config_text}" if rel_path.name == "pyproject.toml" else config_text
        config_path = Path(tmpdir) / rel_path
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text(text, "utf-8")

        griffe2md.main(["griffe2md"])

    mock_write.assert_called_once_with("griffe2md", expected_config, None)
