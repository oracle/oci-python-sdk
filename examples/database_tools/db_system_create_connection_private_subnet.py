# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


# Creates a connection to a VM DB System with Private Endpoint (PE) in a Private Subnet
# - Requires Database Tools Private Endpoint Reverse Connection: Yes
# - Requires a KeyStore: No
#
# 1- Create a Database Tools Private Endpoint for A Reverse Connection to the VM DB System
# 2- Create required secrets
# 3- Create a connection
# 4- Validate the connection
#
# Prerequisites are:
# - An DB system created following the instructions from: https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/creatingDBsystem.htm with NSG for port 1521
# - A compartment Id where the vcn, DB System, vault, private endpoint and connection will reside
# - vault_id: a vault created in KMS with at least one master key.
# - subnet_id of the Database Tools Private Endpoint and the DB system. Best practice is to use a private subnet.

import oci
from oci.config import from_file, validate_config
from utils.dbtools import get_dbtools_clients, get_database_clients, get_secrets_client, \
    get_kms_vault_client, get_vaults_clients, create_secret, delete_secret

from datetime import datetime, timedelta
import pkg_resources
import base64

# Specify Compartment and subnet to use for tests
compartment_id = "ocid1.compartment.oc1.changeme"
# Specify vault id to use in the test. Must in compartment_name
vault_id = "ocid1.vault.oc1.changeme"
# Specify subnet id
subnet_id = "ocid1.subnet.oc1.changeme"
# Specify VM DB System Id
db_system_id = "ocid1.dbsystem.oc1.changeme"
# Specify VM DB Password
db_password = "example-password"

utc_now = datetime.utcnow()
db_password_secret_name = "db_password_SDK_" + utc_now.strftime("%m-%d%.%H%M")

# Display OCI Python SDK version
print("oci version:", pkg_resources.get_distribution("oci").version)

# Set do_clean_up_at_end to false to keep the Database Tools Private Endpoint, secrets and connection created
do_clean_up_at_end = True

# Variables that will be modified during the processing
vault_key_id = None
password_secret_id = None
private_endpoint_id = None
connection_id = None

# Load OCI Config
oci_config = from_file(file_location="~/.oci/config", profile_name="DEFAULT")

# Validate OCI Config
validate_config(oci_config)

# Prepare all clients that we will need
db_client, db_async_client = get_database_clients(oci_config)
vaults_client, vaults_async_client = get_vaults_clients(oci_config)
kms_vault_client = get_kms_vault_client(oci_config)
secrets_client = get_secrets_client(oci_config)
dbtools_client, dbtools_async_client = get_dbtools_clients(oci_config)

# Prepare a dict that contains all the required clients
clients = {"db_client": db_client, "db_async_client": db_async_client,
           "vaults_client": vaults_client, "vaults_async_client": vaults_async_client,
           "kms_vault_client": kms_vault_client,
           "secrets_client": secrets_client,
           "dbtools_client": dbtools_client, "dbtools_async_client": dbtools_async_client}


def get_endpoint_services():
    """
    DBTools Endpoints Services
    """
    print("===DBTools Service - Endpoint Services")

    endpoint_services_response = clients["dbtools_client"].list_database_tools_endpoint_services(compartment_id)

    assert endpoint_services_response, "list_database_tools_endpoint_services should return a response"
    assert endpoint_services_response.data, "endpoint_services should return data"
    assert endpoint_services_response.data.items, "endpoint_services should contain a list of endpoints"

    # Use the first endpoint_service
    endpoint_service = endpoint_services_response.data.items[0]
    print(f"===Endpoints Services - Using {endpoint_service}.")
    assert endpoint_service.lifecycle_state == "ACTIVE", "endpoint_service must be ACTIVE"

    return endpoint_service.id


