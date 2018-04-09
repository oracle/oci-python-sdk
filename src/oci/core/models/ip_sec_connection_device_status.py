# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IPSecConnectionDeviceStatus(object):
    """
    Status of the IPSec connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IPSecConnectionDeviceStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this IPSecConnectionDeviceStatus.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this IPSecConnectionDeviceStatus.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this IPSecConnectionDeviceStatus.
        :type time_created: datetime

        :param tunnels:
            The value to assign to the tunnels property of this IPSecConnectionDeviceStatus.
        :type tunnels: list[TunnelStatus]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'tunnels': 'list[TunnelStatus]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'id': 'id',
            'time_created': 'timeCreated',
            'tunnels': 'tunnels'
        }

        self._compartment_id = None
        self._id = None
        self._time_created = None
        self._tunnels = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IPSecConnectionDeviceStatus.
        The OCID of the compartment containing the IPSec connection.


        :return: The compartment_id of this IPSecConnectionDeviceStatus.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnectionDeviceStatus.
        The OCID of the compartment containing the IPSec connection.


        :param compartment_id: The compartment_id of this IPSecConnectionDeviceStatus.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IPSecConnectionDeviceStatus.
        The IPSec connection's Oracle ID (OCID).


        :return: The id of this IPSecConnectionDeviceStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnectionDeviceStatus.
        The IPSec connection's Oracle ID (OCID).


        :param id: The id of this IPSecConnectionDeviceStatus.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this IPSecConnectionDeviceStatus.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this IPSecConnectionDeviceStatus.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IPSecConnectionDeviceStatus.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this IPSecConnectionDeviceStatus.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def tunnels(self):
        """
        Gets the tunnels of this IPSecConnectionDeviceStatus.
        Two :class:`TunnelStatus` objects.


        :return: The tunnels of this IPSecConnectionDeviceStatus.
        :rtype: list[TunnelStatus]
        """
        return self._tunnels

    @tunnels.setter
    def tunnels(self, tunnels):
        """
        Sets the tunnels of this IPSecConnectionDeviceStatus.
        Two :class:`TunnelStatus` objects.


        :param tunnels: The tunnels of this IPSecConnectionDeviceStatus.
        :type: list[TunnelStatus]
        """
        self._tunnels = tunnels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
