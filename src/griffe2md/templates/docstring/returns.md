{%- if config.docstring_section_style == "table" %}
{%- block table_style %}

{%- set name_column = section.value|selectattr("name")|any -%}
**{{ section.title or "Returns:" }}**

{% if name_column -%}Name | {% endif -%}Type | Description
{% if name_column -%}---- | {% endif -%}---- | -----------
{%- for returns in section.value %}
{%- if name_column -%}{%- if returns.name -%}`{{ returns.name }}`{%- endif %} | {% endif %}{% if returns.annotation -%}{%- with expression = returns.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- endif %} | {{ returns.description }}
{%- endfor -%}
{%- endblock table_style -%}

{%- elif config.docstring_section_style == "list" %}
{%- block list_style %}

**{{ section.title or "Returns:" }}**
{% for returns in section.value %}
- {% if returns.name -%}**{{ returns.name }}**{%- endif -%}{%- if returns.annotation -%}{%- with expression = returns.annotation -%}{%- if returns.name %} ({%- endif -%}`{%- include "expression.md" with context -%}`{%- if returns.name -%}){%- endif -%}{%- endwith -%}{%- endif %} – {{ returns.description }}
{%- endfor -%}
{%- endblock list_style -%}
{%- endif -%}