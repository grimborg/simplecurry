#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

curdir = os.path.dirname(os.path.abspath(__file__))

setup(
    name = 'simplecurry',
    description = 'Curried decorator',
    license = 'gplv2',
    version = '1.0',
    author = 'Òscar Vilaplana',
    author_email = 'dev@oscarvilaplana.cat',
    url = '',
    packages=find_packages(curdir),
    )
