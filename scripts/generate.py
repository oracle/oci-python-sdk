#!/usr/bin/env python

import os

# This script generates src/oci/__init__.py.  It is called by one of the
# steps in main pom.xml.  It uses the directory listing from the poms
# folder to determine the services that need to be included in
# src/oci/__init__.py

ROOT_INIT_LOCATION = "src/oci/__init__.py"
SOURCE_LOCATION = "poms"

ROOT_INIT_FILE_TEMPLATE = """from . import auth, config, constants, decorators, exceptions, regions, pagination, retry, fips
from .base_client import BaseClient
from .request import Request
from .response import Response
from .signer import Signer
from .version import __version__  # noqa
from .waiter import wait_until
import os

fips.enable_fips_mode()

if os.getenv("OCI_PYTHON_SDK_NO_SERVICE_IMPORTS", "").lower() in ["true", "1"]:
    pass
else:
    from . import {spec_names}

    __all__ = [
        "BaseClient", "Error", "Request", "Response", "Signer", "config", "constants", "decorators", "exceptions", "regions", "wait_until", "pagination", "auth", "retry", "fips",
        {quoted_spec_names}
    ]
"""


def spec_names_as_csv(spec_names):
    sorted_spec_names = sorted(spec_names)
    spec_names_csv = ', '.join(sorted_spec_names)

    return spec_names_csv


def quote_spec_names(spec_names):
    sorted_spec_names = sorted(spec_names)
    quoted_spec_names = ', '.join(['"{}"'.format(spec_name) for spec_name in sorted_spec_names])

    return quoted_spec_names


def write_root_init_file():
    spec_names = []
    for item in os.listdir(SOURCE_LOCATION):
        path = os.path.join(SOURCE_LOCATION, item)
        if os.path.isdir(path):
            spec_names.append(item)

    spec_names_csv = spec_names_as_csv(spec_names)
    spec_names_quoted = quote_spec_names(spec_names)

    # print(spec_names_csv)
    # print(spec_names_quoted)

    with open(ROOT_INIT_LOCATION, 'w+') as f:
        content = ROOT_INIT_FILE_TEMPLATE.format(spec_names=spec_names_csv, quoted_spec_names=spec_names_quoted)
        f.write(content)


write_root_init_file()
