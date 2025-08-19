from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Literal, TypedDict, cast

# YORE: EOL 3.10: Replace block with line 2.
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

if TYPE_CHECKING:
    from re import Pattern

_logger = logging.getLogger(__name__)

CONFIG_FILE_PATHS = (
    Path(".config/griffe2md.toml"),
    Path("config/griffe2md.toml"),
    Path("pyproject.toml"),
)
"""Paths to default configuration files."""


def _locate_config_file() -> Path | None:
    for path in CONFIG_FILE_PATHS:
        if path.is_file():
            return path
    return None


def load_config() -> ConfigDict | None:
    """Load the configuration if config file or config entry in pyproject.toml exists.

    If neither config file was found or pyproject.toml file doesn't have
    a `[tool.griffe2md]` section, None is returned.
    """
    if not (config_path := _locate_config_file()):
        return None

    _logger.debug("Loading config from %s", config_path)

    with config_path.open("rb") as f:
        config = tomllib.load(f)

    if config_path.name == "pyproject.toml":
        return config.get("tool", {}).get("griffe2md", None)
    return cast("ConfigDict", config)


class ConfigDict(TypedDict):
    """Configuration for griffe2md, griffe and mkdocstrings."""

    allow_inspection: bool
    """Allow using introspection on modules for which sources aren't available (compiled modules, etc.)."""

    annotations_path: Literal["brief", "source", "full"]
    """The verbosity for annotations path: `brief` (recommended), `source` (as written in the source), or `full`."""

    docstring_options: dict
    """mkdocstring [configuration](https://mkdocstrings.github.io/python/usage/configuration/general/)"""

    docstring_section_style: Literal["list", "table"]
    """The style used to render docstring sections."""

    docstring_style: Literal["google", "numpy", "sphinx", "auto"] | None
    """The style in which docstrings are written: `auto`, `google`, `numpy`, `sphinx`, or `None`."""

    filters: list[str] | list[tuple[Pattern[str], bool]]
    """A list of filters.

    A filter starting with `!` will exclude matching objects instead of including them.
    The `members` option takes precedence over `filters` (filters will still be applied recursively
    to lower members in the hierarchy).
    """

    group_by_category: bool
    """Group the object's children by categories: attributes, classes, functions, and modules."""

    heading_level: int
    """The initial heading level to use."""

    inherited_members: bool | list[str]
    """A boolean, or an explicit list of inherited members to render.

    If true, select all inherited members, which can then be filtered with `members`.
    If false or empty list, do not select any inherited member.
    """

    line_length: int
    """Maximum line length when formatting code/signatures."""

    load_external_modules: bool
    """Whether to always load external modules/packages."""

    members: list[str] | bool | None
    """A boolean, or an explicit list of members to render.

    If true, select all members without further filtering.
    If false or empty list, do not render members.
    If none, select all members and apply further filtering with filters and docstrings.
    """

    members_order: Literal["alphabetical", "source"]
    """The members ordering to use.

    - `alphabetical`: order members alphabetically;
    - `source`: order members as they appear in the source file.
    """

    merge_init_into_class: bool
    """Whether to merge the `__init__` method into the class' signature and docstring."""

    preload_modules: list[str] | None
    """Pre-load modules that are not specified directly in autodoc instructions (`::: identifier`).

    It is useful when you want to render documentation for a particular member of an object,
    and this member is imported from another package than its parent.

    For an imported member to be rendered, you need to add it to the `__all__` attribute
    of the importing module.

    The modules must be listed as an array of strings.
    """

    separate_signature: bool
    """Whether to put the whole signature in a code block below the heading.

    If Black or Ruff are installed, the signature is also formatted using them.
    """

    show_bases: bool
    """Show the base classes of a class."""

    show_category_heading: bool
    """When grouped by categories, show a heading for each category."""

    show_docstring_attributes: bool
    """Whether to display the 'Attributes' section in the object's docstring."""

    show_docstring_classes: bool
    """Whether to display the 'Classes' section in the object's docstring."""

    show_docstring_description: bool
    """Whether to display the textual block (including admonitions) in the object's docstring."""

    show_docstring_examples: bool
    """Whether to display the 'Examples' section in the object's docstring."""

    show_docstring_functions: bool
    """Whether to display the 'Functions' section in the object's docstring."""

    show_docstring_modules: bool
    """Whether to display the 'Modules' section in the object's docstring."""

    show_docstring_other_parameters: bool
    """Whether to display the 'Other Parameters' section in the object's docstring."""

    show_docstring_parameters: bool
    """Whether to display the 'Parameters' section in the object's docstring."""

    show_docstring_raises: bool
    """Whether to display the 'Raises' section in the object's docstring."""

    show_docstring_receives: bool
    """Whether to display the 'Receives' section in the object's docstring."""

    show_docstring_returns: bool
    """Whether to display the 'Returns' section in the object's docstring."""

    show_docstring_warns: bool
    """Whether to display the 'Warns' section in the object's docstring."""

    show_docstring_yields: bool
    """Whether to display the 'Yields' section in the object's docstring."""

    show_if_no_docstring: bool
    """Show the object heading even if it has no docstring or children with docstrings."""

    show_object_full_path: bool
    """Show the full Python path of every object."""

    show_root_full_path: bool
    """Show the full Python path for the root object heading."""

    show_root_heading: bool
    """Show the heading of the object at the root of the documentation tree.

    The root object is the object referenced by the identifier after `:::`.
    """

    show_root_members_full_path: bool
    """Show the full Python path of the root members."""

    show_signature: bool
    """Show methods and functions signatures."""

    show_signature_annotations: bool
    """Show the type annotations in methods and functions signatures."""

    show_submodules: bool
    """When rendering a module, show its submodules recursively."""

    signature_crossrefs: bool
    """Whether to render cross-references for type annotations in signatures."""

    summary: bool | dict
    """Whether to render summaries of modules, classes, functions (methods) and attributes."""


default_config: ConfigDict = {
    "docstring_style": "google",
    "docstring_options": {"ignore_init_summary": True},
    "show_root_heading": True,
    "show_root_full_path": True,
    "show_root_members_full_path": True,
    "show_object_full_path": True,
    "show_category_heading": False,
    "show_if_no_docstring": True,
    "show_signature": True,
    "show_signature_annotations": False,
    "signature_crossrefs": False,
    "separate_signature": True,
    "line_length": 80,
    "merge_init_into_class": True,
    "show_docstring_attributes": True,
    "show_docstring_description": True,
    "show_docstring_examples": True,
    "show_docstring_other_parameters": True,
    "show_docstring_parameters": True,
    "show_docstring_raises": True,
    "show_docstring_receives": True,
    "show_docstring_returns": True,
    "show_docstring_warns": True,
    "show_docstring_yields": True,
    "show_bases": True,
    "show_submodules": True,
    "group_by_category": False,
    "heading_level": 2,
    "members_order": "alphabetical",
    "docstring_section_style": "list",
    "members": None,
    "inherited_members": True,
    "filters": ["!^_"],
    "annotations_path": "brief",
    "preload_modules": None,
    "load_external_modules": False,
    "allow_inspection": True,
    "summary": True,
    "show_docstring_classes": True,
    "show_docstring_functions": True,
    "show_docstring_modules": True,
}
"""Default configuration values."""
