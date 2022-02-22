# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTestNetworkConnectivityDetails(object):
    """
    The network validation payload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTestNetworkConnectivityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_asset_key:
            The value to assign to the data_asset_key property of this CreateTestNetworkConnectivityDetails.
        :type data_asset_key: str

        """
        self.swagger_types = {
            'data_asset_key': 'str'
        }

        self.attribute_map = {
            'data_asset_key': 'dataAssetKey'
        }

        self._data_asset_key = None

    @property
    def data_asset_key(self):
        """
        **[Required]** Gets the data_asset_key of this CreateTestNetworkConnectivityDetails.
        Data Asset key


        :return: The data_asset_key of this CreateTestNetworkConnectivityDetails.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this CreateTestNetworkConnectivityDetails.
        Data Asset key


        :param data_asset_key: The data_asset_key of this CreateTestNetworkConnectivityDetails.
        :type: str
        """
        self._data_asset_key = data_asset_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
