# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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

    #: A constant which can be used with the status property of a IPSecConnectionTunnel.
    #: This constant has a value of "PARTIAL_UP"
    STATUS_PARTIAL_UP = "PARTIAL_UP"

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

    #: A constant which can be used with the routing property of a IPSecConnectionTunnel.
    #: This constant has a value of "POLICY"
    ROUTING_POLICY = "POLICY"

    #: A constant which can be used with the oracle_can_initiate property of a IPSecConnectionTunnel.
    #: This constant has a value of "INITIATOR_OR_RESPONDER"
    ORACLE_CAN_INITIATE_INITIATOR_OR_RESPONDER = "INITIATOR_OR_RESPONDER"

    #: A constant which can be used with the oracle_can_initiate property of a IPSecConnectionTunnel.
    #: This constant has a value of "RESPONDER_ONLY"
    ORACLE_CAN_INITIATE_RESPONDER_ONLY = "RESPONDER_ONLY"

    #: A constant which can be used with the nat_translation_enabled property of a IPSecConnectionTunnel.
    #: This constant has a value of "ENABLED"
    NAT_TRANSLATION_ENABLED_ENABLED = "ENABLED"

    #: A constant which can be used with the nat_translation_enabled property of a IPSecConnectionTunnel.
    #: This constant has a value of "DISABLED"
    NAT_TRANSLATION_ENABLED_DISABLED = "DISABLED"

    #: A constant which can be used with the nat_translation_enabled property of a IPSecConnectionTunnel.
    #: This constant has a value of "AUTO"
    NAT_TRANSLATION_ENABLED_AUTO = "AUTO"

    #: A constant which can be used with the dpd_mode property of a IPSecConnectionTunnel.
    #: This constant has a value of "INITIATE_AND_RESPOND"
    DPD_MODE_INITIATE_AND_RESPOND = "INITIATE_AND_RESPOND"

    #: A constant which can be used with the dpd_mode property of a IPSecConnectionTunnel.
    #: This constant has a value of "RESPOND_ONLY"
    DPD_MODE_RESPOND_ONLY = "RESPOND_ONLY"

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
            Allowed values for this property are: "UP", "DOWN", "DOWN_FOR_MAINTENANCE", "PARTIAL_UP", 'UNKNOWN_ENUM_VALUE'.
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
        :type bgp_session_info: oci.core.models.BgpSessionInfo

        :param encryption_domain_config:
            The value to assign to the encryption_domain_config property of this IPSecConnectionTunnel.
        :type encryption_domain_config: oci.core.models.EncryptionDomainConfig

        :param routing:
            The value to assign to the routing property of this IPSecConnectionTunnel.
            Allowed values for this property are: "BGP", "STATIC", "POLICY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type routing: str

        :param time_created:
            The value to assign to the time_created property of this IPSecConnectionTunnel.
        :type time_created: datetime

        :param time_status_updated:
            The value to assign to the time_status_updated property of this IPSecConnectionTunnel.
        :type time_status_updated: datetime

        :param oracle_can_initiate:
            The value to assign to the oracle_can_initiate property of this IPSecConnectionTunnel.
            Allowed values for this property are: "INITIATOR_OR_RESPONDER", "RESPONDER_ONLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type oracle_can_initiate: str

        :param nat_translation_enabled:
            The value to assign to the nat_translation_enabled property of this IPSecConnectionTunnel.
            Allowed values for this property are: "ENABLED", "DISABLED", "AUTO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type nat_translation_enabled: str

        :param dpd_mode:
            The value to assign to the dpd_mode property of this IPSecConnectionTunnel.
            Allowed values for this property are: "INITIATE_AND_RESPOND", "RESPOND_ONLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dpd_mode: str

        :param dpd_timeout_in_sec:
            The value to assign to the dpd_timeout_in_sec property of this IPSecConnectionTunnel.
        :type dpd_timeout_in_sec: int

        :param phase_one_details:
            The value to assign to the phase_one_details property of this IPSecConnectionTunnel.
        :type phase_one_details: oci.core.models.TunnelPhaseOneDetails

        :param phase_two_details:
            The value to assign to the phase_two_details property of this IPSecConnectionTunnel.
        :type phase_two_details: oci.core.models.TunnelPhaseTwoDetails

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
            'encryption_domain_config': 'EncryptionDomainConfig',
            'routing': 'str',
            'time_created': 'datetime',
            'time_status_updated': 'datetime',
            'oracle_can_initiate': 'str',
            'nat_translation_enabled': 'str',
            'dpd_mode': 'str',
            'dpd_timeout_in_sec': 'int',
            'phase_one_details': 'TunnelPhaseOneDetails',
            'phase_two_details': 'TunnelPhaseTwoDetails'
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
            'encryption_domain_config': 'encryptionDomainConfig',
            'routing': 'routing',
            'time_created': 'timeCreated',
            'time_status_updated': 'timeStatusUpdated',
            'oracle_can_initiate': 'oracleCanInitiate',
            'nat_translation_enabled': 'natTranslationEnabled',
            'dpd_mode': 'dpdMode',
            'dpd_timeout_in_sec': 'dpdTimeoutInSec',
            'phase_one_details': 'phaseOneDetails',
            'phase_two_details': 'phaseTwoDetails'
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
        self._encryption_domain_config = None
        self._routing = None
        self._time_created = None
        self._time_status_updated = None
        self._oracle_can_initiate = None
        self._nat_translation_enabled = None
        self._dpd_mode = None
        self._dpd_timeout_in_sec = None
        self._phase_one_details = None
        self._phase_two_details = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IPSecConnectionTunnel.
        The `OCID`__ of the compartment containing the tunnel.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnectionTunnel.
        The `OCID`__ of the compartment containing the tunnel.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this IPSecConnectionTunnel.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IPSecConnectionTunnel.
        The `OCID`__ of the tunnel.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnectionTunnel.
        The `OCID`__ of the tunnel.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


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

        Allowed values for this property are: "UP", "DOWN", "DOWN_FOR_MAINTENANCE", "PARTIAL_UP", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["UP", "DOWN", "DOWN_FOR_MAINTENANCE", "PARTIAL_UP"]
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
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IPSecConnectionTunnel.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this IPSecConnectionTunnel.
        :type: str
        """
        self._display_name = display_name

    @property
    def bgp_session_info(self):
        """
        Gets the bgp_session_info of this IPSecConnectionTunnel.

        :return: The bgp_session_info of this IPSecConnectionTunnel.
        :rtype: oci.core.models.BgpSessionInfo
        """
        return self._bgp_session_info

    @bgp_session_info.setter
    def bgp_session_info(self, bgp_session_info):
        """
        Sets the bgp_session_info of this IPSecConnectionTunnel.

        :param bgp_session_info: The bgp_session_info of this IPSecConnectionTunnel.
        :type: oci.core.models.BgpSessionInfo
        """
        self._bgp_session_info = bgp_session_info

    @property
    def encryption_domain_config(self):
        """
        Gets the encryption_domain_config of this IPSecConnectionTunnel.

        :return: The encryption_domain_config of this IPSecConnectionTunnel.
        :rtype: oci.core.models.EncryptionDomainConfig
        """
        return self._encryption_domain_config

    @encryption_domain_config.setter
    def encryption_domain_config(self, encryption_domain_config):
        """
        Sets the encryption_domain_config of this IPSecConnectionTunnel.

        :param encryption_domain_config: The encryption_domain_config of this IPSecConnectionTunnel.
        :type: oci.core.models.EncryptionDomainConfig
        """
        self._encryption_domain_config = encryption_domain_config

    @property
    def routing(self):
        """
        Gets the routing of this IPSecConnectionTunnel.
        The type of routing used for this tunnel (either BGP dynamic routing or static routing).

        Allowed values for this property are: "BGP", "STATIC", "POLICY", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["BGP", "STATIC", "POLICY"]
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

    @property
    def oracle_can_initiate(self):
        """
        Gets the oracle_can_initiate of this IPSecConnectionTunnel.
        Indicates whether Oracle can either initiate the tunnel or respond, or respond only.

        Allowed values for this property are: "INITIATOR_OR_RESPONDER", "RESPONDER_ONLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The oracle_can_initiate of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._oracle_can_initiate

    @oracle_can_initiate.setter
    def oracle_can_initiate(self, oracle_can_initiate):
        """
        Sets the oracle_can_initiate of this IPSecConnectionTunnel.
        Indicates whether Oracle can either initiate the tunnel or respond, or respond only.


        :param oracle_can_initiate: The oracle_can_initiate of this IPSecConnectionTunnel.
        :type: str
        """
        allowed_values = ["INITIATOR_OR_RESPONDER", "RESPONDER_ONLY"]
        if not value_allowed_none_or_none_sentinel(oracle_can_initiate, allowed_values):
            oracle_can_initiate = 'UNKNOWN_ENUM_VALUE'
        self._oracle_can_initiate = oracle_can_initiate

    @property
    def nat_translation_enabled(self):
        """
        Gets the nat_translation_enabled of this IPSecConnectionTunnel.
        Whether NAT-T Enabled on the tunnel

        Allowed values for this property are: "ENABLED", "DISABLED", "AUTO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The nat_translation_enabled of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._nat_translation_enabled

    @nat_translation_enabled.setter
    def nat_translation_enabled(self, nat_translation_enabled):
        """
        Sets the nat_translation_enabled of this IPSecConnectionTunnel.
        Whether NAT-T Enabled on the tunnel


        :param nat_translation_enabled: The nat_translation_enabled of this IPSecConnectionTunnel.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "AUTO"]
        if not value_allowed_none_or_none_sentinel(nat_translation_enabled, allowed_values):
            nat_translation_enabled = 'UNKNOWN_ENUM_VALUE'
        self._nat_translation_enabled = nat_translation_enabled

    @property
    def dpd_mode(self):
        """
        Gets the dpd_mode of this IPSecConnectionTunnel.
        dpd mode

        Allowed values for this property are: "INITIATE_AND_RESPOND", "RESPOND_ONLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dpd_mode of this IPSecConnectionTunnel.
        :rtype: str
        """
        return self._dpd_mode

    @dpd_mode.setter
    def dpd_mode(self, dpd_mode):
        """
        Sets the dpd_mode of this IPSecConnectionTunnel.
        dpd mode


        :param dpd_mode: The dpd_mode of this IPSecConnectionTunnel.
        :type: str
        """
        allowed_values = ["INITIATE_AND_RESPOND", "RESPOND_ONLY"]
        if not value_allowed_none_or_none_sentinel(dpd_mode, allowed_values):
            dpd_mode = 'UNKNOWN_ENUM_VALUE'
        self._dpd_mode = dpd_mode

    @property
    def dpd_timeout_in_sec(self):
        """
        Gets the dpd_timeout_in_sec of this IPSecConnectionTunnel.
        Dead peer detection (DPD) timeout in seconds.


        :return: The dpd_timeout_in_sec of this IPSecConnectionTunnel.
        :rtype: int
        """
        return self._dpd_timeout_in_sec

    @dpd_timeout_in_sec.setter
    def dpd_timeout_in_sec(self, dpd_timeout_in_sec):
        """
        Sets the dpd_timeout_in_sec of this IPSecConnectionTunnel.
        Dead peer detection (DPD) timeout in seconds.


        :param dpd_timeout_in_sec: The dpd_timeout_in_sec of this IPSecConnectionTunnel.
        :type: int
        """
        self._dpd_timeout_in_sec = dpd_timeout_in_sec

    @property
    def phase_one_details(self):
        """
        Gets the phase_one_details of this IPSecConnectionTunnel.

        :return: The phase_one_details of this IPSecConnectionTunnel.
        :rtype: oci.core.models.TunnelPhaseOneDetails
        """
        return self._phase_one_details

    @phase_one_details.setter
    def phase_one_details(self, phase_one_details):
        """
        Sets the phase_one_details of this IPSecConnectionTunnel.

        :param phase_one_details: The phase_one_details of this IPSecConnectionTunnel.
        :type: oci.core.models.TunnelPhaseOneDetails
        """
        self._phase_one_details = phase_one_details

    @property
    def phase_two_details(self):
        """
        Gets the phase_two_details of this IPSecConnectionTunnel.

        :return: The phase_two_details of this IPSecConnectionTunnel.
        :rtype: oci.core.models.TunnelPhaseTwoDetails
        """
        return self._phase_two_details

    @phase_two_details.setter
    def phase_two_details(self, phase_two_details):
        """
        Sets the phase_two_details of this IPSecConnectionTunnel.

        :param phase_two_details: The phase_two_details of this IPSecConnectionTunnel.
        :type: oci.core.models.TunnelPhaseTwoDetails
        """
        self._phase_two_details = phase_two_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
