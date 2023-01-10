# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import sys
from datetime import datetime
from datetime import timedelta

# ==========================================================
# This file provides examples of basic key management service usage
# * - Get a vault
# * - Create a vault
# Management endpoint operations
# * - Get a key
# * - Create a key
# * - Enable a key
# * - Disable a key
# Secrets Management operations
# * - Create a secret
# * - Create a new secret version
# * - Update a secret
# * - Move a secret to a new compartment
# * - Delete a secret
# Documentation : https://docs.cloud.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingsecrets.htm

# Usage : python secret_examples.py compartment_id OCI_PROFILE
# OCI_PROFILE is the name of profile that you want to use from OCI config file.


def create_vault(compartment_id, vault_name, sac_composite):
    print(" Creating vault {} in {} compartment.".format(vault_name,
                                                         compartment_id))

    # Create vault_details object that needs to be passed when creating vault.
    vault_details = oci.key_management.models.CreateVaultDetails(
        compartment_id=compartment_id,
        vault_type="DEFAULT",
        display_name=vault_name)

    print("Vault details {}.".format(vault_details.vault_type))

    # Since vault creation is asynchronous; we need to wait for the stream to become active.
    response = sac_composite.create_vault_and_wait_for_state(
        vault_details,
        wait_for_states=[oci.key_management.models.Vault.LIFECYCLE_STATE_ACTIVE])
    return response


def get_vault(client, vault_id):
    return client.get_vault(vault_id)


def create_key(key_mgmt_composite, key_name, compartment_id):
    print(" Creating key {} in compartment {}.".format(key_name, compartment_id))

    # Create key_details object that needs to be passed when creating key.
    key_shape = oci.key_management.models.KeyShape(algorithm="AES", length=32)
    key_details = oci.key_management.models.CreateKeyDetails(
        compartment_id=compartment_id,
        display_name=key_name,
        key_shape=key_shape)

    # Since key creation is asynchronous; we need to wait for the key to become enabled.
    response = key_mgmt_composite.create_key_and_wait_for_state(key_details,
                                                                wait_for_states=[
                                                                    oci.key_management.models.Key.LIFECYCLE_STATE_ENABLED])
    return response


def get_key(client, key_id):
    return client.get_key(key_id)


def enable_key(key_mgmt_composite, key_id):
    print(" Enabling key {}.".format(key_id))

    # Since enabling key is asynchronous; we need to wait for the key to become enabled.
    response = key_mgmt_composite.enable_key_and_wait_for_state(key_id,
                                                                wait_for_states=[
                                                                    oci.key_management.models.Key.LIFECYCLE_STATE_ENABLED])
    return response


def disable_key(key_mgmt_composite, key_id):
    print(" Disabling key {}.".format(key_id))

    # Since disabling key is asynchronous; we need to wait for the key to become disabled.
    response = key_mgmt_composite.disable_key_and_wait_for_state(key_id,
                                                                 wait_for_states=[
                                                                     oci.key_management.models.Key.LIFECYCLE_STATE_DISABLED])
    return response


def create_secret(vaults_client_composite, compartment_id, secret_content, secret_name, valult_id, key_id):
    print("Creating a secret {}.".format(secret_name))

    # Create secret_content_details that needs to be passed when creating secret.
    secret_description = "This is just a test"
    secret_content_details = oci.vault.models.Base64SecretContentDetails(
        content_type=oci.vault.models.SecretContentDetails.CONTENT_TYPE_BASE64,
        name=secret_content,
        stage="CURRENT",
        content=secret_content)
    secrets_details = oci.vault.models.CreateSecretDetails(compartment_id=compartment_id,
                                                           description=secret_description,
                                                           secret_content=secret_content_details,
                                                           secret_name=secret_name,
                                                           vault_id=vault_id,
                                                           key_id=key_id)

    # Create secret and wait for the secret to become active
    response = vaults_client_composite.create_secret_and_wait_for_state(create_secret_details=secrets_details,
                                                                        wait_for_states=[
                                                                            oci.vault.models.Secret.LIFECYCLE_STATE_ACTIVE])
    return response


def create_newsecret_version(vaults_client_composite, secret_content, secret_id):
    print("Creating a new secret version {}.".format(secret_id))

    # Create secret_content_details that needs to be passed when updating secret content.
    secret_content_details = oci.vault.models.Base64SecretContentDetails(
        content_type=oci.vault.models.SecretContentDetails.CONTENT_TYPE_BASE64,
        stage="CURRENT",
        content=secret_content)

    secrets_details = oci.vault.models.UpdateSecretDetails(secret_content=secret_content_details)

    # Create new secret version and wait for the new version to become active.
    response = vaults_client_composite.update_secret_and_wait_for_state(secret_id,
                                                                        secrets_details,
                                                                        wait_for_states=[
                                                                            oci.vault.models.Secret.LIFECYCLE_STATE_ACTIVE])
    return response


