# -*- coding: utf-8 -*-

from pprint import pprint
from unittest import TestCase

import os
import sys
import os.path
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pwdmeter import Meter, NonASCIIFactor, NonDictionaryFactor, LengthFactor, VarietyFactor, CasemixFactor, CharmixFactor


class MeterTest(TestCase):

    @property
    def data(self):
        return {
            "",
            ",",
            "12345678",
            "asdf",
            "pass",
            "fewsIa",
            "fewsIa1234",
            "fewsIa1234.*&",
            "你好",
            "你好啊的算法第三方",
        }

    def test_meter(self):
        m = Meter([NonDictionaryFactor(), NonASCIIFactor(), LengthFactor(), VarietyFactor(), CasemixFactor(), CharmixFactor()])
        for pwd in self.data:
            print "{:*^40}".format(pwd if pwd else '<empty>')
            score, feedbacks = m.test(pwd)
            print "score: ", score
            print "feedbacks: "
            pprint(feedbacks)
            print

