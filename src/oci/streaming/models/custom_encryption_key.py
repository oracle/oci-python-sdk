# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomEncryptionKey(object):
    """
    Custom Encryption Key which will be used for encryption by all the streams in the pool.
    """

    #: A constant which can be used with the key_state property of a CustomEncryptionKey.
    #: This constant has a value of "ACTIVE"
    KEY_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the key_state property of a CustomEncryptionKey.
    #: This constant has a value of "CREATING"
    KEY_STATE_CREATING = "CREATING"

    #: A constant which can be used with the key_state property of a CustomEncryptionKey.
    #: This constant has a value of "DELETING"
    KEY_STATE_DELETING = "DELETING"

    #: A constant which can be used with the key_state property of a CustomEncryptionKey.
    #: This constant has a value of "NONE"
    KEY_STATE_NONE = "NONE"

    #: A constant which can be used with the key_state property of a CustomEncryptionKey.
    #: This constant has a value of "FAILED"
    KEY_STATE_FAILED = "FAILED"

    #: A constant which can be used with the key_state property of a CustomEncryptionKey.
    #: This constant has a value of "UPDATING"
    KEY_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new CustomEncryptionKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CustomEncryptionKey.
        :type kms_key_id: str

        :param key_state:
            The value to assign to the key_state property of this CustomEncryptionKey.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETING", "NONE", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type key_state: str

        """
        self.swagger_types = {
            'kms_key_id': 'str',
            'key_state': 'str'
        }

        self.attribute_map = {
            'kms_key_id': 'kmsKeyId',
            'key_state': 'keyState'
        }

        self._kms_key_id = None
        self._key_state = None

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CustomEncryptionKey.
        Custom Encryption Key (Master Key) ocid.


        :return: The kms_key_id of this CustomEncryptionKey.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CustomEncryptionKey.
        Custom Encryption Key (Master Key) ocid.


        :param kms_key_id: The kms_key_id of this CustomEncryptionKey.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def key_state(self):
        """
        Gets the key_state of this CustomEncryptionKey.
        Life cycle State of the custom key

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETING", "NONE", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The key_state of this CustomEncryptionKey.
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        """
        Sets the key_state of this CustomEncryptionKey.
        Life cycle State of the custom key


        :param key_state: The key_state of this CustomEncryptionKey.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETING", "NONE", "FAILED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(key_state, allowed_values):
            key_state = 'UNKNOWN_ENUM_VALUE'
        self._key_state = key_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
