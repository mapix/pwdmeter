# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest import TestCase

import os
import sys
import os.path
os.environ['PWDMETER_GETTEXT_LANGUAGE'] = 'cn'
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class MathTest(TestCase):

    def test_math(self):
        pass



