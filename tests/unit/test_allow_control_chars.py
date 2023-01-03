# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci


class DecodeableObject(object):
    def __init__(self, obj):
        self.obj = obj

    def decode(self, decode):
        return self.obj


def test_allow_control_character_in_request(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    json_obj = '{"phrase": "test\x08 \x08" }'
    decodeable_obj = DecodeableObject(json_obj)
    deserialized_obj = client.deserialize_response_data(decodeable_obj, 'object', True)
    assert deserialized_obj["phrase"] == "test\x08 \x08"


def test_allow_control_character_in_client_config(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    client.allow_control_chars = True
    json_obj = '{"phrase": "test\x08 \x08" }'
    decodeable_obj = DecodeableObject(json_obj)
    deserialized_obj = client.deserialize_response_data(decodeable_obj, 'object', None)
    assert deserialized_obj["phrase"] == "test\x08 \x08"


def test_allow_control_character_in_global_config(identity, config):
    oci.BaseClient.ALLOW_CONTROL_CHARACTERS = True
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    json_obj = '{"phrase": "test\x08 \x08" }'
    decodeable_obj = DecodeableObject(json_obj)
    deserialized_obj = client.deserialize_response_data(decodeable_obj, 'object', None)
    oci.BaseClient.ALLOW_CONTROL_CHARACTERS = False  # Set it back to false after test
    assert deserialized_obj["phrase"] == "test\x08 \x08"


def test_allow_contorl_chars_request_level_configuration_takes_highest_precedence(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    client.allow_control_chars = False
    json_obj = '{"phrase": "test\x08 \x08" }'
    decodeable_obj = DecodeableObject(json_obj)
    deserialized_obj = client.deserialize_response_data(decodeable_obj, 'object', True)
    assert deserialized_obj["phrase"] == "test\x08 \x08"


def test_do_not_allow_control_character_by_default(identity, config):
    # By default, if allow_control_character is not set in Global/Client/Request, control characters are not allowed.
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})

    json_obj = '{"phrase": "test\x08 \x08" }'
    decodeable_obj = DecodeableObject(json_obj)

    # A string is returned if the json string could not be deserialized.
    # This is the case when control character exists in a json and json.loads() fail to deserialize
    deserialized_res = client.deserialize_response_data(decodeable_obj, 'object')
    assert isinstance(deserialized_res, str)


def test_do_not_allow_control_characters_request_level_config_takes_highest_precedence(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    client.allow_control_chars = True
    json_obj = '{"phrase": "test\x08 \x08" }'
    decodeable_obj = DecodeableObject(json_obj)
    deserialized_res = client.deserialize_response_data(decodeable_obj, 'object', False)
    assert isinstance(deserialized_res, str)
