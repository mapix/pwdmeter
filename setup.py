# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pwdmeter',
    version='0.1.0',
    author='mapix',
    author_email='mapix.me@gmail.com',
    description='A password strength measuring library.',
    packages=find_packages(),
    install_requires=['marisa-trie==0.7.2'],
    include_package_data=True,
    zip_safe=False,
)
