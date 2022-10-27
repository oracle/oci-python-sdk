# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EncryptionKeyInfoSummary(object):
    """
    This is the summary of an encryption key.
    """

    #: A constant which can be used with the key_source property of a EncryptionKeyInfoSummary.
    #: This constant has a value of "ORACLE_MANAGED"
    KEY_SOURCE_ORACLE_MANAGED = "ORACLE_MANAGED"

    #: A constant which can be used with the key_source property of a EncryptionKeyInfoSummary.
    #: This constant has a value of "CUSTOMER_MANAGED"
    KEY_SOURCE_CUSTOMER_MANAGED = "CUSTOMER_MANAGED"

    #: A constant which can be used with the key_type property of a EncryptionKeyInfoSummary.
    #: This constant has a value of "ACTIVE_DATA"
    KEY_TYPE_ACTIVE_DATA = "ACTIVE_DATA"

    #: A constant which can be used with the key_type property of a EncryptionKeyInfoSummary.
    #: This constant has a value of "ARCHIVAL_DATA"
    KEY_TYPE_ARCHIVAL_DATA = "ARCHIVAL_DATA"

    #: A constant which can be used with the key_type property of a EncryptionKeyInfoSummary.
    #: This constant has a value of "ALL"
    KEY_TYPE_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new EncryptionKeyInfoSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_source:
            The value to assign to the key_source property of this EncryptionKeyInfoSummary.
            Allowed values for this property are: "ORACLE_MANAGED", "CUSTOMER_MANAGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type key_source: str

        :param key_id:
            The value to assign to the key_id property of this EncryptionKeyInfoSummary.
        :type key_id: str

        :param key_type:
            The value to assign to the key_type property of this EncryptionKeyInfoSummary.
            Allowed values for this property are: "ACTIVE_DATA", "ARCHIVAL_DATA", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type key_type: str

        """
        self.swagger_types = {
            'key_source': 'str',
            'key_id': 'str',
            'key_type': 'str'
        }

        self.attribute_map = {
            'key_source': 'keySource',
            'key_id': 'keyId',
            'key_type': 'keyType'
        }

        self._key_source = None
        self._key_id = None
        self._key_type = None

    @property
    def key_source(self):
        """
        **[Required]** Gets the key_source of this EncryptionKeyInfoSummary.
        This is the source of the encryption key.

        Allowed values for this property are: "ORACLE_MANAGED", "CUSTOMER_MANAGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The key_source of this EncryptionKeyInfoSummary.
        :rtype: str
        """
        return self._key_source

    @key_source.setter
    def key_source(self, key_source):
        """
        Sets the key_source of this EncryptionKeyInfoSummary.
        This is the source of the encryption key.


        :param key_source: The key_source of this EncryptionKeyInfoSummary.
        :type: str
        """
        allowed_values = ["ORACLE_MANAGED", "CUSTOMER_MANAGED"]
        if not value_allowed_none_or_none_sentinel(key_source, allowed_values):
            key_source = 'UNKNOWN_ENUM_VALUE'
        self._key_source = key_source

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this EncryptionKeyInfoSummary.
        This is the key OCID of the encryption key (null if Oracle-managed).


        :return: The key_id of this EncryptionKeyInfoSummary.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this EncryptionKeyInfoSummary.
        This is the key OCID of the encryption key (null if Oracle-managed).


        :param key_id: The key_id of this EncryptionKeyInfoSummary.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_type(self):
        """
        **[Required]** Gets the key_type of this EncryptionKeyInfoSummary.
        This is the type of data to be encrypted. It can be either active or archival.

        Allowed values for this property are: "ACTIVE_DATA", "ARCHIVAL_DATA", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The key_type of this EncryptionKeyInfoSummary.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """
        Sets the key_type of this EncryptionKeyInfoSummary.
        This is the type of data to be encrypted. It can be either active or archival.


        :param key_type: The key_type of this EncryptionKeyInfoSummary.
        :type: str
        """
        allowed_values = ["ACTIVE_DATA", "ARCHIVAL_DATA", "ALL"]
        if not value_allowed_none_or_none_sentinel(key_type, allowed_values):
            key_type = 'UNKNOWN_ENUM_VALUE'
        self._key_type = key_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
