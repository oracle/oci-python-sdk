# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .container_health_check import ContainerHealthCheck
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerCommandHealthCheck(ContainerHealthCheck):
    """
    Container Health Check with command type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerCommandHealthCheck object with values from keyword arguments. The default value of the :py:attr:`~oci.container_instances.models.ContainerCommandHealthCheck.health_check_type` attribute
        of this class is ``COMMAND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ContainerCommandHealthCheck.
        :type name: str

        :param health_check_type:
            The value to assign to the health_check_type property of this ContainerCommandHealthCheck.
            Allowed values for this property are: "HTTP", "TCP", "COMMAND"
        :type health_check_type: str

        :param initial_delay_in_seconds:
            The value to assign to the initial_delay_in_seconds property of this ContainerCommandHealthCheck.
        :type initial_delay_in_seconds: int

        :param interval_in_seconds:
            The value to assign to the interval_in_seconds property of this ContainerCommandHealthCheck.
        :type interval_in_seconds: int

        :param failure_threshold:
            The value to assign to the failure_threshold property of this ContainerCommandHealthCheck.
        :type failure_threshold: int

        :param success_threshold:
            The value to assign to the success_threshold property of this ContainerCommandHealthCheck.
        :type success_threshold: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this ContainerCommandHealthCheck.
        :type timeout_in_seconds: int

        :param status:
            The value to assign to the status property of this ContainerCommandHealthCheck.
            Allowed values for this property are: "HEALTHY", "UNHEALTHY", "UNKNOWN"
        :type status: str

        :param status_details:
            The value to assign to the status_details property of this ContainerCommandHealthCheck.
        :type status_details: str

        :param failure_action:
            The value to assign to the failure_action property of this ContainerCommandHealthCheck.
            Allowed values for this property are: "KILL", "NONE"
        :type failure_action: str

        :param command:
            The value to assign to the command property of this ContainerCommandHealthCheck.
        :type command: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'health_check_type': 'str',
            'initial_delay_in_seconds': 'int',
            'interval_in_seconds': 'int',
            'failure_threshold': 'int',
            'success_threshold': 'int',
            'timeout_in_seconds': 'int',
            'status': 'str',
            'status_details': 'str',
            'failure_action': 'str',
            'command': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'health_check_type': 'healthCheckType',
            'initial_delay_in_seconds': 'initialDelayInSeconds',
            'interval_in_seconds': 'intervalInSeconds',
            'failure_threshold': 'failureThreshold',
            'success_threshold': 'successThreshold',
            'timeout_in_seconds': 'timeoutInSeconds',
            'status': 'status',
            'status_details': 'statusDetails',
            'failure_action': 'failureAction',
            'command': 'command'
        }

        self._name = None
        self._health_check_type = None
        self._initial_delay_in_seconds = None
        self._interval_in_seconds = None
        self._failure_threshold = None
        self._success_threshold = None
        self._timeout_in_seconds = None
        self._status = None
        self._status_details = None
        self._failure_action = None
        self._command = None
        self._health_check_type = 'COMMAND'

    @property
    def command(self):
        """
        **[Required]** Gets the command of this ContainerCommandHealthCheck.
        The list of strings which will be concatenated to a single command for checking container's status.


        :return: The command of this ContainerCommandHealthCheck.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this ContainerCommandHealthCheck.
        The list of strings which will be concatenated to a single command for checking container's status.


        :param command: The command of this ContainerCommandHealthCheck.
        :type: list[str]
        """
        self._command = command

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
