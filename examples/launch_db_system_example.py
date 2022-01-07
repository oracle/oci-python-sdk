# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to launch a DB system using the Python SDK. This script will:
#
#   * Create a VCN and subnet for the DB system and its related resources
#   * Launch a DB system containing a single DB home and database. See:
#     https://docs.cloud.oracle.com/Content/Database/Concepts/overview.htm and
#     https://docs.cloud.oracle.com/Content/Database/Tasks/launchingDB.htm
#     for more information
#   * Demonstrate listing and retrieving information on individual DB systems, DB homes and databases
#   * Demonstrate taking action on nodes
#
# Resources created by the script will be removed when the script is done.
#
# This script takes the following arguments:
#
#   * The compartment which owns the DB system
#   * The availability domain where the DB system will be launched
#   * The CIDR block for the VCN and subnet (these will use the same CIDR)
#   * The path to the public SSH key which can be used for SSHing into the DB system
#
# This script also makes assumptions on the following database parameters:
#
#   * Core count
#   * DB edition
#   * DB version
#   * Dummy password

import oci
import os.path
import sys

ADMIN_PASSWORD = "ADummyPassw0rd_#1"
DB_VERSION = '12.1.0.2'
DB_SYSTEM_CPU_CORE_COUNT = 4
DB_SYSTEM_DB_EDITION = 'ENTERPRISE_EDITION'
DB_SYSTEM_SHAPE = 'BM.DenseIO1.36'


def create_vcn(virtual_network, compartment_id, cidr_block):
    vcn_name = 'py_sdk_example_vcn'
    result = virtual_network.create_vcn(
        oci.core.models.CreateVcnDetails(
            cidr_block=cidr_block,
            display_name=vcn_name,
            compartment_id=compartment_id,
            dns_label='pysdkex'
        )
    )
    get_vcn_response = oci.wait_until(
        virtual_network,
        virtual_network.get_vcn(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    )
    print('Created VCN: {}'.format(get_vcn_response.data.id))

    return get_vcn_response.data


def delete_vcn(virtual_network, vcn):
    composite_virtual_network = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)
    composite_virtual_network.delete_vcn_and_wait_for_state(
        vcn.id,
        [oci.core.models.Vcn.LIFECYCLE_STATE_TERMINATED]
    )
    print('Deleted VCN: {}'.format(vcn.id))


def create_subnet(virtual_network, vcn, availability_domain):
    subnet_name = 'py_sdk_example_subnet1'
    result = virtual_network.create_subnet(
        oci.core.models.CreateSubnetDetails(
            compartment_id=vcn.compartment_id,
            availability_domain=availability_domain,
            display_name=subnet_name,
            vcn_id=vcn.id,
            cidr_block=vcn.cidr_block,
            dns_label='pysdksubex'
        )
    )
    get_subnet_response = oci.wait_until(
        virtual_network,
        virtual_network.get_subnet(result.data.id),
        'lifecycle_state',
        'AVAILABLE'
    )
    print('Created Subnet: {}'.format(get_subnet_response.data.id))

    return get_subnet_response.data


def delete_subnet(virtual_network, subnet):
    composite_virtual_network = oci.core.VirtualNetworkClientCompositeOperations(virtual_network)
    composite_virtual_network.delete_subnet_and_wait_for_state(
        subnet.id,
        [oci.core.models.Subnet.LIFECYCLE_STATE_TERMINATED]
    )


def list_db_system_shapes(database_client, compartment_id):
    # We can list the different database shapes available to us. This is a paginated operation so we can use the functions
    # in oci.pagination to get all the results without having to manually deal with page tokens
    list_db_shape_results = oci.pagination.list_call_get_all_results(
        database_client.list_db_system_shapes,
        availability_domain=availability_domain,
        compartment_id=compartment_id
    )

    print('\nDB System Shapes')
    print('===========================')
    print('{}\n\n'.format(list_db_shape_results.data))


def list_db_versions(database_client, compartment_id):
    # We can list DB versions. This is a paginated operation so we can use the functions in oci.pagination to get
    # all the results without having to manually deal with page tokens
    list_db_version_results = oci.pagination.list_call_get_all_results(
        database_client.list_db_versions,
        compartment_id=compartment_id
    )

    print('\nDB Versions')
    print('===========================')
    print('{}\n\n'.format(list_db_version_results.data))

    # We can do some additional filtering so that only versions compatible with a given shape are returned. Note
    # the usage of the db_system_shape keword argument
    list_db_version_results = oci.pagination.list_call_get_all_results(
        database_client.list_db_versions,
        compartment_id=compartment_id,
        db_system_shape=DB_SYSTEM_SHAPE
    )

    print('\nDB Versions by shape: {}'.format(DB_SYSTEM_SHAPE))
    print('===========================')
    print('{}\n\n'.format(list_db_version_results.data))


