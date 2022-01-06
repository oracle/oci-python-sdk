# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackendHealth(object):
    """
    The health status of the specified backend server as reported by the primary and standby load balancers.
    """

    #: A constant which can be used with the status property of a BackendHealth.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    #: A constant which can be used with the status property of a BackendHealth.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the status property of a BackendHealth.
    #: This constant has a value of "CRITICAL"
    STATUS_CRITICAL = "CRITICAL"

    #: A constant which can be used with the status property of a BackendHealth.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new BackendHealth object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this BackendHealth.
            Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param health_check_results:
            The value to assign to the health_check_results property of this BackendHealth.
        :type health_check_results: list[oci.load_balancer.models.HealthCheckResult]

        """
        self.swagger_types = {
            'status': 'str',
            'health_check_results': 'list[HealthCheckResult]'
        }

        self.attribute_map = {
            'status': 'status',
            'health_check_results': 'healthCheckResults'
        }

        self._status = None
        self._health_check_results = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this BackendHealth.
        The general health status of the specified backend server as reported by the primary and standby load balancers.

        *   **OK:** Both health checks returned `OK`.

        *   **WARNING:** One health check returned `OK` and one did not.

        *   **CRITICAL:** Neither health check returned `OK`.

        *   **UNKNOWN:** One or both health checks returned `UNKNOWN`, or the system was unable to retrieve metrics at this time.

        Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this BackendHealth.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BackendHealth.
        The general health status of the specified backend server as reported by the primary and standby load balancers.

        *   **OK:** Both health checks returned `OK`.

        *   **WARNING:** One health check returned `OK` and one did not.

        *   **CRITICAL:** Neither health check returned `OK`.

        *   **UNKNOWN:** One or both health checks returned `UNKNOWN`, or the system was unable to retrieve metrics at this time.


        :param status: The status of this BackendHealth.
        :type: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def health_check_results(self):
        """
        **[Required]** Gets the health_check_results of this BackendHealth.
        A list of the most recent health check results returned for the specified backend server.


        :return: The health_check_results of this BackendHealth.
        :rtype: list[oci.load_balancer.models.HealthCheckResult]
        """
        return self._health_check_results

    @health_check_results.setter
    def health_check_results(self, health_check_results):
        """
        Sets the health_check_results of this BackendHealth.
        A list of the most recent health check results returned for the specified backend server.


        :param health_check_results: The health_check_results of this BackendHealth.
        :type: list[oci.load_balancer.models.HealthCheckResult]
        """
        self._health_check_results = health_check_results

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
