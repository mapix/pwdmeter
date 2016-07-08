# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest import TestCase

import os
import sys
import os.path
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pwdmeter import NonDictionaryFactor


class NonDictionaryFactorTest(TestCase):

    def setUp(self):
        self.factor = NonDictionaryFactor()
        super(NonDictionaryFactorTest, self).setUp()

    def test_factor(self):
        pass
