#!/usr/bin/env python

#
# This script handles generating parts of the code that rely on *all* of the specs.
# This is outside the scope of the codegen plugin which is invoked once per spec / service.
#

import xml.etree.ElementTree as ET
import re
import six

POM_LOCATION = "pom.xml"
ROOT_INIT_LOCATION = "src/oci/__init__.py"
SERVICE_ENDPOINTS_FILE_LOCATION = "src/oci/service_endpoints.py"

endpoints = {
    "ambassador": "https://orchestration.{domain}/20170630",
    "audit": "https://audit.{domain}/20160918",
    "blockstorage": "https://iaas.{domain}/20160918",
    "compute": "https://iaas.{domain}/20160918",
    "database": "https://database.{domain}/20160918",
    "identity": "https://identity.{domain}/20160918",
    "load_balancer": "https://iaas.{domain}/20170115",
    "orchestration": "https://orchestration.{domain}/20170630",
    "object_storage": "https://objectstorage.{domain}",
    "virtual_network": "https://iaas.{domain}/20160918"
}

ROOT_INIT_FILE_TEMPLATE = """
from . import {spec_names}
from . import config, constants, decorators, exceptions, regions
from .base_client import BaseClient
from .request import Request
from .response import Response
from .signer import Signer
from .version import __version__  # noqa
from .waiter import wait_until


__all__ = [
    "BaseClient", "Error", "Request", "Response", "Signer", "config", "constants", "decorators", "exceptions", "regions", "wait_until",
    {spec_names}
]
"""

SERVICE_ENDPOINTS_TEMPLATE = """
# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

SERVICE_ENDPOINTS = {{
    {endpoints}
}}
"""

def parse_pom():
    with open(POM_LOCATION) as f:
        xmlstring = f.read()

    # Remove the default namespace definition (xmlns="http://some/namespace")
    # Otherwise for every 'iter' or 'find' we need to specify namespace
    xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)

    return ET.fromstring(xmlstring) 


def get_spec_names(pom):
    # read specName from each execution of bmc-sdk-swagger-maven-plugin
    spec_names = []
    for execution in pom.iter('execution'):
        # in each execution find the specName
        for spec_name in execution.iter('specName'):
            spec_names.append(spec_name.text)
        
    spec_names.sort()
    return spec_names


def write_root_init_file(spec_names):
    spec_names_csv = ', '.join(spec_names)
    with open(ROOT_INIT_LOCATION, 'w+') as f:
        content = ROOT_INIT_FILE_TEMPLATE.format(spec_names=spec_names_csv)
        f.write(content)


def write_regions_file(endpoints):
    entries = []
    entry_format = '"{spec_name}": "{endpoint}"'
    services = sorted(endpoints, key=endpoints.get)
    for service in services:
        entries.append(entry_format.format(spec_name=service, endpoint=endpoints[service]))
    
    content = ",\n    ".join(entries)

    with open(SERVICE_ENDPOINTS_FILE_LOCATION, 'w+') as f:
        content = SERVICE_ENDPOINTS_TEMPLATE.format(endpoints=content)
        f.write(content)


pom = parse_pom()
spec_names = get_spec_names(pom)
write_root_init_file(spec_names)
write_regions_file(endpoints)
