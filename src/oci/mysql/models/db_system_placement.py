# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemPlacement(object):
    """
    The availability domain and fault domain a DB System is placed in.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemPlacement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this DbSystemPlacement.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this DbSystemPlacement.
        :type fault_domain: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'fault_domain': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain'
        }

        self._availability_domain = None
        self._fault_domain = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this DbSystemPlacement.
        The availability domain in which the DB System is placed.


        :return: The availability_domain of this DbSystemPlacement.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DbSystemPlacement.
        The availability domain in which the DB System is placed.


        :param availability_domain: The availability_domain of this DbSystemPlacement.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this DbSystemPlacement.
        The fault domain in which the DB System is placed.


        :return: The fault_domain of this DbSystemPlacement.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this DbSystemPlacement.
        The fault domain in which the DB System is placed.


        :param fault_domain: The fault_domain of this DbSystemPlacement.
        :type: str
        """
        self._fault_domain = fault_domain

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
