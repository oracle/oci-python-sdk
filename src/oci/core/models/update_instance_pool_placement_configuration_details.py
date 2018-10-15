# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInstancePoolPlacementConfigurationDetails(object):
    """
    The location for where an instance pool will place instances.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInstancePoolPlacementConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this UpdateInstancePoolPlacementConfigurationDetails.
        :type availability_domain: str

        :param primary_subnet_id:
            The value to assign to the primary_subnet_id property of this UpdateInstancePoolPlacementConfigurationDetails.
        :type primary_subnet_id: str

        :param secondary_vnic_subnets:
            The value to assign to the secondary_vnic_subnets property of this UpdateInstancePoolPlacementConfigurationDetails.
        :type secondary_vnic_subnets: list[InstancePoolPlacementSecondaryVnicSubnet]

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
        **[Required]** Gets the availability_domain of this UpdateInstancePoolPlacementConfigurationDetails.
        The availability domain to place instances.
        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this UpdateInstancePoolPlacementConfigurationDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this UpdateInstancePoolPlacementConfigurationDetails.
        The availability domain to place instances.
        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this UpdateInstancePoolPlacementConfigurationDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def primary_subnet_id(self):
        """
        **[Required]** Gets the primary_subnet_id of this UpdateInstancePoolPlacementConfigurationDetails.
        The OCID of the primary subnet to place instances.


        :return: The primary_subnet_id of this UpdateInstancePoolPlacementConfigurationDetails.
        :rtype: str
        """
        return self._primary_subnet_id

    @primary_subnet_id.setter
    def primary_subnet_id(self, primary_subnet_id):
        """
        Sets the primary_subnet_id of this UpdateInstancePoolPlacementConfigurationDetails.
        The OCID of the primary subnet to place instances.


        :param primary_subnet_id: The primary_subnet_id of this UpdateInstancePoolPlacementConfigurationDetails.
        :type: str
        """
        self._primary_subnet_id = primary_subnet_id

    @property
    def secondary_vnic_subnets(self):
        """
        Gets the secondary_vnic_subnets of this UpdateInstancePoolPlacementConfigurationDetails.
        The set of subnet OCIDs for secondary VNICs for instances in the pool.


        :return: The secondary_vnic_subnets of this UpdateInstancePoolPlacementConfigurationDetails.
        :rtype: list[InstancePoolPlacementSecondaryVnicSubnet]
        """
        return self._secondary_vnic_subnets

    @secondary_vnic_subnets.setter
    def secondary_vnic_subnets(self, secondary_vnic_subnets):
        """
        Sets the secondary_vnic_subnets of this UpdateInstancePoolPlacementConfigurationDetails.
        The set of subnet OCIDs for secondary VNICs for instances in the pool.


        :param secondary_vnic_subnets: The secondary_vnic_subnets of this UpdateInstancePoolPlacementConfigurationDetails.
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
