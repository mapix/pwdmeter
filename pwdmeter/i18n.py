# -*- coding: utf-8 -*-

import os
import os.path
import gettext

resource_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'i18n')
trans = gettext.translation('pwdmeter', localedir=resource_path, languages=[os.getenv('PWDMETER_GETTEXT_LANGUAGE', 'en')], fallback=True)
_ = trans.gettext
