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

- https://your-site.example/pdb
- https://your-site.example/Plone/pdb

## Features

When you access the `pdb` path, you will be dropped into a pdb session where you can inspect the state of your application and debug any issues you may be facing.
You can use all the features of pdbpp, such as syntax highlighting, tab completion, and more.
In addition you will have Plone specific commands available and enhanced display using the `rich` library.

For example, you will have immediately available `plone.api`:
```shell
(Pdb++) api.portal.get()
<PloneSite at /Plone>
```
and `registered_layers()` to see the registered browser layers in your Plone site:
```shell
(Pdb++) pp registered_layers()
[
│   <InterfaceClass plone.app.z3cform.interfaces.IPloneFormLayer>,
│   <InterfaceClass plone.app.theming.interfaces.IThemingLayer>,
│   <InterfaceClass plone.app.contenttypes.interfaces.IPloneAppContenttypesLayer>,
│   <InterfaceClass plone.app.event.interfaces.IBrowserLayer>,
│   <InterfaceClass plone.app.layout.interfaces.IPloneAppLayoutLayer>
]
```
You can even use `self.layers` to see just the layers that are active for the current request:
```shell
(Pdb++) self.layers
[
│   'plone.app.z3cform.interfaces.IPloneFormLayer',
│   'plone.app.theming.interfaces.IThemingLayer',
│   'plone.app.contenttypes.interfaces.IPloneAppContenttypesLayer',
│   'plone.app.event.interfaces.IBrowserLayer',
│   'plone.app.layout.interfaces.IPloneAppLayoutLayer'
]
```

The `pp` command is customized to use `rich` for enhanced display of complex data structures, making it easier to read and understand the output.
It also understands Plone specific data structures, such as views,
request, BTrees objects, and displays them in a more informative way.

See, e.g.:
```shell
(Pdb++) pp request
╭──────────────────────── <class 'ZPublisher.HTTPRequest.WSGIRequest'> ─╮
│ <WSGIRequest, URL=https://your-site.example/Plone/pdb>                │
│                                                                       │
│ path = []                                                             │
│ form = {}                                                             │
│ other = {                                                             │
│     'SERVER_URL': 'https://your-site.example',                        │
│     'URL': 'https://your-site.example/Plone/pdb',                     │
│     'PATH_INFO': '/Plone/pdb',                                        │
│     'ACTUAL_URL': 'https://your-site.example/Plone/pdb'               │
│ }                                                                     │
╰───────────────────────────────────────────────────────────────────────╯
```

You also have an enhanced inspect command (`ii`) that uses `rich` to display details of the object you are inspecting, e.g.:
```shell
(Pdb++) ii api
╭───────────── <module 'plone.api' from '.../plone/api/__init__.py'> ─────────────╮
│      addon = <module 'plone.api.addon' from '.../plone/api/addon.py'>           │
│    content = <module 'plone.api.content' from '.../plone/api/content.py'>       │
│        env = <module 'plone.api.env' from '.../plone/api/env.py'>               │
│        exc = <module 'plone.api.exc' from '.../plone/api/exc.py'>               │
│      group = <module 'plone.api.group' from '.../plone/api/group.py'>           │
│     portal = <module 'plone.api.portal' from '.../plone/api/portal.py'>         │
│   relation = <module 'plone.api.relation' from '.../plone/api/relation.py'>     │
│       user = <module 'plone.api.user' from '.../plone/api/user.py'>             │
│ validation = <module 'plone.api.validation' from '.../plone/api/validation.py'> │
╰─────────────────────────────────────────────────────────────────────────────────╯
```

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
