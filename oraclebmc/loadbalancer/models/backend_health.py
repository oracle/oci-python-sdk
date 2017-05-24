# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class BackendHealth(object):

    def __init__(self):

        self.swagger_types = {
            'instance_id': 'str',
            'is_healthy': 'bool',
            'last_health_check_result': 'str',
            'subnet_id': 'str',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'instance_id': 'instanceId',
            'is_healthy': 'isHealthy',
            'last_health_check_result': 'lastHealthCheckResult',
            'subnet_id': 'subnetId',
            'time_updated': 'timeUpdated'
        }

        self._instance_id = None
        self._is_healthy = None
        self._last_health_check_result = None
        self._subnet_id = None
        self._time_updated = None

    @property
    def instance_id(self):
        """
        Gets the instance_id of this BackendHealth.
        A unique identifier to be used primarily for determining same-subnet instances apart.


        :return: The instance_id of this BackendHealth.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this BackendHealth.
        A unique identifier to be used primarily for determining same-subnet instances apart.


        :param instance_id: The instance_id of this BackendHealth.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def is_healthy(self):
        """
        Gets the is_healthy of this BackendHealth.
        Interprets the healthCheckResult value to true or false.

        Example: `true`


        :return: The is_healthy of this BackendHealth.
        :rtype: bool
        """
        return self._is_healthy

    @is_healthy.setter
    def is_healthy(self, is_healthy):
        """
        Sets the is_healthy of this BackendHealth.
        Interprets the healthCheckResult value to true or false.

        Example: `true`


        :param is_healthy: The is_healthy of this BackendHealth.
        :type: bool
        """
        self._is_healthy = is_healthy

    @property
    def last_health_check_result(self):
        """
        Gets the last_health_check_result of this BackendHealth.
        The result of the last fetched health check.

        Allowed values for this property are: "OK", "INVALID_STATUS_CODE", "TIMED_OUT", "REGEX_MISMATCH", "CONNECT_FAILURE", "IO_ERROR", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_health_check_result of this BackendHealth.
        :rtype: str
        """
        return self._last_health_check_result

    @last_health_check_result.setter
    def last_health_check_result(self, last_health_check_result):
        """
        Sets the last_health_check_result of this BackendHealth.
        The result of the last fetched health check.


        :param last_health_check_result: The last_health_check_result of this BackendHealth.
        :type: str
        """
        allowed_values = ["OK", "INVALID_STATUS_CODE", "TIMED_OUT", "REGEX_MISMATCH", "CONNECT_FAILURE", "IO_ERROR", "OFFLINE"]
        if last_health_check_result not in allowed_values:
            last_health_check_result = 'UNKNOWN_ENUM_VALUE'
        self._last_health_check_result = last_health_check_result

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this BackendHealth.
        The ocid of the specific subnet that this health status comes from.


        :return: The subnet_id of this BackendHealth.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this BackendHealth.
        The ocid of the specific subnet that this health status comes from.


        :param subnet_id: The subnet_id of this BackendHealth.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BackendHealth.
        A timestamp of the last time this data was fetched.

        Example: `2016-07-11T14:58:10`


        :return: The time_updated of this BackendHealth.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BackendHealth.
        A timestamp of the last time this data was fetched.

        Example: `2016-07-11T14:58:10`


        :param time_updated: The time_updated of this BackendHealth.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