def list_db_home_and_databases_under_db_system(database_client, compartment_id, db_system):
    # A DB System contains DB Homes and the DB Homes contain databases. First, let's find the DB homes for the
    # DB system by listing them. Listing is a paginated operation so we can use the functions in oci.pagination
    # here
    list_db_homes_response = oci.pagination.list_call_get_all_results(
        database_client.list_db_homes,
        compartment_id=compartment_id,
        db_system_id=db_system.id
    )
    print('\nDB Homes For DB System')
    print('===========================')
    print('{}\n\n'.format(list_db_homes_response.data))

    # The results returned in the list operation are DbHomeSummary objects. We can also call get_db_home to fetch
    # the full information about the DB home
    db_home_summary = list_db_homes_response.data[0]
    db_home = database_client.get_db_home(db_home_summary.id).data
    print('\nGet DB Home')
    print('===============')
    print('{}\n\n'.format(db_home))

    # DB Homes contain databases. We can find the databases in a DB home by listing them. This is a paginated
    # operation so we can use the functions in oci.pagination here
    list_databases_response = oci.pagination.list_call_get_all_results(
        database_client.list_databases,
        compartment_id=compartment_id,
        db_home_id=db_home.id
    )
    print('\nDatabases For DB Home')
    print('===========================')
    print('{}\n\n'.format(list_databases_response.data))

    # The results returned in the list operation are DatabaseSummary objects. We can also call get_database to fetch
    # the full information about the DB home
    database_summary = list_databases_response.data[0]
    database = database_client.get_database(database_summary.id).data
    print('\nGet Database')
    print('===============')
    print('{}\n\n'.format(database))


if len(sys.argv) != 5:
    raise RuntimeError('Invalid number of arguments provided to the script. Consult the script header for required arguments')

compartment_id = sys.argv[1]
availability_domain = sys.argv[2]
cidr_block = sys.argv[3]
ssh_public_key_path = os.path.expandvars(os.path.expanduser(sys.argv[4]))

# Default config file and profile
config = oci.config.from_file()
database_client = oci.database.DatabaseClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)

list_db_system_shapes(database_client, compartment_id)
list_db_versions(database_client, compartment_id)

vcn = None
subnet = None
try:
    vcn = create_vcn(virtual_network_client, compartment_id, cidr_block)
    subnet = create_subnet(virtual_network_client, vcn, availability_domain)

    with open(ssh_public_key_path, mode='r') as file:
        ssh_key = file.read()

    launch_db_system_details = oci.database.models.LaunchDbSystemDetails(
        availability_domain=availability_domain,
        compartment_id=compartment_id,
        cpu_core_count=DB_SYSTEM_CPU_CORE_COUNT,
        database_edition=DB_SYSTEM_DB_EDITION,
        db_home=oci.database.models.CreateDbHomeDetails(
            db_version=DB_VERSION,
            display_name='py sdk example db home',
            database=oci.database.models.CreateDatabaseDetails(
                admin_password=ADMIN_PASSWORD,
                db_name='testdb'
            )
        ),
        display_name='testdb',
        hostname='pysdk-example-db-host',
        shape=DB_SYSTEM_SHAPE,
        ssh_public_keys=[ssh_key],
        subnet_id=subnet.id
    )

    launch_response = database_client.launch_db_system(launch_db_system_details)
    print('\nLaunched DB System')
    print('===========================')
    print('{}\n\n'.format(launch_response.data))

    # We can wait until the DB system is available. A DB system can take some time to launch (e.g. on the order
    # of magnitude of hours) so we can change the max_interval_seconds and max_wait_seconds to account for this.
    # The wait_until defaults of checking every 30 seconds and waiting for a maximum of 1200 seconds (20 minutes)
    # may not be sufficient.
    #
    # In the below example, we check every 900 seconds (15 minutes) and wait a max of 21600 seconds (6 hours)
    get_db_system_response = oci.wait_until(
        database_client,
        database_client.get_db_system(launch_response.data.id),
        'lifecycle_state',
        'AVAILABLE',
        max_interval_seconds=900,
        max_wait_seconds=21600
    )

    print('\nDB System Available')
    print('===========================')
    print('{}\n\n'.format(get_db_system_response.data))

    list_db_home_and_databases_under_db_system(database_client, compartment_id, get_db_system_response.data)

    # Once we're done with the DB system, we can terminate it and wait for it to be terminated. We also use
    # succeed_on_not_found for the waiter in case the DB system is no longer returned by get_db_system calls
    # as that implies our delete/termination has succeeded.
    #
    # In this basic scenario where we have a single DB system, DB home and database, terminating the DB system
    # will also delete the DB home and database.
    get_db_system_response = database_client.get_db_system(launch_response.data.id)
    database_client.terminate_db_system(get_db_system_response.data.id)
    oci.wait_until(
        database_client,
        get_db_system_response,
        'lifecycle_state',
        'TERMINATED',
        succeed_on_not_found=True
    )
    print('Terminated DB system')
finally:
    if subnet:
        delete_subnet(virtual_network_client, subnet)

    if vcn:
        delete_vcn(virtual_network_client, vcn)
