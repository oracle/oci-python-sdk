# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# -----------------------------------------------------------------------------
# Example Use Case: Existing ADB-S with Private Endpoint
# -----------------------------------------------------------------------------
# This example creates a Database Tools connection to an Autonomous Database
# (ADB-S) accessible by private endpoint (PE). Note, since this connection will
# be for an ADB-S PE, a Database Tools PE is required to make a reverse connection.
# This example serves as an academic exercise of the SDK. It is a best practice
# to use separate subnets for the database and the Database Tools PE.
#
# Prerequisites:
#
#  - An existing ADB-S with PE and network security group (i.e. ingress on 1522)
#  - Available capacity (limits apply) to create a new private endpoint
#  - An existing vault for storage of secrets, with at least one master key
#  - A previously configured .oci/config file with a [DEFAULT] section
#  - Set the following variables in the code below:
#      + compartment_id          : The ocid for the target compartment
#      + vault_id                : The ocid for a vault (to store secrets)
#      + autonomous_database_id  : The ocid for an Autonomous Database
#      + subnet_id               : The ocid for a subnet where the ADB endpoint exists
#      + db_username             : The database user to connect with
#      + db_password             : The database password to connect with
#
# High-level Steps:
#
#  1- Create a Database Tools private endpoint
#  2- Create required secrets
#  3- Create a connection using the Database Tools private endpoint
#  4- Validate the connection
# -----------------------------------------------------------------------------

import oci
from oci.config import from_file, validate_config
from utils.dbtools import get_dbtools_clients, get_database_clients, get_secrets_client, get_kms_vault_client
from utils.dbtools import get_vaults_clients, delete_secret, get_wallet_and_create_secrets

import pkg_resources
from datetime import datetime, timedelta

# Set do_clean_up_at_end = False to keep the secrets, connection, and PE created
do_clean_up_at_end = True

# Specify compartment ocid to use. (can also use tenancy ocid if applicable)
compartment_id = "ocid1.tenancy......changeme"

# Specify vault ocid to use. (For this example, vault must be in compartment_id and contain a master key)
vault_id = "ocid1.vault.....changeme"

# Specify Autonomous Database ocid to use
autonomous_database_id = "ocid1.autonomousdatabase.....changeme"

# Specifiy the VCN subnet ocid where the ADB-S PE was created
subnet_id = "ocid1.subnet.....changeme"

# Specify the database username and password
db_username = "changeme_user"
db_password = "example-password"

print("Using oci version:", pkg_resources.get_distribution("oci").version)


