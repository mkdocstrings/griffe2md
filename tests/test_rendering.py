import griffe
from inline_snapshot import snapshot

from griffe2md import render_object_docs


def test_mdformat_extensions() -> None:
    docstring = griffe.Docstring(
        """A docstring with a table.

        Header 1  | Header 2
        ------ | ---
        Cell 1    | Cell 2
        """,
    )
    attribute = griffe.Attribute(name="render_me", parent=None, value="...", docstring=docstring)

    not_formatted = render_object_docs(attribute, format_md=False).strip("\n") + "\n"
    assert not_formatted == snapshot("""\
## `render_me`

```python
render_me = ...
```

A docstring with a table.

Header 1  | Header 2
------ | ---
Cell 1    | Cell 2
""")

    formatted_no_table = render_object_docs(attribute, format_md=True).strip("\n") + "\n"
    assert formatted_no_table == snapshot("""\
## `render_me`

```python
render_me = ...
```

A docstring with a table.

Header 1 | Header 2
------ | ---
Cell 1 | Cell 2
""")
    formatted_table = (
        render_object_docs(attribute, config={"mdformat_extensions": ["tables"]}, format_md=True).strip("\n") + "\n"
    )
    assert formatted_table == snapshot("""\
## `render_me`

```python
render_me = ...
```

A docstring with a table.

| Header 1 | Header 2 |
| -------- | -------- |
| Cell 1   | Cell 2   |
""")
