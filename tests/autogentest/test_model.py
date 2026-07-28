# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import oci.util
import datetime
import json
import pytest
from oci.auth.signers import KeyPairSigner


@pytest.fixture
def new_instance():
    def _new_instance(**kwargs):
        instance = oci.core.models.Instance()
        instance.availability_domain = 'some ad'
        instance.compartment_id = 'some compartment'
        instance.display_name = 'some name'
        instance.id = 'some id'
        instance.image_id = 'some image'
        instance.metadata = {'foo': 'bar', 'foo2': 'bar2'}
        instance.region = 'some region'
        instance.shape = 'some shape'
        instance.lifecycle_state = 'RUNNING'
        instance.time_created = datetime.date(1999, 12, 31)
        for name, value in kwargs.items():
            setattr(instance, name, value)
        return instance
    return _new_instance


@pytest.fixture
def instance(new_instance):
    return new_instance()


def test_model_values(instance):
    assert 'some ad' == instance.availability_domain
    assert 'some compartment' == instance.compartment_id
    assert 'some name' == instance.display_name
    assert 'some id' == instance.id
    assert 'some image' == instance.image_id
    assert 'bar' == instance.metadata['foo']
    assert 'some region' == instance.region
    assert 'some shape' == instance.shape
    assert 'RUNNING' == instance.lifecycle_state
    assert datetime.date(1999, 12, 31) == instance.time_created


def test_equal(new_instance):
    assert new_instance() == new_instance()


def test_not_equal(new_instance):
    assert new_instance() != new_instance(shape="some other shape")


def test_equal_none(instance):
    # Explicit variable so we can use ==, != directly
    none = None
    assert instance != none
    assert none != instance
    assert not (instance == none)


def test_to_string(instance):
    string = str(instance)
    assert 'some name' in string
    assert 'foo2' in string
    assert '1999' in string


def test_to_dict(instance):
    instance_dict = oci.util.to_dict(instance)

    assert 'some ad' == instance_dict['availability_domain']
    assert 'some compartment' == instance_dict['compartment_id']
    assert 'some name' == instance_dict['display_name']
    assert 'some id' == instance_dict['id']
    assert 'some image' == instance_dict['image_id']
    assert 'bar' == instance_dict['metadata']['foo']
    assert 'some region' == instance_dict['region']
    assert 'some shape' == instance_dict['shape']
    assert 'RUNNING' == instance_dict['lifecycle_state']
    assert "1999-12-31" == instance_dict['time_created']


def test_redact_password_field():
    value = {
        'password': 'top-secret',
        'items': [
            {'nested': {'token': 'secret-token'}},
            {'nested': {'token': 'other-secret-token'}}
        ]
    }
    assert oci.util.redact_password_field(value, ['password']) == value
    oci.util.redact_password_field(value, ['items', '*', 'nested', 'token'])

    assert value['password'] == '<redacted>'
    assert value['items'][0]['nested']['token'] == '<redacted>'
    assert value['items'][1]['nested']['token'] == '<redacted>'


def test_password_field_redacted_in_model_repr():
    model = oci.apm_synthetics.models.PasswordInText()
    model.password = 'top-secret'

    model_repr = repr(model)

    assert 'top-secret' not in model_repr
    assert '<redacted>' in model_repr


def test_formatted_flat_dict_redacts_password_field():
    model = ModelWithRedactedFieldPaths()
    model.username = 'user'
    model.password = 'top-secret'

    model_dict = oci.util.to_dict(model)
    assert model_dict['password'] == 'top-secret'
    assert model_dict['username'] == 'user'

    redacted_model_dict = oci.util.to_dict(model, redact_sensitive_fields=True)
    assert redacted_model_dict['password'] == '<redacted>'
    assert redacted_model_dict['username'] == 'user'

    formatted_model = oci.util.formatted_flat_dict(model)
    assert 'top-secret' not in formatted_model
    assert '<redacted>' in formatted_model
    assert 'user' in formatted_model

    model_repr = repr(model)
    assert 'top-secret' not in model_repr
    assert '<redacted>' in model_repr
    assert 'user' in model_repr


