# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrateVaultKeyDetails(object):
    """
    Details for replacing existing Oracle-managed keys with customer-managed `Vault service`__ keys and vice-versa is not supported.

    __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MigrateVaultKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this MigrateVaultKeyDetails.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this MigrateVaultKeyDetails.
        :type kms_key_version_id: str

        """
        self.swagger_types = {
            'kms_key_id': 'str',
            'kms_key_version_id': 'str'
        }

        self.attribute_map = {
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId'
        }

        self._kms_key_id = None
        self._kms_key_version_id = None

    @property
    def kms_key_id(self):
        """
        **[Required]** Gets the kms_key_id of this MigrateVaultKeyDetails.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :return: The kms_key_id of this MigrateVaultKeyDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this MigrateVaultKeyDetails.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :param kms_key_id: The kms_key_id of this MigrateVaultKeyDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def kms_key_version_id(self):
        """
        Gets the kms_key_version_id of this MigrateVaultKeyDetails.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :return: The kms_key_version_id of this MigrateVaultKeyDetails.
        :rtype: str
        """
        return self._kms_key_version_id

    @kms_key_version_id.setter
    def kms_key_version_id(self, kms_key_version_id):
        """
        Sets the kms_key_version_id of this MigrateVaultKeyDetails.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :param kms_key_version_id: The kms_key_version_id of this MigrateVaultKeyDetails.
        :type: str
        """
        self._kms_key_version_id = kms_key_version_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
