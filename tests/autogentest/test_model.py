# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import oci.util
import datetime
import pytest


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
