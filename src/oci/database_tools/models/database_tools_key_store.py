# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsKeyStore(object):
    """
    The details of the key store.
    """

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStore.
    #: This constant has a value of "JAVA_KEY_STORE"
    KEY_STORE_TYPE_JAVA_KEY_STORE = "JAVA_KEY_STORE"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStore.
    #: This constant has a value of "JAVA_TRUST_STORE"
    KEY_STORE_TYPE_JAVA_TRUST_STORE = "JAVA_TRUST_STORE"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStore.
    #: This constant has a value of "PKCS12"
    KEY_STORE_TYPE_PKCS12 = "PKCS12"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStore.
    #: This constant has a value of "SSO"
    KEY_STORE_TYPE_SSO = "SSO"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsKeyStore object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_store_type:
            The value to assign to the key_store_type property of this DatabaseToolsKeyStore.
            Allowed values for this property are: "JAVA_KEY_STORE", "JAVA_TRUST_STORE", "PKCS12", "SSO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type key_store_type: str

        :param key_store_content:
            The value to assign to the key_store_content property of this DatabaseToolsKeyStore.
        :type key_store_content: oci.database_tools.models.DatabaseToolsKeyStoreContent

        :param key_store_password:
            The value to assign to the key_store_password property of this DatabaseToolsKeyStore.
        :type key_store_password: oci.database_tools.models.DatabaseToolsKeyStorePassword

        """
        self.swagger_types = {
            'key_store_type': 'str',
            'key_store_content': 'DatabaseToolsKeyStoreContent',
            'key_store_password': 'DatabaseToolsKeyStorePassword'
        }

        self.attribute_map = {
            'key_store_type': 'keyStoreType',
            'key_store_content': 'keyStoreContent',
            'key_store_password': 'keyStorePassword'
        }

        self._key_store_type = None
        self._key_store_content = None
        self._key_store_password = None

    @property
    def key_store_type(self):
        """
        Gets the key_store_type of this DatabaseToolsKeyStore.
        The key store type.

        Allowed values for this property are: "JAVA_KEY_STORE", "JAVA_TRUST_STORE", "PKCS12", "SSO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The key_store_type of this DatabaseToolsKeyStore.
        :rtype: str
        """
        return self._key_store_type

    @key_store_type.setter
    def key_store_type(self, key_store_type):
        """
        Sets the key_store_type of this DatabaseToolsKeyStore.
        The key store type.


        :param key_store_type: The key_store_type of this DatabaseToolsKeyStore.
        :type: str
        """
        allowed_values = ["JAVA_KEY_STORE", "JAVA_TRUST_STORE", "PKCS12", "SSO"]
        if not value_allowed_none_or_none_sentinel(key_store_type, allowed_values):
            key_store_type = 'UNKNOWN_ENUM_VALUE'
        self._key_store_type = key_store_type

    @property
    def key_store_content(self):
        """
        Gets the key_store_content of this DatabaseToolsKeyStore.

        :return: The key_store_content of this DatabaseToolsKeyStore.
        :rtype: oci.database_tools.models.DatabaseToolsKeyStoreContent
        """
        return self._key_store_content

    @key_store_content.setter
    def key_store_content(self, key_store_content):
        """
        Sets the key_store_content of this DatabaseToolsKeyStore.

        :param key_store_content: The key_store_content of this DatabaseToolsKeyStore.
        :type: oci.database_tools.models.DatabaseToolsKeyStoreContent
        """
        self._key_store_content = key_store_content

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this DatabaseToolsKeyStore.

        :return: The key_store_password of this DatabaseToolsKeyStore.
        :rtype: oci.database_tools.models.DatabaseToolsKeyStorePassword
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this DatabaseToolsKeyStore.

        :param key_store_password: The key_store_password of this DatabaseToolsKeyStore.
        :type: oci.database_tools.models.DatabaseToolsKeyStorePassword
        """
        self._key_store_password = key_store_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
