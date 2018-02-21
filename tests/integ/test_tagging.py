# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from . import util
from .. import test_config_container

import oci
import os
import pytest
import time


@pytest.fixture(scope="module")
def tagging_identity_client(request):
    config = oci.config.from_file(
        file_location=request.config.getoption("--config-file"),
        profile_name=request.config.getoption("--config-profile")
    )
    pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
    if pass_phrase:
        config['pass_phrase'] = pass_phrase

    identity_client = oci.identity.IdentityClient(config)
    util.init_availability_domain_variables(identity_client, config['tenancy'])

    return identity_client


@pytest.fixture(scope="module")
def tagging_block_storage_client(request):
    config = oci.config.from_file(
        file_location=request.config.getoption("--config-file"),
        profile_name=request.config.getoption("--config-profile")
    )
    pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
    if pass_phrase:
        config['pass_phrase'] = pass_phrase

    return oci.core.BlockstorageClient(config)


@pytest.fixture(scope="module")
def tag_namespace(tagging_identity_client):
    with test_config_container.create_vcr().use_cassette('test_tagging_tag_namespace_fixture.yml'):
        tag_namespace = None

        # Support reuse of a tag namespace instead of just creating them all the time (note that this could
        # have parallelism issues if the same test suite is run multiple times simultaneously since the checking
        # that we do could encounter unexpected results)
        if not os.environ.get('OCI_PYSDK_TAG_NAMESPACE_ID'):
            tag_namespace_name = util.random_name('tagns')

            create_tag_namespace_response = tagging_identity_client.create_tag_namespace(
                oci.identity.models.CreateTagNamespaceDetails(
                    compartment_id=util.COMPARTMENT_ID,
                    name=tag_namespace_name,
                    description='Python SDK integ test namespace'
                )
            )
            util.validate_response(create_tag_namespace_response)
            assert tag_namespace_name == create_tag_namespace_response.data.name
            assert 'Python SDK integ test namespace' == create_tag_namespace_response.data.description
            assert util.COMPARTMENT_ID == create_tag_namespace_response.data.compartment_id
            assert not create_tag_namespace_response.data.is_retired
            assert create_tag_namespace_response.data.time_created is not None
            assert create_tag_namespace_response.data.id is not None

            tag_namespace = create_tag_namespace_response.data
        else:
            get_tag_namespace_response = tagging_identity_client.get_tag_namespace(os.environ.get('OCI_PYSDK_TAG_NAMESPACE_ID'))

            if get_tag_namespace_response.data.is_retired:
                update_tag_namespace_response = tagging_identity_client.update_tag_namespace(
                    get_tag_namespace_response.data.id,
                    oci.identity.models.UpdateTagNamespaceDetails(is_retired=False)
                )
                util.validate_response(update_tag_namespace_response)
                tag_namespace = update_tag_namespace_response.data
            else:
                tag_namespace = get_tag_namespace_response.data

    yield tag_namespace


