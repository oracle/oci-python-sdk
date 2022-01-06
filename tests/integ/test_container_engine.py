# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
