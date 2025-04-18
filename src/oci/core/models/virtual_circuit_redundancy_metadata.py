# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualCircuitRedundancyMetadata(object):
    """
    This resource provides redundancy level details for the virtual circuit. For more about redundancy, see `FastConnect Redundancy Best Practices`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnectresiliency.htm
    """

    #: A constant which can be used with the configured_redundancy_level property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "DEVICE"
    CONFIGURED_REDUNDANCY_LEVEL_DEVICE = "DEVICE"

    #: A constant which can be used with the configured_redundancy_level property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "POP"
    CONFIGURED_REDUNDANCY_LEVEL_POP = "POP"

    #: A constant which can be used with the configured_redundancy_level property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "REGION"
    CONFIGURED_REDUNDANCY_LEVEL_REGION = "REGION"

    #: A constant which can be used with the configured_redundancy_level property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "NON_REDUNDANT"
    CONFIGURED_REDUNDANCY_LEVEL_NON_REDUNDANT = "NON_REDUNDANT"

    #: A constant which can be used with the configured_redundancy_level property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "PENDING"
    CONFIGURED_REDUNDANCY_LEVEL_PENDING = "PENDING"

    #: A constant which can be used with the ipv4bgp_session_redundancy_status property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "CONFIGURATION_MATCH"
    IPV4BGP_SESSION_REDUNDANCY_STATUS_CONFIGURATION_MATCH = "CONFIGURATION_MATCH"

    #: A constant which can be used with the ipv4bgp_session_redundancy_status property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "CONFIGURATION_MISMATCH"
    IPV4BGP_SESSION_REDUNDANCY_STATUS_CONFIGURATION_MISMATCH = "CONFIGURATION_MISMATCH"

    #: A constant which can be used with the ipv4bgp_session_redundancy_status property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "NOT_MET_SLA"
    IPV4BGP_SESSION_REDUNDANCY_STATUS_NOT_MET_SLA = "NOT_MET_SLA"

    #: A constant which can be used with the ipv6bgp_session_redundancy_status property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "CONFIGURATION_MATCH"
    IPV6BGP_SESSION_REDUNDANCY_STATUS_CONFIGURATION_MATCH = "CONFIGURATION_MATCH"

    #: A constant which can be used with the ipv6bgp_session_redundancy_status property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "CONFIGURATION_MISMATCH"
    IPV6BGP_SESSION_REDUNDANCY_STATUS_CONFIGURATION_MISMATCH = "CONFIGURATION_MISMATCH"

    #: A constant which can be used with the ipv6bgp_session_redundancy_status property of a VirtualCircuitRedundancyMetadata.
    #: This constant has a value of "NOT_MET_SLA"
    IPV6BGP_SESSION_REDUNDANCY_STATUS_NOT_MET_SLA = "NOT_MET_SLA"

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualCircuitRedundancyMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param configured_redundancy_level:
            The value to assign to the configured_redundancy_level property of this VirtualCircuitRedundancyMetadata.
            Allowed values for this property are: "DEVICE", "POP", "REGION", "NON_REDUNDANT", "PENDING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type configured_redundancy_level: str

        :param ipv4bgp_session_redundancy_status:
            The value to assign to the ipv4bgp_session_redundancy_status property of this VirtualCircuitRedundancyMetadata.
            Allowed values for this property are: "CONFIGURATION_MATCH", "CONFIGURATION_MISMATCH", "NOT_MET_SLA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ipv4bgp_session_redundancy_status: str

        :param ipv6bgp_session_redundancy_status:
            The value to assign to the ipv6bgp_session_redundancy_status property of this VirtualCircuitRedundancyMetadata.
            Allowed values for this property are: "CONFIGURATION_MATCH", "CONFIGURATION_MISMATCH", "NOT_MET_SLA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ipv6bgp_session_redundancy_status: str

        """
        self.swagger_types = {
            'configured_redundancy_level': 'str',
            'ipv4bgp_session_redundancy_status': 'str',
            'ipv6bgp_session_redundancy_status': 'str'
        }
        self.attribute_map = {
            'configured_redundancy_level': 'configuredRedundancyLevel',
            'ipv4bgp_session_redundancy_status': 'ipv4bgpSessionRedundancyStatus',
            'ipv6bgp_session_redundancy_status': 'ipv6bgpSessionRedundancyStatus'
        }
        self._configured_redundancy_level = None
        self._ipv4bgp_session_redundancy_status = None
        self._ipv6bgp_session_redundancy_status = None

    @property
    def configured_redundancy_level(self):
        """
        Gets the configured_redundancy_level of this VirtualCircuitRedundancyMetadata.
        The configured redundancy level of the virtual circuit.

        Allowed values for this property are: "DEVICE", "POP", "REGION", "NON_REDUNDANT", "PENDING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The configured_redundancy_level of this VirtualCircuitRedundancyMetadata.
        :rtype: str
        """
        return self._configured_redundancy_level

    @configured_redundancy_level.setter
    def configured_redundancy_level(self, configured_redundancy_level):
        """
        Sets the configured_redundancy_level of this VirtualCircuitRedundancyMetadata.
        The configured redundancy level of the virtual circuit.


        :param configured_redundancy_level: The configured_redundancy_level of this VirtualCircuitRedundancyMetadata.
        :type: str
        """
        allowed_values = ["DEVICE", "POP", "REGION", "NON_REDUNDANT", "PENDING"]
        if not value_allowed_none_or_none_sentinel(configured_redundancy_level, allowed_values):
            configured_redundancy_level = 'UNKNOWN_ENUM_VALUE'
        self._configured_redundancy_level = configured_redundancy_level

    @property
    def ipv4bgp_session_redundancy_status(self):
        """
        Gets the ipv4bgp_session_redundancy_status of this VirtualCircuitRedundancyMetadata.
        Indicates if the configured level is met for IPv4 BGP redundancy.

        Allowed values for this property are: "CONFIGURATION_MATCH", "CONFIGURATION_MISMATCH", "NOT_MET_SLA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ipv4bgp_session_redundancy_status of this VirtualCircuitRedundancyMetadata.
        :rtype: str
        """
        return self._ipv4bgp_session_redundancy_status

    @ipv4bgp_session_redundancy_status.setter
    def ipv4bgp_session_redundancy_status(self, ipv4bgp_session_redundancy_status):
        """
        Sets the ipv4bgp_session_redundancy_status of this VirtualCircuitRedundancyMetadata.
        Indicates if the configured level is met for IPv4 BGP redundancy.


        :param ipv4bgp_session_redundancy_status: The ipv4bgp_session_redundancy_status of this VirtualCircuitRedundancyMetadata.
        :type: str
        """
        allowed_values = ["CONFIGURATION_MATCH", "CONFIGURATION_MISMATCH", "NOT_MET_SLA"]
        if not value_allowed_none_or_none_sentinel(ipv4bgp_session_redundancy_status, allowed_values):
            ipv4bgp_session_redundancy_status = 'UNKNOWN_ENUM_VALUE'
        self._ipv4bgp_session_redundancy_status = ipv4bgp_session_redundancy_status

    @property
    def ipv6bgp_session_redundancy_status(self):
        """
        Gets the ipv6bgp_session_redundancy_status of this VirtualCircuitRedundancyMetadata.
        Indicates if the configured level is met for IPv6 BGP redundancy.

        Allowed values for this property are: "CONFIGURATION_MATCH", "CONFIGURATION_MISMATCH", "NOT_MET_SLA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ipv6bgp_session_redundancy_status of this VirtualCircuitRedundancyMetadata.
        :rtype: str
        """
        return self._ipv6bgp_session_redundancy_status

    @ipv6bgp_session_redundancy_status.setter
    def ipv6bgp_session_redundancy_status(self, ipv6bgp_session_redundancy_status):
        """
        Sets the ipv6bgp_session_redundancy_status of this VirtualCircuitRedundancyMetadata.
        Indicates if the configured level is met for IPv6 BGP redundancy.


        :param ipv6bgp_session_redundancy_status: The ipv6bgp_session_redundancy_status of this VirtualCircuitRedundancyMetadata.
        :type: str
        """
        allowed_values = ["CONFIGURATION_MATCH", "CONFIGURATION_MISMATCH", "NOT_MET_SLA"]
        if not value_allowed_none_or_none_sentinel(ipv6bgp_session_redundancy_status, allowed_values):
            ipv6bgp_session_redundancy_status = 'UNKNOWN_ENUM_VALUE'
        self._ipv6bgp_session_redundancy_status = ipv6bgp_session_redundancy_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
