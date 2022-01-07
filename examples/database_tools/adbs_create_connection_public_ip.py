# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


# Creates a connection to an Autonomous Databases with Shared Exadata Infrastructure. With a Public IP.
# - Requires Database Tools Private Endpoint Reverse Connection: No
# - Requires a KeyStore: Yes, for mTLS
#
# 1- Create a new Autonomous Database
# 2- Create required secrets
# 3- Create a connection
# 4- Validate the connection
#
# If variable do_clean_up_at_end is set to True, connection, secrets and DB are removed upon completion.
#
# Prerequisites are:
# - A compartment_id where the vcn, autonomous database, vault and connection will reside.
# - vault_id: a Vault created in KMS with at least one master key.

import oci
from oci.config import from_file, validate_config
from utils.dbtools import get_dbtools_clients, get_database_clients, get_secrets_client, \
    get_kms_vault_client, get_vaults_clients, get_wallet_and_create_secrets, delete_secret

from datetime import datetime, timedelta
import pkg_resources

# Specify Compartment to use for tests
compartment_id = "ocid1.compartment.oc1.changeme"
# Specify Vault id to use in the test. Must be in compartment_id and contain a master Key
vault_id = "ocid1.vault.oc1.phx.changeme"

utc_now = datetime.utcnow()
dbname = "DB" + utc_now.strftime("%m%d%H%M")
db_password = "example-password"

db_password_secret_name = "db" + "this-is-not-the-secret" + dbname
db_wallet_secret_name = "wallet" + "this-is-not-the-secret" + dbname

# Display OCI Python SDK version
print("oci version:", pkg_resources.get_distribution("oci").version)

# Set do_clean_up_at_end to false to keep the autonomous database, secrets and connection created
do_clean_up_at_end = True

# Variables that will be modified during the processing
autonomous_database_id = None
wallet_secret_id = None
password_secret_id = None
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


def create_db(compartment_id, database_name, database_password, db_workload="OLTP"):
    """
    Create an Autonomous Databases with Shared Exadata Infrastructure. With a Public IP.
    """
    global autonomous_database_id

    # If an autonomous db with same name already exists, return the OCID of the existing db
    list_db_response = clients["db_client"].list_autonomous_databases(
        compartment_id=compartment_id,
        display_name=database_name
    )
    assert list_db_response, "List db should return a response"
    if list_db_response.data:
        print(f"DB with name {database_name} already exists. Using: {list_db_response.data[0].id}")
        autonomous_database_id = list_db_response.data[0].id
        return

    # Provision a new Database
    db_details = oci.database.models.CreateAutonomousDatabaseDetails(
        admin_password=database_password,
        compartment_id=compartment_id,
        db_name=database_name,
        display_name=database_name,
        db_workload=db_workload,
        whitelisted_ips=["0.0.0.0/0"],
        cpu_core_count=1,
        data_storage_size_in_tbs=1
    )

    print(f"Creating Database with name {database_name}...")
    create_db_response = clients["db_async_client"].create_autonomous_database_and_wait_for_state(
        create_autonomous_database_details=db_details,
        wait_for_states=["FAILED", "AVAILABLE", "CANCELED"]
    )

    assert create_db_response, "create_autonomous_database_and_wait_for_state should return a response"
    assert create_db_response.data, "DB Response should contain data"

    # Get the OCID for the new Database
    autonomous_database_id = create_db_response.data.id
    print(f"Created Database with name {database_name} and OCID {autonomous_database_id}")


