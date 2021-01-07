# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionValidationDetails(object):
    """
    The properties used in create connection validation operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionValidationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_asset:
            The value to assign to the data_asset property of this CreateConnectionValidationDetails.
        :type data_asset: oci.data_integration.models.CreateDataAssetDetails

        :param connection:
            The value to assign to the connection property of this CreateConnectionValidationDetails.
        :type connection: oci.data_integration.models.CreateConnectionDetails

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateConnectionValidationDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        """
        self.swagger_types = {
            'data_asset': 'CreateDataAssetDetails',
            'connection': 'CreateConnectionDetails',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'data_asset': 'dataAsset',
            'connection': 'connection',
            'registry_metadata': 'registryMetadata'
        }

        self._data_asset = None
        self._connection = None
        self._registry_metadata = None

    @property
    def data_asset(self):
        """
        Gets the data_asset of this CreateConnectionValidationDetails.

        :return: The data_asset of this CreateConnectionValidationDetails.
        :rtype: oci.data_integration.models.CreateDataAssetDetails
        """
        return self._data_asset

    @data_asset.setter
    def data_asset(self, data_asset):
        """
        Sets the data_asset of this CreateConnectionValidationDetails.

        :param data_asset: The data_asset of this CreateConnectionValidationDetails.
        :type: oci.data_integration.models.CreateDataAssetDetails
        """
        self._data_asset = data_asset

    @property
    def connection(self):
        """
        Gets the connection of this CreateConnectionValidationDetails.

        :return: The connection of this CreateConnectionValidationDetails.
        :rtype: oci.data_integration.models.CreateConnectionDetails
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this CreateConnectionValidationDetails.

        :param connection: The connection of this CreateConnectionValidationDetails.
        :type: oci.data_integration.models.CreateConnectionDetails
        """
        self._connection = connection

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CreateConnectionValidationDetails.

        :return: The registry_metadata of this CreateConnectionValidationDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateConnectionValidationDetails.

        :param registry_metadata: The registry_metadata of this CreateConnectionValidationDetails.
        :type: oci.data_integration.models.RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
