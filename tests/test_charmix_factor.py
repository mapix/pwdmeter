# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest import TestCase

import os
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
from pwdmeter import CharmixFactor


class CharmixFactorTest(TestCase):

    def setUp(self):
        self.factor = CharmixFactor()
        super(CharmixFactorTest, self).setUp()

    def test_factor(self):
        pass
