#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

curdir = os.path.dirname(os.path.abspath(__file__))

setup(
    name = 'simplecurry',
    description = 'Curried decorator',
    license = 'gplv2',
    version = '1.1',
    author = 'Òscar Vilaplana',
    author_email = 'dev@oscarvilaplana.cat',
    url = 'https://github.com/grimborg/simplecurry',
    py_modules=['simplecurry'],
    )
