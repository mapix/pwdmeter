# -*- coding: utf-8 -*-

from pwdmeter.i18n import _
from pwdmeter.math import Sigmoid
from pwdmeter.factors.factor import Factor


class LengthFactor(Factor):

    category = 'length'
    lx_min = None
    lx_max = None

    def __init__(self, length=8, **kwargs):
        self.length = length
        lx_max = float(self.length * 1) / (self.length - 1)
        self.ajust = Sigmoid(target=lx_max)
        self.lx_min = self.ajust(0)
        self.lx_max = lx_max
        super(LengthFactor, self).__init__(**kwargs)

    def _test(self, value):
        if len(value) < self.length:
            score = (1.0 - self.lx_min) * (float(len(value)) / self.length) ** 2
        else:
            score = self.ajust(len(value))
        return score, (None if score >= self.threshold else _('Increase the length of the password'))
