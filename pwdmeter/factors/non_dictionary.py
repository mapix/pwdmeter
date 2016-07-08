# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from os.path import join, abspath, dirname

from pwdmeter.i18n import _
from pwdmeter.utils import Resource
from pwdmeter.factors.factor import Factor


class NonDictionaryFactor(Factor):

    category = 'non_dictionary'
    lx_min = 0.0
    lx_max = 1.0

    def __init__(self, ly_min=0.01, ly_max=1.0, resource=None, **kwargs):
        self.resource = resource or DefaultResource()
        super(NonDictionaryFactor, self).__init__(ly_min=ly_min, ly_max=ly_max, **kwargs)

    def _test(self, value):
        if self.resource.check(value):
            return (self.lx_min, _('Avoid using most common passwords'))
        return (self.lx_max, None)


class DefaultResource(Resource):

    @property
    def path(self):
        return join(dirname(abspath(dirname(__file__))), 'res/common.txt')
