# griffe2md

griffe2md package.

Output API docs to Markdown using Griffe.

Modules:

- **`cli`** – Deprecated. Import from griffe2md directly.
- **`main`** – Deprecated. Import from griffe2md directly.
- **`rendering`** – Deprecated. Import from griffe2md directly.

Classes:

- **`ConfigDict`** – Configuration for griffe2md, griffe and mkdocstrings.
- **`Order`** – Enumeration for the possible members ordering.

Functions:

- **`do_any`** – Check if at least one of the item in the sequence evaluates to true.
- **`do_as_attributes_section`** – Build an attributes section from a list of attributes.
- **`do_as_classes_section`** – Build a classes section from a list of classes.
- **`do_as_functions_section`** – Build a functions section from a list of functions.
- **`do_as_modules_section`** – Build a modules section from a list of modules.
- **`do_filter_objects`** – Filter a dictionary of objects based on their docstrings.
- **`do_format_attribute`** – Format an attribute using Black.
- **`do_format_code`** – Format code using Black.
- **`do_format_signature`** – Format a signature using Black.
- **`do_heading`** – Render a Markdown heading.
- **`do_order_members`** – Order members given an ordering method.
- **`do_split_path`** – Split object paths for building cross-references.
- **`from_private_package`** – Tell if an alias points to an object coming from a corresponding private package.
- **`get_parser`** – Return the CLI argument parser.
- **`load_config`** – Load the configuration if config file or config entry in pyproject.toml exists.
- **`prepare_context`** – Prepare Jinja context.
- **`prepare_env`** – Prepare Jinja environment.
- **`render_object_docs`** – Render docs for a given object.
- **`render_package_docs`** – Render docs for a given package.
- **`write_package_docs`** – Write docs for a given package to a file or stdout.

Attributes:

- **`CONFIG_FILE_PATHS`** – Paths to default configuration files.
- **`default_config`** (`ConfigDict`) – Default configuration values.
- **`order_map`** – Order mapping for sorting objects.

## CONFIG_FILE_PATHS

```
CONFIG_FILE_PATHS = (
    Path(".config/griffe2md.toml"),
    Path("config/griffe2md.toml"),
    Path("pyproject.toml"),
)
```

Paths to default configuration files.

## default_config

```
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
    "force_inspection": False,
    "summary": True,
    "show_docstring_classes": True,
    "show_docstring_functions": True,
    "show_docstring_modules": True,
    "extensions": [],
    "search_paths": [],
}
```

Default configuration values.

## order_map

```
order_map = {
    alphabetical.value: _sort_key_alphabetical,
    source.value: _sort_key_source,
}
```

Order mapping for sorting objects.

## ConfigDict

Bases: `TypedDict`

Configuration for griffe2md, griffe and mkdocstrings.

Attributes:

