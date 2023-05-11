{%- if obj.members -%}
{%- if root_members -%}
{%- set members_list = config.members -%}
{%- else -%}
{%- set members_list = none -%}
{%- endif -%}

{%- if config.group_by_category -%}

{%- with -%}

{%- if config.show_category_heading -%}
{%- set extra_level = 1 -%}
{%- else -%}
{%- set extra_level = 0 -%}
{%- endif -%}

{%- with attributes = obj.attributes|filter_objects(filters=config.filters, members_list=members_list, keep_no_docstrings=config.show_if_no_docstring) -%}
{%- if attributes -%}
{%- if config.show_category_heading %}

{% filter heading(heading_level) -%}Attributes{%- endfilter -%}
{%- endif -%}
{%- with heading_level = heading_level + extra_level -%}
{%- for attribute in attributes|order_members(config.members_order, members_list) -%}
{%- if not attribute.is_alias or attribute.is_explicitely_exported -%}
{%- include "attribute.md" with context -%}
{%- endif -%}
{%- endfor -%}
{%- endwith -%}
{%- endif -%}
{%- endwith -%}

{%- with classes = obj.classes|filter_objects(filters=config.filters, members_list=members_list, keep_no_docstrings=config.show_if_no_docstring) -%}
{%- if classes -%}
{%- if config.show_category_heading %}

{% filter heading(heading_level) -%}Classes{%- endfilter -%}
{%- endif -%}
{%- with heading_level = heading_level + extra_level -%}
{%- for class in classes|order_members(config.members_order, members_list) -%}
{%- if not class.is_alias or class.is_explicitely_exported -%}
{%- include "class.md" with context -%}
{%- endif -%}
{%- endfor -%}
{%- endwith -%}
{%- endif -%}
{%- endwith -%}

{%- with functions = obj.functions|filter_objects(filters=config.filters, members_list=members_list, keep_no_docstrings=config.show_if_no_docstring) -%}
{%- if functions -%}
{%- if config.show_category_heading %}

{% filter heading(heading_level) -%}Functions{%- endfilter -%}
{%- endif -%}
{%- with heading_level = heading_level + extra_level -%}
{%- for function in functions|order_members(config.members_order, members_list) -%}
{%- if not (obj.kind.value == "class" and function.name == "__init__" and config.merge_init_into_class) -%}
{%- if not function.is_alias or function.is_explicitely_exported -%}
{%- include "function.md" with context -%}
{%- endif -%}
{%- endif -%}
{%- endfor -%}
{%- endwith -%}
{%- endif -%}
{%- endwith -%}

{%- if config.show_submodules -%}
{%- with modules = obj.modules|filter_objects(filters=config.filters, members_list=members_list, keep_no_docstrings=config.show_if_no_docstring) -%}
{%- if modules -%}
{%- if config.show_category_heading %}

{% filter heading(heading_level) -%}Modules{%- endfilter -%}
{%- endif -%}
{%- with heading_level = heading_level + extra_level -%}
{%- for module in modules|order_members(config.members_order, members_list) -%}
{%- if not module.is_alias or module.is_explicitely_exported -%}
{%- include "module.md" with context -%}
{%- endif -%}
{%- endfor -%}
{%- endwith -%}
{%- endif -%}
{%- endwith -%}
{%- endif -%}

{%- endwith -%}

{%- else -%}

{%- for child in obj.members|
filter_objects(filters=config.filters, members_list=members_list, keep_no_docstrings=config.show_if_no_docstring)|
order_members(config.members_order, members_list) -%}

{%- if not (obj.kind.value == "class" and child.name == "__init__" and config.merge_init_into_class) -%}

{%- if child.kind.value == "attribute" -%}
{%- with attribute = child -%}
{%- include "attribute.md" with context -%}
{%- endwith -%}

{%- elif child.kind.value == "class" -%}
{%- with class = child -%}
{%- include "class.md" with context -%}
{%- endwith -%}

{%- elif child.kind.value == "function" -%}
{%- with function = child -%}
{%- include "function.md" with context -%}
{%- endwith -%}

{%- elif child.kind.value == "module" and config.show_submodules -%}
{%- with module = child -%}
{%- include "module.md" with context -%}
{%- endwith -%}

{%- endif -%}

{%- endif -%}

{%- endfor -%}

{%- endif -%}

{%- endif -%}
