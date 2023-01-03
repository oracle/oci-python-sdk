# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import functools
import random
import time
import traceback
import oci
import os
from oci.object_storage.transfer.constants import MEBIBYTE
from .. import test_config_container

TEST_DATA_VERSION = '2'

COMPARTMENT_ID = os.environ.get("OCI_PYSDK_COMPARTMENT_ID")
COMPARTMENT_NAME = os.environ.get("OCI_PYSDK_COMPARTMENT_NAME")

REGIONAL_CONFIG = {
    'us-phoenix-1': {
        'bucket_prefix': '',
        'windows_vm_image': 'ocid1.image.oc1.phx.aaaaaaaa53cliasgvqmutflwqkafbro2y4ywjebci5szc4eus5byy2e2b7ua',
        'oracle_linux_image': 'ocid1.image.oc1.phx.aaaaaaaamv5wg7ffvaxaba3orhpuya7x7opz24hd6m7epmwfqbeudi6meepq'},
    'us-ashburn-1': {
        'bucket_prefix': 'iad_',
        'windows_vm_image': 'ocid1.image.oc1.iad.aaaaaaaatob7wb2ljtvsvjy7olpsyuttodb7ok3osflx3hqd2nt4l6jagxla',
        'oracle_linux_image': 'ocid1.image.oc1.iad.aaaaaaaay7kt3yikvnm47x7rhb7myj5yxbsl7hfuuxn5fikdpb73y76woiba'}
}

# This global can be changed to influence what configuration data this module vends.
target_region = 'us-phoenix-1'

# Primary and secondary availability domains used as part of the tests
first_ad = None
second_ad = None


def availability_domain():
    return first_ad


def second_availability_domain():
    return second_ad


def init_availability_domain_variables(identity_api, tenant_id):
    global first_ad, second_ad

    if first_ad is None or second_ad is None:
        availability_domains = identity_api.list_availability_domains(tenant_id).data

        if len(availability_domains) == 1:
            first_ad = availability_domains[0].name
            second_ad = availability_domains[0].name
        elif len(availability_domains) == 2:
            first_ad = availability_domains[0].name
            second_ad = availability_domains[1].name
        else:
            # We need consistency in the vended availability domains if we're mocking, so don't randomize
            if test_config_container.using_vcr_with_mock_responses():
                first_ad = availability_domains[0].name
                second_ad = availability_domains[1].name
            else:
                chosen_domains = random.sample(availability_domains, 2)
                first_ad = chosen_domains[0].name
                second_ad = chosen_domains[1].name


def bucket_prefix():
    return REGIONAL_CONFIG[target_region]['bucket_prefix']


def oracle_linux_image():
    return REGIONAL_CONFIG[target_region]['oracle_linux_image']


def windows_vm_image():
    return REGIONAL_CONFIG[target_region]['windows_vm_image']


def random_name(prefix, insert_underscore=True):
    if test_config_container.using_vcr_with_mock_responses():
        return prefix + ('_' if insert_underscore else '') + 'vcr'
    else:
        return prefix + ('_' if insert_underscore else '') + str(random.randint(0, 1000000))


def validate_response(result, extra_validation=None, includes_debug_data=False, expect_etag=False):
    try:
        assert result.status == 200 or result.status == 204

        if includes_debug_data:
            assert result.headers['opc-request-id']
            assert result.headers['opc-client-info']
            assert result.headers['user-agent']

        if expect_etag:
            assert result.headers['etag']

        if extra_validation:
            extra_validation(result)

    except AssertionError:
        print(result)
        raise


def validate_service_error(result, error_message=None, debug=False):
    try:
        assert result.status != 200
        if debug:
            assert isinstance(result.exception, oci.exceptions.ServiceError)
            if error_message:
                assert error_message in str(result.exception)
        else:
            if error_message:
                assert error_message in result.message
    except AssertionError:
        # TODO better inspection for failing tests
        print(str(result))
        raise


def wait_until(get_command, state, max_wait_seconds=30, max_interval_seconds=15, succeed_if_not_found=False, item_index_in_list_response=None):
    """Poll the given get command until the result has a lifecycle-state that matches the given state.
    The Polling interval will double with each call until max_interval_seconds is reached."""
    sleep_interval_seconds = 1
    start_time = time.time()

    while True:
        try:
            result = get_command()
        except Exception as error:
            if succeed_if_not_found and hasattr(error, 'status') and error.status == 404:
                break

            raise RuntimeError('Error while waiting for state: ' + str(error))

        # if an index is supplied, check the state of the corresponding item in the list
        if result:
            if item_index_in_list_response is not None:
                if len(result.data) > item_index_in_list_response and result.data[item_index_in_list_response].lifecycle_state == state:
                    break
            elif result.data.lifecycle_state == state:
                break

        if not test_config_container.using_vcr_with_mock_responses():
            time.sleep(sleep_interval_seconds)

        # Double the sleep each time up to the maximum.
        sleep_interval_seconds = min(sleep_interval_seconds * 2, max_interval_seconds)

        elapsed_seconds = (time.time() - start_time)

        if elapsed_seconds + sleep_interval_seconds > max_wait_seconds:
            if max_wait_seconds <= elapsed_seconds:
                raise RuntimeError('Maximum wait time has been exceeded.')


