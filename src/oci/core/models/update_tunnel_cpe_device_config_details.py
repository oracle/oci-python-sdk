# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTunnelCpeDeviceConfigDetails(object):
    """
    UpdateTunnelCpeDeviceConfigDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTunnelCpeDeviceConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tunnel_cpe_device_config:
            The value to assign to the tunnel_cpe_device_config property of this UpdateTunnelCpeDeviceConfigDetails.
        :type tunnel_cpe_device_config: list[CpeDeviceConfigAnswer]

        """
        self.swagger_types = {
            'tunnel_cpe_device_config': 'list[CpeDeviceConfigAnswer]'
        }

        self.attribute_map = {
            'tunnel_cpe_device_config': 'tunnelCpeDeviceConfig'
        }

        self._tunnel_cpe_device_config = None

    @property
    def tunnel_cpe_device_config(self):
        """
        Gets the tunnel_cpe_device_config of this UpdateTunnelCpeDeviceConfigDetails.
        The set of configuration answers for a CPE device.


        :return: The tunnel_cpe_device_config of this UpdateTunnelCpeDeviceConfigDetails.
        :rtype: list[CpeDeviceConfigAnswer]
        """
        return self._tunnel_cpe_device_config

    @tunnel_cpe_device_config.setter
    def tunnel_cpe_device_config(self, tunnel_cpe_device_config):
        """
        Sets the tunnel_cpe_device_config of this UpdateTunnelCpeDeviceConfigDetails.
        The set of configuration answers for a CPE device.


        :param tunnel_cpe_device_config: The tunnel_cpe_device_config of this UpdateTunnelCpeDeviceConfigDetails.
        :type: list[CpeDeviceConfigAnswer]
        """
        self._tunnel_cpe_device_config = tunnel_cpe_device_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
