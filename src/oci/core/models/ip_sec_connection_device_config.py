# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IPSecConnectionDeviceConfig(object):

    def __init__(self, **kwargs):
        """
        Initializes a new IPSecConnectionDeviceConfig object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this IPSecConnectionDeviceConfig.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this IPSecConnectionDeviceConfig.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this IPSecConnectionDeviceConfig.
        :type time_created: datetime

        :param tunnels:
            The value to assign to the tunnels property of this IPSecConnectionDeviceConfig.
        :type tunnels: list[TunnelConfig]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'tunnels': 'list[TunnelConfig]'
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
        **[Required]** Gets the compartment_id of this IPSecConnectionDeviceConfig.
        The OCID of the compartment containing the IPSec connection.


        :return: The compartment_id of this IPSecConnectionDeviceConfig.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnectionDeviceConfig.
        The OCID of the compartment containing the IPSec connection.


        :param compartment_id: The compartment_id of this IPSecConnectionDeviceConfig.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IPSecConnectionDeviceConfig.
        The IPSec connection's Oracle ID (OCID).


        :return: The id of this IPSecConnectionDeviceConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnectionDeviceConfig.
        The IPSec connection's Oracle ID (OCID).


        :param id: The id of this IPSecConnectionDeviceConfig.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this IPSecConnectionDeviceConfig.
        The date and time the IPSec connection was created.


        :return: The time_created of this IPSecConnectionDeviceConfig.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IPSecConnectionDeviceConfig.
        The date and time the IPSec connection was created.


        :param time_created: The time_created of this IPSecConnectionDeviceConfig.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def tunnels(self):
        """
        Gets the tunnels of this IPSecConnectionDeviceConfig.
        Two :class:`TunnelConfig` objects.


        :return: The tunnels of this IPSecConnectionDeviceConfig.
        :rtype: list[TunnelConfig]
        """
        return self._tunnels

    @tunnels.setter
    def tunnels(self, tunnels):
        """
        Sets the tunnels of this IPSecConnectionDeviceConfig.
        Two :class:`TunnelConfig` objects.


        :param tunnels: The tunnels of this IPSecConnectionDeviceConfig.
        :type: list[TunnelConfig]
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
