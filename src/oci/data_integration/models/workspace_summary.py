# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkspaceSummary(object):
    """
    Summary details of a workspace.
    """

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a WorkspaceSummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkspaceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkspaceSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this WorkspaceSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this WorkspaceSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkspaceSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this WorkspaceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this WorkspaceSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WorkspaceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WorkspaceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WorkspaceSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this WorkspaceSummary.
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
        self._defined_tags = None
        self._lifecycle_state = None
        self._state_message = None

    @property
    def id(self):
        """
        Gets the id of this WorkspaceSummary.
        A system-generated and immutable identifier assigned to the workspace upon creation.


        :return: The id of this WorkspaceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkspaceSummary.
        A system-generated and immutable identifier assigned to the workspace upon creation.


        :param id: The id of this WorkspaceSummary.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this WorkspaceSummary.
        A user defined description for the workspace.


        :return: The description of this WorkspaceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkspaceSummary.
        A user defined description for the workspace.


        :param description: The description of this WorkspaceSummary.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this WorkspaceSummary.
        A user-friendly display name that is changeable. Avoid entering confidential information.


        :return: The display_name of this WorkspaceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WorkspaceSummary.
        A user-friendly display name that is changeable. Avoid entering confidential information.


        :param display_name: The display_name of this WorkspaceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this WorkspaceSummary.
        The OCID of the compartment that contains the workspace.


        :return: The compartment_id of this WorkspaceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkspaceSummary.
        The OCID of the compartment that contains the workspace.


        :param compartment_id: The compartment_id of this WorkspaceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this WorkspaceSummary.
        The date and time the workspace was created, in the timestamp format defined by RFC3339.


        :return: The time_created of this WorkspaceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WorkspaceSummary.
        The date and time the workspace was created, in the timestamp format defined by RFC3339.


        :param time_created: The time_created of this WorkspaceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this WorkspaceSummary.
        The date and time the workspace was updated, in the timestamp format defined by RFC3339.


        :return: The time_updated of this WorkspaceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this WorkspaceSummary.
        The date and time the workspace was updated, in the timestamp format defined by RFC3339.


        :param time_updated: The time_updated of this WorkspaceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this WorkspaceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this WorkspaceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this WorkspaceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this WorkspaceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this WorkspaceSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this WorkspaceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this WorkspaceSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this WorkspaceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this WorkspaceSummary.
        The current state of the workspace.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this WorkspaceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this WorkspaceSummary.
        The current state of the workspace.


        :param lifecycle_state: The lifecycle_state of this WorkspaceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this WorkspaceSummary.
        A detailed description about the current state of the workspace. Used to provide actionable information if the workspace is in a failed state.


        :return: The state_message of this WorkspaceSummary.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this WorkspaceSummary.
        A detailed description about the current state of the workspace. Used to provide actionable information if the workspace is in a failed state.


        :param state_message: The state_message of this WorkspaceSummary.
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
