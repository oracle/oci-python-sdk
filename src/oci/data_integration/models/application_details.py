# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationDetails(object):
    """
    The information about the application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ApplicationDetails.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this ApplicationDetails.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this ApplicationDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this ApplicationDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this ApplicationDetails.
        :type description: str

        :param application_version:
            The value to assign to the application_version property of this ApplicationDetails.
        :type application_version: int

        :param object_status:
            The value to assign to the object_status property of this ApplicationDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ApplicationDetails.
        :type identifier: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ApplicationDetails.
        :type parent_ref: ParentReference

        :param object_version:
            The value to assign to the object_version property of this ApplicationDetails.
        :type object_version: int

        :param metadata:
            The value to assign to the metadata property of this ApplicationDetails.
        :type metadata: ObjectMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'application_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'parent_ref': 'ParentReference',
            'object_version': 'int',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'application_version': 'applicationVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parent_ref': 'parentRef',
            'object_version': 'objectVersion',
            'metadata': 'metadata'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._application_version = None
        self._object_status = None
        self._identifier = None
        self._parent_ref = None
        self._object_version = None
        self._metadata = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this ApplicationDetails.
        Generated key that can be used in API calls to identify application.


        :return: The key of this ApplicationDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ApplicationDetails.
        Generated key that can be used in API calls to identify application.


        :param key: The key of this ApplicationDetails.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this ApplicationDetails.
        The type of the object.


        :return: The model_type of this ApplicationDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ApplicationDetails.
        The type of the object.


        :param model_type: The model_type of this ApplicationDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this ApplicationDetails.
        The model version of an object.


        :return: The model_version of this ApplicationDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ApplicationDetails.
        The model version of an object.


        :param model_version: The model_version of this ApplicationDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this ApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :return: The name of this ApplicationDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :param name: The name of this ApplicationDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ApplicationDetails.
        Detailed description for the object.


        :return: The description of this ApplicationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ApplicationDetails.
        Detailed description for the object.


        :param description: The description of this ApplicationDetails.
        :type: str
        """
        self._description = description

    @property
    def application_version(self):
        """
        Gets the application_version of this ApplicationDetails.
        version


        :return: The application_version of this ApplicationDetails.
        :rtype: int
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """
        Sets the application_version of this ApplicationDetails.
        version


        :param application_version: The application_version of this ApplicationDetails.
        :type: int
        """
        self._application_version = application_version

    @property
    def object_status(self):
        """
        Gets the object_status of this ApplicationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this ApplicationDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this ApplicationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this ApplicationDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this ApplicationDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :return: The identifier of this ApplicationDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ApplicationDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :param identifier: The identifier of this ApplicationDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ApplicationDetails.

        :return: The parent_ref of this ApplicationDetails.
        :rtype: ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ApplicationDetails.

        :param parent_ref: The parent_ref of this ApplicationDetails.
        :type: ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def object_version(self):
        """
        **[Required]** Gets the object_version of this ApplicationDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this ApplicationDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this ApplicationDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this ApplicationDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def metadata(self):
        """
        Gets the metadata of this ApplicationDetails.

        :return: The metadata of this ApplicationDetails.
        :rtype: ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this ApplicationDetails.

        :param metadata: The metadata of this ApplicationDetails.
        :type: ObjectMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
