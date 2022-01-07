# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackendSetHealth(object):
    """
    The health status details for a backend set.

    This object does not explicitly enumerate backend servers with a status of `OK`. However, the backend sets are included in the
    `totalBackendCount` sum.
    """

    #: A constant which can be used with the status property of a BackendSetHealth.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    #: A constant which can be used with the status property of a BackendSetHealth.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the status property of a BackendSetHealth.
    #: This constant has a value of "CRITICAL"
    STATUS_CRITICAL = "CRITICAL"

    #: A constant which can be used with the status property of a BackendSetHealth.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new BackendSetHealth object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this BackendSetHealth.
            Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param warning_state_backend_names:
            The value to assign to the warning_state_backend_names property of this BackendSetHealth.
        :type warning_state_backend_names: list[str]

        :param critical_state_backend_names:
            The value to assign to the critical_state_backend_names property of this BackendSetHealth.
        :type critical_state_backend_names: list[str]

        :param unknown_state_backend_names:
            The value to assign to the unknown_state_backend_names property of this BackendSetHealth.
        :type unknown_state_backend_names: list[str]

        :param total_backend_count:
            The value to assign to the total_backend_count property of this BackendSetHealth.
        :type total_backend_count: int

        """
        self.swagger_types = {
            'status': 'str',
            'warning_state_backend_names': 'list[str]',
            'critical_state_backend_names': 'list[str]',
            'unknown_state_backend_names': 'list[str]',
            'total_backend_count': 'int'
        }

        self.attribute_map = {
            'status': 'status',
            'warning_state_backend_names': 'warningStateBackendNames',
            'critical_state_backend_names': 'criticalStateBackendNames',
            'unknown_state_backend_names': 'unknownStateBackendNames',
            'total_backend_count': 'totalBackendCount'
        }

        self._status = None
        self._warning_state_backend_names = None
        self._critical_state_backend_names = None
        self._unknown_state_backend_names = None
        self._total_backend_count = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this BackendSetHealth.
        Overall health status of the backend set.

        *  **OK:** All backend servers in the backend set return a status of `OK`.

        *  **WARNING:** Half or more of the backend servers in a backend set return a status of `OK` and at least one backend
        server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`.

        *  **CRITICAL:** Fewer than half of the backend servers in a backend set return a status of `OK`.

        *  **UNKNOWN:** If no probes have yet been sent to the backends, or the system is
        unable to retrieve metrics from the backends.

        Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this BackendSetHealth.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BackendSetHealth.
        Overall health status of the backend set.

        *  **OK:** All backend servers in the backend set return a status of `OK`.

        *  **WARNING:** Half or more of the backend servers in a backend set return a status of `OK` and at least one backend
        server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`.

        *  **CRITICAL:** Fewer than half of the backend servers in a backend set return a status of `OK`.

        *  **UNKNOWN:** If no probes have yet been sent to the backends, or the system is
        unable to retrieve metrics from the backends.


        :param status: The status of this BackendSetHealth.
        :type: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def warning_state_backend_names(self):
        """
        **[Required]** Gets the warning_state_backend_names of this BackendSetHealth.
        A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by
        IP address or OCID and port.

        Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`


        :return: The warning_state_backend_names of this BackendSetHealth.
        :rtype: list[str]
        """
        return self._warning_state_backend_names

    @warning_state_backend_names.setter
    def warning_state_backend_names(self, warning_state_backend_names):
        """
        Sets the warning_state_backend_names of this BackendSetHealth.
        A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by
        IP address or OCID and port.

        Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`


        :param warning_state_backend_names: The warning_state_backend_names of this BackendSetHealth.
        :type: list[str]
        """
        self._warning_state_backend_names = warning_state_backend_names

    @property
    def critical_state_backend_names(self):
        """
        **[Required]** Gets the critical_state_backend_names of this BackendSetHealth.
        A list of backend servers that are currently in the `CRITICAL` health state. The list identifies each backend server by
        IP address and port.

        Example: `10.0.0.4:8080`


        :return: The critical_state_backend_names of this BackendSetHealth.
        :rtype: list[str]
        """
        return self._critical_state_backend_names

    @critical_state_backend_names.setter
    def critical_state_backend_names(self, critical_state_backend_names):
        """
        Sets the critical_state_backend_names of this BackendSetHealth.
        A list of backend servers that are currently in the `CRITICAL` health state. The list identifies each backend server by
        IP address and port.

        Example: `10.0.0.4:8080`


        :param critical_state_backend_names: The critical_state_backend_names of this BackendSetHealth.
        :type: list[str]
        """
        self._critical_state_backend_names = critical_state_backend_names

    @property
    def unknown_state_backend_names(self):
        """
        **[Required]** Gets the unknown_state_backend_names of this BackendSetHealth.
        A list of backend servers that are currently in the `UNKNOWN` health state. The list identifies each backend server by
        IP address and port.

        Example: `10.0.0.5:8080`


        :return: The unknown_state_backend_names of this BackendSetHealth.
        :rtype: list[str]
        """
        return self._unknown_state_backend_names

    @unknown_state_backend_names.setter
    def unknown_state_backend_names(self, unknown_state_backend_names):
        """
        Sets the unknown_state_backend_names of this BackendSetHealth.
        A list of backend servers that are currently in the `UNKNOWN` health state. The list identifies each backend server by
        IP address and port.

        Example: `10.0.0.5:8080`


        :param unknown_state_backend_names: The unknown_state_backend_names of this BackendSetHealth.
        :type: list[str]
        """
        self._unknown_state_backend_names = unknown_state_backend_names

    @property
    def total_backend_count(self):
        """
        **[Required]** Gets the total_backend_count of this BackendSetHealth.
        The total number of backend servers in this backend set.

        Example: `7`


        :return: The total_backend_count of this BackendSetHealth.
        :rtype: int
        """
        return self._total_backend_count

    @total_backend_count.setter
    def total_backend_count(self, total_backend_count):
        """
        Sets the total_backend_count of this BackendSetHealth.
        The total number of backend servers in this backend set.

        Example: `7`


        :param total_backend_count: The total_backend_count of this BackendSetHealth.
        :type: int
        """
        self._total_backend_count = total_backend_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
