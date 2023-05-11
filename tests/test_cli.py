"""Tests for the `cli` module."""

from __future__ import annotations

import pytest

from griffe2md import cli


def test_main() -> None:
    """Basic CLI test."""
    with pytest.raises(expected_exception=SystemExit):
        cli.main([])


def test_show_help(capsys: pytest.CaptureFixture) -> None:
    """Show help.

    Parameters:
        capsys: Pytest fixture to capture output.
    """
    with pytest.raises(SystemExit):
        cli.main(["-h"])
    captured = capsys.readouterr()
    assert "griffe2md" in captured.out


def test_render_self() -> None:
    """Render docs for itself."""
    cli.main(["griffe2md", "-o/dev/null"])
