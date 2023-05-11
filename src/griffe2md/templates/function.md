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

{%- if show_full_path -%}{{ function.path }}{%- else -%}{{ function.name }}{%- endif -%}
{%- if not config.separate_signature -%}
{%- include "signature.md" with context -%}
{%- endif -%}
{%- endfilter -%}

{%- if config.separate_signature -%}
```python
{% filter format_signature(function, config.line_length, crossrefs=config.signature_crossrefs) -%}
{%- if show_full_path -%}{{ function.path }}{%- else -%}{{ function.name }}{%- endif -%}
{% endfilter %}
```

{% endif %}

{% else -%}
{%- set heading_level = heading_level - 1 -%}
{%- endif -%}

{%- with docstring_sections = function.docstring.parsed -%}
{%- include "docstring.md" with context -%}
{%- endwith -%}
