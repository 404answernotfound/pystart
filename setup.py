# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Pystart',
    version='0.1.0',
    description='Welcome to my Python Starter, based on the book "A hitchhiker\'s guide to Python"',
    long_description=readme,
    author='Lorenzo Pieri',
    author_email='-',
    url='https://github.com/404anwernotfound/pystart',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

