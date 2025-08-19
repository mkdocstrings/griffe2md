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
