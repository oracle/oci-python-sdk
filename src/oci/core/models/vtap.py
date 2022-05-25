# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Vtap(object):
    """
    A virtual test access point (VTAP) provides a way to mirror all traffic from a designated source to a selected target in order to facilitate troubleshooting, security analysis, and data monitoring.
    A VTAP is functionally similar to a test access point (TAP) you might deploy in your on-premises network.

    A *:class:`CaptureFilter`* contains a set of *:func:`capture_filter_rule_details`* governing what traffic a VTAP mirrors.
    """

    #: A constant which can be used with the lifecycle_state property of a Vtap.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Vtap.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Vtap.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Vtap.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Vtap.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state_details property of a Vtap.
    #: This constant has a value of "RUNNING"
    LIFECYCLE_STATE_DETAILS_RUNNING = "RUNNING"

    #: A constant which can be used with the lifecycle_state_details property of a Vtap.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_DETAILS_STOPPED = "STOPPED"

    #: A constant which can be used with the encapsulation_protocol property of a Vtap.
    #: This constant has a value of "VXLAN"
    ENCAPSULATION_PROTOCOL_VXLAN = "VXLAN"

    #: A constant which can be used with the source_type property of a Vtap.
    #: This constant has a value of "VNIC"
    SOURCE_TYPE_VNIC = "VNIC"

    #: A constant which can be used with the source_type property of a Vtap.
    #: This constant has a value of "SUBNET"
    SOURCE_TYPE_SUBNET = "SUBNET"

    #: A constant which can be used with the source_type property of a Vtap.
    #: This constant has a value of "LOAD_BALANCER"
    SOURCE_TYPE_LOAD_BALANCER = "LOAD_BALANCER"

    #: A constant which can be used with the source_type property of a Vtap.
    #: This constant has a value of "DB_SYSTEM"
    SOURCE_TYPE_DB_SYSTEM = "DB_SYSTEM"

    #: A constant which can be used with the source_type property of a Vtap.
    #: This constant has a value of "EXADATA_VM_CLUSTER"
    SOURCE_TYPE_EXADATA_VM_CLUSTER = "EXADATA_VM_CLUSTER"

    #: A constant which can be used with the source_type property of a Vtap.
    #: This constant has a value of "AUTONOMOUS_DATA_WAREHOUSE"
    SOURCE_TYPE_AUTONOMOUS_DATA_WAREHOUSE = "AUTONOMOUS_DATA_WAREHOUSE"

    #: A constant which can be used with the traffic_mode property of a Vtap.
    #: This constant has a value of "DEFAULT"
    TRAFFIC_MODE_DEFAULT = "DEFAULT"

    #: A constant which can be used with the traffic_mode property of a Vtap.
    #: This constant has a value of "PRIORITY"
    TRAFFIC_MODE_PRIORITY = "PRIORITY"

    #: A constant which can be used with the target_type property of a Vtap.
    #: This constant has a value of "VNIC"
    TARGET_TYPE_VNIC = "VNIC"

    #: A constant which can be used with the target_type property of a Vtap.
    #: This constant has a value of "NETWORK_LOAD_BALANCER"
    TARGET_TYPE_NETWORK_LOAD_BALANCER = "NETWORK_LOAD_BALANCER"

    #: A constant which can be used with the target_type property of a Vtap.
    #: This constant has a value of "IP_ADDRESS"
    TARGET_TYPE_IP_ADDRESS = "IP_ADDRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new Vtap object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Vtap.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this Vtap.
        :type vcn_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Vtap.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Vtap.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Vtap.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Vtap.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Vtap.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this Vtap.
            Allowed values for this property are: "RUNNING", "STOPPED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state_details: str

        :param time_created:
            The value to assign to the time_created property of this Vtap.
        :type time_created: datetime

        :param source_id:
            The value to assign to the source_id property of this Vtap.
        :type source_id: str

        :param target_id:
            The value to assign to the target_id property of this Vtap.
        :type target_id: str

        :param target_ip:
            The value to assign to the target_ip property of this Vtap.
        :type target_ip: str

        :param capture_filter_id:
            The value to assign to the capture_filter_id property of this Vtap.
        :type capture_filter_id: str

        :param encapsulation_protocol:
            The value to assign to the encapsulation_protocol property of this Vtap.
            Allowed values for this property are: "VXLAN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type encapsulation_protocol: str

        :param vxlan_network_identifier:
            The value to assign to the vxlan_network_identifier property of this Vtap.
        :type vxlan_network_identifier: int

        :param is_vtap_enabled:
            The value to assign to the is_vtap_enabled property of this Vtap.
        :type is_vtap_enabled: bool

        :param source_type:
            The value to assign to the source_type property of this Vtap.
            Allowed values for this property are: "VNIC", "SUBNET", "LOAD_BALANCER", "DB_SYSTEM", "EXADATA_VM_CLUSTER", "AUTONOMOUS_DATA_WAREHOUSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param traffic_mode:
            The value to assign to the traffic_mode property of this Vtap.
            Allowed values for this property are: "DEFAULT", "PRIORITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type traffic_mode: str

        :param max_packet_size:
            The value to assign to the max_packet_size property of this Vtap.
        :type max_packet_size: int

        :param target_type:
            The value to assign to the target_type property of this Vtap.
            Allowed values for this property are: "VNIC", "NETWORK_LOAD_BALANCER", "IP_ADDRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_type: str

        :param source_private_endpoint_ip:
            The value to assign to the source_private_endpoint_ip property of this Vtap.
        :type source_private_endpoint_ip: str

        :param source_private_endpoint_subnet_id:
            The value to assign to the source_private_endpoint_subnet_id property of this Vtap.
        :type source_private_endpoint_subnet_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'vcn_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'time_created': 'datetime',
            'source_id': 'str',
            'target_id': 'str',
            'target_ip': 'str',
            'capture_filter_id': 'str',
            'encapsulation_protocol': 'str',
            'vxlan_network_identifier': 'int',
            'is_vtap_enabled': 'bool',
            'source_type': 'str',
            'traffic_mode': 'str',
            'max_packet_size': 'int',
            'target_type': 'str',
            'source_private_endpoint_ip': 'str',
            'source_private_endpoint_subnet_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'time_created': 'timeCreated',
            'source_id': 'sourceId',
            'target_id': 'targetId',
            'target_ip': 'targetIp',
            'capture_filter_id': 'captureFilterId',
            'encapsulation_protocol': 'encapsulationProtocol',
            'vxlan_network_identifier': 'vxlanNetworkIdentifier',
            'is_vtap_enabled': 'isVtapEnabled',
            'source_type': 'sourceType',
            'traffic_mode': 'trafficMode',
            'max_packet_size': 'maxPacketSize',
            'target_type': 'targetType',
            'source_private_endpoint_ip': 'sourcePrivateEndpointIp',
            'source_private_endpoint_subnet_id': 'sourcePrivateEndpointSubnetId'
        }

        self._compartment_id = None
        self._vcn_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._time_created = None
        self._source_id = None
        self._target_id = None
        self._target_ip = None
        self._capture_filter_id = None
        self._encapsulation_protocol = None
        self._vxlan_network_identifier = None
        self._is_vtap_enabled = None
        self._source_type = None
        self._traffic_mode = None
        self._max_packet_size = None
        self._target_type = None
        self._source_private_endpoint_ip = None
        self._source_private_endpoint_subnet_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Vtap.
        The `OCID`__ of the compartment containing the `Vtap` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Vtap.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vtap.
        The `OCID`__ of the compartment containing the `Vtap` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Vtap.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this Vtap.
        The `OCID`__ of the VCN containing the `Vtap` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this Vtap.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this Vtap.
        The `OCID`__ of the VCN containing the `Vtap` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this Vtap.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Vtap.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Vtap.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Vtap.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Vtap.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this Vtap.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Vtap.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vtap.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Vtap.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Vtap.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Vtap.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Vtap.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Vtap.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Vtap.
        The VTAP's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Vtap.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vtap.
        The VTAP's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Vtap.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Vtap.
        The VTAP's administrative lifecycle state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Vtap.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Vtap.
        The VTAP's administrative lifecycle state.


        :param lifecycle_state: The lifecycle_state of this Vtap.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this Vtap.
        The VTAP's current running state.

        Allowed values for this property are: "RUNNING", "STOPPED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state_details of this Vtap.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this Vtap.
        The VTAP's current running state.


        :param lifecycle_state_details: The lifecycle_state_details of this Vtap.
        :type: str
        """
        allowed_values = ["RUNNING", "STOPPED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state_details, allowed_values):
            lifecycle_state_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def time_created(self):
        """
        Gets the time_created of this Vtap.
        The date and time the VTAP was created, in the format defined by `RFC3339`__.

        Example: `2020-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Vtap.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vtap.
        The date and time the VTAP was created, in the format defined by `RFC3339`__.

        Example: `2020-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Vtap.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def source_id(self):
        """
        **[Required]** Gets the source_id of this Vtap.
        The `OCID`__ of the source point where packets are captured.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_id of this Vtap.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this Vtap.
        The `OCID`__ of the source point where packets are captured.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this Vtap.
        :type: str
        """
        self._source_id = source_id

    @property
    def target_id(self):
        """
        Gets the target_id of this Vtap.
        The `OCID`__ of the destination resource where mirrored packets are sent.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The target_id of this Vtap.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this Vtap.
        The `OCID`__ of the destination resource where mirrored packets are sent.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param target_id: The target_id of this Vtap.
        :type: str
        """
        self._target_id = target_id

    @property
    def target_ip(self):
        """
        Gets the target_ip of this Vtap.
        The IP address of the destination resource where mirrored packets are sent.


        :return: The target_ip of this Vtap.
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        """
        Sets the target_ip of this Vtap.
        The IP address of the destination resource where mirrored packets are sent.


        :param target_ip: The target_ip of this Vtap.
        :type: str
        """
        self._target_ip = target_ip

    @property
    def capture_filter_id(self):
        """
        **[Required]** Gets the capture_filter_id of this Vtap.
        The capture filter's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The capture_filter_id of this Vtap.
        :rtype: str
        """
        return self._capture_filter_id

    @capture_filter_id.setter
    def capture_filter_id(self, capture_filter_id):
        """
        Sets the capture_filter_id of this Vtap.
        The capture filter's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param capture_filter_id: The capture_filter_id of this Vtap.
        :type: str
        """
        self._capture_filter_id = capture_filter_id

    @property
    def encapsulation_protocol(self):
        """
        Gets the encapsulation_protocol of this Vtap.
        Defines an encapsulation header type for the VTAP's mirrored traffic.

        Allowed values for this property are: "VXLAN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The encapsulation_protocol of this Vtap.
        :rtype: str
        """
        return self._encapsulation_protocol

    @encapsulation_protocol.setter
    def encapsulation_protocol(self, encapsulation_protocol):
        """
        Sets the encapsulation_protocol of this Vtap.
        Defines an encapsulation header type for the VTAP's mirrored traffic.


        :param encapsulation_protocol: The encapsulation_protocol of this Vtap.
        :type: str
        """
        allowed_values = ["VXLAN"]
        if not value_allowed_none_or_none_sentinel(encapsulation_protocol, allowed_values):
            encapsulation_protocol = 'UNKNOWN_ENUM_VALUE'
        self._encapsulation_protocol = encapsulation_protocol

    @property
    def vxlan_network_identifier(self):
        """
        Gets the vxlan_network_identifier of this Vtap.
        The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.


        :return: The vxlan_network_identifier of this Vtap.
        :rtype: int
        """
        return self._vxlan_network_identifier

    @vxlan_network_identifier.setter
    def vxlan_network_identifier(self, vxlan_network_identifier):
        """
        Sets the vxlan_network_identifier of this Vtap.
        The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.


        :param vxlan_network_identifier: The vxlan_network_identifier of this Vtap.
        :type: int
        """
        self._vxlan_network_identifier = vxlan_network_identifier

    @property
    def is_vtap_enabled(self):
        """
        Gets the is_vtap_enabled of this Vtap.
        Used to start or stop a `Vtap` resource.

        * `TRUE` directs the VTAP to start mirroring traffic.
        * `FALSE` (Default) directs the VTAP to stop mirroring traffic.


        :return: The is_vtap_enabled of this Vtap.
        :rtype: bool
        """
        return self._is_vtap_enabled

    @is_vtap_enabled.setter
    def is_vtap_enabled(self, is_vtap_enabled):
        """
        Sets the is_vtap_enabled of this Vtap.
        Used to start or stop a `Vtap` resource.

        * `TRUE` directs the VTAP to start mirroring traffic.
        * `FALSE` (Default) directs the VTAP to stop mirroring traffic.


        :param is_vtap_enabled: The is_vtap_enabled of this Vtap.
        :type: bool
        """
        self._is_vtap_enabled = is_vtap_enabled

    @property
    def source_type(self):
        """
        Gets the source_type of this Vtap.
        The source type for the VTAP.

        Allowed values for this property are: "VNIC", "SUBNET", "LOAD_BALANCER", "DB_SYSTEM", "EXADATA_VM_CLUSTER", "AUTONOMOUS_DATA_WAREHOUSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this Vtap.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this Vtap.
        The source type for the VTAP.


        :param source_type: The source_type of this Vtap.
        :type: str
        """
        allowed_values = ["VNIC", "SUBNET", "LOAD_BALANCER", "DB_SYSTEM", "EXADATA_VM_CLUSTER", "AUTONOMOUS_DATA_WAREHOUSE"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    @property
    def traffic_mode(self):
        """
        Gets the traffic_mode of this Vtap.
        Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT

        Allowed values for this property are: "DEFAULT", "PRIORITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The traffic_mode of this Vtap.
        :rtype: str
        """
        return self._traffic_mode

    @traffic_mode.setter
    def traffic_mode(self, traffic_mode):
        """
        Sets the traffic_mode of this Vtap.
        Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT


        :param traffic_mode: The traffic_mode of this Vtap.
        :type: str
        """
        allowed_values = ["DEFAULT", "PRIORITY"]
        if not value_allowed_none_or_none_sentinel(traffic_mode, allowed_values):
            traffic_mode = 'UNKNOWN_ENUM_VALUE'
        self._traffic_mode = traffic_mode

    @property
    def max_packet_size(self):
        """
        Gets the max_packet_size of this Vtap.
        The maximum size of the packets to be included in the filter.


        :return: The max_packet_size of this Vtap.
        :rtype: int
        """
        return self._max_packet_size

    @max_packet_size.setter
    def max_packet_size(self, max_packet_size):
        """
        Sets the max_packet_size of this Vtap.
        The maximum size of the packets to be included in the filter.


        :param max_packet_size: The max_packet_size of this Vtap.
        :type: int
        """
        self._max_packet_size = max_packet_size

    @property
    def target_type(self):
        """
        Gets the target_type of this Vtap.
        The target type for the VTAP.

        Allowed values for this property are: "VNIC", "NETWORK_LOAD_BALANCER", "IP_ADDRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_type of this Vtap.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this Vtap.
        The target type for the VTAP.


        :param target_type: The target_type of this Vtap.
        :type: str
        """
        allowed_values = ["VNIC", "NETWORK_LOAD_BALANCER", "IP_ADDRESS"]
        if not value_allowed_none_or_none_sentinel(target_type, allowed_values):
            target_type = 'UNKNOWN_ENUM_VALUE'
        self._target_type = target_type

    @property
    def source_private_endpoint_ip(self):
        """
        Gets the source_private_endpoint_ip of this Vtap.
        The IP Address of the source private endpoint.


        :return: The source_private_endpoint_ip of this Vtap.
        :rtype: str
        """
        return self._source_private_endpoint_ip

    @source_private_endpoint_ip.setter
    def source_private_endpoint_ip(self, source_private_endpoint_ip):
        """
        Sets the source_private_endpoint_ip of this Vtap.
        The IP Address of the source private endpoint.


        :param source_private_endpoint_ip: The source_private_endpoint_ip of this Vtap.
        :type: str
        """
        self._source_private_endpoint_ip = source_private_endpoint_ip

    @property
    def source_private_endpoint_subnet_id(self):
        """
        Gets the source_private_endpoint_subnet_id of this Vtap.
        The `OCID`__ of the subnet that source private endpoint belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_private_endpoint_subnet_id of this Vtap.
        :rtype: str
        """
        return self._source_private_endpoint_subnet_id

    @source_private_endpoint_subnet_id.setter
    def source_private_endpoint_subnet_id(self, source_private_endpoint_subnet_id):
        """
        Sets the source_private_endpoint_subnet_id of this Vtap.
        The `OCID`__ of the subnet that source private endpoint belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_private_endpoint_subnet_id: The source_private_endpoint_subnet_id of this Vtap.
        :type: str
        """
        self._source_private_endpoint_subnet_id = source_private_endpoint_subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
