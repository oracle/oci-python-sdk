from . import util

import json
import oci
import time


def test_explicit_none_sentinel_results_in_serialized_null(object_storage):
    update_bucket_details = oci.object_storage.models.UpdateBucketDetails()
    update_bucket_details.name = 'Some name'

    serialized = object_storage.base_client.sanitize_for_serialization(update_bucket_details)
    assert {'name': 'Some name'} == serialized

    update_bucket_details.metadata = {'one': 'two'}
    serialized = object_storage.base_client.sanitize_for_serialization(update_bucket_details)
    assert {'name': 'Some name', 'metadata': {'one': 'two'}} == serialized

    update_bucket_details = oci.object_storage.models.UpdateBucketDetails()
    update_bucket_details.metadata = oci.util.NONE_SENTINEL
    serialized = object_storage.base_client.sanitize_for_serialization(update_bucket_details)
    assert {'metadata': None} == serialized
    assert '{"metadata": null}' == json.dumps(serialized)


def test_none_sentinel_falsey():
    assert not oci.util.NONE_SENTINEL


def test_assign_none_results_in_field_not_serialized(object_storage):
    update_bucket_details = oci.object_storage.models.UpdateBucketDetails()
    update_bucket_details.name = 'Some name'
    update_bucket_details.metadata = None

    serialized = object_storage.base_client.sanitize_for_serialization(update_bucket_details)
    assert {'name': 'Some name'} == serialized


def test_none_sentinel_with_bucket_metadata(object_storage):
    namespace = object_storage.get_namespace().data

    create_bucket_details = oci.object_storage.models.CreateBucketDetails()
    create_bucket_details.name = 'NoneSentinelTest_{}'.format(int(time.time()))
    create_bucket_details.compartment_id = util.COMPARTMENT_ID
    create_bucket_details.metadata = {'key1': 'val1', 'key2': 'val2'}
    create_bucket_details.public_access_type = 'NoPublicAccess'

    object_storage.create_bucket(namespace, create_bucket_details)
    bucket = object_storage.get_bucket(namespace, create_bucket_details.name).data
    assert create_bucket_details.name == bucket.name
    assert create_bucket_details.metadata == bucket.metadata

    update_bucket_details = oci.object_storage.models.UpdateBucketDetails()
    
    update_bucket_details.metadata = oci.util.NONE_SENTINEL  # should clear it
    object_storage.update_bucket(namespace, create_bucket_details.name, update_bucket_details)
    bucket = object_storage.get_bucket(namespace, create_bucket_details.name).data
    assert {} == bucket.metadata

    update_bucket_details.metadata = {'key5': 'val5', 'key6': 'val6'}
    object_storage.update_bucket(namespace, create_bucket_details.name, update_bucket_details)
    bucket = object_storage.get_bucket(namespace, create_bucket_details.name).data
    assert create_bucket_details.name == bucket.name
    assert update_bucket_details.metadata == bucket.metadata

    object_storage.delete_bucket(namespace, create_bucket_details.name)
