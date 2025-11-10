# griffe2md

Output API docs to Markdown using Griffe.

## Installation

```
pip install griffe2md
```

With [`uv`](https://docs.astral.sh/uv/):

```
uv tool install griffe2md
```

## Usage

Simply call `griffe2md` with a package name, or the path to a package folder:

```
griffe2md markdown
griffe2md path/to/my/src/package
```

Use the `-o`, `--output` option to write to a file instead of standard output:

```
griffe2md markdown -o markdown.md
```

`griffe2md` can be configured in either `pyproject.toml` or a `griffe2md.toml` file. The latter can be placed in a `.config` or `config` directory in the project root.

`griffe2md.toml` file is structured as a simple key-value dictionary, e.g.:

```
docstring_style = "sphinx"
```

If you configure it in `pyproject.toml`, the configuration should go under the `tool.griffe2md` key:

```
[tool.griffe2md]
docstring_style = "sphinx"
```

See [the documentation](https://mkdocstrings.github.io/griffe2md/reference/griffe2md/config/#griffe2md.config.ConfigDict) for reference.

## Sponsors
