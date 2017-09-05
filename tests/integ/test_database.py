# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from . import util


# basic smoke tests that db service is working, more in depth testing is covered in the CLI
def test_list_db_systems(config, database_client):
    response = database_client.list_db_systems(config['tenancy'])
    assert response.status == 200


def test_list_db_shapes(config, database_client):
    ad = util.availability_domain()
    response = database_client.list_db_system_shapes(ad, config['tenancy'])
    assert response.status == 200
