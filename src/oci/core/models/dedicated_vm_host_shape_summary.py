# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedVmHostShapeSummary(object):
    """
    The shape used to launch the dedicated virtual machine (VM) host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedVmHostShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this DedicatedVmHostShapeSummary.
        :type availability_domain: str

        :param dedicated_vm_host_shape:
            The value to assign to the dedicated_vm_host_shape property of this DedicatedVmHostShapeSummary.
        :type dedicated_vm_host_shape: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'dedicated_vm_host_shape': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'dedicated_vm_host_shape': 'dedicatedVmHostShape'
        }

        self._availability_domain = None
        self._dedicated_vm_host_shape = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this DedicatedVmHostShapeSummary.
        The shape's availability domain.


        :return: The availability_domain of this DedicatedVmHostShapeSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DedicatedVmHostShapeSummary.
        The shape's availability domain.


        :param availability_domain: The availability_domain of this DedicatedVmHostShapeSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def dedicated_vm_host_shape(self):
        """
        **[Required]** Gets the dedicated_vm_host_shape of this DedicatedVmHostShapeSummary.
        The name of the dedicated vm host shape. You can enumerate all available shapes by calling
        :class:`DedicatedVmHostShapes`.


        :return: The dedicated_vm_host_shape of this DedicatedVmHostShapeSummary.
        :rtype: str
        """
        return self._dedicated_vm_host_shape

    @dedicated_vm_host_shape.setter
    def dedicated_vm_host_shape(self, dedicated_vm_host_shape):
        """
        Sets the dedicated_vm_host_shape of this DedicatedVmHostShapeSummary.
        The name of the dedicated vm host shape. You can enumerate all available shapes by calling
        :class:`DedicatedVmHostShapes`.


        :param dedicated_vm_host_shape: The dedicated_vm_host_shape of this DedicatedVmHostShapeSummary.
        :type: str
        """
        self._dedicated_vm_host_shape = dedicated_vm_host_shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
