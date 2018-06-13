# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from . import util
from .. import test_config_container

# basic smoke tests for the container engine client and service.
def test_list_clusters(config, container_engine):
    with test_config_container.create_vcr().use_cassette('test_container_engine_list_clusters.yml'):
        response = container_engine.list_clusters(config['tenancy'])
        assert response.status == 200

def test_list_node_pools(config, container_engine):
    with test_config_container.create_vcr().use_cassette('test_container_engine_list_node_pools.yml'):
        response = container_engine.list_node_pools(config['tenancy'])
        assert response.status == 200

def test_list_work_requests(config, container_engine):
    with test_config_container.create_vcr().use_cassette('test_container_engine_list_work_requests.yml'):
        response = container_engine.list_work_requests(config['tenancy'])
        assert response.status == 200