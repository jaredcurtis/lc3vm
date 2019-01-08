#!/bin/env python

"""Setup for lc3vm"""

from setuptools import setup, find_packages

setup(
    name="lc3vm",
    description="Virtual Machine for LC3 architecture",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    tests_require=["unittest2"],
)
