# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# -----------------------------------------------------------------------------
# Example Use Case: Existing ADB-S with Public IP (no ACL)
# -----------------------------------------------------------------------------
# This example creates a Database Tools connection to an Autonomous Database
# on shared Exadata infrastructure (ADB-S), accessible by public ip. Note, since
# this connection will be against a public ip address, a Database Tools private
# endpoint is not required, however, mTLS is required.
#
# Prerequisites:
#
#  - A compartment where Autonomous Database, vault, and connection will reside
#  - An existing vault for storage of secrets, with at least one master key
#  - A previously configured .oci/config file with a [DEFAULT] section
#  - Set the following variables in the code below:
#      + compartment_id    : The compartment to use with the example
#      + vault_id          : The ocid for a vault (to store secrets)
#      + db_password       : The database password for the ADMIN user
#
# High-level Steps:
#
#  1- Create a new Autonomous Database (ADB-S)
#  2- Create required secrets
#  3- Create a connection
#  4- Validate the connection
# -----------------------------------------------------------------------------

import oci
from oci.config import from_file, validate_config
from utils.dbtools import get_dbtools_clients, get_database_clients, get_secrets_client, get_kms_vault_client
from utils.dbtools import get_vaults_clients, get_wallet_and_create_secrets, delete_secret

import pkg_resources
from datetime import datetime, timedelta

# Set do_clean_up_at_end = False to keep the secrets and connection created
do_clean_up_at_end = True

# Specify compartment ocid to use. (can also use tenancy ocid if applicable)
compartment_id = "ocid1.tenancy......changeme"

# Specify vault ocid to use. (For this example, vault must be in compartment_id and contain a master key)
vault_id = "ocid1.vault.....changeme"

# Specify the password for the ADB-S database ADMIN user
db_password = "example-password"

print("Using oci version:", pkg_resources.get_distribution("oci").version)


