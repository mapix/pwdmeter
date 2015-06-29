# -*- coding: utf-8 -*-

import marisa_trie
from os.path import join, abspath, dirname


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Resource(object):

    __metaclass__ = Singleton

    def __init__(self):
        path = join(abspath(dirname(__file__)), 'res/%s.txt' % self.kind)
        self.trie = marisa_trie.Trie(map(lambda x:x.decode('utf-8'), open(path)))

    def check(self, value):
        return self.trie.has_keys_with_prefix(value.lower().decode('utf-8'))
