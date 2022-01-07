# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterNetworkPlacementConfigurationDetails(object):
    """
    The location for where the instance pools in a cluster network will place instances.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterNetworkPlacementConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this ClusterNetworkPlacementConfigurationDetails.
        :type availability_domain: str

        :param primary_subnet_id:
            The value to assign to the primary_subnet_id property of this ClusterNetworkPlacementConfigurationDetails.
        :type primary_subnet_id: str

        :param secondary_vnic_subnets:
            The value to assign to the secondary_vnic_subnets property of this ClusterNetworkPlacementConfigurationDetails.
        :type secondary_vnic_subnets: list[oci.core.models.InstancePoolPlacementSecondaryVnicSubnet]

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'primary_subnet_id': 'str',
            'secondary_vnic_subnets': 'list[InstancePoolPlacementSecondaryVnicSubnet]'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'primary_subnet_id': 'primarySubnetId',
            'secondary_vnic_subnets': 'secondaryVnicSubnets'
        }

        self._availability_domain = None
        self._primary_subnet_id = None
        self._secondary_vnic_subnets = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ClusterNetworkPlacementConfigurationDetails.
        The availability domain to place instances.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this ClusterNetworkPlacementConfigurationDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ClusterNetworkPlacementConfigurationDetails.
        The availability domain to place instances.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this ClusterNetworkPlacementConfigurationDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def primary_subnet_id(self):
        """
        **[Required]** Gets the primary_subnet_id of this ClusterNetworkPlacementConfigurationDetails.
        The `OCID`__ of the primary subnet to place
        instances.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The primary_subnet_id of this ClusterNetworkPlacementConfigurationDetails.
        :rtype: str
        """
        return self._primary_subnet_id

    @primary_subnet_id.setter
    def primary_subnet_id(self, primary_subnet_id):
        """
        Sets the primary_subnet_id of this ClusterNetworkPlacementConfigurationDetails.
        The `OCID`__ of the primary subnet to place
        instances.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param primary_subnet_id: The primary_subnet_id of this ClusterNetworkPlacementConfigurationDetails.
        :type: str
        """
        self._primary_subnet_id = primary_subnet_id

    @property
    def secondary_vnic_subnets(self):
        """
        Gets the secondary_vnic_subnets of this ClusterNetworkPlacementConfigurationDetails.
        The set of secondary VNIC data for instances in the pool.


        :return: The secondary_vnic_subnets of this ClusterNetworkPlacementConfigurationDetails.
        :rtype: list[oci.core.models.InstancePoolPlacementSecondaryVnicSubnet]
        """
        return self._secondary_vnic_subnets

    @secondary_vnic_subnets.setter
    def secondary_vnic_subnets(self, secondary_vnic_subnets):
        """
        Sets the secondary_vnic_subnets of this ClusterNetworkPlacementConfigurationDetails.
        The set of secondary VNIC data for instances in the pool.


        :param secondary_vnic_subnets: The secondary_vnic_subnets of this ClusterNetworkPlacementConfigurationDetails.
        :type: list[oci.core.models.InstancePoolPlacementSecondaryVnicSubnet]
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
