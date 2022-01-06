# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Patch(object):
    """
    The patch object contains the audit summary information and the definition of the patch.
    """

    #: A constant which can be used with the patch_type property of a Patch.
    #: This constant has a value of "PUBLISH"
    PATCH_TYPE_PUBLISH = "PUBLISH"

    #: A constant which can be used with the patch_type property of a Patch.
    #: This constant has a value of "REFRESH"
    PATCH_TYPE_REFRESH = "REFRESH"

    #: A constant which can be used with the patch_type property of a Patch.
    #: This constant has a value of "UNPUBLISH"
    PATCH_TYPE_UNPUBLISH = "UNPUBLISH"

    #: A constant which can be used with the patch_status property of a Patch.
    #: This constant has a value of "QUEUED"
    PATCH_STATUS_QUEUED = "QUEUED"

    #: A constant which can be used with the patch_status property of a Patch.
    #: This constant has a value of "SUCCESSFUL"
    PATCH_STATUS_SUCCESSFUL = "SUCCESSFUL"

    #: A constant which can be used with the patch_status property of a Patch.
    #: This constant has a value of "FAILED"
    PATCH_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the patch_status property of a Patch.
    #: This constant has a value of "IN_PROGRESS"
    PATCH_STATUS_IN_PROGRESS = "IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new Patch object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Patch.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this Patch.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this Patch.
        :type model_version: str

        :param name:
            The value to assign to the name property of this Patch.
        :type name: str

        :param description:
            The value to assign to the description property of this Patch.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Patch.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this Patch.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Patch.
        :type identifier: str

        :param time_patched:
            The value to assign to the time_patched property of this Patch.
        :type time_patched: datetime

        :param error_messages:
            The value to assign to the error_messages property of this Patch.
        :type error_messages: dict(str, str)

        :param application_version:
            The value to assign to the application_version property of this Patch.
        :type application_version: int

        :param patch_type:
            The value to assign to the patch_type property of this Patch.
            Allowed values for this property are: "PUBLISH", "REFRESH", "UNPUBLISH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type patch_type: str

        :param patch_status:
            The value to assign to the patch_status property of this Patch.
            Allowed values for this property are: "QUEUED", "SUCCESSFUL", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type patch_status: str

        :param dependent_object_metadata:
            The value to assign to the dependent_object_metadata property of this Patch.
        :type dependent_object_metadata: list[oci.data_integration.models.PatchObjectMetadata]

        :param patch_object_metadata:
            The value to assign to the patch_object_metadata property of this Patch.
        :type patch_object_metadata: list[oci.data_integration.models.PatchObjectMetadata]

        :param parent_ref:
            The value to assign to the parent_ref property of this Patch.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this Patch.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this Patch.
        :type key_map: dict(str, str)

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'time_patched': 'datetime',
            'error_messages': 'dict(str, str)',
            'application_version': 'int',
            'patch_type': 'str',
            'patch_status': 'str',
            'dependent_object_metadata': 'list[PatchObjectMetadata]',
            'patch_object_metadata': 'list[PatchObjectMetadata]',
            'parent_ref': 'ParentReference',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'time_patched': 'timePatched',
            'error_messages': 'errorMessages',
            'application_version': 'applicationVersion',
            'patch_type': 'patchType',
            'patch_status': 'patchStatus',
            'dependent_object_metadata': 'dependentObjectMetadata',
            'patch_object_metadata': 'patchObjectMetadata',
            'parent_ref': 'parentRef',
            'metadata': 'metadata',
            'key_map': 'keyMap'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._time_patched = None
        self._error_messages = None
        self._application_version = None
        self._patch_type = None
        self._patch_status = None
        self._dependent_object_metadata = None
        self._patch_object_metadata = None
        self._parent_ref = None
        self._metadata = None
        self._key_map = None

    @property
    def key(self):
        """
        Gets the key of this Patch.
        The object key.


        :return: The key of this Patch.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Patch.
        The object key.


        :param key: The key of this Patch.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this Patch.
        The object type.


        :return: The model_type of this Patch.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Patch.
        The object type.


        :param model_type: The model_type of this Patch.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this Patch.
        The object's model version.


        :return: The model_version of this Patch.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Patch.
        The object's model version.


        :param model_version: The model_version of this Patch.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this Patch.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this Patch.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Patch.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this Patch.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Patch.
        Detailed description for the object.


        :return: The description of this Patch.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Patch.
        Detailed description for the object.


        :param description: The description of this Patch.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this Patch.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this Patch.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this Patch.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this Patch.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this Patch.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this Patch.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this Patch.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this Patch.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this Patch.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this Patch.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Patch.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this Patch.
        :type: str
        """
        self._identifier = identifier

    @property
    def time_patched(self):
        """
        Gets the time_patched of this Patch.
        The date and time the patch was applied, in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_patched of this Patch.
        :rtype: datetime
        """
        return self._time_patched

    @time_patched.setter
    def time_patched(self, time_patched):
        """
        Sets the time_patched of this Patch.
        The date and time the patch was applied, in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_patched: The time_patched of this Patch.
        :type: datetime
        """
        self._time_patched = time_patched

    @property
    def error_messages(self):
        """
        Gets the error_messages of this Patch.
        The errors encountered while applying the patch, if any.


        :return: The error_messages of this Patch.
        :rtype: dict(str, str)
        """
        return self._error_messages

    @error_messages.setter
    def error_messages(self, error_messages):
        """
        Sets the error_messages of this Patch.
        The errors encountered while applying the patch, if any.


        :param error_messages: The error_messages of this Patch.
        :type: dict(str, str)
        """
        self._error_messages = error_messages

    @property
    def application_version(self):
        """
        Gets the application_version of this Patch.
        The application version of the patch.


        :return: The application_version of this Patch.
        :rtype: int
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """
        Sets the application_version of this Patch.
        The application version of the patch.


        :param application_version: The application_version of this Patch.
        :type: int
        """
        self._application_version = application_version

    @property
    def patch_type(self):
        """
        Gets the patch_type of this Patch.
        The type of the patch applied or being applied on the application.

        Allowed values for this property are: "PUBLISH", "REFRESH", "UNPUBLISH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The patch_type of this Patch.
        :rtype: str
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """
        Sets the patch_type of this Patch.
        The type of the patch applied or being applied on the application.


        :param patch_type: The patch_type of this Patch.
        :type: str
        """
        allowed_values = ["PUBLISH", "REFRESH", "UNPUBLISH"]
        if not value_allowed_none_or_none_sentinel(patch_type, allowed_values):
            patch_type = 'UNKNOWN_ENUM_VALUE'
        self._patch_type = patch_type

    @property
    def patch_status(self):
        """
        Gets the patch_status of this Patch.
        Status of the patch applied or being applied on the application

        Allowed values for this property are: "QUEUED", "SUCCESSFUL", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The patch_status of this Patch.
        :rtype: str
        """
        return self._patch_status

    @patch_status.setter
    def patch_status(self, patch_status):
        """
        Sets the patch_status of this Patch.
        Status of the patch applied or being applied on the application


        :param patch_status: The patch_status of this Patch.
        :type: str
        """
        allowed_values = ["QUEUED", "SUCCESSFUL", "FAILED", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(patch_status, allowed_values):
            patch_status = 'UNKNOWN_ENUM_VALUE'
        self._patch_status = patch_status

    @property
    def dependent_object_metadata(self):
        """
        Gets the dependent_object_metadata of this Patch.
        List of dependent objects in this patch.


        :return: The dependent_object_metadata of this Patch.
        :rtype: list[oci.data_integration.models.PatchObjectMetadata]
        """
        return self._dependent_object_metadata

    @dependent_object_metadata.setter
    def dependent_object_metadata(self, dependent_object_metadata):
        """
        Sets the dependent_object_metadata of this Patch.
        List of dependent objects in this patch.


        :param dependent_object_metadata: The dependent_object_metadata of this Patch.
        :type: list[oci.data_integration.models.PatchObjectMetadata]
        """
        self._dependent_object_metadata = dependent_object_metadata

    @property
    def patch_object_metadata(self):
        """
        Gets the patch_object_metadata of this Patch.
        List of objects that are published or unpublished in this patch.


        :return: The patch_object_metadata of this Patch.
        :rtype: list[oci.data_integration.models.PatchObjectMetadata]
        """
        return self._patch_object_metadata

    @patch_object_metadata.setter
    def patch_object_metadata(self, patch_object_metadata):
        """
        Sets the patch_object_metadata of this Patch.
        List of objects that are published or unpublished in this patch.


        :param patch_object_metadata: The patch_object_metadata of this Patch.
        :type: list[oci.data_integration.models.PatchObjectMetadata]
        """
        self._patch_object_metadata = patch_object_metadata

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this Patch.

        :return: The parent_ref of this Patch.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this Patch.

        :param parent_ref: The parent_ref of this Patch.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def metadata(self):
        """
        Gets the metadata of this Patch.

        :return: The metadata of this Patch.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Patch.

        :param metadata: The metadata of this Patch.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this Patch.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :return: The key_map of this Patch.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this Patch.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :param key_map: The key_map of this Patch.
        :type: dict(str, str)
        """
        self._key_map = key_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
