# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import oci


# This script demonstrates some of the Container Engine operations.
# Please review the documentation for more information about
# how Container Engine works, including permissions needed.
#
# https://docs.cloud.oracle.com/Content/ContEng/Concepts/contengoverview.htm

# Note: Exception handling is rudimentary and would need to be expanded for use in
#       production.  Please be aware resources may need to be cleaned up manually
#       if an exception occures.

# Load the default configuration
config = oci.config.from_file()

# This is the root compartment.  You can use another compartment in your tenancy.
compartment_id = config["tenancy"]

print("Compartment id: {}".format(compartment_id))

#############################
# Container Engine operations
#############################


def create_cluster(ce_client, vcn):
    """
    create_cluster

    This function demonstrates the process of creating a cluster.  The cidrs
    and other values are just for demonstration purposes.
    """
    success = True
    kubernetes_network_config = oci.container_engine.models.KubernetesNetworkConfig(pods_cidr="10.244.0.0/16",
                                                                                    services_cidr="10.96.0.0/16")

    cluster_create_options = oci.container_engine.models.ClusterCreateOptions(service_lb_subnet_ids=vcn['lb_subnets'],
                                                                              kubernetes_network_config=kubernetes_network_config)

    cluster_details = oci.container_engine.models.CreateClusterDetails(name="PythonSDK_cluster1",
                                                                       compartment_id=compartment_id,
                                                                       vcn_id=vcn['id'],
                                                                       kubernetes_version=get_kubernetes_version(ce_client),
                                                                       options=cluster_create_options)

    ce_composite_ops = oci.container_engine.ContainerEngineClientCompositeOperations(ce_client)

    response = ce_composite_ops.create_cluster_and_wait_for_state(cluster_details,
                                                                  wait_for_states=[oci.container_engine.models.WorkRequest.STATUS_SUCCEEDED,
                                                                                   oci.container_engine.models.WorkRequest.STATUS_FAILED])

    # response.data is a WorkRequestSummary
    # gather the created resources from the work request
    resources = {}
    for resource in response.data.resources:
        print("{}: {}".format(resource.entity_type, resource.identifier))
        resources[resource.entity_type] = resource.identifier

    # If the workrequest failed, get the work request errors.
    if response.data.status == oci.container_engine.models.WorkRequest.STATUS_FAILED:
        get_work_request_errors(ce_client, compartment_id, response.data.id)
        success = False
    else:
        print("Create cluster succeed")

    # Get the work request logs
    print_header("Work request logs:")
    response = ce_client.list_work_request_logs(compartment_id, response.data.id)
    print(response.data)

    return success, resources


def update_cluster(ce_client, cluster_id):
    """
    update_cluster

    Currently there are two items you can update on the cluster the name and the kubernetes version.
    This function demonstrates updating the name.  Updating the kubernetes version works in
    a similar fashion.
    """

    update_cluster_details = oci.container_engine.models.UpdateClusterDetails(name="PythonSDK_cluster_1")

    ce_composite_ops = oci.container_engine.ContainerEngineClientCompositeOperations(ce_client)

    response = ce_composite_ops.update_cluster_and_wait_for_state(cluster_id,
                                                                  update_cluster_details,
                                                                  wait_for_states=[oci.container_engine.models.WorkRequest.STATUS_SUCCEEDED,
                                                                                   oci.container_engine.models.WorkRequest.STATUS_FAILED])

    # If the workrequest failed, get the work request errors.
    if response.data.status == oci.container_engine.models.WorkRequest.STATUS_FAILED:
        get_work_request_errors(ce_client, compartment_id, response.data.id)
    else:
        print("Update cluster succeeded")

    return


def delete_cluster(ce_client, cluster_id):
    """
    delete_cluster

    Delete the clusted associated with the cluster_id passed in
    """
    ce_composite_ops = oci.container_engine.ContainerEngineClientCompositeOperations(ce_client)

    response = ce_composite_ops.delete_cluster_and_wait_for_state(cluster_id,
                                                                  wait_for_states=[oci.container_engine.models.WorkRequest.STATUS_SUCCEEDED])

    if response.status == 200:
        print("Cluster deleted successfully")
    else:
        print("Recieved '{}' when attempting to delete the cluster".format(response.status))

    return


