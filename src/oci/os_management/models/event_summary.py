# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EventSummary(object):
    """
    Summary of the Event.
    """

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "KERNEL_OOPS"
    EVENT_TYPE_KERNEL_OOPS = "KERNEL_OOPS"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "KERNEL_CRASH"
    EVENT_TYPE_KERNEL_CRASH = "KERNEL_CRASH"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "CRASH"
    EVENT_TYPE_CRASH = "CRASH"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "EXPLOIT_ATTEMPT"
    EVENT_TYPE_EXPLOIT_ATTEMPT = "EXPLOIT_ATTEMPT"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "COMPLIANCE"
    EVENT_TYPE_COMPLIANCE = "COMPLIANCE"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "TUNING_SUGGESTION"
    EVENT_TYPE_TUNING_SUGGESTION = "TUNING_SUGGESTION"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "TUNING_APPLIED"
    EVENT_TYPE_TUNING_APPLIED = "TUNING_APPLIED"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "SECURITY"
    EVENT_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "ERROR"
    EVENT_TYPE_ERROR = "ERROR"

    #: A constant which can be used with the event_type property of a EventSummary.
    #: This constant has a value of "WARNING"
    EVENT_TYPE_WARNING = "WARNING"

    def __init__(self, **kwargs):
        """
        Initializes a new EventSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EventSummary.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this EventSummary.
        :type instance_id: str

        :param summary:
            The value to assign to the summary property of this EventSummary.
        :type summary: str

        :param event_type:
            The value to assign to the event_type property of this EventSummary.
            Allowed values for this property are: "KERNEL_OOPS", "KERNEL_CRASH", "CRASH", "EXPLOIT_ATTEMPT", "COMPLIANCE", "TUNING_SUGGESTION", "TUNING_APPLIED", "SECURITY", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type event_type: str

        :param count:
            The value to assign to the count property of this EventSummary.
        :type count: int

        :param timestamp:
            The value to assign to the timestamp property of this EventSummary.
        :type timestamp: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EventSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EventSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EventSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'instance_id': 'str',
            'summary': 'str',
            'event_type': 'str',
            'count': 'int',
            'timestamp': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'instance_id': 'instanceId',
            'summary': 'summary',
            'event_type': 'eventType',
            'count': 'count',
            'timestamp': 'timestamp',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._instance_id = None
        self._summary = None
        self._event_type = None
        self._count = None
        self._timestamp = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EventSummary.
        OCID identifier of the event


        :return: The id of this EventSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EventSummary.
        OCID identifier of the event


        :param id: The id of this EventSummary.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this EventSummary.
        Unique OCI identifier of the instance where the event occurred


        :return: The instance_id of this EventSummary.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this EventSummary.
        Unique OCI identifier of the instance where the event occurred


        :param instance_id: The instance_id of this EventSummary.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def summary(self):
        """
        Gets the summary of this EventSummary.
        human readable description of the event


        :return: The summary of this EventSummary.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this EventSummary.
        human readable description of the event


        :param summary: The summary of this EventSummary.
        :type: str
        """
        self._summary = summary

    @property
    def event_type(self):
        """
        **[Required]** Gets the event_type of this EventSummary.
        Type of the event.

        Allowed values for this property are: "KERNEL_OOPS", "KERNEL_CRASH", "CRASH", "EXPLOIT_ATTEMPT", "COMPLIANCE", "TUNING_SUGGESTION", "TUNING_APPLIED", "SECURITY", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The event_type of this EventSummary.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this EventSummary.
        Type of the event.


        :param event_type: The event_type of this EventSummary.
        :type: str
        """
        allowed_values = ["KERNEL_OOPS", "KERNEL_CRASH", "CRASH", "EXPLOIT_ATTEMPT", "COMPLIANCE", "TUNING_SUGGESTION", "TUNING_APPLIED", "SECURITY", "ERROR", "WARNING"]
        if not value_allowed_none_or_none_sentinel(event_type, allowed_values):
            event_type = 'UNKNOWN_ENUM_VALUE'
        self._event_type = event_type

    @property
    def count(self):
        """
        Gets the count of this EventSummary.
        Event occurrence count. Number of time the same event happened on the system.


        :return: The count of this EventSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this EventSummary.
        Event occurrence count. Number of time the same event happened on the system.


        :param count: The count of this EventSummary.
        :type: int
        """
        self._count = count

    @property
    def timestamp(self):
        """
        Gets the timestamp of this EventSummary.
        Time of the occurrence of the event


        :return: The timestamp of this EventSummary.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this EventSummary.
        Time of the occurrence of the event


        :param timestamp: The timestamp of this EventSummary.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EventSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EventSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EventSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EventSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EventSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EventSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EventSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EventSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this EventSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this EventSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this EventSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this EventSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
