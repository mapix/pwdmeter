# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import range

from unittest import TestCase

import os
import sys
import os.path
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pwdmeter import LengthFactor


class LengthFactorTest(TestCase):

    def setUp(self):
        self.factor = LengthFactor(length=8)
        super(LengthFactorTest, self).setUp()

    def test_length(self):
        last_score = -1
        for i in range(self.factor.length):
            score, _ = self.factor.test('a' * (i + 1))
            assert score > last_score
            last_score = score

        score, feedback = self.factor._test('a' * self.factor.length)
        assert score == 1.0

        for i in range(self.factor.length, self.factor.length + 10):
            score, feedback = self.factor.test('a' * (i + 1))
            assert score > last_score
            last_score = score
