# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Problem(object):
    """
    Problem Definition.
    """

    #: A constant which can be used with the risk_level property of a Problem.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a Problem.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a Problem.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a Problem.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a Problem.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    #: A constant which can be used with the lifecycle_state property of a Problem.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Problem.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_detail property of a Problem.
    #: This constant has a value of "OPEN"
    LIFECYCLE_DETAIL_OPEN = "OPEN"

    #: A constant which can be used with the lifecycle_detail property of a Problem.
    #: This constant has a value of "RESOLVED"
    LIFECYCLE_DETAIL_RESOLVED = "RESOLVED"

    #: A constant which can be used with the lifecycle_detail property of a Problem.
    #: This constant has a value of "DISMISSED"
    LIFECYCLE_DETAIL_DISMISSED = "DISMISSED"

    #: A constant which can be used with the detector_id property of a Problem.
    #: This constant has a value of "IAAS_ACTIVITY_DETECTOR"
    DETECTOR_ID_IAAS_ACTIVITY_DETECTOR = "IAAS_ACTIVITY_DETECTOR"

    #: A constant which can be used with the detector_id property of a Problem.
    #: This constant has a value of "IAAS_CONFIGURATION_DETECTOR"
    DETECTOR_ID_IAAS_CONFIGURATION_DETECTOR = "IAAS_CONFIGURATION_DETECTOR"

    def __init__(self, **kwargs):
        """
        Initializes a new Problem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Problem.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Problem.
        :type compartment_id: str

        :param detector_rule_id:
            The value to assign to the detector_rule_id property of this Problem.
        :type detector_rule_id: str

        :param region:
            The value to assign to the region property of this Problem.
        :type region: str

        :param regions:
            The value to assign to the regions property of this Problem.
        :type regions: list[str]

        :param risk_level:
            The value to assign to the risk_level property of this Problem.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param resource_id:
            The value to assign to the resource_id property of this Problem.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this Problem.
        :type resource_name: str

        :param resource_type:
            The value to assign to the resource_type property of this Problem.
        :type resource_type: str

        :param labels:
            The value to assign to the labels property of this Problem.
        :type labels: list[str]

        :param time_last_detected:
            The value to assign to the time_last_detected property of this Problem.
        :type time_last_detected: datetime

        :param time_first_detected:
            The value to assign to the time_first_detected property of this Problem.
        :type time_first_detected: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Problem.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_detail:
            The value to assign to the lifecycle_detail property of this Problem.
            Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_detail: str

        :param detector_id:
            The value to assign to the detector_id property of this Problem.
            Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type detector_id: str

        :param target_id:
            The value to assign to the target_id property of this Problem.
        :type target_id: str

        :param comment:
            The value to assign to the comment property of this Problem.
        :type comment: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'detector_rule_id': 'str',
            'region': 'str',
            'regions': 'list[str]',
            'risk_level': 'str',
            'resource_id': 'str',
            'resource_name': 'str',
            'resource_type': 'str',
            'labels': 'list[str]',
            'time_last_detected': 'datetime',
            'time_first_detected': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_detail': 'str',
            'detector_id': 'str',
            'target_id': 'str',
            'comment': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'detector_rule_id': 'detectorRuleId',
            'region': 'region',
            'regions': 'regions',
            'risk_level': 'riskLevel',
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'resource_type': 'resourceType',
            'labels': 'labels',
            'time_last_detected': 'timeLastDetected',
            'time_first_detected': 'timeFirstDetected',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_detail': 'lifecycleDetail',
            'detector_id': 'detectorId',
            'target_id': 'targetId',
            'comment': 'comment'
        }

        self._id = None
        self._compartment_id = None
        self._detector_rule_id = None
        self._region = None
        self._regions = None
        self._risk_level = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._labels = None
        self._time_last_detected = None
        self._time_first_detected = None
        self._lifecycle_state = None
        self._lifecycle_detail = None
        self._detector_id = None
        self._target_id = None
        self._comment = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Problem.
        Unique identifier that is immutable on creation


        :return: The id of this Problem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Problem.
        Unique identifier that is immutable on creation


        :param id: The id of this Problem.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Problem.
        Compartment Identifier where the resource is created


        :return: The compartment_id of this Problem.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Problem.
        Compartment Identifier where the resource is created


        :param compartment_id: The compartment_id of this Problem.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def detector_rule_id(self):
        """
        Gets the detector_rule_id of this Problem.
        Identifier of the rule


        :return: The detector_rule_id of this Problem.
        :rtype: str
        """
        return self._detector_rule_id

    @detector_rule_id.setter
    def detector_rule_id(self, detector_rule_id):
        """
        Sets the detector_rule_id of this Problem.
        Identifier of the rule


        :param detector_rule_id: The detector_rule_id of this Problem.
        :type: str
        """
        self._detector_rule_id = detector_rule_id

    @property
    def region(self):
        """
        Gets the region of this Problem.
        DEPRECATED


        :return: The region of this Problem.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Problem.
        DEPRECATED


        :param region: The region of this Problem.
        :type: str
        """
        self._region = region

    @property
    def regions(self):
        """
        Gets the regions of this Problem.
        Regions where the problem is found


        :return: The regions of this Problem.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this Problem.
        Regions where the problem is found


        :param regions: The regions of this Problem.
        :type: list[str]
        """
        self._regions = regions

    @property
    def risk_level(self):
        """
        Gets the risk_level of this Problem.
        The Risk Level

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this Problem.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this Problem.
        The Risk Level


        :param risk_level: The risk_level of this Problem.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def resource_id(self):
        """
        Gets the resource_id of this Problem.
        Identifier of the Resource


        :return: The resource_id of this Problem.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this Problem.
        Identifier of the Resource


        :param resource_id: The resource_id of this Problem.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        Gets the resource_name of this Problem.
        DisplayName of the Resource


        :return: The resource_name of this Problem.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this Problem.
        DisplayName of the Resource


        :param resource_name: The resource_name of this Problem.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this Problem.
        Type of the Resource


        :return: The resource_type of this Problem.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this Problem.
        Type of the Resource


        :param resource_type: The resource_type of this Problem.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def labels(self):
        """
        Gets the labels of this Problem.
        user defined labels on the problem


        :return: The labels of this Problem.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this Problem.
        user defined labels on the problem


        :param labels: The labels of this Problem.
        :type: list[str]
        """
        self._labels = labels

    @property
    def time_last_detected(self):
        """
        Gets the time_last_detected of this Problem.
        The date and time the problem was last detected. Format defined by RFC3339.


        :return: The time_last_detected of this Problem.
        :rtype: datetime
        """
        return self._time_last_detected

    @time_last_detected.setter
    def time_last_detected(self, time_last_detected):
        """
        Sets the time_last_detected of this Problem.
        The date and time the problem was last detected. Format defined by RFC3339.


        :param time_last_detected: The time_last_detected of this Problem.
        :type: datetime
        """
        self._time_last_detected = time_last_detected

    @property
    def time_first_detected(self):
        """
        Gets the time_first_detected of this Problem.
        The date and time the problem was first detected. Format defined by RFC3339.


        :return: The time_first_detected of this Problem.
        :rtype: datetime
        """
        return self._time_first_detected

    @time_first_detected.setter
    def time_first_detected(self, time_first_detected):
        """
        Sets the time_first_detected of this Problem.
        The date and time the problem was first detected. Format defined by RFC3339.


        :param time_first_detected: The time_first_detected of this Problem.
        :type: datetime
        """
        self._time_first_detected = time_first_detected

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Problem.
        The current state of the Problem.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Problem.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Problem.
        The current state of the Problem.


        :param lifecycle_state: The lifecycle_state of this Problem.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_detail(self):
        """
        Gets the lifecycle_detail of this Problem.
        The lifecycleDetail will give more detail on the substate of the lifecycleState.

        Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_detail of this Problem.
        :rtype: str
        """
        return self._lifecycle_detail

    @lifecycle_detail.setter
    def lifecycle_detail(self, lifecycle_detail):
        """
        Sets the lifecycle_detail of this Problem.
        The lifecycleDetail will give more detail on the substate of the lifecycleState.


        :param lifecycle_detail: The lifecycle_detail of this Problem.
        :type: str
        """
        allowed_values = ["OPEN", "RESOLVED", "DISMISSED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_detail, allowed_values):
            lifecycle_detail = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_detail = lifecycle_detail

    @property
    def detector_id(self):
        """
        Gets the detector_id of this Problem.
        Id of the detector associated with the Problem.

        Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The detector_id of this Problem.
        :rtype: str
        """
        return self._detector_id

    @detector_id.setter
    def detector_id(self, detector_id):
        """
        Sets the detector_id of this Problem.
        Id of the detector associated with the Problem.


        :param detector_id: The detector_id of this Problem.
        :type: str
        """
        allowed_values = ["IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR"]
        if not value_allowed_none_or_none_sentinel(detector_id, allowed_values):
            detector_id = 'UNKNOWN_ENUM_VALUE'
        self._detector_id = detector_id

    @property
    def target_id(self):
        """
        Gets the target_id of this Problem.
        targetId of the problem


        :return: The target_id of this Problem.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this Problem.
        targetId of the problem


        :param target_id: The target_id of this Problem.
        :type: str
        """
        self._target_id = target_id

    @property
    def comment(self):
        """
        Gets the comment of this Problem.
        User Comments


        :return: The comment of this Problem.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Problem.
        User Comments


        :param comment: The comment of this Problem.
        :type: str
        """
        self._comment = comment

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
