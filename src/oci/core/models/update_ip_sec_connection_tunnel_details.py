# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIPSecConnectionTunnelDetails(object):
    """
    UpdateIPSecConnectionTunnelDetails model.
    """

    #: A constant which can be used with the routing property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "BGP"
    ROUTING_BGP = "BGP"

    #: A constant which can be used with the routing property of a UpdateIPSecConnectionTunnelDetails.
    #: This constant has a value of "STATIC"
    ROUTING_STATIC = "STATIC"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIPSecConnectionTunnelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateIPSecConnectionTunnelDetails.
        :type display_name: str

        :param routing:
            The value to assign to the routing property of this UpdateIPSecConnectionTunnelDetails.
            Allowed values for this property are: "BGP", "STATIC"
        :type routing: str

        :param bgp_session_config:
            The value to assign to the bgp_session_config property of this UpdateIPSecConnectionTunnelDetails.
        :type bgp_session_config: UpdateIPSecTunnelBgpSessionDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'routing': 'str',
            'bgp_session_config': 'UpdateIPSecTunnelBgpSessionDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'routing': 'routing',
            'bgp_session_config': 'bgpSessionConfig'
        }

        self._display_name = None
        self._routing = None
        self._bgp_session_config = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateIPSecConnectionTunnelDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this UpdateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateIPSecConnectionTunnelDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this UpdateIPSecConnectionTunnelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def routing(self):
        """
        Gets the routing of this UpdateIPSecConnectionTunnelDetails.
        The type of routing to use for this tunnel (either BGP dynamic routing or static routing).

        Allowed values for this property are: "BGP", "STATIC"


        :return: The routing of this UpdateIPSecConnectionTunnelDetails.
        :rtype: str
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """
        Sets the routing of this UpdateIPSecConnectionTunnelDetails.
        The type of routing to use for this tunnel (either BGP dynamic routing or static routing).


        :param routing: The routing of this UpdateIPSecConnectionTunnelDetails.
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
    def bgp_session_config(self):
        """
        Gets the bgp_session_config of this UpdateIPSecConnectionTunnelDetails.
        Information for establishing a BGP session for the IPSec tunnel.


        :return: The bgp_session_config of this UpdateIPSecConnectionTunnelDetails.
        :rtype: UpdateIPSecTunnelBgpSessionDetails
        """
        return self._bgp_session_config

    @bgp_session_config.setter
    def bgp_session_config(self, bgp_session_config):
        """
        Sets the bgp_session_config of this UpdateIPSecConnectionTunnelDetails.
        Information for establishing a BGP session for the IPSec tunnel.


        :param bgp_session_config: The bgp_session_config of this UpdateIPSecConnectionTunnelDetails.
        :type: UpdateIPSecTunnelBgpSessionDetails
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
