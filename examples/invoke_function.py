# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import sys

import oci

from oci import config
from oci import core
from oci import functions
from oci import identity
from oci import pagination

from oci.core import models as core_models
from oci.functions import models as fn_models

# *** Function as a Service - Python Example ***
#
# This is a basic example of how to register and invoke a serverless Function
# on OCI using the Python SDK.
#
# The example has some pre-requisites. In particular you will need to create a
# Function and publish it to OCIR. The best way to do this is with the 'Fn
# CLI':
#
# 1. Install the Fn CLI :
#      https://github.com/fnproject/cli
#
# 2. Create Function - Quick Guide :
#      https://github.com/fnproject/fn/blob/master/README.md
#
#
# This sample will do following things:
#
# 1. Create VCN and subnets - Provide an endpoint on which your function can be
#    invoked.
#
# 2. Create Application and Function - Register and configure your function.
#
# 3. Invoke Function - How your function can be invoked.
#
# 4. Clean-up - Tidy up the resources created above.
#
#    NB: To simplify things, this example is hardcoded to the 'us-phoenix-1' OCI
#    region.
#
# It is also necessary to create two environment variables to configure the sample.
#
# 1) COMPARTMENT_NAME : Must be a valid OCI Compartment name.
# 2) OCIR_FN_IMAGE    : Must be a valid OCIR function image.
#
#    NB: Currently, after invoking a function we must wait upto 30 minutes before
#    clearing down any supporting Subnets and VCN.
#
# For more information see the OCI Function Docs:
#   https://docs.cloud.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm

NAME_PREFIX = "oci-python-sdk-function-example"

SETUP = "setup"
INVOKE = "invoke"
TEARDOWN = "teardown"


def setup_resources(oci_cfg, compartment_id, name, image):
    """
    Setup the minimal OCI resources required to establish an invocable function.

    :param compartment_id: The compartment_id in which to create the resources.
    :type compartment_id: str

    :param name: The name to identify all created resources with.
    :type name: str

    :param image: An accessible OCIR Function image that can be invoked.
    :type image: str
    """
    identity_client = identity.IdentityClient(oci_cfg)
    network_client = core.VirtualNetworkClient(oci_cfg)
    fn_management_client = functions.FunctionsManagementClient(oci_cfg)

    vn_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(network_client)

    print("setup_resources")

    #  1. A VCN is required to host subnets.
    vcn = get_unique_vcn_by_name(network_client, compartment_id, vcn_name(name))
    if vcn is None:
        vcn_details = core_models.CreateVcnDetails(
            compartment_id=compartment_id, display_name=vcn_name(name), cidr_block="10.0.0.0/16"
        )
        result = vn_composite_ops.create_vcn_and_wait_for_state(
            vcn_details, wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE]
        )
        print('Created Vcn: {}'.format(result.data.display_name))
        vcn = result.data

    # 2. An Internet Gateway is required to enable the VCN to talk to the wider world.
    ig = get_unique_ig_by_name(network_client, compartment_id, vcn.id, ig_name(name))
    if ig is None:
        gateway_details = core_models.CreateInternetGatewayDetails(
            compartment_id=compartment_id, vcn_id=vcn.id, display_name=ig_name(name), is_enabled=True
        )
        result = vn_composite_ops.create_internet_gateway_and_wait_for_state(
            gateway_details, wait_for_states=[oci.core.models.InternetGateway.LIFECYCLE_STATE_AVAILABLE]
        )
        print('Created Internet Gateway: {}'.format(result.data.display_name))
        ig = result.data

    # 3. We must configure the VCN's traffic to be routed through the Internet Gateway.
    rt = get_unique_route_table_by_name(network_client, compartment_id, vcn.id, drt_name(name))
    if rt is not None:
        configure_ig(network_client, compartment_id, vcn.id, ig.id, drt_name(name))

    # 4. A subnet is required to expose and be able invoke the function.
    # In multiple AD regions, subnets can be created in multiple ADs to provide redundency.
    sn = get_unique_subnet_by_name(network_client, compartment_id, vcn.id, subnet_name(name))
    if sn is None:
        ad = get_availability_domains(identity_client, compartment_id)[0]
        print("Using AD: " + str(ad.name))
        subnet_details = core_models.CreateSubnetDetails(
            compartment_id=compartment_id, vcn_id=vcn.id, availability_domain=ad.name,
            display_name=subnet_name(name), cidr_block="10.0.0.0/24"
        )
        result = vn_composite_ops.create_subnet_and_wait_for_state(
            subnet_details, wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE]
        )
        print('Created Subnet: {}'.format(result.data.display_name))
        sn = result.data

    # 5. Create an Application to host and manage the function(s).
    app = get_unique_application_by_name(fn_management_client, compartment_id, application_name(name))
    if app is None:
        fm_composite_ops = oci.functions.FunctionsManagementClientCompositeOperations(fn_management_client)
        app_details = fn_models.CreateApplicationDetails(
            compartment_id=compartment_id, display_name=application_name(name), subnet_ids=[sn.id]
        )
        result = fm_composite_ops.create_application_and_wait_for_state(
            app_details, wait_for_states=[fn_models.Application.LIFECYCLE_STATE_ACTIVE]
        )
        print('Created Application: {}'.format(result.data.display_name))
        app = result.data

    # 6. Create a single Function, set its execution image and limits.
    fn = get_unique_function_by_name(fn_management_client, app.id, function_name(name))
    if fn is None:
        fm_composite_ops = oci.functions.FunctionsManagementClientCompositeOperations(fn_management_client)
        fn_details = fn_models.CreateFunctionDetails(
            application_id=app.id, display_name=function_name(name),
            image=image, memory_in_mbs=128, timeout_in_seconds=30
        )
        result = fm_composite_ops.create_function_and_wait_for_state(
            fn_details, wait_for_states=[fn_models.Function.LIFECYCLE_STATE_ACTIVE]
        )
        print('Created Function: {}'.format(result.data.display_name))
        fn = result.data


