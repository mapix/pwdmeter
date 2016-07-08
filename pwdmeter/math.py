# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from builtins import object
from past.utils import old_div
from math import sqrt, fabs


class SectionMap(object):

    def __init__(self, lx_min, lx_max, ly_min, ly_max, skew=0.5):
        self.lx_min = float(lx_min)
        self.lx_max = float(lx_max)
        self.ly_min = float(ly_min)
        self.ly_max = float(ly_max)
        self.skew = skew

    def __call__(self, v):
        v = float(v)
        r = (2.0 * (old_div(1.0, self.skew) -1.0) ** 2.0 + 1.0 + 2.0 * (old_div(1.0,self.skew) - 1.0 ))
        return (self.ly_max - self.ly_min) * (sqrt(r - (old_div((v - self.lx_min), (self.lx_max - self.lx_min)) - old_div(1.0, self.skew)) ** 2.0) + 1.0 - old_div(1.0, self.skew)) + self.ly_min

    def calc(self, v):
        return self(v)


class Sigmoid(object):

    'Ref: https://en.wikipedia.org/wiki/Sigmoid_function#Examples'

    def __init__(self, target=1.0):
        self.target = float(target)

    def __call__(self, x):
        return self.target * float(x) / (self.target + fabs(x))

    def calc(self, x):
        return self(x)


class Descend(object):

    def __init__(self, tardiness=10.0, begin=1.0, end=0.0):
        self.tardiness = tardiness
        self.begin = begin
        self.end = end

    def __call__(self, x):
        return self.begin * (old_div(self.tardiness, (fabs(x) + self.tardiness))) + self.end

    def calc(self, x):
        return self(x)
