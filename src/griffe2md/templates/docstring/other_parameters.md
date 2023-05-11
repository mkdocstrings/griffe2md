{%- if config.docstring_section_style == "table" %}
{%- block table_style %}

**{{ section.title or "Other Parameters:" }}**

Name | Type | Description
---- | ---- | -----------
{%- for parameter in section.value %}
`{{ parameter.name }}` | {% if parameter.annotation -%}{%- with expression = parameter.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- endif %} | {{ parameter.description }}
{%- endfor -%}
{%- endblock table_style -%}

{%- elif config.docstring_section_style == "list" %}
{%- block list_style %}

**{{ section.title or "Other Parameters:" }}**
{% for parameter in section.value %}
- **{{ parameter.name }}**{%- if parameter.annotation -%}{%- with expression = parameter.annotation %} (`{%- include "expression.md" with context -%}`){%- endwith -%}{%- endif %} – {{ parameter.description }}
{%- endfor -%}
{%- endblock list_style -%}
{%- endif -%}