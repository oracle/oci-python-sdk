import oraclebmc
import pytest
import tests.util


def test_invalid_compartment(identity):

    with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
        identity.list_users('invalid_compartment')
    assert excinfo.value.status == 403
    assert excinfo.value.headers is not None
    assert type(excinfo.value.data) is oraclebmc.models.Error


def test_invalid_endpoint_host():
    config = oraclebmc.config.from_file(
        file_location=tests.util.get_resource_path('config'),
        profile_name="DEFAULT"
    )
    client = oraclebmc.clients.IdentityClient(config)
    client.base_client.endpoints["identity"] = "https://identity.us-phoenix-999999.oraclecloud.com/v1"

    with pytest.raises(Exception):
        client.list_users('invalid_compartment')
