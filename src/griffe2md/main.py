"""Main function of the program."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import IO

import mdformat
from griffe.docstrings import Parser
from griffe.loader import GriffeLoader
from jinja2 import Environment, FileSystemLoader

from griffe2md import rendering


def _output(text: str, to: IO | str | None = None) -> None:
    if isinstance(to, str):
        with open(to, "w") as output:
            output.write(text)
    else:
        if to is None:
            to = sys.stdout
        to.write(text)


def render_package_docs(package: str, config: dict | None = None) -> str:
    """Render docs for a given package.

    Parameters:
        package: The package to render docs for.
        config: The rendering configuration.


    Returns:
        Markdown.
    """
    config = config or dict(rendering.default_config)
    if config["filters"]:
        config["filters"] = [(re.compile(filtr.lstrip("!")), filtr.startswith("!")) for filtr in config["filters"]]
    parser = config["docstring_style"] and Parser(config["docstring_style"])
    loader = GriffeLoader(docstring_parser=parser)
    module = loader.load_module(package)
    loader.resolve_aliases()
    env = Environment(
        autoescape=False,  # noqa: S701
        loader=FileSystemLoader([Path(__file__).parent / "templates"]),
        auto_reload=False,
    )
    env.filters["any"] = rendering.do_any
    env.filters["filter_objects"] = rendering.do_filter_objects
    env.filters["heading"] = rendering.do_heading
    env.filters["order_members"] = rendering.do_order_members
    env.filters["format_code"] = rendering.do_format_code
    env.filters["format_signature"] = rendering.do_format_signature

    rendered = env.get_template("module.md").render(module=module, root=True, config=config, heading_level=2)
    return mdformat.text(rendered)


def write_package_docs(package: str, config: dict | None = None, output: IO | str | None = None) -> None:
    """Write docs for a given package to a file or stdout.

    Parameters:
        package: The package to render docs for.
        config: The rendering configuration.
        output: The file to write to.
    """
    _output(render_package_docs(package, config), to=output)
