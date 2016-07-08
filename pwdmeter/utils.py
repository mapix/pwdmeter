# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import object

import marisa_trie
from future.utils import with_metaclass


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Resource(with_metaclass(Singleton, object)):

    @property
    def path(self):
        raise NotImplementedError

    def __init__(self):
        self.trie = marisa_trie.Trie([x for x in open(self.path)])

    def check(self, value):
        return self.trie.has_keys_with_prefix(value.lower())