def get_kubeconfig(ce_client, cluster_id):
    """
    get_kubeconfig

    Given a cluster id, retrieve the kubconfig.
    """

    response = ce_client.create_kubeconfig(cluster_id)

    # response.data.text contains the contents of the kubeconfig file which
    # can be writen to a file using code like the following snippet.
    """
    with open('kubconfig.txt', 'w') as f:
        f.write(response.data.text)
    """
    if response.data.text:
        print("kubeconfig retrieved")
    else:
        print("Error retrieving the kubeconfig")

    return


def create_node_pool(ce_client, ads, cluster_id, subnet):
    """
    create_node_pool

    Creates a node pool inside of a cluser
    """
    node_pool_placement_configs_details = []
    for ad in ads:
        node_pool_placement_configs_details.append(oci.container_engine.models.NodePoolPlacementConfigDetails(
            availability_domain=ad,
            subnet_id=subnet)
        )

    create_node_pool_node_config_details = oci.container_engine.models.CreateNodePoolNodeConfigDetails(
        size=len(ads),
        placement_configs=node_pool_placement_configs_details
    )

    success = True
    node_pool_create_details = oci.container_engine.models.CreateNodePoolDetails(compartment_id=compartment_id,
                                                                                 cluster_id=cluster_id,
                                                                                 name="PythonSDK_nodepool1",
                                                                                 kubernetes_version=get_kubernetes_version(ce_client),
                                                                                 node_image_name="Oracle-Linux-7.4",
                                                                                 node_shape="VM.Standard1.1",
                                                                                 initial_node_labels=[{"nodes": "Example Nodes"}],
                                                                                 node_config_details=create_node_pool_node_config_details)

    ce_composite_ops = oci.container_engine.ContainerEngineClientCompositeOperations(ce_client)

    response = ce_composite_ops.create_node_pool_and_wait_for_state(node_pool_create_details,
                                                                    wait_for_states=[oci.container_engine.models.WorkRequest.STATUS_SUCCEEDED,
                                                                                     oci.container_engine.models.WorkRequest.STATUS_FAILED])

    # gather the created resources from the work request
    resources = {}
    for resource in response.data.resources:
        resources[resource.entity_type] = resource.identifier

    # If the workrequest failed, get the work request errors.
    if response.data.status == oci.container_engine.models.WorkRequest.STATUS_FAILED:
        get_work_request_errors(ce_client, compartment_id, response.data.id)
        success = False
    else:
        print("Create node pool succeeded")

    return success, resources


def update_node_pool(ce_client, node_pool_id):
    """
    update_node_pool

    Currently there are a number of features that can be updated in the node pool.
    This example will only update the name.  Please see the documentation for
    the other features which can be updated
    """

    update_node_pool_details = oci.container_engine.models.UpdateNodePoolDetails(name="PythonSDK_noodpool_1")

    ce_composite_ops = oci.container_engine.ContainerEngineClientCompositeOperations(ce_client)

    response = ce_composite_ops.update_node_pool_and_wait_for_state(node_pool_id,
                                                                    update_node_pool_details,
                                                                    wait_for_states=[oci.container_engine.models.WorkRequest.STATUS_SUCCEEDED,
                                                                                     oci.container_engine.models.WorkRequest.STATUS_FAILED])

    if response.data.status == oci.container_engine.models.WorkRequest.STATUS_FAILED:
        get_work_request_errors(ce_client, compartment_id, response.data.id)
    else:
        print("Update node pool succeeded")

    return


def delete_node_pool(ce_client, node_pool_id):
    """
    delete_node_pool

    Deletes the specified node pool.  The cluster is not deleted.
    """
    ce_composite_ops = oci.container_engine.ContainerEngineClientCompositeOperations(ce_client)

    response = ce_composite_ops.delete_node_pool_and_wait_for_state(node_pool_id,
                                                                    wait_for_states=[oci.container_engine.models.WorkRequest.STATUS_SUCCEEDED])

    if response.status == 200:
        print("Node pool deleted successfully")
    else:
        print("Recieved '{}' when attempting to delete the node pool".format(response.status))

    return