- **`allow_inspection`** (`bool`) – Allow using introspection on modules for which sources aren't available (compiled modules, etc.).
- **`annotations_path`** (`Literal['brief', 'source', 'full']`) – The verbosity for annotations path: brief (recommended), source (as written in the source), or full.
- **`docstring_options`** (`DocstringOptions`) – mkdocstring configuration
- **`docstring_section_style`** (`Literal['list', 'table']`) – The style used to render docstring sections.
- **`docstring_style`** (`Literal['google', 'numpy', 'sphinx', 'auto'] | None`) – The style in which docstrings are written: auto, google, numpy, sphinx, or None.
- **`extensions`** (`list[LoadableExtensionType]`) – A list of Griffe extensions to load.
- **`filters`** (`list[str] | list[tuple[Pattern[str], bool]]`) – A list of filters.
- **`force_inspection`** (`bool`) – Force using introspection on modules even if sources are available.
- **`group_by_category`** (`bool`) – Group the object's children by categories: attributes, classes, functions, and modules.
- **`heading_level`** (`int`) – The initial heading level to use.
- **`inherited_members`** (`bool | list[str]`) – A boolean, or an explicit list of inherited members to render.
- **`line_length`** (`int`) – Maximum line length when formatting code/signatures.
- **`load_external_modules`** (`bool`) – Whether to always load external modules/packages.
- **`members`** (`list[str] | bool | None`) – A boolean, or an explicit list of members to render.
- **`members_order`** (`Literal['alphabetical', 'source']`) – The members ordering to use.
- **`merge_init_into_class`** (`bool`) – Whether to merge the __init__ method into the class' signature and docstring.
- **`preload_modules`** (`list[str] | None`) – Pre-load modules that are not specified directly in autodoc instructions (::: identifier).
- **`search_paths`** (`list[str]`) – A list of paths to search packages into.
- **`separate_signature`** (`bool`) – Whether to put the whole signature in a code block below the heading.
- **`show_bases`** (`bool`) – Show the base classes of a class.
- **`show_category_heading`** (`bool`) – When grouped by categories, show a heading for each category.
- **`show_docstring_attributes`** (`bool`) – Whether to display the 'Attributes' section in the object's docstring.
- **`show_docstring_classes`** (`bool`) – Whether to display the 'Classes' section in the object's docstring.
- **`show_docstring_description`** (`bool`) – Whether to display the textual block (including admonitions) in the object's docstring.
- **`show_docstring_examples`** (`bool`) – Whether to display the 'Examples' section in the object's docstring.
- **`show_docstring_functions`** (`bool`) – Whether to display the 'Functions' section in the object's docstring.
- **`show_docstring_modules`** (`bool`) – Whether to display the 'Modules' section in the object's docstring.
- **`show_docstring_other_parameters`** (`bool`) – Whether to display the 'Other Parameters' section in the object's docstring.
- **`show_docstring_parameters`** (`bool`) – Whether to display the 'Parameters' section in the object's docstring.
- **`show_docstring_raises`** (`bool`) – Whether to display the 'Raises' section in the object's docstring.
- **`show_docstring_receives`** (`bool`) – Whether to display the 'Receives' section in the object's docstring.
- **`show_docstring_returns`** (`bool`) – Whether to display the 'Returns' section in the object's docstring.
- **`show_docstring_warns`** (`bool`) – Whether to display the 'Warns' section in the object's docstring.
- **`show_docstring_yields`** (`bool`) – Whether to display the 'Yields' section in the object's docstring.
- **`show_if_no_docstring`** (`bool`) – Show the object heading even if it has no docstring or children with docstrings.
- **`show_object_full_path`** (`bool`) – Show the full Python path of every object.
- **`show_root_full_path`** (`bool`) – Show the full Python path for the root object heading.
- **`show_root_heading`** (`bool`) – Show the heading of the object at the root of the documentation tree.
- **`show_root_members_full_path`** (`bool`) – Show the full Python path of the root members.
- **`show_signature`** (`bool`) – Show methods and functions signatures.
- **`show_signature_annotations`** (`bool`) – Show the type annotations in methods and functions signatures.
- **`show_submodules`** (`bool`) – When rendering a module, show its submodules recursively.
- **`signature_crossrefs`** (`bool`) – Whether to render cross-references for type annotations in signatures.
- **`summary`** (`bool | dict`) – Whether to render summaries of modules, classes, functions (methods) and attributes.

### allow_inspection

```
allow_inspection: bool
```

Allow using introspection on modules for which sources aren't available (compiled modules, etc.).

### annotations_path

```
annotations_path: Literal['brief', 'source', 'full']
```

The verbosity for annotations path: `brief` (recommended), `source` (as written in the source), or `full`.

### docstring_options

```
docstring_options: DocstringOptions
```

