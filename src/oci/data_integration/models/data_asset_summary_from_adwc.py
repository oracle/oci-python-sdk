# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_asset_summary import DataAssetSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetSummaryFromAdwc(DataAssetSummary):
    """
    Summary details for the Autonomous Data Warehouse data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetSummaryFromAdwc object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataAssetSummaryFromAdwc.model_type` attribute
        of this class is ``ORACLE_ADWC_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataAssetSummaryFromAdwc.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataAssetSummaryFromAdwc.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAssetSummaryFromAdwc.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DataAssetSummaryFromAdwc.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAssetSummaryFromAdwc.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAssetSummaryFromAdwc.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataAssetSummaryFromAdwc.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetSummaryFromAdwc.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAssetSummaryFromAdwc.
        :type asset_properties: dict(str, str)

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAssetSummaryFromAdwc.
        :type native_type_system: oci.data_integration.models.TypeSystem

        :param object_version:
            The value to assign to the object_version property of this DataAssetSummaryFromAdwc.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this DataAssetSummaryFromAdwc.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this DataAssetSummaryFromAdwc.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param service_name:
            The value to assign to the service_name property of this DataAssetSummaryFromAdwc.
        :type service_name: str

        :param service_names:
            The value to assign to the service_names property of this DataAssetSummaryFromAdwc.
        :type service_names: list[str]

        :param driver_class:
            The value to assign to the driver_class property of this DataAssetSummaryFromAdwc.
        :type driver_class: str

        :param default_connection:
            The value to assign to the default_connection property of this DataAssetSummaryFromAdwc.
        :type default_connection: oci.data_integration.models.ConnectionSummaryFromAdwc

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'native_type_system': 'TypeSystem',
            'object_version': 'int',
            'parent_ref': 'ParentReference',
            'metadata': 'ObjectMetadata',
            'service_name': 'str',
            'service_names': 'list[str]',
            'driver_class': 'str',
            'default_connection': 'ConnectionSummaryFromAdwc'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'native_type_system': 'nativeTypeSystem',
            'object_version': 'objectVersion',
            'parent_ref': 'parentRef',
            'metadata': 'metadata',
            'service_name': 'serviceName',
            'service_names': 'serviceNames',
            'driver_class': 'driverClass',
            'default_connection': 'defaultConnection'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._native_type_system = None
        self._object_version = None
        self._parent_ref = None
        self._metadata = None
        self._service_name = None
        self._service_names = None
        self._driver_class = None
        self._default_connection = None
        self._model_type = 'ORACLE_ADWC_DATA_ASSET'

    @property
    def service_name(self):
        """
        Gets the service_name of this DataAssetSummaryFromAdwc.
        The Autonomous Data Warehouse instance service name.


        :return: The service_name of this DataAssetSummaryFromAdwc.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this DataAssetSummaryFromAdwc.
        The Autonomous Data Warehouse instance service name.


        :param service_name: The service_name of this DataAssetSummaryFromAdwc.
        :type: str
        """
        self._service_name = service_name

    @property
    def service_names(self):
        """
        Gets the service_names of this DataAssetSummaryFromAdwc.
        Array of service names that are available for selection in the serviceName property.


        :return: The service_names of this DataAssetSummaryFromAdwc.
        :rtype: list[str]
        """
        return self._service_names

    @service_names.setter
    def service_names(self, service_names):
        """
        Sets the service_names of this DataAssetSummaryFromAdwc.
        Array of service names that are available for selection in the serviceName property.


        :param service_names: The service_names of this DataAssetSummaryFromAdwc.
        :type: list[str]
        """
        self._service_names = service_names

    @property
    def driver_class(self):
        """
        Gets the driver_class of this DataAssetSummaryFromAdwc.
        The Autonomous Data Warehouse driver class.


        :return: The driver_class of this DataAssetSummaryFromAdwc.
        :rtype: str
        """
        return self._driver_class

    @driver_class.setter
    def driver_class(self, driver_class):
        """
        Sets the driver_class of this DataAssetSummaryFromAdwc.
        The Autonomous Data Warehouse driver class.


        :param driver_class: The driver_class of this DataAssetSummaryFromAdwc.
        :type: str
        """
        self._driver_class = driver_class

    @property
    def default_connection(self):
        """
        Gets the default_connection of this DataAssetSummaryFromAdwc.

        :return: The default_connection of this DataAssetSummaryFromAdwc.
        :rtype: oci.data_integration.models.ConnectionSummaryFromAdwc
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this DataAssetSummaryFromAdwc.

        :param default_connection: The default_connection of this DataAssetSummaryFromAdwc.
        :type: oci.data_integration.models.ConnectionSummaryFromAdwc
        """
        self._default_connection = default_connection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
