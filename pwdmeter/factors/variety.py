# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals
from builtins import range
from past.utils import old_div
from pwdmeter.i18n import _
from pwdmeter.math import Descend
from pwdmeter.factors.factor import Factor


class VarietyFactor(Factor):

    category = 'variety'
    lx_min = 0.0
    lx_max = 1.0

    def __init__(self, ly_min=0.0, ly_max=1.0, **kwargs):
        self.ajust = Descend(tardiness=1.0)
        super(VarietyFactor, self).__init__(**kwargs)

    def _test(self, value):
        same_count = 0
        last_char = None
        for idx in range(1, len(value)):
            if last_char == value[idx]:
                same_count += 1
            last_char = value[idx]
        if not same_count:
            return self.lx_max, None
        elif same_count == len(value):
            return self.lx_min, _('Minimize character duplicates and repetitions')
        score = self.ajust(old_div(float(same_count), float(len(value))))
        return score, (None if score >= self.threshold else _('Minimize character duplicates and repetitions'))
