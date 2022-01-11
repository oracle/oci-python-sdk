# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import sys
from datetime import datetime
from datetime import timedelta

# ==========================================================
# This file provides examples of basic key management service usage
# * - Get a vault
# * - Create a vault
# * - Update vault details
# * - Schedule deletion for a vault
# * - Cancel deletion for a vault
# Management endpoint operations
# * - Get a key
# * - Create a key
# * - Enable a key
# * - Disable a key
# * - Update key details
# Crypto endpoint operations
# * - Generate Data Encryption Key
# * - Encrypt
# * - Decrypt
# Documentation : https://docs.cloud.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm

# Usage : python kms_examples.py <compartment id>

VAULT_NAME = "KmsVault"
VAULT_UPDATE_NAME = "UpdatedKmsVault"
KEY_NAME = "KmsVault"
KEY_UPDATE_NAME = "UpdatedKmsVault"
TEST_PLAIN_TEXT = "TestInput"


def create_vault(compartment_id, vault_name, sac_composite):
    print(
        " Creating vault {} in {} compartment.".format(vault_name,
                                                       compartment_id))

    # Create vault_details object that needs to be passed when creating vault.
    vault_details = oci.key_management.models.CreateVaultDetails(
        compartment_id=compartment_id,
        vault_type="VIRTUAL_PRIVATE",
        display_name=vault_name)

    # Since vault creation is asynchronous; we need to wait for the stream to become active.
    response = sac_composite.create_vault_and_wait_for_state(
        vault_details,
        wait_for_states=[oci.key_management.models.Vault.LIFECYCLE_STATE_ACTIVE])
    return response


def get_vault(client, vault_id):
    return client.get_vault(vault_id)


def update_vault(vault_id, vault_name, client):
    print(" Updating vault {} to name {}.".format(vault_id, vault_name))

    # Create update_vault_details object that needs to be passed when updating vault.
    update_vault_details = oci.key_management.models.UpdateVaultDetails(
        display_name=vault_name)
    return client.update_vault(vault_id, update_vault_details)


def change_vault_compartment(vault_id, v_client, target_compartment_id):
    print("Changing compartment for vault {}".format(vault_id))
    # Create change_vault_compartment_details object

    change_vault_compartment_details = oci.key_management.models.ChangeVaultCompartmentDetails(
        compartment_id=target_compartment_id)

    response = v_client.change_vault_compartment(
        change_vault_compartment_details
    )

    # Wait for vault to become ACTIVE again
    target_state = oci.key_management.models.Vault.LIFECYCLE_STATE_ACTIVE.lower()

    try:
        waiter_result = oci.wait_until(
            v_client,
            v_client.get_vault(vault_id),
            evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() == target_state,
            waiter_kwargs={}
        )
        result_to_return = waiter_result

        return result_to_return
    except Exception as e:
        raise oci.exceptions.CompositeOperationError(partial_results=[response], cause=e)


def schedule_deletion_vault(vault_id, vc_composite, deletion_time):
    print(" Scheduling Deletion for Vault {}".format(vault_id))
    # Create schedule_vault_deletion_details object that needs to be passed when scheduling vault deletion.
    schedule_vault_deletion_details = oci.key_management.models.ScheduleVaultDeletionDetails(
        time_of_deletion=deletion_time)

    # Since scheduling vault deletion is asynchronous; we need to wait for the vault to go to pending deletion state.
    response = vc_composite.schedule_vault_deletion_and_wait_for_state(
        schedule_vault_deletion_details,
        wait_for_states=[
            oci.key_management.models.Vault.LIFECYCLE_STATE_PENDING_DELETION])
    return response


def cancel_deletion_vault(vault_id, vc_composite, ):
    print(" Cancelling Deletion for Vault {}".format(vault_id))
    # Cancelling vault deletion is asynchronous; we need to wait for the vault to become active.
    response = vc_composite.cancel_vault_deletion_and_wait_for_state(
        vault_id,
        wait_for_states=[oci.key_management.models.Vault.LIFECYCLE_STATE_ACTIVE])
    return response


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


