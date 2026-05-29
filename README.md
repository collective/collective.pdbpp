[![CI](https://github.com/collective/collective.pdbpp/actions/workflows/plone-package.yml/badge.svg)](https://github.com/collective/collective.pdbpp/actions/workflows/plone-package.yml)
[![Coveralls](https://coveralls.io/repos/github/collective/collective.pdbpp/badge.svg?branch=main)](https://coveralls.io/github/collective/collective.pdbpp?branch=main)
[![Codecov](https://codecov.io/gh/collective/collective.pdbpp/branch/master/graph/badge.svg)](https://codecov.io/gh/collective/collective.pdbpp)
[![Latest Version](https://img.shields.io/pypi/v/collective.pdbpp.svg)](https://pypi.python.org/pypi/collective.pdbpp/)
[![Package Status](https://img.shields.io/pypi/status/collective.pdbpp.svg)](https://pypi.python.org/pypi/collective.pdbpp)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/collective.pdbpp.svg)
[![License](https://img.shields.io/pypi/l/collective.pdbpp.svg)](https://pypi.python.org/pypi/collective.pdbpp/)

# collective.pdbpp

An add-on for Plone that allows you to use [pdbpp](https://github.com/pdbpp/pdbpp).

## Installation

Install `collective.pdbpp` by adding it to your buildout:

```ini
[instance]
eggs +=
    collective.pdbpp
```

Then run:

```bash
bin/buildout
```

When your instance starts, you can enter a pdb session by adding the `pdb` path to any URL, for example:

- http://localhost:8080/pdb
- http://localhost:8080/Plone/pdb

## Authors

The [Syslab.com](https://www.syslab.com) Team.

## Contributors

Put your name here, you deserve it!

- Alessandro Pisa, [Syslab.com](https://www.syslab.com)

## Contribute

- Issue Tracker: https://github.com/collective/collective.pdbpp/issues
- Source Code: https://github.com/collective/collective.pdbpp
- Documentation: https://github.com/collective/collective.pdbpp#readme

## Support

If you are having issues, please let us know in the [issue tracker](https://github.com/collective/collective.pdbpp/issues).

## License

The project is licensed under GPLv2.
