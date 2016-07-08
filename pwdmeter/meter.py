# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from builtins import object

import logging

logger = logging.getLogger(__name__)


class Meter(object):

    def __init__(self, factors, threshold=0.75, language='en'):
        self.factors = factors
        self.threshold = float(threshold)

    def test(self, value):
        total_score = 1.0
        feedbacks = {}
        for factor in self.factors:
            score, feedback = factor.test(value)
            logger.debug("%s: %s, %s" % (factor.category, score, feedback))
            if feedback is not None:
                feedbacks[factor.category] = feedback
            total_score *= score
        return total_score, None if total_score >= self.threshold else feedbacks


def test(value):
    from pwdmeter import NonASCIIFactor, NonDictionaryFactor, LengthFactor, VarietyFactor, CasemixFactor, CharmixFactor
    m = Meter([NonDictionaryFactor(), NonASCIIFactor(), LengthFactor(), VarietyFactor(), CasemixFactor(), CharmixFactor()])
    return m.test(value)
