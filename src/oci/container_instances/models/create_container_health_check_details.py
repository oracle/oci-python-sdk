# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerHealthCheckDetails(object):
    """
    Container Health Check is using for checking container status and taking appropriate actions on behalf of customers.
    """

    #: A constant which can be used with the health_check_type property of a CreateContainerHealthCheckDetails.
    #: This constant has a value of "HTTP"
    HEALTH_CHECK_TYPE_HTTP = "HTTP"

    #: A constant which can be used with the health_check_type property of a CreateContainerHealthCheckDetails.
    #: This constant has a value of "TCP"
    HEALTH_CHECK_TYPE_TCP = "TCP"

    #: A constant which can be used with the health_check_type property of a CreateContainerHealthCheckDetails.
    #: This constant has a value of "COMMAND"
    HEALTH_CHECK_TYPE_COMMAND = "COMMAND"

    #: A constant which can be used with the failure_action property of a CreateContainerHealthCheckDetails.
    #: This constant has a value of "KILL"
    FAILURE_ACTION_KILL = "KILL"

    #: A constant which can be used with the failure_action property of a CreateContainerHealthCheckDetails.
    #: This constant has a value of "NONE"
    FAILURE_ACTION_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerHealthCheckDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.container_instances.models.CreateContainerTcpHealthCheckDetails`
        * :class:`~oci.container_instances.models.CreateContainerHttpHealthCheckDetails`
        * :class:`~oci.container_instances.models.CreateContainerCommandHealthCheckDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateContainerHealthCheckDetails.
        :type name: str

        :param health_check_type:
            The value to assign to the health_check_type property of this CreateContainerHealthCheckDetails.
            Allowed values for this property are: "HTTP", "TCP", "COMMAND"
        :type health_check_type: str

        :param initial_delay_in_seconds:
            The value to assign to the initial_delay_in_seconds property of this CreateContainerHealthCheckDetails.
        :type initial_delay_in_seconds: int

        :param interval_in_seconds:
            The value to assign to the interval_in_seconds property of this CreateContainerHealthCheckDetails.
        :type interval_in_seconds: int

        :param failure_threshold:
            The value to assign to the failure_threshold property of this CreateContainerHealthCheckDetails.
        :type failure_threshold: int

        :param success_threshold:
            The value to assign to the success_threshold property of this CreateContainerHealthCheckDetails.
        :type success_threshold: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this CreateContainerHealthCheckDetails.
        :type timeout_in_seconds: int

        :param failure_action:
            The value to assign to the failure_action property of this CreateContainerHealthCheckDetails.
            Allowed values for this property are: "KILL", "NONE"
        :type failure_action: str

        """
        self.swagger_types = {
            'name': 'str',
            'health_check_type': 'str',
            'initial_delay_in_seconds': 'int',
            'interval_in_seconds': 'int',
            'failure_threshold': 'int',
            'success_threshold': 'int',
            'timeout_in_seconds': 'int',
            'failure_action': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'health_check_type': 'healthCheckType',
            'initial_delay_in_seconds': 'initialDelayInSeconds',
            'interval_in_seconds': 'intervalInSeconds',
            'failure_threshold': 'failureThreshold',
            'success_threshold': 'successThreshold',
            'timeout_in_seconds': 'timeoutInSeconds',
            'failure_action': 'failureAction'
        }

        self._name = None
        self._health_check_type = None
        self._initial_delay_in_seconds = None
        self._interval_in_seconds = None
        self._failure_threshold = None
        self._success_threshold = None
        self._timeout_in_seconds = None
        self._failure_action = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['healthCheckType']

        if type == 'TCP':
            return 'CreateContainerTcpHealthCheckDetails'

        if type == 'HTTP':
            return 'CreateContainerHttpHealthCheckDetails'

        if type == 'COMMAND':
            return 'CreateContainerCommandHealthCheckDetails'
        else:
            return 'CreateContainerHealthCheckDetails'

    @property
    def name(self):
        """
        Gets the name of this CreateContainerHealthCheckDetails.
        Health check name.


        :return: The name of this CreateContainerHealthCheckDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateContainerHealthCheckDetails.
        Health check name.


        :param name: The name of this CreateContainerHealthCheckDetails.
        :type: str
        """
        self._name = name

    @property
    def health_check_type(self):
        """
        **[Required]** Gets the health_check_type of this CreateContainerHealthCheckDetails.
        Container health check type.

        Allowed values for this property are: "HTTP", "TCP", "COMMAND"


        :return: The health_check_type of this CreateContainerHealthCheckDetails.
        :rtype: str
        """
        return self._health_check_type

    @health_check_type.setter
    def health_check_type(self, health_check_type):
        """
        Sets the health_check_type of this CreateContainerHealthCheckDetails.
        Container health check type.


        :param health_check_type: The health_check_type of this CreateContainerHealthCheckDetails.
        :type: str
        """
        allowed_values = ["HTTP", "TCP", "COMMAND"]
        if not value_allowed_none_or_none_sentinel(health_check_type, allowed_values):
            raise ValueError(
                "Invalid value for `health_check_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._health_check_type = health_check_type

    @property
    def initial_delay_in_seconds(self):
        """
        Gets the initial_delay_in_seconds of this CreateContainerHealthCheckDetails.
        The initial delay in seconds before start checking container health status.


        :return: The initial_delay_in_seconds of this CreateContainerHealthCheckDetails.
        :rtype: int
        """
        return self._initial_delay_in_seconds

    @initial_delay_in_seconds.setter
    def initial_delay_in_seconds(self, initial_delay_in_seconds):
        """
        Sets the initial_delay_in_seconds of this CreateContainerHealthCheckDetails.
        The initial delay in seconds before start checking container health status.


        :param initial_delay_in_seconds: The initial_delay_in_seconds of this CreateContainerHealthCheckDetails.
        :type: int
        """
        self._initial_delay_in_seconds = initial_delay_in_seconds

    @property
    def interval_in_seconds(self):
        """
        Gets the interval_in_seconds of this CreateContainerHealthCheckDetails.
        Number of seconds between two consecutive runs for checking container health.


        :return: The interval_in_seconds of this CreateContainerHealthCheckDetails.
        :rtype: int
        """
        return self._interval_in_seconds

    @interval_in_seconds.setter
    def interval_in_seconds(self, interval_in_seconds):
        """
        Sets the interval_in_seconds of this CreateContainerHealthCheckDetails.
        Number of seconds between two consecutive runs for checking container health.


        :param interval_in_seconds: The interval_in_seconds of this CreateContainerHealthCheckDetails.
        :type: int
        """
        self._interval_in_seconds = interval_in_seconds

    @property
    def failure_threshold(self):
        """
        Gets the failure_threshold of this CreateContainerHealthCheckDetails.
        Number of consecutive failures at which we consider the check failed.


        :return: The failure_threshold of this CreateContainerHealthCheckDetails.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """
        Sets the failure_threshold of this CreateContainerHealthCheckDetails.
        Number of consecutive failures at which we consider the check failed.


        :param failure_threshold: The failure_threshold of this CreateContainerHealthCheckDetails.
        :type: int
        """
        self._failure_threshold = failure_threshold

    @property
    def success_threshold(self):
        """
        Gets the success_threshold of this CreateContainerHealthCheckDetails.
        Number of consecutive successes at which we consider the check succeeded again after it was in failure state.


        :return: The success_threshold of this CreateContainerHealthCheckDetails.
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        """
        Sets the success_threshold of this CreateContainerHealthCheckDetails.
        Number of consecutive successes at which we consider the check succeeded again after it was in failure state.


        :param success_threshold: The success_threshold of this CreateContainerHealthCheckDetails.
        :type: int
        """
        self._success_threshold = success_threshold

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this CreateContainerHealthCheckDetails.
        Length of waiting time in seconds before marking health check failed.


        :return: The timeout_in_seconds of this CreateContainerHealthCheckDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this CreateContainerHealthCheckDetails.
        Length of waiting time in seconds before marking health check failed.


        :param timeout_in_seconds: The timeout_in_seconds of this CreateContainerHealthCheckDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def failure_action(self):
        """
        Gets the failure_action of this CreateContainerHealthCheckDetails.
        The action will be triggered when the container health check fails. There are two types of action: KILL or NONE. The default
        action is KILL. If failure action is KILL, the container will be subject to the container restart policy.

        Allowed values for this property are: "KILL", "NONE"


        :return: The failure_action of this CreateContainerHealthCheckDetails.
        :rtype: str
        """
        return self._failure_action

    @failure_action.setter
    def failure_action(self, failure_action):
        """
        Sets the failure_action of this CreateContainerHealthCheckDetails.
        The action will be triggered when the container health check fails. There are two types of action: KILL or NONE. The default
        action is KILL. If failure action is KILL, the container will be subject to the container restart policy.


        :param failure_action: The failure_action of this CreateContainerHealthCheckDetails.
        :type: str
        """
        allowed_values = ["KILL", "NONE"]
        if not value_allowed_none_or_none_sentinel(failure_action, allowed_values):
            raise ValueError(
                "Invalid value for `failure_action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._failure_action = failure_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