def get_secret(vaults_client, secret_id):
    return vaults_client.get_secret(secret_id)


def delete_secret(vaults_client, secret_id, deletion_time):
    print("Deleting a secret")

    # Create Secret deletion details object.
    secret_deletion_details = oci.vault.models.ScheduleSecretDeletionDetails(time_of_deletion=deletion_time)
    # secret_deletion_details = oci.vault.models.ScheduleSecretDeletionDetails()

    # Delete the secret or mark the secret for deletion
    response = vaults_client.schedule_secret_deletion(secret_id, secret_deletion_details)
    print("Secret deletion response is: {}.".format(response.data))


def delete_secret_version(vaults_client, secret_id, deletion_time, secret_version_number):
    print("Deleting a specific version of a secret")

    # Create Secret version deletion object
    secret_version_deletion_details = oci.vault.models.ScheduleSecretVersionDeletionDetails(time_of_deletion=deletion_time)

    # Delete the secret version or mark the version for deletion.
    response = vaults_client.schedule_secret_version_deletion(secret_id,
                                                              secret_version_number=secret_version_number,
                                                              schedule_secret_version_deletion_details=secret_version_deletion_details)
    print("Secret deletion response is: {}.".format(response.data))


def move_secret(vaults_client, secret_id, target_compartment_id):
    print("Moving secret to a target compartment")

    # Create an object of Change Secret Compartment Details
    target_compartment_details = oci.vault.models.ChangeSecretCompartmentDetails(compartment_id=target_compartment_id)

    # Move the secret to target compartment and then wait for the state to become active.
    response = vaults_client.change_secret_compartment(secret_id, change_secret_compartment_details=target_compartment_details)
    target_state = oci.vault.models.Secret.LIFECYCLE_STATE_ACTIVE.lower()
    try:
        waiter_result = oci.wait_until(
            vaults_client,
            vaults_client.get_secret(secret_id),
            evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() == target_state,
            waiter_kwargs={}
        )
        result_to_return = waiter_result
        print("Change compartment response is {}.".format(result_to_return.data))
        return result_to_return
    except Exception as e:
        raise oci.exceptions.CompositeOperationError(partial_results=[response], cause=e)


if len(sys.argv) != 3:
    raise RuntimeError(
        'This example expects an ocid for the secret to read.')

compartment_id = sys.argv[1]
oci_profile = sys.argv[2]

config = config = oci.config.from_file(
    "~/.oci/config",
    oci_profile)

secret_content = "TestContent"
secret_name = "TestSecret"
VAULT_NAME = "KmsVault"
KEY_NAME = "KmsKey"

# Vault client to create vault
kms_vault_client = oci.key_management.KmsVaultClient(config)
kms_vault_client_composite = oci.key_management.KmsVaultClientCompositeOperations(
    kms_vault_client)

# This will create a vault in the given compartment
vault = create_vault(compartment_id, VAULT_NAME, kms_vault_client_composite).data
# vault = get_vault(kms_vault_client, vault_id).data
vault_id = vault.id
print(" Created vault {} with id : {}".format(VAULT_NAME, vault_id))

# Vault Management client to create a key
vault_management_client = oci.key_management.KmsManagementClient(config,
                                                                 service_endpoint=vault.management_endpoint)
vault_management_client_composite = oci.key_management.KmsManagementClientCompositeOperations(
    vault_management_client)

# Create key in given compartment
key = create_key(vault_management_client_composite, KEY_NAME, compartment_id).data
# key = get_key(vault_management_client,key_id).data
key_id = key.id
print(" Created key {} with id : {}".format(KEY_NAME, key.id))

# Vault client to manage secrets
vaults_client = oci.vault.VaultsClient(config)
vaults_management_client_composite = oci.vault.VaultsClientCompositeOperations(vaults_client)

secret = create_secret(vaults_management_client_composite, compartment_id, secret_content, secret_name, vault_id, key_id).data
secret_id = secret.id
print("Secret ID is {}.".format(secret_id))

secret_deletion_time = datetime.now() + timedelta(days=2)
delete_secret(vaults_client, secret_id, secret_deletion_time)
