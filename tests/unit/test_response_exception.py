import oci
import pytest


def test_connection_exception(identity, config):
    identity.base_client.endpoint = 'https://fakeendpoint.oracle'
    with pytest.raises(oci.exceptions.RequestException):
        identity.list_users(config['tenancy'])
