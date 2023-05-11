{%- if config.docstring_section_style == "table" %}
{%- block table_style %}

**{{ section.title or "Parameters:" }}**

Name | Type | Description | Default
---- | ---- | ----------- | -------
{%- for parameter in section.value %}
`{{ parameter.name }}` | {% if parameter.annotation -%}{%- with expression = parameter.annotation -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- endif %} | {{ parameter.description }} | {% if parameter.default -%}{%- with expression = parameter.default -%}`{%- include "expression.md" with context -%}`{%- endwith -%}{%- else -%}*required*{%- endif %}
{%- endfor -%}
{%- endblock table_style -%}

{%- elif config.docstring_section_style == "list" %}
{%- block list_style %}

**{{ section.title or "Parameters:" }}**
{% for parameter in section.value %}
- **{{ parameter.name }}**{%- if parameter.annotation -%}{%- with expression = parameter.annotation %} (`{%- include "expression.md" with context -%}`){%- endwith -%}{%- endif %} – {{ parameter.description }}
{%- endfor -%}
{%- endblock list_style -%}
{%- endif -%}