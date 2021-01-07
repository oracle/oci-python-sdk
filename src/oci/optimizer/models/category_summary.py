# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CategorySummary(object):
    """
    The metadata associated with the category summary.

    **Caution:** Avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CategorySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    def __init__(self, **kwargs):
        """
        Initializes a new CategorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CategorySummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CategorySummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CategorySummary.
        :type name: str

        :param description:
            The value to assign to the description property of this CategorySummary.
        :type description: str

        :param recommendation_counts:
            The value to assign to the recommendation_counts property of this CategorySummary.
        :type recommendation_counts: list[oci.optimizer.models.RecommendationCount]

        :param resource_counts:
            The value to assign to the resource_counts property of this CategorySummary.
        :type resource_counts: list[oci.optimizer.models.ResourceCount]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CategorySummary.
            Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param estimated_cost_saving:
            The value to assign to the estimated_cost_saving property of this CategorySummary.
        :type estimated_cost_saving: float

        :param time_created:
            The value to assign to the time_created property of this CategorySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CategorySummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'recommendation_counts': 'list[RecommendationCount]',
            'resource_counts': 'list[ResourceCount]',
            'lifecycle_state': 'str',
            'estimated_cost_saving': 'float',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'recommendation_counts': 'recommendationCounts',
            'resource_counts': 'resourceCounts',
            'lifecycle_state': 'lifecycleState',
            'estimated_cost_saving': 'estimatedCostSaving',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._recommendation_counts = None
        self._resource_counts = None
        self._lifecycle_state = None
        self._estimated_cost_saving = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CategorySummary.
        The unique OCID of the category.


        :return: The id of this CategorySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CategorySummary.
        The unique OCID of the category.


        :param id: The id of this CategorySummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CategorySummary.
        The OCID of the tenancy. The tenancy is the root compartment.


        :return: The compartment_id of this CategorySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CategorySummary.
        The OCID of the tenancy. The tenancy is the root compartment.


        :param compartment_id: The compartment_id of this CategorySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CategorySummary.
        The name assigned to the category.


        :return: The name of this CategorySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CategorySummary.
        The name assigned to the category.


        :param name: The name of this CategorySummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CategorySummary.
        Text describing the category.


        :return: The description of this CategorySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CategorySummary.
        Text describing the category.


        :param description: The description of this CategorySummary.
        :type: str
        """
        self._description = description

    @property
    def recommendation_counts(self):
        """
        **[Required]** Gets the recommendation_counts of this CategorySummary.
        An array of `RecommendationCount` objects grouped by the level of importance assigned to each recommendation.


        :return: The recommendation_counts of this CategorySummary.
        :rtype: list[oci.optimizer.models.RecommendationCount]
        """
        return self._recommendation_counts

    @recommendation_counts.setter
    def recommendation_counts(self, recommendation_counts):
        """
        Sets the recommendation_counts of this CategorySummary.
        An array of `RecommendationCount` objects grouped by the level of importance assigned to each recommendation.


        :param recommendation_counts: The recommendation_counts of this CategorySummary.
        :type: list[oci.optimizer.models.RecommendationCount]
        """
        self._recommendation_counts = recommendation_counts

    @property
    def resource_counts(self):
        """
        **[Required]** Gets the resource_counts of this CategorySummary.
        An array of `ResourceCount` objects grouped by the status of each recommendation.


        :return: The resource_counts of this CategorySummary.
        :rtype: list[oci.optimizer.models.ResourceCount]
        """
        return self._resource_counts

    @resource_counts.setter
    def resource_counts(self, resource_counts):
        """
        Sets the resource_counts of this CategorySummary.
        An array of `ResourceCount` objects grouped by the status of each recommendation.


        :param resource_counts: The resource_counts of this CategorySummary.
        :type: list[oci.optimizer.models.ResourceCount]
        """
        self._resource_counts = resource_counts

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CategorySummary.
        The category's current state.

        Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CategorySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CategorySummary.
        The category's current state.


        :param lifecycle_state: The lifecycle_state of this CategorySummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def estimated_cost_saving(self):
        """
        **[Required]** Gets the estimated_cost_saving of this CategorySummary.
        The estimated cost savings, in dollars, for the category.


        :return: The estimated_cost_saving of this CategorySummary.
        :rtype: float
        """
        return self._estimated_cost_saving

    @estimated_cost_saving.setter
    def estimated_cost_saving(self, estimated_cost_saving):
        """
        Sets the estimated_cost_saving of this CategorySummary.
        The estimated cost savings, in dollars, for the category.


        :param estimated_cost_saving: The estimated_cost_saving of this CategorySummary.
        :type: float
        """
        self._estimated_cost_saving = estimated_cost_saving

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CategorySummary.
        The date and time the category details were created, in the format defined by RFC3339.


        :return: The time_created of this CategorySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CategorySummary.
        The date and time the category details were created, in the format defined by RFC3339.


        :param time_created: The time_created of this CategorySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this CategorySummary.
        The date and time the category details were last updated, in the format defined by RFC3339.


        :return: The time_updated of this CategorySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this CategorySummary.
        The date and time the category details were last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this CategorySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
