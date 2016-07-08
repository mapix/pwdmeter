# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re

from pwdmeter.i18n import _
from pwdmeter.math import Sigmoid
from pwdmeter.factors.factor import Factor


class NonASCIIFactor(Factor):

    category = 'non_ascii'
    lx_min = 0.0
    lx_max = 1.0

    non_ascii_re = re.compile('[^a-zA-Z0-9_]')

    def __init__(self, ly_min=0.9, ly_max=2.0, **kwargs):
        self.ajust = Sigmoid(self.lx_max)
        super(NonASCIIFactor, self).__init__(ly_min=ly_min, ly_max=ly_max, **kwargs)

    def _test(self, value):
        count = len(self.non_ascii_re.findall(value))
        if not count:
            return self.lx_min, _('Use non-ASCII chars')
        score = self.ajust(count)
        return score, None
