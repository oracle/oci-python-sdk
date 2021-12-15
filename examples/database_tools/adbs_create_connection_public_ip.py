#!/usr/bin/env python3
"""
Creates a connection to an Autonomous Databases with Shared Exadata Infrastructure. With a Public IP.
- Requires Database Tools Private Endpoint Reverse Connection: No
- Requires a KeyStore: Yes, for mTLS

1- Create a new Autonomous Database
2- Create required secrets
3- Create a connection
4- Validate the connection

If variable do_clean_up_at_end is set to True, connection, secrets and DB are removed upon completion.

Pre-requisite are:
- A compartment_id where the vcn, autonomous database, vault and connection will reside.
- vault_id: a Vault created in KMS with at least one master key.

"""
import oci
from oci.config import from_file, validate_config

from datetime import datetime, timedelta
import pkg_resources
from zipfile import ZipFile
import io
import base64

# Specify Compartment and subnet to use for tests
compartment_id = "ocid1.compartment.oc1.changeme"
# Specify vault id to use in the test. Must be in compartment_id and contain a master Key
vault_id = "ocid1.vault.oc1.phx.changeme"

dbname = "DB12151133"
db_password = "ChangeMe1111####"

db_password_secret_name = "db_password_SDK" + dbname
db_wallet_secret_name = "wallet_SDK_" + dbname

# Display OCI Python SDK version
print("oci version:", pkg_resources.get_distribution("oci").version)

# Set do_clean_up_at_end to false to keep the autonomous database, secrets and connection created
do_clean_up_at_end = True

# Variables
vault_key_id = None
autonomous_database_id = None
wallet_secret_id = None
password_secret_id = None
connection_id = None

# Load OCI Config
oci_config = from_file(file_location="~/.oci/config", profile_name="DEFAULT")

# Validate OCI Config
validate_config(oci_config)


def get_dbtools_clients(oci_config):
    client = oci.database_tools.DatabaseToolsClient(config=oci_config)
    # Composite client waits for async operations to complete.
    composite_client = oci.database_tools.DatabaseToolsClientCompositeOperations(client)
    return client, composite_client


def get_database_client(oci_config):
    client = oci.database.DatabaseClient(config=oci_config)
    # Composite client waits for async operations to complete.
    composite_client = oci.database.DatabaseClientCompositeOperations(client)
    return client, composite_client


def get_secrets_client(oci_config):
    client = oci.secrets.SecretsClient(config=oci_config)
    return client


def get_kms_vault_client(oci_config):
    client = oci.key_management.KmsVaultClient(config=oci_config)
    return client


def get_kms_management_client(oci_config, service_endpoint):
    client = oci.key_management.KmsManagementClient(config=oci_config, service_endpoint=service_endpoint)
    return client


def get_vaults_client(oci_config):
    client = oci.vault.VaultsClient(config=oci_config)
    # Composite client waits for async operations to complete.
    composite_client = oci.vault.VaultsClientCompositeOperations(client)
    return client, composite_client


# Prepare all clients that we will need
db_client, db_async_client = get_database_client(oci_config)
vaults_client, vaults_async_client = get_vaults_client(oci_config)
kms_vault_client = get_kms_vault_client(oci_config)
secrets_client = get_secrets_client(oci_config)
dbtools_client, dbtools_async_client = get_dbtools_clients(oci_config)


def extract_zip(input_zip):
    """
    Return a dict of Key=filename with Value=content from a zipped file
    """
    input_zip = ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}


