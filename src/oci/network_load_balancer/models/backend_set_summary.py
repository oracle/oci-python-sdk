# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackendSetSummary(object):
    """
    The configuration of a network load balancer backend set.
    For more information about backend set configuration, see
    `Managing Backend Sets`__.

    **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingbackendsets.htm
    """

    #: A constant which can be used with the policy property of a BackendSetSummary.
    #: This constant has a value of "TWO_TUPLE"
    POLICY_TWO_TUPLE = "TWO_TUPLE"

    #: A constant which can be used with the policy property of a BackendSetSummary.
    #: This constant has a value of "THREE_TUPLE"
    POLICY_THREE_TUPLE = "THREE_TUPLE"

    #: A constant which can be used with the policy property of a BackendSetSummary.
    #: This constant has a value of "FIVE_TUPLE"
    POLICY_FIVE_TUPLE = "FIVE_TUPLE"

    #: A constant which can be used with the ip_version property of a BackendSetSummary.
    #: This constant has a value of "IPV4"
    IP_VERSION_IPV4 = "IPV4"

    #: A constant which can be used with the ip_version property of a BackendSetSummary.
    #: This constant has a value of "IPV6"
    IP_VERSION_IPV6 = "IPV6"

    def __init__(self, **kwargs):
        """
        Initializes a new BackendSetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this BackendSetSummary.
        :type name: str

        :param policy:
            The value to assign to the policy property of this BackendSetSummary.
            Allowed values for this property are: "TWO_TUPLE", "THREE_TUPLE", "FIVE_TUPLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type policy: str

        :param is_preserve_source:
            The value to assign to the is_preserve_source property of this BackendSetSummary.
        :type is_preserve_source: bool

        :param ip_version:
            The value to assign to the ip_version property of this BackendSetSummary.
            Allowed values for this property are: "IPV4", "IPV6", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ip_version: str

        :param backends:
            The value to assign to the backends property of this BackendSetSummary.
        :type backends: list[oci.network_load_balancer.models.Backend]

        :param health_checker:
            The value to assign to the health_checker property of this BackendSetSummary.
        :type health_checker: oci.network_load_balancer.models.HealthChecker

        """
        self.swagger_types = {
            'name': 'str',
            'policy': 'str',
            'is_preserve_source': 'bool',
            'ip_version': 'str',
            'backends': 'list[Backend]',
            'health_checker': 'HealthChecker'
        }

        self.attribute_map = {
            'name': 'name',
            'policy': 'policy',
            'is_preserve_source': 'isPreserveSource',
            'ip_version': 'ipVersion',
            'backends': 'backends',
            'health_checker': 'healthChecker'
        }

        self._name = None
        self._policy = None
        self._is_preserve_source = None
        self._ip_version = None
        self._backends = None
        self._health_checker = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this BackendSetSummary.
        A user-friendly name for the backend set that must be unique and cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
        contain spaces. Avoid entering confidential information.

        Example: `example_backend_set`


        :return: The name of this BackendSetSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BackendSetSummary.
        A user-friendly name for the backend set that must be unique and cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
        contain spaces. Avoid entering confidential information.

        Example: `example_backend_set`


        :param name: The name of this BackendSetSummary.
        :type: str
        """
        self._name = name

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this BackendSetSummary.
        The network load balancer policy for the backend set.

        Example: `FIVE_TUPLE`

        Allowed values for this property are: "TWO_TUPLE", "THREE_TUPLE", "FIVE_TUPLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy of this BackendSetSummary.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this BackendSetSummary.
        The network load balancer policy for the backend set.

        Example: `FIVE_TUPLE`


        :param policy: The policy of this BackendSetSummary.
        :type: str
        """
        allowed_values = ["TWO_TUPLE", "THREE_TUPLE", "FIVE_TUPLE"]
        if not value_allowed_none_or_none_sentinel(policy, allowed_values):
            policy = 'UNKNOWN_ENUM_VALUE'
        self._policy = policy

    @property
    def is_preserve_source(self):
        """
        Gets the is_preserve_source of this BackendSetSummary.
        If this parameter is enabled, the network load balancer preserves the source IP of the packet forwarded to the backend servers.
        Backend servers see the original source IP. If the `isPreserveSourceDestination` parameter is enabled for the network load balancer resource, this parameter cannot be disabled.
        The value is true by default.


        :return: The is_preserve_source of this BackendSetSummary.
        :rtype: bool
        """
        return self._is_preserve_source

    @is_preserve_source.setter
    def is_preserve_source(self, is_preserve_source):
        """
        Sets the is_preserve_source of this BackendSetSummary.
        If this parameter is enabled, the network load balancer preserves the source IP of the packet forwarded to the backend servers.
        Backend servers see the original source IP. If the `isPreserveSourceDestination` parameter is enabled for the network load balancer resource, this parameter cannot be disabled.
        The value is true by default.


        :param is_preserve_source: The is_preserve_source of this BackendSetSummary.
        :type: bool
        """
        self._is_preserve_source = is_preserve_source

    @property
    def ip_version(self):
        """
        Gets the ip_version of this BackendSetSummary.
        IP version associated with the backend set.

        Allowed values for this property are: "IPV4", "IPV6", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ip_version of this BackendSetSummary.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """
        Sets the ip_version of this BackendSetSummary.
        IP version associated with the backend set.


        :param ip_version: The ip_version of this BackendSetSummary.
        :type: str
        """
        allowed_values = ["IPV4", "IPV6"]
        if not value_allowed_none_or_none_sentinel(ip_version, allowed_values):
            ip_version = 'UNKNOWN_ENUM_VALUE'
        self._ip_version = ip_version

    @property
    def backends(self):
        """
        **[Required]** Gets the backends of this BackendSetSummary.
        An array of backends.


        :return: The backends of this BackendSetSummary.
        :rtype: list[oci.network_load_balancer.models.Backend]
        """
        return self._backends

    @backends.setter
    def backends(self, backends):
        """
        Sets the backends of this BackendSetSummary.
        An array of backends.


        :param backends: The backends of this BackendSetSummary.
        :type: list[oci.network_load_balancer.models.Backend]
        """
        self._backends = backends

    @property
    def health_checker(self):
        """
        **[Required]** Gets the health_checker of this BackendSetSummary.

        :return: The health_checker of this BackendSetSummary.
        :rtype: oci.network_load_balancer.models.HealthChecker
        """
        return self._health_checker

    @health_checker.setter
    def health_checker(self, health_checker):
        """
        Sets the health_checker of this BackendSetSummary.

        :param health_checker: The health_checker of this BackendSetSummary.
        :type: oci.network_load_balancer.models.HealthChecker
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
