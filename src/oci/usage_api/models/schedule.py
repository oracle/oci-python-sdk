# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Schedule(object):
    """
    The schedule.
    """

    #: A constant which can be used with the lifecycle_state property of a Schedule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Schedule.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new Schedule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Schedule.
        :type id: str

        :param name:
            The value to assign to the name property of this Schedule.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Schedule.
        :type compartment_id: str

        :param result_location:
            The value to assign to the result_location property of this Schedule.
        :type result_location: oci.usage_api.models.ResultLocation

        :param schedule_recurrences:
            The value to assign to the schedule_recurrences property of this Schedule.
        :type schedule_recurrences: str

        :param time_scheduled:
            The value to assign to the time_scheduled property of this Schedule.
        :type time_scheduled: datetime

        :param query_properties:
            The value to assign to the query_properties property of this Schedule.
        :type query_properties: oci.usage_api.models.QueryProperties

        :param time_created:
            The value to assign to the time_created property of this Schedule.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Schedule.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Schedule.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Schedule.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Schedule.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'result_location': 'ResultLocation',
            'schedule_recurrences': 'str',
            'time_scheduled': 'datetime',
            'query_properties': 'QueryProperties',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'result_location': 'resultLocation',
            'schedule_recurrences': 'scheduleRecurrences',
            'time_scheduled': 'timeScheduled',
            'query_properties': 'queryProperties',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._result_location = None
        self._schedule_recurrences = None
        self._time_scheduled = None
        self._query_properties = None
        self._time_created = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Schedule.
        The OCID representing unique shedule


        :return: The id of this Schedule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Schedule.
        The OCID representing unique shedule


        :param id: The id of this Schedule.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Schedule.
        The unique name of the schedule created by the user


        :return: The name of this Schedule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Schedule.
        The unique name of the schedule created by the user


        :param name: The name of this Schedule.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Schedule.
        The tenancy of the customer


        :return: The compartment_id of this Schedule.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Schedule.
        The tenancy of the customer


        :param compartment_id: The compartment_id of this Schedule.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def result_location(self):
        """
        **[Required]** Gets the result_location of this Schedule.

        :return: The result_location of this Schedule.
        :rtype: oci.usage_api.models.ResultLocation
        """
        return self._result_location

    @result_location.setter
    def result_location(self, result_location):
        """
        Sets the result_location of this Schedule.

        :param result_location: The result_location of this Schedule.
        :type: oci.usage_api.models.ResultLocation
        """
        self._result_location = result_location

    @property
    def schedule_recurrences(self):
        """
        **[Required]** Gets the schedule_recurrences of this Schedule.
        In x-obmcs-recurring-time format shown here: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10
        Describes the frequency of when the schedule will be run


        :return: The schedule_recurrences of this Schedule.
        :rtype: str
        """
        return self._schedule_recurrences

    @schedule_recurrences.setter
    def schedule_recurrences(self, schedule_recurrences):
        """
        Sets the schedule_recurrences of this Schedule.
        In x-obmcs-recurring-time format shown here: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10
        Describes the frequency of when the schedule will be run


        :param schedule_recurrences: The schedule_recurrences of this Schedule.
        :type: str
        """
        self._schedule_recurrences = schedule_recurrences

    @property
    def time_scheduled(self):
        """
        **[Required]** Gets the time_scheduled of this Schedule.
        The date and time of the first time job execution


        :return: The time_scheduled of this Schedule.
        :rtype: datetime
        """
        return self._time_scheduled

    @time_scheduled.setter
    def time_scheduled(self, time_scheduled):
        """
        Sets the time_scheduled of this Schedule.
        The date and time of the first time job execution


        :param time_scheduled: The time_scheduled of this Schedule.
        :type: datetime
        """
        self._time_scheduled = time_scheduled

    @property
    def query_properties(self):
        """
        **[Required]** Gets the query_properties of this Schedule.

        :return: The query_properties of this Schedule.
        :rtype: oci.usage_api.models.QueryProperties
        """
        return self._query_properties

    @query_properties.setter
    def query_properties(self, query_properties):
        """
        Sets the query_properties of this Schedule.

        :param query_properties: The query_properties of this Schedule.
        :type: oci.usage_api.models.QueryProperties
        """
        self._query_properties = query_properties

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Schedule.
        The date and time of when the schedule was created


        :return: The time_created of this Schedule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Schedule.
        The date and time of when the schedule was created


        :param time_created: The time_created of this Schedule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Schedule.
        The lifecycle state of the schedule

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Schedule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Schedule.
        The lifecycle state of the schedule


        :param lifecycle_state: The lifecycle_state of this Schedule.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Schedule.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Schedule.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Schedule.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Schedule.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Schedule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Schedule.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Schedule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Schedule.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Schedule.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Schedule.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Schedule.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Schedule.
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
