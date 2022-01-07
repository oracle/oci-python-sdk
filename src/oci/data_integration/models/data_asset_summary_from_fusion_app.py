# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_asset_summary import DataAssetSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetSummaryFromFusionApp(DataAssetSummary):
    """
    Summary details for the FUSION_APP data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetSummaryFromFusionApp object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataAssetSummaryFromFusionApp.model_type` attribute
        of this class is ``FUSION_APP_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataAssetSummaryFromFusionApp.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataAssetSummaryFromFusionApp.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAssetSummaryFromFusionApp.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DataAssetSummaryFromFusionApp.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAssetSummaryFromFusionApp.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAssetSummaryFromFusionApp.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataAssetSummaryFromFusionApp.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetSummaryFromFusionApp.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAssetSummaryFromFusionApp.
        :type asset_properties: dict(str, str)

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAssetSummaryFromFusionApp.
        :type native_type_system: oci.data_integration.models.TypeSystem

        :param object_version:
            The value to assign to the object_version property of this DataAssetSummaryFromFusionApp.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this DataAssetSummaryFromFusionApp.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this DataAssetSummaryFromFusionApp.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param service_url:
            The value to assign to the service_url property of this DataAssetSummaryFromFusionApp.
        :type service_url: str

        :param default_connection:
            The value to assign to the default_connection property of this DataAssetSummaryFromFusionApp.
        :type default_connection: oci.data_integration.models.ConnectionSummaryFromBICC

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
            'service_url': 'str',
            'default_connection': 'ConnectionSummaryFromBICC'
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
            'service_url': 'serviceUrl',
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
        self._service_url = None
        self._default_connection = None
        self._model_type = 'FUSION_APP_DATA_ASSET'

    @property
    def service_url(self):
        """
        Gets the service_url of this DataAssetSummaryFromFusionApp.
        The generic JDBC host name.


        :return: The service_url of this DataAssetSummaryFromFusionApp.
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """
        Sets the service_url of this DataAssetSummaryFromFusionApp.
        The generic JDBC host name.


        :param service_url: The service_url of this DataAssetSummaryFromFusionApp.
        :type: str
        """
        self._service_url = service_url

    @property
    def default_connection(self):
        """
        Gets the default_connection of this DataAssetSummaryFromFusionApp.

        :return: The default_connection of this DataAssetSummaryFromFusionApp.
        :rtype: oci.data_integration.models.ConnectionSummaryFromBICC
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this DataAssetSummaryFromFusionApp.

        :param default_connection: The default_connection of this DataAssetSummaryFromFusionApp.
        :type: oci.data_integration.models.ConnectionSummaryFromBICC
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
