# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import object

from abc import ABCMeta, abstractmethod, abstractproperty

from pwdmeter.math import SectionMap
from future.utils import with_metaclass


class Factor(with_metaclass(ABCMeta, object)):

    @abstractproperty
    def category(self):
        pass

    @abstractproperty
    def lx_min(self):
        pass

    @abstractproperty
    def lx_max(self):
        pass

    def __init__(self, ly_min=0.0, ly_max=1.0, skew=0.5, threshold=1.0):
        self.ly_min = float(ly_min)
        self.ly_max = float(ly_max)
        self.skew = float(skew)
        self.threshold = float(threshold)
        self.map = SectionMap(self.lx_min, self.lx_max, self.ly_min, self.ly_max, skew)

    @abstractmethod
    def _test(self, value):
        pass

    def test(self, value):
        score, feedback = self._test(value)
        return self.map.calc(score), feedback
