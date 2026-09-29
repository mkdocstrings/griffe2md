# SPDX-License-Identifier: ISC
#
# ISC License
#
# Copyright (c) 2023, Timothée Mazzucotelli and contributors
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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

    mock_write.assert_called_once_with("griffe2md", expected_config, None, format_md=False)
