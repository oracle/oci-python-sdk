# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBdsApiKeyDetails(object):
    """
    API key created on user's behalf.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBdsApiKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_id:
            The value to assign to the user_id property of this CreateBdsApiKeyDetails.
        :type user_id: str

        :param passphrase:
            The value to assign to the passphrase property of this CreateBdsApiKeyDetails.
        :type passphrase: str

        :param default_region:
            The value to assign to the default_region property of this CreateBdsApiKeyDetails.
        :type default_region: str

        :param key_alias:
            The value to assign to the key_alias property of this CreateBdsApiKeyDetails.
        :type key_alias: str

        """
        self.swagger_types = {
            'user_id': 'str',
            'passphrase': 'str',
            'default_region': 'str',
            'key_alias': 'str'
        }

        self.attribute_map = {
            'user_id': 'userId',
            'passphrase': 'passphrase',
            'default_region': 'defaultRegion',
            'key_alias': 'keyAlias'
        }

        self._user_id = None
        self._passphrase = None
        self._default_region = None
        self._key_alias = None

    @property
    def user_id(self):
        """
        **[Required]** Gets the user_id of this CreateBdsApiKeyDetails.
        The OCID of the user for whom this new generated API key pair will be created.


        :return: The user_id of this CreateBdsApiKeyDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CreateBdsApiKeyDetails.
        The OCID of the user for whom this new generated API key pair will be created.


        :param user_id: The user_id of this CreateBdsApiKeyDetails.
        :type: str
        """
        self._user_id = user_id

    @property
    def passphrase(self):
        """
        **[Required]** Gets the passphrase of this CreateBdsApiKeyDetails.
        Base64 passphrase used to secure the private key which will be created on user behalf.


        :return: The passphrase of this CreateBdsApiKeyDetails.
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """
        Sets the passphrase of this CreateBdsApiKeyDetails.
        Base64 passphrase used to secure the private key which will be created on user behalf.


        :param passphrase: The passphrase of this CreateBdsApiKeyDetails.
        :type: str
        """
        self._passphrase = passphrase

    @property
    def default_region(self):
        """
        Gets the default_region of this CreateBdsApiKeyDetails.
        The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/
        for additional information.


        :return: The default_region of this CreateBdsApiKeyDetails.
        :rtype: str
        """
        return self._default_region

    @default_region.setter
    def default_region(self, default_region):
        """
        Sets the default_region of this CreateBdsApiKeyDetails.
        The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/
        for additional information.


        :param default_region: The default_region of this CreateBdsApiKeyDetails.
        :type: str
        """
        self._default_region = default_region

    @property
    def key_alias(self):
        """
        **[Required]** Gets the key_alias of this CreateBdsApiKeyDetails.
        User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster.
        Only ASCII alphanumeric characters with no spaces allowed.


        :return: The key_alias of this CreateBdsApiKeyDetails.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        """
        Sets the key_alias of this CreateBdsApiKeyDetails.
        User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster.
        Only ASCII alphanumeric characters with no spaces allowed.


        :param key_alias: The key_alias of this CreateBdsApiKeyDetails.
        :type: str
        """
        self._key_alias = key_alias

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
