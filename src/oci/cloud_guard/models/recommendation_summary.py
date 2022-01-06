# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecommendationSummary(object):
    """
    Recommendation Definition.
    """

    #: A constant which can be used with the type property of a RecommendationSummary.
    #: This constant has a value of "DETECTOR_PROBLEMS"
    TYPE_DETECTOR_PROBLEMS = "DETECTOR_PROBLEMS"

    #: A constant which can be used with the type property of a RecommendationSummary.
    #: This constant has a value of "RESOLVED_PROBLEMS"
    TYPE_RESOLVED_PROBLEMS = "RESOLVED_PROBLEMS"

    #: A constant which can be used with the risk_level property of a RecommendationSummary.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a RecommendationSummary.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a RecommendationSummary.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a RecommendationSummary.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a RecommendationSummary.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_detail property of a RecommendationSummary.
    #: This constant has a value of "OPEN"
    LIFECYCLE_DETAIL_OPEN = "OPEN"

    #: A constant which can be used with the lifecycle_detail property of a RecommendationSummary.
    #: This constant has a value of "RESOLVED"
    LIFECYCLE_DETAIL_RESOLVED = "RESOLVED"

    #: A constant which can be used with the lifecycle_detail property of a RecommendationSummary.
    #: This constant has a value of "DISMISSED"
    LIFECYCLE_DETAIL_DISMISSED = "DISMISSED"

    def __init__(self, **kwargs):
        """
        Initializes a new RecommendationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RecommendationSummary.
        :type id: str

        :param type:
            The value to assign to the type property of this RecommendationSummary.
            Allowed values for this property are: "DETECTOR_PROBLEMS", "RESOLVED_PROBLEMS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param tenant_id:
            The value to assign to the tenant_id property of this RecommendationSummary.
        :type tenant_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RecommendationSummary.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this RecommendationSummary.
        :type target_id: str

        :param details:
            The value to assign to the details property of this RecommendationSummary.
        :type details: dict(str, str)

        :param risk_level:
            The value to assign to the risk_level property of this RecommendationSummary.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param problem_count:
            The value to assign to the problem_count property of this RecommendationSummary.
        :type problem_count: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RecommendationSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_detail:
            The value to assign to the lifecycle_detail property of this RecommendationSummary.
            Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_detail: str

        :param time_created:
            The value to assign to the time_created property of this RecommendationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RecommendationSummary.
        :type time_updated: datetime

        :param name:
            The value to assign to the name property of this RecommendationSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this RecommendationSummary.
        :type description: str

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'tenant_id': 'str',
            'compartment_id': 'str',
            'target_id': 'str',
            'details': 'dict(str, str)',
            'risk_level': 'str',
            'problem_count': 'int',
            'lifecycle_state': 'str',
            'lifecycle_detail': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'name': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'tenant_id': 'tenantId',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'details': 'details',
            'risk_level': 'riskLevel',
            'problem_count': 'problemCount',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_detail': 'lifecycleDetail',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'name': 'name',
            'description': 'description'
        }

        self._id = None
        self._type = None
        self._tenant_id = None
        self._compartment_id = None
        self._target_id = None
        self._details = None
        self._risk_level = None
        self._problem_count = None
        self._lifecycle_state = None
        self._lifecycle_detail = None
        self._time_created = None
        self._time_updated = None
        self._name = None
        self._description = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RecommendationSummary.
        Unique identifier for Recommendation


        :return: The id of this RecommendationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RecommendationSummary.
        Unique identifier for Recommendation


        :param id: The id of this RecommendationSummary.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        Gets the type of this RecommendationSummary.
        Recommendation type

        Allowed values for this property are: "DETECTOR_PROBLEMS", "RESOLVED_PROBLEMS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this RecommendationSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RecommendationSummary.
        Recommendation type


        :param type: The type of this RecommendationSummary.
        :type: str
        """
        allowed_values = ["DETECTOR_PROBLEMS", "RESOLVED_PROBLEMS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this RecommendationSummary.
        Tenant Identifier


        :return: The tenant_id of this RecommendationSummary.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this RecommendationSummary.
        Tenant Identifier


        :param tenant_id: The tenant_id of this RecommendationSummary.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RecommendationSummary.
        Compartment Identifier


        :return: The compartment_id of this RecommendationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RecommendationSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this RecommendationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this RecommendationSummary.
        targetId associated with the problem


        :return: The target_id of this RecommendationSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this RecommendationSummary.
        targetId associated with the problem


        :param target_id: The target_id of this RecommendationSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def details(self):
        """
        **[Required]** Gets the details of this RecommendationSummary.
        Recommendation details


        :return: The details of this RecommendationSummary.
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this RecommendationSummary.
        Recommendation details


        :param details: The details of this RecommendationSummary.
        :type: dict(str, str)
        """
        self._details = details

    @property
    def risk_level(self):
        """
        Gets the risk_level of this RecommendationSummary.
        The Risk Level

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this RecommendationSummary.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this RecommendationSummary.
        The Risk Level


        :param risk_level: The risk_level of this RecommendationSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def problem_count(self):
        """
        **[Required]** Gets the problem_count of this RecommendationSummary.
        Count number of the problem


        :return: The problem_count of this RecommendationSummary.
        :rtype: int
        """
        return self._problem_count

    @problem_count.setter
    def problem_count(self, problem_count):
        """
        Sets the problem_count of this RecommendationSummary.
        Count number of the problem


        :param problem_count: The problem_count of this RecommendationSummary.
        :type: int
        """
        self._problem_count = problem_count

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RecommendationSummary.
        The current state of the Recommendation.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RecommendationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RecommendationSummary.
        The current state of the Recommendation.


        :param lifecycle_state: The lifecycle_state of this RecommendationSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_detail(self):
        """
        **[Required]** Gets the lifecycle_detail of this RecommendationSummary.
        The lifecycleDetail will give more detail on the substate of the lifecycleState.

        Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_detail of this RecommendationSummary.
        :rtype: str
        """
        return self._lifecycle_detail

    @lifecycle_detail.setter
    def lifecycle_detail(self, lifecycle_detail):
        """
        Sets the lifecycle_detail of this RecommendationSummary.
        The lifecycleDetail will give more detail on the substate of the lifecycleState.


        :param lifecycle_detail: The lifecycle_detail of this RecommendationSummary.
        :type: str
        """
        allowed_values = ["OPEN", "RESOLVED", "DISMISSED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_detail, allowed_values):
            lifecycle_detail = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_detail = lifecycle_detail

    @property
    def time_created(self):
        """
        Gets the time_created of this RecommendationSummary.
        problem creating time


        :return: The time_created of this RecommendationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RecommendationSummary.
        problem creating time


        :param time_created: The time_created of this RecommendationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RecommendationSummary.
        problem updating time


        :return: The time_updated of this RecommendationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RecommendationSummary.
        problem updating time


        :param time_updated: The time_updated of this RecommendationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def name(self):
        """
        **[Required]** Gets the name of this RecommendationSummary.
        recommendation string showing on UX


        :return: The name of this RecommendationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RecommendationSummary.
        recommendation string showing on UX


        :param name: The name of this RecommendationSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this RecommendationSummary.
        description of the recommendation


        :return: The description of this RecommendationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RecommendationSummary.
        description of the recommendation


        :param description: The description of this RecommendationSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
