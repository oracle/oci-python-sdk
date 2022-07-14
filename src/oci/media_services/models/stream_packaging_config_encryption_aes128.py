# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .stream_packaging_config_encryption import StreamPackagingConfigEncryption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamPackagingConfigEncryptionAes128(StreamPackagingConfigEncryption):
    """
    AES128 encryption type (enabled by default).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StreamPackagingConfigEncryptionAes128 object with values from keyword arguments. The default value of the :py:attr:`~oci.media_services.models.StreamPackagingConfigEncryptionAes128.algorithm` attribute
        of this class is ``AES128`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param algorithm:
            The value to assign to the algorithm property of this StreamPackagingConfigEncryptionAes128.
            Allowed values for this property are: "NONE", "AES128"
        :type algorithm: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this StreamPackagingConfigEncryptionAes128.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'algorithm': 'str',
            'kms_key_id': 'str'
        }

        self.attribute_map = {
            'algorithm': 'algorithm',
            'kms_key_id': 'kmsKeyId'
        }

        self._algorithm = None
        self._kms_key_id = None
        self._algorithm = 'AES128'

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this StreamPackagingConfigEncryptionAes128.
        The identifier of the customer managed Vault KMS symmetric encryption key (null if Oracle managed).


        :return: The kms_key_id of this StreamPackagingConfigEncryptionAes128.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this StreamPackagingConfigEncryptionAes128.
        The identifier of the customer managed Vault KMS symmetric encryption key (null if Oracle managed).


        :param kms_key_id: The kms_key_id of this StreamPackagingConfigEncryptionAes128.
        :type: str
        """
        self._kms_key_id = kms_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