def create_private_endpoint(endpoint_service_id):
    """
    Create a DBTools Private Endpoint
    """
    global private_endpoint_id

    print("===DBTools Service - Private Endpoints")

    #
    # Create a Database Tools Private Endpoint
    #
    display_name = "pe_pysdk_" + utc_now.strftime("%Y-%m-%d_%H-%M-%S")
    description = "test with Python SDK"
    pe_details_for_create = oci.database_tools.models.CreateDatabaseToolsPrivateEndpointDetails(
        compartment_id=compartment_id,
        endpoint_service_id=endpoint_service_id,
        subnet_id=subnet_id,
        display_name=display_name,
        description=description)
    print("===Private Endpoint - Create")
    create_pe_response = clients["dbtools_async_client"].create_database_tools_private_endpoint_and_wait_for_state(
        pe_details_for_create, wait_for_states=["FAILED", "SUCCEEDED", "CANCELED"])

    assert create_pe_response, "create_database_tools_private_endpoint_and_wait_for_state should return a response"
    assert create_pe_response.data, "create_database_tools_private_endpoint_and_wait_for_state should return data"

    status = create_pe_response.data.status
    private_endpoint_id = create_pe_response.data.resources[0].identifier
    print(f"Database Tools Private Endpoint created. Status: {status}, name: {display_name}, pe id: {private_endpoint_id}.")
    assert status == "SUCCEEDED", "Create Private Endpoint should succeed"

    #
    # Get the Private Endpoint by Id
    #
    print("===Private endpoints - Get by id:", private_endpoint_id)
    get_pe_response = clients["dbtools_client"].get_database_tools_private_endpoint(private_endpoint_id)
    print("Read created Private Endpoint:", get_pe_response.data)
    assert get_pe_response, "get_database_tools_private_endpoint should return a response"
    assert get_pe_response.data, "get_database_tools_private_endpoint should return data"
    assert get_pe_response.data.lifecycle_state == "ACTIVE", "Private Endpoint should be ACTIVE"


def create_connection():
    """
    Do tests related to DBTools Connections
    - Create Connection
    - Get created connection
    - Validate Connection. This makes sure that we can use this connection to connect to the ADB-S.
    """
    global connection_id, password_secret_id, vault_key_id
    print("===DBTools Service - Connections")

    # 1. Get Connection String for VM DB System
    #
    # - List dbHomes in compartment for our dbSystemId
    #   - Take the first
    # - List database in compartment for the dbHome of our DB System
    #   - Take the 1 one that matches dbSystemId
    # - List pdbs in database
    #   - Take the 1 one/
    #   - connection string is in pdb_default of the connection strings.

    # List db_homes in compartment for our db_system_id
    db_homes_response = clients["db_client"].list_db_homes(
        compartment_id=compartment_id,
        db_system_id=db_system_id
    )
    assert db_homes_response, "list_db_homes should return a response"
    assert db_homes_response.data, "list_db_homes should return data"
    db_home = db_homes_response.data[0]
    db_home_id = db_home.id

    # List databases in compartment for the dbHome of our DB System
    databases_response = clients["db_client"].list_databases(
        compartment_id=compartment_id,
        db_home_id=db_home_id
    )
    assert databases_response, "list_databases should return a response"
    assert databases_response.data, "list_databases should return data"
    database_summary = databases_response.data[0]

    assert database_summary.db_system_id == db_system_id, "This database should be for our VM DB System"
    print("database:", database_summary)

    # List pdbs in database
    pdbs_response = clients["db_client"].list_pluggable_databases(
        database_id=database_summary.id
    )
    assert pdbs_response, "list_pluggable_databases should return a response"
    assert pdbs_response.data, "list_pluggable_databases should return data"
    pdb = pdbs_response.data[0]

    assert pdb.connection_strings, "pdb should have connection_strings"
    assert pdb.connection_strings.pdb_default, "pdb should have a default pdb connection_string"
    connection_string = pdb.connection_strings.pdb_default
    print(f"Using connection_string {connection_string}")

    # 4. Store the DB password in the vault as a secret under name X. If name X already exists, we will simply use it.
    base64_db_password_str = base64.b64encode(db_password.encode()).decode()
    password_secret_id, vault_key_id = create_secret(oci_config,
                                                     compartment_id=compartment_id,
                                                     clients=clients,
                                                     vault_id=vault_id,
                                                     vault_key_id=vault_key_id,
                                                     name=db_password_secret_name,
                                                     base64_password=base64_db_password_str)

    #
    # 2. Create connection using:
    #    - DB Compartment
    #    - Connection String
    #    - dbUser
    #    - dbPasswordSecretId
    #    - Time generated display name
    #    - Related Resource
    #    - Advanced property since we want to connect with SYS as SYSDBA
    #
    print("===Connection - Create")
    user_name = "system"
    user_password = oci.database_tools.models.DatabaseToolsUserPasswordSecretIdDetails(
        secret_id=password_secret_id)

    display_name = "conn_pysdk_" + utc_now.strftime("%Y-%m-%d_%H-%M-%S")
    related_resource = oci.database_tools.models.CreateDatabaseToolsRelatedResourceDetails(
        entity_type=oci.database_tools.models.CreateDatabaseToolsRelatedResourceDetails.ENTITY_TYPE_PLUGGABLEDATABASE,
        identifier=db_system_id)

    conn_details_for_create = oci.database_tools.models.CreateDatabaseToolsConnectionOracleDatabaseDetails(
        compartment_id=compartment_id,
        connection_string=connection_string,
        user_name=user_name,
        user_password=user_password,
        display_name=display_name,
        private_endpoint_id=private_endpoint_id,
        related_resource=related_resource
    )
    create_conn_response = clients["dbtools_async_client"].create_database_tools_connection_and_wait_for_state(
        conn_details_for_create, wait_for_states=["FAILED", "SUCCEEDED", "CANCELED"])

    assert create_conn_response, "create_database_tools_connection_and_wait_for_state should return a response"
    assert create_conn_response.data, "Create db Response should contain data"

    status = create_conn_response.data.status
    connection_id = create_conn_response.data.resources[0].identifier
    print(f"Creating Connection. Status: {status}, name: {display_name}, connection id: {connection_id}.")
    assert status == "SUCCEEDED", "Create Connection should succeed"

    #
    # 3. Get connection that we just created BY Id
    #
    print("===Connection - Get by id:", connection_id)
    connection = clients["dbtools_client"].get_database_tools_connection(connection_id)
    print("Read created Connection:", connection.data)
    assert connection.data, "Created Connection data should exist"
    assert connection.data.display_name == display_name, "Unexpected Connection display name"
    assert connection.data.lifecycle_state == "ACTIVE", "Connection should be ACTIVE"

    #
    # 4. Validate Connection
    #
    print("===Connection - Validate by id:", connection_id)
    validate_detail = oci.database_tools.models.ValidateDatabaseToolsConnectionOracleDatabaseDetails(
        type="ORACLE_DATABASE")
    result = clients["dbtools_client"].validate_database_tools_connection(connection_id, validate_detail)
    assert result.data, "Validation should return a validation info"
    print("Validation Result:", result.data)
    assert result.data.code == "OK", "Created connection should be valid"


