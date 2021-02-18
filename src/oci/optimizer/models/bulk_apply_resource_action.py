# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkApplyResourceAction(object):
    """
    The resource action that a recommendation will be applied to.
    """

    #: A constant which can be used with the status property of a BulkApplyResourceAction.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    #: A constant which can be used with the status property of a BulkApplyResourceAction.
    #: This constant has a value of "DISMISSED"
    STATUS_DISMISSED = "DISMISSED"

    #: A constant which can be used with the status property of a BulkApplyResourceAction.
    #: This constant has a value of "POSTPONED"
    STATUS_POSTPONED = "POSTPONED"

    #: A constant which can be used with the status property of a BulkApplyResourceAction.
    #: This constant has a value of "IMPLEMENTED"
    STATUS_IMPLEMENTED = "IMPLEMENTED"

    def __init__(self, **kwargs):
        """
        Initializes a new BulkApplyResourceAction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_action_id:
            The value to assign to the resource_action_id property of this BulkApplyResourceAction.
        :type resource_action_id: str

        :param status:
            The value to assign to the status property of this BulkApplyResourceAction.
            Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"
        :type status: str

        :param time_status_end:
            The value to assign to the time_status_end property of this BulkApplyResourceAction.
        :type time_status_end: datetime

        :param parameters:
            The value to assign to the parameters property of this BulkApplyResourceAction.
        :type parameters: dict(str, object)

        :param strategy_name:
            The value to assign to the strategy_name property of this BulkApplyResourceAction.
        :type strategy_name: str

        """
        self.swagger_types = {
            'resource_action_id': 'str',
            'status': 'str',
            'time_status_end': 'datetime',
            'parameters': 'dict(str, object)',
            'strategy_name': 'str'
        }

        self.attribute_map = {
            'resource_action_id': 'resourceActionId',
            'status': 'status',
            'time_status_end': 'timeStatusEnd',
            'parameters': 'parameters',
            'strategy_name': 'strategyName'
        }

        self._resource_action_id = None
        self._status = None
        self._time_status_end = None
        self._parameters = None
        self._strategy_name = None

    @property
    def resource_action_id(self):
        """
        **[Required]** Gets the resource_action_id of this BulkApplyResourceAction.
        The unique OCIDs of the resource actions that recommendations are applied to.


        :return: The resource_action_id of this BulkApplyResourceAction.
        :rtype: str
        """
        return self._resource_action_id

    @resource_action_id.setter
    def resource_action_id(self, resource_action_id):
        """
        Sets the resource_action_id of this BulkApplyResourceAction.
        The unique OCIDs of the resource actions that recommendations are applied to.


        :param resource_action_id: The resource_action_id of this BulkApplyResourceAction.
        :type: str
        """
        self._resource_action_id = resource_action_id

    @property
    def status(self):
        """
        Gets the status of this BulkApplyResourceAction.
        The current status of the recommendation.

        Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"


        :return: The status of this BulkApplyResourceAction.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BulkApplyResourceAction.
        The current status of the recommendation.


        :param status: The status of this BulkApplyResourceAction.
        :type: str
        """
        allowed_values = ["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def time_status_end(self):
        """
        Gets the time_status_end of this BulkApplyResourceAction.
        The date and time the current status will change. The format is defined by RFC3339.

        For example, \"The current `postponed` status of the resource action will end and change to `pending` on this
        date and time.\"


        :return: The time_status_end of this BulkApplyResourceAction.
        :rtype: datetime
        """
        return self._time_status_end

    @time_status_end.setter
    def time_status_end(self, time_status_end):
        """
        Sets the time_status_end of this BulkApplyResourceAction.
        The date and time the current status will change. The format is defined by RFC3339.

        For example, \"The current `postponed` status of the resource action will end and change to `pending` on this
        date and time.\"


        :param time_status_end: The time_status_end of this BulkApplyResourceAction.
        :type: datetime
        """
        self._time_status_end = time_status_end

    @property
    def parameters(self):
        """
        Gets the parameters of this BulkApplyResourceAction.
        Additional parameter key-value pairs defining the resource action.
        For example:

        `{\"timeAmount\": 15, \"timeUnit\": \"seconds\"}`


        :return: The parameters of this BulkApplyResourceAction.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this BulkApplyResourceAction.
        Additional parameter key-value pairs defining the resource action.
        For example:

        `{\"timeAmount\": 15, \"timeUnit\": \"seconds\"}`


        :param parameters: The parameters of this BulkApplyResourceAction.
        :type: dict(str, object)
        """
        self._parameters = parameters

    @property
    def strategy_name(self):
        """
        Gets the strategy_name of this BulkApplyResourceAction.
        The name of the strategy.


        :return: The strategy_name of this BulkApplyResourceAction.
        :rtype: str
        """
        return self._strategy_name

    @strategy_name.setter
    def strategy_name(self, strategy_name):
        """
        Sets the strategy_name of this BulkApplyResourceAction.
        The name of the strategy.


        :param strategy_name: The strategy_name of this BulkApplyResourceAction.
        :type: str
        """
        self._strategy_name = strategy_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