def get_kubernetes_version(ce_client):
    """
    get_kubernetes_version

    Get the supported kubernetes versions from the service.  There are multiple
    versions supported but for the example we will just use the last one in the
    list.
    """
    response = ce_client.get_cluster_options(cluster_option_id="all")

    versions = response.data.kubernetes_versions
    if len(versions) > 0:
        kubernetes_version = versions[-1]
    else:
        raise RuntimeError("No supported Kubernetes versions found")

    return kubernetes_version

################
# VCN operations
################


def create_vcn(vn_client, ads, number_of_worker_subnets=1, number_of_lb_subnets=1):
    """
    create_vcn

    See https://docs.cloud.oracle.com/Content/ContEng/Concepts/contengnetworkconfig.htm#VCN
    for details on how the VCN should be configured for container engine.

    This function will build a Virtual Cloud Network based on the example network resource configuration:
    https://docs.cloud.oracle.com/Content/ContEng/Concepts/contengnetworkconfigexample.htm

    The function returns a dictionary containing the id of the VCN created, a list of worker subnets and
    a list of load balancer subnets
    """

    vcn = {'id': None,
           'worker_subnets': [],
           'lb_subnets': []}

    subnet_template = "10.0.{}.0/24"

    vn_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(vn_client)

    vcn_details = oci.core.models.CreateVcnDetails(cidr_block='10.0.0.0/16',
                                                   display_name='PythonSDKContainerEngineExampleVcn',
                                                   dns_label='cevcn',
                                                   compartment_id=compartment_id,
                                                   )

    result = vn_composite_ops.create_vcn_and_wait_for_state(vcn_details,
                                                            wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE])

    vcn['id'] = result.data.id
    print("VCN Id: {}".format(vcn['id']))

    # Setup the gateway
    gateway_details = oci.core.models.CreateInternetGatewayDetails(compartment_id=compartment_id,
                                                                   display_name='PythonCE-gateway-0',
                                                                   is_enabled=True,
                                                                   vcn_id=vcn['id'])

    result = vn_composite_ops.create_internet_gateway_and_wait_for_state(gateway_details,
                                                                         wait_for_states=[oci.core.models.InternetGateway.LIFECYCLE_STATE_AVAILABLE])

    gateway_id = result.data.id
    print('Gateway Id: {}'.format(gateway_id))

    # Setup the route table
    route_table_rule = oci.core.models.RouteRule(cidr_block=None,
                                                 destination='0.0.0.0/0',
                                                 destination_type='CIDR_BLOCK',
                                                 network_entity_id=gateway_id)

    route_table_details = oci.core.models.CreateRouteTableDetails(compartment_id=compartment_id,
                                                                  display_name='PythonCE-routetable-0',
                                                                  route_rules=[route_table_rule],
                                                                  vcn_id=vcn['id'])

    result = vn_composite_ops.create_route_table_and_wait_for_state(route_table_details,
                                                                    wait_for_states=[oci.core.models.RouteTable.LIFECYCLE_STATE_AVAILABLE])

    route_table_id = result.data.id
    print('Route Table Id: {}'.format(route_table_id))

    ################
    # Security Lists and Security Rules
    # More information on the security list configuration for container engine can be found here:
    # https://docs.cloud.oracle.com/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig
    ################

    # Load balancer security rules
    load_balancer_egress_rule = oci.core.models.EgressSecurityRule(destination='0.0.0.0/0',
                                                                   destination_type=oci.core.models.EgressSecurityRule.DESTINATION_TYPE_CIDR_BLOCK,
                                                                   is_stateless=True,
                                                                   protocol='6',
                                                                   tcp_options=oci.core.models.TcpOptions())

    load_balancer_ingress_rule = oci.core.models.IngressSecurityRule(source='0.0.0.0/0',
                                                                     source_type=oci.core.models.IngressSecurityRule.SOURCE_TYPE_CIDR_BLOCK,
                                                                     is_stateless=True,
                                                                     protocol='6',
                                                                     tcp_options=oci.core.models.TcpOptions())

    load_balancers_security_list_details = oci.core.models.CreateSecurityListDetails(compartment_id=compartment_id,
                                                                                     display_name='PythonCE-LB-SecurityList',
                                                                                     egress_security_rules=[load_balancer_egress_rule],
                                                                                     ingress_security_rules=[load_balancer_ingress_rule],
                                                                                     vcn_id=vcn['id'])

    result = vn_composite_ops.create_security_list_and_wait_for_state(load_balancers_security_list_details,
                                                                      wait_for_states=[oci.core.models.SecurityList.LIFECYCLE_STATE_AVAILABLE])

    load_balancer_security_list_id = result.data.id
    print('Load Balancer Security List Id: {}'.format(load_balancer_security_list_id))

    # Worker security rules
    worker_egress_rules = []

    for i in range(number_of_worker_subnets):
        destination = subnet_template.format(10 + i)
        worker_egress_rules.append(oci.core.models.EgressSecurityRule(destination=destination,
                                                                      destination_type=oci.core.models.EgressSecurityRule.DESTINATION_TYPE_CIDR_BLOCK,
                                                                      is_stateless=True,
                                                                      protocol='all'))

    worker_egress_rules.append(oci.core.models.EgressSecurityRule(destination='0.0.0.0/0',
                                                                  destination_type=oci.core.models.EgressSecurityRule.DESTINATION_TYPE_CIDR_BLOCK,
                                                                  is_stateless=False,
                                                                  protocol='all'))
    worker_ingress_rules = []

    for i in range(number_of_worker_subnets):
        source = subnet_template.format(10 + i)
        worker_ingress_rules.append(oci.core.models.IngressSecurityRule(source=source,
                                                                        source_type=oci.core.models.IngressSecurityRule.SOURCE_TYPE_CIDR_BLOCK,
                                                                        is_stateless=True,
                                                                        protocol='all'))

    worker_ingress_rules.append(oci.core.models.IngressSecurityRule(source='0.0.0.0/0',
                                                                    source_type=oci.core.models.IngressSecurityRule.SOURCE_TYPE_CIDR_BLOCK,
                                                                    is_stateless=False,
                                                                    protocol='1',
                                                                    icmp_options=oci.core.models.IcmpOptions(type=3, code=4)))

    worker_ingress_rules.append(oci.core.models.IngressSecurityRule(source='130.35.0.0/16',
                                                                    source_type=oci.core.models.IngressSecurityRule.SOURCE_TYPE_CIDR_BLOCK,
                                                                    is_stateless=False,
                                                                    protocol='6',
                                                                    tcp_options=oci.core.models.TcpOptions(destination_port_range=oci.core.models.PortRange(min=22, max=22))))

    worker_ingress_rules.append(oci.core.models.IngressSecurityRule(source='138.1.0.0/17',
                                                                    source_type=oci.core.models.IngressSecurityRule.SOURCE_TYPE_CIDR_BLOCK,
                                                                    is_stateless=False,
                                                                    protocol='6',
                                                                    tcp_options=oci.core.models.TcpOptions(destination_port_range=oci.core.models.PortRange(min=22, max=22))))

    worker_ingress_rules.append(oci.core.models.IngressSecurityRule(source='0.0.0.0/0',
                                                                    source_type=oci.core.models.IngressSecurityRule.SOURCE_TYPE_CIDR_BLOCK,
                                                                    is_stateless=False,
                                                                    protocol='6',
                                                                    tcp_options=oci.core.models.TcpOptions(destination_port_range=oci.core.models.PortRange(min=22, max=22))))

    worker_security_list_details = oci.core.models.CreateSecurityListDetails(compartment_id=compartment_id,
                                                                             display_name='PythonCE-Worker-SecurityList',
                                                                             egress_security_rules=worker_egress_rules,
                                                                             ingress_security_rules=worker_ingress_rules,
                                                                             vcn_id=vcn['id'])

    result = vn_composite_ops.create_security_list_and_wait_for_state(worker_security_list_details,
                                                                      wait_for_states=[oci.core.models.SecurityList.LIFECYCLE_STATE_AVAILABLE])

    worker_security_list_id = result.data.id
    print('Worker Security List Id: {}'.format(worker_security_list_id))

    ################
    # Subnets
    # More information on the subnet configuration for container engine can be found here:
    # https://docs.cloud.oracle.com/Content/ContEng/Concepts/contengnetworkconfig.htm#subnetconfig
    ################

    # Worker subnets
    display_name_template = 'PythonSDKCE-workers-{}'
    dns_label_template = 'workers{}'
    for i in range(number_of_worker_subnets):
        cidr_block = subnet_template.format(10 + i)
        display_name = display_name_template.format(1 + i)
        dns_label = dns_label_template.format(1 + i)

        subnet_details = oci.core.models.CreateSubnetDetails(compartment_id=compartment_id,
                                                             cidr_block=cidr_block,
                                                             display_name=display_name,
                                                             dns_label=dns_label,
                                                             vcn_id=vcn['id'],
                                                             route_table_id=route_table_id,
                                                             security_list_ids=[worker_security_list_id])

        result = vn_composite_ops.create_subnet_and_wait_for_state(subnet_details,
                                                                   wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE])
        vcn['worker_subnets'].append(result.data.id)

    print("Worker Subnets: {}".format(vcn['worker_subnets']))

    # Load balancer subnets
    display_name_template = 'PythonSDKCE-loadbalancers-{}'
    dns_label_template = 'loadbalancers{}'
    for i in range(number_of_lb_subnets):
        cidr_block = subnet_template.format(20 + i)
        display_name = display_name_template.format(1 + i)
        dns_label = dns_label_template.format(1 + i)
        subnet_details = oci.core.models.CreateSubnetDetails(compartment_id=compartment_id,
                                                             cidr_block=cidr_block,
                                                             display_name=display_name,
                                                             dns_label=dns_label,
                                                             vcn_id=vcn['id'],
                                                             route_table_id=route_table_id,
                                                             security_list_ids=[load_balancer_security_list_id])

        result = vn_composite_ops.create_subnet_and_wait_for_state(subnet_details,
                                                                   wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE])
        vcn['lb_subnets'].append(result.data.id)

    print("Loadbalancer Subnets: {}".format(vcn['lb_subnets']))

    return vcn