def invoke_function(oci_cfg, compartment_id, name, content):
    """
    Invoke a Function!

    :param compartment_id: The compartment_id in of the Function.
    :type compartment_id: str

    :param name: The Function name.
    :type name: str

    :param content: The data to send when invoking the Function.
    :type content: str
    """
    fn_management_client = functions.FunctionsManagementClient(oci_cfg)

    print("invoke_function")

    app = get_unique_application_by_name(
        fn_management_client, compartment_id, application_name(name))
    fn = get_unique_function_by_name(
        fn_management_client, app.id, function_name(name))

    # 8. Create an invocation client and invoke the Function!
    invoke_client = functions.FunctionsInvokeClient(
        oci_cfg, service_endpoint=fn.invoke_endpoint)

    resp = invoke_client.invoke_function(fn.id, invoke_function_body=content)
    print(resp.data.text)


def teardown_resources(oci_cfg, compartment_id, name):
    """
    Clean up all Function resources for this example.

    NB: If nay errors occur, please tidy up resources manually using the OCI console.

    :param compartment_id: The compartment_id in which to create the resources.
    :type compartment_id: str

    :param name: The name to identify all created resources with.
    :type name: str
    """
    network_client = core.VirtualNetworkClient(oci_cfg)
    fn_management_client = functions.FunctionsManagementClient(oci_cfg)

    vn_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(network_client)
    fm_composite_ops = oci.functions.FunctionsManagementClientCompositeOperations(fn_management_client)

    print("teardown_resources")

    # Collect the OCI resources to delete.
    vcn = ig = rt = sn = app = fn = None

    vcn = get_unique_vcn_by_name(network_client, compartment_id, vcn_name(name))
    if vcn is not None:
        ig = get_unique_ig_by_name(
            network_client, compartment_id, vcn.id, ig_name(name))
        rt = get_unique_route_table_by_name(
            network_client, compartment_id, vcn.id, drt_name(name))
        sn = get_unique_subnet_by_name(
            network_client, compartment_id, vcn.id, subnet_name(name))

    app = get_unique_application_by_name(
        fn_management_client, compartment_id, application_name(name))
    if app is not None:
        fn = get_unique_function_by_name(
            fn_management_client, app.id, function_name(name))

    # Delete resources. Please note the ordering.
    if fn is not None:
        fm_composite_ops.delete_function_and_wait_for_state(
            fn.id, wait_for_states=[fn_models.Function.LIFECYCLE_STATE_DELETED]
        )
        print('Delete Function: {}'.format(fn.id))

    if app is not None:
        fm_composite_ops.delete_application_and_wait_for_state(
            app.id, wait_for_states=[fn_models.Application.LIFECYCLE_STATE_DELETED]
        )
        print('Delete Application: {}'.format(app.id))

    if sn is not None:
        vn_composite_ops.delete_subnet_and_wait_for_state(
            sn.id, wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
        )
        print('Delete Subnet: {}'.format(sn.id))

    if rt is not None:
        prepare_route_table_for_delete(network_client, rt.id)

    if ig is not None:
        vn_composite_ops.delete_internet_gateway_and_wait_for_state(
            ig.id, wait_for_states=[oci.core.models.InternetGateway.LIFECYCLE_STATE_TERMINATED]
        )
        print('Delete Internet Gateway: {}'.format(ig.id))

    if vcn is not None:
        vn_composite_ops.delete_vcn_and_wait_for_state(
            vcn.id, wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED])
        print('Delete VCN: {}'.format(vcn.id))


