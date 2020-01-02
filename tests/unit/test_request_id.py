# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


def test_core_automatic_request_id(virtual_network, config):
    response = virtual_network.list_vcns(config["tenancy"])
    assert response.status == 200
    assert response.request_id is not None
    assert len(response.request_id.split('/')) == 3
    assert len(response.request_id) == 98


def test_supplied_request_id(load_balancer_client, config):
    my_request_id = load_balancer_client.base_client.build_request_id()
    response = load_balancer_client.list_load_balancers(config['tenancy'], opc_request_id=my_request_id)
    assert response.status == 200
    assert response.request_id is not None
    assert len(response.request_id.split('/')) == 3

    assert my_request_id.lower() in response.request_id.lower()


'''
# Commenting this out until Object Storage updates support for request ID.

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
