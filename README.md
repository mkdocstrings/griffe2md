# griffe2md

[![ci](https://github.com/mkdocstrings/griffe2md/workflows/ci/badge.svg)](https://github.com/mkdocstrings/griffe2md/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe2md/)
[![pypi version](https://img.shields.io/pypi/v/griffe2md.svg)](https://pypi.org/project/griffe2md/)
[![gitter](https://img.shields.io/badge/matrix-chat-4DB798.svg?style=flat)](https://app.gitter.im/#/room/#griffe2md:gitter.im)

Output API docs to Markdown using Griffe.

## Installation

```bash
pip install griffe2md
```

With [`uv`](https://docs.astral.sh/uv/):

```bash
uv tool install griffe2md
```

## Usage

Simply call `griffe2md` with a package name, or the path to a package folder:

```bash
griffe2md markdown
griffe2md path/to/my/src/package
```

Use the `-o`, `--output` option to write to a file instead of standard output:

```bash
griffe2md markdown -o markdown.md
```

`griffe2md` can be configured in either `pyproject.toml` or a `griffe2md.toml` file. The latter can be placed in a `.config` or `config` directory in the project root.

`griffe2md.toml` file is structured as a simple key-value dictionary, e.g.:

```toml
docstring_style = "sphinx"
```

If you configure it in `pyproject.toml`, the configuration should go under the `tool.griffe2md` key:

```toml
[tool.griffe2md]
docstring_style = "sphinx"
```

See [the documentation](https://mkdocstrings.github.io/griffe2md/reference/griffe2md/config/#griffe2md.config.ConfigDict) for reference.
