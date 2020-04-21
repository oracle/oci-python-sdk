# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceAvailability(object):
    """
    The availability of a given resource limit, based on the usage, tenant service limits and quotas set for the tenancy.
    Note: We cannot guarantee this data for all the limits. In those cases, these fields will be empty.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceAvailability object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param used:
            The value to assign to the used property of this ResourceAvailability.
        :type used: int

        :param available:
            The value to assign to the available property of this ResourceAvailability.
        :type available: int

        """
        self.swagger_types = {
            'used': 'int',
            'available': 'int'
        }

        self.attribute_map = {
            'used': 'used',
            'available': 'available'
        }

        self._used = None
        self._available = None

    @property
    def used(self):
        """
        Gets the used of this ResourceAvailability.
        The current usage in the given compartment.


        :return: The used of this ResourceAvailability.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """
        Sets the used of this ResourceAvailability.
        The current usage in the given compartment.


        :param used: The used of this ResourceAvailability.
        :type: int
        """
        self._used = used

    @property
    def available(self):
        """
        Gets the available of this ResourceAvailability.
        The count of available resources.


        :return: The available of this ResourceAvailability.
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """
        Sets the available of this ResourceAvailability.
        The count of available resources.


        :param available: The available of this ResourceAvailability.
        :type: int
        """
        self._available = available

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
