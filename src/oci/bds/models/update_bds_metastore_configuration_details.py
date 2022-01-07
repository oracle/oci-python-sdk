# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBdsMetastoreConfigurationDetails(object):
    """
    The request body when updating BDS metastore configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBdsMetastoreConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateBdsMetastoreConfigurationDetails.
        :type display_name: str

        :param bds_api_key_id:
            The value to assign to the bds_api_key_id property of this UpdateBdsMetastoreConfigurationDetails.
        :type bds_api_key_id: str

        :param bds_api_key_passphrase:
            The value to assign to the bds_api_key_passphrase property of this UpdateBdsMetastoreConfigurationDetails.
        :type bds_api_key_passphrase: str

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this UpdateBdsMetastoreConfigurationDetails.
        :type cluster_admin_password: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'bds_api_key_id': 'str',
            'bds_api_key_passphrase': 'str',
            'cluster_admin_password': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'bds_api_key_id': 'bdsApiKeyId',
            'bds_api_key_passphrase': 'bdsApiKeyPassphrase',
            'cluster_admin_password': 'clusterAdminPassword'
        }

        self._display_name = None
        self._bds_api_key_id = None
        self._bds_api_key_passphrase = None
        self._cluster_admin_password = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateBdsMetastoreConfigurationDetails.
        The display name of the metastore configuration.


        :return: The display_name of this UpdateBdsMetastoreConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateBdsMetastoreConfigurationDetails.
        The display name of the metastore configuration.


        :param display_name: The display_name of this UpdateBdsMetastoreConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def bds_api_key_id(self):
        """
        Gets the bds_api_key_id of this UpdateBdsMetastoreConfigurationDetails.
        The ID of BDS Api Key used for Data Catalog metastore integration. Set only if metastore's type is EXTERNAL.


        :return: The bds_api_key_id of this UpdateBdsMetastoreConfigurationDetails.
        :rtype: str
        """
        return self._bds_api_key_id

    @bds_api_key_id.setter
    def bds_api_key_id(self, bds_api_key_id):
        """
        Sets the bds_api_key_id of this UpdateBdsMetastoreConfigurationDetails.
        The ID of BDS Api Key used for Data Catalog metastore integration. Set only if metastore's type is EXTERNAL.


        :param bds_api_key_id: The bds_api_key_id of this UpdateBdsMetastoreConfigurationDetails.
        :type: str
        """
        self._bds_api_key_id = bds_api_key_id

    @property
    def bds_api_key_passphrase(self):
        """
        Gets the bds_api_key_passphrase of this UpdateBdsMetastoreConfigurationDetails.
        Base-64 encoded passphrase of the BDS Api Key.


        :return: The bds_api_key_passphrase of this UpdateBdsMetastoreConfigurationDetails.
        :rtype: str
        """
        return self._bds_api_key_passphrase

    @bds_api_key_passphrase.setter
    def bds_api_key_passphrase(self, bds_api_key_passphrase):
        """
        Sets the bds_api_key_passphrase of this UpdateBdsMetastoreConfigurationDetails.
        Base-64 encoded passphrase of the BDS Api Key.


        :param bds_api_key_passphrase: The bds_api_key_passphrase of this UpdateBdsMetastoreConfigurationDetails.
        :type: str
        """
        self._bds_api_key_passphrase = bds_api_key_passphrase

    @property
    def cluster_admin_password(self):
        """
        Gets the cluster_admin_password of this UpdateBdsMetastoreConfigurationDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this UpdateBdsMetastoreConfigurationDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this UpdateBdsMetastoreConfigurationDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this UpdateBdsMetastoreConfigurationDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
