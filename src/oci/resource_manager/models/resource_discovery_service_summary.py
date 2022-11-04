# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceDiscoveryServiceSummary(object):
    """
    A service supported for use with `Resource Discovery`__.

    __ https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services
    """

    #: A constant which can be used with the discovery_scope property of a ResourceDiscoveryServiceSummary.
    #: This constant has a value of "TENANCY"
    DISCOVERY_SCOPE_TENANCY = "TENANCY"

    #: A constant which can be used with the discovery_scope property of a ResourceDiscoveryServiceSummary.
    #: This constant has a value of "COMPARTMENT"
    DISCOVERY_SCOPE_COMPARTMENT = "COMPARTMENT"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceDiscoveryServiceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ResourceDiscoveryServiceSummary.
        :type name: str

        :param discovery_scope:
            The value to assign to the discovery_scope property of this ResourceDiscoveryServiceSummary.
            Allowed values for this property are: "TENANCY", "COMPARTMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type discovery_scope: str

        """
        self.swagger_types = {
            'name': 'str',
            'discovery_scope': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'discovery_scope': 'discoveryScope'
        }

        self._name = None
        self._discovery_scope = None

    @property
    def name(self):
        """
        Gets the name of this ResourceDiscoveryServiceSummary.
        A supported service. Example: `core`
        For reference on service names, see the `Terraform provider documentation`__.

        __ https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services


        :return: The name of this ResourceDiscoveryServiceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResourceDiscoveryServiceSummary.
        A supported service. Example: `core`
        For reference on service names, see the `Terraform provider documentation`__.

        __ https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services


        :param name: The name of this ResourceDiscoveryServiceSummary.
        :type: str
        """
        self._name = name

    @property
    def discovery_scope(self):
        """
        Gets the discovery_scope of this ResourceDiscoveryServiceSummary.
        The scope of the service as used with Resource Discovery.
        This property determines the type of compartment OCID required: root compartment (`TENANCY`) or not (`COMPARTMENT`).
        For example, `identity` is at the root compartment scope while `database` is at the compartment scope.

        Allowed values for this property are: "TENANCY", "COMPARTMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The discovery_scope of this ResourceDiscoveryServiceSummary.
        :rtype: str
        """
        return self._discovery_scope

    @discovery_scope.setter
    def discovery_scope(self, discovery_scope):
        """
        Sets the discovery_scope of this ResourceDiscoveryServiceSummary.
        The scope of the service as used with Resource Discovery.
        This property determines the type of compartment OCID required: root compartment (`TENANCY`) or not (`COMPARTMENT`).
        For example, `identity` is at the root compartment scope while `database` is at the compartment scope.


        :param discovery_scope: The discovery_scope of this ResourceDiscoveryServiceSummary.
        :type: str
        """
        allowed_values = ["TENANCY", "COMPARTMENT"]
        if not value_allowed_none_or_none_sentinel(discovery_scope, allowed_values):
            discovery_scope = 'UNKNOWN_ENUM_VALUE'
        self._discovery_scope = discovery_scope

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
