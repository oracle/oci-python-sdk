# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaseAnnouncementsPreferences(object):
    """
    The object that contains the announcement email preferences configured for the tenancy (root compartment).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BaseAnnouncementsPreferences object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.announcements_service.models.AnnouncementsPreferencesSummary`
        * :class:`~oci.announcements_service.models.AnnouncementsPreferences`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BaseAnnouncementsPreferences.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BaseAnnouncementsPreferences.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this BaseAnnouncementsPreferences.
        :type id: str

        :param is_unsubscribed:
            The value to assign to the is_unsubscribed property of this BaseAnnouncementsPreferences.
        :type is_unsubscribed: bool

        :param time_created:
            The value to assign to the time_created property of this BaseAnnouncementsPreferences.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BaseAnnouncementsPreferences.
        :type time_updated: datetime

        :param preference_type:
            The value to assign to the preference_type property of this BaseAnnouncementsPreferences.
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'AnnouncementsPreferencesSummary':
            return 'AnnouncementsPreferencesSummary'

        if type == 'AnnouncementsPreferences':
            return 'AnnouncementsPreferences'
        else:
            return 'BaseAnnouncementsPreferences'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this BaseAnnouncementsPreferences.
        The entity type, which specifies either an object or a summary object for announcement email preferences.


        :return: The type of this BaseAnnouncementsPreferences.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BaseAnnouncementsPreferences.
        The entity type, which specifies either an object or a summary object for announcement email preferences.


        :param type: The type of this BaseAnnouncementsPreferences.
        :type: str
        """
        self._type = type

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this BaseAnnouncementsPreferences.
        The OCID of the compartment for which the email preferences apply. Because announcements are
        specific to a tenancy, specify the tenancy by providing the root compartment OCID.


        :return: The compartment_id of this BaseAnnouncementsPreferences.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BaseAnnouncementsPreferences.
        The OCID of the compartment for which the email preferences apply. Because announcements are
        specific to a tenancy, specify the tenancy by providing the root compartment OCID.


        :param compartment_id: The compartment_id of this BaseAnnouncementsPreferences.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        Gets the id of this BaseAnnouncementsPreferences.
        The ID of the preferences.


        :return: The id of this BaseAnnouncementsPreferences.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BaseAnnouncementsPreferences.
        The ID of the preferences.


        :param id: The id of this BaseAnnouncementsPreferences.
        :type: str
        """
        self._id = id

    @property
    def is_unsubscribed(self):
        """
        Gets the is_unsubscribed of this BaseAnnouncementsPreferences.
        A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email.
        (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)


        :return: The is_unsubscribed of this BaseAnnouncementsPreferences.
        :rtype: bool
        """
        return self._is_unsubscribed

    @is_unsubscribed.setter
    def is_unsubscribed(self, is_unsubscribed):
        """
        Sets the is_unsubscribed of this BaseAnnouncementsPreferences.
        A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email.
        (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)


        :param is_unsubscribed: The is_unsubscribed of this BaseAnnouncementsPreferences.
        :type: bool
        """
        self._is_unsubscribed = is_unsubscribed

    @property
    def time_created(self):
        """
        Gets the time_created of this BaseAnnouncementsPreferences.
        When the preferences were set initially.


        :return: The time_created of this BaseAnnouncementsPreferences.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BaseAnnouncementsPreferences.
        When the preferences were set initially.


        :param time_created: The time_created of this BaseAnnouncementsPreferences.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BaseAnnouncementsPreferences.
        When the preferences were last updated.


        :return: The time_updated of this BaseAnnouncementsPreferences.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BaseAnnouncementsPreferences.
        When the preferences were last updated.


        :param time_updated: The time_updated of this BaseAnnouncementsPreferences.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def preference_type(self):
        """
        Gets the preference_type of this BaseAnnouncementsPreferences.
        The string representing the user's preference regarding receiving announcements by email.


        :return: The preference_type of this BaseAnnouncementsPreferences.
        :rtype: str
        """
        return self._preference_type

    @preference_type.setter
    def preference_type(self, preference_type):
        """
        Sets the preference_type of this BaseAnnouncementsPreferences.
        The string representing the user's preference regarding receiving announcements by email.


        :param preference_type: The preference_type of this BaseAnnouncementsPreferences.
        :type: str
        """
        self._preference_type = preference_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