def test_manage_tags_and_namespace(tagging_identity_client, tag_namespace):
    with test_config_container.create_vcr().use_cassette('test_tagging_manage_tags_and_namespace.yml'):
        # List all namespaces and make sure that our namespace appears
        tag_namespaces = []
        page = None
        while True:
            if page:
                list_namespaces_response = tagging_identity_client.list_tag_namespaces(
                    compartment_id=util.COMPARTMENT_ID,
                    page=page
                )
            else:
                list_namespaces_response = tagging_identity_client.list_tag_namespaces(compartment_id=util.COMPARTMENT_ID)

            tag_namespaces.extend(list_namespaces_response.data)

            page = list_namespaces_response.next_page
            if not page:
                break

        found_namespace = False
        for tn in tag_namespaces:
            if tn.id == tag_namespace.id:
                found_namespace = True
                assert tag_namespace.name == tn.name
                assert not tn.is_retired
        assert found_namespace

        get_tag_namespace_response = tagging_identity_client.get_tag_namespace(tag_namespace.id)
        assert tag_namespace.compartment_id == get_tag_namespace_response.data.compartment_id
        assert tag_namespace.id == get_tag_namespace_response.data.id
        assert tag_namespace.name == get_tag_namespace_response.data.name
        assert not get_tag_namespace_response.data.is_retired

        tag_one_name = util.random_name('tagone')
        tag_one = create_or_reactivate_tag(tagging_identity_client, tag_namespace, tag_one_name)
        tag_one = update_and_retire_tag(tagging_identity_client, tag_one)

        tag_two_name = util.random_name('tagtwo')
        tag_two = create_or_reactivate_tag(tagging_identity_client, tag_namespace, tag_two_name)

        update_tag_namespace_response = tagging_identity_client.update_tag_namespace(
            tag_namespace.id,
            oci.identity.models.UpdateTagNamespaceDetails(description='updated tag ns', is_retired=True)
        )
        util.validate_response(update_tag_namespace_response)
        assert 'updated tag ns' == update_tag_namespace_response.data.description
        assert update_tag_namespace_response.data.is_retired

        # List the tags in the namespace and make sure that the ones we created appear
        tags = []
        page = None
        while True:
            if page:
                list_tags_response = tagging_identity_client.list_tags(
                    tag_namespace_id=tag_namespace.id,
                    page=page
                )
            else:
                list_tags_response = tagging_identity_client.list_tags(tag_namespace_id=tag_namespace.id)

            tags.extend(list_tags_response.data)

            page = list_tags_response.next_page
            if not page:
                break

        found_tag_one = False
        found_tag_two = True
        for t in tags:
            if t.id == tag_one.id:
                found_tag_one = True
                assert t.name == tag_one.name
                assert t.description == tag_one.description
                assert t.is_retired
            elif t.id == tag_two.id:
                found_tag_two = True
                assert t.name == tag_two.name
                assert t.description == tag_two.description
                assert not t.is_retired

            if found_tag_one and found_tag_two:
                break
        assert found_tag_one and found_tag_two

        # Retiring the namespace should also retire the tags under the namespace. tag_one was already retired,
        # but tag_two wasn't so check it is now retired.
        get_tag_response = tagging_identity_client.get_tag(tag_two.tag_namespace_id, tag_two.name)
        util.validate_response(get_tag_response)
        assert get_tag_response.data.is_retired

        get_tag_namespace_response = tagging_identity_client.get_tag_namespace(tag_namespace.id)
        util.validate_response(get_tag_namespace_response)
        assert 'updated tag ns' == get_tag_namespace_response.data.description
        assert get_tag_namespace_response.data.is_retired


