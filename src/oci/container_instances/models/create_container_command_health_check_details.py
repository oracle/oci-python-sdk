# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210415

from .create_container_health_check_details import CreateContainerHealthCheckDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerCommandHealthCheckDetails(CreateContainerHealthCheckDetails):
    """
    Container Health Check Command type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerCommandHealthCheckDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_instances.models.CreateContainerCommandHealthCheckDetails.health_check_type` attribute
        of this class is ``COMMAND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateContainerCommandHealthCheckDetails.
        :type name: str

        :param health_check_type:
            The value to assign to the health_check_type property of this CreateContainerCommandHealthCheckDetails.
            Allowed values for this property are: "HTTP", "TCP", "COMMAND"
        :type health_check_type: str

        :param initial_delay_in_seconds:
            The value to assign to the initial_delay_in_seconds property of this CreateContainerCommandHealthCheckDetails.
        :type initial_delay_in_seconds: int

        :param interval_in_seconds:
            The value to assign to the interval_in_seconds property of this CreateContainerCommandHealthCheckDetails.
        :type interval_in_seconds: int

        :param failure_threshold:
            The value to assign to the failure_threshold property of this CreateContainerCommandHealthCheckDetails.
        :type failure_threshold: int

        :param success_threshold:
            The value to assign to the success_threshold property of this CreateContainerCommandHealthCheckDetails.
        :type success_threshold: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this CreateContainerCommandHealthCheckDetails.
        :type timeout_in_seconds: int

        :param failure_action:
            The value to assign to the failure_action property of this CreateContainerCommandHealthCheckDetails.
            Allowed values for this property are: "KILL", "NONE"
        :type failure_action: str

        :param command:
            The value to assign to the command property of this CreateContainerCommandHealthCheckDetails.
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
        self._failure_action = None
        self._command = None
        self._health_check_type = 'COMMAND'

    @property
    def command(self):
        """
        **[Required]** Gets the command of this CreateContainerCommandHealthCheckDetails.
        The list of strings that will be simplified to a single command for checking the status of the container.


        :return: The command of this CreateContainerCommandHealthCheckDetails.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this CreateContainerCommandHealthCheckDetails.
        The list of strings that will be simplified to a single command for checking the status of the container.


        :param command: The command of this CreateContainerCommandHealthCheckDetails.
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
