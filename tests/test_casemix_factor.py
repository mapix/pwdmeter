# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest import TestCase

import os
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
from pwdmeter import CasemixFactor


class CasemixFactorTest(TestCase):

    def setUp(self):
        self.factor = CasemixFactor()
        super(CasemixFactorTest, self).setUp()

    def test_factor(self):
        pass


