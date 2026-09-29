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

"""griffe2md package.

Output API docs to Markdown using Griffe.
"""

from __future__ import annotations

from griffe2md._internal.cli import get_parser, main
from griffe2md._internal.config import CONFIG_FILE_PATHS, ConfigDict, default_config, load_config
from griffe2md._internal.main import (
    prepare_context,
    prepare_env,
    render_object_docs,
    render_package_docs,
    write_package_docs,
)
from griffe2md._internal.rendering import (
    Order,
    do_any,
    do_as_attributes_section,
    do_as_classes_section,
    do_as_functions_section,
    do_as_modules_section,
    do_filter_objects,
    do_format_attribute,
    do_format_code,
    do_format_signature,
    do_heading,
    do_order_members,
    do_split_path,
    from_private_package,
    order_map,
)

__all__: list[str] = [
    "CONFIG_FILE_PATHS",
    "ConfigDict",
    "Order",
    "default_config",
    "do_any",
    "do_as_attributes_section",
    "do_as_classes_section",
    "do_as_functions_section",
    "do_as_modules_section",
    "do_filter_objects",
    "do_format_attribute",
    "do_format_code",
    "do_format_signature",
    "do_heading",
    "do_order_members",
    "do_split_path",
    "from_private_package",
    "get_parser",
    "load_config",
    "main",
    "order_map",
    "prepare_context",
    "prepare_env",
    "render_object_docs",
    "render_package_docs",
    "write_package_docs",
]
