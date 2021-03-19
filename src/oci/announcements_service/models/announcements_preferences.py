# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_announcements_preferences import BaseAnnouncementsPreferences
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnnouncementsPreferences(BaseAnnouncementsPreferences):
    """
    The object for announcement email preferences.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnnouncementsPreferences object with values from keyword arguments. The default value of the :py:attr:`~oci.announcements_service.models.AnnouncementsPreferences.type` attribute
        of this class is ``AnnouncementsPreferences`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AnnouncementsPreferences.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AnnouncementsPreferences.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this AnnouncementsPreferences.
        :type id: str

        :param is_unsubscribed:
            The value to assign to the is_unsubscribed property of this AnnouncementsPreferences.
        :type is_unsubscribed: bool

        :param time_created:
            The value to assign to the time_created property of this AnnouncementsPreferences.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AnnouncementsPreferences.
        :type time_updated: datetime

        :param preference_type:
            The value to assign to the preference_type property of this AnnouncementsPreferences.
        :type preference_type: str

        """
        self.swagger_types = {
            'type': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'is_unsubscribed': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'preference_type': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'is_unsubscribed': 'isUnsubscribed',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'preference_type': 'preferenceType'
        }

        self._type = None
        self._compartment_id = None
        self._id = None
        self._is_unsubscribed = None
        self._time_created = None
        self._time_updated = None
        self._preference_type = None
        self._type = 'AnnouncementsPreferences'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
