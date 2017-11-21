# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HealthCheckResult(object):

    def __init__(self, **kwargs):
        """
        Initializes a new HealthCheckResult object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param health_check_status:
            The value to assign to the health_check_status property of this HealthCheckResult.
            Allowed values for this property are: "OK", "INVALID_STATUS_CODE", "TIMED_OUT", "REGEX_MISMATCH", "CONNECT_FAILED", "IO_ERROR", "OFFLINE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type health_check_status: str

        :param source_ip_address:
            The value to assign to the source_ip_address property of this HealthCheckResult.
        :type source_ip_address: str

        :param subnet_id:
            The value to assign to the subnet_id property of this HealthCheckResult.
        :type subnet_id: str

        :param timestamp:
            The value to assign to the timestamp property of this HealthCheckResult.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'health_check_status': 'str',
            'source_ip_address': 'str',
            'subnet_id': 'str',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'health_check_status': 'healthCheckStatus',
            'source_ip_address': 'sourceIpAddress',
            'subnet_id': 'subnetId',
            'timestamp': 'timestamp'
        }

        self._health_check_status = None
        self._source_ip_address = None
        self._subnet_id = None
        self._timestamp = None

    @property
    def health_check_status(self):
        """
        Gets the health_check_status of this HealthCheckResult.
        The result of the most recent health check.

        Allowed values for this property are: "OK", "INVALID_STATUS_CODE", "TIMED_OUT", "REGEX_MISMATCH", "CONNECT_FAILED", "IO_ERROR", "OFFLINE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The health_check_status of this HealthCheckResult.
        :rtype: str
        """
        return self._health_check_status

    @health_check_status.setter
    def health_check_status(self, health_check_status):
        """
        Sets the health_check_status of this HealthCheckResult.
        The result of the most recent health check.


        :param health_check_status: The health_check_status of this HealthCheckResult.
        :type: str
        """
        allowed_values = ["OK", "INVALID_STATUS_CODE", "TIMED_OUT", "REGEX_MISMATCH", "CONNECT_FAILED", "IO_ERROR", "OFFLINE", "UNKNOWN"]
        if health_check_status not in allowed_values:
            health_check_status = 'UNKNOWN_ENUM_VALUE'
        self._health_check_status = health_check_status

    @property
    def source_ip_address(self):
        """
        Gets the source_ip_address of this HealthCheckResult.
        The IP address of the health check status report provider. This identifier helps you differentiate same-subnet
        (private) load balancers that report health check status.

        Example: `10.2.0.1`


        :return: The source_ip_address of this HealthCheckResult.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """
        Sets the source_ip_address of this HealthCheckResult.
        The IP address of the health check status report provider. This identifier helps you differentiate same-subnet
        (private) load balancers that report health check status.

        Example: `10.2.0.1`


        :param source_ip_address: The source_ip_address of this HealthCheckResult.
        :type: str
        """
        self._source_ip_address = source_ip_address

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this HealthCheckResult.
        The OCID of the subnet hosting the load balancer that reported this health check status.


        :return: The subnet_id of this HealthCheckResult.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this HealthCheckResult.
        The OCID of the subnet hosting the load balancer that reported this health check status.


        :param subnet_id: The subnet_id of this HealthCheckResult.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def timestamp(self):
        """
        Gets the timestamp of this HealthCheckResult.
        The date and time the data was retrieved, in the format defined by RFC3339.

        Example: `2017-06-02T18:28:11+00:00`


        :return: The timestamp of this HealthCheckResult.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this HealthCheckResult.
        The date and time the data was retrieved, in the format defined by RFC3339.

        Example: `2017-06-02T18:28:11+00:00`


        :param timestamp: The timestamp of this HealthCheckResult.
        :type: datetime
        """
        self._timestamp = timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
