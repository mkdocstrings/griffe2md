"""Module that contains the command line application."""

# Why does this file exist, and why not put this in `__main__`?
#
# You might be tempted to import things from `__main__` later,
# but that will cause problems: the code will get executed twice:
#
# - When you run `python -m griffe2md` python will execute
#   `__main__.py` as a script. That means there won't be any
#   `griffe2md.__main__` in `sys.modules`.
# - When you import `__main__` it will get executed again (as a module) because
#   there's no `griffe2md.__main__` in `sys.modules`.

from __future__ import annotations

import argparse

from griffe2md.main import write_package_docs


def get_parser() -> argparse.ArgumentParser:
    """Return the CLI argument parser.

    Returns:
        An argparse parser.
    """
    parser = argparse.ArgumentParser(prog="griffe2md")
    parser.add_argument("package", help="The package to output Markdown docs for.")
    parser.add_argument("-o", "--output", default=None, help="File to write to. Default: stdout.")
    return parser


def main(args: list[str] | None = None) -> int:
    """Run the main program.

    This function is executed when you type `griffe2md` or `python -m griffe2md`.

    Parameters:
        args: Arguments passed from the command line.

    Returns:
        An exit code.
    """
    parser = get_parser()
    opts = parser.parse_args(args=args)
    write_package_docs(opts.package, output=opts.output)
    return 0