def update_key(key_id, key_name, client):
    print(" Updating key {} to name {}.".format(key_id, key_name))

    # Create update_key_details object that needs to be passed when updating key.
    update_key_details = oci.key_management.models.UpdateKeyDetails(
        display_name=key_name)
    return client.update_key(key_id, update_key_details)


def enable_key(key_mgmt_composite, key_id):
    print(" Enabling key {}.".format(key_id))

    # Since enabling key is asynchronous; we need to wait for the key to become enabled.
    response = key_mgmt_composite.enable_key_and_wait_for_state(key_id,
                                                                wait_for_states=[
                                                                    oci.key_management.models.Key.LIFECYCLE_STATE_ENABLED])
    return response


def schedule_deletion_key(key_mgmt_composite, deletion_time, key_id):
    print(" Scheduling Deletion for Key {}".format(key_id))
    # Create schedule_vault_deletion_details object that needs to be passed when scheduling vault deletion.
    schedule_key_deletion_details = oci.key_management.models.sc(
        time_of_deletion=deletion_time)

    # Since scheduling vault deletion is asynchronous; we need to wait for the vault to go to pending deletion state.
    response = key_mgmt_composite.schedule_key_deletion_and_wait_for_state(
        schedule_key_deletion_details,
        wait_for_states=[
            oci.key_management.models.Key.LIFECYCLE_STATE_PENDING_DELETION])
    return response


def change_key_compartment(v_management_client, target_compartment_id, key_id):
    print("Changing compartment for Key {}".format(key_id))
    # Create change_key_compartment_details object
    change_key_compartment_details = oci.key_management.models.ChangeKeyCompartmentDetails(
        compartment_id=target_compartment_id)

    response = v_management_client.change_key_compartment(
        change_key_compartment_details
    )

    # Wait for key to become ENABLED again
    target_state = oci.key_management.models.Key.LIFECYCLE_STATE_ENABLED.lower()
    try:
        waiter_result = oci.wait_until(
            v_management_client,
            v_management_client.get_key(key_id),
            evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() == target_state,
            waiter_kwargs={}
        )
        result_to_return = waiter_result

        return result_to_return
    except Exception as e:
        raise oci.exceptions.CompositeOperationError(partial_results=[response], cause=e)


def cancel_deletion_key(key_mgmt_composite, key_id):
    print(" Canceling key deletion {}.".format(key_id))

    # Since enabling key is asynchronous; we need to wait for the key to become enabled.
    response = key_mgmt_composite.cancel_key_deletion_and_wait_for_state(key_id,
                                                                         wait_for_states=[
                                                                             oci.key_management.models.Key.LIFECYCLE_STATE_ENABLED,
                                                                             oci.key_management.models.Key.LIFECYCLE_STATE_DISABLED])
    return response


def disable_key(key_mgmt_composite, key_id):
    print(" Disabling key {}.".format(key_id))

    # Since disabling key is asynchronous; we need to wait for the key to become disabled.
    response = key_mgmt_composite.disable_key_and_wait_for_state(key_id,
                                                                 wait_for_states=[
                                                                     oci.key_management.models.Key.LIFECYCLE_STATE_DISABLED])
    return response


def generate_dek(key_crypto_client, key_id):
    print(" Generating DEK {}.".format(key_id))

    # Create generate_key_details object that needs to be passed when generating dek.
    key_shape = oci.key_management.models.KeyShape(algorithm="AES", length=32)
    generate_dek_details = oci.key_management.models.GenerateKeyDetails(
        include_plaintext_key=False,
        key_id=key_id,
        key_shape=key_shape)
    response = key_crypto_client.generate_data_encryption_key(
        generate_dek_details)
    return response


def encrypt_data(key_crypto_client, key_id, clear_text):
    print(" Encrypting text with key {}.".format(key_id))

    encrypt_data_details = oci.key_management.models.EncryptDataDetails(
        key_id=key_id,
        plaintext=clear_text)
    response = key_crypto_client.encrypt(encrypt_data_details)
    print(" Encrypted text {}.".format(response.ciphertext))
    return response.ciphertext


