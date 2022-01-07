# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetPermissionsSummary(object):
    """
    Permissions object for data assets.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetPermissionsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_asset_key:
            The value to assign to the data_asset_key property of this DataAssetPermissionsSummary.
        :type data_asset_key: str

        :param user_permissions:
            The value to assign to the user_permissions property of this DataAssetPermissionsSummary.
        :type user_permissions: list[str]

        """
        self.swagger_types = {
            'data_asset_key': 'str',
            'user_permissions': 'list[str]'
        }

        self.attribute_map = {
            'data_asset_key': 'dataAssetKey',
            'user_permissions': 'userPermissions'
        }

        self._data_asset_key = None
        self._user_permissions = None

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this DataAssetPermissionsSummary.
        The unique key of the parent data asset.


        :return: The data_asset_key of this DataAssetPermissionsSummary.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this DataAssetPermissionsSummary.
        The unique key of the parent data asset.


        :param data_asset_key: The data_asset_key of this DataAssetPermissionsSummary.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def user_permissions(self):
        """
        Gets the user_permissions of this DataAssetPermissionsSummary.
        An array of permissions.


        :return: The user_permissions of this DataAssetPermissionsSummary.
        :rtype: list[str]
        """
        return self._user_permissions

    @user_permissions.setter
    def user_permissions(self, user_permissions):
        """
        Sets the user_permissions of this DataAssetPermissionsSummary.
        An array of permissions.


        :param user_permissions: The user_permissions of this DataAssetPermissionsSummary.
        :type: list[str]
        """
        self._user_permissions = user_permissions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
