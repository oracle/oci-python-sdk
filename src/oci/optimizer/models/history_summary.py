# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HistorySummary(object):
    """
    The metadata associated with the recommendation history and its related resources.
    """

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a HistorySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the status property of a HistorySummary.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    #: A constant which can be used with the status property of a HistorySummary.
    #: This constant has a value of "DISMISSED"
    STATUS_DISMISSED = "DISMISSED"

    #: A constant which can be used with the status property of a HistorySummary.
    #: This constant has a value of "POSTPONED"
    STATUS_POSTPONED = "POSTPONED"

    #: A constant which can be used with the status property of a HistorySummary.
    #: This constant has a value of "IMPLEMENTED"
    STATUS_IMPLEMENTED = "IMPLEMENTED"

    def __init__(self, **kwargs):
        """
        Initializes a new HistorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this HistorySummary.
        :type id: str

        :param name:
            The value to assign to the name property of this HistorySummary.
        :type name: str

        :param resource_type:
            The value to assign to the resource_type property of this HistorySummary.
        :type resource_type: str

        :param category_id:
            The value to assign to the category_id property of this HistorySummary.
        :type category_id: str

        :param recommendation_id:
            The value to assign to the recommendation_id property of this HistorySummary.
        :type recommendation_id: str

        :param recommendation_name:
            The value to assign to the recommendation_name property of this HistorySummary.
        :type recommendation_name: str

        :param resource_id:
            The value to assign to the resource_id property of this HistorySummary.
        :type resource_id: str

        :param resource_action_id:
            The value to assign to the resource_action_id property of this HistorySummary.
        :type resource_action_id: str

        :param action:
            The value to assign to the action property of this HistorySummary.
        :type action: oci.optimizer.models.Action

        :param compartment_id:
            The value to assign to the compartment_id property of this HistorySummary.
        :type compartment_id: str

        :param compartment_name:
            The value to assign to the compartment_name property of this HistorySummary.
        :type compartment_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this HistorySummary.
            Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param estimated_cost_saving:
            The value to assign to the estimated_cost_saving property of this HistorySummary.
        :type estimated_cost_saving: float

        :param status:
            The value to assign to the status property of this HistorySummary.
            Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param metadata:
            The value to assign to the metadata property of this HistorySummary.
        :type metadata: dict(str, str)

        :param extended_metadata:
            The value to assign to the extended_metadata property of this HistorySummary.
        :type extended_metadata: dict(str, object)

        :param time_created:
            The value to assign to the time_created property of this HistorySummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'resource_type': 'str',
            'category_id': 'str',
            'recommendation_id': 'str',
            'recommendation_name': 'str',
            'resource_id': 'str',
            'resource_action_id': 'str',
            'action': 'Action',
            'compartment_id': 'str',
            'compartment_name': 'str',
            'lifecycle_state': 'str',
            'estimated_cost_saving': 'float',
            'status': 'str',
            'metadata': 'dict(str, str)',
            'extended_metadata': 'dict(str, object)',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'resource_type': 'resourceType',
            'category_id': 'categoryId',
            'recommendation_id': 'recommendationId',
            'recommendation_name': 'recommendationName',
            'resource_id': 'resourceId',
            'resource_action_id': 'resourceActionId',
            'action': 'action',
            'compartment_id': 'compartmentId',
            'compartment_name': 'compartmentName',
            'lifecycle_state': 'lifecycleState',
            'estimated_cost_saving': 'estimatedCostSaving',
            'status': 'status',
            'metadata': 'metadata',
            'extended_metadata': 'extendedMetadata',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._name = None
        self._resource_type = None
        self._category_id = None
        self._recommendation_id = None
        self._recommendation_name = None
        self._resource_id = None
        self._resource_action_id = None
        self._action = None
        self._compartment_id = None
        self._compartment_name = None
        self._lifecycle_state = None
        self._estimated_cost_saving = None
        self._status = None
        self._metadata = None
        self._extended_metadata = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this HistorySummary.
        The unique OCID associated with the recommendation history.


        :return: The id of this HistorySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HistorySummary.
        The unique OCID associated with the recommendation history.


        :param id: The id of this HistorySummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this HistorySummary.
        The name assigned to the resource.


        :return: The name of this HistorySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HistorySummary.
        The name assigned to the resource.


        :param name: The name of this HistorySummary.
        :type: str
        """
        self._name = name

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this HistorySummary.
        The kind of resource.


        :return: The resource_type of this HistorySummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this HistorySummary.
        The kind of resource.


        :param resource_type: The resource_type of this HistorySummary.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def category_id(self):
        """
        **[Required]** Gets the category_id of this HistorySummary.
        The unique OCID associated with the category.


        :return: The category_id of this HistorySummary.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this HistorySummary.
        The unique OCID associated with the category.


        :param category_id: The category_id of this HistorySummary.
        :type: str
        """
        self._category_id = category_id

    @property
    def recommendation_id(self):
        """
        **[Required]** Gets the recommendation_id of this HistorySummary.
        The unique OCID associated with the recommendation.


        :return: The recommendation_id of this HistorySummary.
        :rtype: str
        """
        return self._recommendation_id

    @recommendation_id.setter
    def recommendation_id(self, recommendation_id):
        """
        Sets the recommendation_id of this HistorySummary.
        The unique OCID associated with the recommendation.


        :param recommendation_id: The recommendation_id of this HistorySummary.
        :type: str
        """
        self._recommendation_id = recommendation_id

    @property
    def recommendation_name(self):
        """
        **[Required]** Gets the recommendation_name of this HistorySummary.
        The name assigned to the recommendation.


        :return: The recommendation_name of this HistorySummary.
        :rtype: str
        """
        return self._recommendation_name

    @recommendation_name.setter
    def recommendation_name(self, recommendation_name):
        """
        Sets the recommendation_name of this HistorySummary.
        The name assigned to the recommendation.


        :param recommendation_name: The recommendation_name of this HistorySummary.
        :type: str
        """
        self._recommendation_name = recommendation_name

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this HistorySummary.
        The unique OCID associated with the resource.


        :return: The resource_id of this HistorySummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this HistorySummary.
        The unique OCID associated with the resource.


        :param resource_id: The resource_id of this HistorySummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_action_id(self):
        """
        **[Required]** Gets the resource_action_id of this HistorySummary.
        The unique OCID associated with the resource action.


        :return: The resource_action_id of this HistorySummary.
        :rtype: str
        """
        return self._resource_action_id

    @resource_action_id.setter
    def resource_action_id(self, resource_action_id):
        """
        Sets the resource_action_id of this HistorySummary.
        The unique OCID associated with the resource action.


        :param resource_action_id: The resource_action_id of this HistorySummary.
        :type: str
        """
        self._resource_action_id = resource_action_id

    @property
    def action(self):
        """
        **[Required]** Gets the action of this HistorySummary.

        :return: The action of this HistorySummary.
        :rtype: oci.optimizer.models.Action
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this HistorySummary.

        :param action: The action of this HistorySummary.
        :type: oci.optimizer.models.Action
        """
        self._action = action

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this HistorySummary.
        The OCID of the compartment.


        :return: The compartment_id of this HistorySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this HistorySummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this HistorySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compartment_name(self):
        """
        **[Required]** Gets the compartment_name of this HistorySummary.
        The name assigned to the compartment.


        :return: The compartment_name of this HistorySummary.
        :rtype: str
        """
        return self._compartment_name

    @compartment_name.setter
    def compartment_name(self, compartment_name):
        """
        Sets the compartment_name of this HistorySummary.
        The name assigned to the compartment.


        :param compartment_name: The compartment_name of this HistorySummary.
        :type: str
        """
        self._compartment_name = compartment_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this HistorySummary.
        The recommendation history's current state.

        Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this HistorySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this HistorySummary.
        The recommendation history's current state.


        :param lifecycle_state: The lifecycle_state of this HistorySummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def estimated_cost_saving(self):
        """
        **[Required]** Gets the estimated_cost_saving of this HistorySummary.
        The estimated cost savings, in dollars, for the resource action.


        :return: The estimated_cost_saving of this HistorySummary.
        :rtype: float
        """
        return self._estimated_cost_saving

    @estimated_cost_saving.setter
    def estimated_cost_saving(self, estimated_cost_saving):
        """
        Sets the estimated_cost_saving of this HistorySummary.
        The estimated cost savings, in dollars, for the resource action.


        :param estimated_cost_saving: The estimated_cost_saving of this HistorySummary.
        :type: float
        """
        self._estimated_cost_saving = estimated_cost_saving

    @property
    def status(self):
        """
        **[Required]** Gets the status of this HistorySummary.
        The current status of the resource action.

        Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this HistorySummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this HistorySummary.
        The current status of the resource action.


        :param status: The status of this HistorySummary.
        :type: str
        """
        allowed_values = ["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def metadata(self):
        """
        Gets the metadata of this HistorySummary.
        Custom metadata key/value pairs for the resource action.

         **Metadata Example**

              \"metadata\" : {
                 \"cpuRecommendedShape\": \"VM.Standard1.1\",
                 \"computeMemoryUtilization\": \"26.05734124418388\",
                 \"currentShape\": \"VM.Standard1.2\",
                 \"instanceRecommendedShape\": \"VM.Standard1.1\",
                 \"computeCpuUtilization\": \"7.930035319720132\",
                 \"memoryRecommendedShape\": \"None\"
              }


        :return: The metadata of this HistorySummary.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this HistorySummary.
        Custom metadata key/value pairs for the resource action.

         **Metadata Example**

              \"metadata\" : {
                 \"cpuRecommendedShape\": \"VM.Standard1.1\",
                 \"computeMemoryUtilization\": \"26.05734124418388\",
                 \"currentShape\": \"VM.Standard1.2\",
                 \"instanceRecommendedShape\": \"VM.Standard1.1\",
                 \"computeCpuUtilization\": \"7.930035319720132\",
                 \"memoryRecommendedShape\": \"None\"
              }


        :param metadata: The metadata of this HistorySummary.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def extended_metadata(self):
        """
        Gets the extended_metadata of this HistorySummary.
        Additional metadata key/value pairs that you provide.
        They serve the same purpose and functionality as fields in the `metadata` object.

        They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).

        For example:

        `{\"CurrentShape\": {\"name\":\"VM.Standard2.16\"}, \"RecommendedShape\": {\"name\":\"VM.Standard2.8\"}}`


        :return: The extended_metadata of this HistorySummary.
        :rtype: dict(str, object)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this HistorySummary.
        Additional metadata key/value pairs that you provide.
        They serve the same purpose and functionality as fields in the `metadata` object.

        They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).

        For example:

        `{\"CurrentShape\": {\"name\":\"VM.Standard2.16\"}, \"RecommendedShape\": {\"name\":\"VM.Standard2.8\"}}`


        :param extended_metadata: The extended_metadata of this HistorySummary.
        :type: dict(str, object)
        """
        self._extended_metadata = extended_metadata

    @property
    def time_created(self):
        """
        Gets the time_created of this HistorySummary.
        The date and time the recommendation history was created, in the format defined by RFC3339.


        :return: The time_created of this HistorySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HistorySummary.
        The date and time the recommendation history was created, in the format defined by RFC3339.


        :param time_created: The time_created of this HistorySummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
