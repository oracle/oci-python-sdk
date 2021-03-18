# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaseCreateAnnouncementsPreferencesDetails(object):
    """
    The model for the parameters of announcement email preferences configured for the tenancy (root compartment).
    """

    #: A constant which can be used with the preference_type property of a BaseCreateAnnouncementsPreferencesDetails.
    #: This constant has a value of "OPT_IN_TENANT_ANNOUNCEMENTS"
    PREFERENCE_TYPE_OPT_IN_TENANT_ANNOUNCEMENTS = "OPT_IN_TENANT_ANNOUNCEMENTS"

    #: A constant which can be used with the preference_type property of a BaseCreateAnnouncementsPreferencesDetails.
    #: This constant has a value of "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS"
    PREFERENCE_TYPE_OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS = "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS"

    #: A constant which can be used with the preference_type property of a BaseCreateAnnouncementsPreferencesDetails.
    #: This constant has a value of "OPT_OUT_ALL_ANNOUNCEMENTS"
    PREFERENCE_TYPE_OPT_OUT_ALL_ANNOUNCEMENTS = "OPT_OUT_ALL_ANNOUNCEMENTS"

    def __init__(self, **kwargs):
        """
        Initializes a new BaseCreateAnnouncementsPreferencesDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.announcements_service.models.CreateAnnouncementsPreferencesDetails`
        * :class:`~oci.announcements_service.models.UpdateAnnouncementsPreferencesDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BaseCreateAnnouncementsPreferencesDetails.
        :type type: str

        :param is_unsubscribed:
            The value to assign to the is_unsubscribed property of this BaseCreateAnnouncementsPreferencesDetails.
        :type is_unsubscribed: bool

        :param compartment_id:
            The value to assign to the compartment_id property of this BaseCreateAnnouncementsPreferencesDetails.
        :type compartment_id: str

        :param preference_type:
            The value to assign to the preference_type property of this BaseCreateAnnouncementsPreferencesDetails.
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'CreateAnnouncementsPreferencesDetails':
            return 'CreateAnnouncementsPreferencesDetails'

        if type == 'UpdateAnnouncementsPreferencesDetails':
            return 'UpdateAnnouncementsPreferencesDetails'
        else:
            return 'BaseCreateAnnouncementsPreferencesDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this BaseCreateAnnouncementsPreferencesDetails.
        The entity type, which specifies a model that either creates new announcement email preferences or updates existing preferences.


        :return: The type of this BaseCreateAnnouncementsPreferencesDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BaseCreateAnnouncementsPreferencesDetails.
        The entity type, which specifies a model that either creates new announcement email preferences or updates existing preferences.


        :param type: The type of this BaseCreateAnnouncementsPreferencesDetails.
        :type: str
        """
        self._type = type

    @property
    def is_unsubscribed(self):
        """
        Gets the is_unsubscribed of this BaseCreateAnnouncementsPreferencesDetails.
        A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email.
        (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)


        :return: The is_unsubscribed of this BaseCreateAnnouncementsPreferencesDetails.
        :rtype: bool
        """
        return self._is_unsubscribed

    @is_unsubscribed.setter
    def is_unsubscribed(self, is_unsubscribed):
        """
        Sets the is_unsubscribed of this BaseCreateAnnouncementsPreferencesDetails.
        A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email.
        (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)


        :param is_unsubscribed: The is_unsubscribed of this BaseCreateAnnouncementsPreferencesDetails.
        :type: bool
        """
        self._is_unsubscribed = is_unsubscribed

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this BaseCreateAnnouncementsPreferencesDetails.
        The OCID of the compartment for which you want to manage announcement email preferences. (Specify the tenancy by providing the
        root compartment OCID.)


        :return: The compartment_id of this BaseCreateAnnouncementsPreferencesDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BaseCreateAnnouncementsPreferencesDetails.
        The OCID of the compartment for which you want to manage announcement email preferences. (Specify the tenancy by providing the
        root compartment OCID.)


        :param compartment_id: The compartment_id of this BaseCreateAnnouncementsPreferencesDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def preference_type(self):
        """
        **[Required]** Gets the preference_type of this BaseCreateAnnouncementsPreferencesDetails.
        The string representing the user's preference, whether to opt in to only required announcements, to opt in to all announcements, including informational announcements, or to opt out of all announcements.

        Allowed values for this property are: "OPT_IN_TENANT_ANNOUNCEMENTS", "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS", "OPT_OUT_ALL_ANNOUNCEMENTS"


        :return: The preference_type of this BaseCreateAnnouncementsPreferencesDetails.
        :rtype: str
        """
        return self._preference_type

    @preference_type.setter
    def preference_type(self, preference_type):
        """
        Sets the preference_type of this BaseCreateAnnouncementsPreferencesDetails.
        The string representing the user's preference, whether to opt in to only required announcements, to opt in to all announcements, including informational announcements, or to opt out of all announcements.


        :param preference_type: The preference_type of this BaseCreateAnnouncementsPreferencesDetails.
        :type: str
        """
        allowed_values = ["OPT_IN_TENANT_ANNOUNCEMENTS", "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS", "OPT_OUT_ALL_ANNOUNCEMENTS"]
        if not value_allowed_none_or_none_sentinel(preference_type, allowed_values):
            raise ValueError(
                "Invalid value for `preference_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._preference_type = preference_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
