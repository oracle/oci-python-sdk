# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from . import util
from oci._vendor import six


# basic smoke tests that db service is working, more in depth testing is covered in the CLI
def test_list_db_systems(config, database_client):
    response = database_client.list_db_systems(config['tenancy'])
    assert response.status == 200


def test_list_db_shapes(config, database_client):
    ad = util.availability_domain()
    response = database_client.list_db_system_shapes(ad, config['tenancy'])
    assert response.status == 200
    assert len(response.data) > 0
    for db_system_shape_summary in response.data:
        for attribute_name in six.iterkeys(db_system_shape_summary.swagger_types):
            # It is possible for core_count_increment to be 0, so a straight assertion on
            # getattr would not work
            assert getattr(db_system_shape_summary, attribute_name) is not None
