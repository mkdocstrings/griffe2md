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
{%- if show_full_path -%}{{ attribute.path }}{%- else -%}{{ attribute.name }}{%- endif -%}
{%- else -%}
`
{%- if show_full_path -%}{{ attribute.path }}{%- else -%}{{ attribute.name }}{%- endif -%}
{%- if attribute.annotation -%}: {{ attribute.annotation }}{%- endif -%}
{%- if attribute.value -%} = {{ attribute.value }}{%- endif -%}
`
{%- endif -%}
{%- endfilter -%}

{%- if config.separate_signature -%}
```python
{% filter format_code(config.line_length) -%}
{%- if show_full_path -%}{{ attribute.path }}{%- else -%}{{ attribute.name }}{%- endif -%}
{%- if attribute.annotation -%}: {{ attribute.annotation|safe }}{%- endif -%}
{%- if attribute.value -%} = {{ attribute.value|safe }}{%- endif -%}
{%- endfilter %}
```
{%- endif %}

{%- else -%}
{%- if config.show_root_toc_entry %}
{% filter heading(heading_level) -%}
{%- endfilter -%}
{%- endif -%}
{%- set heading_level = heading_level - 1 -%}
{%- endif -%}

{%- with docstring_sections = attribute.docstring.parsed -%}
{%- include "docstring.md" with context -%}
{%- endwith -%}
