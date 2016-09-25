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
    api = oraclebmc.config_file_loader.load_config(
        file_location=tests.util.get_resource_path('config'),
        profile_name="INVALID_ENDPOINT_HOST"
    )

    with pytest.raises(Exception):
        api.list_users('invalid_compartment')
