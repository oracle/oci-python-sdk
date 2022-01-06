# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import pytest
from oci.exceptions import ServiceError


def test_declared_type_int(compute):
    # validate exception if wrong primitive type is passed
    attach_vnic_details = oci.core.models.AttachVnicDetails()
    attach_vnic_details.nic_index = 'ShouldBeAnInt'
    with pytest.raises(TypeError) as excinfo:
        compute.attach_vnic(attach_vnic_details)

    assert 'Field nic_index with value ShouldBeAnInt was expected to be of type int but was of type str' in str(excinfo)

    # validate no TypeError thrown if float is give for field declared as 'int'
    attach_vnic_details.nic_index = 10.0
    with pytest.raises(ServiceError):
        compute.attach_vnic(attach_vnic_details)


def test_declared_type_str(identity, compute):
    # validate exception if wrong primitive type is passed
    create_user_details = oci.identity.models.CreateUserDetails()
    create_user_details.name = 1

    with pytest.raises(TypeError) as excinfo:
        identity.create_user(create_user_details)

    assert 'TypeError: Field name with value 1 was expected to be of type str but was of type int' in str(excinfo)

    # validate better exception for when bytes object is passed
    bytes_content = open('tests/resources/config', 'rb').read()
    launch_instance_details = oci.core.models.LaunchInstanceDetails()
    launch_instance_details.metadata = {
        'ssh_authorized_keys': bytes_content
    }

    # if bytes_content is already a str (Python 2) then we dont expect a type error
    if isinstance(bytes_content, str):
        with pytest.raises(ServiceError) as excinfo:
            compute.launch_instance(launch_instance_details)
    else:
        with pytest.raises(TypeError) as excinfo:
            compute.launch_instance(launch_instance_details)

        assert 'Field metadata.ssh_authorized_keys with value' in str(excinfo)
        assert 'was expected to be of type str but was of type bytes' in str(excinfo)


def test_declared_type_bool(compute):
    # validate exception if wrong primitive type is passed
    launch_instance_details = oci.core.models.LaunchInstanceDetails()
    create_vnic_details = oci.core.models.CreateVnicDetails()
    create_vnic_details.assign_public_ip = 1
    launch_instance_details.create_vnic_details = create_vnic_details

    # ServiceError validates that we did not fail this request during serialization
    with pytest.raises(TypeError) as excinfo:
        compute.launch_instance(launch_instance_details)

    assert 'Field create_vnic_details.assign_public_ip with value 1 was expected to be of type bool but was of type int' in str(excinfo)


def test_declared_type_float(compute):
    # this is a contrived example because we dont have any request models that declare fields as 'float'
    # thus we are sending up a response model

    # validate that int is accepted for type declared 'float'
    cross_connect_status = oci.core.models.CrossConnectStatus()
    cross_connect_status.light_level_ind_bm = 1

    # ServiceError validates that we did not fail this request during serialization
    with pytest.raises(ServiceError):
        compute.launch_instance({
            "cross_connect_status": cross_connect_status
        })


def test_declared_type_dict_input_invalid_throws_on_serialization(compute):
    launch_instance_details = oci.core.models.LaunchInstanceDetails()
    launch_instance_details.metadata = []

    with pytest.raises(TypeError) as excinfo:
        compute.launch_instance(launch_instance_details)

    assert 'TypeError: Field metadata with value [] was expected to be of type dict(str, str) but was of type list' in str(excinfo)


def test_declared_type_dict_value_type_invalid_throws_on_serialization(compute):
    launch_instance_details = oci.core.models.LaunchInstanceDetails()
    launch_instance_details.metadata = {'key': 1}  # this should be a dict(str, str)

    with pytest.raises(TypeError) as excinfo:
        compute.launch_instance(launch_instance_details)

    assert 'Field metadata.key with value 1 was expected to be of type str but was of type int' in str(excinfo)


