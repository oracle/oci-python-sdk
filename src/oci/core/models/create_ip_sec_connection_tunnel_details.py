# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIPSecConnectionTunnelDetails(object):
    """
    CreateIPSecConnectionTunnelDetails model.
    """

    #: A constant which can be used with the routing property of a CreateIPSecConnectionTunnelDetails.
    #: This constant has a value of "BGP"
    ROUTING_BGP = "BGP"

    #: A constant which can be used with the routing property of a CreateIPSecConnectionTunnelDetails.
    #: This constant has a value of "STATIC"
    ROUTING_STATIC = "STATIC"

    #: A constant which can be used with the ike_version property of a CreateIPSecConnectionTunnelDetails.
    #: This constant has a value of "V1"
    IKE_VERSION_V1 = "V1"

    #: A constant which can be used with the ike_version property of a CreateIPSecConnectionTunnelDetails.
    #: This constant has a value of "V2"
    IKE_VERSION_V2 = "V2"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIPSecConnectionTunnelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateIPSecConnectionTunnelDetails.
        :type display_name: str

        :param routing:
            The value to assign to the routing property of this CreateIPSecConnectionTunnelDetails.
            Allowed values for this property are: "BGP", "STATIC"
        :type routing: str

        :param ike_version:
            The value to assign to the ike_version property of this CreateIPSecConnectionTunnelDetails.
            Allowed values for this property are: "V1", "V2"
        :type ike_version: str

        :param shared_secret:
            The value to assign to the shared_secret property of this CreateIPSecConnectionTunnelDetails.
        :type shared_secret: str

        :param bgp_session_config:
            The value to assign to the bgp_session_config property of this CreateIPSecConnectionTunnelDetails.
        :type bgp_session_config: CreateIPSecTunnelBgpSessionDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'routing': 'str',
            'ike_version': 'str',
            'shared_secret': 'str',
            'bgp_session_config': 'CreateIPSecTunnelBgpSessionDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'routing': 'routing',
            'ike_version': 'ikeVersion',
            'shared_secret': 'sharedSecret',
            'bgp_session_config': 'bgpSessionConfig'
        }

        self._display_name = None
        self._routing = None
        self._ike_version = None
        self._shared_secret = None
        self._bgp_session_config = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateIPSecConnectionTunnelDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this CreateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateIPSecConnectionTunnelDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this CreateIPSecConnectionTunnelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def routing(self):
        """
        Gets the routing of this CreateIPSecConnectionTunnelDetails.
        The type of routing to use for this tunnel (either BGP dynamic routing or static routing).

        Allowed values for this property are: "BGP", "STATIC"


        :return: The routing of this CreateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """
        Sets the routing of this CreateIPSecConnectionTunnelDetails.
        The type of routing to use for this tunnel (either BGP dynamic routing or static routing).


        :param routing: The routing of this CreateIPSecConnectionTunnelDetails.
        :type: str
        """
        allowed_values = ["BGP", "STATIC"]
        if not value_allowed_none_or_none_sentinel(routing, allowed_values):
            raise ValueError(
                "Invalid value for `routing`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._routing = routing

    @property
    def ike_version(self):
        """
        Gets the ike_version of this CreateIPSecConnectionTunnelDetails.
        Internet Key Exchange protocol version.

        Allowed values for this property are: "V1", "V2"


        :return: The ike_version of this CreateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._ike_version

    @ike_version.setter
    def ike_version(self, ike_version):
        """
        Sets the ike_version of this CreateIPSecConnectionTunnelDetails.
        Internet Key Exchange protocol version.


        :param ike_version: The ike_version of this CreateIPSecConnectionTunnelDetails.
        :type: str
        """
        allowed_values = ["V1", "V2"]
        if not value_allowed_none_or_none_sentinel(ike_version, allowed_values):
            raise ValueError(
                "Invalid value for `ike_version`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ike_version = ike_version

    @property
    def shared_secret(self):
        """
        Gets the shared_secret of this CreateIPSecConnectionTunnelDetails.
        The shared secret (pre-shared key) to use for the IPSec tunnel. Only numbers, letters, and
        spaces are allowed. If you don't provide a value,
        Oracle generates a value for you. You can specify your own shared secret later if
        you like with :func:`update_ip_sec_connection_tunnel_shared_secret`.


        :return: The shared_secret of this CreateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """
        Sets the shared_secret of this CreateIPSecConnectionTunnelDetails.
        The shared secret (pre-shared key) to use for the IPSec tunnel. Only numbers, letters, and
        spaces are allowed. If you don't provide a value,
        Oracle generates a value for you. You can specify your own shared secret later if
        you like with :func:`update_ip_sec_connection_tunnel_shared_secret`.


        :param shared_secret: The shared_secret of this CreateIPSecConnectionTunnelDetails.
        :type: str
        """
        self._shared_secret = shared_secret

    @property
    def bgp_session_config(self):
        """
        Gets the bgp_session_config of this CreateIPSecConnectionTunnelDetails.
        Information for establishing a BGP session for the IPSec tunnel. Required if the tunnel uses
        BGP dynamic routing.

        If the tunnel instead uses static routing, you may optionally provide
        this object and set an IP address for one or both ends of the IPSec tunnel for the purposes
        of troubleshooting or monitoring the tunnel.


        :return: The bgp_session_config of this CreateIPSecConnectionTunnelDetails.
        :rtype: CreateIPSecTunnelBgpSessionDetails
        """
        return self._bgp_session_config

    @bgp_session_config.setter
    def bgp_session_config(self, bgp_session_config):
        """
        Sets the bgp_session_config of this CreateIPSecConnectionTunnelDetails.
        Information for establishing a BGP session for the IPSec tunnel. Required if the tunnel uses
        BGP dynamic routing.

        If the tunnel instead uses static routing, you may optionally provide
        this object and set an IP address for one or both ends of the IPSec tunnel for the purposes
        of troubleshooting or monitoring the tunnel.


        :param bgp_session_config: The bgp_session_config of this CreateIPSecConnectionTunnelDetails.
        :type: CreateIPSecTunnelBgpSessionDetails
        """
        self._bgp_session_config = bgp_session_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
