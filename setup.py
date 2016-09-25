import io
import os
import re
from setuptools import setup


def open_relative(*path):
    """
    Opens files in read-only with a fixed utf-8 encoding.

    All locations are relative to this setup.py file.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(here, *path)
    return io.open(filename, mode="r", encoding="utf-8")


with open_relative("oraclebmc", "version.py") as fd:
    version = re.search(
        r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
        fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError("Cannot find version information")

with open_relative("README.rst") as f:
    readme = f.read()

packages = [
    "oraclebmc",
    "oraclebmc.apis",
    "oraclebmc.models"
]

requires = [
    "certifi",
    "httpsig==1.1.2",
    "pycrypto==2.7a1",
    "python-dateutil==2.5.3",
    "requests==2.10.0",
    "six==1.10.0",
]

setup(
    name="oraclebmc",
    version=version,
    description="Oracle Bare Metal Cloud Python SDK",
    long_description=readme,
    author_email="",
    url="",
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    dependency_links=[
        "https://github.com/dlitz/pycrypto/tarball/v2.7a1#egg=pycrypto-2.7a1"
    ]
)
