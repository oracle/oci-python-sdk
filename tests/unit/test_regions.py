# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import pytest

from oci.regions import endpoint_for, get_region_from_short_name, get_realm_from_region, is_region, is_region_short_name, REGIONS_SHORT_NAMES, REGIONS, REGION_REALMS, REALMS, _has_been_read_external_sources, ExternalSources
from oci._vendor import six


def reset_external_sources_dict():
    _has_been_read_external_sources[ExternalSources.REGIONS_CFG_FILE] = False
    _has_been_read_external_sources[ExternalSources.ENV_VAR] = False
    _has_been_read_external_sources[ExternalSources.IMDS] = True


def test_endpoint_for_service_template():
    reset_external_sources_dict()
    # set region template
    endpoint = endpoint_for('blockstorage', 'foo_region', None, 'https://{region}.bar.com')
    assert endpoint == 'https://foo_region.bar.com'

    # no template
    endpoint = endpoint_for('blockstorage', 'us-foo_region-1', None, None)
    assert endpoint == 'https://iaas.us-foo_region-1.oraclecloud.com'

    # second level domain template with unknown region
    endpoint = endpoint_for('blockstorage', 'us-foo_region-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclecloud.com'

    # second level domain template with oc1 region
    endpoint = endpoint_for('blockstorage', 'us-phoenix-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclecloud.com'

    # second level domain template with oc2 region
    endpoint = endpoint_for('blockstorage', 'us-langley-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclegovcloud.com'

    # second level domain template with oc3 region
    endpoint = endpoint_for('blockstorage', 'us-gov-ashburn-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclegovcloud.com'


def test_endpoint_for_endpoint():
    reset_external_sources_dict()
    # only endpoint set
    endpoint = endpoint_for('compute', None, 'endpoint', None)
    assert endpoint == 'https://iaas.endpoint'

    # both endpoint and region set, then endpoint should take over
    endpoint = endpoint_for('compute', 'us-foo_region-1', 'endpoint', None)
    assert endpoint == 'https://iaas.endpoint'


def test_endpoint_for_region():
    reset_external_sources_dict()
    # oc1
    endpoint = endpoint_for('compute', 'us-phoenix-1', None, None)
    assert endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com'

    # oc2
    endpoint = endpoint_for('compute', 'us-langley-1', None, None)
    assert endpoint == 'https://iaas.us-langley-1.oraclegovcloud.com'

    # oc3
    endpoint = endpoint_for('compute', 'us-gov-ashburn-1', None, None)
    assert endpoint == 'https://iaas.us-gov-ashburn-1.oraclegovcloud.com'

    # region contains dot
    endpoint = endpoint_for('compute', '.us-phoenix-1', 'test.com', None)
    assert endpoint == 'https://iaas.test.com'

    endpoint = endpoint_for('compute', 'us-phoenix-1.oraclecloud.com', None, None)
    assert endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com'

    # Unknown region should fall back to OC1 realm
    endpoint = endpoint_for('compute', 'abc', None, None)
    assert endpoint == 'https://iaas.abc.oraclecloud.com'

    # Support short codes
    endpoint = endpoint_for('compute', 'phx', None, None)
    assert endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com'


def test_short_name_to_region():
    reset_external_sources_dict()
    for shortname in six.iterkeys(REGIONS_SHORT_NAMES):
        assert(REGIONS_SHORT_NAMES[shortname] in REGIONS)


def test_short_name_to_realm():
    reset_external_sources_dict()
    for shortname in six.iterkeys(REGIONS_SHORT_NAMES):
        assert(REGIONS_SHORT_NAMES[shortname] in REGION_REALMS)


def test_region_to_realm():
    reset_external_sources_dict()
    for region in REGIONS:
        assert(region in REGION_REALMS)
        assert(REGION_REALMS[region] in REALMS)


def test_region_from_env_variable():
    reset_external_sources_dict()

    # Normal case
    os.environ['OCI_REGION_METADATA'] = '{"realmKey" : "OC100", "realmDomainComponent" : "oc100.com", "regionKey" : "XYZ1", "regionIdentifier" : "test-region-1"}'
    endpoint = endpoint_for('compute', 'test-region-1', None, None)
    assert endpoint == 'https://iaas.test-region-1.oc100.com'

    reset_external_sources_dict()

    # Normal case with short code
    os.environ['OCI_REGION_METADATA'] = '{"realmKey" : "OC200", "realmDomainComponent" : "oc200.com", "regionKey" : "XYZ2", "regionIdentifier" : "test-region-2"}'
    endpoint = endpoint_for('compute', 'XYZ2', None, None)
    assert endpoint == 'https://iaas.test-region-2.oc200.com'

    reset_external_sources_dict()

    # If env variable is not well-formed then logic should fall back to OC1 - NOTE - This is assuming we don't get info from instance metadata
    os.environ['OCI_REGION_METADATA'] = '{"test": "test"}'
    endpoint = endpoint_for('compute', 'test', None, None)
    assert endpoint == 'https://iaas.test.oraclecloud.com'

    reset_external_sources_dict()

    # Missing keys should default to OC1 - NOTE - This is assuming we don't get info from instance metadata
    os.environ['OCI_REGION_METADATA'] = '{"realmKey" : "OC300", "realmDomainComponent" : "", "regionKey" : "XYZ3", "regionIdentifier" : "test-region-3"}'
    endpoint = endpoint_for('compute', 'test-region-3', None, None)
    assert endpoint == 'https://iaas.test-region-3.oraclecloud.com'

    reset_external_sources_dict()

    # Invalid JSON defaults to OC1 - NOTE - This is assuming we don't get info from instance metadata
    os.environ['OCI_REGION_METADATA'] = '{"realmKey" : "OC400", "realmDomainComponent" : "oc400.com", "regionKey" : "XYZ4", "regionIdentifier" : "test-region-4"'
    endpoint = endpoint_for('compute', 'test-region-4', None, None)
    assert endpoint == 'https://iaas.test-region-4.oraclecloud.com'

    reset_external_sources_dict()

    # Test region metadata is added even if that region is not requested, and falls back to OC1 - NOTE - This is assuming we don't get info from instance metadata
    os.environ['OCI_REGION_METADATA'] = '{"realmKey" : "OC500", "realmDomainComponent" : "oc500.com", "regionKey" : "XYZ5", "regionIdentifier" : "test-region-5"}'
    endpoint = endpoint_for('compute', 'garbage', None, None)
    assert endpoint == 'https://iaas.garbage.oraclecloud.com'
    assert "xyz5" in REGIONS_SHORT_NAMES
    assert "test-region-5" in REGIONS
    assert "oc500" in REALMS
    assert "test-region-5" in REGION_REALMS

    # Cleanup
    del os.environ['OCI_REGION_METADATA']
    reset_external_sources_dict()


def test_regions_config_file():
    regions_configuration_file_content = """[
    {
        "realmKey" : "OC700",
        "realmDomainComponent" : "oc700.com",
        "regionKey" : "xyz7",
        "regionIdentifier" : "test-region-7"
    },
    {
        "realmKey" : "",
        "realmDomainComponent" : "oc800.com",
        "regionKey" : "xyz8",
        "regionIdentifier" : "test-region-8"
    },
    {
        "regionKey" : "xyz8",
        "regionIdentifier" : "test-region-8"
    },
    {}
]
"""
    regions_file_path = os.path.join('~', '.oci')
    regions_file_location = os.path.join('~', '.oci', 'regions-config.json')
    expanded_file_path = os.path.expanduser(regions_file_path)
    expanded_file_location = os.path.expanduser(regions_file_location)

    # Check if .oci folder exists
    if not os.path.isdir(expanded_file_path):
        # Try to create directory
        try:
            os.mkdir(expanded_file_path, 0o777)
        except (OSError, IOError) as e:
            pytest.fail("Cannot create .oci directory in home folder: {}".format(e))

    try:
        with open(expanded_file_location, 'w') as regions_config_file:
            regions_config_file.write(regions_configuration_file_content)
        os.chmod(expanded_file_location, 0o644)
    except (OSError, IOError) as e:
        pytest.fail("Failed to write regions-config.json file: {}".format(e))

    # Normal Case
    endpoint = endpoint_for('compute', 'test-region-7', None, None)
    assert endpoint == 'https://iaas.test-region-7.oc700.com'

    reset_external_sources_dict()

    # Malformed JSON falls back to OC1
    endpoint = endpoint_for('compute', 'test-region-8', None, None)
    assert endpoint == 'https://iaas.test-region-8.oraclecloud.com'

    reset_external_sources_dict()

    # Check fallback to env variable
    os.environ['OCI_REGION_METADATA'] = '{"realmKey" : "OC800", "realmDomainComponent" : "oc800.com", "regionKey" : "XYZ8", "regionIdentifier" : "test-region-8"}'
    endpoint = endpoint_for('compute', 'test-region-8', None, None)
    assert endpoint == 'https://iaas.test-region-8.oc800.com'

    reset_external_sources_dict()


def test_getters():
    # Normal case
    assert is_region("us-phoenix-1")
    assert is_region_short_name("phx")

    assert not is_region("test-region-6")
    assert not is_region("xyz6")

    reset_external_sources_dict()
    os.environ['OCI_REGION_METADATA'] = '{"realmKey" : "OC600", "realmDomainComponent" : "oc600.com", "regionKey" : "XYZ6", "regionIdentifier" : "test-region-6"}'
    assert is_region("test-region-6")
    assert is_region_short_name("xyz6")

    long_code = get_region_from_short_name("xyz6")
    assert long_code == "test-region-6"

    long_code = get_region_from_short_name("phx")
    assert long_code == "us-phoenix-1"

    # Handle long code
    long_code = get_region_from_short_name("us-phoenix-1")
    assert long_code == "us-phoenix-1"

    # Handle unknown
    long_code = get_region_from_short_name("garbage")
    assert long_code == "garbage"

    # Test Realm
    realm = get_realm_from_region("us-langley-1")
    assert realm == "oc2"

    # Short code
    realm = get_realm_from_region("lhr")
    assert realm == "oc1"

    # Unknown should default to oc1
    realm = get_realm_from_region("garbage")
    assert realm == "oc1"

    realm = get_realm_from_region("test-region-6")
    assert realm == "oc600"

    realm = get_realm_from_region("xyz6")
    assert realm == "oc600"
