# TODO (jmcross) disabled for initial release (identity, object_storage only)
# def test_core_automatic_request_id(virtual_network, config):
#     response = virtual_network.list_vcns(config["tenancy"])
#     assert response.status == 200
#     assert response.request_id is not None
#     assert len(response.request_id.split('/')) == 3
#     assert len(response.request_id) == 98


'''
# Commenting this out until Casper updates support for request ID.

def test_object_storage_request_id(object_storage):
    request_id = 'example_request_id_1234'
    response = object_storage.get_namespace(opc_client_request_id=request_id)
    assert response.status == 200
    assert response.request_id is not None
    assert 3 == len(response.request_id.split('/'))
    assert request_id in response.request_id


def test_object_storage_automatic_request_id(object_storage):
    response = object_storage.get_namespace()
    assert response.status == 200
    assert response.request_id is not None
    assert 3 == len(response.request_id.split('/'))
'''
