# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkLoadBalancerHealthSummary(object):
    """
    A health status summary for the specified network load balancer
    """

    #: A constant which can be used with the status property of a NetworkLoadBalancerHealthSummary.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    #: A constant which can be used with the status property of a NetworkLoadBalancerHealthSummary.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the status property of a NetworkLoadBalancerHealthSummary.
    #: This constant has a value of "CRITICAL"
    STATUS_CRITICAL = "CRITICAL"

    #: A constant which can be used with the status property of a NetworkLoadBalancerHealthSummary.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkLoadBalancerHealthSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_load_balancer_id:
            The value to assign to the network_load_balancer_id property of this NetworkLoadBalancerHealthSummary.
        :type network_load_balancer_id: str

        :param status:
            The value to assign to the status property of this NetworkLoadBalancerHealthSummary.
            Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'network_load_balancer_id': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'network_load_balancer_id': 'networkLoadBalancerId',
            'status': 'status'
        }

        self._network_load_balancer_id = None
        self._status = None

    @property
    def network_load_balancer_id(self):
        """
        **[Required]** Gets the network_load_balancer_id of this NetworkLoadBalancerHealthSummary.
        The `OCID`__ of the network load balancer with which the health status is associated.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The network_load_balancer_id of this NetworkLoadBalancerHealthSummary.
        :rtype: str
        """
        return self._network_load_balancer_id

    @network_load_balancer_id.setter
    def network_load_balancer_id(self, network_load_balancer_id):
        """
        Sets the network_load_balancer_id of this NetworkLoadBalancerHealthSummary.
        The `OCID`__ of the network load balancer with which the health status is associated.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param network_load_balancer_id: The network_load_balancer_id of this NetworkLoadBalancerHealthSummary.
        :type: str
        """
        self._network_load_balancer_id = network_load_balancer_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this NetworkLoadBalancerHealthSummary.
        The overall health status of the network load balancer.

        *  **OK:** All backend sets associated with the network load balancer return a status of `OK`.

        *  **WARNING:** At least one of the backend sets associated with the network load balancer returns a status of `WARNING`,
        no backend sets return a status of `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`.

        *  **CRITICAL:** One or more of the backend sets associated with the network load balancer returns a status of `CRITICAL`.

        *  **UNKNOWN:** If any one of the following conditions is true:

            *  The network load balancer life cycle state is not `ACTIVE`.

            *  No backend sets are defined for the network load balancer.

            *  More than half of the backend sets associated with the network load balancer return a status of `UNKNOWN`, none of the backend
               sets returns a status of `WARNING` or `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`.

            *  The system could not retrieve metrics for any reason.

        Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this NetworkLoadBalancerHealthSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NetworkLoadBalancerHealthSummary.
        The overall health status of the network load balancer.

        *  **OK:** All backend sets associated with the network load balancer return a status of `OK`.

        *  **WARNING:** At least one of the backend sets associated with the network load balancer returns a status of `WARNING`,
        no backend sets return a status of `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`.

        *  **CRITICAL:** One or more of the backend sets associated with the network load balancer returns a status of `CRITICAL`.

        *  **UNKNOWN:** If any one of the following conditions is true:

            *  The network load balancer life cycle state is not `ACTIVE`.

            *  No backend sets are defined for the network load balancer.

            *  More than half of the backend sets associated with the network load balancer return a status of `UNKNOWN`, none of the backend
               sets returns a status of `WARNING` or `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`.

            *  The system could not retrieve metrics for any reason.


        :param status: The status of this NetworkLoadBalancerHealthSummary.
        :type: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
