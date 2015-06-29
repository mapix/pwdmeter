# -*- coding: utf-8 -*-

from unittest import TestCase

import os
import sys
import os.path
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pwdmeter import NonASCIIFactor


class NonAsciiFactorTest(TestCase):

    def setUp(self):
        self.factor = NonASCIIFactor()
        super(NonAsciiFactorTest, self).setUp()

    def test_factor(self):
        pass