def do_connection_tests():
    """
    Do tests related to DBTools Connections
    - Create Connection
    - Get created connection
    - Update Connection
    - Validate Connection. This makes sure that we can use this connection to connect to the DB.
    """
    global connection_id, wallet_secret_id, password_secret_id
    print("===DBTools Service - Connections")

    # 1.get DB
    autonomous_database_response = clients["db_client"].get_autonomous_database(autonomous_database_id)
    assert autonomous_database_response, "No autonomous database found"
    assert autonomous_database_response.data, "get_autonomous_database should return data"
    autonomous_database = autonomous_database_response.data

    # 2. Prepare Wallet and secrets
    wallet_secret_id, password_secret_id = get_wallet_and_create_secrets(oci_config=oci_config,
                                                                         compartment_id=compartment_id,
                                                                         clients=clients,
                                                                         autonomous_database_id=autonomous_database_id,
                                                                         vault_id=vault_id,
                                                                         db_wallet_secret_name=db_wallet_secret_name,
                                                                         db_password_secret_name=db_password_secret_name,
                                                                         db_password=db_password)

    # 3. get Connection string with mTLS from DB
    assert autonomous_database.connection_strings
    assert autonomous_database.connection_strings.profiles
    profiles = autonomous_database.connection_strings.profiles

    m_tls = oci.database.models.DatabaseConnectionStringProfile.TLS_AUTHENTICATION_MUTUAL
    low = oci.database.models.DatabaseConnectionStringProfile.CONSUMER_GROUP_LOW
    connection_string = next((p.value for p in profiles if
                              p.tls_authentication == m_tls and p.consumer_group == low), None)

    print(f"Using connection_string {connection_string}")

    # 4. create SSO keyStore using wallet_secret_id
    key_store = oci.database_tools.models.DatabaseToolsKeyStoreDetails(
        key_store_type=oci.database_tools.models.DatabaseToolsKeyStoreDetails.KEY_STORE_TYPE_SSO,
        key_store_content=oci.database_tools.models.DatabaseToolsKeyStoreContentSecretIdDetails(
            value_type=oci.database_tools.models.DatabaseToolsKeyStoreContentSecretIdDetails.VALUE_TYPE_SECRETID,
            secret_id=wallet_secret_id)
    )

    #
    # 5. Create connection using:
    #    - DB Compartment
    #    - Connection String
    #    - dbUser
    #    - dbPasswordSecretId
    #    - Time generated display name
    #    - Related Resource
    #    - keyStore
    #
    print("===Connection - Create")
    user_name = "admin"
    user_password = oci.database_tools.models.DatabaseToolsUserPasswordSecretIdDetails(
        secret_id=password_secret_id)

    display_name = "conn_pysdk_" + utc_now.strftime("%Y-%m-%d_%H-%M-%S")
    related_resource = oci.database_tools.models.CreateDatabaseToolsRelatedResourceDetails(
        entity_type=oci.database_tools.models.CreateDatabaseToolsRelatedResourceDetails.ENTITY_TYPE_AUTONOMOUSDATABASE,
        identifier=autonomous_database_id)

    conn_details_for_create = oci.database_tools.models.CreateDatabaseToolsConnectionOracleDatabaseDetails(
        compartment_id=compartment_id,
        connection_string=connection_string,
        user_name=user_name,
        user_password=user_password,
        display_name=display_name,
        related_resource=related_resource,
        key_stores=[key_store]
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
    # 6. Get connection that we just created BY Id
    #
    print("===Connection - Get by id:", connection_id)
    connection = clients["dbtools_client"].get_database_tools_connection(connection_id)
    print("Read created Connection:", connection.data)
    assert connection.data is not None, "Created Connection data should exist"
    assert connection.data.display_name == display_name, "Unexpected Connection display name"
    assert connection.data.lifecycle_state == "ACTIVE", "Connection should be ACTIVE"

    #
    # 7. Update connection that we just created BY Id
    #
    # Changing only the display name.
    print("===Connection - Update by id:", connection_id)
    connection_details_for_update = oci.database_tools.models.UpdateDatabaseToolsConnectionOracleDatabaseDetails(
        display_name=display_name + "_updated")
    result = clients["dbtools_async_client"].update_database_tools_connection_and_wait_for_state(connection_id,
                                                                                                 connection_details_for_update,
                                                                                                 wait_for_states=[
                                                                                                     "FAILED",
                                                                                                     "SUCCEEDED",
                                                                                                     "CANCELED"])
    status = result.data.status
    print(
        f"Updating Connection. Status: {status}, name: {display_name}, connection id: {connection_id}.")
    assert status == "SUCCEEDED", "Update Connection should succeed"

    #
    # 8. Get connection that we just updated BY Id
    #
    print("===Connection - after update - Get by id:", connection_id)
    connection = clients["dbtools_client"].get_database_tools_connection(connection_id)
    assert connection.data is not None, "Updated Connection data should exist"
    assert connection.data.display_name != display_name, "Unexpected Connection display name after update"
    assert connection.data.lifecycle_state == "ACTIVE", "Connection should be ACTIVE after update"

    #
    # 9. Validate Connection
    #
    print("===Connection - Validate by id:", connection_id)
    validate_detail = oci.database_tools.models.ValidateDatabaseToolsConnectionOracleDatabaseDetails(
        type="ORACLE_DATABASE")
    result = clients["dbtools_client"].validate_database_tools_connection(connection_id, validate_detail)
    assert result.data is not None, "validation should return a validation info"
    print("Validation Result:", result.data)
    assert result.data.code == "OK", "validation should pass"


def do_connection_cleanup(conn_id):
    """
    Delete the connection that we used for our tests
    """
    if connection_id:
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


def do_secrets_cleanup(secrets_ids, days=2):
    """
    Delete the secrets that we used in our tests
    """
    # Delete Secret in vault clean-up
    secret_deletion_time = datetime.now() + timedelta(days=days)
    for secret_id in secrets_ids:
        if secret_id:
            delete_secret(clients,
                          secret_id=secret_id,
                          deletion_time=secret_deletion_time)


def do_db_delete(adb_id):
    # Beware, this actually DELETES the specified DB
    clients["db_client"].delete_autonomous_database(adb_id)
    print(f"TERMINATED Autonomous Database: {adb_id}")


#
# main logic
#
if __name__ == "__main__":
    # Output Colors
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    try:
        # Create Autonomous Database
        create_db(compartment_id, dbname, db_password)

        # Create and test Connections
        do_connection_tests()

        print(f"{OKGREEN}Python SDK Test completed OK{ENDC}")
    except Exception as e:
        print(f"{FAIL}Exception during tests:{ENDC} {e}")
    finally:
        # Clean-up
        if do_clean_up_at_end:
            print("Starting resource clean-up.")
            do_connection_cleanup(connection_id)
            do_secrets_cleanup([password_secret_id, wallet_secret_id])
            do_db_delete(autonomous_database_id)
            print("Clean-up completed.")
        else:
            print("Skipping resource clean-up.")
