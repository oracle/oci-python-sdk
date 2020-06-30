# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IPSecConnectionTunnel(object):
    """
    Information about a single tunnel in an IPSec connection. This object does not include the tunnel's
    shared secret (pre-shared key). That is in the
    :class:`IPSecConnectionTunnelSharedSecret` object.
    """

    #: A constant which can be used with the status property of a IPSecConnectionTunnel.
    #: This constant has a value of "UP"
    STATUS_UP = "UP"

    #: A constant which can be used with the status property of a IPSecConnectionTunnel.
    #: This constant has a value of "DOWN"
    STATUS_DOWN = "DOWN"

    #: A constant which can be used with the status property of a IPSecConnectionTunnel.
    #: This constant has a value of "DOWN_FOR_MAINTENANCE"
    STATUS_DOWN_FOR_MAINTENANCE = "DOWN_FOR_MAINTENANCE"

    #: A constant which can be used with the ike_version property of a IPSecConnectionTunnel.
    #: This constant has a value of "V1"
    IKE_VERSION_V1 = "V1"

    #: A constant which can be used with the ike_version property of a IPSecConnectionTunnel.
    #: This constant has a value of "V2"
    IKE_VERSION_V2 = "V2"

    #: A constant which can be used with the lifecycle_state property of a IPSecConnectionTunnel.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a IPSecConnectionTunnel.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a IPSecConnectionTunnel.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a IPSecConnectionTunnel.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the routing property of a IPSecConnectionTunnel.
    #: This constant has a value of "BGP"
    ROUTING_BGP = "BGP"

    #: A constant which can be used with the routing property of a IPSecConnectionTunnel.
    #: This constant has a value of "STATIC"
    ROUTING_STATIC = "STATIC"

    def __init__(self, **kwargs):
        """
        Initializes a new IPSecConnectionTunnel object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this IPSecConnectionTunnel.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this IPSecConnectionTunnel.
        :type id: str

        :param vpn_ip:
            The value to assign to the vpn_ip property of this IPSecConnectionTunnel.
        :type vpn_ip: str

        :param cpe_ip:
            The value to assign to the cpe_ip property of this IPSecConnectionTunnel.
        :type cpe_ip: str

        :param status:
            The value to assign to the status property of this IPSecConnectionTunnel.
            Allowed values for this property are: "UP", "DOWN", "DOWN_FOR_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param ike_version:
            The value to assign to the ike_version property of this IPSecConnectionTunnel.
            Allowed values for this property are: "V1", "V2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ike_version: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IPSecConnectionTunnel.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this IPSecConnectionTunnel.
        :type display_name: str

        :param bgp_session_info:
            The value to assign to the bgp_session_info property of this IPSecConnectionTunnel.
        :type bgp_session_info: BgpSessionInfo

        :param routing:
            The value to assign to the routing property of this IPSecConnectionTunnel.
            Allowed values for this property are: "BGP", "STATIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type routing: str

        :param time_created:
            The value to assign to the time_created property of this IPSecConnectionTunnel.
        :type time_created: datetime

        :param time_status_updated:
            The value to assign to the time_status_updated property of this IPSecConnectionTunnel.
        :type time_status_updated: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'vpn_ip': 'str',
            'cpe_ip': 'str',
            'status': 'str',
            'ike_version': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'bgp_session_info': 'BgpSessionInfo',
            'routing': 'str',
            'time_created': 'datetime',
            'time_status_updated': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'id': 'id',
            'vpn_ip': 'vpnIp',
            'cpe_ip': 'cpeIp',
            'status': 'status',
            'ike_version': 'ikeVersion',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'bgp_session_info': 'bgpSessionInfo',
            'routing': 'routing',
            'time_created': 'timeCreated',
            'time_status_updated': 'timeStatusUpdated'
        }

        self._compartment_id = None
        self._id = None
        self._vpn_ip = None
        self._cpe_ip = None
        self._status = None
        self._ike_version = None
        self._lifecycle_state = None
        self._display_name = None
        self._bgp_session_info = None
        self._routing = None
        self._time_created = None
        self._time_status_updated = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IPSecConnectionTunnel.
        The `OCID`__ of the compartment containing the tunnel.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnectionTunnel.
        The `OCID`__ of the compartment containing the tunnel.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this IPSecConnectionTunnel.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IPSecConnectionTunnel.
        The `OCID`__ of the tunnel.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnectionTunnel.
        The `OCID`__ of the tunnel.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this IPSecConnectionTunnel.
        :type: str
        """
        self._id = id

    @property
    def vpn_ip(self):
        """
        Gets the vpn_ip of this IPSecConnectionTunnel.
        The IP address of Oracle's VPN headend.

        Example: `203.0.113.21`


        :return: The vpn_ip of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._vpn_ip

    @vpn_ip.setter
    def vpn_ip(self, vpn_ip):
        """
        Sets the vpn_ip of this IPSecConnectionTunnel.
        The IP address of Oracle's VPN headend.

        Example: `203.0.113.21`


        :param vpn_ip: The vpn_ip of this IPSecConnectionTunnel.
        :type: str
        """
        self._vpn_ip = vpn_ip

    @property
    def cpe_ip(self):
        """
        Gets the cpe_ip of this IPSecConnectionTunnel.
        The IP address of the CPE's VPN headend.

        Example: `203.0.113.22`


        :return: The cpe_ip of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._cpe_ip

    @cpe_ip.setter
    def cpe_ip(self, cpe_ip):
        """
        Sets the cpe_ip of this IPSecConnectionTunnel.
        The IP address of the CPE's VPN headend.

        Example: `203.0.113.22`


        :param cpe_ip: The cpe_ip of this IPSecConnectionTunnel.
        :type: str
        """
        self._cpe_ip = cpe_ip

    @property
    def status(self):
        """
        Gets the status of this IPSecConnectionTunnel.
        The status of the tunnel based on IPSec protocol characteristics.

        Allowed values for this property are: "UP", "DOWN", "DOWN_FOR_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this IPSecConnectionTunnel.
        The status of the tunnel based on IPSec protocol characteristics.


        :param status: The status of this IPSecConnectionTunnel.
        :type: str
        """
        allowed_values = ["UP", "DOWN", "DOWN_FOR_MAINTENANCE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def ike_version(self):
        """
        Gets the ike_version of this IPSecConnectionTunnel.
        Internet Key Exchange protocol version.

        Allowed values for this property are: "V1", "V2", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ike_version of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._ike_version

    @ike_version.setter
    def ike_version(self, ike_version):
        """
        Sets the ike_version of this IPSecConnectionTunnel.
        Internet Key Exchange protocol version.


        :param ike_version: The ike_version of this IPSecConnectionTunnel.
        :type: str
        """
        allowed_values = ["V1", "V2"]
        if not value_allowed_none_or_none_sentinel(ike_version, allowed_values):
            ike_version = 'UNKNOWN_ENUM_VALUE'
        self._ike_version = ike_version

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this IPSecConnectionTunnel.
        The tunnel's lifecycle state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IPSecConnectionTunnel.
        The tunnel's lifecycle state.


        :param lifecycle_state: The lifecycle_state of this IPSecConnectionTunnel.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        Gets the display_name of this IPSecConnectionTunnel.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IPSecConnectionTunnel.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this IPSecConnectionTunnel.
        :type: str
        """
        self._display_name = display_name

    @property
    def bgp_session_info(self):
        """
        Gets the bgp_session_info of this IPSecConnectionTunnel.
        Information for establishing the tunnel's BGP session.


        :return: The bgp_session_info of this IPSecConnectionTunnel.
        :rtype: BgpSessionInfo
        """
        return self._bgp_session_info

    @bgp_session_info.setter
    def bgp_session_info(self, bgp_session_info):
        """
        Sets the bgp_session_info of this IPSecConnectionTunnel.
        Information for establishing the tunnel's BGP session.


        :param bgp_session_info: The bgp_session_info of this IPSecConnectionTunnel.
        :type: BgpSessionInfo
        """
        self._bgp_session_info = bgp_session_info

    @property
    def routing(self):
        """
        Gets the routing of this IPSecConnectionTunnel.
        The type of routing used for this tunnel (either BGP dynamic routing or static routing).

        Allowed values for this property are: "BGP", "STATIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The routing of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """
        Sets the routing of this IPSecConnectionTunnel.
        The type of routing used for this tunnel (either BGP dynamic routing or static routing).


        :param routing: The routing of this IPSecConnectionTunnel.
        :type: str
        """
        allowed_values = ["BGP", "STATIC"]
        if not value_allowed_none_or_none_sentinel(routing, allowed_values):
            routing = 'UNKNOWN_ENUM_VALUE'
        self._routing = routing

    @property
    def time_created(self):
        """
        Gets the time_created of this IPSecConnectionTunnel.
        The date and time the IPSec connection tunnel was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this IPSecConnectionTunnel.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IPSecConnectionTunnel.
        The date and time the IPSec connection tunnel was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this IPSecConnectionTunnel.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_status_updated(self):
        """
        Gets the time_status_updated of this IPSecConnectionTunnel.
        When the status of the tunnel last changed, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_status_updated of this IPSecConnectionTunnel.
        :rtype: datetime
        """
        return self._time_status_updated

    @time_status_updated.setter
    def time_status_updated(self, time_status_updated):
        """
        Sets the time_status_updated of this IPSecConnectionTunnel.
        When the status of the tunnel last changed, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_status_updated: The time_status_updated of this IPSecConnectionTunnel.
        :type: datetime
        """
        self._time_status_updated = time_status_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
