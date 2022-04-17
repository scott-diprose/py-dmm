# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pydmm',
    version='0.1.0',
    description=
    'Object model for standardising the structure of metadata applicable for mapping from one source data set to a target. Potentially being reshaped during the transfer.',
    long_description=readme,
    author='Scott Diprose',
    author_email='scott.on.github@gmail.com',
    url='https://github.com/scott-diprose/pydmm',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')))
