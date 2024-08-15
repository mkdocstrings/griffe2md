# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [1.0.1](https://github.com/mkdocstrings/griffe2md/releases/tag/1.0.1) - 2024-08-15

<small>[Compare with 1.0.0](https://github.com/mkdocstrings/griffe2md/compare/1.0.0...1.0.1)</small>

### Build

- Depend on Griffe 0.49 ([e7fef87](https://github.com/mkdocstrings/griffe2md/commit/e7fef8732f2ffb52706967b9fa828261aedf9380) by Timothée Mazzucotelli).

### Code Refactoring

- Update code for Griffe 0.49 ([b321b39](https://github.com/mkdocstrings/griffe2md/commit/b321b3980e5ee2524c8f2db95c19ba897ad658b9) by Timothée Mazzucotelli).

## [1.0.0](https://github.com/mkdocstrings/griffe2md/releases/tag/1.0.0) - 2024-01-03

<small>[Compare with first commit](https://github.com/mkdocstrings/griffe2md/compare/d92385072e50ec53f4def83371884bf4558cb9a5...1.0.0)</small>

### Dependencies

- Bump required Griffe version to 0.36 ([7fd172e](https://github.com/mkdocstrings/griffe2md/commit/7fd172e92160154d0ecae8a94264bd5d31553510) by Timothée Mazzucotelli).

### Features

- Resolve external aliases pointing to objects in corresponding private packages (`ast.AST` -> `_ast.AST`) ([5630fdf](https://github.com/mkdocstrings/griffe2md/commit/5630fdf20606534c49eea1d2a31f6cc7f5945d60) by Timothée Mazzucotelli).
- Support latest Griffe, add auto-summaries and cross-references ([e744fac](https://github.com/mkdocstrings/griffe2md/commit/e744fac35a2dc13126fada91c35f50158c43938f) by Timothée Mazzucotelli).
- Add initial rendering feature ([d6e23ad](https://github.com/mkdocstrings/griffe2md/commit/d6e23ad5cd3dd87696fa43bdf110f9fbaa89cad9) by Timothée Mazzucotelli).

### Bug Fixes

- Use all members as well when not grouping by category ([b7086c7](https://github.com/mkdocstrings/griffe2md/commit/b7086c78cb5e91fb78c098c8103b83253c48620e) by Timothée Mazzucotelli).
- Never fail when trying to format code with Black ([940aa7a](https://github.com/mkdocstrings/griffe2md/commit/940aa7a6561e35bdeb71647daf9b8680850db81f) by Timothée Mazzucotelli).
- Add back logger to rendering module ([29ff6f8](https://github.com/mkdocstrings/griffe2md/commit/29ff6f8602d779132db20438b6d8aa61071d0430) by Timothée Mazzucotelli).
- Don't import stuff from mkdocstrings ([1108a3f](https://github.com/mkdocstrings/griffe2md/commit/1108a3f3eb324009a23d9598ba67053bcb93ec90) by Timothée Mazzucotelli).
- Add missing jinja2 dependency ([4b9067b](https://github.com/mkdocstrings/griffe2md/commit/4b9067ba2df89a3470f2cab9ddad673191efac47) by Timothée Mazzucotelli).

### Code Refactoring

- Never use full path in separate signatures ([ddfeac4](https://github.com/mkdocstrings/griffe2md/commit/ddfeac4b169acb86fdf128c233fe9c324d94d919) by Timothée Mazzucotelli).
- Use `html_links` option, stop using Textual click links ([f916d90](https://github.com/mkdocstrings/griffe2md/commit/f916d90c844e6e41304db4ca62418cc345af2a74) by Timothée Mazzucotelli).