#  === Helper Functions ===

def get_compartment_id(oci_cfg, compartment_name):
    """
    Get the compartment_id by name for the configured tenancy.

    :param oci_cfg: OCI auth config
    :param compartment_name: OCI tenancy compartment name

    :return: OCI tenancy compartment.
    :rtype: str
    """
    identity_client = identity.IdentityClient(oci_cfg)
    result = pagination.list_call_get_all_results(
        identity_client.list_compartments,
        cfg["tenancy"],
        compartment_id_in_subtree=True,
        access_level="ACCESSIBLE",
    )
    for c in result.data:
        if compartment_name == c.name:
            return c
    raise Exception("Compartment not found.")


def get_availability_domains(identity_client, compartment_id):
    """
    Gets the list of AvailabilityDomain for the specified compartment.

    :param network_client: OCI VirtualNetworkClient client
    :type network_client: oci.core.VirtualNetworkClient

    :param compartment_id: The OCID of the compartment to check.
    :type compartment_id: str

    :return: The AvailabilityDomains
    :rtype: [identity_models.AvailabilityDomain]
    """
    result = pagination.list_call_get_all_results(
        identity_client.list_availability_domains,
        compartment_id
    )
    return result.data


def get_unique_vcn_by_name(network_client, compartment_id, display_name):
    """
    Find a unique Vcn by name.

    :param network_client: OCI VirtualNetworkClient client
    :type network_client: oci.core.VirtualNetworkClient

    :param compartment_id: The OCID of the compartment which owns the Vcn.
    :type compartment_id: str

    :param display_name: The display name of the Vcn.
    :type display_name: str

    :return: The Vcn
    :rtype: core_models.Vcn
    """
    result = pagination.list_call_get_all_results(
        network_client.list_vcns,
        compartment_id,
        display_name=display_name
    )
    for vcn in result.data:
        if display_name == vcn.display_name:
            return vcn