class DBToolsExample:
    """
    A Database Tools example that demonstrates usage of the OCI Python SDK.
    """
    def __init__(self, compartment, vault, password):

        # Load an OCI config with the DEFAULT profile
        self.oci_config = from_file(file_location="~/.oci/config", profile_name="DEFAULT")

        self.compartment_id = compartment
        self.vault_id = vault
        self.db_password = password

        self.db_name = "DB" + datetime.utcnow().strftime("%m%d%H%M")

        validate_config(self.oci_config)

        # Prepare SDK clients used in this example
        self.dbtools_client, self.dbtools_async_client = get_dbtools_clients(self.oci_config)
        self.db_client, self.db_async_client = get_database_clients(self.oci_config)
        self.vaults_client, self.vaults_async_client = get_vaults_clients(self.oci_config)
        self.kms_vault_client = get_kms_vault_client(self.oci_config)
        self.secrets_client = get_secrets_client(self.oci_config)

        # Dict that contains all the clients (used by utils.dbtools helpers)
        self.clients = {"dbtools_client": self.dbtools_client, "dbtools_async_client": self.dbtools_async_client,
                        "db_client": self.db_client, "db_async_client": self.db_async_client,
                        "vaults_client": self.vaults_client, "vaults_async_client": self.vaults_async_client,
                        "kms_vault_client": self.kms_vault_client,
                        "secrets_client": self.secrets_client}

        self.autonomous_database_id = None  # populated at runtime
        self.wallet_secret_id = None        # populated at runtime
        self.password_secret_id = None      # populated at runtime
        self.connection_id = None           # populated at runtime
        self.connection_string = None       # populated at runtime

        # When waiting for asynchronous calls, which status is considered "done"
        self.terminal_states = ["FAILED", "SUCCEEDED", "CANCELED", "AVAILABLE"]

    def create_db(self, db_workload="OLTP"):
        """
        Create an Autonomous Database with shared Exadata infrastructure and a public ip.
        """
        print("=== DBTools Example - Create Autonomous Database Named:", self.db_name)

        response = self.db_client.list_autonomous_databases(
            compartment_id=self.compartment_id,
            display_name=self.db_name)

        assert response, "list_autonomous_databases should return a response"

        # If a database with same name already exists, abort the example to avoid
        # accidentally deleting an existing Autonomous Database
        assert len(response.data) == 0, f"a database with the name {self.db_name} should not already exist"

        db_details = oci.database.models.CreateAutonomousDatabaseDetails(
            admin_password=self.db_password,
            compartment_id=self.compartment_id,
            db_name=self.db_name,
            display_name=self.db_name,
            db_workload=db_workload,
            whitelisted_ips=["0.0.0.0/0"],
            cpu_core_count=1,
            data_storage_size_in_tbs=1)

        create_db_response = self.db_async_client.create_autonomous_database_and_wait_for_state(
            create_autonomous_database_details=db_details,
            wait_for_states=self.terminal_states)

        assert create_db_response, "create_autonomous_database_and_wait_for_state should return a response"
        assert create_db_response.data.id, "create_db_response data should contain an id"

        self.autonomous_database_id = create_db_response.data.id
        print(f"Created database. Name: {self.db_name}, ocid: {self.autonomous_database_id}")

    def save_secrets_to_vault(self):
        """
        Database Tools connections don't store secrets directly. Instead, they hold a pointer to
        secrets stored securely in a vault.
        """
        print("=== DBTools Example - Save Secrets to Vault")

        db_wallet_secret_name = "dbtools-temp-secretw-" + datetime.utcnow().strftime("%m%d%H%M")
        db_password_secret_name = "dbtools-temp-secretp-" + datetime.utcnow().strftime("%m%d%H%M")

        # The wallet zip file generated by the Autonomous Database contains the cwallet.sso file
        # needed to establish an mTLS connection. Extract this and store it as a base64 encoded
        # secret in the vault, along with a new secret for the database password.

        response = self.db_client.get_autonomous_database(self.autonomous_database_id)
        assert response, "get_autonomous_database should return a response"
        assert response.data, "response should contain data"
        autonomous_database = response.data

        self.wallet_secret_id, self.password_secret_id = get_wallet_and_create_secrets(oci_config=self.oci_config,
                                                                                       compartment_id=self.compartment_id,
                                                                                       clients=self.clients,
                                                                                       autonomous_database_id=self.autonomous_database_id,
                                                                                       vault_id=self.vault_id,
                                                                                       db_wallet_secret_name=db_wallet_secret_name,
                                                                                       db_password_secret_name=db_password_secret_name,
                                                                                       db_password=self.db_password)

        # Get the connection string with mTLS from the database
        assert autonomous_database.connection_strings, "autonomous_database should have connection strings"
        assert autonomous_database.connection_strings.profiles, "connection_strings should have profiles"

        profiles = autonomous_database.connection_strings.profiles
        m_tls = oci.database.models.DatabaseConnectionStringProfile.TLS_AUTHENTICATION_MUTUAL
        low = oci.database.models.DatabaseConnectionStringProfile.CONSUMER_GROUP_LOW
        self.connection_string = next((p.value for p in profiles if
                                       p.tls_authentication == m_tls and p.consumer_group == low), None)

        print(f"Created secret. Name: {db_wallet_secret_name}, ocid: {self.wallet_secret_id}")
        print(f"Created secret. Name: {db_password_secret_name}, ocid: {self.password_secret_id}")

    def create_connection(self):
        """
        Given the configuration details provided above and the secrets stored in the vault,
        create a Database Tools connection to the Autonomous Database.
        """
        print("=== DBTools Example - Create Connection Using:", self.connection_string)

        # Setup SSO key store using wallet_secret_id (required for mTLS)
        key_store = oci.database_tools.models.DatabaseToolsKeyStoreDetails(
            key_store_type=oci.database_tools.models.DatabaseToolsKeyStoreDetails.KEY_STORE_TYPE_SSO,
            key_store_content=oci.database_tools.models.DatabaseToolsKeyStoreContentSecretIdDetails(
                value_type=oci.database_tools.models.DatabaseToolsKeyStoreContentSecretIdDetails.VALUE_TYPE_SECRETID,
                secret_id=self.wallet_secret_id))

        # ADMIN is automatically created when deploying a new Autonomous Database
        user_name = "admin"
        user_password = oci.database_tools.models.DatabaseToolsUserPasswordSecretIdDetails(
            secret_id=self.password_secret_id)

        display_name = "conn_pysdk_" + datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        related_resource = oci.database_tools.models.CreateDatabaseToolsRelatedResourceDetails(
            entity_type=oci.database_tools.models.CreateDatabaseToolsRelatedResourceDetails.ENTITY_TYPE_AUTONOMOUSDATABASE,
            identifier=self.autonomous_database_id)

        conn_details_for_create = oci.database_tools.models.CreateDatabaseToolsConnectionOracleDatabaseDetails(
            compartment_id=self.compartment_id,
            connection_string=self.connection_string,
            user_name=user_name,
            user_password=user_password,
            display_name=display_name,
            related_resource=related_resource,
            key_stores=[key_store])

        response = self.dbtools_async_client.create_database_tools_connection_and_wait_for_state(
            conn_details_for_create, wait_for_states=self.terminal_states)

        assert response, "create_database_tools_connection_and_wait_for_state should return a response"
        assert response.data, "response should contain data"
        assert response.data.resources, "response data should return resources"

        status = response.data.status
        assert status == "SUCCEEDED", f"create connection should return status SUCCEEDED but was {status}"

        self.connection_id = response.data.resources[0].identifier
        print(f"Created connection. Name: {display_name}, ocid: {self.connection_id}.")

    def get_connection(self):
        """
        Given an existing Database Tools connection, this method shows how to get the connection by id.
        """
        print("=== DBTools Connection - Get by id:", self.connection_id)

        response = self.dbtools_client.get_database_tools_connection(self.connection_id)
        assert response.data, "response should contain data"
        assert response.data.lifecycle_state == "ACTIVE", f"lifecycle_state should be ACTIVE but was {response.data.lifecycle_state}"

        print("Read created connection:", response.data)

    def update_connection(self):
        """
        Given an existing Database Tools connection, this method shows how to update the connection by id.
        """
        print("=== DBTools Connection - Update by id:", self.connection_id)

        connection = self.dbtools_client.get_database_tools_connection(self.connection_id)
        display_name = connection.data.display_name

        connection_details_for_update = oci.database_tools.models.UpdateDatabaseToolsConnectionOracleDatabaseDetails(
            display_name=display_name + "_updated")

        response = self.dbtools_async_client.update_database_tools_connection_and_wait_for_state(self.connection_id,
                                                                                                 connection_details_for_update,
                                                                                                 wait_for_states=self.terminal_states)
        status = response.data.status
        assert status == "SUCCEEDED", f"update connection should return status SUCCEEDED but was {status}"

        # After update, get the connection again and confirm the change
        connection = self.dbtools_client.get_database_tools_connection(self.connection_id)
        assert connection.data, "updated connection data should exist"
        assert connection.data.display_name != display_name, "unexpected connection display name after update"
        assert connection.data.lifecycle_state == "ACTIVE", f"lifecycle_state should be ACTIVE after update but was {connection.data.lifecycle_state}"

        print(f"Updated connection. Name: {connection.data.display_name}, ocid: {self.connection_id}.")

    def validate_connection(self):
        """
        Given an existing Database Tools connection, this method shows how to validate a connection by id.
        For a connection to be able to route traffic to a database, it must be valid. (code == OK)
        """
        print("=== DBTools Connection - Validate by id:", self.connection_id)

        validate_detail = oci.database_tools.models.ValidateDatabaseToolsConnectionOracleDatabaseDetails()
        response = self.dbtools_client.validate_database_tools_connection(self.connection_id, validate_detail)
        assert response, "validate_database_tools_connection should return a response"
        assert response.data, "response should contain data"

        print("Validation result:", response.data)
        assert response.data.code == "OK", f"validation code should be OK but was {response.data.code}"

    def do_connection_cleanup(self):
        """
        Delete the Database Tools connection created by the example.
        """
        if self.connection_id is None:
            print("do_connection_cleanup skipped")
            return

        print("=== DBTools Connection - Delete by id:", self.connection_id)
        response = self.dbtools_async_client.delete_database_tools_connection_and_wait_for_state(self.connection_id,
                                                                                                 wait_for_states=self.terminal_states)
        assert response, "delete_database_tools_connection_and_wait_for_state should return a response"
        assert response.data, "response should contain data"

        status = response.data.status
        assert status == "SUCCEEDED", f"delete connection should return status SUCCEEDED but was {status}"

        print(f"Deleted connection. Status: {status}, ocid: {self.connection_id}.")

    def do_secrets_cleanup(self, days=2):
        """
        Schedule deletion of the secrets created by the example.
        """
        secret_deletion_time = datetime.now() + timedelta(days=days)
        if self.password_secret_id is not None:
            print("=== DBTools Example - Schedule Secret Deletion:", self.password_secret_id)
            delete_secret(clients=self.clients, secret_id=self.password_secret_id, deletion_time=secret_deletion_time)
        else:
            print("do_secrets_cleanup skipped (password)")

        if self.wallet_secret_id is not None:
            print("=== DBTools Example - Schedule Secret Deletion:", self.wallet_secret_id)
            delete_secret(clients=self.clients, secret_id=self.wallet_secret_id, deletion_time=secret_deletion_time)
        else:
            print("do_secrets_cleanup skipped (wallet)")

    def do_database_cleanup(self):
        # Beware, this actually DELETES the specified DB
        if self.autonomous_database_id is not None:
            print("=== DBTools Example - Terminate Database:", self.autonomous_database_id)
            self.db_client.delete_autonomous_database(self.autonomous_database_id)
            print("Database terminated.")
        else:
            print("do_database_cleanup skipped")


#
# Run DBToolsExample and print results
#
if __name__ == "__main__":
    # Output Colors
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    example = None

    try:
        example = DBToolsExample(compartment_id, vault_id, db_password)

        example.create_db()
        example.save_secrets_to_vault()
        example.create_connection()
        example.get_connection()
        example.update_connection()
        example.validate_connection()

        print(f"{OKGREEN}Python SDK test completed OK{ENDC}")

    except Exception as e:
        print(f"{FAIL}Exception during tests:{ENDC} {e}")

    finally:
        if do_clean_up_at_end and example is not None:
            print("Starting resource clean-up.")
            example.do_connection_cleanup()
            example.do_secrets_cleanup()
            example.do_database_cleanup()
            print("Clean-up completed.")
        else:
            print("Skipping resource clean-up.")
