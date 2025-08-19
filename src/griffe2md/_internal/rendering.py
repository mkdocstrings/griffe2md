from __future__ import annotations

import enum
import logging
import random
import re
import string
import sys
from functools import lru_cache, partial
from re import Pattern
from typing import TYPE_CHECKING, Any, Callable

from griffe import (
    AliasResolutionError,
    CyclicAliasError,
    DocstringAttribute,
    DocstringClass,
    DocstringFunction,
    DocstringModule,
    DocstringSectionAttributes,
    DocstringSectionClasses,
    DocstringSectionFunctions,
    DocstringSectionModules,
)
from jinja2 import pass_context

if TYPE_CHECKING:
    from collections.abc import Sequence

    from griffe import Alias, Attribute, Class, Function, Module, Object
    from jinja2.runtime import Context
    from markupsafe import Markup


_logger = logging.getLogger(__name__)


class Order(str, enum.Enum):
    """Enumeration for the possible members ordering."""

    alphabetical = "alphabetical"
    """Alphabetical order."""
    source = "source"
    """Source code order."""


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


def _sort_key_alphabetical(item: Object | Alias) -> Any:
    # chr(sys.maxunicode) is a string that contains the final unicode
    # character, so if 'name' isn't found on the object, the item will go to
    # the end of the list.
    return item.name or chr(sys.maxunicode)


def _sort_key_source(item: Object | Alias) -> Any:
    # if 'lineno' is none, the item will go to the start of the list.
    return item.lineno if item.lineno is not None else -1


order_map = {
    Order.alphabetical.value: _sort_key_alphabetical,
    Order.source.value: _sort_key_source,
}
"""Order mapping for sorting objects."""


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


_stash_key_alphabet = string.ascii_letters + string.digits


def _gen_key(length: int) -> str:
    return "_" + "".join(random.choice(_stash_key_alphabet) for _ in range(max(1, length - 1)))  # noqa: S311


def _gen_stash_key(stash: dict[str, str], length: int) -> str:
    key = _gen_key(length)
    while key in stash:
        key = _gen_key(length)
    return key


def _stash_crossref(stash: dict[str, str], crossref: str, *, length: int) -> str:
    key = _gen_stash_key(stash, length)
    stash[key] = crossref
    return key


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
    annotations: bool | None = None,
    crossrefs: bool = False,
) -> str:
    """Format a signature using Black.

    Parameters:
        context: Jinja context, passed automatically.
        callable_path: The path of the callable we render the signature of.
        function: The function we render the signature of.
        line_length: The line length to give to Black.
        annotations: Whether to show type annotations.
        crossrefs: Whether to cross-reference types in the signature.

    Returns:
        The same code, formatted.
    """
    env = context.environment
    template = env.get_template("signature.md.jinja")
    config_annotations = context.parent["config"]["show_signature_annotations"]
    old_stash_ref_filter = env.filters["stash_crossref"]

    stash: dict[str, str] = {}
    if (annotations or config_annotations) and crossrefs:
        env.filters["stash_crossref"] = partial(_stash_crossref, stash)

    if annotations is None:
        new_context = context.parent
    else:
        new_context = dict(context.parent)
        new_context["config"] = dict(new_context["config"])
        new_context["config"]["show_signature_annotations"] = annotations
    try:
        signature = template.render(new_context, function=function, signature=True)
    finally:
        env.filters["stash_crossref"] = old_stash_ref_filter

    signature = _format_signature(callable_path, signature, line_length)

    if stash:
        for key, value in stash.items():
            signature = re.sub(rf"\b{key}\b", value, signature)

    return signature


