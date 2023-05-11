{%- if config.docstring_section_style == "table" %}
{%- block table_style %}

**{{ section.title or "Attributes:" }}**

Name | Type | Description
---- | ---- | -----------
{%- for attribute in section.value %}
`{{ attribute.name }}` | {% if attribute.annotation -%}{%- with expression = attribute.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- endif %} | {{ attribute.description }}
{%- endfor -%}
{%- endblock table_style -%}

{%- elif config.docstring_section_style == "list" %}
{%- block list_style %}

**{{ section.title or "Attributes:" }}**
{% for attribute in section.value %}
- **{{ attribute.name }}**{%- if attribute.annotation -%}{%- with expression = attribute.annotation %} (`{%- include "expression.md" with context -%}`){%- endwith -%}{%- endif %} – {{ attribute.description }}
{%- endfor -%}
{%- endblock list_style -%}
{%- endif -%}