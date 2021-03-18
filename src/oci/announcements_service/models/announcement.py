# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_announcement import BaseAnnouncement
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Announcement(BaseAnnouncement):
    """
    A message about an impactful operational event.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Announcement object with values from keyword arguments. The default value of the :py:attr:`~oci.announcements_service.models.Announcement.type` attribute
        of this class is ``Announcement`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Announcement.
        :type id: str

        :param type:
            The value to assign to the type property of this Announcement.
        :type type: str

        :param reference_ticket_number:
            The value to assign to the reference_ticket_number property of this Announcement.
        :type reference_ticket_number: str

        :param summary:
            The value to assign to the summary property of this Announcement.
        :type summary: str

        :param time_one_title:
            The value to assign to the time_one_title property of this Announcement.
        :type time_one_title: str

        :param time_one_type:
            The value to assign to the time_one_type property of this Announcement.
            Allowed values for this property are: "ACTION_REQUIRED_BY", "NEW_START_TIME", "ORIGINAL_END_TIME", "REPORT_DATE", "START_TIME", "TIME_DETECTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type time_one_type: str

        :param time_one_value:
            The value to assign to the time_one_value property of this Announcement.
        :type time_one_value: datetime

        :param time_two_title:
            The value to assign to the time_two_title property of this Announcement.
        :type time_two_title: str

        :param time_two_type:
            The value to assign to the time_two_type property of this Announcement.
            Allowed values for this property are: "END_TIME", "NEW_END_TIME", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type time_two_type: str

        :param time_two_value:
            The value to assign to the time_two_value property of this Announcement.
        :type time_two_value: datetime

        :param services:
            The value to assign to the services property of this Announcement.
        :type services: list[str]

        :param affected_regions:
            The value to assign to the affected_regions property of this Announcement.
        :type affected_regions: list[str]

        :param announcement_type:
            The value to assign to the announcement_type property of this Announcement.
            Allowed values for this property are: "ACTION_RECOMMENDED", "ACTION_REQUIRED", "EMERGENCY_CHANGE", "EMERGENCY_MAINTENANCE", "EMERGENCY_MAINTENANCE_COMPLETE", "EMERGENCY_MAINTENANCE_EXTENDED", "EMERGENCY_MAINTENANCE_RESCHEDULED", "INFORMATION", "PLANNED_CHANGE", "PLANNED_CHANGE_COMPLETE", "PLANNED_CHANGE_EXTENDED", "PLANNED_CHANGE_RESCHEDULED", "PRODUCTION_EVENT_NOTIFICATION", "SCHEDULED_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type announcement_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Announcement.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_banner:
            The value to assign to the is_banner property of this Announcement.
        :type is_banner: bool

        :param time_created:
            The value to assign to the time_created property of this Announcement.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Announcement.
        :type time_updated: datetime

        :param description:
            The value to assign to the description property of this Announcement.
        :type description: str

        :param additional_information:
            The value to assign to the additional_information property of this Announcement.
        :type additional_information: str

        :param affected_resources:
            The value to assign to the affected_resources property of this Announcement.
        :type affected_resources: list[oci.announcements_service.models.AffectedResource]

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'reference_ticket_number': 'str',
            'summary': 'str',
            'time_one_title': 'str',
            'time_one_type': 'str',
            'time_one_value': 'datetime',
            'time_two_title': 'str',
            'time_two_type': 'str',
            'time_two_value': 'datetime',
            'services': 'list[str]',
            'affected_regions': 'list[str]',
            'announcement_type': 'str',
            'lifecycle_state': 'str',
            'is_banner': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'description': 'str',
            'additional_information': 'str',
            'affected_resources': 'list[AffectedResource]'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'reference_ticket_number': 'referenceTicketNumber',
            'summary': 'summary',
            'time_one_title': 'timeOneTitle',
            'time_one_type': 'timeOneType',
            'time_one_value': 'timeOneValue',
            'time_two_title': 'timeTwoTitle',
            'time_two_type': 'timeTwoType',
            'time_two_value': 'timeTwoValue',
            'services': 'services',
            'affected_regions': 'affectedRegions',
            'announcement_type': 'announcementType',
            'lifecycle_state': 'lifecycleState',
            'is_banner': 'isBanner',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'description': 'description',
            'additional_information': 'additionalInformation',
            'affected_resources': 'affectedResources'
        }

        self._id = None
        self._type = None
        self._reference_ticket_number = None
        self._summary = None
        self._time_one_title = None
        self._time_one_type = None
        self._time_one_value = None
        self._time_two_title = None
        self._time_two_type = None
        self._time_two_value = None
        self._services = None
        self._affected_regions = None
        self._announcement_type = None
        self._lifecycle_state = None
        self._is_banner = None
        self._time_created = None
        self._time_updated = None
        self._description = None
        self._additional_information = None
        self._affected_resources = None
        self._type = 'Announcement'

    @property
    def description(self):
        """
        Gets the description of this Announcement.
        A detailed explanation of the event, expressed by using Markdown language. Avoid entering
        confidential information.


        :return: The description of this Announcement.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Announcement.
        A detailed explanation of the event, expressed by using Markdown language. Avoid entering
        confidential information.


        :param description: The description of this Announcement.
        :type: str
        """
        self._description = description

    @property
    def additional_information(self):
        """
        Gets the additional_information of this Announcement.
        Additional information about the event, expressed by using Markdown language and included in the
        details view of an announcement. Additional information might include remediation steps or
        answers to frequently asked questions. Avoid entering confidential information.


        :return: The additional_information of this Announcement.
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """
        Sets the additional_information of this Announcement.
        Additional information about the event, expressed by using Markdown language and included in the
        details view of an announcement. Additional information might include remediation steps or
        answers to frequently asked questions. Avoid entering confidential information.


        :param additional_information: The additional_information of this Announcement.
        :type: str
        """
        self._additional_information = additional_information

    @property
    def affected_resources(self):
        """
        Gets the affected_resources of this Announcement.
        The list of resources, if any, affected by the event described in the announcement.


        :return: The affected_resources of this Announcement.
        :rtype: list[oci.announcements_service.models.AffectedResource]
        """
        return self._affected_resources

    @affected_resources.setter
    def affected_resources(self, affected_resources):
        """
        Sets the affected_resources of this Announcement.
        The list of resources, if any, affected by the event described in the announcement.


        :param affected_resources: The affected_resources of this Announcement.
        :type: list[oci.announcements_service.models.AffectedResource]
        """
        self._affected_resources = affected_resources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
