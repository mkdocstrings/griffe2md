{%- if config.docstring_section_style == "table" %}
{%- block table_style %}

**{{ section.title or "Warns:" }}**

Type | Description
---- | -----------
{%- for warns in section.value %}
{%- if warns.annotation -%}{%- with expression = warns.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- endif -%} | {{ warns.description }}
{%- endfor -%}
{%- endblock table_style -%}

{%- elif config.docstring_section_style == "list" %}
{%- block list_style %}

**{{ section.title or "Warns:" }}**
{% for warns in section.value %}
- {% if warns.annotation -%}{%- with expression = warns.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith %} – {% endif -%}{{ warns.description }}
{%- endfor -%}
{%- endblock list_style -%}
{%- endif -%}