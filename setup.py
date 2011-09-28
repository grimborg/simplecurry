#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

curdir = os.path.dirname(os.path.abspath(__file__))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'simplecurry',
    description = 'Curried decorator',
    long_description = read('README.rst'),
    license = 'http://www.gnu.org/licenses/gpl-2.0.html',
    version = '1.11',
    author = 'Òscar Vilaplana',
    author_email = 'dev@oscarvilaplana.cat',
    url = 'https://github.com/grimborg/simplecurry',
    py_modules=['simplecurry'],
    )
