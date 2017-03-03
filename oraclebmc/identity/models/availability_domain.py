# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class AvailabilityDomain(object):

    def __init__(self):

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
