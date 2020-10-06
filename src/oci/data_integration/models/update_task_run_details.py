# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTaskRunDetails(object):
    """
    Properties used in task run update operations.
    """

    #: A constant which can be used with the status property of a UpdateTaskRunDetails.
    #: This constant has a value of "TERMINATING"
    STATUS_TERMINATING = "TERMINATING"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTaskRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this UpdateTaskRunDetails.
        :type key: str

        :param status:
            The value to assign to the status property of this UpdateTaskRunDetails.
            Allowed values for this property are: "TERMINATING"
        :type status: str

        :param model_type:
            The value to assign to the model_type property of this UpdateTaskRunDetails.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this UpdateTaskRunDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this UpdateTaskRunDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateTaskRunDetails.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this UpdateTaskRunDetails.
        :type object_version: int

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateTaskRunDetails.
        :type registry_metadata: RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'status': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'status': 'status',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._status = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_version = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        Gets the key of this UpdateTaskRunDetails.
        The key of the object.


        :return: The key of this UpdateTaskRunDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this UpdateTaskRunDetails.
        The key of the object.


        :param key: The key of this UpdateTaskRunDetails.
        :type: str
        """
        self._key = key

    @property
    def status(self):
        """
        Gets the status of this UpdateTaskRunDetails.
        The status of the object.

        Allowed values for this property are: "TERMINATING"


        :return: The status of this UpdateTaskRunDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateTaskRunDetails.
        The status of the object.


        :param status: The status of this UpdateTaskRunDetails.
        :type: str
        """
        allowed_values = ["TERMINATING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def model_type(self):
        """
        Gets the model_type of this UpdateTaskRunDetails.
        The type of the object.


        :return: The model_type of this UpdateTaskRunDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this UpdateTaskRunDetails.
        The type of the object.


        :param model_type: The model_type of this UpdateTaskRunDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this UpdateTaskRunDetails.
        The model version of an object.


        :return: The model_version of this UpdateTaskRunDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this UpdateTaskRunDetails.
        The model version of an object.


        :param model_version: The model_version of this UpdateTaskRunDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this UpdateTaskRunDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this UpdateTaskRunDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateTaskRunDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this UpdateTaskRunDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateTaskRunDetails.
        Detailed description for the object.


        :return: The description of this UpdateTaskRunDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateTaskRunDetails.
        Detailed description for the object.


        :param description: The description of this UpdateTaskRunDetails.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this UpdateTaskRunDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this UpdateTaskRunDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this UpdateTaskRunDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this UpdateTaskRunDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this UpdateTaskRunDetails.

        :return: The registry_metadata of this UpdateTaskRunDetails.
        :rtype: RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this UpdateTaskRunDetails.

        :param registry_metadata: The registry_metadata of this UpdateTaskRunDetails.
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
