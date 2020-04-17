# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_announcement import BaseAnnouncement
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnnouncementSummary(BaseAnnouncement):
    """
    Summary representation of an announcement.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnnouncementSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.announcements_service.models.AnnouncementSummary.type` attribute
        of this class is ``AnnouncementSummary`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AnnouncementSummary.
        :type id: str

        :param type:
            The value to assign to the type property of this AnnouncementSummary.
        :type type: str

        :param reference_ticket_number:
            The value to assign to the reference_ticket_number property of this AnnouncementSummary.
        :type reference_ticket_number: str

        :param summary:
            The value to assign to the summary property of this AnnouncementSummary.
        :type summary: str

        :param time_one_title:
            The value to assign to the time_one_title property of this AnnouncementSummary.
        :type time_one_title: str

        :param time_one_value:
            The value to assign to the time_one_value property of this AnnouncementSummary.
        :type time_one_value: datetime

        :param time_two_title:
            The value to assign to the time_two_title property of this AnnouncementSummary.
        :type time_two_title: str

        :param time_two_value:
            The value to assign to the time_two_value property of this AnnouncementSummary.
        :type time_two_value: datetime

        :param services:
            The value to assign to the services property of this AnnouncementSummary.
        :type services: list[str]

        :param affected_regions:
            The value to assign to the affected_regions property of this AnnouncementSummary.
        :type affected_regions: list[str]

        :param announcement_type:
            The value to assign to the announcement_type property of this AnnouncementSummary.
            Allowed values for this property are: "ACTION_RECOMMENDED", "ACTION_REQUIRED", "EMERGENCY_CHANGE", "EMERGENCY_MAINTENANCE", "EMERGENCY_MAINTENANCE_COMPLETE", "EMERGENCY_MAINTENANCE_EXTENDED", "EMERGENCY_MAINTENANCE_RESCHEDULED", "INFORMATION", "PLANNED_CHANGE", "PLANNED_CHANGE_COMPLETE", "PLANNED_CHANGE_EXTENDED", "PLANNED_CHANGE_RESCHEDULED", "PRODUCTION_EVENT_NOTIFICATION", "SCHEDULED_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type announcement_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AnnouncementSummary.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_banner:
            The value to assign to the is_banner property of this AnnouncementSummary.
        :type is_banner: bool

        :param time_created:
            The value to assign to the time_created property of this AnnouncementSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AnnouncementSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'reference_ticket_number': 'str',
            'summary': 'str',
            'time_one_title': 'str',
            'time_one_value': 'datetime',
            'time_two_title': 'str',
            'time_two_value': 'datetime',
            'services': 'list[str]',
            'affected_regions': 'list[str]',
            'announcement_type': 'str',
            'lifecycle_state': 'str',
            'is_banner': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'reference_ticket_number': 'referenceTicketNumber',
            'summary': 'summary',
            'time_one_title': 'timeOneTitle',
            'time_one_value': 'timeOneValue',
            'time_two_title': 'timeTwoTitle',
            'time_two_value': 'timeTwoValue',
            'services': 'services',
            'affected_regions': 'affectedRegions',
            'announcement_type': 'announcementType',
            'lifecycle_state': 'lifecycleState',
            'is_banner': 'isBanner',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._type = None
        self._reference_ticket_number = None
        self._summary = None
        self._time_one_title = None
        self._time_one_value = None
        self._time_two_title = None
        self._time_two_value = None
        self._services = None
        self._affected_regions = None
        self._announcement_type = None
        self._lifecycle_state = None
        self._is_banner = None
        self._time_created = None
        self._time_updated = None
        self._type = 'AnnouncementSummary'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
