# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActivateBdsMetastoreConfigurationDetails(object):
    """
    The reqeust body when activating a BDS metastore configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ActivateBdsMetastoreConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bds_api_key_passphrase:
            The value to assign to the bds_api_key_passphrase property of this ActivateBdsMetastoreConfigurationDetails.
        :type bds_api_key_passphrase: str

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this ActivateBdsMetastoreConfigurationDetails.
        :type cluster_admin_password: str

        """
        self.swagger_types = {
            'bds_api_key_passphrase': 'str',
            'cluster_admin_password': 'str'
        }

        self.attribute_map = {
            'bds_api_key_passphrase': 'bdsApiKeyPassphrase',
            'cluster_admin_password': 'clusterAdminPassword'
        }

        self._bds_api_key_passphrase = None
        self._cluster_admin_password = None

    @property
    def bds_api_key_passphrase(self):
        """
        Gets the bds_api_key_passphrase of this ActivateBdsMetastoreConfigurationDetails.
        Base-64 encoded passphrase of the BDS Api Key. Set only if metastore's type is EXTERNAL.


        :return: The bds_api_key_passphrase of this ActivateBdsMetastoreConfigurationDetails.
        :rtype: str
        """
        return self._bds_api_key_passphrase

    @bds_api_key_passphrase.setter
    def bds_api_key_passphrase(self, bds_api_key_passphrase):
        """
        Sets the bds_api_key_passphrase of this ActivateBdsMetastoreConfigurationDetails.
        Base-64 encoded passphrase of the BDS Api Key. Set only if metastore's type is EXTERNAL.


        :param bds_api_key_passphrase: The bds_api_key_passphrase of this ActivateBdsMetastoreConfigurationDetails.
        :type: str
        """
        self._bds_api_key_passphrase = bds_api_key_passphrase

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this ActivateBdsMetastoreConfigurationDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this ActivateBdsMetastoreConfigurationDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this ActivateBdsMetastoreConfigurationDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this ActivateBdsMetastoreConfigurationDetails.
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
