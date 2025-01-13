# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Creates a Generic JDBC Database Tools connection.

# 1- Stores a secret consisting of the database password in the provided Vault
# 2- Creates a new connection in the provided compartment
#
# If variable do_clean_up_at_end is set to True, connection, secrets and DB are removed upon completion.

# Prerequisites are:
# - A compartment_id where the vcn, autonomous database, vault and connection will reside.
# - A Vault id created in KMS with at least one master key.
# - A previously configured .oci/config file with a [DEFAULT] section should already setup.

import oci
import base64
from oci.config import from_file, validate_config
from utils.dbtools import get_dbtools_clients, get_secrets_client, get_kms_vault_client, get_vaults_clients, delete_secret, create_secret
from utils.dbtools import Colors
from datetime import datetime, timedelta


# The compartment ID where 1) the connection will be stored 2) where the Vault is located
compartment_id = "ocid1.compartment.......changeme"

# Specify Vault id to use in the test. Must be in compartment_id and contain a master Key
vault_id = "ocid1.vault.oc1.......changeme"

# The name of the connection that will be created
connection_name = "test-generic-jdbc-connection-with-python-sdk"

# The name of the secret that will be created to store the password
secret_name = "generic_jdbc_password_secret-6"


class DBToolsExample:
    def __init__(self, compartment, vault, connection_name, secret_name):
        self.oci_config = from_file(file_location="~/.oci/config", profile_name="DEFAULT")
        validate_config(self.oci_config)

        self.compartment = compartment
        self.vault = vault
        self.connection_name = connection_name
        self.secret_name = secret_name
        self.secret_id = None
        self.secret_needs_cleanup = None
        self.connection_id = None

        self.clients = {
            "vaults_async_client": get_vaults_clients(self.oci_config)[1],
            "kms_vault_client": get_kms_vault_client(self.oci_config),
            "secrets_client": get_secrets_client(self.oci_config),
            "dbtools_async_client": get_dbtools_clients(self.oci_config)[1]
        }

    def store_secret_in_vault(self):
        create_secret_response = create_secret(
            oci_config=self.oci_config,
            compartment_id=self.compartment,
            clients=self.clients,
            vault_id=self.vault,
            name=self.secret_name,
            base64_secret_content=base64.b64encode("DataBase12##".encode("ascii")).decode("ascii")
        )
        self.secret_id = create_secret_response[0]
        self.secret_needs_cleanup = create_secret_response[2]

    def create_generic_jdbc_connection(self):
        connection_details = oci.database_tools.models.CreateDatabaseToolsConnectionGenericJdbcDetails(
            type="GENERIC_JDBC",
            runtime_support="UNSUPPORTED",
            compartment_id=compartment_id,
            url="jdbc:mysql://localhost:3306",
            user_name="test_user_name",
            user_password=oci.database_tools.models.DatabaseToolsUserPasswordSecretIdDetails(secret_id=self.secret_id),
            display_name=connection_name
        )

        response = self.clients["dbtools_async_client"].create_database_tools_connection_and_wait_for_state(
            create_database_tools_connection_details=connection_details,
            wait_for_states=["FAILED", "SUCCEEDED", "CANCELED"]
        )

        assert response, "create_database_tools_connection_and_wait_for_state should return a response"
        assert response.data, "response should contain data"
        assert response.data.resources, "response data should return resources"
        assert response.data.status == "SUCCEEDED", f"create connection should return status SUCCEEDED but was {response.data.status}"

        self.connection_id = response.data.resources[0].identifier

        print(f"Connection created with name {connection_name} and OCID {self.connection_id}")

    def secret_cleanup(self):
        if self.secret_id is None:
            print("Skipping secret cleanup because no secret was created or found")
            return

        secret_deletion_time = datetime.now() + timedelta(days=2)
        if self.secret_needs_cleanup:
            print("Scheduled secret deletion:", self.secret_id)
            delete_secret(clients=self.clients, secret_id=self.secret_id, deletion_time=secret_deletion_time)

    def connection_cleanup(self):
        if self.connection_id is None:
            print("Skipping connection cleanup because no connection was created")
            return

        response = self.clients["dbtools_async_client"].delete_database_tools_connection_and_wait_for_state(
            self.connection_id,
            wait_for_states=["FAILED", "SUCCEEDED", "CANCELED"]
        )

        assert response, "delete_database_tools_connection_and_wait_for_state should return a response"
        assert response.data, "response should contain data"
        assert response.data.status == "SUCCEEDED", f"delete connection should return status SUCCEEDED but was {response.data.status}"

        print(f"Deleted connection {self.connection_id}.")


#
# Run DBToolsExample and print results
#
if __name__ == "__main__":
    example = None

    try:
        example = DBToolsExample(compartment_id, vault_id, connection_name, secret_name)
        example.store_secret_in_vault()
        example.create_generic_jdbc_connection()
    except Exception as e:
        print(f"{Colors.FAIL}Exception during tests:{Colors.ENDC} {e}")
    finally:
        if example.secret_needs_cleanup:
            example.secret_cleanup()
        else:
            print("Secret cleanup was skipped because it already existed")
        example.connection_cleanup()
        print(f"{Colors.OKGREEN}Python SDK test completed OK{Colors.ENDC}")
