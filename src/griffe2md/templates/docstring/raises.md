{%- if config.docstring_section_style == "table" %}
{%- block table_style %}

**{{ section.title or "Raises:" }}**

Type | Description
---- | -----------
{%- for raises in section.value %}
{%- if raises.annotation -%}{%- with expression = raises.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- endif -%} | {{ raises.description }}
{%- endfor -%}
{%- endblock table_style -%}

{%- elif config.docstring_section_style == "list" %}
{%- block list_style %}

**{{ section.title or "Raises:" }}**
{% for raises in section.value %}
- {% if raises.annotation -%}{%- with expression = raises.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith %} – {% endif -%}{{ raises.description }}
{%- endfor -%}
{%- endblock list_style -%}
{%- endif -%}