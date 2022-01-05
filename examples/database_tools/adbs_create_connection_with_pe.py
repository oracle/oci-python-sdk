#!/usr/bin/env python3
"""
Creates a connection to an Autonomous Databases with Shared Exadata Infrastructure (ADB-S) with Private Endpoint (PE)
- Requires Database Tools Private Endpoint Reverse Connection: Yes
- Requires a KeyStore: Yes, for mTLS

1- Create a Database Tools Private Endpoint for A Reverse Connection to the PE of the ADB-S
2- Create required secrets
3- Create a connection
4- Validate the connection

Prerequisites are:
- An ADB-S created following the instructions from: https://docs.oracle.com/en-us/iaas/Content/Database/Concepts/adbsprivateaccess.htm
- A compartment Id where the vcn, autonomous database, vault, private endpoint and connection will reside
- vault_id: a vault created in KMS with at least one master key.
- subnet_id of the Database Tools Private Endpoint and the PE of the ADB-S. Best practice is use separate subnets.
"""
import oci
from oci.config import from_file, validate_config
from utils.dbtools import get_dbtools_clients, get_database_clients, get_secrets_client, \
    get_kms_vault_client, get_vaults_clients, delete_secret, get_wallet_and_create_secrets

from datetime import datetime, timedelta
import pkg_resources

# Specify ADB-S id
autonomous_database_id = "ocid1.autonomousdatabase.oc1.changeme"
# Specify Compartment and subnet to use for tests
compartment_id = "ocid1.compartment.oc1.changeme"
# Specify vault id to use in the test. Must in compartment_name
vault_id = "ocid1.vault.oc1.changeme"
# Specify subnet id
subnet_id = "ocid1.subnet.oc1.changeme"

db_password = "example-password"

utc_now = datetime.utcnow()
db_password_secret_name = "db" + "this-is-not-the-secret" + "dbname"
db_wallet_secret_name = "wallet" + "this-is-not-the-secret" + "dbname"

# Display OCI Python SDK version
print("oci version:", pkg_resources.get_distribution("oci").version)

# Set do_clean_up_at_end to false to keep the Database Tools Private Endpoint, secrets and connection created
do_clean_up_at_end = True

# Variables
wallet_secret_id = None
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
    global connection_id, wallet_secret_id, password_secret_id
    print("===DBTools Service - Connections")

    # 1.get ADB-S
    autonomous_database_response = clients["db_client"].get_autonomous_database(autonomous_database_id)
    assert autonomous_database_response, "No autonomous database found"
    assert autonomous_database_response.data, "should contain data"
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

    # 3. get mTLS Connection string from DB
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
    #    - Related Resource ...
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
        private_endpoint_id=private_endpoint_id,
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
    assert connection.data, "Created Connection data should exist"
    assert connection.data.display_name == display_name, "Unexpected Connection display name"
    assert connection.data.lifecycle_state == "ACTIVE", "Connection should be ACTIVE"

    #
    # 7. Validate Connection
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
                f"delete_database_tools_private_endpoint_and_wait_for_state. Status: {status}, connection id: {pe_id}.")
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
            do_secrets_cleanup([password_secret_id, wallet_secret_id])
            print("Clean-up completed.")
        else:
            print("Skipping resource clean-up.")
