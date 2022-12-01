# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerVnic(object):
    """
    An interface to a virtual network available to Containers on a Container Instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerVnic object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vnic_id:
            The value to assign to the vnic_id property of this ContainerVnic.
        :type vnic_id: str

        """
        self.swagger_types = {
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'vnic_id': 'vnicId'
        }

        self._vnic_id = None

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this ContainerVnic.
        The ID of the Virtual Network Interface Card (VNIC) over which
        Containers accessing this network can communicate with the
        larger Virtual Client Network.


        :return: The vnic_id of this ContainerVnic.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this ContainerVnic.
        The ID of the Virtual Network Interface Card (VNIC) over which
        Containers accessing this network can communicate with the
        larger Virtual Client Network.


        :param vnic_id: The vnic_id of this ContainerVnic.
        :type: str
        """
        self._vnic_id = vnic_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