def test_formatted_flat_dict_redacts_nested_password_fields():
    nested_model = ModelWithNestedRedactedFieldPaths()
    nested_model.display_name = 'nested-display-name'
    nested_model.nested_model = ModelWithRedactedFieldPaths(
        username='nested-user',
        password='nested-secret'
    )
    nested_model.nested_model_list = [
        ModelWithRedactedFieldPaths(username='list-user', password='list-secret')
    ]
    nested_model.nested_model_map = {
        'item': ModelWithRedactedFieldPaths(username='map-user', password='map-secret')
    }

    nested_model_dict = oci.util.to_dict(nested_model)
    assert nested_model_dict['display_name'] == 'nested-display-name'
    assert nested_model_dict['nested_model']['password'] == 'nested-secret'
    assert nested_model_dict['nested_model']['username'] == 'nested-user'
    assert nested_model_dict['nested_model_list'][0]['password'] == 'list-secret'
    assert nested_model_dict['nested_model_list'][0]['username'] == 'list-user'
    assert nested_model_dict['nested_model_map']['item']['password'] == 'map-secret'
    assert nested_model_dict['nested_model_map']['item']['username'] == 'map-user'

    redacted_nested_model_dict = oci.util.to_dict(nested_model, redact_sensitive_fields=True)
    assert redacted_nested_model_dict['display_name'] == 'nested-display-name'
    assert redacted_nested_model_dict['nested_model']['password'] == '<redacted>'
    assert redacted_nested_model_dict['nested_model']['username'] == 'nested-user'
    assert redacted_nested_model_dict['nested_model_list'][0]['password'] == '<redacted>'
    assert redacted_nested_model_dict['nested_model_list'][0]['username'] == 'list-user'
    assert redacted_nested_model_dict['nested_model_map']['item']['password'] == '<redacted>'
    assert redacted_nested_model_dict['nested_model_map']['item']['username'] == 'map-user'

    formatted_nested_model = oci.util.formatted_flat_dict(nested_model)
    assert 'nested-secret' not in formatted_nested_model
    assert 'list-secret' not in formatted_nested_model
    assert 'map-secret' not in formatted_nested_model
    assert 'nested-display-name' in formatted_nested_model
    assert 'nested-user' in formatted_nested_model
    assert 'list-user' in formatted_nested_model
    assert 'map-user' in formatted_nested_model
    assert formatted_nested_model.count('<redacted>') == 3

    nested_model_repr = repr(nested_model)
    assert 'nested-secret' not in nested_model_repr
    assert 'list-secret' not in nested_model_repr
    assert 'map-secret' not in nested_model_repr
    assert 'nested-display-name' in nested_model_repr
    assert 'nested-user' in nested_model_repr
    assert 'list-user' in nested_model_repr
    assert 'map-user' in nested_model_repr
    assert nested_model_repr.count('<redacted>') == 3


def test_api_request_serialization_preserves_password_while_log_safe_helpers_redact():
    secret = 'top-secret'
    model = ModelWithRedactedFieldPaths(username='user', password=secret)

    model_repr = repr(model)
    formatted_model = oci.util.formatted_flat_dict(model)

    assert secret not in model_repr
    assert secret not in formatted_model
    assert '<redacted>' in model_repr
    assert '<redacted>' in formatted_model

    signer = DummyKeyPairSigner.__new__(DummyKeyPairSigner)
    client = oci.BaseClient(
        'identity',
        {},
        signer,
        {},
        service_endpoint='https://identity.us-phoenix-1.oraclecloud.com'
    )
    client.request = lambda request, *args, **kwargs: request
    request = client.call_api(
        resource_path='/test',
        method='POST',
        header_params={'content-type': 'application/json'},
        body=model
    )

    request_body = json.loads(request.body)
    assert request_body['password'] == secret
    assert request_body['username'] == 'user'


class DummyKeyPairSigner(KeyPairSigner):
    pass


