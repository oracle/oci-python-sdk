# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .import_inventory_details import ImportInventoryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportInventoryViaAssetsDetails(ImportInventoryDetails):
    """
    Details for importing assets from a file.
    """

    #: A constant which can be used with the asset_type property of a ImportInventoryViaAssetsDetails.
    #: This constant has a value of "VMWARE_VM"
    ASSET_TYPE_VMWARE_VM = "VMWARE_VM"

    #: A constant which can be used with the asset_type property of a ImportInventoryViaAssetsDetails.
    #: This constant has a value of "VM"
    ASSET_TYPE_VM = "VM"

    def __init__(self, **kwargs):
        """
        Initializes a new ImportInventoryViaAssetsDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_bridge.models.ImportInventoryViaAssetsDetails.resource_type` attribute
        of this class is ``ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ImportInventoryViaAssetsDetails.
        :type compartment_id: str

        :param resource_type:
            The value to assign to the resource_type property of this ImportInventoryViaAssetsDetails.
            Allowed values for this property are: "ASSET"
        :type resource_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ImportInventoryViaAssetsDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ImportInventoryViaAssetsDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param data:
            The value to assign to the data property of this ImportInventoryViaAssetsDetails.
        :type data: str

        :param asset_type:
            The value to assign to the asset_type property of this ImportInventoryViaAssetsDetails.
            Allowed values for this property are: "VMWARE_VM", "VM"
        :type asset_type: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'resource_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'data': 'str',
            'asset_type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'resource_type': 'resourceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'data': 'data',
            'asset_type': 'assetType'
        }

        self._compartment_id = None
        self._resource_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._data = None
        self._asset_type = None
        self._resource_type = 'ASSET'

    @property
    def data(self):
        """
        Gets the data of this ImportInventoryViaAssetsDetails.
        The file body to be sent in the request.


        :return: The data of this ImportInventoryViaAssetsDetails.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ImportInventoryViaAssetsDetails.
        The file body to be sent in the request.


        :param data: The data of this ImportInventoryViaAssetsDetails.
        :type: str
        """
        self._data = data

    @property
    def asset_type(self):
        """
        Gets the asset_type of this ImportInventoryViaAssetsDetails.
        The type of asset.

        Allowed values for this property are: "VMWARE_VM", "VM"


        :return: The asset_type of this ImportInventoryViaAssetsDetails.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """
        Sets the asset_type of this ImportInventoryViaAssetsDetails.
        The type of asset.


        :param asset_type: The asset_type of this ImportInventoryViaAssetsDetails.
        :type: str
        """
        allowed_values = ["VMWARE_VM", "VM"]
        if not value_allowed_none_or_none_sentinel(asset_type, allowed_values):
            raise ValueError(
                "Invalid value for `asset_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._asset_type = asset_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
