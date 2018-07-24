# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

# Basic sanity tests that we can pass a retry strategy to a service call and it can succeed

import oci
import pytest

from . import util
from .. import test_config_container


def test_create_volume(block_storage):
    volume_id = None

    try:
        volume_name_gbs = util.random_name('python_sdk_test_volume_gb')
        create_volume_details = oci.core.models.CreateVolumeDetails()
        create_volume_details.availability_domain = util.availability_domain()
        create_volume_details.compartment_id = util.COMPARTMENT_ID
        create_volume_details.display_name = volume_name_gbs
        create_volume_details.size_in_gbs = 50

        result = block_storage.create_volume(create_volume_details, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

        util.validate_response(result)
        volume_id = result.data.id
        test_config_container.do_wait(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)
    finally:
        if volume_id:
            block_storage.delete_volume(volume_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
            test_config_container.do_wait(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180, succeed_on_not_found=True)


def test_list_buckets(object_storage):
    namespace = object_storage.get_namespace(retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
    buckets = object_storage.list_buckets(namespace, util.COMPARTMENT_ID, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
    assert len(buckets.data) > 0  # util.ensure_test_data ensures there's at least one bucket


def test_list_images_and_instances(compute):
    images = compute.list_images(util.COMPARTMENT_ID, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
    assert len(images.data) > 0  # We'll always get at least Oracle-offered images

    instances = compute.list_instances(util.COMPARTMENT_ID, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
    assert instances.data is not None  # Can't guarantee we'll have an instance, but the returned data should not be None


def test_list_get_users(identity, config):
    users = identity.list_users(config['tenancy'], retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
    assert len(users.data) > 0  # Always at least one user

    user_ocid = users.data[0].id

    user_no_retry = identity.get_user(user_ocid)
    user_with_retries = identity.get_user(user_ocid, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
    assert user_no_retry.data == user_with_retries.data


def test_client_level_retry_strategy(config):
    class ThrowRetryStrategy:
        def make_retrying_call(self, func_ref, *func_args, **func_kwargs):
            raise RuntimeError('Used ThrowRetryStrategy')

    client = oci.identity.IdentityClient(config, retry_strategy=ThrowRetryStrategy())
    client.base_client.endpoint = 'https://fakeendpoint.oracle'

    with pytest.raises(RuntimeError) as exc_info:
        client.list_users(config['tenancy'])

    assert str(exc_info.value) == 'Used ThrowRetryStrategy'


def test_method_level_retry_strategy_overrides_client_retry_strategy(config):
    class ThrowRetryStrategy:
        def make_retrying_call(self, func_ref, *func_args, **func_kwargs):
            raise RuntimeError('Used ThrowRetryStrategy')

    client = oci.identity.IdentityClient(config, retry_strategy=ThrowRetryStrategy())
    client.base_client.endpoint = 'https://fakeendpoint.oracle'

    with pytest.raises(oci.exceptions.RequestException):
        client.list_users(config['tenancy'], retry_strategy=oci.retry.NoneRetryStrategy())
