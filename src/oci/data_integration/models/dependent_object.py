# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DependentObject(object):
    """
    The information about a dependent object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DependentObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DependentObject.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this DependentObject.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this DependentObject.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DependentObject.
        :type name: str

        :param description:
            The value to assign to the description property of this DependentObject.
        :type description: str

        :param application_version:
            The value to assign to the application_version property of this DependentObject.
        :type application_version: int

        :param object_status:
            The value to assign to the object_status property of this DependentObject.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DependentObject.
        :type identifier: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DependentObject.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param object_version:
            The value to assign to the object_version property of this DependentObject.
        :type object_version: int

        :param dependent_object_metadata:
            The value to assign to the dependent_object_metadata property of this DependentObject.
        :type dependent_object_metadata: list[oci.data_integration.models.PatchObjectMetadata]

        :param published_object_metadata:
            The value to assign to the published_object_metadata property of this DependentObject.
        :type published_object_metadata: dict(str, PatchObjectMetadata)

        :param source_application_info:
            The value to assign to the source_application_info property of this DependentObject.
        :type source_application_info: oci.data_integration.models.SourceApplicationInfo

        :param time_patched:
            The value to assign to the time_patched property of this DependentObject.
        :type time_patched: datetime

        :param metadata:
            The value to assign to the metadata property of this DependentObject.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this DependentObject.
        :type key_map: dict(str, str)

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
            'dependent_object_metadata': 'list[PatchObjectMetadata]',
            'published_object_metadata': 'dict(str, PatchObjectMetadata)',
            'source_application_info': 'SourceApplicationInfo',
            'time_patched': 'datetime',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
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
            'dependent_object_metadata': 'dependentObjectMetadata',
            'published_object_metadata': 'publishedObjectMetadata',
            'source_application_info': 'sourceApplicationInfo',
            'time_patched': 'timePatched',
            'metadata': 'metadata',
            'key_map': 'keyMap'
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
        self._dependent_object_metadata = None
        self._published_object_metadata = None
        self._source_application_info = None
        self._time_patched = None
        self._metadata = None
        self._key_map = None

    @property
    def key(self):
        """
        Gets the key of this DependentObject.
        Generated key that can be used in API calls to identify application.


        :return: The key of this DependentObject.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DependentObject.
        Generated key that can be used in API calls to identify application.


        :param key: The key of this DependentObject.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this DependentObject.
        The object type.


        :return: The model_type of this DependentObject.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DependentObject.
        The object type.


        :param model_type: The model_type of this DependentObject.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this DependentObject.
        The object's model version.


        :return: The model_version of this DependentObject.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DependentObject.
        The object's model version.


        :param model_version: The model_version of this DependentObject.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this DependentObject.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this DependentObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DependentObject.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this DependentObject.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DependentObject.
        Detailed description for the object.


        :return: The description of this DependentObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DependentObject.
        Detailed description for the object.


        :param description: The description of this DependentObject.
        :type: str
        """
        self._description = description

    @property
    def application_version(self):
        """
        Gets the application_version of this DependentObject.
        The application's version.


        :return: The application_version of this DependentObject.
        :rtype: int
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """
        Sets the application_version of this DependentObject.
        The application's version.


        :param application_version: The application_version of this DependentObject.
        :type: int
        """
        self._application_version = application_version

    @property
    def object_status(self):
        """
        Gets the object_status of this DependentObject.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DependentObject.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DependentObject.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DependentObject.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this DependentObject.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this DependentObject.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DependentObject.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DependentObject.
        :type: str
        """
        self._identifier = identifier

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this DependentObject.

        :return: The parent_ref of this DependentObject.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this DependentObject.

        :param parent_ref: The parent_ref of this DependentObject.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def object_version(self):
        """
        Gets the object_version of this DependentObject.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DependentObject.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DependentObject.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DependentObject.
        :type: int
        """
        self._object_version = object_version

    @property
    def dependent_object_metadata(self):
        """
        Gets the dependent_object_metadata of this DependentObject.
        A list of dependent objects in this patch.


        :return: The dependent_object_metadata of this DependentObject.
        :rtype: list[oci.data_integration.models.PatchObjectMetadata]
        """
        return self._dependent_object_metadata

    @dependent_object_metadata.setter
    def dependent_object_metadata(self, dependent_object_metadata):
        """
        Sets the dependent_object_metadata of this DependentObject.
        A list of dependent objects in this patch.


        :param dependent_object_metadata: The dependent_object_metadata of this DependentObject.
        :type: list[oci.data_integration.models.PatchObjectMetadata]
        """
        self._dependent_object_metadata = dependent_object_metadata

    @property
    def published_object_metadata(self):
        """
        Gets the published_object_metadata of this DependentObject.
        A list of objects that are published or unpublished in this patch.


        :return: The published_object_metadata of this DependentObject.
        :rtype: dict(str, PatchObjectMetadata)
        """
        return self._published_object_metadata

    @published_object_metadata.setter
    def published_object_metadata(self, published_object_metadata):
        """
        Sets the published_object_metadata of this DependentObject.
        A list of objects that are published or unpublished in this patch.


        :param published_object_metadata: The published_object_metadata of this DependentObject.
        :type: dict(str, PatchObjectMetadata)
        """
        self._published_object_metadata = published_object_metadata

    @property
    def source_application_info(self):
        """
        Gets the source_application_info of this DependentObject.

        :return: The source_application_info of this DependentObject.
        :rtype: oci.data_integration.models.SourceApplicationInfo
        """
        return self._source_application_info

    @source_application_info.setter
    def source_application_info(self, source_application_info):
        """
        Sets the source_application_info of this DependentObject.

        :param source_application_info: The source_application_info of this DependentObject.
        :type: oci.data_integration.models.SourceApplicationInfo
        """
        self._source_application_info = source_application_info

    @property
    def time_patched(self):
        """
        Gets the time_patched of this DependentObject.
        The date and time the application was patched, in the timestamp format defined by RFC3339.


        :return: The time_patched of this DependentObject.
        :rtype: datetime
        """
        return self._time_patched

    @time_patched.setter
    def time_patched(self, time_patched):
        """
        Sets the time_patched of this DependentObject.
        The date and time the application was patched, in the timestamp format defined by RFC3339.


        :param time_patched: The time_patched of this DependentObject.
        :type: datetime
        """
        self._time_patched = time_patched

    @property
    def metadata(self):
        """
        Gets the metadata of this DependentObject.

        :return: The metadata of this DependentObject.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this DependentObject.

        :param metadata: The metadata of this DependentObject.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this DependentObject.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :return: The key_map of this DependentObject.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this DependentObject.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :param key_map: The key_map of this DependentObject.
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