def delete_vcn(vn_client, vcn_resources):
    """
    delete_vcn

    Deletes the example VCN.  There are more resources associated
    with the VCN than passed in with the vcn_resources dictionary.  Those
    resources will be discovered and deleted.
    """

    vn_composite_ops = oci.core.VirtualNetworkClientCompositeOperations(vn_client)

    # Delete the load balancer subnets
    print("Deleting load balancer subnets...")
    for subnet in vcn_resources['lb_subnets']:
        vn_composite_ops.delete_subnet_and_wait_for_state(subnet,
                                                          wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED])

    # Delete the worker subnets
    print("Deleting worker subnets...")
    for subnet in vcn_resources['worker_subnets']:
        vn_composite_ops.delete_subnet_and_wait_for_state(subnet,
                                                          wait_for_states=[oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED])

    # VCNs have default security lists, route tables which cannot be deleted.
    # Get the details of the VCN to get the default security list and default route table ids so
    # they can be skipped when getting the security lists and route tables
    response = vn_client.get_vcn(vcn_resources['id'])
    default_security_list_id = response.data.default_security_list_id
    default_route_table_id = response.data.default_route_table_id

    # Retrieve and delete the security lists
    print("Deleting security lists...")
    # We could just retrieve all of the security lists, but there may be cases where not all of them
    # would come back in a single page.  Here is another example of using the pagaination to
    # retrieve items from a list call.  More examples are in pagination.py
    for security_list in oci.pagination.list_call_get_all_results_generator(vn_client.list_security_lists,
                                                                            'record',
                                                                            compartment_id,
                                                                            vcn_resources['id'],
                                                                            lifecycle_state=oci.core.models.SecurityList.LIFECYCLE_STATE_AVAILABLE):
        if security_list.id != default_security_list_id:
            vn_composite_ops.delete_security_list_and_wait_for_state(security_list.id,
                                                                     wait_for_states=[oci.core.models.SecurityList.LIFECYCLE_STATE_TERMINATED])

    # Retrieve and delete the route tables
    print("Deleting route tables...")
    for route_table in oci.pagination.list_call_get_all_results_generator(vn_client.list_route_tables,
                                                                          'record',
                                                                          compartment_id,
                                                                          vcn_resources['id'],
                                                                          lifecycle_state=oci.core.models.RouteTable.LIFECYCLE_STATE_AVAILABLE):
        if route_table.id != default_route_table_id:
            vn_composite_ops.delete_route_table_and_wait_for_state(route_table.id,
                                                                   wait_for_states=[oci.core.models.RouteTable.LIFECYCLE_STATE_TERMINATED])

    # Retrieve and delete the gateway
    print("Deleting internet gateways...")
    for gateway in oci.pagination.list_call_get_all_results_generator(vn_client.list_internet_gateways,
                                                                      'record',
                                                                      compartment_id,
                                                                      vcn_resources['id'],
                                                                      lifecycle_state=oci.core.models.InternetGateway.LIFECYCLE_STATE_AVAILABLE):
        vn_composite_ops.delete_internet_gateway_and_wait_for_state(gateway.id, wait_for_states=[oci.core.models.InternetGateway.LIFECYCLE_STATE_TERMINATED])

    print("Deleting virtual cloud network...")
    response = vn_composite_ops.delete_vcn_and_wait_for_state(vcn_resources['id'],
                                                              wait_for_states=[oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED])

    print("VCN {} has been deleted".format(vcn_resources['id']))


