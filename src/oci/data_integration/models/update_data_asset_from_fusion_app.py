# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_data_asset_details import UpdateDataAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDataAssetFromFusionApp(UpdateDataAssetDetails):
    """
    Details for the Autonomous Transaction Processing data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDataAssetFromFusionApp object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.UpdateDataAssetFromFusionApp.model_type` attribute
        of this class is ``FUSION_APP_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UpdateDataAssetFromFusionApp.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this UpdateDataAssetFromFusionApp.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UpdateDataAssetFromFusionApp.
        :type model_version: str

        :param name:
            The value to assign to the name property of this UpdateDataAssetFromFusionApp.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateDataAssetFromFusionApp.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateDataAssetFromFusionApp.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this UpdateDataAssetFromFusionApp.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this UpdateDataAssetFromFusionApp.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this UpdateDataAssetFromFusionApp.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this UpdateDataAssetFromFusionApp.
        :type asset_properties: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateDataAssetFromFusionApp.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param service_url:
            The value to assign to the service_url property of this UpdateDataAssetFromFusionApp.
        :type service_url: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'registry_metadata': 'RegistryMetadata',
            'service_url': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'registry_metadata': 'registryMetadata',
            'service_url': 'serviceUrl'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._registry_metadata = None
        self._service_url = None
        self._model_type = 'FUSION_APP_DATA_ASSET'

    @property
    def service_url(self):
        """
        Gets the service_url of this UpdateDataAssetFromFusionApp.
        The service url of the BI Server.


        :return: The service_url of this UpdateDataAssetFromFusionApp.
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """
        Sets the service_url of this UpdateDataAssetFromFusionApp.
        The service url of the BI Server.


        :param service_url: The service_url of this UpdateDataAssetFromFusionApp.
        :type: str
        """
        self._service_url = service_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