def get_unique_ig_by_name(network_client, compartment_id, vcn_id, display_name):
    """
    Find a unique InternetGateway by name.

    :param network_client: OCI VirtualNetworkClient client
    :type network_client: oci.core.VirtualNetworkClient

    :param compartment_id: The OCID of the compartment which owns the Vcn.
    :type compartment_id: str

    :param vcn_id: The OCID of the Vcn which will own the InternetGateway.
    :type vcn_id: str

    :param display_name: The display name of the InternetGateway.
    :type display_name: str

    :return: The InternetGateway
    :rtype: core_models.InternetGateway
    """
    result = pagination.list_call_get_all_results(
        network_client.list_internet_gateways,
        compartment_id,
        vcn_id,
        display_name=display_name
    )
    for ig in result.data:
        if display_name == ig.display_name:
            return ig


def configure_ig(network_client, compartment_id, vcn_id, ig_id, display_name):
    """
    Configures a Vcn's default RoutingTable to add a RouteRule that provides
    Internet access via the specified InternetGateway.

    :param network_client: OCI VirtualNetworkClient client
    :type network_client: oci.core.VirtualNetworkClient

    :param compartment_id: The OCID of the compartment which owns the Vcn.
    :type compartment_id: str

    :param vcn_id: The OCID of the Vcn which will own the subnet.
    :type vcn_id: str

    :param ig_id: The OCID of the Vcn which will own the subnet.
    :type ig_id: str

    :param display_name: The display name of the RoutingTable to configure.
    :type display_name: str
    """
    # Get the default route table for the Vcn.
    rt = get_unique_route_table_by_name(network_client, compartment_id, vcn_id, display_name)
    route_rules = rt.route_rules
    if len(route_rules) == 0:
        # Create a global access routing rule.
        destination_cidr = "0.0.0.0/0"
        access = core_models.RouteRule(
            cidr_block=destination_cidr, destination=destination_cidr, destination_type="CIDR_BLOCK",
            network_entity_id=ig_id
        )
        route_rules.append(access)
        # Update the route table with the new access rule.
        update = core_models.UpdateRouteTableDetails(route_rules=route_rules)
        network_client.update_route_table(rt.id, update)
        print('Configured Internet Gateway Default Route Table Rules: {}'.format(display_name))


def get_unique_route_table_by_name(network_client, compartment_id, vcn_id, display_name):
    """
    Find a unique RouteTable by name.

    :param network_client: OCI VirtualNetworkClient client
    :type network_client: oci.core.VirtualNetworkClient

    :param compartment_id: The OCID of the compartment which owns the RouteTable.
    :type compartment_id: str

    :param vcn_id: The OCID of the Vcn which will own the RouteTable.
    :type vcn_id: str

    :param display_name: The display name of the RouteTable.
    :type display_name: str

    :return: The RouteTable.
    :rtype: core_models.RouteTable
    """
    result = pagination.list_call_get_all_results(
        network_client.list_route_tables,
        compartment_id,
        vcn_id,
        display_name=display_name
    )
    for rt in result.data:
        if display_name == rt.display_name:
            return rt


def prepare_route_table_for_delete(network_client, rt_id):
    """
    Prepares a DefaultRouteTable for deletion by deleting all RouteRules.

    :param network_client: OCI VirtualNetworkClient client
    :type network_client: oci.core.VirtualNetworkClient

    :param rt_id: The OCID of the RouteTable to clean.
    :type rt_id: str
    """
    update = core_models.UpdateRouteTableDetails(route_rules=[])
    network_client.update_route_table(rt_id, update)
    print('Cleaned Default Route Table Rules: {}'.format(rt_id))


def get_unique_subnet_by_name(network_client, compartment_id, vcn_id, display_name):
    """
    Find a unique Subnet by name.

    :param network_client: OCI VirtualNetworkClient client
    :type network_client: oci.core.VirtualNetworkClient

    :param compartment_id: The OCID of the compartment which owns the VCN.
    :type compartment_id: str

    :param vcn_id: The OCID of the VCN which will own the subnet.
    :type vcn_id: str

    :param display_name: The display name of the subnet.
    :type display_name: str

    :return: The Subnet
    :rtype: core_models.Subnet
    """
    result = pagination.list_call_get_all_results(
        network_client.list_subnets,
        compartment_id,
        vcn_id,
        display_name=display_name
    )
    for subnet in result.data:
        if display_name == subnet.display_name:
            return subnet