# Sanity test tagging by applying it to a resource
def test_tag_resource(tagging_identity_client, tagging_block_storage_client, tag_namespace):
    with test_config_container.create_vcr().use_cassette('test_tagging_tag_resource.yml'):
        # Make sure that the namespace is not retired (so we can create tags in it) before we start
        update_tag_namespace_response = tagging_identity_client.update_tag_namespace(
            tag_namespace.id,
            oci.identity.models.UpdateTagNamespaceDetails(is_retired=False)
        )

        tag_one_name = util.random_name('tagresone')
        create_or_reactivate_tag(tagging_identity_client, tag_namespace, tag_one_name)

        tag_two_name = util.random_name('tagrestwo')
        create_or_reactivate_tag(tagging_identity_client, tag_namespace, tag_two_name)

        # There seems to be some eventual consistency thing with tags where sometimes we can't
        # use a tag we created straight away. This manifests as a 404, so retry in this case

        num_tries = 0
        while True:
            try:
                # Create a thing with tags
                create_volume_response = tagging_block_storage_client.create_volume(
                    oci.core.models.CreateVolumeDetails(
                        availability_domain=util.availability_domain(),
                        compartment_id=util.COMPARTMENT_ID,
                        size_in_gbs=50,
                        display_name=util.random_name('py_sdk_tag_test'),
                        freeform_tags={'free': 'form', 'bat': 'man'},
                        defined_tags={tag_namespace.name: {tag_one_name: 'hello', tag_two_name: 'world'}}
                    )
                )
                break
            except oci.exceptions.ServiceError as e:
                if e.status == 404:
                    num_tries += 1

                    if num_tries >= 3:  # If we can't get it in 3 tries, something is probably wrong...
                        raise
                    else:
                        time.sleep(5)
                else:
                    raise

        volume_id = create_volume_response.data.id
        volume = oci.wait_until(tagging_block_storage_client, tagging_block_storage_client.get_volume(volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180).data
        assert {'free': 'form', 'bat': 'man'} == volume.freeform_tags
        assert {tag_namespace.name: {tag_one_name: 'hello', tag_two_name: 'world'}} == volume.defined_tags

        # Replace tags on the thing
        update_volume_response = tagging_block_storage_client.update_volume(
            volume_id,
            oci.core.models.UpdateVolumeDetails(
                freeform_tags={'other': 'tag'},
                defined_tags={tag_namespace.name: {tag_two_name: 'newval'}}
            )
        )
        assert {'other': 'tag'} == update_volume_response.data.freeform_tags
        assert {tag_namespace.name: {tag_two_name: 'newval'}} == update_volume_response.data.defined_tags

        volume = tagging_block_storage_client.get_volume(volume_id).data
        assert {'other': 'tag'} == volume.freeform_tags
        assert {tag_namespace.name: {tag_two_name: 'newval'}} == volume.defined_tags

        # Nuke tags on the thing
        update_volume_response = tagging_block_storage_client.update_volume(
            volume_id,
            oci.core.models.UpdateVolumeDetails(
                freeform_tags={},
                defined_tags={}
            )
        )
        assert {} == update_volume_response.data.freeform_tags
        assert {} == update_volume_response.data.defined_tags

        volume = tagging_block_storage_client.get_volume(volume_id).data
        assert {} == volume.freeform_tags
        assert {} == volume.defined_tags

        tagging_block_storage_client.delete_volume(volume_id)

        # Retire the tag namespace at the end of our tests
        update_tag_namespace_response = tagging_identity_client.update_tag_namespace(
            tag_namespace.id,
            oci.identity.models.UpdateTagNamespaceDetails(is_retired=True)
        )
        util.validate_response(update_tag_namespace_response)
        assert update_tag_namespace_response.data.is_retired


def create_or_reactivate_tag(tagging_identity_client, tag_namespace, tag_name):
    # It is possible that the tag already exists, if so we will reactivate it rather than creating it
    tag_exists = False
    try:
        # This should 404 if the tag does not exist
        tagging_identity_client.get_tag(tag_namespace.id, tag_name)
        tag_exists = True
    except oci.exceptions.ServiceError as e:
        print(e)
        if e.status == 404:
            pass
        else:
            raise

    if not tag_exists:
        create_tag_response = tagging_identity_client.create_tag(
            tag_namespace.id,
            oci.identity.models.CreateTagDetails(name=tag_name, description='integ test tag {}'.format(tag_name))
        )
        util.validate_response(create_tag_response)
        assert tag_namespace.id == create_tag_response.data.tag_namespace_id
        assert tag_name == create_tag_response.data.name
        assert 'integ test tag {}'.format(tag_name) == create_tag_response.data.description
        assert create_tag_response.data.id is not None
        assert create_tag_response.data.time_created is not None
        assert not create_tag_response.data.is_retired

        return create_tag_response.data
    else:
        # Make sure that the tag is active
        update_tag_response = tagging_identity_client.update_tag(
            tag_namespace.id,
            tag_name,
            oci.identity.models.UpdateTagDetails(description='reactivated tag', is_retired=False)
        )
        return update_tag_response.data


def update_and_retire_tag(tagging_identity_client, tag):
    update_tag_response = tagging_identity_client.update_tag(
        tag.tag_namespace_id,
        tag.name,
        oci.identity.models.UpdateTagDetails(description='hello world', is_retired=True)
    )
    util.validate_response(update_tag_response)
    assert 'hello world' == update_tag_response.data.description
    assert update_tag_response.data.is_retired

    update_tag_response = tagging_identity_client.update_tag(
        tag.tag_namespace_id,
        tag.name,
        oci.identity.models.UpdateTagDetails(is_retired=False)
    )
    util.validate_response(update_tag_response)
    assert 'hello world' == update_tag_response.data.description
    assert not update_tag_response.data.is_retired

    update_tag_response = tagging_identity_client.update_tag(
        tag.tag_namespace_id,
        tag.name,
        oci.identity.models.UpdateTagDetails(is_retired=True)
    )
    util.validate_response(update_tag_response)
    assert 'hello world' == update_tag_response.data.description
    assert update_tag_response.data.is_retired

    get_tag_response = tagging_identity_client.get_tag(tag.tag_namespace_id, tag.name)
    util.validate_response(get_tag_response)
    assert 'hello world' == get_tag_response.data.description
    assert get_tag_response.data.is_retired

    return get_tag_response.data
