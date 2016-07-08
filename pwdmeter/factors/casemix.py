# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re

from pwdmeter.i18n import _
from pwdmeter.math import Descend
from pwdmeter.factors.factor import Factor


class CasemixFactor(Factor):

    category = 'casemix'
    lx_min = 0
    lx_max = 1

    lower_re = re.compile('[a-z]')
    upper_re = re.compile('[A-Z]')

    def __init__(self, ly_min=0.8, ly_max=1.5, threshold=0.1, tardiness=10.0, **kwargs):
        self.ajust = Descend(tardiness, self.lx_max, self.lx_min)
        super(CasemixFactor, self).__init__(ly_min=ly_min, ly_max=ly_max, threshold=threshold, **kwargs)

    def _test(self, value):
        upper_count = len(self.upper_re.findall(value))
        lower_count = len(self.lower_re.findall(value))
        if not (upper_count and lower_count):
            return self.lx_min, _('Use a good mix of upper case and lower case letters')
        score = self.ajust(upper_count - lower_count)
        return score, (None if score >= self.threshold else _('Use a good mix of upper case and lower case letters'))
