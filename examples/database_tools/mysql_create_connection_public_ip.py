# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# -----------------------------------------------------------------------------
# Example Use Case: Existing MySQL Database with Public IP (customer-managed)
# -----------------------------------------------------------------------------
# This example creates a Database Tools connection to a MySQL database
# accessible by public ip. Note, since this connection will be against a
# public ip address, a Database Tools private endpoint is not required.
# Exposing a database directly to the Internet is NOT a recommended practice
# for security reasons. This example serves as an academic exercise of the SDK.
#
# Prerequisites:
#
#  - An existing MySQL database on a compute node, for example
#  - Firewall or security list entries allowing TCP traffic to MySQL
#  - An existing Vault for storage of secrets, with at least one master key.
#  - A previously configured .oci/config file with a [DEFAULT] section
#  - Set the following variables in the code below:
#      + compartment_id    : The compartment to use with the example
#      + vault_id          : The ocid for a vault (to store secrets)
#      + db_username       : The MySQL database user to connect with
#      + db_password       : The MySQL database password to connect with
#      + connection_string : The MySQL connection string
#
# High-level Steps:
#
#  1- Create required secret
#  2- Create a connection
#  3- Validate the connection
# -----------------------------------------------------------------------------

import oci
from oci.config import from_file, validate_config
from utils.dbtools import get_dbtools_clients, get_secrets_client, get_kms_vault_client, get_vaults_clients
from utils.dbtools import create_secret, delete_secret

import pkg_resources
import base64
from datetime import datetime, timedelta

# Set do_clean_up_at_end = False to keep the secret and connection created
do_clean_up_at_end = True

# Specify compartment ocid to use. (can also use tenancy ocid if applicable)
compartment_id = "ocid1.tenancy......changeme"

# Specify vault ocid to use. (For this example, vault must be in compartment_id and contain a master key)
vault_id = "ocid1.vault.....changeme"

# Specify the MySQL database connection string
connection_string = "mysql://host.changeme:port/"

# Specify the database username and password
db_username = "example-username"
db_password = "example-password"

print("Using oci version:", pkg_resources.get_distribution("oci").version)


class DBToolsExample:
    """
    A Database Tools example that demonstrates usage of the OCI Python SDK.
    """
    def __init__(self, compartment, vault, connection_string, username, password):

        # Load an OCI config with the DEFAULT profile
        self.oci_config = from_file(file_location="~/.oci/config", profile_name="DEFAULT")

        self.compartment_id = compartment
        self.vault_id = vault
        self.connection_string = connection_string
        self.db_username = username
        self.db_password = password

        validate_config(self.oci_config)

        # Prepare SDK clients used in this example
        self.dbtools_client, self.dbtools_async_client = get_dbtools_clients(self.oci_config)
        self.vaults_client, self.vaults_async_client = get_vaults_clients(self.oci_config)
        self.kms_vault_client = get_kms_vault_client(self.oci_config)
        self.secrets_client = get_secrets_client(self.oci_config)

        # Dict that contains all the clients (used by utils.dbtools helpers)
        self.clients = {"vaults_client": self.vaults_client, "vaults_async_client": self.vaults_async_client,
                        "kms_vault_client": self.kms_vault_client,
                        "secrets_client": self.secrets_client,
                        "dbtools_client": self.dbtools_client, "dbtools_async_client": self.dbtools_async_client}

        self.password_secret_id = None  # populated at runtime
        self.connection_id = None       # populated at runtime

        # When waiting for asynchronous calls, which status is considered "done"
        self.terminal_states = ["FAILED", "SUCCEEDED", "CANCELED"]

    def save_dbpassword_to_vault(self):
        """
        Database Tools connections don't store secrets directly. Instead, they hold a pointer to
        secrets stored securely in a vault.
        """
        print("=== DBTools Example - Save DB Password to Vault")

        db_password_secret_name = "dbtools-temp-secretp-" + datetime.utcnow().strftime("%m%d%H%M")
        base64_secret_content = base64.b64encode(self.db_password.encode()).decode()

        self.password_secret_id = create_secret(oci_config=self.oci_config,
                                                compartment_id=self.compartment_id,
                                                vault_id=self.vault_id,
                                                name=db_password_secret_name,
                                                base64_secret_content=base64_secret_content,
                                                clients=self.clients)[0]

        print(f"Created secret. Name: {db_password_secret_name}, ocid: {self.password_secret_id}")

    def create_connection(self):
        """
        Given the configuration details provided above and the secrets stored in the vault,
        create a Database Tools connection to the MySQL database.
        """
        print("=== DBTools Example - Create Connection Using:", self.connection_string)

        user_password = oci.database_tools.models.DatabaseToolsUserPasswordSecretIdDetails(
            secret_id=self.password_secret_id)

        display_name = "conn_pysdk_" + datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

        conn_details_for_create = oci.database_tools.models.CreateDatabaseToolsConnectionMySqlDetails(
            compartment_id=self.compartment_id,
            connection_string=self.connection_string,
            user_name=self.db_username,
            user_password=user_password,
            display_name=display_name)

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

        connection_details_for_update = oci.database_tools.models.UpdateDatabaseToolsConnectionMySqlDetails(
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

        validate_detail = oci.database_tools.models.ValidateDatabaseToolsConnectionMySqlDetails()
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
        example = DBToolsExample(compartment_id, vault_id, connection_string, db_username, db_password)

        example.save_dbpassword_to_vault()
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
            print("Clean-up completed.")
        else:
            print("Skipping resource clean-up.")