def get_unique_application_by_name(fn_management_client, compartment_id, display_name):
    """
    Find a unique Application by name.

    :param fn_management_client: OCI FunctionsManagementClient client
    :type fn_management_client: functions.FunctionsManagementClient

    :param compartment_id: The OCID of the compartment which owns the Application.
    :type compartment_id: str

    :param display_name: The display name of the subnet.
    :type display_name: str

    :return: The Subnet
    :rtype: core_models.Subnet
    """
    result = pagination.list_call_get_all_results(
        fn_management_client.list_applications,
        compartment_id,
        display_name=display_name
    )
    for app in result.data:
        if display_name == app.display_name:
            return app


def get_unique_function_by_name(fn_management_client, application_id, display_name):
    """
    Find a unique Function by name.

    :param fn_management_client: OCI FunctionsManagementClient client.
    :type fn_management_client: functions.FunctionsManagementClient

    :param application_id: The OCID of the Application which owns the Function.
    :type application_id: str

    :param display_name: The display name of the Function.
    :type display_name: str

    :return: The Function.
    :rtype: core_models.Function
    """
    result = pagination.list_call_get_all_results(
        fn_management_client.list_functions,
        application_id,
        display_name=display_name
    )
    for fn in result.data:
        if display_name == fn.display_name:
            return fn


#  === Utility Helpers ===

def vcn_name(name):
    return name + "-vcn"


def ig_name(name):
    return name + "-ig"


def drt_name(name):
    return "Default Route Table for " + name + "-vcn"


def subnet_name(name):
    return name + "-subnet"


def application_name(name):
    return name + "-app"


def function_name(name):
    return name + "-fn"


#  === Main ===

if __name__ == "__main__":
    """
    Setup, invoke, or, teardown a function.

    :param args: The commandline args: setup, invoke, teardown
    :type argv: [str]
    """

    # All resources will be prefixed with this name.
    name = NAME_PREFIX

    # Load OCI credentials from default location and profile.
    cfg = config.from_file(
        file_location=os.getenv(
            "OCI_CONFIG_PATH", config.DEFAULT_LOCATION),
        profile_name=os.getenv(
            "OCI_CONFIG_PROFILE", config.DEFAULT_PROFILE)
    )
    config.validate_config(cfg)

    # All resources will be created in the specified compartment.
    compartment_name = os.environ.get('COMPARTMENT_NAME')
    if compartment_name is not None:
        compartment_id = get_compartment_id(cfg, compartment_name).id
    else:
        compartment_id = os.environ.get('COMPARTMENT_ID')
    if compartment_id is None:
        print("The COMPARTMENT_ID (or COMPARTMENT_NAME) environment variable must be set.")
        sys.exit(1)

    # We need an accessible image to invoke.
    # e.g. phx.ocir.io/tenancy-name/registry/imagename:version
    image = os.environ.get('OCIR_FN_IMAGE')

    # If the target image require input, it can be defined with FN_PAYLOAD
    # environment variable.
    content = os.environ.get('FN_PAYLOAD')
    if content is None:
        content = ""

    # Attempt to setup the minimal OCI resources for a Function.
    if SETUP in sys.argv:
        if image is None:
            print("The OCIR_FN_IMAGE environment variable must be set.")
            sys.exit(1)
        setup_resources(cfg, compartment_id, name, image)

    # Invoke a Function.
    if INVOKE in sys.argv:
        invoke_function(cfg, compartment_id, name, content)

    # Attempt to clean-up resources.
    if TEARDOWN in sys.argv:
        teardown_resources(cfg, compartment_id, name)
