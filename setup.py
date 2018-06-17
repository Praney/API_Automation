from setuptools import setup, find_packages
from os import path
setup(name = 'runtastic-test',
version = '1.0',
description = 'Test Strategry for Runtastic',
author = 'Praney Madan',
packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
