# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Event(object):
    """
    Description of Event.
    """

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "KERNEL_OOPS"
    EVENT_TYPE_KERNEL_OOPS = "KERNEL_OOPS"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "KERNEL_CRASH"
    EVENT_TYPE_KERNEL_CRASH = "KERNEL_CRASH"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "CRASH"
    EVENT_TYPE_CRASH = "CRASH"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "EXPLOIT_ATTEMPT"
    EVENT_TYPE_EXPLOIT_ATTEMPT = "EXPLOIT_ATTEMPT"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "COMPLIANCE"
    EVENT_TYPE_COMPLIANCE = "COMPLIANCE"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "TUNING_SUGGESTION"
    EVENT_TYPE_TUNING_SUGGESTION = "TUNING_SUGGESTION"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "TUNING_APPLIED"
    EVENT_TYPE_TUNING_APPLIED = "TUNING_APPLIED"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "SECURITY"
    EVENT_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "ERROR"
    EVENT_TYPE_ERROR = "ERROR"

    #: A constant which can be used with the event_type property of a Event.
    #: This constant has a value of "WARNING"
    EVENT_TYPE_WARNING = "WARNING"

    def __init__(self, **kwargs):
        """
        Initializes a new Event object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.os_management.models.KernelOopsEvent`
        * :class:`~oci.os_management.models.KernelCrashEvent`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Event.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this Event.
        :type instance_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Event.
        :type compartment_id: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this Event.
        :type tenancy_id: str

        :param summary:
            The value to assign to the summary property of this Event.
        :type summary: str

        :param timestamp:
            The value to assign to the timestamp property of this Event.
        :type timestamp: datetime

        :param event_fingerprint:
            The value to assign to the event_fingerprint property of this Event.
        :type event_fingerprint: str

        :param count:
            The value to assign to the count property of this Event.
        :type count: int

        :param event_type:
            The value to assign to the event_type property of this Event.
            Allowed values for this property are: "KERNEL_OOPS", "KERNEL_CRASH", "CRASH", "EXPLOIT_ATTEMPT", "COMPLIANCE", "TUNING_SUGGESTION", "TUNING_APPLIED", "SECURITY", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type event_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Event.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Event.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Event.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'instance_id': 'str',
            'compartment_id': 'str',
            'tenancy_id': 'str',
            'summary': 'str',
            'timestamp': 'datetime',
            'event_fingerprint': 'str',
            'count': 'int',
            'event_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'instance_id': 'instanceId',
            'compartment_id': 'compartmentId',
            'tenancy_id': 'tenancyId',
            'summary': 'summary',
            'timestamp': 'timestamp',
            'event_fingerprint': 'eventFingerprint',
            'count': 'count',
            'event_type': 'eventType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._instance_id = None
        self._compartment_id = None
        self._tenancy_id = None
        self._summary = None
        self._timestamp = None
        self._event_fingerprint = None
        self._count = None
        self._event_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['eventType']

        if type == 'KERNEL_OOPS':
            return 'KernelOopsEvent'

        if type == 'KERNEL_CRASH':
            return 'KernelCrashEvent'
        else:
            return 'Event'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Event.
        OCID identifier of the event


        :return: The id of this Event.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Event.
        OCID identifier of the event


        :param id: The id of this Event.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        Gets the instance_id of this Event.
        OCI identifier of the instance where the event occurred


        :return: The instance_id of this Event.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this Event.
        OCI identifier of the instance where the event occurred


        :param instance_id: The instance_id of this Event.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Event.
        OCI identifier of the compartement where the instance is


        :return: The compartment_id of this Event.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Event.
        OCI identifier of the compartement where the instance is


        :param compartment_id: The compartment_id of this Event.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this Event.
        OCID identifier of the instance tenancy.


        :return: The tenancy_id of this Event.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this Event.
        OCID identifier of the instance tenancy.


        :param tenancy_id: The tenancy_id of this Event.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def summary(self):
        """
        Gets the summary of this Event.
        human readable description of the event


        :return: The summary of this Event.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this Event.
        human readable description of the event


        :param summary: The summary of this Event.
        :type: str
        """
        self._summary = summary

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Event.
        Time of the occurrence of the event


        :return: The timestamp of this Event.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Event.
        Time of the occurrence of the event


        :param timestamp: The timestamp of this Event.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def event_fingerprint(self):
        """
        Gets the event_fingerprint of this Event.
        Unique ID used to group event with the same characteristics together.
        The list of such groups of event can be retrieved via /recurringEvents/{EventFingerprint}


        :return: The event_fingerprint of this Event.
        :rtype: str
        """
        return self._event_fingerprint

    @event_fingerprint.setter
    def event_fingerprint(self, event_fingerprint):
        """
        Sets the event_fingerprint of this Event.
        Unique ID used to group event with the same characteristics together.
        The list of such groups of event can be retrieved via /recurringEvents/{EventFingerprint}


        :param event_fingerprint: The event_fingerprint of this Event.
        :type: str
        """
        self._event_fingerprint = event_fingerprint

    @property
    def count(self):
        """
        Gets the count of this Event.
        Event occurrence count. Number of time the event has happen on the system.


        :return: The count of this Event.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this Event.
        Event occurrence count. Number of time the event has happen on the system.


        :param count: The count of this Event.
        :type: int
        """
        self._count = count

    @property
    def event_type(self):
        """
        **[Required]** Gets the event_type of this Event.
        Type of the Event.

        Allowed values for this property are: "KERNEL_OOPS", "KERNEL_CRASH", "CRASH", "EXPLOIT_ATTEMPT", "COMPLIANCE", "TUNING_SUGGESTION", "TUNING_APPLIED", "SECURITY", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The event_type of this Event.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this Event.
        Type of the Event.


        :param event_type: The event_type of this Event.
        :type: str
        """
        allowed_values = ["KERNEL_OOPS", "KERNEL_CRASH", "CRASH", "EXPLOIT_ATTEMPT", "COMPLIANCE", "TUNING_SUGGESTION", "TUNING_APPLIED", "SECURITY", "ERROR", "WARNING"]
        if not value_allowed_none_or_none_sentinel(event_type, allowed_values):
            event_type = 'UNKNOWN_ENUM_VALUE'
        self._event_type = event_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Event.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Event.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Event.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Event.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Event.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Event.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Event.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Event.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Event.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Event.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Event.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Event.
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