def decrypt_data(key_crypto_client, key_id, encrypted_text):
    print(" Decrypting text with key {}.".format(key_id))

    decrypt_data_details = oci.key_management.models.DecryptDataDetails(
        key_id=key_id,
        ciphertext=encrypted_text)
    response = key_crypto_client.decrypt(decrypt_data_details)
    print(" Decrypted text {}.".format(response.plaintext))
    return response.plaintext


# Load the default configuration
config = oci.config.from_file()

# Create a VaultClientCompositeOperations for composite operations.
vault_client = oci.key_management.KmsVaultClient(config)
vault_client_composite = oci.key_management.KmsVaultClientCompositeOperations(
    vault_client)

if len(sys.argv) != 3:
    raise RuntimeError(
        'This example expects an ocid for the compartment in which vault should be created '
        ' and a destination compartment for the resource move examples.')

compartment = sys.argv[1]
target_compartment = sys.argv[2]

# This will create a vault in the given compartment
vault = create_vault(compartment, VAULT_NAME, vault_client_composite).data
v_id = vault.id
print(" Created vault {} with id : {}".format(vault.name, vault.id))

updated_vault = update_vault(v_id, VAULT_UPDATE_NAME, vault_client).data
print(" Updated vault {} with name : {}".format(vault.id, updated_vault.name))

change_vault_compartment(v_id, vault_client, target_compartment)
print(" Changed vault compartment to {}".format(vault.id))

# Create a vault management client using the endpoint in the vault object.
vault_management_client = oci.key_management.KmsManagementClient(config,
                                                                 service_endpoint=vault.management_endpoint)
vault_management_client_composite = oci.key_management.KmsManagementClientCompositeOperations(
    vault_management_client)

# Create a vault crypto client using the endpoint in the vault object.
vault_crypto_client = oci.key_management.KmsCryptoClient(config,
                                                         service_endpoint=vault.crypto_endpoint)
# Schedule vault deletion
print(" Scheduling vault deletion for vault {} with time {}".format(vault.id,
                                                                    datetime.now() + timedelta(
                                                                        days=15)))
schedule_deletion_vault(v_id, vault_client_composite,
                        datetime.now() + timedelta(days=15))

# Cancel vault deletion
print(" Cancelling scheduled deletion for vault {}".format(vault.id))
cancel_deletion_vault(v_id, vault_client_composite)

# Create key in given compartment
key = create_key(vault_management_client_composite, KEY_NAME, v_id).data
k_id = key.id
print(" Created key {} with id : {}".format(key.name, key.id))

updated_key = update_key(k_id, KEY_UPDATE_NAME, vault_management_client)
print(" Updated key {} with name : {}".format(key.id, updated_key.name))

print(" Disabling key {}.".format(k_id))
disable_key(vault_management_client_composite, k_id)

print(" Enabling key {}.".format(k_id))
enable_key(vault_management_client_composite, k_id)

print(" Changing key compartment to {}.".format(target_compartment))
change_key_compartment(vault_management_client, target_compartment, k_id)

print(" Scheduling key deletion {}.".format(k_id))
schedule_deletion_key(vault_management_client_composite, k_id,
                      datetime.now() + timedelta(days=15))

print(" Canceling key deletion {}.".format(k_id))
cancel_deletion_key(vault_management_client_composite, k_id)

# Generate Data Encryption Key
generate_dek(vault_crypto_client, k_id)

# Encrypt plain text
print(" Encrypting plain text {}.".format(TEST_PLAIN_TEXT))
en_text = encrypt_data(vault_crypto_client, k_id, TEST_PLAIN_TEXT)

# decrypt encrypted text
print(" Decrypting encrypted text {}.".format(en_text))
plain_text = decrypt_data(vault_crypto_client, k_id, en_text)
print(" Decrypted text {}.".format(plain_text))

# Cleanup - Schedule vault deletion
schedule_deletion_vault(v_id, vault_client_composite,
                        datetime.now() + timedelta(days=15))
