"""Init and utils."""

from AccessControl import Unauthorized
from pdb import Pdb  # type: ignore
from plone import api
from Products.Five import BrowserView
from rich import inspect
from rich import pretty
from rich import print
from rich import print_json

import logging


def initialize(context):
    pass


def _do_pp(self, arg):
    """Override the pp (pretty-print) command to use rich."""
    try:
        # Evaluate the argument in the current debugging context
        obj = self._getval(arg)
        # Use rich's pprint to display the object
        pretty.pprint(obj, expand_all=True)
    except Exception:
        self._original_do_pp(arg)



Pdb._original_do_pp = Pdb.do_pp
Pdb.do_pp = _do_pp


class PdbView(BrowserView):
    def __call__(self):
        if not api.env.debug_mode():
            raise Unauthorized

        locals().update(
            {
                "api": api,
                "context": self.context,
                "inspect": inspect,
                "print_json": print_json,
                "print": print,
                "request": self.request,
            }
        )

        pretty.install()
        print(locals())
        breakpoint()
        logging.info("Exiting the interactive session")
        return self.request.response.redirect(self.context.absolute_url())