def print_latest_exception(exception):
    print("ERROR {type}: {message}".format(type=exception.__class__.__name__, message=str(exception)))
    traceback.print_exc()


def log_test(func):
    @functools.wraps(func)
    def wrapped_call(ctx, *args, **kwargs):
        print("Test {name}...".format(name=func.__name__))
        func(ctx, *args, **kwargs)
        print("Test {name} Complete".format(name=func.__name__))

    return wrapped_call


def ensure_test_data(api, namespace, compartment, bucket_prefix):
    """The test data will be deleted and recreated only if the version has changed."""
    test_data_metadata_bucket = bucket_prefix + '_test_metadata'
    test_data_version_object = 'test_data_version'

    # Check test data version.
    try:
        version = api.get_object(
            namespace,
            test_data_metadata_bucket,
            test_data_version_object).data.content.decode('UTF-8')

        if version == TEST_DATA_VERSION:
            return True
    except Exception as error:
        # if the bucket has never been created with the test_metadata, then create it
        if error.status == 404:
            print(error)
            create_bucket(api, namespace, compartment, test_data_metadata_bucket)
            api.put_object(namespace, test_data_metadata_bucket, test_data_version_object, TEST_DATA_VERSION)
        else:
            raise error

    print("Recreating test data.")
    clear_test_data(api, namespace, compartment)

    print('Creating test data.')
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket1',
                  objects=['object1', 'object2', 'object3', 'object4', 'object5'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket2',
                  objects=['a/b/c/object1', 'a/b/c/object2', 'a/b/c/object3', 'a/b/object4', 'a/b/object5'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket3', objects=['a/b/object1'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket4')
    create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket4', 'hasUserMetadata.json', metadata={'foo1': 'bar1', 'foo2': 'bar2'})
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket5', {'foo1': 'bar1', 'foo2': 'bar2'})

    # Update test data version
    create_bucket(api, namespace, compartment, test_data_metadata_bucket)
    api.put_object(namespace, test_data_metadata_bucket, test_data_version_object, TEST_DATA_VERSION)

    return True


def create_bucket(api, namespace, compartment, bucket_name, metadata=None, objects=None):
    """Deletes all buckets and objects in the given compartment."""
    request = oci.object_storage.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = compartment
    request.metadata = metadata
    api.create_bucket(namespace, request)
    show_progress()

    if objects:
        for obj in objects:
            create_object(api, namespace, bucket_name, obj)


def create_object(api, namespace, bucket_name, object_name, file_name=None, metadata=None):
    args = {}
    if metadata:
        # TODO what is this for?
        args['opc_meta'] = metadata
    if file_name:
        with open(file_name, 'rb') as file:
            api.put_object(namespace, bucket_name, object_name, file, **args)
    else:
        api.put_object(namespace, bucket_name, object_name, object_name, **args)

    show_progress()


def clear_test_data(api, namespace, compartment):
    print('Deleting test data.')
    bucket_list = []
    next_page = None
    count = 0
    while True:
        if next_page:
            response = api.list_buckets(namespace, compartment, page=next_page)
        else:
            response = api.list_buckets(namespace, compartment)

        bucket_list.extend([bucket.name for bucket in response.data])

        count += 1
        if count > 100:
            raise RuntimeError("Too many pages, something is probably wrong.")

        if not response.has_next_page:
            break
        next_page = response.next_page

    for bucket in bucket_list:
        object_list = []
        next_start = None
        count = 0
        while True:
            if next_start:
                response = api.list_objects(namespace, bucket, start=next_start)
            else:
                response = api.list_objects(namespace, bucket)

            object_list.extend([obj.name for obj in response.data.objects])

            count += 1
            if count > 100:
                raise RuntimeError("Too many pages, something is probably wrong.")

            next_start = response.data.next_start_with
            if next_start is None:
                break

        for obj in object_list:
            api.delete_object(namespace, bucket, obj)

        api.delete_bucket(namespace, bucket)
        show_progress()


def show_progress():
    print('.', end='', flush=True)


def create_large_file(filename, size_in_mebibytes):
    sample_content = b'a'
    with open(filename, 'wb') as f:
        f.write(sample_content * MEBIBYTE * size_in_mebibytes)


def get_all_pages(list_service_function, ** kwargs):
    result_records = []
    cloned_kwargs = kwargs.copy()

    keep_paginating = True
    next_page = None
    while keep_paginating:
        if next_page is not None:
            cloned_kwargs['page'] = next_page
        response = list_service_function(** cloned_kwargs)

        result_records.extend(response.data)
        next_page = response.next_page
        keep_paginating = (next_page is not None)

    return result_records
