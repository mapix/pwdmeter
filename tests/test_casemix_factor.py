# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest import TestCase

import os
import sys
import os.path
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pwdmeter import CasemixFactor


class CasemixFactorTest(TestCase):

    def setUp(self):
        self.factor = CasemixFactor()
        super(CasemixFactorTest, self).setUp()

    def test_factor(self):
        pass


