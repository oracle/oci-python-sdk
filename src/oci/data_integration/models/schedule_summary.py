# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleSummary(object):
    """
    The schedule summary information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ScheduleSummary.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ScheduleSummary.
        :type model_version: str

        :param model_type:
            The value to assign to the model_type property of this ScheduleSummary.
        :type model_type: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ScheduleSummary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this ScheduleSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this ScheduleSummary.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this ScheduleSummary.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this ScheduleSummary.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ScheduleSummary.
        :type identifier: str

        :param frequency_details:
            The value to assign to the frequency_details property of this ScheduleSummary.
        :type frequency_details: oci.data_integration.models.AbstractFrequencyDetails

        :param timezone:
            The value to assign to the timezone property of this ScheduleSummary.
        :type timezone: str

        :param is_daylight_adjustment_enabled:
            The value to assign to the is_daylight_adjustment_enabled property of this ScheduleSummary.
        :type is_daylight_adjustment_enabled: bool

        :param metadata:
            The value to assign to the metadata property of this ScheduleSummary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'model_type': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'frequency_details': 'AbstractFrequencyDetails',
            'timezone': 'str',
            'is_daylight_adjustment_enabled': 'bool',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'model_type': 'modelType',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'frequency_details': 'frequencyDetails',
            'timezone': 'timezone',
            'is_daylight_adjustment_enabled': 'isDaylightAdjustmentEnabled',
            'metadata': 'metadata'
        }

        self._key = None
        self._model_version = None
        self._model_type = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._frequency_details = None
        self._timezone = None
        self._is_daylight_adjustment_enabled = None
        self._metadata = None

    @property
    def key(self):
        """
        Gets the key of this ScheduleSummary.
        Generated key that can be used in API calls to identify schedule. On scenarios where reference to the schedule is needed, a value can be passed in create.


        :return: The key of this ScheduleSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ScheduleSummary.
        Generated key that can be used in API calls to identify schedule. On scenarios where reference to the schedule is needed, a value can be passed in create.


        :param key: The key of this ScheduleSummary.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this ScheduleSummary.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :return: The model_version of this ScheduleSummary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ScheduleSummary.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :param model_version: The model_version of this ScheduleSummary.
        :type: str
        """
        self._model_version = model_version

    @property
    def model_type(self):
        """
        Gets the model_type of this ScheduleSummary.
        The type of the object.


        :return: The model_type of this ScheduleSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ScheduleSummary.
        The type of the object.


        :param model_type: The model_type of this ScheduleSummary.
        :type: str
        """
        self._model_type = model_type

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ScheduleSummary.

        :return: The parent_ref of this ScheduleSummary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ScheduleSummary.

        :param parent_ref: The parent_ref of this ScheduleSummary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this ScheduleSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this ScheduleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ScheduleSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this ScheduleSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ScheduleSummary.
        Detailed description for the object.


        :return: The description of this ScheduleSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScheduleSummary.
        Detailed description for the object.


        :param description: The description of this ScheduleSummary.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this ScheduleSummary.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :return: The object_version of this ScheduleSummary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this ScheduleSummary.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :param object_version: The object_version of this ScheduleSummary.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this ScheduleSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this ScheduleSummary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this ScheduleSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this ScheduleSummary.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this ScheduleSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this ScheduleSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ScheduleSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this ScheduleSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def frequency_details(self):
        """
        Gets the frequency_details of this ScheduleSummary.

        :return: The frequency_details of this ScheduleSummary.
        :rtype: oci.data_integration.models.AbstractFrequencyDetails
        """
        return self._frequency_details

    @frequency_details.setter
    def frequency_details(self, frequency_details):
        """
        Sets the frequency_details of this ScheduleSummary.

        :param frequency_details: The frequency_details of this ScheduleSummary.
        :type: oci.data_integration.models.AbstractFrequencyDetails
        """
        self._frequency_details = frequency_details

    @property
    def timezone(self):
        """
        Gets the timezone of this ScheduleSummary.
        The timezone for the schedule.


        :return: The timezone of this ScheduleSummary.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ScheduleSummary.
        The timezone for the schedule.


        :param timezone: The timezone of this ScheduleSummary.
        :type: str
        """
        self._timezone = timezone

    @property
    def is_daylight_adjustment_enabled(self):
        """
        Gets the is_daylight_adjustment_enabled of this ScheduleSummary.
        A flag to indicate whether daylight adjustment should be considered or not.


        :return: The is_daylight_adjustment_enabled of this ScheduleSummary.
        :rtype: bool
        """
        return self._is_daylight_adjustment_enabled

    @is_daylight_adjustment_enabled.setter
    def is_daylight_adjustment_enabled(self, is_daylight_adjustment_enabled):
        """
        Sets the is_daylight_adjustment_enabled of this ScheduleSummary.
        A flag to indicate whether daylight adjustment should be considered or not.


        :param is_daylight_adjustment_enabled: The is_daylight_adjustment_enabled of this ScheduleSummary.
        :type: bool
        """
        self._is_daylight_adjustment_enabled = is_daylight_adjustment_enabled

    @property
    def metadata(self):
        """
        Gets the metadata of this ScheduleSummary.

        :return: The metadata of this ScheduleSummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this ScheduleSummary.

        :param metadata: The metadata of this ScheduleSummary.
        :type: oci.data_integration.models.ObjectMetadata
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
