# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest import TestCase

import os
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
from pwdmeter import NonASCIIFactor


class NonAsciiFactorTest(TestCase):

    def setUp(self):
        self.factor = NonASCIIFactor()
        super(NonAsciiFactorTest, self).setUp()

    def test_factor(self):
        pass
