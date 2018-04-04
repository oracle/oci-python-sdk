# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancerHealth(object):
    """
    The health status details for the specified load balancer.

    This object does not explicitly enumerate backend sets with a status of `OK`. However, they are included in the
    `totalBackendSetCount` sum.
    """

    #: A constant which can be used with the status property of a LoadBalancerHealth.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    #: A constant which can be used with the status property of a LoadBalancerHealth.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the status property of a LoadBalancerHealth.
    #: This constant has a value of "CRITICAL"
    STATUS_CRITICAL = "CRITICAL"

    #: A constant which can be used with the status property of a LoadBalancerHealth.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancerHealth object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param critical_state_backend_set_names:
            The value to assign to the critical_state_backend_set_names property of this LoadBalancerHealth.
        :type critical_state_backend_set_names: list[str]

        :param status:
            The value to assign to the status property of this LoadBalancerHealth.
            Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param total_backend_set_count:
            The value to assign to the total_backend_set_count property of this LoadBalancerHealth.
        :type total_backend_set_count: int

        :param unknown_state_backend_set_names:
            The value to assign to the unknown_state_backend_set_names property of this LoadBalancerHealth.
        :type unknown_state_backend_set_names: list[str]

        :param warning_state_backend_set_names:
            The value to assign to the warning_state_backend_set_names property of this LoadBalancerHealth.
        :type warning_state_backend_set_names: list[str]

        """
        self.swagger_types = {
            'critical_state_backend_set_names': 'list[str]',
            'status': 'str',
            'total_backend_set_count': 'int',
            'unknown_state_backend_set_names': 'list[str]',
            'warning_state_backend_set_names': 'list[str]'
        }

        self.attribute_map = {
            'critical_state_backend_set_names': 'criticalStateBackendSetNames',
            'status': 'status',
            'total_backend_set_count': 'totalBackendSetCount',
            'unknown_state_backend_set_names': 'unknownStateBackendSetNames',
            'warning_state_backend_set_names': 'warningStateBackendSetNames'
        }

        self._critical_state_backend_set_names = None
        self._status = None
        self._total_backend_set_count = None
        self._unknown_state_backend_set_names = None
        self._warning_state_backend_set_names = None

    @property
    def critical_state_backend_set_names(self):
        """
        **[Required]** Gets the critical_state_backend_set_names of this LoadBalancerHealth.
        A list of backend sets that are currently in the `CRITICAL` health state. The list identifies each backend set by the
        friendly name you assigned when you created it.

        Example: `My_backend_set`


        :return: The critical_state_backend_set_names of this LoadBalancerHealth.
        :rtype: list[str]
        """
        return self._critical_state_backend_set_names

    @critical_state_backend_set_names.setter
    def critical_state_backend_set_names(self, critical_state_backend_set_names):
        """
        Sets the critical_state_backend_set_names of this LoadBalancerHealth.
        A list of backend sets that are currently in the `CRITICAL` health state. The list identifies each backend set by the
        friendly name you assigned when you created it.

        Example: `My_backend_set`


        :param critical_state_backend_set_names: The critical_state_backend_set_names of this LoadBalancerHealth.
        :type: list[str]
        """
        self._critical_state_backend_set_names = critical_state_backend_set_names

    @property
    def status(self):
        """
        **[Required]** Gets the status of this LoadBalancerHealth.
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


        :return: The status of this LoadBalancerHealth.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LoadBalancerHealth.
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


        :param status: The status of this LoadBalancerHealth.
        :type: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def total_backend_set_count(self):
        """
        **[Required]** Gets the total_backend_set_count of this LoadBalancerHealth.
        The total number of backend sets associated with this load balancer.

        Example: `4`


        :return: The total_backend_set_count of this LoadBalancerHealth.
        :rtype: int
        """
        return self._total_backend_set_count

    @total_backend_set_count.setter
    def total_backend_set_count(self, total_backend_set_count):
        """
        Sets the total_backend_set_count of this LoadBalancerHealth.
        The total number of backend sets associated with this load balancer.

        Example: `4`


        :param total_backend_set_count: The total_backend_set_count of this LoadBalancerHealth.
        :type: int
        """
        self._total_backend_set_count = total_backend_set_count

    @property
    def unknown_state_backend_set_names(self):
        """
        **[Required]** Gets the unknown_state_backend_set_names of this LoadBalancerHealth.
        A list of backend sets that are currently in the `UNKNOWN` health state. The list identifies each backend set by the
        friendly name you assigned when you created it.

        Example: `Backend_set2`


        :return: The unknown_state_backend_set_names of this LoadBalancerHealth.
        :rtype: list[str]
        """
        return self._unknown_state_backend_set_names

    @unknown_state_backend_set_names.setter
    def unknown_state_backend_set_names(self, unknown_state_backend_set_names):
        """
        Sets the unknown_state_backend_set_names of this LoadBalancerHealth.
        A list of backend sets that are currently in the `UNKNOWN` health state. The list identifies each backend set by the
        friendly name you assigned when you created it.

        Example: `Backend_set2`


        :param unknown_state_backend_set_names: The unknown_state_backend_set_names of this LoadBalancerHealth.
        :type: list[str]
        """
        self._unknown_state_backend_set_names = unknown_state_backend_set_names

    @property
    def warning_state_backend_set_names(self):
        """
        **[Required]** Gets the warning_state_backend_set_names of this LoadBalancerHealth.
        A list of backend sets that are currently in the `WARNING` health state. The list identifies each backend set by the
        friendly name you assigned when you created it.

        Example: `Backend_set3`


        :return: The warning_state_backend_set_names of this LoadBalancerHealth.
        :rtype: list[str]
        """
        return self._warning_state_backend_set_names

    @warning_state_backend_set_names.setter
    def warning_state_backend_set_names(self, warning_state_backend_set_names):
        """
        Sets the warning_state_backend_set_names of this LoadBalancerHealth.
        A list of backend sets that are currently in the `WARNING` health state. The list identifies each backend set by the
        friendly name you assigned when you created it.

        Example: `Backend_set3`


        :param warning_state_backend_set_names: The warning_state_backend_set_names of this LoadBalancerHealth.
        :type: list[str]
        """
        self._warning_state_backend_set_names = warning_state_backend_set_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
