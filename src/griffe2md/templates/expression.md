{%- set original_expression = expression -%}
{%- if original_expression is iterable and original_expression is not string -%}
{%- for expression in original_expression -%}
{%- include "expression.md" with context -%}
{%- endfor -%}
{%- elif original_expression is string -%}
{{ original_expression }}
{%- else -%}
{%- with annotation = original_expression|attr(config.annotations_path) -%}
{{ annotation }}
{%- endwith -%}
{%- endif -%}
