"""End-to-end markdown spacing tests."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import griffe
import pytest
from griffe import GriffeLoader, Parser

from griffe2md import render_object_docs

if TYPE_CHECKING:
    from griffe._internal.models import Module

snapshot = pytest.importorskip("inline_snapshot").snapshot


code = '''"""Package docs first paragraph.

Package docs second paragraph.
"""


def render_me(first: str, second: str = "x") -> tuple[bool, bool]:
    """Render this function.

    More details in a second paragraph.

    Args:
        first: First parameter.
        second: Second parameter.

    Raises:
        ValueError: First error.
        RuntimeError: Second error.

    Warns:
        UserWarning: First warning.
        DeprecationWarning: Second warning.

    Returns:
        Status 1.
        Status 2.

    Examples:
        A simple example:

        >>> render_me("a")
        (True, True)

        Another example:

        >>> render_me("a", "y")
        (True, True)
    """
    return True, True


def render_you() -> None:
    """Hello."""
'''


def _render(**kwargs: Any) -> str:
    with griffe.temporary_pyfile(code) as (module_name, module_path):
        loader = GriffeLoader(
            search_paths=[str(module_path.parent)],
            docstring_parser=Parser("google"),
            allow_inspection=False,
            force_inspection=False,
        )
        module: Module = loader.load(module_name)  # ty:ignore[invalid-assignment]

    return render_object_docs(
        module,
        {
            "show_root_full_path": False,
            "show_root_members_full_path": False,
            "show_object_full_path": False,
            "show_category_heading": False,
            "show_signature": True,
            **kwargs,
        },
        format_md=False,
    )


def _assert_common_spacing_rules(rendered: str) -> None:
    assert all(not line.endswith((" ", "\t")) for line in rendered.splitlines())
    assert "\n\n- **first**" in rendered
    assert "\n- **first**\n\n- **second**" not in rendered


def test_render_markdown_spacing_list_style() -> None:
    rendered = (
        _render(
            docstring_section_style="list",
            separate_signature=True,
            summary=True,
        ).strip("\n")
        + "\n"
    )

    _assert_common_spacing_rules(rendered)

    assert rendered == snapshot("""\
## `module`

Package docs first paragraph.

Package docs second paragraph.

**Functions:**

- [**render_me**](#module.render_me) – Render this function.
- [**render_you**](#module.render_you) – Hello.

### `render_me`

```python
render_me(first, second='x')
```

Render this function.

More details in a second paragraph.

**Parameters:**

- **first** (<code>[str](#str)</code>) – First parameter.
- **second** (<code>[str](#str)</code>) – Second parameter.

**Raises:**

- <code>[ValueError](#ValueError)</code> – First error.
- <code>[RuntimeError](#RuntimeError)</code> – Second error.

**Warns:**

- <code>UserWarning</code> – First warning.
- <code>DeprecationWarning</code> – Second warning.

**Returns:**

- <code>[bool](#bool)</code> – Status 1.
- <code>[bool](#bool)</code> – Status 2.

**Examples:**

A simple example:

```pycon
>>> render_me("a")
(True, True)
```

Another example:

```pycon
>>> render_me("a", "y")
(True, True)
```

### `render_you`

```python
render_you()
```

Hello.
""")


def test_render_markdown_spacing_table_style() -> None:
    rendered = (
        _render(
            docstring_section_style="table",
            separate_signature=True,
            summary=True,
        ).strip("\n")
        + "\n"
    )
    assert rendered == snapshot("""\
## `module`

Package docs first paragraph.

Package docs second paragraph.

**Functions:**

Name | Description
---- | -----------
[`render_me`](#module.render_me) | Render this function.
[`render_you`](#module.render_you) | Hello.

### `render_me`

```python
render_me(first, second='x')
```

Render this function.

More details in a second paragraph.

**Parameters:**

Name | Type | Description | Default
---- | ---- | ----------- | -------
`first` | <code>[str](#str)</code> | First parameter. | *required*
`second` | <code>[str](#str)</code> | Second parameter. | <code>'x'</code>

**Raises:**

Type | Description
---- | -----------
<code>[ValueError](#ValueError)</code> | First error.
<code>[RuntimeError](#RuntimeError)</code> | Second error.

**Warns:**

Type | Description
---- | -----------
<code>UserWarning</code> | First warning.
<code>DeprecationWarning</code> | Second warning.

**Returns:**

Type | Description
---- | -----------
<code>[bool](#bool)</code> | Status 1.
<code>[bool](#bool)</code> | Status 2.

**Examples:**

A simple example:

```pycon
>>> render_me("a")
(True, True)
```

Another example:

```pycon
>>> render_me("a", "y")
(True, True)
```

### `render_you`

```python
render_you()
```

Hello.
""")
