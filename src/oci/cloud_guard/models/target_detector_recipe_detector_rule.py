# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetDetectorRecipeDetectorRule(object):
    """
    Detector Recipe Rule
    """

    #: A constant which can be used with the detector property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "IAAS_ACTIVITY_DETECTOR"
    DETECTOR_IAAS_ACTIVITY_DETECTOR = "IAAS_ACTIVITY_DETECTOR"

    #: A constant which can be used with the detector property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "IAAS_CONFIGURATION_DETECTOR"
    DETECTOR_IAAS_CONFIGURATION_DETECTOR = "IAAS_CONFIGURATION_DETECTOR"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "CIDR_BLOCK"
    MANAGED_LIST_TYPES_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "USERS"
    MANAGED_LIST_TYPES_USERS = "USERS"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "GROUPS"
    MANAGED_LIST_TYPES_GROUPS = "GROUPS"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "IPV4ADDRESS"
    MANAGED_LIST_TYPES_IPV4_ADDRESS = "IPV4ADDRESS"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "IPV6ADDRESS"
    MANAGED_LIST_TYPES_IPV6_ADDRESS = "IPV6ADDRESS"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "RESOURCE_OCID"
    MANAGED_LIST_TYPES_RESOURCE_OCID = "RESOURCE_OCID"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "REGION"
    MANAGED_LIST_TYPES_REGION = "REGION"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "COUNTRY"
    MANAGED_LIST_TYPES_COUNTRY = "COUNTRY"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "STATE"
    MANAGED_LIST_TYPES_STATE = "STATE"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "CITY"
    MANAGED_LIST_TYPES_CITY = "CITY"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "TAGS"
    MANAGED_LIST_TYPES_TAGS = "TAGS"

    #: A constant which can be used with the managed_list_types property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "GENERIC"
    MANAGED_LIST_TYPES_GENERIC = "GENERIC"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeDetectorRule.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetDetectorRecipeDetectorRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param detector_rule_id:
            The value to assign to the detector_rule_id property of this TargetDetectorRecipeDetectorRule.
        :type detector_rule_id: str

        :param display_name:
            The value to assign to the display_name property of this TargetDetectorRecipeDetectorRule.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TargetDetectorRecipeDetectorRule.
        :type description: str

        :param recommendation:
            The value to assign to the recommendation property of this TargetDetectorRecipeDetectorRule.
        :type recommendation: str

        :param detector:
            The value to assign to the detector property of this TargetDetectorRecipeDetectorRule.
            Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type detector: str

        :param service_type:
            The value to assign to the service_type property of this TargetDetectorRecipeDetectorRule.
        :type service_type: str

        :param resource_type:
            The value to assign to the resource_type property of this TargetDetectorRecipeDetectorRule.
        :type resource_type: str

        :param details:
            The value to assign to the details property of this TargetDetectorRecipeDetectorRule.
        :type details: oci.cloud_guard.models.TargetDetectorDetails

        :param managed_list_types:
            The value to assign to the managed_list_types property of this TargetDetectorRecipeDetectorRule.
            Allowed values for items in this list are: "CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS", "GENERIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type managed_list_types: list[str]

        :param time_created:
            The value to assign to the time_created property of this TargetDetectorRecipeDetectorRule.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TargetDetectorRecipeDetectorRule.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetDetectorRecipeDetectorRule.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TargetDetectorRecipeDetectorRule.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'detector_rule_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'recommendation': 'str',
            'detector': 'str',
            'service_type': 'str',
            'resource_type': 'str',
            'details': 'TargetDetectorDetails',
            'managed_list_types': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'detector_rule_id': 'detectorRuleId',
            'display_name': 'displayName',
            'description': 'description',
            'recommendation': 'recommendation',
            'detector': 'detector',
            'service_type': 'serviceType',
            'resource_type': 'resourceType',
            'details': 'details',
            'managed_list_types': 'managedListTypes',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._detector_rule_id = None
        self._display_name = None
        self._description = None
        self._recommendation = None
        self._detector = None
        self._service_type = None
        self._resource_type = None
        self._details = None
        self._managed_list_types = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def detector_rule_id(self):
        """
        **[Required]** Gets the detector_rule_id of this TargetDetectorRecipeDetectorRule.
        The unique identifier of the detector rule


        :return: The detector_rule_id of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._detector_rule_id

    @detector_rule_id.setter
    def detector_rule_id(self, detector_rule_id):
        """
        Sets the detector_rule_id of this TargetDetectorRecipeDetectorRule.
        The unique identifier of the detector rule


        :param detector_rule_id: The detector_rule_id of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        self._detector_rule_id = detector_rule_id

    @property
    def display_name(self):
        """
        Gets the display_name of this TargetDetectorRecipeDetectorRule.
        displayName


        :return: The display_name of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetDetectorRecipeDetectorRule.
        displayName


        :param display_name: The display_name of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TargetDetectorRecipeDetectorRule.
        Description for TargetDetectorRecipeDetectorRule


        :return: The description of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TargetDetectorRecipeDetectorRule.
        Description for TargetDetectorRecipeDetectorRule


        :param description: The description of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        self._description = description

    @property
    def recommendation(self):
        """
        Gets the recommendation of this TargetDetectorRecipeDetectorRule.
        Recommendation for TargetDetectorRecipeDetectorRule


        :return: The recommendation of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """
        Sets the recommendation of this TargetDetectorRecipeDetectorRule.
        Recommendation for TargetDetectorRecipeDetectorRule


        :param recommendation: The recommendation of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        self._recommendation = recommendation

    @property
    def detector(self):
        """
        **[Required]** Gets the detector of this TargetDetectorRecipeDetectorRule.
        detector for the rule

        Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The detector of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """
        Sets the detector of this TargetDetectorRecipeDetectorRule.
        detector for the rule


        :param detector: The detector of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        allowed_values = ["IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR"]
        if not value_allowed_none_or_none_sentinel(detector, allowed_values):
            detector = 'UNKNOWN_ENUM_VALUE'
        self._detector = detector

    @property
    def service_type(self):
        """
        **[Required]** Gets the service_type of this TargetDetectorRecipeDetectorRule.
        service type of the configuration to which the rule is applied


        :return: The service_type of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """
        Sets the service_type of this TargetDetectorRecipeDetectorRule.
        service type of the configuration to which the rule is applied


        :param service_type: The service_type of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        self._service_type = service_type

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this TargetDetectorRecipeDetectorRule.
        resource type of the configuration to which the rule is applied


        :return: The resource_type of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this TargetDetectorRecipeDetectorRule.
        resource type of the configuration to which the rule is applied


        :param resource_type: The resource_type of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def details(self):
        """
        Gets the details of this TargetDetectorRecipeDetectorRule.

        :return: The details of this TargetDetectorRecipeDetectorRule.
        :rtype: oci.cloud_guard.models.TargetDetectorDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this TargetDetectorRecipeDetectorRule.

        :param details: The details of this TargetDetectorRecipeDetectorRule.
        :type: oci.cloud_guard.models.TargetDetectorDetails
        """
        self._details = details

    @property
    def managed_list_types(self):
        """
        Gets the managed_list_types of this TargetDetectorRecipeDetectorRule.
        List of cloudguard managed list types related to this rule

        Allowed values for items in this list are: "CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS", "GENERIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The managed_list_types of this TargetDetectorRecipeDetectorRule.
        :rtype: list[str]
        """
        return self._managed_list_types

    @managed_list_types.setter
    def managed_list_types(self, managed_list_types):
        """
        Sets the managed_list_types of this TargetDetectorRecipeDetectorRule.
        List of cloudguard managed list types related to this rule


        :param managed_list_types: The managed_list_types of this TargetDetectorRecipeDetectorRule.
        :type: list[str]
        """
        allowed_values = ["CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS", "GENERIC"]
        if managed_list_types:
            managed_list_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in managed_list_types]
        self._managed_list_types = managed_list_types

    @property
    def time_created(self):
        """
        Gets the time_created of this TargetDetectorRecipeDetectorRule.
        The date and time the target detector recipe rule was created. Format defined by RFC3339.


        :return: The time_created of this TargetDetectorRecipeDetectorRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetDetectorRecipeDetectorRule.
        The date and time the target detector recipe rule was created. Format defined by RFC3339.


        :param time_created: The time_created of this TargetDetectorRecipeDetectorRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TargetDetectorRecipeDetectorRule.
        The date and time the target detector recipe rule was updated. Format defined by RFC3339.


        :return: The time_updated of this TargetDetectorRecipeDetectorRule.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TargetDetectorRecipeDetectorRule.
        The date and time the target detector recipe rule was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this TargetDetectorRecipeDetectorRule.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TargetDetectorRecipeDetectorRule.
        The current state of the DetectorRule.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TargetDetectorRecipeDetectorRule.
        The current state of the DetectorRule.


        :param lifecycle_state: The lifecycle_state of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TargetDetectorRecipeDetectorRule.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TargetDetectorRecipeDetectorRule.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TargetDetectorRecipeDetectorRule.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TargetDetectorRecipeDetectorRule.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
