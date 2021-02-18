# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkApplyRecommendationsDetails(object):
    """
    Details about bulk recommendation actions.
    """

    #: A constant which can be used with the status property of a BulkApplyRecommendationsDetails.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    #: A constant which can be used with the status property of a BulkApplyRecommendationsDetails.
    #: This constant has a value of "DISMISSED"
    STATUS_DISMISSED = "DISMISSED"

    #: A constant which can be used with the status property of a BulkApplyRecommendationsDetails.
    #: This constant has a value of "POSTPONED"
    STATUS_POSTPONED = "POSTPONED"

    #: A constant which can be used with the status property of a BulkApplyRecommendationsDetails.
    #: This constant has a value of "IMPLEMENTED"
    STATUS_IMPLEMENTED = "IMPLEMENTED"

    def __init__(self, **kwargs):
        """
        Initializes a new BulkApplyRecommendationsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_action_ids:
            The value to assign to the resource_action_ids property of this BulkApplyRecommendationsDetails.
        :type resource_action_ids: list[str]

        :param actions:
            The value to assign to the actions property of this BulkApplyRecommendationsDetails.
        :type actions: list[oci.optimizer.models.BulkApplyResourceAction]

        :param status:
            The value to assign to the status property of this BulkApplyRecommendationsDetails.
            Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"
        :type status: str

        :param time_status_end:
            The value to assign to the time_status_end property of this BulkApplyRecommendationsDetails.
        :type time_status_end: datetime

        """
        self.swagger_types = {
            'resource_action_ids': 'list[str]',
            'actions': 'list[BulkApplyResourceAction]',
            'status': 'str',
            'time_status_end': 'datetime'
        }

        self.attribute_map = {
            'resource_action_ids': 'resourceActionIds',
            'actions': 'actions',
            'status': 'status',
            'time_status_end': 'timeStatusEnd'
        }

        self._resource_action_ids = None
        self._actions = None
        self._status = None
        self._time_status_end = None

    @property
    def resource_action_ids(self):
        """
        Gets the resource_action_ids of this BulkApplyRecommendationsDetails.
        The unique OCIDs of the resource actions that recommendations are applied to.

        This field is deprecated.


        :return: The resource_action_ids of this BulkApplyRecommendationsDetails.
        :rtype: list[str]
        """
        return self._resource_action_ids

    @resource_action_ids.setter
    def resource_action_ids(self, resource_action_ids):
        """
        Sets the resource_action_ids of this BulkApplyRecommendationsDetails.
        The unique OCIDs of the resource actions that recommendations are applied to.

        This field is deprecated.


        :param resource_action_ids: The resource_action_ids of this BulkApplyRecommendationsDetails.
        :type: list[str]
        """
        self._resource_action_ids = resource_action_ids

    @property
    def actions(self):
        """
        Gets the actions of this BulkApplyRecommendationsDetails.
        The unique resource actions that recommendations are applied to.


        :return: The actions of this BulkApplyRecommendationsDetails.
        :rtype: list[oci.optimizer.models.BulkApplyResourceAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this BulkApplyRecommendationsDetails.
        The unique resource actions that recommendations are applied to.


        :param actions: The actions of this BulkApplyRecommendationsDetails.
        :type: list[oci.optimizer.models.BulkApplyResourceAction]
        """
        self._actions = actions

    @property
    def status(self):
        """
        **[Required]** Gets the status of this BulkApplyRecommendationsDetails.
        The current status of the recommendation.

        Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"


        :return: The status of this BulkApplyRecommendationsDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BulkApplyRecommendationsDetails.
        The current status of the recommendation.


        :param status: The status of this BulkApplyRecommendationsDetails.
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
        Gets the time_status_end of this BulkApplyRecommendationsDetails.
        The date and time the current status will change. The format is defined by RFC3339.

        For example, \"The current `postponed` status of the resource action will end and change to `pending` on this
        date and time.\"


        :return: The time_status_end of this BulkApplyRecommendationsDetails.
        :rtype: datetime
        """
        return self._time_status_end

    @time_status_end.setter
    def time_status_end(self, time_status_end):
        """
        Sets the time_status_end of this BulkApplyRecommendationsDetails.
        The date and time the current status will change. The format is defined by RFC3339.

        For example, \"The current `postponed` status of the resource action will end and change to `pending` on this
        date and time.\"


        :param time_status_end: The time_status_end of this BulkApplyRecommendationsDetails.
        :type: datetime
        """
        self._time_status_end = time_status_end

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
