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
    "oraclebmc.clients",
    "oraclebmc.models"
]

requires = [
    "certifi",
    "configparser==3.5.0",
    "cryptography==1.5.2",
    "httpsig_cffi==15.0.0",
    "python-dateutil==2.5.3",
    "requests==2.11.1",
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
)
