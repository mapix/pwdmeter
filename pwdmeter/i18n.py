# -*- coding: utf-8 -*-

from gettext import gettext


def _(message, *args, **kwargs):
    if args or kwargs:
        return gettext(message).format(*args, **kwargs)
    return gettext(message)
