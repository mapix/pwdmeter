# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import object
from io import open

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
        f = open(self.path, 'rt')
        self.trie = marisa_trie.Trie([x for x in f])
        f.close()

    def check(self, value):
        return self.trie.has_keys_with_prefix(value.lower())
