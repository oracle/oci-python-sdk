# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "oraclebmi"
VERSION = "0.0.1"

REQUIRES = ['certifi',
            'httpsig >= 1.1.2',
            'six >= 1.9',
            'urllib3 >= 1.10',
            'python-dateutil >= 2.0',
            'requests >= 2.7.0']

setup(
    name=NAME,
    version=VERSION,
    description="Oracle Bare Metal IaaS Python SDK",
    author_email="",
    url="",
    keywords=[""],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the Public Python SDK for the Oracle Bare Metal IaaS.
    """
)


