# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_asset_summary import DataAssetSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetSummaryFromAmazonS3(DataAssetSummary):
    """
    Summary details for the Amazon s3 data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetSummaryFromAmazonS3 object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataAssetSummaryFromAmazonS3.model_type` attribute
        of this class is ``AMAZON_S3_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataAssetSummaryFromAmazonS3.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_HOUSE_DATA_ASSET", "REST_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataAssetSummaryFromAmazonS3.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAssetSummaryFromAmazonS3.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DataAssetSummaryFromAmazonS3.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAssetSummaryFromAmazonS3.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAssetSummaryFromAmazonS3.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataAssetSummaryFromAmazonS3.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetSummaryFromAmazonS3.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAssetSummaryFromAmazonS3.
        :type asset_properties: dict(str, str)

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAssetSummaryFromAmazonS3.
        :type native_type_system: oci.data_integration.models.TypeSystem

        :param object_version:
            The value to assign to the object_version property of this DataAssetSummaryFromAmazonS3.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this DataAssetSummaryFromAmazonS3.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this DataAssetSummaryFromAmazonS3.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param region:
            The value to assign to the region property of this DataAssetSummaryFromAmazonS3.
        :type region: str

        :param default_connection:
            The value to assign to the default_connection property of this DataAssetSummaryFromAmazonS3.
        :type default_connection: oci.data_integration.models.ConnectionSummaryFromAmazonS3

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
            'region': 'str',
            'default_connection': 'ConnectionSummaryFromAmazonS3'
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
            'region': 'region',
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
        self._region = None
        self._default_connection = None
        self._model_type = 'AMAZON_S3_DATA_ASSET'

    @property
    def region(self):
        """
        Gets the region of this DataAssetSummaryFromAmazonS3.
        The region for Amazon s3


        :return: The region of this DataAssetSummaryFromAmazonS3.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this DataAssetSummaryFromAmazonS3.
        The region for Amazon s3


        :param region: The region of this DataAssetSummaryFromAmazonS3.
        :type: str
        """
        self._region = region

    @property
    def default_connection(self):
        """
        Gets the default_connection of this DataAssetSummaryFromAmazonS3.

        :return: The default_connection of this DataAssetSummaryFromAmazonS3.
        :rtype: oci.data_integration.models.ConnectionSummaryFromAmazonS3
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this DataAssetSummaryFromAmazonS3.

        :param default_connection: The default_connection of this DataAssetSummaryFromAmazonS3.
        :type: oci.data_integration.models.ConnectionSummaryFromAmazonS3
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
