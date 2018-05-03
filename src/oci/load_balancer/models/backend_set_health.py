# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackendSetHealth(object):
    """
    The health status details for a backend set.

    This object does not explicitly enumerate backend servers with a status of `OK`. However, they are included in the
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

        :param critical_state_backend_names:
            The value to assign to the critical_state_backend_names property of this BackendSetHealth.
        :type critical_state_backend_names: list[str]

        :param status:
            The value to assign to the status property of this BackendSetHealth.
            Allowed values for this property are: "OK", "WARNING", "CRITICAL", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param total_backend_count:
            The value to assign to the total_backend_count property of this BackendSetHealth.
        :type total_backend_count: int

        :param unknown_state_backend_names:
            The value to assign to the unknown_state_backend_names property of this BackendSetHealth.
        :type unknown_state_backend_names: list[str]

        :param warning_state_backend_names:
            The value to assign to the warning_state_backend_names property of this BackendSetHealth.
        :type warning_state_backend_names: list[str]

        """
        self.swagger_types = {
            'critical_state_backend_names': 'list[str]',
            'status': 'str',
            'total_backend_count': 'int',
            'unknown_state_backend_names': 'list[str]',
            'warning_state_backend_names': 'list[str]'
        }

        self.attribute_map = {
            'critical_state_backend_names': 'criticalStateBackendNames',
            'status': 'status',
            'total_backend_count': 'totalBackendCount',
            'unknown_state_backend_names': 'unknownStateBackendNames',
            'warning_state_backend_names': 'warningStateBackendNames'
        }

        self._critical_state_backend_names = None
        self._status = None
        self._total_backend_count = None
        self._unknown_state_backend_names = None
        self._warning_state_backend_names = None

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
    def status(self):
        """
        **[Required]** Gets the status of this BackendSetHealth.
        Overall health status of the backend set.

        *  **OK:** All backend servers in the backend set return a status of `OK`.

        *  **WARNING:** Half or more of the backend set's backend servers return a status of `OK` and at least one backend
        server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`.

        *  **CRITICAL:** Fewer than half of the backend set's backend servers return a status of `OK`.

        *  **UNKNOWN:** More than half of the backend set's backend servers return a status of `UNKNOWN`, the system was
        unable to retrieve metrics, or the backend set does not have a listener attached.

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

        *  **WARNING:** Half or more of the backend set's backend servers return a status of `OK` and at least one backend
        server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`.

        *  **CRITICAL:** Fewer than half of the backend set's backend servers return a status of `OK`.

        *  **UNKNOWN:** More than half of the backend set's backend servers return a status of `UNKNOWN`, the system was
        unable to retrieve metrics, or the backend set does not have a listener attached.


        :param status: The status of this BackendSetHealth.
        :type: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

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
    def warning_state_backend_names(self):
        """
        **[Required]** Gets the warning_state_backend_names of this BackendSetHealth.
        A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by
        IP address and port.

        Example: `10.0.0.3:8080`


        :return: The warning_state_backend_names of this BackendSetHealth.
        :rtype: list[str]
        """
        return self._warning_state_backend_names

    @warning_state_backend_names.setter
    def warning_state_backend_names(self, warning_state_backend_names):
        """
        Sets the warning_state_backend_names of this BackendSetHealth.
        A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by
        IP address and port.

        Example: `10.0.0.3:8080`


        :param warning_state_backend_names: The warning_state_backend_names of this BackendSetHealth.
        :type: list[str]
        """
        self._warning_state_backend_names = warning_state_backend_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
