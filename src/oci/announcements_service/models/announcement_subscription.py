# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnnouncementSubscription(object):
    """
    A subscription with the Announcements service to receive selected announcements in the format and delivery mechanisms supported by a corresponding topic endpoint configured in the Oracle Cloud Infrastructure Notifications service.
    """

    #: A constant which can be used with the lifecycle_state property of a AnnouncementSubscription.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnnouncementSubscription.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AnnouncementSubscription.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AnnouncementSubscription object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AnnouncementSubscription.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AnnouncementSubscription.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AnnouncementSubscription.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AnnouncementSubscription.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this AnnouncementSubscription.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AnnouncementSubscription.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AnnouncementSubscription.
            Allowed values for this property are: "ACTIVE", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AnnouncementSubscription.
        :type lifecycle_details: str

        :param ons_topic_id:
            The value to assign to the ons_topic_id property of this AnnouncementSubscription.
        :type ons_topic_id: str

        :param filter_groups:
            The value to assign to the filter_groups property of this AnnouncementSubscription.
        :type filter_groups: dict(str, FilterGroup)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AnnouncementSubscription.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AnnouncementSubscription.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AnnouncementSubscription.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'ons_topic_id': 'str',
            'filter_groups': 'dict(str, FilterGroup)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'ons_topic_id': 'onsTopicId',
            'filter_groups': 'filterGroups',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._ons_topic_id = None
        self._filter_groups = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AnnouncementSubscription.
        The `OCID`__ of the announcement subscription.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AnnouncementSubscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AnnouncementSubscription.
        The `OCID`__ of the announcement subscription.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AnnouncementSubscription.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AnnouncementSubscription.
        A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this AnnouncementSubscription.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AnnouncementSubscription.
        A user-friendly name for the announcement subscription. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this AnnouncementSubscription.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this AnnouncementSubscription.
        A description of the announcement subscription. Avoid entering confidential information.


        :return: The description of this AnnouncementSubscription.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AnnouncementSubscription.
        A description of the announcement subscription. Avoid entering confidential information.


        :param description: The description of this AnnouncementSubscription.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AnnouncementSubscription.
        The OCID of the compartment that contains the announcement subscription.


        :return: The compartment_id of this AnnouncementSubscription.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AnnouncementSubscription.
        The OCID of the compartment that contains the announcement subscription.


        :param compartment_id: The compartment_id of this AnnouncementSubscription.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AnnouncementSubscription.
        The date and time that the announcement subscription was created, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AnnouncementSubscription.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AnnouncementSubscription.
        The date and time that the announcement subscription was created, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AnnouncementSubscription.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AnnouncementSubscription.
        The date and time that the announcement subscription was updated, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this AnnouncementSubscription.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AnnouncementSubscription.
        The date and time that the announcement subscription was updated, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this AnnouncementSubscription.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AnnouncementSubscription.
        The current lifecycle state of the announcement subscription.

        Allowed values for this property are: "ACTIVE", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AnnouncementSubscription.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AnnouncementSubscription.
        The current lifecycle state of the announcement subscription.


        :param lifecycle_state: The lifecycle_state of this AnnouncementSubscription.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AnnouncementSubscription.
        A message describing the current lifecycle state in more detail. For example, details might provide required or recommended actions for a resource in a Failed state.


        :return: The lifecycle_details of this AnnouncementSubscription.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AnnouncementSubscription.
        A message describing the current lifecycle state in more detail. For example, details might provide required or recommended actions for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this AnnouncementSubscription.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def ons_topic_id(self):
        """
        **[Required]** Gets the ons_topic_id of this AnnouncementSubscription.
        The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription.


        :return: The ons_topic_id of this AnnouncementSubscription.
        :rtype: str
        """
        return self._ons_topic_id

    @ons_topic_id.setter
    def ons_topic_id(self, ons_topic_id):
        """
        Sets the ons_topic_id of this AnnouncementSubscription.
        The OCID of the Notifications service topic that is the target for publishing announcements that match the configured announcement subscription.


        :param ons_topic_id: The ons_topic_id of this AnnouncementSubscription.
        :type: str
        """
        self._ons_topic_id = ons_topic_id

    @property
    def filter_groups(self):
        """
        Gets the filter_groups of this AnnouncementSubscription.
        A list of filter groups for the announcement subscription. A filter group is a combination of multiple filters applied to announcements for matching purposes.


        :return: The filter_groups of this AnnouncementSubscription.
        :rtype: dict(str, FilterGroup)
        """
        return self._filter_groups

    @filter_groups.setter
    def filter_groups(self, filter_groups):
        """
        Sets the filter_groups of this AnnouncementSubscription.
        A list of filter groups for the announcement subscription. A filter group is a combination of multiple filters applied to announcements for matching purposes.


        :param filter_groups: The filter_groups of this AnnouncementSubscription.
        :type: dict(str, FilterGroup)
        """
        self._filter_groups = filter_groups

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this AnnouncementSubscription.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this AnnouncementSubscription.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AnnouncementSubscription.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this AnnouncementSubscription.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this AnnouncementSubscription.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AnnouncementSubscription.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AnnouncementSubscription.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AnnouncementSubscription.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AnnouncementSubscription.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AnnouncementSubscription.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AnnouncementSubscription.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AnnouncementSubscription.
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