def test_declared_type_list_input_invalid_throws_on_serialization(virtual_network):
    create_dhcp_details = oci.core.models.CreateDhcpDetails()
    create_dhcp_details.options = {}

    with pytest.raises(TypeError) as excinfo:
        virtual_network.create_dhcp_options(create_dhcp_details)

    assert 'TypeError: Field options with value {} was expected to be of type list[DhcpOption] but was of type dict' in str(excinfo)


def test_declared_type_list_item_type_invalid_throws_on_serialization(virtual_network):
    create_dhcp_details = oci.core.models.CreateDhcpDetails()

    create_dhcp_details.options = [1]

    with pytest.raises(TypeError) as excinfo:
        virtual_network.create_dhcp_options(create_dhcp_details)

    assert 'TypeError: Field options[*] with value 1 was expected to be of type DhcpOption but was of type int' in str(excinfo)


def test_subtype_of_declared_type_does_not_throw_on_serialization(compute):
    class MyVnicDetails(oci.core.models.CreateVnicDetails):
        pass

    launch_instance_details = oci.core.models.LaunchInstanceDetails()
    launch_instance_details.create_vnic_details = MyVnicDetails()

    # ServiceError validates that we did not fail this request during serialization
    with pytest.raises(oci.exceptions.ServiceError):
        compute.launch_instance(launch_instance_details)


def test_do_not_validate_types_on_dict_on_serialization(identity):
    create_user_details = {
        "compartmentId": 'compartment_id',
        "name": 1,
        "description": 'description'
    }

    # ServiceError validates that we did not fail this request during serialization
    with pytest.raises(oci.exceptions.ServiceError):
        identity.create_user(create_user_details)


def test_do_not_validate_types_on_nested_generic_dict_on_serialization(compute):
    launch_instance_details = oci.core.models.LaunchInstanceDetails()
    launch_instance_details.create_vnic_details = {
        "assignPublicIp": "ShouldBeABool"
    }

    # ServiceError validates that we did not fail this request during serialization
    with pytest.raises(oci.exceptions.ServiceError):
        compute.launch_instance(launch_instance_details)


def test_nested_field_name_correct_in_serialization_error(compute):
    launch_instance_details = oci.core.models.LaunchInstanceDetails()

    create_vnic_details = oci.core.models.CreateVnicDetails()
    create_vnic_details.assign_public_ip = "ShouldBeABool"
    launch_instance_details.create_vnic_details = create_vnic_details

    with pytest.raises(TypeError) as excinfo:
        compute.launch_instance(launch_instance_details)

    assert 'Field create_vnic_details.assign_public_ip with value ShouldBeABool was expected to be of type bool but was of type str' in str(excinfo)


def test_invalid_model_inside_dict_throws_on_serialization(compute):
    launch_instance_details = {}

    create_vnic_details = oci.core.models.CreateVnicDetails()
    create_vnic_details.assign_public_ip = "ShouldBeABool"
    launch_instance_details['createVnicDetails'] = create_vnic_details

    with pytest.raises(TypeError) as excinfo:
        compute.launch_instance(launch_instance_details)

    assert 'Field createVnicDetails.assign_public_ip with value ShouldBeABool was expected to be of type bool but was of type str' in str(excinfo)


def test_unrecognized_type_throws_on_serialization(compute):
    with pytest.raises(TypeError) as excinfo:
        compute.launch_instance(compute)

    assert 'TypeError: Not able to serialize data' in str(excinfo)


def test_extract_dict_value_type(compute):
    assert 'str' == compute.base_client.extract_dict_value_type_from_swagger_type('dict(str, str)')
    assert 'dict(str, str)' == compute.base_client.extract_dict_value_type_from_swagger_type('dict(str, dict(str, str))')
    assert compute.base_client.extract_dict_value_type_from_swagger_type('dict(int, str)') is None


def test_extract_list_value_type(compute):
    assert 'str' == compute.base_client.extract_list_item_type_from_swagger_type('list[str]')
    assert 'list[dict(str, str)]' == compute.base_client.extract_list_item_type_from_swagger_type('list[list[dict(str, str)]]')