def do_connection_cleanup(conn_id):
    """
    Delete the connection that we used for our tests
    """
    if conn_id:
        print("===Connection - Delete by id:", conn_id)
        result = clients["dbtools_async_client"].delete_database_tools_connection_and_wait_for_state(conn_id,
                                                                                                     wait_for_states=[
                                                                                                         "FAILED",
                                                                                                         "SUCCEEDED",
                                                                                                         "CANCELED"])

        if result and result.data:
            status = result.data.status
            print(
                f"delete_database_tools_connection_and_wait_for_state. Status: {status}, connection id: {conn_id}.")
            assert status == "SUCCEEDED", "Delete Connection should succeed"
        else:
            print("Error. do_connection_tests_cleanup failed")
    else:
        print("Error. do_connection_tests_cleanup skipped")


def do_private_endpoint_cleanup(pe_id):
    """
    Delete the Database Tools Private endpoint that we used for our tests
    """
    if pe_id:
        print("===Private Endpoint - Delete by id:", pe_id)
        result = clients["dbtools_async_client"].delete_database_tools_private_endpoint_and_wait_for_state(pe_id,
                                                                                                           wait_for_states=[
                                                                                                               "FAILED",
                                                                                                               "SUCCEEDED",
                                                                                                               "CANCELED"])

        if result and result.data:
            status = result.data.status
            print(
                f"delete_database_tools_private_endpoint_and_wait_for_state. Status: {status}, connection id: {private_endpoint_id}.")
            assert status == "SUCCEEDED", "Delete Private Endpoint should succeed"
        else:
            print("Error. do_private_endpoint_cleanup failed")
    else:
        print("Error. do_private_endpoint_cleanup skipped")


def do_secrets_cleanup(secrets_ids, days=2):
    """
    Delete the secrets that we used for our tests
    """
    # Delete Secret in vault clean-up
    secret_deletion_time = datetime.now() + timedelta(days=days)
    for secret_id in secrets_ids:
        if secret_id:
            delete_secret(clients,
                          secret_id=secret_id,
                          deletion_time=secret_deletion_time)


#
# main logic
#
if __name__ == "__main__":
    # Output Colors
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    try:
        # Endpoint Service
        endpoint_service_id = get_endpoint_services()

        # Create a Database Tools Private Endpoint
        create_private_endpoint(endpoint_service_id)

        # Create and Validate a Database Tools Connection
        create_connection()

        print(f"{OKGREEN}Python SDK Test completed OK{ENDC}")
    except Exception as e:
        print(f"{FAIL}Exception during tests:{ENDC} {e}")
    finally:
        # Clean-up
        if do_clean_up_at_end:
            print("Starting resource clean-up.")
            do_connection_cleanup(connection_id)
            do_private_endpoint_cleanup(private_endpoint_id)
            do_secrets_cleanup([password_secret_id])
            print("Clean-up completed.")
        else:
            print("Skipping resource clean-up.")
