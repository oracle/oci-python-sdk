# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VcnDnsResolverAssociation(object):
    """
    The information about the VCN and the DNS resolver in the association.
    """

    #: A constant which can be used with the lifecycle_state property of a VcnDnsResolverAssociation.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a VcnDnsResolverAssociation.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a VcnDnsResolverAssociation.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a VcnDnsResolverAssociation.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new VcnDnsResolverAssociation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn_id:
            The value to assign to the vcn_id property of this VcnDnsResolverAssociation.
        :type vcn_id: str

        :param dns_resolver_id:
            The value to assign to the dns_resolver_id property of this VcnDnsResolverAssociation.
        :type dns_resolver_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VcnDnsResolverAssociation.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'vcn_id': 'str',
            'dns_resolver_id': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'vcn_id': 'vcnId',
            'dns_resolver_id': 'dnsResolverId',
            'lifecycle_state': 'lifecycleState'
        }

        self._vcn_id = None
        self._dns_resolver_id = None
        self._lifecycle_state = None

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this VcnDnsResolverAssociation.
        The `OCID`__ of the VCN in the association.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this VcnDnsResolverAssociation.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this VcnDnsResolverAssociation.
        The `OCID`__ of the VCN in the association.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this VcnDnsResolverAssociation.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def dns_resolver_id(self):
        """
        Gets the dns_resolver_id of this VcnDnsResolverAssociation.
        The `OCID`__ of the DNS resolver in the association.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The dns_resolver_id of this VcnDnsResolverAssociation.
        :rtype: str
        """
        return self._dns_resolver_id

    @dns_resolver_id.setter
    def dns_resolver_id(self, dns_resolver_id):
        """
        Sets the dns_resolver_id of this VcnDnsResolverAssociation.
        The `OCID`__ of the DNS resolver in the association.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param dns_resolver_id: The dns_resolver_id of this VcnDnsResolverAssociation.
        :type: str
        """
        self._dns_resolver_id = dns_resolver_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VcnDnsResolverAssociation.
        The current state of the association.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VcnDnsResolverAssociation.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VcnDnsResolverAssociation.
        The current state of the association.


        :param lifecycle_state: The lifecycle_state of this VcnDnsResolverAssociation.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
