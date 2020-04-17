# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancerHealthSummary(object):
    """
    A health status summary for the specified load balancer.
    """

    #: A constant which can be used with the status property of a LoadBalancerHealthSummary.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    #: A constant which can be used with the status property of a LoadBalancerHealthSummary.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the status property of a LoadBalancerHealthSummary.
    #: This constant has a value of "CRITICAL"
    STATUS_CRITICAL = "CRITICAL"

    #: A constant which can be used with the status property of a LoadBalancerHealthSummary.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancerHealthSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this LoadBalancerHealthSummary.
        :type load_balancer_id: str

        :param status:
            The value to assign to the status property of this LoadBalancerHealthSummary.
            Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'load_balancer_id': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'load_balancer_id': 'loadBalancerId',
            'status': 'status'
        }

        self._load_balancer_id = None
        self._status = None

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this LoadBalancerHealthSummary.
        The `OCID`__ of the load balancer the health status is associated with.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The load_balancer_id of this LoadBalancerHealthSummary.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this LoadBalancerHealthSummary.
        The `OCID`__ of the load balancer the health status is associated with.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param load_balancer_id: The load_balancer_id of this LoadBalancerHealthSummary.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this LoadBalancerHealthSummary.
        The overall health status of the load balancer.

        *  **OK:** All backend sets associated with the load balancer return a status of `OK`.

        *  **WARNING:** At least one of the backend sets associated with the load balancer returns a status of `WARNING`,
        no backend sets return a status of `CRITICAL`, and the load balancer life cycle state is `ACTIVE`.

        *  **CRITICAL:** One or more of the backend sets associated with the load balancer return a status of `CRITICAL`.

        *  **UNKNOWN:** If any one of the following conditions is true:

            *  The load balancer life cycle state is not `ACTIVE`.

            *  No backend sets are defined for the load balancer.

            *  More than half of the backend sets associated with the load balancer return a status of `UNKNOWN`, none of the backend
               sets return a status of `WARNING` or `CRITICAL`, and the load balancer life cycle state is `ACTIVE`.

            *  The system could not retrieve metrics for any reason.

        Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this LoadBalancerHealthSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LoadBalancerHealthSummary.
        The overall health status of the load balancer.

        *  **OK:** All backend sets associated with the load balancer return a status of `OK`.

        *  **WARNING:** At least one of the backend sets associated with the load balancer returns a status of `WARNING`,
        no backend sets return a status of `CRITICAL`, and the load balancer life cycle state is `ACTIVE`.

        *  **CRITICAL:** One or more of the backend sets associated with the load balancer return a status of `CRITICAL`.

        *  **UNKNOWN:** If any one of the following conditions is true:

            *  The load balancer life cycle state is not `ACTIVE`.

            *  No backend sets are defined for the load balancer.

            *  More than half of the backend sets associated with the load balancer return a status of `UNKNOWN`, none of the backend
               sets return a status of `WARNING` or `CRITICAL`, and the load balancer life cycle state is `ACTIVE`.

            *  The system could not retrieve metrics for any reason.


        :param status: The status of this LoadBalancerHealthSummary.
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
