# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailabilityHistorySummary(object):
    """
    Availability history of Management Agent.
    """

    #: A constant which can be used with the availability_status property of a AvailabilityHistorySummary.
    #: This constant has a value of "ACTIVE"
    AVAILABILITY_STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the availability_status property of a AvailabilityHistorySummary.
    #: This constant has a value of "SILENT"
    AVAILABILITY_STATUS_SILENT = "SILENT"

    #: A constant which can be used with the availability_status property of a AvailabilityHistorySummary.
    #: This constant has a value of "NOT_AVAILABLE"
    AVAILABILITY_STATUS_NOT_AVAILABLE = "NOT_AVAILABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new AvailabilityHistorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param management_agent_id:
            The value to assign to the management_agent_id property of this AvailabilityHistorySummary.
        :type management_agent_id: str

        :param availability_status:
            The value to assign to the availability_status property of this AvailabilityHistorySummary.
            Allowed values for this property are: "ACTIVE", "SILENT", "NOT_AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type availability_status: str

        :param time_availability_status_started:
            The value to assign to the time_availability_status_started property of this AvailabilityHistorySummary.
        :type time_availability_status_started: datetime

        :param time_availability_status_ended:
            The value to assign to the time_availability_status_ended property of this AvailabilityHistorySummary.
        :type time_availability_status_ended: datetime

        """
        self.swagger_types = {
            'management_agent_id': 'str',
            'availability_status': 'str',
            'time_availability_status_started': 'datetime',
            'time_availability_status_ended': 'datetime'
        }

        self.attribute_map = {
            'management_agent_id': 'managementAgentId',
            'availability_status': 'availabilityStatus',
            'time_availability_status_started': 'timeAvailabilityStatusStarted',
            'time_availability_status_ended': 'timeAvailabilityStatusEnded'
        }

        self._management_agent_id = None
        self._availability_status = None
        self._time_availability_status_started = None
        self._time_availability_status_ended = None

    @property
    def management_agent_id(self):
        """
        **[Required]** Gets the management_agent_id of this AvailabilityHistorySummary.
        agent identifier


        :return: The management_agent_id of this AvailabilityHistorySummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this AvailabilityHistorySummary.
        agent identifier


        :param management_agent_id: The management_agent_id of this AvailabilityHistorySummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def availability_status(self):
        """
        **[Required]** Gets the availability_status of this AvailabilityHistorySummary.
        The availability status of managementAgent

        Allowed values for this property are: "ACTIVE", "SILENT", "NOT_AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The availability_status of this AvailabilityHistorySummary.
        :rtype: str
        """
        return self._availability_status

    @availability_status.setter
    def availability_status(self, availability_status):
        """
        Sets the availability_status of this AvailabilityHistorySummary.
        The availability status of managementAgent


        :param availability_status: The availability_status of this AvailabilityHistorySummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "SILENT", "NOT_AVAILABLE"]
        if not value_allowed_none_or_none_sentinel(availability_status, allowed_values):
            availability_status = 'UNKNOWN_ENUM_VALUE'
        self._availability_status = availability_status

    @property
    def time_availability_status_started(self):
        """
        Gets the time_availability_status_started of this AvailabilityHistorySummary.
        The time at which the Management Agent moved to the availability status. An RFC3339 formatted datetime string


        :return: The time_availability_status_started of this AvailabilityHistorySummary.
        :rtype: datetime
        """
        return self._time_availability_status_started

    @time_availability_status_started.setter
    def time_availability_status_started(self, time_availability_status_started):
        """
        Sets the time_availability_status_started of this AvailabilityHistorySummary.
        The time at which the Management Agent moved to the availability status. An RFC3339 formatted datetime string


        :param time_availability_status_started: The time_availability_status_started of this AvailabilityHistorySummary.
        :type: datetime
        """
        self._time_availability_status_started = time_availability_status_started

    @property
    def time_availability_status_ended(self):
        """
        Gets the time_availability_status_ended of this AvailabilityHistorySummary.
        The time till which the Management Agent was known to be in the availability status. An RFC3339 formatted datetime string


        :return: The time_availability_status_ended of this AvailabilityHistorySummary.
        :rtype: datetime
        """
        return self._time_availability_status_ended

    @time_availability_status_ended.setter
    def time_availability_status_ended(self, time_availability_status_ended):
        """
        Sets the time_availability_status_ended of this AvailabilityHistorySummary.
        The time till which the Management Agent was known to be in the availability status. An RFC3339 formatted datetime string


        :param time_availability_status_ended: The time_availability_status_ended of this AvailabilityHistorySummary.
        :type: datetime
        """
        self._time_availability_status_ended = time_availability_status_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
