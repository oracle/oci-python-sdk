# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstancePoolPlacementSecondaryVnicSubnet(object):
    """
    The secondary VNIC object for the placement configuration for an instance pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstancePoolPlacementSecondaryVnicSubnet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this InstancePoolPlacementSecondaryVnicSubnet.
        :type display_name: str

        :param subnet_id:
            The value to assign to the subnet_id property of this InstancePoolPlacementSecondaryVnicSubnet.
        :type subnet_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'subnet_id': 'subnetId'
        }

        self._display_name = None
        self._subnet_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this InstancePoolPlacementSecondaryVnicSubnet.
        The display name of the VNIC. This is also use to match against the instance configuration defined
        secondary VNIC.


        :return: The display_name of this InstancePoolPlacementSecondaryVnicSubnet.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstancePoolPlacementSecondaryVnicSubnet.
        The display name of the VNIC. This is also use to match against the instance configuration defined
        secondary VNIC.


        :param display_name: The display_name of this InstancePoolPlacementSecondaryVnicSubnet.
        :type: str
        """
        self._display_name = display_name

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this InstancePoolPlacementSecondaryVnicSubnet.
        The subnet `OCID`__ for the secondary VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this InstancePoolPlacementSecondaryVnicSubnet.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this InstancePoolPlacementSecondaryVnicSubnet.
        The subnet `OCID`__ for the secondary VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this InstancePoolPlacementSecondaryVnicSubnet.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
