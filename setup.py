# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
    "configparser==4.0.2 ; python_version < '3'",
    "cryptography>=3.2.1,<46.0.0",
    "pyOpenSSL>=17.5.0,<25.0.0",
    "python-dateutil>=2.5.3,<3.0.0",
    "pytz>=2016.10",
    "circuitbreaker>=1.3.1,<2.0.0; python_version <= '3.6'",
    "circuitbreaker>=1.3.1,<3.0.0; python_version >= '3.7'"
]

setup(
    name="oci",
    url="https://docs.oracle.com/en-us/iaas/tools/python/latest/index.html",
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
