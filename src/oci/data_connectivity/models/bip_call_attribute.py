# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_call_attribute import AbstractCallAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BipCallAttribute(AbstractCallAttribute):
    """
    The call attributes impl
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BipCallAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.BipCallAttribute.model_type` attribute
        of this class is ``BIPCALLATTRIBUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this BipCallAttribute.
            Allowed values for this property are: "BIPCALLATTRIBUTE"
        :type model_type: str

        :param staging_bucket:
            The value to assign to the staging_bucket property of this BipCallAttribute.
        :type staging_bucket: oci.data_connectivity.models.Schema

        :param offset_parameter:
            The value to assign to the offset_parameter property of this BipCallAttribute.
        :type offset_parameter: str

        :param fetch_next_rows_parameter:
            The value to assign to the fetch_next_rows_parameter property of this BipCallAttribute.
        :type fetch_next_rows_parameter: str

        :param staging_data_asset:
            The value to assign to the staging_data_asset property of this BipCallAttribute.
        :type staging_data_asset: oci.data_connectivity.models.DataAsset

        :param staging_connection:
            The value to assign to the staging_connection property of this BipCallAttribute.
        :type staging_connection: oci.data_connectivity.models.Connection

        :param staging_prefix:
            The value to assign to the staging_prefix property of this BipCallAttribute.
        :type staging_prefix: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'staging_bucket': 'Schema',
            'offset_parameter': 'str',
            'fetch_next_rows_parameter': 'str',
            'staging_data_asset': 'DataAsset',
            'staging_connection': 'Connection',
            'staging_prefix': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'staging_bucket': 'stagingBucket',
            'offset_parameter': 'offsetParameter',
            'fetch_next_rows_parameter': 'fetchNextRowsParameter',
            'staging_data_asset': 'stagingDataAsset',
            'staging_connection': 'stagingConnection',
            'staging_prefix': 'stagingPrefix'
        }

        self._model_type = None
        self._staging_bucket = None
        self._offset_parameter = None
        self._fetch_next_rows_parameter = None
        self._staging_data_asset = None
        self._staging_connection = None
        self._staging_prefix = None
        self._model_type = 'BIPCALLATTRIBUTE'

    @property
    def staging_bucket(self):
        """
        Gets the staging_bucket of this BipCallAttribute.

        :return: The staging_bucket of this BipCallAttribute.
        :rtype: oci.data_connectivity.models.Schema
        """
        return self._staging_bucket

    @staging_bucket.setter
    def staging_bucket(self, staging_bucket):
        """
        Sets the staging_bucket of this BipCallAttribute.

        :param staging_bucket: The staging_bucket of this BipCallAttribute.
        :type: oci.data_connectivity.models.Schema
        """
        self._staging_bucket = staging_bucket

    @property
    def offset_parameter(self):
        """
        Gets the offset_parameter of this BipCallAttribute.
        Parameter to set offset


        :return: The offset_parameter of this BipCallAttribute.
        :rtype: str
        """
        return self._offset_parameter

    @offset_parameter.setter
    def offset_parameter(self, offset_parameter):
        """
        Sets the offset_parameter of this BipCallAttribute.
        Parameter to set offset


        :param offset_parameter: The offset_parameter of this BipCallAttribute.
        :type: str
        """
        self._offset_parameter = offset_parameter

    @property
    def fetch_next_rows_parameter(self):
        """
        Gets the fetch_next_rows_parameter of this BipCallAttribute.
        Parameter to fetch next set of rows


        :return: The fetch_next_rows_parameter of this BipCallAttribute.
        :rtype: str
        """
        return self._fetch_next_rows_parameter

    @fetch_next_rows_parameter.setter
    def fetch_next_rows_parameter(self, fetch_next_rows_parameter):
        """
        Sets the fetch_next_rows_parameter of this BipCallAttribute.
        Parameter to fetch next set of rows


        :param fetch_next_rows_parameter: The fetch_next_rows_parameter of this BipCallAttribute.
        :type: str
        """
        self._fetch_next_rows_parameter = fetch_next_rows_parameter

    @property
    def staging_data_asset(self):
        """
        Gets the staging_data_asset of this BipCallAttribute.

        :return: The staging_data_asset of this BipCallAttribute.
        :rtype: oci.data_connectivity.models.DataAsset
        """
        return self._staging_data_asset

    @staging_data_asset.setter
    def staging_data_asset(self, staging_data_asset):
        """
        Sets the staging_data_asset of this BipCallAttribute.

        :param staging_data_asset: The staging_data_asset of this BipCallAttribute.
        :type: oci.data_connectivity.models.DataAsset
        """
        self._staging_data_asset = staging_data_asset

    @property
    def staging_connection(self):
        """
        Gets the staging_connection of this BipCallAttribute.

        :return: The staging_connection of this BipCallAttribute.
        :rtype: oci.data_connectivity.models.Connection
        """
        return self._staging_connection

    @staging_connection.setter
    def staging_connection(self, staging_connection):
        """
        Sets the staging_connection of this BipCallAttribute.

        :param staging_connection: The staging_connection of this BipCallAttribute.
        :type: oci.data_connectivity.models.Connection
        """
        self._staging_connection = staging_connection

    @property
    def staging_prefix(self):
        """
        Gets the staging_prefix of this BipCallAttribute.
        Prefix for the staging DataAsset


        :return: The staging_prefix of this BipCallAttribute.
        :rtype: str
        """
        return self._staging_prefix

    @staging_prefix.setter
    def staging_prefix(self, staging_prefix):
        """
        Sets the staging_prefix of this BipCallAttribute.
        Prefix for the staging DataAsset


        :param staging_prefix: The staging_prefix of this BipCallAttribute.
        :type: str
        """
        self._staging_prefix = staging_prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
