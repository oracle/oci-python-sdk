# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .create_key_details import CreateKeyDetails
from .create_vault_details import CreateVaultDetails
from .decrypt_data_details import DecryptDataDetails
from .decrypted_data import DecryptedData
from .encrypt_data_details import EncryptDataDetails
from .encrypted_data import EncryptedData
from .generate_key_details import GenerateKeyDetails
from .generated_key import GeneratedKey
from .key import Key
from .key_shape import KeyShape
from .key_summary import KeySummary
from .key_version import KeyVersion
from .key_version_summary import KeyVersionSummary
from .schedule_vault_deletion_details import ScheduleVaultDeletionDetails
from .update_key_details import UpdateKeyDetails
from .update_vault_details import UpdateVaultDetails
from .vault import Vault
from .vault_summary import VaultSummary

# Maps type names to classes for key_management services.
key_management_type_mapping = {
    "CreateKeyDetails": CreateKeyDetails,
    "CreateVaultDetails": CreateVaultDetails,
    "DecryptDataDetails": DecryptDataDetails,
    "DecryptedData": DecryptedData,
    "EncryptDataDetails": EncryptDataDetails,
    "EncryptedData": EncryptedData,
    "GenerateKeyDetails": GenerateKeyDetails,
    "GeneratedKey": GeneratedKey,
    "Key": Key,
    "KeyShape": KeyShape,
    "KeySummary": KeySummary,
    "KeyVersion": KeyVersion,
    "KeyVersionSummary": KeyVersionSummary,
    "ScheduleVaultDeletionDetails": ScheduleVaultDeletionDetails,
    "UpdateKeyDetails": UpdateKeyDetails,
    "UpdateVaultDetails": UpdateVaultDetails,
    "Vault": Vault,
    "VaultSummary": VaultSummary
}
