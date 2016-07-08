# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from pprint import pprint
from unittest import TestCase

import os
import sys
import os.path
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pwdmeter import Meter, NonASCIIFactor, NonDictionaryFactor, LengthFactor, VarietyFactor, CasemixFactor, CharmixFactor


class MeterTest(TestCase):

    def setUp(self):
        self.m = Meter([NonDictionaryFactor(), NonASCIIFactor(), LengthFactor(), VarietyFactor(), CasemixFactor(), CharmixFactor()])
        self.threshold = self.m.threshold
        super(MeterTest, self).setUp()

    @property
    def data(self):
        return [
            ("",                       False, []),
            (",",                      False, []),
            ("12345678",               False, []),
            ("asdf",                   False, []),
            ("pass",                   False, []),
            ("fewsIa",                 True, []),
            ("fewsIa1234",             True, []),
            ("fewsIa1234.*&",          True, []),
            ("你好啊",                 False, []),
            ("你好啊的算法第三方",     True, []),
            ("douban",                 False, []),
            ("mapix",                  False, []),
        ]

    def p(self, value):
        pprint(value)

    def test_meter(self):
        for pwd, condition, _ in self.data:
            score, feedbacks = self.m.test(pwd)
            assert (score > 0.5) is condition
