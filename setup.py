#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import inspect

import setuptools
from setuptools import setup

__location__ = os.path.join(os.getcwd(), os.path.dirname(inspect.getfile(inspect.currentframe())))


def read_version(package):
    data = {}
    with open(os.path.join(package, '__init__.py'), 'r') as fd:
        exec (fd.read(), data)
    return data['__version__']


NAME = 'rgbxy'
MAIN_PACKAGE = 'rgbxy'
VERSION = read_version(MAIN_PACKAGE)
DESCRIPTION = 'RGB conversion tool written in Python for Philips Hue.'
LICENSE = 'MIT'
URL = 'https://github.com/benknight/hue-python-rgb-converter'
AUTHOR = 'Ben Knight'
EMAIL = 'ben@benknight.me'

# Add here all kinds of additional classifiers as defined under
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
]

def read_file(name):
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        name
    )
    data = open(filepath)
    try:
        return data.read()
    except IOError:
        print "could not read %r" % name
        data.close()

def setup_package():
    # Some helper variables
    version = VERSION

    install_reqs=[],

    setup(
        name=NAME,
        version=version,
        url=URL,
        description=DESCRIPTION,
        author=AUTHOR,
        author_email=EMAIL,
        license=LICENSE,
        keywords='philips hue light rgb xy',
        packages=setuptools.find_packages(),
        long_description=read_file('README.md'),
        install_requires=install_reqs
    )


if __name__ == '__main__':
    setup_package()
