# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataAssetDetails(object):
    """
    Properties used in data asset update operations.
    """

    #: A constant which can be used with the model_type property of a CreateDataAssetDetails.
    #: This constant has a value of "ORACLE_DATA_ASSET"
    MODEL_TYPE_ORACLE_DATA_ASSET = "ORACLE_DATA_ASSET"

    #: A constant which can be used with the model_type property of a CreateDataAssetDetails.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE_DATA_ASSET"
    MODEL_TYPE_ORACLE_OBJECT_STORAGE_DATA_ASSET = "ORACLE_OBJECT_STORAGE_DATA_ASSET"

    #: A constant which can be used with the model_type property of a CreateDataAssetDetails.
    #: This constant has a value of "ORACLE_ATP_DATA_ASSET"
    MODEL_TYPE_ORACLE_ATP_DATA_ASSET = "ORACLE_ATP_DATA_ASSET"

    #: A constant which can be used with the model_type property of a CreateDataAssetDetails.
    #: This constant has a value of "ORACLE_ADWC_DATA_ASSET"
    MODEL_TYPE_ORACLE_ADWC_DATA_ASSET = "ORACLE_ADWC_DATA_ASSET"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataAssetDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.CreateDataAssetFromOracle`
        * :class:`~oci.data_integration.models.CreateDataAssetFromAdwc`
        * :class:`~oci.data_integration.models.CreateDataAssetFromAtp`
        * :class:`~oci.data_integration.models.CreateDataAssetFromObjectStorage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateDataAssetDetails.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateDataAssetDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateDataAssetDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this CreateDataAssetDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDataAssetDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateDataAssetDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateDataAssetDetails.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this CreateDataAssetDetails.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this CreateDataAssetDetails.
        :type asset_properties: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateDataAssetDetails.
        :type registry_metadata: RegistryMetadata

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
            'registry_metadata': 'RegistryMetadata'
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
            'registry_metadata': 'registryMetadata'
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
        self._registry_metadata = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'ORACLE_DATA_ASSET':
            return 'CreateDataAssetFromOracle'

        if type == 'ORACLE_ADWC_DATA_ASSET':
            return 'CreateDataAssetFromAdwc'

        if type == 'ORACLE_ATP_DATA_ASSET':
            return 'CreateDataAssetFromAtp'

        if type == 'ORACLE_OBJECT_STORAGE_DATA_ASSET':
            return 'CreateDataAssetFromObjectStorage'
        else:
            return 'CreateDataAssetDetails'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this CreateDataAssetDetails.
        The type of the data asset.

        Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET"


        :return: The model_type of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateDataAssetDetails.
        The type of the data asset.


        :param model_type: The model_type of this CreateDataAssetDetails.
        :type: str
        """
        allowed_values = ["ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this CreateDataAssetDetails.
        Currently not used on data asset creation. Reserved for future.


        :return: The key of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateDataAssetDetails.
        Currently not used on data asset creation. Reserved for future.


        :param key: The key of this CreateDataAssetDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateDataAssetDetails.
        The model version of an object.


        :return: The model_version of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateDataAssetDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateDataAssetDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateDataAssetDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :return: The name of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDataAssetDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :param name: The name of this CreateDataAssetDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateDataAssetDetails.
        Detailed description for the object.


        :return: The description of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDataAssetDetails.
        Detailed description for the object.


        :param description: The description of this CreateDataAssetDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateDataAssetDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateDataAssetDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateDataAssetDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateDataAssetDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateDataAssetDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :return: The identifier of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateDataAssetDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :param identifier: The identifier of this CreateDataAssetDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def external_key(self):
        """
        Gets the external_key of this CreateDataAssetDetails.
        The external key for the object


        :return: The external_key of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this CreateDataAssetDetails.
        The external key for the object


        :param external_key: The external_key of this CreateDataAssetDetails.
        :type: str
        """
        self._external_key = external_key

    @property
    def asset_properties(self):
        """
        Gets the asset_properties of this CreateDataAssetDetails.
        assetProperties


        :return: The asset_properties of this CreateDataAssetDetails.
        :rtype: dict(str, str)
        """
        return self._asset_properties

    @asset_properties.setter
    def asset_properties(self, asset_properties):
        """
        Sets the asset_properties of this CreateDataAssetDetails.
        assetProperties


        :param asset_properties: The asset_properties of this CreateDataAssetDetails.
        :type: dict(str, str)
        """
        self._asset_properties = asset_properties

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CreateDataAssetDetails.

        :return: The registry_metadata of this CreateDataAssetDetails.
        :rtype: RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateDataAssetDetails.

        :param registry_metadata: The registry_metadata of this CreateDataAssetDetails.
        :type: RegistryMetadata
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
