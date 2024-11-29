"""Init and utils."""

from AccessControl import Unauthorized
from plone import api
from Products.Five import BrowserView
from rich import inspect
from rich import pretty
from rich import print
from rich import print_json

import logging


def initialize(context):
    pass


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


class RaiseView(BrowserView):
    def __call__(self):
        raise Exception("This is a test exception")
