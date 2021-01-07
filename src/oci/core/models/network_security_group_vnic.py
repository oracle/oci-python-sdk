# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkSecurityGroupVnic(object):
    """
    Information about a VNIC that belongs to a network security group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkSecurityGroupVnic object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this NetworkSecurityGroupVnic.
        :type resource_id: str

        :param time_associated:
            The value to assign to the time_associated property of this NetworkSecurityGroupVnic.
        :type time_associated: datetime

        :param vnic_id:
            The value to assign to the vnic_id property of this NetworkSecurityGroupVnic.
        :type vnic_id: str

        """
        self.swagger_types = {
            'resource_id': 'str',
            'time_associated': 'datetime',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'time_associated': 'timeAssociated',
            'vnic_id': 'vnicId'
        }

        self._resource_id = None
        self._time_associated = None
        self._vnic_id = None

    @property
    def resource_id(self):
        """
        Gets the resource_id of this NetworkSecurityGroupVnic.
        The `OCID`__ of the parent resource that the VNIC
        is attached to (for example, a Compute instance).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this NetworkSecurityGroupVnic.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this NetworkSecurityGroupVnic.
        The `OCID`__ of the parent resource that the VNIC
        is attached to (for example, a Compute instance).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this NetworkSecurityGroupVnic.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def time_associated(self):
        """
        Gets the time_associated of this NetworkSecurityGroupVnic.
        The date and time the VNIC was added to the network security group, in the format
        defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_associated of this NetworkSecurityGroupVnic.
        :rtype: datetime
        """
        return self._time_associated

    @time_associated.setter
    def time_associated(self, time_associated):
        """
        Sets the time_associated of this NetworkSecurityGroupVnic.
        The date and time the VNIC was added to the network security group, in the format
        defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_associated: The time_associated of this NetworkSecurityGroupVnic.
        :type: datetime
        """
        self._time_associated = time_associated

    @property
    def vnic_id(self):
        """
        **[Required]** Gets the vnic_id of this NetworkSecurityGroupVnic.
        The `OCID`__ of the VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vnic_id of this NetworkSecurityGroupVnic.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this NetworkSecurityGroupVnic.
        The `OCID`__ of the VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vnic_id: The vnic_id of this NetworkSecurityGroupVnic.
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
