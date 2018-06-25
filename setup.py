#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from setuptools import find_packages, setup

requirements = [line.strip() for line in open('requirements.txt', 'r').readlines()]
version      = '0.13'

if os.path.isfile('VERSION'):
    version = open('VERSION', 'r').readline().strip() or version

setup(
    name                = 'botbond',
    version             = version,
    description         = 'botbond',
    author              = 'Adrien Delle Cave',
    author_email        = 'pypi@doowan.net',
    license             = 'License GPL-2',
    url                 = 'https://github.com/decryptus/botbond',
    scripts             = ['bin/botbond'],
    packages		= find_packages(),
    install_requires    = requirements
)
