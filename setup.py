#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
  name='gustavo',
  version='0.0.1',
  description='A simple hello world installable package',
  url='git@github.com:eguezgustavo/gustavo_installable.git',
  author='Gustavo Eguez',
  author_email='eguezgustavo@gmail.com',
  packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
  license='LICENSE.txt',

  
  author='Raphael Schubert',
  author_email='raphael.schubert@digitalbankscorp.com',
  license='unlicense',
  packages=['ptolemaios'],
  zip_safe=False
)
