# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAnnouncementSubscriptionDetails(object):
    """
    The details for updating an announcement subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAnnouncementSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAnnouncementSubscriptionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateAnnouncementSubscriptionDetails.
        :type description: str

        :param ons_topic_id:
            The value to assign to the ons_topic_id property of this UpdateAnnouncementSubscriptionDetails.
        :type ons_topic_id: str

        :param preferred_language:
            The value to assign to the preferred_language property of this UpdateAnnouncementSubscriptionDetails.
        :type preferred_language: str

        :param preferred_time_zone:
            The value to assign to the preferred_time_zone property of this UpdateAnnouncementSubscriptionDetails.
        :type preferred_time_zone: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAnnouncementSubscriptionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAnnouncementSubscriptionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'ons_topic_id': 'str',
            'preferred_language': 'str',
            'preferred_time_zone': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'ons_topic_id': 'onsTopicId',
            'preferred_language': 'preferredLanguage',
            'preferred_time_zone': 'preferredTimeZone',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._ons_topic_id = None
        self._preferred_language = None
        self._preferred_time_zone = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAnnouncementSubscriptionDetails.
        A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAnnouncementSubscriptionDetails.
        A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateAnnouncementSubscriptionDetails.
        A description of the announcement subscription. Avoid entering confidential information.


        :return: The description of this UpdateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateAnnouncementSubscriptionDetails.
        A description of the announcement subscription. Avoid entering confidential information.


        :param description: The description of this UpdateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._description = description

    @property
    def ons_topic_id(self):
        """
        Gets the ons_topic_id of this UpdateAnnouncementSubscriptionDetails.
        The `OCID`__ of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription. The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about Notifications permissions, see `Details for Notifications`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Identity/policyreference/notificationpolicyreference.htm


        :return: The ons_topic_id of this UpdateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._ons_topic_id

    @ons_topic_id.setter
    def ons_topic_id(self, ons_topic_id):
        """
        Sets the ons_topic_id of this UpdateAnnouncementSubscriptionDetails.
        The `OCID`__ of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription. The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about Notifications permissions, see `Details for Notifications`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Identity/policyreference/notificationpolicyreference.htm


        :param ons_topic_id: The ons_topic_id of this UpdateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._ons_topic_id = ons_topic_id

    @property
    def preferred_language(self):
        """
        Gets the preferred_language of this UpdateAnnouncementSubscriptionDetails.
        (For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.


        :return: The preferred_language of this UpdateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """
        Sets the preferred_language of this UpdateAnnouncementSubscriptionDetails.
        (For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.


        :param preferred_language: The preferred_language of this UpdateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._preferred_language = preferred_language

    @property
    def preferred_time_zone(self):
        """
        Gets the preferred_time_zone of this UpdateAnnouncementSubscriptionDetails.
        The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example America/Los_Angeles.


        :return: The preferred_time_zone of this UpdateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._preferred_time_zone

    @preferred_time_zone.setter
    def preferred_time_zone(self, preferred_time_zone):
        """
        Sets the preferred_time_zone of this UpdateAnnouncementSubscriptionDetails.
        The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example America/Los_Angeles.


        :param preferred_time_zone: The preferred_time_zone of this UpdateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._preferred_time_zone = preferred_time_zone

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAnnouncementSubscriptionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateAnnouncementSubscriptionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAnnouncementSubscriptionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateAnnouncementSubscriptionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAnnouncementSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateAnnouncementSubscriptionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAnnouncementSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateAnnouncementSubscriptionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
