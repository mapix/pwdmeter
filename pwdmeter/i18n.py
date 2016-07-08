# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import os.path
import gettext

from builtins import str

resource_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'i18n')
trans = gettext.translation('pwdmeter', localedir=resource_path, languages=[os.getenv('PWDMETER_GETTEXT_LANGUAGE', 'en')], fallback=True)

def _(*args, **kwargs):
    r = trans.gettext(*args, **kwargs)
    if not isinstance(r, str):
        r = r.decode('utf-8')
    return r
