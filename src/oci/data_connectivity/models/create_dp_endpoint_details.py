# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDpEndpointDetails(object):
    """
    Properties used in the create operations of the endpoint.
    """

    #: A constant which can be used with the model_type property of a CreateDpEndpointDetails.
    #: This constant has a value of "PRIVATE_END_POINT"
    MODEL_TYPE_PRIVATE_END_POINT = "PRIVATE_END_POINT"

    #: A constant which can be used with the model_type property of a CreateDpEndpointDetails.
    #: This constant has a value of "PUBLIC_END_POINT"
    MODEL_TYPE_PUBLIC_END_POINT = "PUBLIC_END_POINT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDpEndpointDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.CreateDpEndpointFromPublic`
        * :class:`~oci.data_connectivity.models.CreateDpEndpointFromPrivate`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateDpEndpointDetails.
            Allowed values for this property are: "PRIVATE_END_POINT", "PUBLIC_END_POINT"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateDpEndpointDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateDpEndpointDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateDpEndpointDetails.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateDpEndpointDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDpEndpointDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateDpEndpointDetails.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this CreateDpEndpointDetails.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this CreateDpEndpointDetails.
        :type identifier: str

        :param data_assets:
            The value to assign to the data_assets property of this CreateDpEndpointDetails.
        :type data_assets: list[oci.data_connectivity.models.DataAsset]

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'data_assets': 'list[DataAsset]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'data_assets': 'dataAssets'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._data_assets = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'PUBLIC_END_POINT':
            return 'CreateDpEndpointFromPublic'

        if type == 'PRIVATE_END_POINT':
            return 'CreateDpEndpointFromPrivate'
        else:
            return 'CreateDpEndpointDetails'

    @property
    def model_type(self):
        """
        Gets the model_type of this CreateDpEndpointDetails.
        The type of the endpoint.

        Allowed values for this property are: "PRIVATE_END_POINT", "PUBLIC_END_POINT"


        :return: The model_type of this CreateDpEndpointDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateDpEndpointDetails.
        The type of the endpoint.


        :param model_type: The model_type of this CreateDpEndpointDetails.
        :type: str
        """
        allowed_values = ["PRIVATE_END_POINT", "PUBLIC_END_POINT"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this CreateDpEndpointDetails.
        Generated key that can be used in API calls to identify the endpoint. In scenarios where reference to the endpoint is required, a value can be passed in create.


        :return: The key of this CreateDpEndpointDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateDpEndpointDetails.
        Generated key that can be used in API calls to identify the endpoint. In scenarios where reference to the endpoint is required, a value can be passed in create.


        :param key: The key of this CreateDpEndpointDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateDpEndpointDetails.
        The model version of an object.


        :return: The model_version of this CreateDpEndpointDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateDpEndpointDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateDpEndpointDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this CreateDpEndpointDetails.

        :return: The parent_ref of this CreateDpEndpointDetails.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this CreateDpEndpointDetails.

        :param parent_ref: The parent_ref of this CreateDpEndpointDetails.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateDpEndpointDetails.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateDpEndpointDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDpEndpointDetails.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateDpEndpointDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateDpEndpointDetails.
        User-defined description of the endpoint.


        :return: The description of this CreateDpEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDpEndpointDetails.
        User-defined description of the endpoint.


        :param description: The description of this CreateDpEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateDpEndpointDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateDpEndpointDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateDpEndpointDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateDpEndpointDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def object_version(self):
        """
        Gets the object_version of this CreateDpEndpointDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this CreateDpEndpointDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this CreateDpEndpointDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this CreateDpEndpointDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateDpEndpointDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateDpEndpointDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateDpEndpointDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateDpEndpointDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def data_assets(self):
        """
        Gets the data_assets of this CreateDpEndpointDetails.
        The list of data assets that belong to the endpoint.


        :return: The data_assets of this CreateDpEndpointDetails.
        :rtype: list[oci.data_connectivity.models.DataAsset]
        """
        return self._data_assets

    @data_assets.setter
    def data_assets(self, data_assets):
        """
        Sets the data_assets of this CreateDpEndpointDetails.
        The list of data assets that belong to the endpoint.


        :param data_assets: The data_assets of this CreateDpEndpointDetails.
        :type: list[oci.data_connectivity.models.DataAsset]
        """
        self._data_assets = data_assets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
