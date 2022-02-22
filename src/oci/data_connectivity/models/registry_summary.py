# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RegistrySummary(object):
    """
    Summary of a Registry.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RegistrySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RegistrySummary.
        :type id: str

        :param description:
            The value to assign to the description property of this RegistrySummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this RegistrySummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RegistrySummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this RegistrySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RegistrySummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RegistrySummary.
        :type freeform_tags: dict(str, str)

        :param updated_by:
            The value to assign to the updated_by property of this RegistrySummary.
        :type updated_by: str

        :param defined_tags:
            The value to assign to the defined_tags property of this RegistrySummary.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RegistrySummary.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this RegistrySummary.
        :type state_message: str

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'updated_by': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'state_message': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'updated_by': 'updatedBy',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState',
            'state_message': 'stateMessage'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._updated_by = None
        self._defined_tags = None
        self._lifecycle_state = None
        self._state_message = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RegistrySummary.
        Unique identifier that is immutable on creation


        :return: The id of this RegistrySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RegistrySummary.
        Unique identifier that is immutable on creation


        :param id: The id of this RegistrySummary.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this RegistrySummary.
        Registry description


        :return: The description of this RegistrySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RegistrySummary.
        Registry description


        :param description: The description of this RegistrySummary.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RegistrySummary.
        Data Connectivity Management Registry display name, registries can be renamed


        :return: The display_name of this RegistrySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RegistrySummary.
        Data Connectivity Management Registry display name, registries can be renamed


        :param display_name: The display_name of this RegistrySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this RegistrySummary.
        Compartment Identifier


        :return: The compartment_id of this RegistrySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RegistrySummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this RegistrySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this RegistrySummary.
        The time the Data Connectivity Management Registry was created. An RFC3339 formatted datetime string


        :return: The time_created of this RegistrySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RegistrySummary.
        The time the Data Connectivity Management Registry was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this RegistrySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RegistrySummary.
        The time the Data Connectivity Management Registry was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this RegistrySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RegistrySummary.
        The time the Data Connectivity Management Registry was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this RegistrySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RegistrySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this RegistrySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RegistrySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this RegistrySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def updated_by(self):
        """
        Gets the updated_by of this RegistrySummary.
        Name of the user who updated the DCMS Registry.


        :return: The updated_by of this RegistrySummary.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this RegistrySummary.
        Name of the user who updated the DCMS Registry.


        :param updated_by: The updated_by of this RegistrySummary.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RegistrySummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this RegistrySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RegistrySummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this RegistrySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this RegistrySummary.
        The current state of the registry.


        :return: The lifecycle_state of this RegistrySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RegistrySummary.
        The current state of the registry.


        :param lifecycle_state: The lifecycle_state of this RegistrySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this RegistrySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this RegistrySummary.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this RegistrySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this RegistrySummary.
        :type: str
        """
        self._state_message = state_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
