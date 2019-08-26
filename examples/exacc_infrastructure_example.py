# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of how use database CLI in terms of:
#   - Creating an Exadata Infrastructure at Customer Cloud

# Usage: python exacc_infrastructure_example.py <Compartment OCID> <Activation Key File Path>

# This script takes the following arguments:
#
#   * The compartment in which infrastructure will be created
#   * The path to the key file for activation


import oci
import sys
import random
import string


def random_string(elements, num):
    result = ''
    for _ in range(num):
        result += random.choice(elements)
    return result


shape = 'Exadata.Quarter3.100'
time_zone = 'UTC'
display_name = 'Exacc_Infra_'.join(random_string(string.ascii_lowercase, 8))

if len(sys.argv) < 3:
    print("Missing the required arguments! an OCID of the compartment and path to the key file for activation")

# cloud_control_plane_server1 and cloud_control_plane_server1 must be a valid unused IP within the admin network CIDR
admin_network_cidr = '0.31.16.0/20'
cloud_control_plane_server1 = '10.31.153.83'
cloud_control_plane_server2 = '10.31.153.84'
corporate_proxy = 'fake-proxy.us.oracle.com'
dns_server = ['10.89.138.33']
ntp_server = ['10.89.138.33']
infini_band_network_cidr = ['192.168.31.0/24']
gateway = '10.31.16.1'
netmask = '255.255.240.0'

compartment_id = sys.argv[1]
activation_key_file = sys.argv[2]


config = oci.config.from_file()
client = oci.database.DatabaseClient(config)
client_composite_ops = oci.database.DatabaseClientCompositeOperations(client)

create_infrastructure_details = oci.database.models.CreateExadataInfrastructureDetails(
    compartment_id=compartment_id,
    display_name=display_name,
    shape=shape,
    time_zone=time_zone,
    cloud_control_plane_server1=cloud_control_plane_server1,
    cloud_control_plane_server2=cloud_control_plane_server2,
    gateway=gateway,
    netmask=netmask,
    infini_band_network_cidr=infini_band_network_cidr,
    corporate_proxy=corporate_proxy,
    admin_network_cidr=admin_network_cidr,
    dns_server=dns_server,
    ntp_server=ntp_server
)

# Create exadata infrastructure
# We can wait until the Exadata Infrastructure is in REQUIRES_ACTIVATION state.

life_cycle_creation_succeed_state = oci.database.models.ExadataInfrastructure.LIFECYCLE_STATE_REQUIRES_ACTIVATION
exacc_infra = client_composite_ops.create_exadata_infrastructure_and_wait_for_state(
    create_infrastructure_details,
    [life_cycle_creation_succeed_state]
)

infrastructure_ocid = exacc_infra.data.id


new_netmask = '255.255.240.1'

update_infrastructure_details = oci.database.models.UpdateExadataInfrastructureDetails(
    netmask=new_netmask
)

exacc_infra_updated = client_composite_ops.update_exadata_infrastructure_and_wait_for_state(infrastructure_ocid, update_infrastructure_details, [life_cycle_creation_succeed_state])

print(exacc_infra_updated.data)

activate_exadata_infrastructure_details = oci.database.models.ActivateExadataInfrastructureDetails(
    activation_file=activation_key_file
)


life_cycle_activation_succeed_state = oci.database.models.ExadataInfrastructure.LIFECYCLE_STATE_ACTIVE
exacc_infra_activated = client_composite_ops.activate_exadata_infrastructure_and_wait_for_state(infrastructure_ocid, activate_exadata_infrastructure_details, [life_cycle_activation_succeed_state])

print(exacc_infra_activated.data)

life_cycle_deletion_succeed_state = oci.database.models.ExadataInfrastructure.LIFECYCLE_STATE_DELETED
exacc_infra_deleted = client_composite_ops.delete_exadata_infrastructure_and_wait_for_state(infrastructure_ocid, [life_cycle_deletion_succeed_state])

print(exacc_infra_deleted.data)

print('Deleted Exadata Infrastructure')
