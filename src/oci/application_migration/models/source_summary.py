# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceSummary(object):
    """
    The Source object. Sources represent external locations from which
    applications may be imported into an OCI tenancy.
    """

    #: A constant which can be used with the type property of a SourceSummary.
    #: This constant has a value of "OCIC"
    TYPE_OCIC = "OCIC"

    #: A constant which can be used with the type property of a SourceSummary.
    #: This constant has a value of "INTERNAL_COMPUTE"
    TYPE_INTERNAL_COMPUTE = "INTERNAL_COMPUTE"

    def __init__(self, **kwargs):
        """
        Initializes a new SourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SourceSummary.
        :type id: str

        :param type:
            The value to assign to the type property of this SourceSummary.
            Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SourceSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SourceSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SourceSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this SourceSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SourceSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SourceSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._type = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this SourceSummary.
        Unique identifier (OCID) for the source


        :return: The id of this SourceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SourceSummary.
        Unique identifier (OCID) for the source


        :param id: The id of this SourceSummary.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        Gets the type of this SourceSummary.
        The type of source environment

        Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this SourceSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SourceSummary.
        The type of source environment


        :param type: The type of this SourceSummary.
        :type: str
        """
        allowed_values = ["OCIC", "INTERNAL_COMPUTE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this SourceSummary.
        Unique idenfifier (OCID) for the compartment where the Source is located.


        :return: The compartment_id of this SourceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SourceSummary.
        Unique idenfifier (OCID) for the compartment where the Source is located.


        :param compartment_id: The compartment_id of this SourceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this SourceSummary.
        Human-readable name of the source.


        :return: The display_name of this SourceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SourceSummary.
        Human-readable name of the source.


        :param display_name: The display_name of this SourceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SourceSummary.
        Description of the source.


        :return: The description of this SourceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SourceSummary.
        Description of the source.


        :param description: The description of this SourceSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this SourceSummary.
        The date and time at which the source was created.


        :return: The time_created of this SourceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SourceSummary.
        The date and time at which the source was created.


        :param time_created: The time_created of this SourceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SourceSummary.
        The current state of the Source


        :return: The lifecycle_state of this SourceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SourceSummary.
        The current state of the Source


        :param lifecycle_state: The lifecycle_state of this SourceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SourceSummary.
        Details about the current lifecycle state


        :return: The lifecycle_details of this SourceSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SourceSummary.
        Details about the current lifecycle state


        :param lifecycle_details: The lifecycle_details of this SourceSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this SourceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this SourceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this SourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this SourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
