# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecommendationSummary(object):
    """
    The metadata associated with the recommendation summary.

    **Caution:** Avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the importance property of a RecommendationSummary.
    #: This constant has a value of "CRITICAL"
    IMPORTANCE_CRITICAL = "CRITICAL"

    #: A constant which can be used with the importance property of a RecommendationSummary.
    #: This constant has a value of "HIGH"
    IMPORTANCE_HIGH = "HIGH"

    #: A constant which can be used with the importance property of a RecommendationSummary.
    #: This constant has a value of "MODERATE"
    IMPORTANCE_MODERATE = "MODERATE"

    #: A constant which can be used with the importance property of a RecommendationSummary.
    #: This constant has a value of "LOW"
    IMPORTANCE_LOW = "LOW"

    #: A constant which can be used with the importance property of a RecommendationSummary.
    #: This constant has a value of "MINOR"
    IMPORTANCE_MINOR = "MINOR"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a RecommendationSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the status property of a RecommendationSummary.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    #: A constant which can be used with the status property of a RecommendationSummary.
    #: This constant has a value of "DISMISSED"
    STATUS_DISMISSED = "DISMISSED"

    #: A constant which can be used with the status property of a RecommendationSummary.
    #: This constant has a value of "POSTPONED"
    STATUS_POSTPONED = "POSTPONED"

    #: A constant which can be used with the status property of a RecommendationSummary.
    #: This constant has a value of "IMPLEMENTED"
    STATUS_IMPLEMENTED = "IMPLEMENTED"

    def __init__(self, **kwargs):
        """
        Initializes a new RecommendationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RecommendationSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RecommendationSummary.
        :type compartment_id: str

        :param category_id:
            The value to assign to the category_id property of this RecommendationSummary.
        :type category_id: str

        :param name:
            The value to assign to the name property of this RecommendationSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this RecommendationSummary.
        :type description: str

        :param importance:
            The value to assign to the importance property of this RecommendationSummary.
            Allowed values for this property are: "CRITICAL", "HIGH", "MODERATE", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type importance: str

        :param resource_counts:
            The value to assign to the resource_counts property of this RecommendationSummary.
        :type resource_counts: list[oci.optimizer.models.ResourceCount]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RecommendationSummary.
            Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param estimated_cost_saving:
            The value to assign to the estimated_cost_saving property of this RecommendationSummary.
        :type estimated_cost_saving: float

        :param status:
            The value to assign to the status property of this RecommendationSummary.
            Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_status_begin:
            The value to assign to the time_status_begin property of this RecommendationSummary.
        :type time_status_begin: datetime

        :param time_status_end:
            The value to assign to the time_status_end property of this RecommendationSummary.
        :type time_status_end: datetime

        :param time_created:
            The value to assign to the time_created property of this RecommendationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RecommendationSummary.
        :type time_updated: datetime

        :param supported_levels:
            The value to assign to the supported_levels property of this RecommendationSummary.
        :type supported_levels: oci.optimizer.models.SupportedLevels

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'category_id': 'str',
            'name': 'str',
            'description': 'str',
            'importance': 'str',
            'resource_counts': 'list[ResourceCount]',
            'lifecycle_state': 'str',
            'estimated_cost_saving': 'float',
            'status': 'str',
            'time_status_begin': 'datetime',
            'time_status_end': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'supported_levels': 'SupportedLevels'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'category_id': 'categoryId',
            'name': 'name',
            'description': 'description',
            'importance': 'importance',
            'resource_counts': 'resourceCounts',
            'lifecycle_state': 'lifecycleState',
            'estimated_cost_saving': 'estimatedCostSaving',
            'status': 'status',
            'time_status_begin': 'timeStatusBegin',
            'time_status_end': 'timeStatusEnd',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'supported_levels': 'supportedLevels'
        }

        self._id = None
        self._compartment_id = None
        self._category_id = None
        self._name = None
        self._description = None
        self._importance = None
        self._resource_counts = None
        self._lifecycle_state = None
        self._estimated_cost_saving = None
        self._status = None
        self._time_status_begin = None
        self._time_status_end = None
        self._time_created = None
        self._time_updated = None
        self._supported_levels = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RecommendationSummary.
        The unique OCID associated with the recommendation.


        :return: The id of this RecommendationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RecommendationSummary.
        The unique OCID associated with the recommendation.


        :param id: The id of this RecommendationSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RecommendationSummary.
        The OCID of the tenancy. The tenancy is the root compartment.


        :return: The compartment_id of this RecommendationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RecommendationSummary.
        The OCID of the tenancy. The tenancy is the root compartment.


        :param compartment_id: The compartment_id of this RecommendationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def category_id(self):
        """
        **[Required]** Gets the category_id of this RecommendationSummary.
        The unique OCID associated with the category.


        :return: The category_id of this RecommendationSummary.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this RecommendationSummary.
        The unique OCID associated with the category.


        :param category_id: The category_id of this RecommendationSummary.
        :type: str
        """
        self._category_id = category_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this RecommendationSummary.
        The name assigned to the recommendation.


        :return: The name of this RecommendationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RecommendationSummary.
        The name assigned to the recommendation.


        :param name: The name of this RecommendationSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this RecommendationSummary.
        Text describing the recommendation.


        :return: The description of this RecommendationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RecommendationSummary.
        Text describing the recommendation.


        :param description: The description of this RecommendationSummary.
        :type: str
        """
        self._description = description

    @property
    def importance(self):
        """
        **[Required]** Gets the importance of this RecommendationSummary.
        The level of importance assigned to the recommendation.

        Allowed values for this property are: "CRITICAL", "HIGH", "MODERATE", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The importance of this RecommendationSummary.
        :rtype: str
        """
        return self._importance

    @importance.setter
    def importance(self, importance):
        """
        Sets the importance of this RecommendationSummary.
        The level of importance assigned to the recommendation.


        :param importance: The importance of this RecommendationSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MODERATE", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(importance, allowed_values):
            importance = 'UNKNOWN_ENUM_VALUE'
        self._importance = importance

    @property
    def resource_counts(self):
        """
        **[Required]** Gets the resource_counts of this RecommendationSummary.
        An array of `ResourceCount` objects grouped by the status of the resource actions.


        :return: The resource_counts of this RecommendationSummary.
        :rtype: list[oci.optimizer.models.ResourceCount]
        """
        return self._resource_counts

    @resource_counts.setter
    def resource_counts(self, resource_counts):
        """
        Sets the resource_counts of this RecommendationSummary.
        An array of `ResourceCount` objects grouped by the status of the resource actions.


        :param resource_counts: The resource_counts of this RecommendationSummary.
        :type: list[oci.optimizer.models.ResourceCount]
        """
        self._resource_counts = resource_counts

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RecommendationSummary.
        The recommendation's current state.

        Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RecommendationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RecommendationSummary.
        The recommendation's current state.


        :param lifecycle_state: The lifecycle_state of this RecommendationSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def estimated_cost_saving(self):
        """
        **[Required]** Gets the estimated_cost_saving of this RecommendationSummary.
        The estimated cost savings, in dollars, for the recommendation.


        :return: The estimated_cost_saving of this RecommendationSummary.
        :rtype: float
        """
        return self._estimated_cost_saving

    @estimated_cost_saving.setter
    def estimated_cost_saving(self, estimated_cost_saving):
        """
        Sets the estimated_cost_saving of this RecommendationSummary.
        The estimated cost savings, in dollars, for the recommendation.


        :param estimated_cost_saving: The estimated_cost_saving of this RecommendationSummary.
        :type: float
        """
        self._estimated_cost_saving = estimated_cost_saving

    @property
    def status(self):
        """
        **[Required]** Gets the status of this RecommendationSummary.
        The current status of the recommendation.

        Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this RecommendationSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RecommendationSummary.
        The current status of the recommendation.


        :param status: The status of this RecommendationSummary.
        :type: str
        """
        allowed_values = ["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_status_begin(self):
        """
        **[Required]** Gets the time_status_begin of this RecommendationSummary.
        The date and time that the recommendation entered its current status. The format is defined by RFC3339.

        For example, \"The status of the recommendation changed from `pending` to `current(ignored)` on this date and time.\"


        :return: The time_status_begin of this RecommendationSummary.
        :rtype: datetime
        """
        return self._time_status_begin

    @time_status_begin.setter
    def time_status_begin(self, time_status_begin):
        """
        Sets the time_status_begin of this RecommendationSummary.
        The date and time that the recommendation entered its current status. The format is defined by RFC3339.

        For example, \"The status of the recommendation changed from `pending` to `current(ignored)` on this date and time.\"


        :param time_status_begin: The time_status_begin of this RecommendationSummary.
        :type: datetime
        """
        self._time_status_begin = time_status_begin

    @property
    def time_status_end(self):
        """
        Gets the time_status_end of this RecommendationSummary.
        The date and time the current status will change. The format is defined by RFC3339.

        For example, \"The current `postponed` status of the recommendation will end and change to `pending` on this
        date and time.\"


        :return: The time_status_end of this RecommendationSummary.
        :rtype: datetime
        """
        return self._time_status_end

    @time_status_end.setter
    def time_status_end(self, time_status_end):
        """
        Sets the time_status_end of this RecommendationSummary.
        The date and time the current status will change. The format is defined by RFC3339.

        For example, \"The current `postponed` status of the recommendation will end and change to `pending` on this
        date and time.\"


        :param time_status_end: The time_status_end of this RecommendationSummary.
        :type: datetime
        """
        self._time_status_end = time_status_end

    @property
    def time_created(self):
        """
        Gets the time_created of this RecommendationSummary.
        The date and time the recommendation details were created, in the format defined by RFC3339.


        :return: The time_created of this RecommendationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RecommendationSummary.
        The date and time the recommendation details were created, in the format defined by RFC3339.


        :param time_created: The time_created of this RecommendationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RecommendationSummary.
        The date and time the recommendation details were last updated, in the format defined by RFC3339.


        :return: The time_updated of this RecommendationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RecommendationSummary.
        The date and time the recommendation details were last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this RecommendationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def supported_levels(self):
        """
        Gets the supported_levels of this RecommendationSummary.

        :return: The supported_levels of this RecommendationSummary.
        :rtype: oci.optimizer.models.SupportedLevels
        """
        return self._supported_levels

    @supported_levels.setter
    def supported_levels(self, supported_levels):
        """
        Sets the supported_levels of this RecommendationSummary.

        :param supported_levels: The supported_levels of this RecommendationSummary.
        :type: oci.optimizer.models.SupportedLevels
        """
        self._supported_levels = supported_levels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