@pass_context
def do_format_attribute(
    context: Context,
    attribute_path: Markup,
    attribute: Attribute,
    line_length: int,
    *,
    crossrefs: bool = False,
) -> str:
    """Format an attribute using Black.

    Parameters:
        context: Jinja context, passed automatically.
        attribute_path: The path of the callable we render the signature of.
        attribute: The attribute we render the signature of.
        line_length: The line length to give to Black.
        crossrefs: Whether to cross-reference types in the signature.

    Returns:
        The same code, formatted.
    """
    env = context.environment
    template = env.get_template("expression.md.jinja")
    annotations = context.parent["config"]["show_signature_annotations"]
    separate_signature = context.parent["config"]["separate_signature"]
    old_stash_ref_filter = env.filters["stash_crossref"]

    stash: dict[str, str] = {}
    if separate_signature and crossrefs:
        env.filters["stash_crossref"] = partial(_stash_crossref, stash)

    try:
        signature = str(attribute_path).strip()
        if annotations and attribute.annotation:
            annotation = template.render(context.parent, expression=attribute.annotation, signature=True)
            signature += f": {annotation}"
        if attribute.value:
            value = template.render(context.parent, expression=attribute.value, signature=True)
            signature += f" = {value}"
    finally:
        env.filters["stash_crossref"] = old_stash_ref_filter

    signature = do_format_code(signature, line_length)

    if stash:
        for key, value in stash.items():
            signature = re.sub(rf"\b{key}\b", value, signature)

    return signature


def do_order_members(
    members: Sequence[Object | Alias],
    order: Order,
    members_list: bool | list[str] | None,  # noqa: FBT001
) -> Sequence[Object | Alias]:
    """Order members given an ordering method.

    Parameters:
        members: The members to order.
        order: The ordering method.
        members_list: An optional member list (manual ordering).

    Returns:
        The same members, ordered.
    """
    if isinstance(members_list, list) and members_list:
        sorted_members = []
        members_dict = {member.name: member for member in members}
        for name in members_list:
            if name in members_dict:
                sorted_members.append(members_dict[name])
        return sorted_members
    return sorted(members, key=order_map[order])


def do_heading(content: str, heading_level: int) -> str:
    """Render a Markdown heading."""
    return f"\n{'#' * heading_level} {content}\n\n"


def do_split_path(path: str, full_path: str) -> list[tuple[str, str]]:
    """Split object paths for building cross-references.

    Parameters:
        path: The path to split.

    Returns:
        A list of pairs (title, full path).
    """
    if "." not in path:
        return [(path, full_path)]
    pairs = []
    full_path = ""
    for part in path.split("."):
        if full_path:
            full_path += f".{part}"
        else:
            full_path = part
        pairs.append((part, full_path))
    return pairs


def _keep_object(name: str, filters: Sequence[tuple[Pattern, bool]]) -> bool:
    keep = None
    rules = set()
    for regex, exclude in filters:
        rules.add(exclude)
        if regex.search(name):
            keep = not exclude
    if keep is None:
        if rules == {False}:  # noqa: SIM103
            # only included stuff, no match = reject
            return False
        # only excluded stuff, or included and excluded stuff, no match = keep
        return True
    return keep


