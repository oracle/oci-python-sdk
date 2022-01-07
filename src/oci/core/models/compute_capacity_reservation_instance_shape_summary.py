# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeCapacityReservationInstanceShapeSummary(object):
    """
    An available shape used to launch instances in a compute capacity reservation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeCapacityReservationInstanceShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this ComputeCapacityReservationInstanceShapeSummary.
        :type availability_domain: str

        :param instance_shape:
            The value to assign to the instance_shape property of this ComputeCapacityReservationInstanceShapeSummary.
        :type instance_shape: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'instance_shape': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'instance_shape': 'instanceShape'
        }

        self._availability_domain = None
        self._instance_shape = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ComputeCapacityReservationInstanceShapeSummary.
        The shape's availability domain.


        :return: The availability_domain of this ComputeCapacityReservationInstanceShapeSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ComputeCapacityReservationInstanceShapeSummary.
        The shape's availability domain.


        :param availability_domain: The availability_domain of this ComputeCapacityReservationInstanceShapeSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def instance_shape(self):
        """
        **[Required]** Gets the instance_shape of this ComputeCapacityReservationInstanceShapeSummary.
        The name of the available shape used to launch instances in a compute capacity reservation.


        :return: The instance_shape of this ComputeCapacityReservationInstanceShapeSummary.
        :rtype: str
        """
        return self._instance_shape

    @instance_shape.setter
    def instance_shape(self, instance_shape):
        """
        Sets the instance_shape of this ComputeCapacityReservationInstanceShapeSummary.
        The name of the available shape used to launch instances in a compute capacity reservation.


        :param instance_shape: The instance_shape of this ComputeCapacityReservationInstanceShapeSummary.
        :type: str
        """
        self._instance_shape = instance_shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
