# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
import pytest
from oci._vendor import six


@pytest.fixture
def base_client(config):
    return oci.BaseClient(
        service='compute',
        config=config,
        signer=None,
        type_mapping={}
    )


def test_process_query_params(base_client):
    raw_query_params = {
        'stuff': 'things',
        'numStuff': 55,
        'collectionFormat': ['hello', 'world'],
        'definedTags': {'tag1': ['val1', 'val2', 'val3'], "tag2": ['val1']},
        'definedTagsExists': {'tag3': True, 'tag4': True}
    }

    expected_query_params = {
        'stuff': 'things',
        'numStuff': '55',
        'collectionFormat': ['hello', 'world'],
        'definedTags.tag1': ['val1', 'val2', 'val3'],
        'definedTags.tag2': ['val1'],
        'definedTagsExists.tag3': True,
        'definedTagsExists.tag4': True,
    }

    assert expected_query_params == base_client.process_query_params(raw_query_params)


def test_generate_collection_format_param_missing(base_client):
    missing = oci.util.Sentinel("Missing")
    assert base_client.generate_collection_format_param(missing, 'csv') is missing


def test_generate_collection_format_none_format(base_client):
    with pytest.raises(ValueError):
        base_client.generate_collection_format_param(['one', 'two'], None)


def test_generate_collection_format_unknown_format(base_client):
    with pytest.raises(ValueError):
        base_client.generate_collection_format_param(['one', 'two'], 'unknown')


def test_generate_collection_format_single_value(base_client):
    for key in six.iterkeys(oci.base_client.VALID_COLLECTION_FORMAT_TYPES):
        if key == 'multi':
            assert ['single'] == base_client.generate_collection_format_param(['single'], key)
        else:
            assert 'single' == base_client.generate_collection_format_param(['single'], key)


def test_generate_collection_format_multiple_values(base_client):
    for key in six.iterkeys(oci.base_client.VALID_COLLECTION_FORMAT_TYPES):
        if key == 'multi':
            assert ['entryOne', 'two'] == base_client.generate_collection_format_param(['entryOne', 'two'], key)
        else:
            assert oci.base_client.VALID_COLLECTION_FORMAT_TYPES[key].join(['entryOne', 'two']) == base_client.generate_collection_format_param(['entryOne', 'two'], key)
