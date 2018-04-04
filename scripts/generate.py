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

# this is to support specs that contain multiple services
SPECS_TO_SERVICES = {
    "core": ["blockstorage", "compute", "virtual_network"],
    "key_management": ["kms_crypto", "kms_provisioning", "kms_vault"]
}

ROOT_INIT_FILE_TEMPLATE = """from . import {spec_names}
from . import auth, config, constants, decorators, exceptions, regions, pagination, retry
from .base_client import BaseClient
from .request import Request
from .response import Response
from .signer import Signer
from .version import __version__  # noqa
from .waiter import wait_until


__all__ = [
    "BaseClient", "Error", "Request", "Response", "Signer", "config", "constants", "decorators", "exceptions", "regions", "wait_until", "pagination", "auth", "retry",
    {quoted_spec_names}
]
"""

SERVICE_ENDPOINTS_TEMPLATE = """SERVICE_ENDPOINTS = {{
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


def get_spec_to_endpoint_map(pom):
    # read specName from each execution of bmc-sdk-swagger-maven-plugin
    specs = {}
    generate_plugin_executions = pom.findall(".//plugin[artifactId='bmc-sdk-swagger-maven-plugin']/executions")[0]
    # specName and endpoint will be in the same additionalProperties node
    for additional_properties in generate_plugin_executions.iter('additionalProperties'):
        spec_name = additional_properties.find('specName').text
        endpoint = additional_properties.find('endpoint').text
        specs[spec_name] = endpoint

    return specs


def write_root_init_file(spec_to_endpoint):
    sorted_spec_names = sorted(spec_to_endpoint)
    quoted_spec_names = ['"{}"'.format(spec_name) for spec_name in sorted_spec_names]
    spec_names_csv = ', '.join(sorted_spec_names)
    quoted_spec_names_csv = ', '.join(quoted_spec_names)
    with open(ROOT_INIT_LOCATION, 'w+') as f:
        content = ROOT_INIT_FILE_TEMPLATE.format(spec_names=spec_names_csv, quoted_spec_names=quoted_spec_names_csv)
        f.write(content)


def write_regions_file(spec_to_endpoint):
    entries = []
    entry_format = '"{spec_name}": "{endpoint}"'
    spec_names = sorted(spec_to_endpoint)
    for spec_name in spec_names:
        if spec_name in SPECS_TO_SERVICES:
            for service in SPECS_TO_SERVICES[spec_name]:
                # the endpoint is specified per spec, so give all serices in that spec the same endpoint
                entries.append(entry_format.format(spec_name=service, endpoint=spec_to_endpoint[spec_name]))
        else:
            entries.append(entry_format.format(spec_name=spec_name, endpoint=spec_to_endpoint[spec_name]))
    
    content = ",\n    ".join(entries)

    with open(SERVICE_ENDPOINTS_FILE_LOCATION, 'w+') as f:
        content = SERVICE_ENDPOINTS_TEMPLATE.format(endpoints=content)
        f.write(content)


pom = parse_pom()
spec_to_endpoint = get_spec_to_endpoint_map(pom)
write_root_init_file(spec_to_endpoint)
write_regions_file(spec_to_endpoint)
