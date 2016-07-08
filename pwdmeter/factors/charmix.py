# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re

from pwdmeter.i18n import _
from pwdmeter.factors.factor import Factor


class CharmixFactor(Factor):

    category = 'charmix'
    lx_min = 0.0
    lx_max = 4.0

    number_re = re.compile('[0-9]')
    letter_re = re.compile('[a-zA-Z]')
    symbol_re = re.compile('[^a-zA-Z0-9]')

    def __init__(self, ly_min=0.8, ly_max=1.5, threshold=4.0, **kwargs):
        super(CharmixFactor, self).__init__(ly_min=ly_min, ly_max=ly_max, threshold=threshold, **kwargs)

    def _test(self, value):
        score = self.lx_min
        number_count = len(self.number_re.findall(value))
        letter_count = len(self.letter_re.findall(value))
        symbol_count = len(self.symbol_re.findall(value))
        mixed_count = [_f for _f in [number_count, letter_count, symbol_count] if _f]
        if len(mixed_count) == 2:
            score += 1
        if len(mixed_count) == 3:
            score += 3
        return score, (None if score >= self.threshold else _('Use a good mix of numbers, letters, and symbols'))
