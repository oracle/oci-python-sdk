# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_read_attribute import AbstractReadAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BipReadAttributes(AbstractReadAttribute):
    """
    Properties to configure reading from a FUSION_APP BIP data asset / connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BipReadAttributes object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.BipReadAttributes.model_type` attribute
        of this class is ``BIP_READ_ATTRIBUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this BipReadAttributes.
            Allowed values for this property are: "ORACLEREADATTRIBUTE", "ORACLE_READ_ATTRIBUTE", "BICC_READ_ATTRIBUTE", "BIP_READ_ATTRIBUTE"
        :type model_type: str

        :param fetch_size:
            The value to assign to the fetch_size property of this BipReadAttributes.
        :type fetch_size: int

        :param row_limit:
            The value to assign to the row_limit property of this BipReadAttributes.
        :type row_limit: int

        :param offset_parameter:
            The value to assign to the offset_parameter property of this BipReadAttributes.
        :type offset_parameter: str

        :param fetch_next_rows_parameter:
            The value to assign to the fetch_next_rows_parameter property of this BipReadAttributes.
        :type fetch_next_rows_parameter: str

        :param custom_parameters:
            The value to assign to the custom_parameters property of this BipReadAttributes.
        :type custom_parameters: list[oci.data_integration.models.BipReportParameterValue]

        :param staging_data_asset:
            The value to assign to the staging_data_asset property of this BipReadAttributes.
        :type staging_data_asset: oci.data_integration.models.DataAssetSummaryFromObjectStorage

        :param staging_connection:
            The value to assign to the staging_connection property of this BipReadAttributes.
        :type staging_connection: oci.data_integration.models.ConnectionSummaryFromObjectStorage

        :param bucket_schema:
            The value to assign to the bucket_schema property of this BipReadAttributes.
        :type bucket_schema: oci.data_integration.models.Schema

        """
        self.swagger_types = {
            'model_type': 'str',
            'fetch_size': 'int',
            'row_limit': 'int',
            'offset_parameter': 'str',
            'fetch_next_rows_parameter': 'str',
            'custom_parameters': 'list[BipReportParameterValue]',
            'staging_data_asset': 'DataAssetSummaryFromObjectStorage',
            'staging_connection': 'ConnectionSummaryFromObjectStorage',
            'bucket_schema': 'Schema'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'fetch_size': 'fetchSize',
            'row_limit': 'rowLimit',
            'offset_parameter': 'offsetParameter',
            'fetch_next_rows_parameter': 'fetchNextRowsParameter',
            'custom_parameters': 'customParameters',
            'staging_data_asset': 'stagingDataAsset',
            'staging_connection': 'stagingConnection',
            'bucket_schema': 'bucketSchema'
        }

        self._model_type = None
        self._fetch_size = None
        self._row_limit = None
        self._offset_parameter = None
        self._fetch_next_rows_parameter = None
        self._custom_parameters = None
        self._staging_data_asset = None
        self._staging_connection = None
        self._bucket_schema = None
        self._model_type = 'BIP_READ_ATTRIBUTE'

    @property
    def fetch_size(self):
        """
        Gets the fetch_size of this BipReadAttributes.
        The fetch size for reading.


        :return: The fetch_size of this BipReadAttributes.
        :rtype: int
        """
        return self._fetch_size

    @fetch_size.setter
    def fetch_size(self, fetch_size):
        """
        Sets the fetch_size of this BipReadAttributes.
        The fetch size for reading.


        :param fetch_size: The fetch_size of this BipReadAttributes.
        :type: int
        """
        self._fetch_size = fetch_size

    @property
    def row_limit(self):
        """
        Gets the row_limit of this BipReadAttributes.
        The maximum number of rows to read.


        :return: The row_limit of this BipReadAttributes.
        :rtype: int
        """
        return self._row_limit

    @row_limit.setter
    def row_limit(self, row_limit):
        """
        Sets the row_limit of this BipReadAttributes.
        The maximum number of rows to read.


        :param row_limit: The row_limit of this BipReadAttributes.
        :type: int
        """
        self._row_limit = row_limit

    @property
    def offset_parameter(self):
        """
        Gets the offset_parameter of this BipReadAttributes.
        Name of BIP report parameter to control the start of the chunk


        :return: The offset_parameter of this BipReadAttributes.
        :rtype: str
        """
        return self._offset_parameter

    @offset_parameter.setter
    def offset_parameter(self, offset_parameter):
        """
        Sets the offset_parameter of this BipReadAttributes.
        Name of BIP report parameter to control the start of the chunk


        :param offset_parameter: The offset_parameter of this BipReadAttributes.
        :type: str
        """
        self._offset_parameter = offset_parameter

    @property
    def fetch_next_rows_parameter(self):
        """
        Gets the fetch_next_rows_parameter of this BipReadAttributes.
        Name of BIP report parameter to control the start of the chunk


        :return: The fetch_next_rows_parameter of this BipReadAttributes.
        :rtype: str
        """
        return self._fetch_next_rows_parameter

    @fetch_next_rows_parameter.setter
    def fetch_next_rows_parameter(self, fetch_next_rows_parameter):
        """
        Sets the fetch_next_rows_parameter of this BipReadAttributes.
        Name of BIP report parameter to control the start of the chunk


        :param fetch_next_rows_parameter: The fetch_next_rows_parameter of this BipReadAttributes.
        :type: str
        """
        self._fetch_next_rows_parameter = fetch_next_rows_parameter

    @property
    def custom_parameters(self):
        """
        Gets the custom_parameters of this BipReadAttributes.
        An array of custom BIP report parameters and their values.


        :return: The custom_parameters of this BipReadAttributes.
        :rtype: list[oci.data_integration.models.BipReportParameterValue]
        """
        return self._custom_parameters

    @custom_parameters.setter
    def custom_parameters(self, custom_parameters):
        """
        Sets the custom_parameters of this BipReadAttributes.
        An array of custom BIP report parameters and their values.


        :param custom_parameters: The custom_parameters of this BipReadAttributes.
        :type: list[oci.data_integration.models.BipReportParameterValue]
        """
        self._custom_parameters = custom_parameters

    @property
    def staging_data_asset(self):
        """
        Gets the staging_data_asset of this BipReadAttributes.

        :return: The staging_data_asset of this BipReadAttributes.
        :rtype: oci.data_integration.models.DataAssetSummaryFromObjectStorage
        """
        return self._staging_data_asset

    @staging_data_asset.setter
    def staging_data_asset(self, staging_data_asset):
        """
        Sets the staging_data_asset of this BipReadAttributes.

        :param staging_data_asset: The staging_data_asset of this BipReadAttributes.
        :type: oci.data_integration.models.DataAssetSummaryFromObjectStorage
        """
        self._staging_data_asset = staging_data_asset

    @property
    def staging_connection(self):
        """
        Gets the staging_connection of this BipReadAttributes.

        :return: The staging_connection of this BipReadAttributes.
        :rtype: oci.data_integration.models.ConnectionSummaryFromObjectStorage
        """
        return self._staging_connection

    @staging_connection.setter
    def staging_connection(self, staging_connection):
        """
        Sets the staging_connection of this BipReadAttributes.

        :param staging_connection: The staging_connection of this BipReadAttributes.
        :type: oci.data_integration.models.ConnectionSummaryFromObjectStorage
        """
        self._staging_connection = staging_connection

    @property
    def bucket_schema(self):
        """
        Gets the bucket_schema of this BipReadAttributes.

        :return: The bucket_schema of this BipReadAttributes.
        :rtype: oci.data_integration.models.Schema
        """
        return self._bucket_schema

    @bucket_schema.setter
    def bucket_schema(self, bucket_schema):
        """
        Sets the bucket_schema of this BipReadAttributes.

        :param bucket_schema: The bucket_schema of this BipReadAttributes.
        :type: oci.data_integration.models.Schema
        """
        self._bucket_schema = bucket_schema

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
