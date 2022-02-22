# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Registry(object):
    """
    A registry is an organizational construct to keep multiple data Connectivity Management solutions and their resources (data assets, data flows, tasks, and so on) separate from each other, helping you to stay organized. For example, you could have separate registries for development, testing, and production.
    """

    #: A constant which can be used with the lifecycle_state property of a Registry.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Registry.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Registry.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Registry.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Registry.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Registry.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Registry.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Registry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Registry.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Registry.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this Registry.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this Registry.
        :type display_name: str

        :param updated_by:
            The value to assign to the updated_by property of this Registry.
        :type updated_by: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Registry.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this Registry.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Registry.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Registry.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this Registry.
        :type state_message: str

        :param id:
            The value to assign to the id property of this Registry.
        :type id: str

        """
        self.swagger_types = {
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str',
            'updated_by': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'state_message': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName',
            'updated_by': 'updatedBy',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'state_message': 'stateMessage',
            'id': 'id'
        }

        self._freeform_tags = None
        self._defined_tags = None
        self._description = None
        self._display_name = None
        self._updated_by = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._state_message = None
        self._id = None

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Registry.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Registry.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Registry.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Registry.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Registry.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Registry.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Registry.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Registry.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this Registry.
        Registry description


        :return: The description of this Registry.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Registry.
        Registry description


        :param description: The description of this Registry.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Registry.
        Data Connectivity Management Registry display name, registries can be renamed


        :return: The display_name of this Registry.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Registry.
        Data Connectivity Management Registry display name, registries can be renamed


        :param display_name: The display_name of this Registry.
        :type: str
        """
        self._display_name = display_name

    @property
    def updated_by(self):
        """
        Gets the updated_by of this Registry.
        Name of the user who updated the DCMS Registry.


        :return: The updated_by of this Registry.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this Registry.
        Name of the user who updated the DCMS Registry.


        :param updated_by: The updated_by of this Registry.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Registry.
        Compartment Identifier


        :return: The compartment_id of this Registry.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Registry.
        Compartment Identifier


        :param compartment_id: The compartment_id of this Registry.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Registry.
        The time the Data Connectivity Management Registry was created. An RFC3339 formatted datetime string


        :return: The time_created of this Registry.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Registry.
        The time the Data Connectivity Management Registry was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this Registry.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Registry.
        The time the Data Connectivity Management Registry was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this Registry.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Registry.
        The time the Data Connectivity Management Registry was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this Registry.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Registry.
        Lifecycle states for registries in Data Connectivity Management Service
        CREATING - The resource is being created and may not be usable until the entire metadata is defined
        UPDATING - The resource is being updated and may not be usable until all changes are commited
        DELETING - The resource is being deleted and might require deep cleanup of children.
        ACTIVE   - The resource is valid and available for access
        INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                 administrative reasons
        DELETED  - The resource has been deleted and isn't available
        FAILED   - The resource is in a failed state due to validation or other errors

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Registry.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Registry.
        Lifecycle states for registries in Data Connectivity Management Service
        CREATING - The resource is being created and may not be usable until the entire metadata is defined
        UPDATING - The resource is being updated and may not be usable until all changes are commited
        DELETING - The resource is being deleted and might require deep cleanup of children.
        ACTIVE   - The resource is valid and available for access
        INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                 administrative reasons
        DELETED  - The resource has been deleted and isn't available
        FAILED   - The resource is in a failed state due to validation or other errors


        :param lifecycle_state: The lifecycle_state of this Registry.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this Registry.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this Registry.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this Registry.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this Registry.
        :type: str
        """
        self._state_message = state_message

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Registry.
        Unique identifier that is immutable on creation


        :return: The id of this Registry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Registry.
        Unique identifier that is immutable on creation


        :param id: The id of this Registry.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
