import oraclebmc
import pytest
import tests.util


def test_invalid_compartment(identity):
    with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
        identity.list_users('invalid_compartment')
    tests.util.validate_service_error(excinfo.value, 403, "NotAllowed", "Operation not allowed")


def test_invalid_policy(identity, config):
    request = oraclebmc.identity.models.CreatePolicyDetails()
    request.compartment_id = config["tenancy"]
    request.name = 'invalid_policy'
    request.description = 'create should fail'
    request.statements = ['ALLOW group NotARealGroup inspect all-resources ON TENANCY']

    with pytest.raises(oraclebmc.exceptions.ServiceError) as excinfo:
        identity.create_policy(request)

    tests.util.validate_service_error(excinfo.value, 400, "InvalidParameter", "The group/compartment specified")


def test_invalid_endpoint_host():
    config = oraclebmc.config.from_file(
        file_location=tests.util.get_resource_path('config'),
        profile_name="DEFAULT"
    )
    client = oraclebmc.identity.IdentityClient(config)
    client.base_client.endpoint = "https://identity.us-phoenix-999999.oraclecloud.com/v1"

    with pytest.raises(Exception):
        client.list_users('invalid_compartment')
