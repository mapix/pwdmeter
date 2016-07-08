# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from setuptools import setup, find_packages

setup(
    name='pwdmeter',
    version='0.3.1',
    author='mapix',
    author_email='mapix.me@gmail.com',
    description='A password strength measuring library.',
    url='https://github.com/mapix/pwdmeter',
    long_description=open('README.rst').read(),
    keywords='password strength checker meter',
    packages=find_packages(),
    platforms=['any'],
    zip_safe=False,
    include_package_data=True,
    install_requires=['marisa-trie==0.7.2', 'future'],
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    license='MIT (http://opensource.org/licenses/MIT)',
)
