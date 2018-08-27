# coding: utf-8
# Copyright (c) 2016, 2017 Oracle and/or its affiliates. All rights reserved.

import io
import os
import re
from setuptools import setup, find_packages


def open_relative(*path):
    """
    Opens files in read-only with a fixed utf-8 encoding.

    All locations are relative to this setup.py file.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(here, *path)
    return io.open(filename, mode="r", encoding="utf-8")


with open_relative("src", "oci", "version.py") as fd:
    version = re.search(
        r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
        fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError("Cannot find version information")

with open_relative("README.rst") as f:
    readme = f.read()

requires = [
    "certifi",
    "configparser>=3.5.0b1",
    "cryptography>=2.1.3",
    "pyOpenSSL<=17.4.0",
    "python-dateutil>=2.5.3,<=2.7.3",
    "pytz>=2016.10",
]

setup(
    name="oci",
    url="https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/index.html",
    version=version,
    description="Oracle Cloud Infrastructure Python SDK",
    long_description=readme,
    author="Oracle",
    author_email="joe.levy@oracle.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=requires,
    license="Universal Permissive License 1.0 or Apache License 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: Universal Permissive License (UPL)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
