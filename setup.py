# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pwdmeter',
    version='0.1.2',
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
    install_requires=['marisa-trie==0.7.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'License :: Public Domain',
    ],
    license='MIT (http://opensource.org/licenses/MIT)',
)
