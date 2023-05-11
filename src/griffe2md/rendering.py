"""Rendering utilites (Jinja filters, etc.)."""

from __future__ import annotations

import enum
import sys
from functools import lru_cache
from typing import TYPE_CHECKING, Callable, Pattern, Sequence

from jinja2 import pass_context

if TYPE_CHECKING:
    from griffe.dataclasses import Alias, Function, Object
    from jinja2.environment import Context
    from markupsafe import Markup


class Order(enum.Enum):
    """Enumeration for the possible members ordering."""

    alphabetical = "alphabetical"
    source = "source"


default_config: dict = {
    "docstring_style": "google",
    "docstring_options": {"ignore_init_summary": True},
    "show_root_heading": True,
    "show_root_full_path": True,
    "show_root_members_full_path": True,
    "show_object_full_path": True,
    "show_category_heading": False,
    "show_if_no_docstring": False,
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
    "group_by_category": True,
    "heading_level": 2,
    "members_order": Order.alphabetical.value,
    "docstring_section_style": "list",
    "members": None,
    "filters": ["!^_"],
    "annotations_path": "brief",
    "preload_modules": None,
    "load_external_modules": False,
    "allow_inspection": True,
}


def _sort_key_alphabetical(item: Object | Alias) -> str:
    # chr(sys.maxunicode) is a string that contains the final unicode
    # character, so if 'name' isn't found on the object, the item will go to
    # the end of the list.
    return item.name or chr(sys.maxunicode)


def _sort_key_source(item: Object | Alias) -> int:
    # if 'lineno' is none, the item will go to the start of the list.
    return item.lineno if item.lineno is not None else -1


order_map = {
    Order.alphabetical.value: _sort_key_alphabetical,
    Order.source.value: _sort_key_source,
}


@lru_cache(maxsize=1)
def _get_black_formatter() -> Callable[[str, int], str]:
    try:
        from black import InvalidInput, Mode, format_str
    except ModuleNotFoundError:
        return lambda text, _: text

    def formatter(code: str, line_length: int) -> str:
        mode = Mode(line_length=line_length)
        try:
            return format_str(code, mode=mode)
        except InvalidInput:
            return code

    return formatter


def do_any(seq: Sequence, attribute: str | None = None) -> bool:
    """Check if at least one of the item in the sequence evaluates to true.

    The `any` builtin as a filter for Jinja templates.

    Arguments:
        seq: An iterable object.
        attribute: The attribute name to use on each object of the iterable.

    Returns:
        A boolean telling if any object of the iterable evaluated to True.
    """
    if attribute is None:
        return any(seq)
    return any(_[attribute] for _ in seq)


def do_format_code(code: str, line_length: int) -> str:
    """Format code using Black.

    Parameters:
        code: The code to format.
        line_length: The line length to give to Black.

    Returns:
        The same code, formatted.
    """
    code = code.strip()
    if len(code) < line_length:
        return code
    formatter = _get_black_formatter()
    return formatter(code, line_length)


def _format_signature(name: Markup, signature: str, line_length: int) -> str:
    name = str(name).strip()  # type: ignore[assignment]
    signature = signature.strip()
    if len(name + signature) < line_length:
        return name + signature

    # Black cannot format names with dots, so we replace
    # the whole name with a string of equal length
    name_length = len(name)
    formatter = _get_black_formatter()
    formatable = f"def {'x' * name_length}{signature}: pass"
    formatted = formatter(formatable, line_length)

    # We put back the original name
    # and remove starting `def ` and trailing `: pass`
    return name + formatted[4:-5].strip()[name_length:-1]


@pass_context
def do_format_signature(
    context: Context,
    callable_path: Markup,
    function: Function,
    line_length: int,
    *,
    crossrefs: bool = False,  # noqa: ARG001
) -> str:
    """Format a signature using Black.

    Parameters:
        callable_path: The path of the callable we render the signature of.
        line_length: The line length to give to Black.
        crossrefs: Whether to cross-reference types in the signature.

    Returns:
        The same code, formatted.
    """
    env = context.environment
    template = env.get_template("signature.md")
    signature = template.render(context.parent, function=function)
    signature = _format_signature(callable_path, signature, line_length)
    return signature


def do_filter_objects(
    objects_dictionary: dict[str, Object | Alias],
    *,
    filters: Sequence[tuple[Pattern, bool]] | None = None,
    members_list: list[str] | None = None,
    keep_no_docstrings: bool = True,
) -> list[Object | Alias]:
    """Filter a dictionary of objects based on their docstrings.

    Parameters:
        objects_dictionary: The dictionary of objects.
        filters: Filters to apply, based on members' names.
            Each element is a tuple: a pattern, and a boolean indicating whether
            to reject the object if the pattern matches.
        members_list: An optional, explicit list of members to keep.
            When given and empty, return an empty list.
            When given and not empty, ignore filters and docstrings presence/absence.
        keep_no_docstrings: Whether to keep objects with no/empty docstrings (recursive check).

    Returns:
        A list of objects.
    """
    # no members
    if members_list is False or members_list == []:
        return []

    objects = list(objects_dictionary.values())

    # all members
    if members_list is True:
        return objects

    # list of members
    if members_list is not None:
        return [obj for obj in objects if obj.name in set(members_list)]

    # none, use filters and docstrings
    if filters:
        objects = [obj for obj in objects if _keep_object(obj.name, filters)]
    if keep_no_docstrings:
        return objects
    return [obj for obj in objects if obj.has_docstrings]


def do_heading(content: str, heading_level: int) -> str:
    """Render a Markdown heading."""
    return f"\n{'#' * heading_level} {content}\n\n"


def _keep_object(name: str, filters: Sequence[tuple[Pattern, bool]]) -> bool:
    keep = None
    rules = set()
    for regex, exclude in filters:
        rules.add(exclude)
        if regex.search(name):
            keep = not exclude
    if keep is None:
        if rules == {False}:
            # only included stuff, no match = reject
            return False
        # only excluded stuff, or included and excluded stuff, no match = keep
        return True
    return keep


def do_order_members(
    members: Sequence[Object | Alias],
    order: str,
    members_list: list[str] | None,
) -> Sequence[Object | Alias]:
    """Order members given an ordering method.

    Parameters:
        members: The members to order.
        order: The ordering method.
        members_list: An optional member list (manual ordering).

    Returns:
        The same members, ordered.
    """
    if members_list:
        sorted_members = []
        members_dict = {member.name: member for member in members}
        for name in members_list:
            if name in members_dict:
                sorted_members.append(members_dict[name])
        return sorted_members
    return sorted(members, key=order_map[order])  # type: ignore[arg-type]