def create_db(compartment_id, database_name, database_password, db_workload="OLTP"):
    """
    Create an Autonomous Databases with Shared Exadata Infrastructure. With a Public IP.
    """
    global autonomous_database_id

    # If an autonomous db with same name already exists, return the OCID of the existing db
    list_db_response = db_client.list_autonomous_databases(
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
    create_db_response = db_async_client.create_autonomous_database_and_wait_for_state(
        create_autonomous_database_details=db_details,
        wait_for_states=["FAILED", "AVAILABLE", "CANCELED"]
    )

    assert create_db_response, "create_autonomous_database_and_wait_for_state should return a response"
    assert create_db_response.data, "DB Response should contain data"

    # Get the OCID for the new Database
    autonomous_database_id = create_db_response.data.id
    print(f"Created Database with name {database_name} and OCID {autonomous_database_id}")


def extract_vault_first_master_key():
    """
    Extract the first Master key from the Vault
    """
    global vault_key_id

    if vault_key_id is None:
        vault_response = kms_vault_client.get_vault(vault_id)
        assert vault_response, "get_vault should return a response"
        assert vault_response.data, "Vault Response should contain data"

        print(f"Vault {vault_id} management endpoint is {vault_response.data.management_endpoint}")
        kms_management_client = get_kms_management_client(oci_config,
                                                          service_endpoint=vault_response.data.management_endpoint)

        # Note: Vault must be in same compartment as DB
        keys_response = kms_management_client.list_keys(compartment_id)
        assert keys_response, "list_keys should return a response"
        assert keys_response.data, "KMS Response should contain data"
        vault_key_id = next((k.id for k in keys_response.data), None)
        print(f"Vault {vault_id} key id is {vault_key_id}")


def create_secret(name: str, base64Secret: str):
    """
    Create a secret using the specified name. The content is in base64Secret.
    If a secret with that name already exists, we simply return its OCID.
    """
    extract_vault_first_master_key()  # Make sure that we have a master key

    try:
        print("Trying to read the secret by name before creating it...")
        bundle_response = secrets_client.get_secret_bundle_by_name(secret_name=name, vault_id=vault_id, stage="CURRENT")
        if bundle_response is not None and \
                bundle_response.data is not None \
                and bundle_response.data.secret_id is not None:
            secret_id = bundle_response.data.secret_id
            print(f"Secret with name {name} found! It will be used instead, secret id: {secret_id}")
            return secret_id
    except Exception:
        print(f"Secret with name {name} not found, it will be created...")

    secret_details = oci.vault.models.CreateSecretDetails(
        vault_id=vault_id,
        key_id=vault_key_id,
        compartment_id=compartment_id,
        secret_name=name,
        secret_content=oci.vault.models.Base64SecretContentDetails(
            content=base64Secret
        )
    )

    create_secret_response = vaults_async_client.create_secret_and_wait_for_state(
        secret_details, wait_for_states=["FAILED", "ACTIVE", "CANCELED"])
    assert create_secret_response, "create_secret_and_wait_for_state should return a response"
    assert create_secret_response.data, "Secret Response should contain data"

    status = create_secret_response.data.lifecycle_state
    secret_id = create_secret_response.data.id
    assert status == "ACTIVE", "Creating Secret should succeed"
    print(f"Created Secret. Status: {status}, name: {name}, secret id: {secret_id}.")
    return secret_id


def delete_secret(secret_id, deletion_time):
    print(f"Deleting secret id {secret_id}")
    secret_deletion_details = oci.vault.models.ScheduleSecretDeletionDetails(
        time_of_deletion=deletion_time
    )

    # Mark the secret for deletion
    delete_secret_response = vaults_client.schedule_secret_deletion(secret_id, secret_deletion_details)
    assert delete_secret_response, "schedule_secret_deletion should return a response"


def get_wallet_and_create_secrets():
    """
    Extract the wallet from the Autonomous Database
    We will store the wallet as a Secret in the vault
    We will also store the database password as a Secret in the vault
    """
    global wallet_secret_id, password_secret_id

    # We will extract wallet and prepare to store wallet as a secret under name X. If name X already exists,
    # we will simply use it.
    print("Extracting Wallet from DB and storing in Vault")

    # 1. Get DB
    autonomous_database_response = db_client.get_autonomous_database(autonomous_database_id)
    assert autonomous_database_response, "get_autonomous_database should return a response"
    assert autonomous_database_response.data, "Autonomous db Response should contain data"

    # 2. Extract Wallet from DB
    # Create a wallet details object
    db_wallet = oci.database.models.GenerateAutonomousDatabaseWalletDetails(
        password="Welcome9"
    )

    print("Extracting Wallet...")
    # Generate the wallet and store the response object
    db_wallet_response = db_client.generate_autonomous_database_wallet(
        autonomous_database_id=autonomous_database_id,
        generate_autonomous_database_wallet_details=db_wallet,
    )

    assert db_wallet_response, "no wallet returned"
    assert db_wallet_response.data, "no wallet data returned"
    assert db_wallet_response.data.content, "no wallet content data returned"

    # Unzip the Wallet in memory to extract the SSO
    filename_to_extract = "cwallet.sso"
    mem_file = io.BytesIO(db_wallet_response.data.content)
    zip_data = extract_zip(mem_file)
    sso_data = zip_data.get(filename_to_extract, None)
    assert sso_data, f"{filename_to_extract} not found in wallet"
    base64_sso_str = base64.b64encode(sso_data).decode()

    # 3. Store Wallet in vault and get that secret (Might already be there
    wallet_secret_id = create_secret(db_wallet_secret_name, base64_sso_str)

    # 4. Store the DB password in the vault as a secret under name X. If name X already exists, we will simply use it.
    base64_db_password_str = base64.b64encode(db_password.encode()).decode()
    password_secret_id = create_secret(db_password_secret_name, base64_db_password_str)


def do_connection_tests():
    """
    Do tests related to DBTools Connections
    - Create Connection
    - Get created connection
    - Update Connection
    - Validate Connection. This makes sure that we can use this connection to connect to the DB.
    """
    global connection_id
    print("===DBTools Service - Connections")

    # 1.get DB
    autonomous_database_response = db_client.get_autonomous_database(autonomous_database_id)
    assert autonomous_database_response, "No autonomous database found"
    assert autonomous_database_response.data, "should contain data"
    autonomous_database = autonomous_database_response.data

    # 2. Prepare Wallet and secrets
    get_wallet_and_create_secrets()

    # 3. get Connection string with mTLS from DB
    assert autonomous_database.connection_strings
    assert autonomous_database.connection_strings.profiles
    profiles = autonomous_database.connection_strings.profiles

    connection_string = next((p.value for p in profiles if
                              p.tls_authentication == oci.database.models.DatabaseConnectionStringProfile.TLS_AUTHENTICATION_MUTUAL
                              and p.consumer_group == oci.database.models.DatabaseConnectionStringProfile.CONSUMER_GROUP_LOW), None)

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

    utc_now = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    display_name = "conn_pysdk_" + utc_now
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
    create_db_response = dbtools_async_client.create_database_tools_connection_and_wait_for_state(
        conn_details_for_create, wait_for_states=["FAILED", "SUCCEEDED", "CANCELED"])

    assert create_db_response, "create_database_tools_connection_and_wait_for_state should return a response"
    assert create_db_response.data, "Create db Response should contain data"

    status = create_db_response.data.status
    connection_id = create_db_response.data.resources[0].identifier
    print(f"Creating Connection. Status: {status}, name: {display_name}, connection id: {connection_id}.")
    assert status == "SUCCEEDED", "Create Connection should succeed"

    #
    # 6. Get connection that we just created BY Id
    #
    print("===Connection - Get by id:", connection_id)
    connection = dbtools_client.get_database_tools_connection(connection_id)
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
    result = dbtools_async_client.update_database_tools_connection_and_wait_for_state(connection_id,
                                                                                      connection_details_for_update,
                                                                                      wait_for_states=["FAILED",
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
    connection = dbtools_client.get_database_tools_connection(connection_id)
    assert connection.data is not None, "Updated Connection data should exist"
    assert connection.data.display_name != display_name, "Unexpected Connection display name after update"
    assert connection.data.lifecycle_state == "ACTIVE", "Connection should be ACTIVE after update"

    #
    # 9. Validate Connection
    #
    print("===Connection - Validate by id:", connection_id)
    validate_detail = oci.database_tools.models.ValidateDatabaseToolsConnectionOracleDatabaseDetails(
        type="ORACLE_DATABASE")
    result = dbtools_client.validate_database_tools_connection(connection_id, validate_detail)
    assert result.data is not None, "validation should return a validation info"
    print("Validation Result:", result.data)
    assert result.data.code == "OK", "validation should pass"


def do_connection_tests_cleanup():
    """
    Delete the connection that we used for our tests
    """
    if connection_id:
        print("===Connection - Delete by id:", connection_id)
        result = dbtools_async_client.delete_database_tools_connection_and_wait_for_state(connection_id,
                                                                                          wait_for_states=["FAILED",
                                                                                                           "SUCCEEDED",
                                                                                                           "CANCELED"])

        if result and result.data:
            status = result.data.status
            print(
                f"delete_database_tools_connection_and_wait_for_state. Status: {status}, connection id: {connection_id}.")
            assert status == "SUCCEEDED", "Delete Connection should succeed"
        else:
            print("Error. do_connection_tests_cleanup failed")
    else:
        print("Error. do_connection_tests_cleanup skipped")


def do_secrets_cleanup():
    """
    Delete the secrets that we used for our tests
    """
    # Delete Secret in vault clean-up
    secret_deletion_time = datetime.now() + timedelta(days=2)
    if password_secret_id:
        delete_secret(password_secret_id, secret_deletion_time)
    if password_secret_id:
        delete_secret(wallet_secret_id, secret_deletion_time)


def do_db_delete():
    # Beware, this actually DELETES the specified DB
    db_client.delete_autonomous_database(autonomous_database_id)
    print(f"TERMINATED Autonomous Database: {autonomous_database_id}")


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
            do_connection_tests_cleanup()
            do_secrets_cleanup()
            do_db_delete()
            print("Clean-up completed.")
        else:
            print("Skipping resource clean-up.")
