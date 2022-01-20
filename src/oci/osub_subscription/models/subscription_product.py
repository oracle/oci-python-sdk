# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscriptionProduct(object):
    """
    Product description
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubscriptionProduct object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param part_number:
            The value to assign to the part_number property of this SubscriptionProduct.
        :type part_number: str

        :param name:
            The value to assign to the name property of this SubscriptionProduct.
        :type name: str

        :param unit_of_measure:
            The value to assign to the unit_of_measure property of this SubscriptionProduct.
        :type unit_of_measure: str

        :param provisioning_group:
            The value to assign to the provisioning_group property of this SubscriptionProduct.
        :type provisioning_group: str

        """
        self.swagger_types = {
            'part_number': 'str',
            'name': 'str',
            'unit_of_measure': 'str',
            'provisioning_group': 'str'
        }

        self.attribute_map = {
            'part_number': 'partNumber',
            'name': 'name',
            'unit_of_measure': 'unitOfMeasure',
            'provisioning_group': 'provisioningGroup'
        }

        self._part_number = None
        self._name = None
        self._unit_of_measure = None
        self._provisioning_group = None

    @property
    def part_number(self):
        """
        **[Required]** Gets the part_number of this SubscriptionProduct.
        Product part numner


        :return: The part_number of this SubscriptionProduct.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this SubscriptionProduct.
        Product part numner


        :param part_number: The part_number of this SubscriptionProduct.
        :type: str
        """
        self._part_number = part_number

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SubscriptionProduct.
        Product name


        :return: The name of this SubscriptionProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SubscriptionProduct.
        Product name


        :param name: The name of this SubscriptionProduct.
        :type: str
        """
        self._name = name

    @property
    def unit_of_measure(self):
        """
        **[Required]** Gets the unit_of_measure of this SubscriptionProduct.
        Unit of measure


        :return: The unit_of_measure of this SubscriptionProduct.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this SubscriptionProduct.
        Unit of measure


        :param unit_of_measure: The unit_of_measure of this SubscriptionProduct.
        :type: str
        """
        self._unit_of_measure = unit_of_measure

    @property
    def provisioning_group(self):
        """
        Gets the provisioning_group of this SubscriptionProduct.
        Product provisioning group


        :return: The provisioning_group of this SubscriptionProduct.
        :rtype: str
        """
        return self._provisioning_group

    @provisioning_group.setter
    def provisioning_group(self, provisioning_group):
        """
        Sets the provisioning_group of this SubscriptionProduct.
        Product provisioning group


        :param provisioning_group: The provisioning_group of this SubscriptionProduct.
        :type: str
        """
        self._provisioning_group = provisioning_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