class ModelWithRedactedFieldPaths(object):
    def __init__(self, **kwargs):
        self.swagger_types = {
            'username': 'str',
            'password': 'str'
        }
        self.attribute_map = {
            'username': 'username',
            'password': 'password'
        }
        self._redacted_field_paths = [
            ['password']
        ]
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')

    def __repr__(self):
        as_dict = oci.util.to_dict(self)
        oci.util.redact_password_field(as_dict, ['password'])
        return oci.util.formatted_flat_dict(as_dict)


class ModelWithNestedRedactedFieldPaths(object):
    def __init__(self):
        self.swagger_types = {
            'display_name': 'str',
            'nested_model': 'ModelWithRedactedFieldPaths',
            'nested_model_list': 'list[ModelWithRedactedFieldPaths]',
            'nested_model_map': 'dict(str, ModelWithRedactedFieldPaths)'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'nested_model': 'nestedModel',
            'nested_model_list': 'nestedModelList',
            'nested_model_map': 'nestedModelMap'
        }
        self._redacted_field_paths = [
            ['nested_model', 'password'],
            ['nested_model_list', '*', 'password'],
            ['nested_model_map', '*', 'password']
        ]
        self.display_name = None
        self.nested_model = None
        self.nested_model_list = None
        self.nested_model_map = None

    def __repr__(self):
        as_dict = oci.util.to_dict(self)
        oci.util.redact_password_field(as_dict, ['nested_model', 'password'])
        oci.util.redact_password_field(as_dict, ['nested_model_list', '*', 'password'])
        oci.util.redact_password_field(as_dict, ['nested_model_map', '*', 'password'])
        return oci.util.formatted_flat_dict(as_dict)


def test_subclass():
    volume_attachment = oci.core.models.IScsiVolumeAttachment()
    assert 'iscsi' == volume_attachment.attachment_type
    assert hasattr(volume_attachment, 'chap_username')
    assert hasattr(volume_attachment, 'availability_domain')
    assert oci.core.models.VolumeAttachment.get_subtype(
        {'attachmentType': volume_attachment.attachment_type}) == 'IScsiVolumeAttachment'

    volume_attachment.chap_secret = 'foo'
    volume_attachment.compartment_id = 'bar'

    assert 'foo' == volume_attachment.chap_secret
    assert 'bar' == volume_attachment.compartment_id

    attachment_dict = oci.util.to_dict(volume_attachment)

    assert 'foo' == attachment_dict['chap_secret']
    assert 'bar' == attachment_dict['compartment_id']


def test_subclass_for_unknown_subtype_defaults_to_base_type():
    subtype = oci.core.models.VolumeAttachment.get_subtype({'attachmentType': 'new_subtype'})
    assert 'VolumeAttachment' == subtype


def test_value_allowed_none_or_none_sentinel_val_is_none():
    assert oci.util.value_allowed_none_or_none_sentinel(None, ['hello', 'world'])


def test_value_allowed_none_or_none_sentinel_val_is_none_sentinel():
    assert oci.util.value_allowed_none_or_none_sentinel(oci.util.NONE_SENTINEL, ['hello', 'world'])


def test_value_allowed_none_or_none_sentinel_val_is_allowed():
    assert oci.util.value_allowed_none_or_none_sentinel('hello', ['hello', 'world'])


def test_value_allowed_none_or_none_sentinel_val_is_not_allowed():
    assert not oci.util.value_allowed_none_or_none_sentinel('bad value', ['hello', 'world'])


def test_enum_none_value_ok(instance):
    instance.lifecycle_state = None
    assert instance.lifecycle_state is None


def test_enum_none_sentinel_value_ok(instance):
    instance.lifecycle_state = oci.util.NONE_SENTINEL
    assert instance.lifecycle_state is oci.util.NONE_SENTINEL


def test_enum_allowed_value_ok(instance):
    instance.lifecycle_state = 'PROVISIONING'
    assert instance.lifecycle_state == 'PROVISIONING'


def test_enum_not_allowed_value_translates_to_unknown_value(instance):
    instance.lifecycle_state = 'superman'
    assert instance.lifecycle_state == 'UNKNOWN_ENUM_VALUE'


def test_enum_not_allowed_value_throws_exception():
    model = oci.object_storage.models.CreateBucketDetails()
    with pytest.raises(ValueError):
        model.public_access_type = 'superman'
