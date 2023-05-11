{%- if config.docstring_section_style == "table" %}
{%- block table_style %}

{%- set name_column = section.value|selectattr("name")|any -%}
**{{ section.title or "Yields:" }}**

{% if name_column -%}Name | {% endif -%}Type | Description
{% if name_column -%}---- | {% endif -%}---- | -----------
{%- for yields in section.value %}
{%- if name_column -%}{%- if yields.name -%}`{{ yields.name }}`{%- endif %} | {% endif -%}{%- if yields.annotation -%}{%- with expression = yields.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- endif %} | {{ yields.description }}
{%- endfor -%}
{%- endblock table_style -%}

{%- elif config.docstring_section_style == "list" %}
{%- block list_style %}

**{{ section.title or "Yields:" }}**
{% for yields in section.value %}
- {% if yields.name -%}**{{ yields.name }}**{%- endif -%}{%- if yields.annotation -%}{%- with expression = yields.annotation -%}{%- if yields.name %} ({%- endif -%}`{%- include "expression.md" with context -%}`{%- if yields.name -%}) {% endif -%}{%- endwith -%}{%- endif -%}– {{ yields.description }}
{%- endfor -%}
{%- endblock list_style -%}
{%- endif -%}