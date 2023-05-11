{%- if root -%}
{%- set show_full_path = config.show_root_full_path -%}
{%- set root_members = True -%}
{%- elif root_members -%}
{%- set show_full_path = config.show_root_members_full_path or config.show_object_full_path -%}
{%- set root_members = False -%}
{%- else -%}
{%- set show_full_path = config.show_object_full_path -%}
{%- endif -%}

{%- if not root or config.show_root_heading %}

{% filter heading(heading_level) -%}
{%- if config.separate_signature -%}
{%- if show_full_path -%}{{ class.path }}{%- else -%}{{ class.name }}{%- endif -%}
{%- elif config.merge_init_into_class and "__init__" in class.members -%}
{%- with function = class.members["__init__"] -%}
{%- if show_full_path -%}{{ class.path }}{%- else -%}{{ class.name }}{%- endif -%}
{%- include "signature.md" with context -%}
{%- endwith -%}
{%- else -%}
`{%- if show_full_path -%}{{ class.path }}{%- else -%}{{ class.name }}{%- endif -%}`
{%- endif -%}
{%- endfilter -%}

{%- if config.separate_signature and config.merge_init_into_class -%}
{%- if "__init__" in class.members -%}
{%- with function = class.members["__init__"] -%}
```python
{% filter format_signature(function, config.line_length, crossrefs=config.signature_crossrefs) -%}
{%- if show_full_path -%}{{ class.path }}{%- else -%}{{ class.name }}{%- endif -%}
{% endfilter %}
```

{% endwith %}
{%- endif -%}
{%- endif -%}

{%- else -%}
{%- set heading_level = heading_level - 1 -%}
{%- endif -%}

{%- if config.show_bases and class.bases -%}
Bases: {% for expression in class.bases -%}
`{%- include "expression.md" with context -%}`{%- if not loop.last -%}, {% endif -%}
{% endfor %}

{% endif %}

{%- with docstring_sections = class.docstring.parsed -%}
{%- include "docstring.md" with context -%}
{%- endwith -%}

{%- if config.merge_init_into_class -%}
{%- if "__init__" in class.members and class.members["__init__"].has_docstring -%}
{%- with docstring_sections = class.members["__init__"].docstring.parsed -%}
{%- include "docstring.md" with context -%}
{%- endwith -%}
{%- endif -%}
{%- endif -%}

{%- with obj = class -%}
{%- set root = False -%}
{%- set heading_level = heading_level + 1 -%}
{%- include "children.md" with context -%}
{%- endwith -%}
