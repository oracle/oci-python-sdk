# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstancePoolPlacementConfiguration(object):
    """
    The location for where an instance pool will place instances.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstancePoolPlacementConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this InstancePoolPlacementConfiguration.
        :type availability_domain: str

        :param primary_subnet_id:
            The value to assign to the primary_subnet_id property of this InstancePoolPlacementConfiguration.
        :type primary_subnet_id: str

        :param fault_domains:
            The value to assign to the fault_domains property of this InstancePoolPlacementConfiguration.
        :type fault_domains: list[str]

        :param secondary_vnic_subnets:
            The value to assign to the secondary_vnic_subnets property of this InstancePoolPlacementConfiguration.
        :type secondary_vnic_subnets: list[InstancePoolPlacementSecondaryVnicSubnet]

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'primary_subnet_id': 'str',
            'fault_domains': 'list[str]',
            'secondary_vnic_subnets': 'list[InstancePoolPlacementSecondaryVnicSubnet]'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'primary_subnet_id': 'primarySubnetId',
            'fault_domains': 'faultDomains',
            'secondary_vnic_subnets': 'secondaryVnicSubnets'
        }

        self._availability_domain = None
        self._primary_subnet_id = None
        self._fault_domains = None
        self._secondary_vnic_subnets = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this InstancePoolPlacementConfiguration.
        The availability domain to place instances.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this InstancePoolPlacementConfiguration.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this InstancePoolPlacementConfiguration.
        The availability domain to place instances.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this InstancePoolPlacementConfiguration.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def primary_subnet_id(self):
        """
        **[Required]** Gets the primary_subnet_id of this InstancePoolPlacementConfiguration.
        The `OCID`__ of the primary subnet to place instances.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The primary_subnet_id of this InstancePoolPlacementConfiguration.
        :rtype: str
        """
        return self._primary_subnet_id

    @primary_subnet_id.setter
    def primary_subnet_id(self, primary_subnet_id):
        """
        Sets the primary_subnet_id of this InstancePoolPlacementConfiguration.
        The `OCID`__ of the primary subnet to place instances.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param primary_subnet_id: The primary_subnet_id of this InstancePoolPlacementConfiguration.
        :type: str
        """
        self._primary_subnet_id = primary_subnet_id

    @property
    def fault_domains(self):
        """
        Gets the fault_domains of this InstancePoolPlacementConfiguration.
        The fault domains to place instances.

        If you don't provide any values, the system makes a best effort to distribute
        instances across all fault domains based on capacity.

        To distribute the instances evenly across selected fault domains, provide a
        set of fault domains. For example, you might want instances to be evenly
        distributed if your applications require high availability.

        To get a list of fault domains, use the
        :func:`list_fault_domains` operation
        in the Identity and Access Management Service API.

        Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`


        :return: The fault_domains of this InstancePoolPlacementConfiguration.
        :rtype: list[str]
        """
        return self._fault_domains

    @fault_domains.setter
    def fault_domains(self, fault_domains):
        """
        Sets the fault_domains of this InstancePoolPlacementConfiguration.
        The fault domains to place instances.

        If you don't provide any values, the system makes a best effort to distribute
        instances across all fault domains based on capacity.

        To distribute the instances evenly across selected fault domains, provide a
        set of fault domains. For example, you might want instances to be evenly
        distributed if your applications require high availability.

        To get a list of fault domains, use the
        :func:`list_fault_domains` operation
        in the Identity and Access Management Service API.

        Example: `[FAULT-DOMAIN-1, FAULT-DOMAIN-2, FAULT-DOMAIN-3]`


        :param fault_domains: The fault_domains of this InstancePoolPlacementConfiguration.
        :type: list[str]
        """
        self._fault_domains = fault_domains

    @property
    def secondary_vnic_subnets(self):
        """
        Gets the secondary_vnic_subnets of this InstancePoolPlacementConfiguration.
        The set of secondary VNIC data for instances in the pool.


        :return: The secondary_vnic_subnets of this InstancePoolPlacementConfiguration.
        :rtype: list[InstancePoolPlacementSecondaryVnicSubnet]
        """
        return self._secondary_vnic_subnets

    @secondary_vnic_subnets.setter
    def secondary_vnic_subnets(self, secondary_vnic_subnets):
        """
        Sets the secondary_vnic_subnets of this InstancePoolPlacementConfiguration.
        The set of secondary VNIC data for instances in the pool.


        :param secondary_vnic_subnets: The secondary_vnic_subnets of this InstancePoolPlacementConfiguration.
        :type: list[InstancePoolPlacementSecondaryVnicSubnet]
        """
        self._secondary_vnic_subnets = secondary_vnic_subnets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
