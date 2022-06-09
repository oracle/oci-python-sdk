# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsKeyStoreMySqlDetails(object):
    """
    The details of the key store.
    """

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreMySqlDetails.
    #: This constant has a value of "CLIENT_CERTIFICATE_PEM"
    KEY_STORE_TYPE_CLIENT_CERTIFICATE_PEM = "CLIENT_CERTIFICATE_PEM"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreMySqlDetails.
    #: This constant has a value of "CLIENT_PRIVATE_KEY_PEM"
    KEY_STORE_TYPE_CLIENT_PRIVATE_KEY_PEM = "CLIENT_PRIVATE_KEY_PEM"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreMySqlDetails.
    #: This constant has a value of "CA_CERTIFICATE_PEM"
    KEY_STORE_TYPE_CA_CERTIFICATE_PEM = "CA_CERTIFICATE_PEM"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsKeyStoreMySqlDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_store_type:
            The value to assign to the key_store_type property of this DatabaseToolsKeyStoreMySqlDetails.
            Allowed values for this property are: "CLIENT_CERTIFICATE_PEM", "CLIENT_PRIVATE_KEY_PEM", "CA_CERTIFICATE_PEM"
        :type key_store_type: str

        :param key_store_content:
            The value to assign to the key_store_content property of this DatabaseToolsKeyStoreMySqlDetails.
        :type key_store_content: oci.database_tools.models.DatabaseToolsKeyStoreContentMySqlDetails

        :param key_store_password:
            The value to assign to the key_store_password property of this DatabaseToolsKeyStoreMySqlDetails.
        :type key_store_password: oci.database_tools.models.DatabaseToolsKeyStorePasswordMySqlDetails

        """
        self.swagger_types = {
            'key_store_type': 'str',
            'key_store_content': 'DatabaseToolsKeyStoreContentMySqlDetails',
            'key_store_password': 'DatabaseToolsKeyStorePasswordMySqlDetails'
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
        Gets the key_store_type of this DatabaseToolsKeyStoreMySqlDetails.
        The key store type.

        Allowed values for this property are: "CLIENT_CERTIFICATE_PEM", "CLIENT_PRIVATE_KEY_PEM", "CA_CERTIFICATE_PEM"


        :return: The key_store_type of this DatabaseToolsKeyStoreMySqlDetails.
        :rtype: str
        """
        return self._key_store_type

    @key_store_type.setter
    def key_store_type(self, key_store_type):
        """
        Sets the key_store_type of this DatabaseToolsKeyStoreMySqlDetails.
        The key store type.


        :param key_store_type: The key_store_type of this DatabaseToolsKeyStoreMySqlDetails.
        :type: str
        """
        allowed_values = ["CLIENT_CERTIFICATE_PEM", "CLIENT_PRIVATE_KEY_PEM", "CA_CERTIFICATE_PEM"]
        if not value_allowed_none_or_none_sentinel(key_store_type, allowed_values):
            raise ValueError(
                "Invalid value for `key_store_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._key_store_type = key_store_type

    @property
    def key_store_content(self):
        """
        Gets the key_store_content of this DatabaseToolsKeyStoreMySqlDetails.

        :return: The key_store_content of this DatabaseToolsKeyStoreMySqlDetails.
        :rtype: oci.database_tools.models.DatabaseToolsKeyStoreContentMySqlDetails
        """
        return self._key_store_content

    @key_store_content.setter
    def key_store_content(self, key_store_content):
        """
        Sets the key_store_content of this DatabaseToolsKeyStoreMySqlDetails.

        :param key_store_content: The key_store_content of this DatabaseToolsKeyStoreMySqlDetails.
        :type: oci.database_tools.models.DatabaseToolsKeyStoreContentMySqlDetails
        """
        self._key_store_content = key_store_content

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this DatabaseToolsKeyStoreMySqlDetails.

        :return: The key_store_password of this DatabaseToolsKeyStoreMySqlDetails.
        :rtype: oci.database_tools.models.DatabaseToolsKeyStorePasswordMySqlDetails
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this DatabaseToolsKeyStoreMySqlDetails.

        :param key_store_password: The key_store_password of this DatabaseToolsKeyStoreMySqlDetails.
        :type: oci.database_tools.models.DatabaseToolsKeyStorePasswordMySqlDetails
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