#########
# Helpers
#########

def get_work_request_errors(ce_client, compartment_id, work_request_id):
    """
    get_work_request_errors

    Retrieves the errors for a work request and prints them.
    """
    print_header('Work request errors:')
    response = ce_client.list_work_request_errors(compartment_id, work_request_id)
    print(response.data)


def print_header(header):
    """
    print_header

    Prints a section header
    """

    print('\n')
    print(header)
    print("=" * len(header))


if __name__ == "__main__":
    # Initialize clients
    ce_client = oci.container_engine.ContainerEngineClient(config)
    vn_client = oci.core.VirtualNetworkClient(config)
    id_client = oci.identity.IdentityClient(config)

    # Get the Availability Domains for the compartment
    response = id_client.list_availability_domains(compartment_id)
    ads = [x.name for x in response.data]

    try:
        ##################
        # Create resources
        ##################
        print_header("Create the Virtual Cloud Network")
        vcn_resources = create_vcn(vn_client, ads)
        print("VNC resources: {}".format(vcn_resources))

        print_header("Create the Cluster")
        cluster_success, cluster_resources = create_cluster(ce_client, vcn_resources)
        print("Cluster resourse: {}".format(cluster_resources)),

        if cluster_success:
            print_header('Create a node pool')
            node_pool_success, node_pool_resources = create_node_pool(ce_client,
                                                                      ads,
                                                                      cluster_resources['cluster'],
                                                                      vcn_resources['worker_subnets'][0])
            print("Node pool resources: {}".format(node_pool_resources))

        if cluster_success:
            print_header("Get kubeconf")
            get_kubeconfig(ce_client, cluster_resources['cluster'])

        ##################
        # Update resources
        ##################

        if cluster_success:
            print_header("Update the Cluster")
            update_cluster(ce_client, cluster_resources['cluster'])

        if cluster_success and node_pool_success:
            print_header('Update the node pool')
            update_node_pool(ce_client, node_pool_resources['nodepool'])

    finally:
        ####################
        # Delete resources
        ####################

        # Note: Any exceptions caught while trying to clean up resources are printed, but not
        #       handled.
        if node_pool_resources:
            print_header('Delete the node pool')
            try:
                delete_node_pool(ce_client, node_pool_resources['nodepool'])
            except Exception as e:
                print("Failed to delete node pool: {}".format(node_pool_resources['nodepool']))
                print(e)

        if cluster_resources:
            print_header("Delete the Cluster")
            try:
                delete_cluster(ce_client, cluster_resources['cluster'])
            except Exception as e:
                print("Failed to delete cluster: {}".format(cluster_resources['cluster']))
                print(e)

        print_header("Delete the Virtual Cloud Network")
        try:
            delete_vcn(vn_client, vcn_resources)
        except Exception as e:
            print("Failed to delete VCN: {}".format(vcn_resources['id']))
            print(e)
