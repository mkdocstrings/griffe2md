# griffe2md

[![ci](https://github.com/mkdocstrings/griffe2md/workflows/ci/badge.svg)](https://github.com/mkdocstrings/griffe2md/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe2md/)
[![pypi version](https://img.shields.io/pypi/v/griffe2md.svg)](https://pypi.org/project/griffe2md/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-708FCC.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/griffe2md)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#griffe2md:gitter.im)

Output API docs to Markdown using Griffe.

## Installation

With `pip`:

```bash
pip install griffe2md
```

With [`pipx`](https://github.com/pipxproject/pipx):

```bash
python3.8 -m pip install --user pipx
pipx install griffe2md
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
