"""Test config loading."""

from pathlib import Path
from unittest.mock import Mock, patch

import pytest

import griffe2md.cli
from griffe2md.config import PYPROJECT


@pytest.mark.parametrize(
    "rel_path",
    [
        ".config/griffe2md.toml",
        "config/griffe2md.toml",
        "pyproject.toml",
    ],
)
def test_load_config(tmpdir, rel_path: str) -> None:  # noqa: ANN001
    """Test that config is loaded."""
    expected_config = {"dummy": True}
    config_text = "dummy=true"

    mock_write = Mock()

    with tmpdir.as_cwd(), patch("griffe2md.cli.write_package_docs", mock_write):
        text = f"[tool.griffe2md]\n{config_text}" if rel_path == PYPROJECT else config_text
        config_path = Path(tmpdir) / rel_path
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text(text, "utf-8")

        griffe2md.cli.main(["griffe2md", "-o/dev/null"])

    mock_write.assert_called_once_with("griffe2md", expected_config, "/dev/null")