def do_filter_objects(
    objects_dictionary: dict[str, Object | Alias],
    *,
    filters: Sequence[tuple[Pattern, bool]] | None = None,
    members_list: bool | list[str] | None = None,
    inherited_members: bool | list[str] = False,
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
        inherited_members: Whether to keep inherited members or exclude them.
        keep_no_docstrings: Whether to keep objects with no/empty docstrings (recursive check).

    Returns:
        A list of objects.
    """
    inherited_members_specified = False
    if inherited_members is True:
        # Include all inherited members.
        objects = list(objects_dictionary.values())
    elif inherited_members is False:
        # Include no inherited members.
        objects = [obj for obj in objects_dictionary.values() if not obj.inherited]
    else:
        # Include specific inherited members.
        inherited_members_specified = True
        objects = [
            obj for obj in objects_dictionary.values() if not obj.inherited or obj.name in set(inherited_members)
        ]

    if members_list is True:
        # Return all pre-selected members.
        return objects

    if members_list is False or members_list == []:
        # Return selected inherited members, if any.
        return [obj for obj in objects if obj.inherited]

    if members_list is not None:
        # Return selected members (keeping any pre-selected inherited members).
        return [
            obj for obj in objects if obj.name in set(members_list) or (inherited_members_specified and obj.inherited)
        ]

    # Use filters and docstrings.
    if filters:
        objects = [
            obj for obj in objects if _keep_object(obj.name, filters) or (inherited_members_specified and obj.inherited)
        ]
    if keep_no_docstrings:
        return objects

    return [obj for obj in objects if obj.has_docstrings or (inherited_members_specified and obj.inherited)]


@lru_cache(maxsize=1)
def _get_black_formatter() -> Callable[[str, int], str]:
    try:
        from black import InvalidInput, Mode, format_str  # noqa: PLC0415
    except ModuleNotFoundError:
        _logger.info("Formatting signatures requires Black to be installed.")
        return lambda text, _: text

    def formatter(code: str, line_length: int) -> str:
        mode = Mode(line_length=line_length)
        try:
            return format_str(code, mode=mode)
        except InvalidInput:
            return code

    return formatter


def from_private_package(obj: Object | Alias) -> bool:
    """Tell if an alias points to an object coming from a corresponding private package.

    For example, return true for an alias in package `ast` pointing at an object in package `_ast`.

    Parameters:
        obj: The object (alias) to check.

    Returns:
        True or false.
    """
    if not obj.is_alias:
        return False
    try:
        return obj.target.package.name == f"_{obj.parent.package.name}"  # type: ignore[union-attr]
    except (AliasResolutionError, CyclicAliasError):
        return False


def do_as_attributes_section(
    attributes: Sequence[Attribute],
    *,
    check_public: bool = True,
) -> DocstringSectionAttributes:
    """Build an attributes section from a list of attributes.

    Parameters:
        attributes: The attributes to build the section from.
        check_public: Whether to check if the attribute is public.

    Returns:
        An attributes docstring section.
    """
    return DocstringSectionAttributes(
        [
            DocstringAttribute(
                name=attribute.name,
                description=attribute.docstring.value.split("\n", 1)[0] if attribute.docstring else "",
                annotation=attribute.annotation,
                value=str(attribute.value) if attribute.value else None,
            )
            for attribute in attributes
            if not check_public or attribute.is_public or from_private_package(attribute)
        ],
    )


def do_as_functions_section(functions: Sequence[Function], *, check_public: bool = True) -> DocstringSectionFunctions:
    """Build a functions section from a list of functions.

    Parameters:
        functions: The functions to build the section from.
        check_public: Whether to check if the function is public.

    Returns:
        A functions docstring section.
    """
    return DocstringSectionFunctions(
        [
            DocstringFunction(
                name=function.name,
                description=function.docstring.value.split("\n", 1)[0] if function.docstring else "",
            )
            for function in functions
            if not check_public or function.is_public or from_private_package(function)
        ],
    )


def do_as_classes_section(classes: Sequence[Class], *, check_public: bool = True) -> DocstringSectionClasses:
    """Build a classes section from a list of classes.

    Parameters:
        classes: The classes to build the section from.
        check_public: Whether to check if the class is public.

    Returns:
        A classes docstring section.
    """
    return DocstringSectionClasses(
        [
            DocstringClass(
                name=cls.name,
                description=cls.docstring.value.split("\n", 1)[0] if cls.docstring else "",
            )
            for cls in classes
            if not check_public or cls.is_public or from_private_package(cls)
        ],
    )


def do_as_modules_section(modules: Sequence[Module], *, check_public: bool = True) -> DocstringSectionModules:
    """Build a modules section from a list of modules.

    Parameters:
        modules: The modules to build the section from.
        check_public: Whether to check if the module is public.

    Returns:
        A modules docstring section.
    """
    return DocstringSectionModules(
        [
            DocstringModule(
                name=module.name,
                description=module.docstring.value.split("\n", 1)[0] if module.docstring else "",
            )
            for module in modules
            if not check_public or module.is_public or from_private_package(module)
        ],
    )
