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
{%- with module_name = module.path if show_full_path else module.name -%}
{%- if config.separate_signature -%}
{{ module_name }}
{%- else -%}
`{{ module_name }}`
{%- endif -%}
{%- endwith -%}
{%- endfilter -%}

{%- else -%}
{%- set heading_level = heading_level - 1 -%}
{%- endif -%}

{%- with docstring_sections = module.docstring.parsed -%}
{%- include "docstring.md" with context -%}
{%- endwith -%}

{%- with obj = module -%}
{%- set root = False -%}
{%- set heading_level = heading_level + 1 -%}
{%- include "children.md" with context -%}
{%- endwith -%}
