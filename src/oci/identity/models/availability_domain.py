# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailabilityDomain(object):
    """
    One or more isolated, fault-tolerant Oracle data centers that host cloud resources such as instances, volumes,
    and subnets. A region contains several Availability Domains. For more information, see
    `Regions and Availability Domains`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailabilityDomain object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AvailabilityDomain.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AvailabilityDomain.
        :type compartment_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId'
        }

        self._name = None
        self._compartment_id = None

    @property
    def name(self):
        """
        Gets the name of this AvailabilityDomain.
        The name of the Availability Domain.


        :return: The name of this AvailabilityDomain.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AvailabilityDomain.
        The name of the Availability Domain.


        :param name: The name of this AvailabilityDomain.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AvailabilityDomain.
        The OCID of the tenancy.


        :return: The compartment_id of this AvailabilityDomain.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AvailabilityDomain.
        The OCID of the tenancy.


        :param compartment_id: The compartment_id of this AvailabilityDomain.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
