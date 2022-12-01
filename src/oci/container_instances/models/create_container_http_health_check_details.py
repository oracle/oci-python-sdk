# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_container_health_check_details import CreateContainerHealthCheckDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerHttpHealthCheckDetails(CreateContainerHealthCheckDetails):
    """
    Container Health Check HTTP type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerHttpHealthCheckDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_instances.models.CreateContainerHttpHealthCheckDetails.health_check_type` attribute
        of this class is ``HTTP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateContainerHttpHealthCheckDetails.
        :type name: str

        :param health_check_type:
            The value to assign to the health_check_type property of this CreateContainerHttpHealthCheckDetails.
            Allowed values for this property are: "HTTP", "TCP", "COMMAND"
        :type health_check_type: str

        :param initial_delay_in_seconds:
            The value to assign to the initial_delay_in_seconds property of this CreateContainerHttpHealthCheckDetails.
        :type initial_delay_in_seconds: int

        :param interval_in_seconds:
            The value to assign to the interval_in_seconds property of this CreateContainerHttpHealthCheckDetails.
        :type interval_in_seconds: int

        :param failure_threshold:
            The value to assign to the failure_threshold property of this CreateContainerHttpHealthCheckDetails.
        :type failure_threshold: int

        :param success_threshold:
            The value to assign to the success_threshold property of this CreateContainerHttpHealthCheckDetails.
        :type success_threshold: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this CreateContainerHttpHealthCheckDetails.
        :type timeout_in_seconds: int

        :param failure_action:
            The value to assign to the failure_action property of this CreateContainerHttpHealthCheckDetails.
            Allowed values for this property are: "KILL", "NONE"
        :type failure_action: str

        :param path:
            The value to assign to the path property of this CreateContainerHttpHealthCheckDetails.
        :type path: str

        :param port:
            The value to assign to the port property of this CreateContainerHttpHealthCheckDetails.
        :type port: int

        :param headers:
            The value to assign to the headers property of this CreateContainerHttpHealthCheckDetails.
        :type headers: list[oci.container_instances.models.HealthCheckHttpHeader]

        """
        self.swagger_types = {
            'name': 'str',
            'health_check_type': 'str',
            'initial_delay_in_seconds': 'int',
            'interval_in_seconds': 'int',
            'failure_threshold': 'int',
            'success_threshold': 'int',
            'timeout_in_seconds': 'int',
            'failure_action': 'str',
            'path': 'str',
            'port': 'int',
            'headers': 'list[HealthCheckHttpHeader]'
        }

        self.attribute_map = {
            'name': 'name',
            'health_check_type': 'healthCheckType',
            'initial_delay_in_seconds': 'initialDelayInSeconds',
            'interval_in_seconds': 'intervalInSeconds',
            'failure_threshold': 'failureThreshold',
            'success_threshold': 'successThreshold',
            'timeout_in_seconds': 'timeoutInSeconds',
            'failure_action': 'failureAction',
            'path': 'path',
            'port': 'port',
            'headers': 'headers'
        }

        self._name = None
        self._health_check_type = None
        self._initial_delay_in_seconds = None
        self._interval_in_seconds = None
        self._failure_threshold = None
        self._success_threshold = None
        self._timeout_in_seconds = None
        self._failure_action = None
        self._path = None
        self._port = None
        self._headers = None
        self._health_check_type = 'HTTP'

    @property
    def path(self):
        """
        **[Required]** Gets the path of this CreateContainerHttpHealthCheckDetails.
        Container health check Http's path.


        :return: The path of this CreateContainerHttpHealthCheckDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this CreateContainerHttpHealthCheckDetails.
        Container health check Http's path.


        :param path: The path of this CreateContainerHttpHealthCheckDetails.
        :type: str
        """
        self._path = path

    @property
    def port(self):
        """
        **[Required]** Gets the port of this CreateContainerHttpHealthCheckDetails.
        Container health check Http's port.


        :return: The port of this CreateContainerHttpHealthCheckDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateContainerHttpHealthCheckDetails.
        Container health check Http's port.


        :param port: The port of this CreateContainerHttpHealthCheckDetails.
        :type: int
        """
        self._port = port

    @property
    def headers(self):
        """
        Gets the headers of this CreateContainerHttpHealthCheckDetails.
        Container health check Http's headers.


        :return: The headers of this CreateContainerHttpHealthCheckDetails.
        :rtype: list[oci.container_instances.models.HealthCheckHttpHeader]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this CreateContainerHttpHealthCheckDetails.
        Container health check Http's headers.


        :param headers: The headers of this CreateContainerHttpHealthCheckDetails.
        :type: list[oci.container_instances.models.HealthCheckHttpHeader]
        """
        self._headers = headers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
