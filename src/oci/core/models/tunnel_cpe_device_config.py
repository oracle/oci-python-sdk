# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TunnelCpeDeviceConfig(object):
    """
    The set of CPE configuration answers for the tunnel, which the customer provides in
    :func:`update_tunnel_cpe_device_config`.
    The answers correlate to the questions that are specific to the CPE device type (see the
    `parameters` attribute of :class:`CpeDeviceShapeDetail`).

    See these related operations:

    * :func:`get_tunnel_cpe_device_config`
    * :func:`get_tunnel_cpe_device_config_content`
    * :func:`get_ipsec_cpe_device_config_content`
    * :func:`get_cpe_device_config_content`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TunnelCpeDeviceConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tunnel_cpe_device_config_parameter:
            The value to assign to the tunnel_cpe_device_config_parameter property of this TunnelCpeDeviceConfig.
        :type tunnel_cpe_device_config_parameter: list[oci.core.models.CpeDeviceConfigAnswer]

        """
        self.swagger_types = {
            'tunnel_cpe_device_config_parameter': 'list[CpeDeviceConfigAnswer]'
        }

        self.attribute_map = {
            'tunnel_cpe_device_config_parameter': 'tunnelCpeDeviceConfigParameter'
        }

        self._tunnel_cpe_device_config_parameter = None

    @property
    def tunnel_cpe_device_config_parameter(self):
        """
        Gets the tunnel_cpe_device_config_parameter of this TunnelCpeDeviceConfig.

        :return: The tunnel_cpe_device_config_parameter of this TunnelCpeDeviceConfig.
        :rtype: list[oci.core.models.CpeDeviceConfigAnswer]
        """
        return self._tunnel_cpe_device_config_parameter

    @tunnel_cpe_device_config_parameter.setter
    def tunnel_cpe_device_config_parameter(self, tunnel_cpe_device_config_parameter):
        """
        Sets the tunnel_cpe_device_config_parameter of this TunnelCpeDeviceConfig.

        :param tunnel_cpe_device_config_parameter: The tunnel_cpe_device_config_parameter of this TunnelCpeDeviceConfig.
        :type: list[oci.core.models.CpeDeviceConfigAnswer]
        """
        self._tunnel_cpe_device_config_parameter = tunnel_cpe_device_config_parameter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
