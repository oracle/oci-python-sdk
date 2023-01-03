# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import os
import pytest

from oci.regions import endpoint_for, get_region_from_short_name, get_realm_from_region, is_region, is_region_short_name, REGIONS_SHORT_NAMES, REGIONS, REGION_REALMS, REALMS, _has_been_read_external_sources, ExternalSources
from oci._vendor import six
from oci.core import BlockstorageClient, ComputeClient
from oci.identity import IdentityClient
from oci.analytics import AnalyticsClient


def reset_external_sources_dict():
    _has_been_read_external_sources[ExternalSources.REGIONS_CFG_FILE] = False
    _has_been_read_external_sources[ExternalSources.ENV_VAR] = False
    _has_been_read_external_sources[ExternalSources.IMDS] = True
    _has_been_read_external_sources[ExternalSources.SECOND_LEVEL_DOMAIN_FALLBACK] = False


def test_realm_fallback():
    reset_external_sources_dict()

    # Test if fallback  goes back to OC1 if env.OCI_DEFAULT_REALM was not set
    endpoint = endpoint_for('compute', 'dummy-region', None, None)
    assert endpoint == 'https://iaas.dummy-region.oraclecloud.com'
    reset_external_sources_dict()

    # Test - Fallback should go to the second level domain as defined in env.OCI_DEFAULT_REALM if region is not found
    os.environ['OCI_DEFAULT_REALM'] = 'fallbacksecondleveldomain.com'
    endpoint = endpoint_for('compute', 'dummy-region', None, None)
    assert endpoint == 'https://iaas.dummy-region.fallbacksecondleveldomain.com'

    # Cleanup
    del os.environ['OCI_DEFAULT_REALM']
    reset_external_sources_dict()


def test_all_regions():
    try:
        with open('tests/resources/regions.json', 'r') as f:
            regions_raw = f.read()
    except (OSError, IOError) as e:
        pytest.fail("Reading regions configuration file failed because of error: {}".format(e))

    # Try importing JSONDecodeError for Python 2 and Python 3 compatibility
    try:
        from json.decoder import JSONDecodeError
    except ImportError:
        JSONDecodeError = ValueError
    try:
        regions = json.loads(regions_raw)
    except JSONDecodeError as e:
        # Unable to parse the json array
        pytest.fail("Decoding JSON array from regions configuration file failed because of error: {}".format(e))

    for region in regions:
        assert (region['regionIdentifier'] in REGIONS)
        assert (region['realmKey'] in REALMS.keys())


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

    # second level domain template with oc4 region
    endpoint = endpoint_for('blockstorage', 'uk-gov-london-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclegovcloud.uk'

    # Same for a service not in service_endpoints.py
    # set region template
    endpoint = endpoint_for('analytics', 'foo_region', None, 'https://{region}.bar.com')
    assert endpoint == 'https://foo_region.bar.com'

    # no template
    try:
        endpoint = endpoint_for('analytics', 'us-foo_region-1', None, None)
        assert False  # this should have failed
    except ValueError:
        pass

    # second level domain template with unknown region
    endpoint = endpoint_for('analytics', 'us-foo_region-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclecloud.com'

    # second level domain template with oc1 region
    endpoint = endpoint_for('analytics', 'us-phoenix-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclecloud.com'

    # second level domain template with oc2 region
    endpoint = endpoint_for('analytics', 'us-langley-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclegovcloud.com'

    # second level domain template with oc3 region
    endpoint = endpoint_for('analytics', 'us-gov-ashburn-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclegovcloud.com'

    # second level domain template with oc4 region
    endpoint = endpoint_for('analytics', 'uk-gov-london-1', None, 'https://test.{secondLevelDomain}')
    assert endpoint == 'https://test.oraclegovcloud.uk'


def test_endpoint_for_dot_in_region_with_endpoint_service_name():
    reset_external_sources_dict()
    # set region template
    endpoint = endpoint_for('blockstorage', 'some.customerdomain.com', None, 'https://{region}.bar.com', 'iaas')
    assert endpoint == 'https://iaas.some.customerdomain.com'

    # no template
    endpoint = endpoint_for('blockstorage', 'some.customerdomain.com', None, None, 'iaas')
    assert endpoint == 'https://iaas.some.customerdomain.com'

    service = 'compute'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, None, 'iaas')
    assert endpoint == 'https://iaas.broom6.us.oracle.com'

    service = 'identity'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, None, 'identity')
    assert endpoint == 'https://identity.broom6.us.oracle.com'

    service = 'identity'
    region = 'broom6.us.oracle.com'
    endpoint_input = 'something.completely.different'
    endpoint = endpoint_for(service, region, endpoint_input, None, 'identity')
    assert endpoint == 'https://identity.something.completely.different'

    service = 'identity'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, None, 'iam')
    assert endpoint == 'https://iam.broom6.us.oracle.com'

    # Same for a service not in service_endpoints.py
    # set region template
    endpoint = endpoint_for('analytics', 'some.customerdomain.com', None, 'https://{region}.bar.com', 'analytics')
    assert endpoint == 'https://analytics.some.customerdomain.com'

    # no template
    endpoint = endpoint_for('analytics', 'some.customerdomain.com', None, None, 'analytics')
    assert endpoint == 'https://analytics.some.customerdomain.com'

    service = 'analytics'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, None, 'analytics')
    assert endpoint == 'https://analytics.broom6.us.oracle.com'

    service = 'analytics'
    region = 'broom6.us.oracle.com'
    endpoint_input = 'something.completely.different'
    endpoint = endpoint_for(service, region, endpoint_input, None, 'analytics')
    assert endpoint == 'https://analytics.something.completely.different'

    service = 'analytics'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, None, 'ml')
    assert endpoint == 'https://ml.broom6.us.oracle.com'


