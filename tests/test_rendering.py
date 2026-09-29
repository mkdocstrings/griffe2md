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
