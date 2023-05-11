{%- if config.docstring_section_style == "table" %}
{%- block table_style %}

{%- set name_column = section.value|selectattr("name")|any -%}
**{{ section.title or "Receives:" }}**

{% if name_column -%}Name | {% endif -%}Type | Description
{% if name_column -%}---- | {% endif -%}---- | -----------
{%- for receives in section.value %}
{%- if name_column -%}{%- if receives.name -%}`{{ receives.name }}`{%- endif %} | {% endif %}{% if receives.annotation -%}{%- with expression = receives.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- endif %} | {{ receives.description }}
{%- endfor -%}
{%- endblock table_style -%}

{%- elif config.docstring_section_style == "list" %}
{%- block list_style %}

**{{ section.title or "Receives:" }}**
{% for receives in section.value %}
- {% if receives.name -%}**{{ receives.name }}**{%- endif -%}{%- if receives.annotation -%}{%- with expression = receives.annotation -%}{%- if receives.name %} ({%- endif -%}`{%- include "expression.md" with context -%}`{%- if receives.name -%}) {% endif -%}{%- endwith -%}{%- endif -%}– {{ receives.description }}
{%- endfor -%}
{%- endblock list_style -%}
{%- endif -%}