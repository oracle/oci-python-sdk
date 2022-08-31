# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDetachDataAssetDetails(object):
    """
    The detach DataAsset payload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDetachDataAssetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_assets:
            The value to assign to the data_assets property of this CreateDetachDataAssetDetails.
        :type data_assets: list[oci.data_connectivity.models.DataAsset]

        """
        self.swagger_types = {
            'data_assets': 'list[DataAsset]'
        }

        self.attribute_map = {
            'data_assets': 'dataAssets'
        }

        self._data_assets = None

    @property
    def data_assets(self):
        """
        **[Required]** Gets the data_assets of this CreateDetachDataAssetDetails.
        The array of DataAsset keys.


        :return: The data_assets of this CreateDetachDataAssetDetails.
        :rtype: list[oci.data_connectivity.models.DataAsset]
        """
        return self._data_assets

    @data_assets.setter
    def data_assets(self, data_assets):
        """
        Sets the data_assets of this CreateDetachDataAssetDetails.
        The array of DataAsset keys.


        :param data_assets: The data_assets of this CreateDetachDataAssetDetails.
        :type: list[oci.data_connectivity.models.DataAsset]
        """
        self._data_assets = data_assets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
