# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import base64
import io
from zipfile import ZipFile


def get_dbtools_clients(oci_config):
    client = oci.database_tools.DatabaseToolsClient(config=oci_config)
    # Composite client waits for async operations to complete.
    composite_client = oci.database_tools.DatabaseToolsClientCompositeOperations(client)
    return client, composite_client


def get_database_clients(oci_config):
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


def get_vaults_clients(oci_config):
    client = oci.vault.VaultsClient(config=oci_config)
    # Composite client waits for async operations to complete.
    composite_client = oci.vault.VaultsClientCompositeOperations(client)
    return client, composite_client


def extract_zip(input_zip):
    """
    Return a dict of Key=filename with Value=content from a zipped file
    """
    input_zip = ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}


def extract_vault_first_master_key(oci_config, compartment_id, clients, vault_id, vault_key_id):
    """
    Extract the first Master key from the Vault
    """
    if vault_key_id is None:
        assert compartment_id, "compartment_id must not be null"
        assert vault_id, "vault_id must not be null"
        vault_response = clients["kms_vault_client"].get_vault(vault_id)
        assert vault_response, "get_vault should return a response"
        assert vault_response.data, "Vault Response should contain data"

        print(f"Vault {vault_id} management endpoint is {vault_response.data.management_endpoint}")
        kms_management_client = get_kms_management_client(oci_config,
                                                          service_endpoint=vault_response.data.management_endpoint)

        # Vault must be in same compartment...
        keys_response = kms_management_client.list_keys(compartment_id)
        assert keys_response, "list_keys should return a response"
        assert keys_response.data, "KMS Response should contain data"
        vault_key_id = next((k.id for k in keys_response.data), None)
        print(f"Vault {vault_id} key id is {vault_key_id}")

    return vault_key_id


def create_secret(oci_config, compartment_id: str, clients, vault_id: str, name: str, base64_secret_content: str, vault_key_id: str = None):
    """
    Create a secret using the specified name. The content is in base64Secret.
    If a secret with that name already exists, we simply return its OCID.
    """
    assert compartment_id, "compartment_id must not be null"
    assert vault_id, "vault_id must not be null"

    vault_key_id = extract_vault_first_master_key(oci_config, compartment_id, clients, vault_id, vault_key_id)  # Make sure that we have a master key

    try:
        print("Trying to read the secret by name before creating it...")
        bundle_response = clients["secrets_client"].get_secret_bundle_by_name(secret_name=name, vault_id=vault_id, stage="CURRENT")
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
            content=base64_secret_content
        )
    )

    create_secret_response = clients["vaults_async_client"].create_secret_and_wait_for_state(
        secret_details, wait_for_states=["FAILED", "ACTIVE", "CANCELED"])
    assert create_secret_response, "create_secret_and_wait_for_state should return a response"
    assert create_secret_response.data, "Secret Response should contain data"

    status = create_secret_response.data.lifecycle_state
    secret_id = create_secret_response.data.id
    assert status == "ACTIVE", "Creating Secret should succeed"
    print(f"Created Secret. Status: {status}, name: {name}, secret id: {secret_id}.")
    return secret_id, vault_key_id


def delete_secret(clients, secret_id: str, deletion_time):
    print(f"Deleting secret id {secret_id}")
    assert secret_id, "secret_id must not be null"
    secret_deletion_details = oci.vault.models.ScheduleSecretDeletionDetails(
        time_of_deletion=deletion_time
    )

    # Mark the secret for deletion
    delete_secret_response = clients["vaults_client"].schedule_secret_deletion(secret_id, secret_deletion_details)
    assert delete_secret_response, "schedule_secret_deletion should return a response"


def get_wallet_and_create_secrets(oci_config, compartment_id, clients, autonomous_database_id, vault_id, db_wallet_secret_name, db_password_secret_name, db_password):
    """
    Extract the wallet from the Autonomous Database
    We will store the wallet as a Secret in the vault
    We will also store the database password as a Secret in the vault
    """

    # We will extract wallet and prepare to store the wallet as a secret under name X. If name X already exists,
    # we will simply use it.
    print("Extracting Wallet from DB and storing in Vault")

    assert compartment_id, "compartment_id must not be null"
    assert autonomous_database_id, "autonomous_database_id must not be null"
    assert db_wallet_secret_name, "db_wallet_secret_name must not be null"
    assert db_password_secret_name, "db_password_secret_name must not be null"
    assert db_password, "db_password must not be null"

    # 1. Get DB
    autonomous_database_response = clients["db_client"].get_autonomous_database(autonomous_database_id)
    assert autonomous_database_response, "get_autonomous_database should return a response"
    assert autonomous_database_response.data, "Autonomous db Response should contain data"

    # 2. Extract Wallet from DB
    # Create a wallet details object
    db_wallet = oci.database.models.GenerateAutonomousDatabaseWalletDetails(
        password="Change-Example-Passw0rd!"
    )

    print("Extracting Wallet...")
    # Generate the wallet and store the response object
    db_wallet_response = clients["db_client"].generate_autonomous_database_wallet(
        autonomous_database_id=autonomous_database_id,
        generate_autonomous_database_wallet_details=db_wallet,
    )

    assert db_wallet_response, "generate_autonomous_database_wallet should return a response"
    assert db_wallet_response.data, "generate_autonomous_database_wallet should return data"
    assert db_wallet_response.data.content, "no wallet content data returned"

    # Unzip the Wallet in memory to extract the SSO
    filename_to_extract = "cwallet.sso"
    mem_file = io.BytesIO(db_wallet_response.data.content)
    zip_data = extract_zip(mem_file)
    sso_data = zip_data.get(filename_to_extract, None)
    assert sso_data, f"{filename_to_extract} not found in wallet"
    base64_sso_str = base64.b64encode(sso_data).decode()

    # 3. Store Wallet in vault and get that secret (Might already be there)
    wallet_secret_id, vault_key_id = create_secret(oci_config,
                                                   compartment_id=compartment_id,
                                                   clients=clients,
                                                   vault_id=vault_id,
                                                   name=db_wallet_secret_name,
                                                   base64_secret_content=base64_sso_str)

    # 4. Store the DB password in the vault as a secret under name X. If name X already exists, we will simply use it.
    base64_db_password_str = base64.b64encode(db_password.encode()).decode()
    password_secret_id, vault_key_id = create_secret(oci_config,
                                                     compartment_id=compartment_id,
                                                     clients=clients,
                                                     vault_id=vault_id,
                                                     vault_key_id=vault_key_id,
                                                     name=db_password_secret_name,
                                                     base64_secret_content=base64_db_password_str)

    return wallet_secret_id, password_secret_id
