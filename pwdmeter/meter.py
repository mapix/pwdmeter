# -*- coding: utf-8 -*-


class Meter(object):

    def __init__(self, factors, threshold=0.75, language='en'):
        self.factors = factors
        self.threshold = float(threshold)

    def test(self, value):
        total_score = 1.0
        feedbacks = {}
        for factor in self.factors:
            score, feedback = factor.test(value)
            print factor.category, score, feedback
            if feedback is not None:
                feedbacks[factor.category] = feedback
            total_score *= score
        return total_score, None if total_score >= self.threshold else feedbacks
