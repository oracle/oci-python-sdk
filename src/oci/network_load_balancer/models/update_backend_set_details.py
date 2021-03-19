# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBackendSetDetails(object):
    """
    The configuration details for updating a load balancer backend set.
    For more information about backend set configuration, see
    `Managing Backend Sets`__.

    **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingbackendsets.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBackendSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this UpdateBackendSetDetails.
        :type policy: str

        :param is_preserve_source:
            The value to assign to the is_preserve_source property of this UpdateBackendSetDetails.
        :type is_preserve_source: bool

        :param backends:
            The value to assign to the backends property of this UpdateBackendSetDetails.
        :type backends: list[oci.network_load_balancer.models.BackendDetails]

        :param health_checker:
            The value to assign to the health_checker property of this UpdateBackendSetDetails.
        :type health_checker: oci.network_load_balancer.models.HealthCheckerDetails

        """
        self.swagger_types = {
            'policy': 'str',
            'is_preserve_source': 'bool',
            'backends': 'list[BackendDetails]',
            'health_checker': 'HealthCheckerDetails'
        }

        self.attribute_map = {
            'policy': 'policy',
            'is_preserve_source': 'isPreserveSource',
            'backends': 'backends',
            'health_checker': 'healthChecker'
        }

        self._policy = None
        self._is_preserve_source = None
        self._backends = None
        self._health_checker = None

    @property
    def policy(self):
        """
        Gets the policy of this UpdateBackendSetDetails.
        The network load balancer policy for the backend set. To get a list of available policies, use the
        :func:`list_network_load_balancers_policies` operation.

        Example: `FIVE_TUPLE`


        :return: The policy of this UpdateBackendSetDetails.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this UpdateBackendSetDetails.
        The network load balancer policy for the backend set. To get a list of available policies, use the
        :func:`list_network_load_balancers_policies` operation.

        Example: `FIVE_TUPLE`


        :param policy: The policy of this UpdateBackendSetDetails.
        :type: str
        """
        self._policy = policy

    @property
    def is_preserve_source(self):
        """
        Gets the is_preserve_source of this UpdateBackendSetDetails.
        If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
        Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled.
        The value is true by default.


        :return: The is_preserve_source of this UpdateBackendSetDetails.
        :rtype: bool
        """
        return self._is_preserve_source

    @is_preserve_source.setter
    def is_preserve_source(self, is_preserve_source):
        """
        Sets the is_preserve_source of this UpdateBackendSetDetails.
        If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
        Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled.
        The value is true by default.


        :param is_preserve_source: The is_preserve_source of this UpdateBackendSetDetails.
        :type: bool
        """
        self._is_preserve_source = is_preserve_source

    @property
    def backends(self):
        """
        Gets the backends of this UpdateBackendSetDetails.
        An array of backends associated with the backend set.


        :return: The backends of this UpdateBackendSetDetails.
        :rtype: list[oci.network_load_balancer.models.BackendDetails]
        """
        return self._backends

    @backends.setter
    def backends(self, backends):
        """
        Sets the backends of this UpdateBackendSetDetails.
        An array of backends associated with the backend set.


        :param backends: The backends of this UpdateBackendSetDetails.
        :type: list[oci.network_load_balancer.models.BackendDetails]
        """
        self._backends = backends

    @property
    def health_checker(self):
        """
        Gets the health_checker of this UpdateBackendSetDetails.

        :return: The health_checker of this UpdateBackendSetDetails.
        :rtype: oci.network_load_balancer.models.HealthCheckerDetails
        """
        return self._health_checker

    @health_checker.setter
    def health_checker(self, health_checker):
        """
        Sets the health_checker of this UpdateBackendSetDetails.

        :param health_checker: The health_checker of this UpdateBackendSetDetails.
        :type: oci.network_load_balancer.models.HealthCheckerDetails
        """
        self._health_checker = health_checker

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
