# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAnnouncementSubscriptionDetails(object):
    """
    The details for creating a new announcement subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAnnouncementSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateAnnouncementSubscriptionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateAnnouncementSubscriptionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAnnouncementSubscriptionDetails.
        :type compartment_id: str

        :param ons_topic_id:
            The value to assign to the ons_topic_id property of this CreateAnnouncementSubscriptionDetails.
        :type ons_topic_id: str

        :param filter_groups:
            The value to assign to the filter_groups property of this CreateAnnouncementSubscriptionDetails.
        :type filter_groups: dict(str, FilterGroupDetails)

        :param preferred_language:
            The value to assign to the preferred_language property of this CreateAnnouncementSubscriptionDetails.
        :type preferred_language: str

        :param preferred_time_zone:
            The value to assign to the preferred_time_zone property of this CreateAnnouncementSubscriptionDetails.
        :type preferred_time_zone: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAnnouncementSubscriptionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAnnouncementSubscriptionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'ons_topic_id': 'str',
            'filter_groups': 'dict(str, FilterGroupDetails)',
            'preferred_language': 'str',
            'preferred_time_zone': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'ons_topic_id': 'onsTopicId',
            'filter_groups': 'filterGroups',
            'preferred_language': 'preferredLanguage',
            'preferred_time_zone': 'preferredTimeZone',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._ons_topic_id = None
        self._filter_groups = None
        self._preferred_language = None
        self._preferred_time_zone = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAnnouncementSubscriptionDetails.
        A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAnnouncementSubscriptionDetails.
        A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateAnnouncementSubscriptionDetails.
        A description of the announcement subscription. Avoid entering confidential information.


        :return: The description of this CreateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAnnouncementSubscriptionDetails.
        A description of the announcement subscription. Avoid entering confidential information.


        :param description: The description of this CreateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAnnouncementSubscriptionDetails.
        The `OCID`__ of the compartment where you want to create the announcement subscription.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAnnouncementSubscriptionDetails.
        The `OCID`__ of the compartment where you want to create the announcement subscription.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def ons_topic_id(self):
        """
        **[Required]** Gets the ons_topic_id of this CreateAnnouncementSubscriptionDetails.
        The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription. The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about Notifications permissions, see `Details for Notifications`__.

        __ https://docs.cloud.oracle.com/Content/Identity/policyreference/notificationpolicyreference.htm


        :return: The ons_topic_id of this CreateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._ons_topic_id

    @ons_topic_id.setter
    def ons_topic_id(self, ons_topic_id):
        """
        Sets the ons_topic_id of this CreateAnnouncementSubscriptionDetails.
        The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription. The caller of the operation needs the ONS_TOPIC_PUBLISH permission for the targeted Notifications service topic. For more information about Notifications permissions, see `Details for Notifications`__.

        __ https://docs.cloud.oracle.com/Content/Identity/policyreference/notificationpolicyreference.htm


        :param ons_topic_id: The ons_topic_id of this CreateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._ons_topic_id = ons_topic_id

    @property
    def filter_groups(self):
        """
        Gets the filter_groups of this CreateAnnouncementSubscriptionDetails.
        A list of filter groups for the announcement subscription. A filter group combines one or more filters that the Announcements service applies to announcements for matching purposes.


        :return: The filter_groups of this CreateAnnouncementSubscriptionDetails.
        :rtype: dict(str, FilterGroupDetails)
        """
        return self._filter_groups

    @filter_groups.setter
    def filter_groups(self, filter_groups):
        """
        Sets the filter_groups of this CreateAnnouncementSubscriptionDetails.
        A list of filter groups for the announcement subscription. A filter group combines one or more filters that the Announcements service applies to announcements for matching purposes.


        :param filter_groups: The filter_groups of this CreateAnnouncementSubscriptionDetails.
        :type: dict(str, FilterGroupDetails)
        """
        self._filter_groups = filter_groups

    @property
    def preferred_language(self):
        """
        Gets the preferred_language of this CreateAnnouncementSubscriptionDetails.
        (For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.


        :return: The preferred_language of this CreateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """
        Sets the preferred_language of this CreateAnnouncementSubscriptionDetails.
        (For announcement subscriptions with Oracle Fusion Applications configured as the service only) The language in which the user prefers to receive emailed announcements. Specify the preference with a value that uses the language tag format (x-obmcs-human-language). For example fr-FR.


        :param preferred_language: The preferred_language of this CreateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._preferred_language = preferred_language

    @property
    def preferred_time_zone(self):
        """
        Gets the preferred_time_zone of this CreateAnnouncementSubscriptionDetails.
        The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example America/Los_Angeles.


        :return: The preferred_time_zone of this CreateAnnouncementSubscriptionDetails.
        :rtype: str
        """
        return self._preferred_time_zone

    @preferred_time_zone.setter
    def preferred_time_zone(self, preferred_time_zone):
        """
        Sets the preferred_time_zone of this CreateAnnouncementSubscriptionDetails.
        The time zone that the user prefers for announcement time stamps. Specify the preference with a value that uses the IANA Time Zone Database format (x-obmcs-time-zone). For example America/Los_Angeles.


        :param preferred_time_zone: The preferred_time_zone of this CreateAnnouncementSubscriptionDetails.
        :type: str
        """
        self._preferred_time_zone = preferred_time_zone

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAnnouncementSubscriptionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateAnnouncementSubscriptionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAnnouncementSubscriptionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateAnnouncementSubscriptionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAnnouncementSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateAnnouncementSubscriptionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAnnouncementSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateAnnouncementSubscriptionDetails.
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
