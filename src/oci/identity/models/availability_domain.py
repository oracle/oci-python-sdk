# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailabilityDomain(object):
    """
    One or more isolated, fault-tolerant Oracle data centers that host cloud resources such as instances, volumes,
    and subnets. A region contains several Availability Domains. For more information, see
    `Regions and Availability Domains`__.

    __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailabilityDomain object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AvailabilityDomain.
        :type name: str

        :param id:
            The value to assign to the id property of this AvailabilityDomain.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AvailabilityDomain.
        :type compartment_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'compartment_id': 'compartmentId'
        }

        self._name = None
        self._id = None
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
    def id(self):
        """
        Gets the id of this AvailabilityDomain.
        The OCID of the Availability Domain.


        :return: The id of this AvailabilityDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AvailabilityDomain.
        The OCID of the Availability Domain.


        :param id: The id of this AvailabilityDomain.
        :type: str
        """
        self._id = id

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