class DBToolsExample:
    """
    A Database Tools example that demonstrates usage of the OCI Python SDK.
    """
    def __init__(self, compartment, vault, db, subnet, username, password):

        # Load an OCI config with the DEFAULT profile
        self.oci_config = from_file(file_location="~/.oci/config", profile_name="DEFAULT")

        self.compartment_id = compartment
        self.vault_id = vault
        self.autonomous_database_id = db
        self.subnet_id = subnet
        self.db_username = username
        self.db_password = password

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

        self.wallet_secret_id = None        # populated at runtime
        self.password_secret_id = None      # populated at runtime
        self.private_endpoint_id = None     # populated at runtime
        self.connection_id = None           # populated at runtime
        self.connection_string = None       # populated at runtime

        # When waiting for asynchronous calls, which status is considered "done"
        self.terminal_states = ["FAILED", "SUCCEEDED", "CANCELED", "AVAILABLE"]

    def get_endpoint_service(self):
        """
        Get the ocid of the Database Tools endpoints service (used to create private endpoints)
        """
        response = self.dbtools_client.list_database_tools_endpoint_services(self.compartment_id)

        assert response, "list_database_tools_endpoint_services should return a response"
        assert response.data, "endpoint_services should return data"
        assert response.data.items, "endpoint_services should contain a list of endpoints"

        # Use the first endpoint_service
        endpoint_service = response.data.items[0]
        assert endpoint_service.lifecycle_state == "ACTIVE", f"endpoint_service should be ACTIVE but was {endpoint_service.lifecycle_state}"

        return endpoint_service.id

    def create_private_endpoint(self):
        """
        Create a Database Tools private endpoint.
        """
        print("=== DBTools Example - Create Private Endpoint")

        endpoint_service_id = self.get_endpoint_service()
        assert endpoint_service_id, "endpoint_service_id is required"

        display_name = "pe_pysdk_" + datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        description = "Test private endpoint with Python SDK"
        pe_details_for_create = oci.database_tools.models.CreateDatabaseToolsPrivateEndpointDetails(
            compartment_id=self.compartment_id,
            endpoint_service_id=endpoint_service_id,
            subnet_id=self.subnet_id,
            display_name=display_name,
            description=description)

        response = self.dbtools_async_client.create_database_tools_private_endpoint_and_wait_for_state(
            pe_details_for_create, wait_for_states=self.terminal_states)

        assert response, "create_database_tools_private_endpoint_and_wait_for_state should return a response"
        assert response.data, "create_database_tools_private_endpoint_and_wait_for_state should return data"

        status = response.data.status
        self.private_endpoint_id = response.data.resources[0].identifier
        assert status == "SUCCEEDED", f"create private endpoint should return status SUCCEEDED but was {status}"

        print(f"Private endpoint created. Name: {display_name}, ocid: {self.private_endpoint_id}.")

    def get_private_endpoint(self):
        """
        Given an existing Database Tools private endpoint, this method shows how to get a PE by id.
        """
        print("=== DBTools Private Endpoint - Get by id:", self.private_endpoint_id)

        response = self.dbtools_client.get_database_tools_private_endpoint(self.private_endpoint_id)
        assert response, "get_database_tools_private_endpoint should return a response"
        assert response.data, "get_database_tools_private_endpoint should return data"
        assert response.data.lifecycle_state == "ACTIVE", f"lifecycle_state should be ACTIVE but was {response.data.lifecycle_state}"

        print("Read created private endpoint:", response.data)

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
        Given the configuration details provided above, the secrets stored in the vault,
        and the PE, create a Database Tools connection to the database.
        """
        print("=== DBTools Example - Create Connection Using:", self.connection_string)

        # Setup SSO key store using wallet_secret_id (required for mTLS)
        key_store = oci.database_tools.models.DatabaseToolsKeyStoreDetails(
            key_store_type=oci.database_tools.models.DatabaseToolsKeyStoreDetails.KEY_STORE_TYPE_SSO,
            key_store_content=oci.database_tools.models.DatabaseToolsKeyStoreContentSecretIdDetails(
                value_type=oci.database_tools.models.DatabaseToolsKeyStoreContentSecretIdDetails.VALUE_TYPE_SECRETID,
                secret_id=self.wallet_secret_id))

        user_name = self.db_username
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
            private_endpoint_id=self.private_endpoint_id,
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
        Given an existing Database Tools connection, this method shows how to get a connection by id.
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
        assert response.data.status == "SUCCEEDED", f"delete connection should return status SUCCEEDED but was {response.data.status}"

        print(f"Deleted connection. ocid: {self.connection_id}.")

    def do_private_endpoint_cleanup(self):
        """
        Delete the Database Tools private endpoint created by the example.
        """
        if self.private_endpoint_id is None:
            print("do_private_endpoint_cleanup skipped")
            return

        print("=== DBTools Private Endpoint - Delete by id:", self.private_endpoint_id)
        response = self.dbtools_async_client.delete_database_tools_private_endpoint_and_wait_for_state(self.private_endpoint_id,
                                                                                                       wait_for_states=self.terminal_states)
        assert response, "delete_database_tools_private_endpoint_and_wait_for_state should return a response"
        assert response.data, "response should contain data"
        assert response.data.status == "SUCCEEDED", f"delete private endpoint should return status SUCCEEDED but was {response.data.status}"

        print(f"Deleted private endpoint. ocid: {self.private_endpoint_id}.")

    def do_secrets_cleanup(self, days=2):
        """
        Schedule deletion of the secrets created by the example.
        """
        secret_deletion_time = datetime.now() + timedelta(days=days)
        if self.password_secret_id:
            print("=== DBTools Example - Schedule Secret Deletion:", self.password_secret_id)
            delete_secret(clients=self.clients, secret_id=self.password_secret_id, deletion_time=secret_deletion_time)
        else:
            print("do_secrets_cleanup skipped (password)")

        if self.wallet_secret_id:
            print("=== DBTools Example - Schedule Secret Deletion:", self.wallet_secret_id)
            delete_secret(clients=self.clients, secret_id=self.wallet_secret_id, deletion_time=secret_deletion_time)
        else:
            print("do_secrets_cleanup skipped (wallet)")


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
        example = DBToolsExample(compartment_id, vault_id, autonomous_database_id, subnet_id, db_username, db_password)

        example.create_private_endpoint()
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
            example.do_private_endpoint_cleanup()
            print("Clean-up completed.")
        else:
            print("Skipping resource clean-up.")
