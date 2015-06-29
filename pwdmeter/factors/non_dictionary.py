# -*- coding: utf-8 -*-

from pwdmeter.i18n import _
from pwdmeter.utils import Resource
from pwdmeter.factors.factor import Factor


class NonDictionaryFactor(Factor):

    category = 'non_dictionary'
    lx_min = 0.0
    lx_max = 1.0

    def __init__(self, ly_min=0.01, ly_max=1.0, **kwargs):
        self.resource = CommonResource()
        super(NonDictionaryFactor, self).__init__(ly_min=ly_min, ly_max=ly_max, **kwargs)

    def _test(self, value):
        if self.resource.check(value):
            return (self.lx_min, _('Avoid using most common passwords'))
        return (self.lx_max, None)


class CommonResource(Resource):

    kind = 'common'
