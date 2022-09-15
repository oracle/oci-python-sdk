# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_asset_summary import DataAssetSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetSummaryFromObjectStorage(DataAssetSummary):
    """
    Summary details for the Oracle Object storage data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetSummaryFromObjectStorage object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataAssetSummaryFromObjectStorage.model_type` attribute
        of this class is ``ORACLE_OBJECT_STORAGE_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataAssetSummaryFromObjectStorage.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_HOUSE_DATA_ASSET", "REST_DATA_ASSET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataAssetSummaryFromObjectStorage.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAssetSummaryFromObjectStorage.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DataAssetSummaryFromObjectStorage.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAssetSummaryFromObjectStorage.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAssetSummaryFromObjectStorage.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataAssetSummaryFromObjectStorage.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetSummaryFromObjectStorage.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAssetSummaryFromObjectStorage.
        :type asset_properties: dict(str, str)

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAssetSummaryFromObjectStorage.
        :type native_type_system: oci.data_integration.models.TypeSystem

        :param object_version:
            The value to assign to the object_version property of this DataAssetSummaryFromObjectStorage.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this DataAssetSummaryFromObjectStorage.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this DataAssetSummaryFromObjectStorage.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param oci_region:
            The value to assign to the oci_region property of this DataAssetSummaryFromObjectStorage.
        :type oci_region: str

        :param url:
            The value to assign to the url property of this DataAssetSummaryFromObjectStorage.
        :type url: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this DataAssetSummaryFromObjectStorage.
        :type tenancy_id: str

        :param namespace:
            The value to assign to the namespace property of this DataAssetSummaryFromObjectStorage.
        :type namespace: str

        :param default_connection:
            The value to assign to the default_connection property of this DataAssetSummaryFromObjectStorage.
        :type default_connection: oci.data_integration.models.ConnectionSummaryFromObjectStorage

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
            'oci_region': 'str',
            'url': 'str',
            'tenancy_id': 'str',
            'namespace': 'str',
            'default_connection': 'ConnectionSummaryFromObjectStorage'
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
            'oci_region': 'ociRegion',
            'url': 'url',
            'tenancy_id': 'tenancyId',
            'namespace': 'namespace',
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
        self._oci_region = None
        self._url = None
        self._tenancy_id = None
        self._namespace = None
        self._default_connection = None
        self._model_type = 'ORACLE_OBJECT_STORAGE_DATA_ASSET'

    @property
    def oci_region(self):
        """
        Gets the oci_region of this DataAssetSummaryFromObjectStorage.
        The Oracle Object storage Region ie. us-ashburn-1


        :return: The oci_region of this DataAssetSummaryFromObjectStorage.
        :rtype: str
        """
        return self._oci_region

    @oci_region.setter
    def oci_region(self, oci_region):
        """
        Sets the oci_region of this DataAssetSummaryFromObjectStorage.
        The Oracle Object storage Region ie. us-ashburn-1


        :param oci_region: The oci_region of this DataAssetSummaryFromObjectStorage.
        :type: str
        """
        self._oci_region = oci_region

    @property
    def url(self):
        """
        Gets the url of this DataAssetSummaryFromObjectStorage.
        The Oracle Object storage URL.


        :return: The url of this DataAssetSummaryFromObjectStorage.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DataAssetSummaryFromObjectStorage.
        The Oracle Object storage URL.


        :param url: The url of this DataAssetSummaryFromObjectStorage.
        :type: str
        """
        self._url = url

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this DataAssetSummaryFromObjectStorage.
        The OCI tenancy OCID.


        :return: The tenancy_id of this DataAssetSummaryFromObjectStorage.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this DataAssetSummaryFromObjectStorage.
        The OCI tenancy OCID.


        :param tenancy_id: The tenancy_id of this DataAssetSummaryFromObjectStorage.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def namespace(self):
        """
        Gets the namespace of this DataAssetSummaryFromObjectStorage.
        The namespace for the specified Oracle Object storage resource. You can find the namespace under Object Storage Settings in the Console.


        :return: The namespace of this DataAssetSummaryFromObjectStorage.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this DataAssetSummaryFromObjectStorage.
        The namespace for the specified Oracle Object storage resource. You can find the namespace under Object Storage Settings in the Console.


        :param namespace: The namespace of this DataAssetSummaryFromObjectStorage.
        :type: str
        """
        self._namespace = namespace

    @property
    def default_connection(self):
        """
        Gets the default_connection of this DataAssetSummaryFromObjectStorage.

        :return: The default_connection of this DataAssetSummaryFromObjectStorage.
        :rtype: oci.data_integration.models.ConnectionSummaryFromObjectStorage
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this DataAssetSummaryFromObjectStorage.

        :param default_connection: The default_connection of this DataAssetSummaryFromObjectStorage.
        :type: oci.data_integration.models.ConnectionSummaryFromObjectStorage
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
