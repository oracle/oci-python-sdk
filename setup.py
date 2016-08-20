# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "oraclebmc"
VERSION = "0.0.1"

REQUIRES = ['certifi==2016.2.28',
            'httpsig==1.1.2',
            'pycrypto==2.6.1',
            'python-dateutil==2.5.3',
            'requests==2.10.0',
            'six==1.10.0',
            'urllib3==1.16']

setup(
    name=NAME,
    version=VERSION,
    description="Oracle Bare Metal Cloud Python SDK",
    author_email="",
    url="",
    keywords=[""],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the Public Python SDK for the Oracle Bare Metal Cloud.
    """
)