mkdocstring [configuration](https://mkdocstrings.github.io/python/usage/configuration/general/)

### docstring_section_style

```
docstring_section_style: Literal['list', 'table']
```

The style used to render docstring sections.

### docstring_style

```
docstring_style: (
    Literal["google", "numpy", "sphinx", "auto"] | None
)
```

The style in which docstrings are written: `auto`, `google`, `numpy`, `sphinx`, or `None`.

### extensions

```
extensions: list[LoadableExtensionType]
```

A list of Griffe extensions to load.

### filters

```
filters: list[str] | list[tuple[Pattern[str], bool]]
```

A list of filters.

A filter starting with `!` will exclude matching objects instead of including them. The `members` option takes precedence over `filters` (filters will still be applied recursively to lower members in the hierarchy).

### force_inspection

```
force_inspection: bool
```

Force using introspection on modules even if sources are available.

### group_by_category

```
group_by_category: bool
```

Group the object's children by categories: attributes, classes, functions, and modules.

### heading_level

```
heading_level: int
```

The initial heading level to use.

### inherited_members

```
inherited_members: bool | list[str]
```

A boolean, or an explicit list of inherited members to render.

If true, select all inherited members, which can then be filtered with `members`. If false or empty list, do not select any inherited member.

### line_length

```
line_length: int
```

Maximum line length when formatting code/signatures.

### load_external_modules

```
load_external_modules: bool
```

Whether to always load external modules/packages.

### members

```
members: list[str] | bool | None
```

A boolean, or an explicit list of members to render.

If true, select all members without further filtering. If false or empty list, do not render members. If none, select all members and apply further filtering with filters and docstrings.

### members_order

```
members_order: Literal['alphabetical', 'source']
```

The members ordering to use.

- `alphabetical`: order members alphabetically;
- `source`: order members as they appear in the source file.

### merge_init_into_class

```
merge_init_into_class: bool
```

Whether to merge the `__init__` method into the class' signature and docstring.

### preload_modules

```
preload_modules: list[str] | None
```

Pre-load modules that are not specified directly in autodoc instructions (`::: identifier`).

It is useful when you want to render documentation for a particular member of an object, and this member is imported from another package than its parent.

For an imported member to be rendered, you need to add it to the `__all__` attribute of the importing module.

The modules must be listed as an array of strings.

### search_paths

```
search_paths: list[str]
```

A list of paths to search packages into.

### separate_signature

```
separate_signature: bool
```

Whether to put the whole signature in a code block below the heading.

If Black or Ruff are installed, the signature is also formatted using them.

### show_bases

```
show_bases: bool
```

Show the base classes of a class.

### show_category_heading

```
show_category_heading: bool
```

When grouped by categories, show a heading for each category.

### show_docstring_attributes

```
show_docstring_attributes: bool
```

Whether to display the 'Attributes' section in the object's docstring.

### show_docstring_classes

```
show_docstring_classes: bool
```

Whether to display the 'Classes' section in the object's docstring.

### show_docstring_description

```
show_docstring_description: bool
```

Whether to display the textual block (including admonitions) in the object's docstring.

### show_docstring_examples

```
show_docstring_examples: bool
```

Whether to display the 'Examples' section in the object's docstring.

### show_docstring_functions

```
show_docstring_functions: bool
```

Whether to display the 'Functions' section in the object's docstring.

### show_docstring_modules

```
show_docstring_modules: bool
```

Whether to display the 'Modules' section in the object's docstring.

### show_docstring_other_parameters

```
show_docstring_other_parameters: bool
```

Whether to display the 'Other Parameters' section in the object's docstring.

### show_docstring_parameters

```
show_docstring_parameters: bool
```

Whether to display the 'Parameters' section in the object's docstring.

### show_docstring_raises

```
show_docstring_raises: bool
```

Whether to display the 'Raises' section in the object's docstring.

### show_docstring_receives

```
show_docstring_receives: bool
```

Whether to display the 'Receives' section in the object's docstring.

### show_docstring_returns

```
show_docstring_returns: bool
```

Whether to display the 'Returns' section in the object's docstring.

### show_docstring_warns

```
show_docstring_warns: bool
```

Whether to display the 'Warns' section in the object's docstring.

### show_docstring_yields

```
show_docstring_yields: bool
```

Whether to display the 'Yields' section in the object's docstring.

### show_if_no_docstring

```
show_if_no_docstring: bool
```

Show the object heading even if it has no docstring or children with docstrings.

### show_object_full_path

```
show_object_full_path: bool
```

Show the full Python path of every object.

### show_root_full_path

```
show_root_full_path: bool
```

Show the full Python path for the root object heading.

### show_root_heading

```
show_root_heading: bool
```

Show the heading of the object at the root of the documentation tree.

The root object is the object referenced by the identifier after `:::`.

### show_root_members_full_path

```
show_root_members_full_path: bool
```

Show the full Python path of the root members.

### show_signature

```
show_signature: bool
```

Show methods and functions signatures.

### show_signature_annotations

```
show_signature_annotations: bool
```

Show the type annotations in methods and functions signatures.

### show_submodules

```
show_submodules: bool
```

When rendering a module, show its submodules recursively.

### signature_crossrefs

```
signature_crossrefs: bool
```

Whether to render cross-references for type annotations in signatures.

### summary

```
summary: bool | dict
```

Whether to render summaries of modules, classes, functions (methods) and attributes.

## Order

Bases: `str`, `Enum`

Enumeration for the possible members ordering.

Attributes:

- **`alphabetical`** – Alphabetical order.
- **`source`** – Source code order.

### alphabetical

```
alphabetical = 'alphabetical'
```

Alphabetical order.

### source

```
source = 'source'
```

Source code order.

## do_any

```
do_any(seq: Sequence, attribute: str | None = None) -> bool
```

Check if at least one of the item in the sequence evaluates to true.

The `any` builtin as a filter for Jinja templates.

Parameters:

- **`seq`** (`Sequence`) – An iterable object.
- **`attribute`** (`str | None`, default: `None` ) – The attribute name to use on each object of the iterable.

Returns:

- `bool` – A boolean telling if any object of the iterable evaluated to True.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_as_attributes_section

```
do_as_attributes_section(
    attributes: Sequence[Attribute],
    *,
    check_public: bool = True,
) -> DocstringSectionAttributes
```

Build an attributes section from a list of attributes.

Parameters:

- **`attributes`** (`Sequence[Attribute]`) – The attributes to build the section from.
- **`check_public`** (`bool`, default: `True` ) – Whether to check if the attribute is public.

Returns:

- `DocstringSectionAttributes` – An attributes docstring section.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_as_classes_section

```
do_as_classes_section(
    classes: Sequence[Class], *, check_public: bool = True
) -> DocstringSectionClasses
```

Build a classes section from a list of classes.

Parameters:

- **`classes`** (`Sequence[Class]`) – The classes to build the section from.
- **`check_public`** (`bool`, default: `True` ) – Whether to check if the class is public.

Returns:

- `DocstringSectionClasses` – A classes docstring section.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_as_functions_section

```
do_as_functions_section(
    functions: Sequence[Function],
    *,
    check_public: bool = True,
) -> DocstringSectionFunctions
```

Build a functions section from a list of functions.

Parameters:

- **`functions`** (`Sequence[Function]`) – The functions to build the section from.
- **`check_public`** (`bool`, default: `True` ) – Whether to check if the function is public.

Returns:

- `DocstringSectionFunctions` – A functions docstring section.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_as_modules_section

```
do_as_modules_section(
    modules: Sequence[Module], *, check_public: bool = True
) -> DocstringSectionModules
```

Build a modules section from a list of modules.

Parameters:

- **`modules`** (`Sequence[Module]`) – The modules to build the section from.
- **`check_public`** (`bool`, default: `True` ) – Whether to check if the module is public.

Returns:

- `DocstringSectionModules` – A modules docstring section.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_filter_objects

```
do_filter_objects(
    objects_dictionary: dict[str, Object | Alias],
    *,
    filters: Sequence[tuple[Pattern, bool]] | None = None,
    members_list: bool | list[str] | None = None,
    inherited_members: bool | list[str] = False,
    keep_no_docstrings: bool = True,
) -> list[Object | Alias]
```

Filter a dictionary of objects based on their docstrings.

Parameters:

- **`objects_dictionary`** (`dict[str, Object | Alias]`) – The dictionary of objects.
- **`filters`** (`Sequence[tuple[Pattern, bool]] | None`, default: `None` ) – Filters to apply, based on members' names. Each element is a tuple: a pattern, and a boolean indicating whether to reject the object if the pattern matches.
- **`members_list`** (`bool | list[str] | None`, default: `None` ) – An optional, explicit list of members to keep. When given and empty, return an empty list. When given and not empty, ignore filters and docstrings presence/absence.
- **`inherited_members`** (`bool | list[str]`, default: `False` ) – Whether to keep inherited members or exclude them.
- **`keep_no_docstrings`** (`bool`, default: `True` ) – Whether to keep objects with no/empty docstrings (recursive check).

Returns:

- `list[Object | Alias]` – A list of objects.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_format_attribute

```
do_format_attribute(
    context: Context,
    attribute_path: Markup,
    attribute: Attribute,
    line_length: int,
    *,
    crossrefs: bool = False,
) -> str
```

Format an attribute using Black.

Parameters:

- **`context`** (`Context`) – Jinja context, passed automatically.
- **`attribute_path`** (`Markup`) – The path of the callable we render the signature of.
- **`attribute`** (`Attribute`) – The attribute we render the signature of.
- **`line_length`** (`int`) – The line length to give to Black.
- **`crossrefs`** (`bool`, default: `False` ) – Whether to cross-reference types in the signature.

Returns:

- `str` – The same code, formatted.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_format_code

```
do_format_code(code: str, line_length: int) -> str
```

Format code using Black.

Parameters:

- **`code`** (`str`) – The code to format.
- **`line_length`** (`int`) – The line length to give to Black.

Returns:

- `str` – The same code, formatted.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_format_signature

```
do_format_signature(
    context: Context,
    callable_path: Markup,
    function: Function,
    line_length: int,
    *,
    annotations: bool | None = None,
    crossrefs: bool = False,
) -> str
```

Format a signature using Black.

Parameters:

- **`context`** (`Context`) – Jinja context, passed automatically.
- **`callable_path`** (`Markup`) – The path of the callable we render the signature of.
- **`function`** (`Function`) – The function we render the signature of.
- **`line_length`** (`int`) – The line length to give to Black.
- **`annotations`** (`bool | None`, default: `None` ) – Whether to show type annotations.
- **`crossrefs`** (`bool`, default: `False` ) – Whether to cross-reference types in the signature.

Returns:

- `str` – The same code, formatted.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_heading

```
do_heading(content: str, heading_level: int) -> str
```

Render a Markdown heading.

Source code in `src/griffe2md/_internal/rendering.py`

```
def do_heading(content: str, heading_level: int) -> str:
    """Render a Markdown heading."""
    return f"\n{'#' * heading_level} {content}\n\n"
```

## do_order_members

```
do_order_members(
    members: Sequence[Object | Alias],
    order: Order,
    members_list: bool | list[str] | None,
) -> Sequence[Object | Alias]
```

Order members given an ordering method.

Parameters:

- **`members`** (`Sequence[Object | Alias]`) – The members to order.
- **`order`** (`Order`) – The ordering method.
- **`members_list`** (`bool | list[str] | None`) – An optional member list (manual ordering).

Returns:

- `Sequence[Object | Alias]` – The same members, ordered.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## do_split_path

```
do_split_path(
    path: str, full_path: str
) -> list[tuple[str, str]]
```

Split object paths for building cross-references.

Parameters:

- **`path`** (`str`) – The path to split.

Returns:

- `list[tuple[str, str]]` – A list of pairs (title, full path).

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## from_private_package

```
from_private_package(obj: Object | Alias) -> bool
```

Tell if an alias points to an object coming from a corresponding private package.

For example, return true for an alias in package `ast` pointing at an object in package `_ast`.

Parameters:

- **`obj`** (`Object | Alias`) – The object (alias) to check.

Returns:

- `bool` – True or false.

Source code in `src/griffe2md/_internal/rendering.py`

```
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
```

## get_parser

```
get_parser() -> ArgumentParser
```

Return the CLI argument parser.

Returns:

- `ArgumentParser` – An argparse parser.

Source code in `src/griffe2md/_internal/cli.py`

```
def get_parser() -> argparse.ArgumentParser:
    """Return the CLI argument parser.

    Returns:
        An argparse parser.
    """
    parser = argparse.ArgumentParser(prog="griffe2md")
    parser.add_argument("package", help="The package to output Markdown docs for.")
    parser.add_argument("-o", "--output", default=None, help="File to write to. Default: stdout.")
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {debug._get_version()}")
    parser.add_argument("--debug-info", action=_DebugInfo, help="Print debug information.")
    return parser
```

## load_config

```
load_config() -> ConfigDict | None
```

Load the configuration if config file or config entry in pyproject.toml exists.

If neither config file was found or pyproject.toml file doesn't have a `[tool.griffe2md]` section, None is returned.

Source code in `src/griffe2md/_internal/config.py`

```
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
```

## prepare_context

```
prepare_context(
    obj: Object, config: ConfigDict | None = None
) -> dict
```

Prepare Jinja context.

Parameters:

- **`obj`** (`Object`) – A Griffe object.
- **`config`** (`ConfigDict | None`, default: `None` ) – The configuration options.

Returns:

- `dict` – The Jinja context.

Source code in `src/griffe2md/_internal/main.py`

```
def prepare_context(obj: Object, config: ConfigDict | None = None) -> dict:
    """Prepare Jinja context.

    Parameters:
        obj: A Griffe object.
        config: The configuration options.

    Returns:
        The Jinja context.
    """
    config = cast("ConfigDict", {**default_config, **(config or {})})
    if config["filters"]:
        config["filters"] = [
            (re.compile(filtr.lstrip("!")), filtr.startswith("!")) if isinstance(filtr, str) else filtr
            for filtr in config["filters"]
        ]

    heading_level = config["heading_level"]
    try:
        config["members_order"] = rendering.Order(config["members_order"]).value
    except ValueError as error:
        choices = "', '".join(item.value for item in rendering.Order)
        raise ValueError(
            f"Unknown members_order '{config['members_order']}', choose between '{choices}'.",
        ) from error

    summary = config["summary"]
    if summary is True:
        config["summary"] = {
            "attributes": True,
            "functions": True,
            "classes": True,
            "modules": True,
        }
    elif summary is False:
        config["summary"] = {
            "attributes": False,
            "functions": False,
            "classes": False,
            "modules": False,
        }
    else:
        config["summary"] = {
            "attributes": summary.get("attributes", False),
            "functions": summary.get("functions", False),
            "classes": summary.get("classes", False),
            "modules": summary.get("modules", False),
        }

    return {
        "config": config,
        obj.kind.value: obj,
        "heading_level": heading_level,
        "root": True,
    }
```

## prepare_env

```
prepare_env(env: Environment | None = None) -> Environment
```

Prepare Jinja environment.

Parameters:

- **`env`** (`Environment | None`, default: `None` ) – A Jinja environment.

Returns:

- `Environment` – The Jinja environment.

Source code in `src/griffe2md/_internal/main.py`

```
def prepare_env(env: Environment | None = None) -> Environment:
    """Prepare Jinja environment.

    Parameters:
        env: A Jinja environment.

    Returns:
        The Jinja environment.
    """
    env = env or Environment(
        autoescape=False,  # noqa: S701
        loader=FileSystemLoader([Path(__file__).parent.parent / "templates"]),
        auto_reload=False,
    )
    env.filters["any"] = rendering.do_any
    env.filters["heading"] = rendering.do_heading
    env.filters["as_attributes_section"] = rendering.do_as_attributes_section
    env.filters["as_classes_section"] = rendering.do_as_classes_section
    env.filters["as_functions_section"] = rendering.do_as_functions_section
    env.filters["as_modules_section"] = rendering.do_as_modules_section
    env.filters["filter_objects"] = rendering.do_filter_objects
    env.filters["format_code"] = rendering.do_format_code
    env.filters["format_signature"] = rendering.do_format_signature
    env.filters["format_attribute"] = rendering.do_format_attribute
    env.filters["order_members"] = rendering.do_order_members
    env.filters["split_path"] = rendering.do_split_path
    env.filters["stash_crossref"] = lambda ref, length: ref
    env.filters["from_private_package"] = rendering.from_private_package
    env.filters["newline_to_br"] = rendering._newline_to_br

    return env
```

## render_object_docs

```
render_object_docs(
    obj: Object, config: ConfigDict | None = None
) -> str
```

Render docs for a given object.

Parameters:

- **`obj`** (`Object`) – The Griffe object to render docs for.
- **`config`** (`ConfigDict | None`, default: `None` ) – The rendering configuration.

Warning

When using this function programmatically, options such as `docstring_style` and `docstring_options` must be passed to the Griffe loader so that they are correctly set when loading data. Check griffe.GriffeLoader for more information.

Returns:

- `str` – Markdown.

Source code in `src/griffe2md/_internal/main.py`

```
def render_object_docs(obj: Object, config: ConfigDict | None = None) -> str:
    """Render docs for a given object.

    Parameters:
        obj: The Griffe object to render docs for.
        config: The rendering configuration.

    Warning:
        When using this function programmatically,
        options such as `docstring_style` and `docstring_options` must be passed
        to the Griffe loader so that they are correctly set when loading data.
        Check [`griffe.GriffeLoader`][] for more information.

    Returns:
        Markdown.
    """
    env = prepare_env()
    context = prepare_context(obj, config)
    rendered = env.get_template(f"{obj.kind.value}.md.jinja").render(**context)
    return mdformat.text(rendered)
```

## render_package_docs

```
render_package_docs(
    package: str, config: ConfigDict | None = None
) -> str
```

Render docs for a given package.

Parameters:

- **`package`** (`str`) – The package (name) to render docs for.
- **`config`** (`ConfigDict | None`, default: `None` ) – The rendering configuration.

Returns:

- `str` – Markdown.

Source code in `src/griffe2md/_internal/main.py`

```
def render_package_docs(package: str, config: ConfigDict | None = None) -> str:
    """Render docs for a given package.

    Parameters:
        package: The package (name) to render docs for.
        config: The rendering configuration.

    Returns:
        Markdown.
    """
    config = cast("ConfigDict", {**default_config, **(config or {})})
    parser = config["docstring_style"] and Parser(config["docstring_style"])
    parser_options: DocstringOptions = config["docstring_options"]
    extensions = load_extensions(*config["extensions"]) if config["extensions"] else None
    loader = GriffeLoader(
        extensions=extensions,
        search_paths=config["search_paths"] + sys.path,
        docstring_parser=parser,
        docstring_options=parser_options,
        allow_inspection=config["allow_inspection"],
        force_inspection=config["force_inspection"],
    )
    module = loader.load(package)
    loader.resolve_aliases(external=True)
    return render_object_docs(module, config)  # type: ignore[arg-type]
```

## write_package_docs

```
write_package_docs(
    package: str,
    config: ConfigDict | None = None,
    output: IO | str | None = None,
) -> None
```

Write docs for a given package to a file or stdout.

Parameters:

- **`package`** (`str`) – The package to render docs for.
- **`config`** (`ConfigDict | None`, default: `None` ) – The rendering configuration.
- **`output`** (`IO | str | None`, default: `None` ) – The file to write to.

Source code in `src/griffe2md/_internal/main.py`

```
def write_package_docs(
    package: str,
    config: ConfigDict | None = None,
    output: IO | str | None = None,
) -> None:
    """Write docs for a given package to a file or stdout.

    Parameters:
        package: The package to render docs for.
        config: The rendering configuration.
        output: The file to write to.
    """
    _output(render_package_docs(package, config), to=output)
```
