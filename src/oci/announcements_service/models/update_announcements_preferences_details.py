# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_create_announcements_preferences_details import BaseCreateAnnouncementsPreferencesDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAnnouncementsPreferencesDetails(BaseCreateAnnouncementsPreferencesDetails):
    """
    The object used to update announcement email preferences.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAnnouncementsPreferencesDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.announcements_service.models.UpdateAnnouncementsPreferencesDetails.type` attribute
        of this class is ``UpdateAnnouncementsPreferencesDetails`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateAnnouncementsPreferencesDetails.
        :type type: str

        :param is_unsubscribed:
            The value to assign to the is_unsubscribed property of this UpdateAnnouncementsPreferencesDetails.
        :type is_unsubscribed: bool

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateAnnouncementsPreferencesDetails.
        :type compartment_id: str

        :param preference_type:
            The value to assign to the preference_type property of this UpdateAnnouncementsPreferencesDetails.
            Allowed values for this property are: "OPT_IN_TENANT_ANNOUNCEMENTS", "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS", "OPT_OUT_ALL_ANNOUNCEMENTS"
        :type preference_type: str

        """
        self.swagger_types = {
            'type': 'str',
            'is_unsubscribed': 'bool',
            'compartment_id': 'str',
            'preference_type': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'is_unsubscribed': 'isUnsubscribed',
            'compartment_id': 'compartmentId',
            'preference_type': 'preferenceType'
        }

        self._type = None
        self._is_unsubscribed = None
        self._compartment_id = None
        self._preference_type = None
        self._type = 'UpdateAnnouncementsPreferencesDetails'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
