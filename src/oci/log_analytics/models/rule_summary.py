# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleSummary(object):
    """
    A generic rule summary object - represents an ingest time rule or a scheduled task.
    """

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the kind property of a RuleSummary.
    #: This constant has a value of "INGEST_TIME"
    KIND_INGEST_TIME = "INGEST_TIME"

    #: A constant which can be used with the kind property of a RuleSummary.
    #: This constant has a value of "SAVED_SEARCH"
    KIND_SAVED_SEARCH = "SAVED_SEARCH"

    #: A constant which can be used with the last_execution_status property of a RuleSummary.
    #: This constant has a value of "FAILED"
    LAST_EXECUTION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the last_execution_status property of a RuleSummary.
    #: This constant has a value of "SUCCEEDED"
    LAST_EXECUTION_STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new RuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RuleSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this RuleSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RuleSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this RuleSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RuleSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RuleSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RuleSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RuleSummary.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param kind:
            The value to assign to the kind property of this RuleSummary.
            Allowed values for this property are: "INGEST_TIME", "SAVED_SEARCH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param display_name:
            The value to assign to the display_name property of this RuleSummary.
        :type display_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this RuleSummary.
        :type is_enabled: bool

        :param last_execution_status:
            The value to assign to the last_execution_status property of this RuleSummary.
            Allowed values for this property are: "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_execution_status: str

        :param time_last_executed:
            The value to assign to the time_last_executed property of this RuleSummary.
        :type time_last_executed: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'kind': 'str',
            'display_name': 'str',
            'is_enabled': 'bool',
            'last_execution_status': 'str',
            'time_last_executed': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState',
            'kind': 'kind',
            'display_name': 'displayName',
            'is_enabled': 'isEnabled',
            'last_execution_status': 'lastExecutionStatus',
            'time_last_executed': 'timeLastExecuted'
        }

        self._id = None
        self._description = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_state = None
        self._kind = None
        self._display_name = None
        self._is_enabled = None
        self._last_execution_status = None
        self._time_last_executed = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RuleSummary.
        The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
        a resource that is provisioned and managed by the customer on their premises or on the cloud.


        :return: The id of this RuleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RuleSummary.
        The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
        a resource that is provisioned and managed by the customer on their premises or on the cloud.


        :param id: The id of this RuleSummary.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this RuleSummary.
        Description for this resource.


        :return: The description of this RuleSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RuleSummary.
        Description for this resource.


        :param description: The description of this RuleSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RuleSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this RuleSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RuleSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this RuleSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this RuleSummary.
        The date and time the resource was created, in the format defined by RFC3339.


        :return: The time_created of this RuleSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RuleSummary.
        The date and time the resource was created, in the format defined by RFC3339.


        :param time_created: The time_created of this RuleSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RuleSummary.
        The date and time the resource was last updated, in the format defined by RFC3339.


        :return: The time_updated of this RuleSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RuleSummary.
        The date and time the resource was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this RuleSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RuleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this RuleSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RuleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this RuleSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RuleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this RuleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RuleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this RuleSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this RuleSummary.
        The current state of the logging analytics rule.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RuleSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RuleSummary.
        The current state of the logging analytics rule.


        :param lifecycle_state: The lifecycle_state of this RuleSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this RuleSummary.
        The kind of rule - either an ingest time rule or a scheduled task.

        Allowed values for this property are: "INGEST_TIME", "SAVED_SEARCH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The kind of this RuleSummary.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this RuleSummary.
        The kind of rule - either an ingest time rule or a scheduled task.


        :param kind: The kind of this RuleSummary.
        :type: str
        """
        allowed_values = ["INGEST_TIME", "SAVED_SEARCH"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            kind = 'UNKNOWN_ENUM_VALUE'
        self._kind = kind

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RuleSummary.
        The ingest time rule or scheduled task display name.


        :return: The display_name of this RuleSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RuleSummary.
        The ingest time rule or scheduled task display name.


        :param display_name: The display_name of this RuleSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this RuleSummary.
        A flag indicating whether or not the ingest time rule or scheduled task is enabled.


        :return: The is_enabled of this RuleSummary.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this RuleSummary.
        A flag indicating whether or not the ingest time rule or scheduled task is enabled.


        :param is_enabled: The is_enabled of this RuleSummary.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def last_execution_status(self):
        """
        Gets the last_execution_status of this RuleSummary.
        The most recent task execution status.

        Allowed values for this property are: "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_execution_status of this RuleSummary.
        :rtype: str
        """
        return self._last_execution_status

    @last_execution_status.setter
    def last_execution_status(self, last_execution_status):
        """
        Sets the last_execution_status of this RuleSummary.
        The most recent task execution status.


        :param last_execution_status: The last_execution_status of this RuleSummary.
        :type: str
        """
        allowed_values = ["FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(last_execution_status, allowed_values):
            last_execution_status = 'UNKNOWN_ENUM_VALUE'
        self._last_execution_status = last_execution_status

    @property
    def time_last_executed(self):
        """
        Gets the time_last_executed of this RuleSummary.
        The date and time the scheduled task last executed, in the format defined by RFC3339.


        :return: The time_last_executed of this RuleSummary.
        :rtype: datetime
        """
        return self._time_last_executed

    @time_last_executed.setter
    def time_last_executed(self, time_last_executed):
        """
        Sets the time_last_executed of this RuleSummary.
        The date and time the scheduled task last executed, in the format defined by RFC3339.


        :param time_last_executed: The time_last_executed of this RuleSummary.
        :type: datetime
        """
        self._time_last_executed = time_last_executed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
