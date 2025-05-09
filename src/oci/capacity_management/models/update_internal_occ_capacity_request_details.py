# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInternalOccCapacityRequestDetails(object):
    """
    The details required for making an internal API update call for the capacity requests.
    """

    #: A constant which can be used with the request_state property of a UpdateInternalOccCapacityRequestDetails.
    #: This constant has a value of "RESOLVED"
    REQUEST_STATE_RESOLVED = "RESOLVED"

    #: A constant which can be used with the request_state property of a UpdateInternalOccCapacityRequestDetails.
    #: This constant has a value of "REJECTED"
    REQUEST_STATE_REJECTED = "REJECTED"

    #: A constant which can be used with the request_state property of a UpdateInternalOccCapacityRequestDetails.
    #: This constant has a value of "IN_PROGRESS"
    REQUEST_STATE_IN_PROGRESS = "IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInternalOccCapacityRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param request_state:
            The value to assign to the request_state property of this UpdateInternalOccCapacityRequestDetails.
            Allowed values for this property are: "RESOLVED", "REJECTED", "IN_PROGRESS"
        :type request_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this UpdateInternalOccCapacityRequestDetails.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'request_state': 'str',
            'lifecycle_details': 'str'
        }
        self.attribute_map = {
            'request_state': 'requestState',
            'lifecycle_details': 'lifecycleDetails'
        }
        self._request_state = None
        self._lifecycle_details = None

    @property
    def request_state(self):
        """
        Gets the request_state of this UpdateInternalOccCapacityRequestDetails.
        The subset of request states available internally for updating the capacity request.

        Allowed values for this property are: "RESOLVED", "REJECTED", "IN_PROGRESS"


        :return: The request_state of this UpdateInternalOccCapacityRequestDetails.
        :rtype: str
        """
        return self._request_state

    @request_state.setter
    def request_state(self, request_state):
        """
        Sets the request_state of this UpdateInternalOccCapacityRequestDetails.
        The subset of request states available internally for updating the capacity request.


        :param request_state: The request_state of this UpdateInternalOccCapacityRequestDetails.
        :type: str
        """
        allowed_values = ["RESOLVED", "REJECTED", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(request_state, allowed_values):
            raise ValueError(
                f"Invalid value for `request_state`, must be None or one of {allowed_values}"
            )
        self._request_state = request_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this UpdateInternalOccCapacityRequestDetails.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :return: The lifecycle_details of this UpdateInternalOccCapacityRequestDetails.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this UpdateInternalOccCapacityRequestDetails.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :param lifecycle_details: The lifecycle_details of this UpdateInternalOccCapacityRequestDetails.
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