def test_endpoint_for_dot_in_region_and_no_endpoint_service_name():
    reset_external_sources_dict()
    # set region template
    endpoint = endpoint_for('blockstorage', 'some.customerdomain.com', None, 'https://iaas.{region}.{secondLevelDomain}', None)
    assert endpoint == 'https://iaas.some.customerdomain.com'

    # no template
    endpoint = endpoint_for('blockstorage', 'some.customerdomain.com', None, None, None)
    assert endpoint == 'https://iaas.some.customerdomain.com'

    service = 'compute'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, 'https://iaas.{region}.{secondLevelDomain}', None)
    assert endpoint == 'https://iaas.broom6.us.oracle.com'

    service = 'identity'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, 'https://identity.{region}.oci.{secondLevelDomain}', None)
    assert endpoint == 'https://identity.broom6.us.oracle.com'

    service = 'identity'
    region = 'broom6.us.oracle.com'
    endpoint_input = 'something.completely.different'
    endpoint = endpoint_for(service, region, endpoint_input, 'https://identity.{region}.oci.{secondLevelDomain}', None)
    assert endpoint == 'https://identity.something.completely.different'

    service = 'identity'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, 'https://identity.{region}.oci.{secondLevelDomain}', None)
    assert endpoint == 'https://identity.broom6.us.oracle.com'

    # Same for a service not in service_endpoints.py
    # set region template
    endpoint = endpoint_for('analytics', 'some.customerdomain.com', None, 'https://analytics.{region}.{secondLevelDomain}', None)
    assert endpoint == 'https://analytics.some.customerdomain.com'

    # no template
    try:
        endpoint = endpoint_for('analytics', 'some.customerdomain.com', None, None, None)
        assert False  # should have failed; we have no endpoint template, and no endpoint service name
    except ValueError:
        pass

    service = 'analytics'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, 'https://analytics.{region}.{secondLevelDomain}', None)
    assert endpoint == 'https://analytics.broom6.us.oracle.com'

    service = 'analytics'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, 'https://analytics.{region}.oci.{secondLevelDomain}', None)
    assert endpoint == 'https://analytics.broom6.us.oracle.com'

    service = 'analytics'
    region = 'broom6.us.oracle.com'
    endpoint_input = 'something.completely.different'
    endpoint = endpoint_for(service, region, endpoint_input, 'https://analytics.{region}.oci.{secondLevelDomain}', None)
    assert endpoint == 'https://analytics.something.completely.different'


def test_endpoint_for_dot_in_region_and_both_endpoint_template_and_endpoint_service_name():
    reset_external_sources_dict()
    service = 'identity'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, 'https://identity.{region}.oci.{secondLevelDomain}', 'iam')
    assert endpoint == 'https://iam.broom6.us.oracle.com'

    # Same for a service not in service_endpoints.py
    service = 'analytics'
    region = 'broom6.us.oracle.com'
    endpoint = endpoint_for(service, region, None, 'https://analytics.{region}.oci.{secondLevelDomain}', 'analytics')
    assert endpoint == 'https://analytics.broom6.us.oracle.com'


def test_endpoint_for_dot_in_region_real_client():
    config = {
        'log_requests': True,
        'user': 'ocid1.user.oc1..abc',
        'fingerprint': '01:23:45:67:89:ab:cd:ef:01:23:45:67:89:ab:cd:ef',
        'key_file': 'keys/no_permissions_unencrypted_key.pem',
        'tenancy': 'ocid1.tenancy.oc1..abc',
        'region': 'us-phoenix-1'
    }

    config_dotted_region = config.copy()
    config_dotted_region['region'] = "broom6.us.oracle.com"

    client = IdentityClient(config)
    assert client.base_client.endpoint == 'https://identity.us-phoenix-1.oci.oraclecloud.com/20160918'

    client = ComputeClient(config)
    assert client.base_client.endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com/20160918'

    client = BlockstorageClient(config)
    assert client.base_client.endpoint == 'https://iaas.us-phoenix-1.oraclecloud.com/20160918'

    client = AnalyticsClient(config)
    assert client.base_client.endpoint == 'https://analytics.us-phoenix-1.ocp.oraclecloud.com/20190331'

    client = IdentityClient(config_dotted_region)
    assert client.base_client.endpoint == 'https://identity.broom6.us.oracle.com/20160918'

    client = ComputeClient(config_dotted_region)
    assert client.base_client.endpoint == 'https://iaas.broom6.us.oracle.com/20160918'

    client = BlockstorageClient(config_dotted_region)
    assert client.base_client.endpoint == 'https://iaas.broom6.us.oracle.com/20160918'

    client = AnalyticsClient(config_dotted_region)
    assert client.base_client.endpoint == 'https://analytics.broom6.us.oracle.com/20190331'


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
        assert (REGIONS_SHORT_NAMES[shortname] in REGIONS)


def test_short_name_to_realm():
    reset_external_sources_dict()
    for shortname in six.iterkeys(REGIONS_SHORT_NAMES):
        assert (REGIONS_SHORT_NAMES[shortname] in REGION_REALMS)


def test_region_to_realm():
    reset_external_sources_dict()
    for region in REGIONS:
        assert (region in REGION_REALMS)
        assert (REGION_REALMS[region] in REALMS)


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
