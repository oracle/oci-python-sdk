# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVtapDetails(object):
    """
    These details can be included in a request to update a virtual test access point (VTAP).
    """

    #: A constant which can be used with the encapsulation_protocol property of a UpdateVtapDetails.
    #: This constant has a value of "VXLAN"
    ENCAPSULATION_PROTOCOL_VXLAN = "VXLAN"

    #: A constant which can be used with the traffic_mode property of a UpdateVtapDetails.
    #: This constant has a value of "DEFAULT"
    TRAFFIC_MODE_DEFAULT = "DEFAULT"

    #: A constant which can be used with the traffic_mode property of a UpdateVtapDetails.
    #: This constant has a value of "PRIORITY"
    TRAFFIC_MODE_PRIORITY = "PRIORITY"

    #: A constant which can be used with the target_type property of a UpdateVtapDetails.
    #: This constant has a value of "VNIC"
    TARGET_TYPE_VNIC = "VNIC"

    #: A constant which can be used with the target_type property of a UpdateVtapDetails.
    #: This constant has a value of "NETWORK_LOAD_BALANCER"
    TARGET_TYPE_NETWORK_LOAD_BALANCER = "NETWORK_LOAD_BALANCER"

    #: A constant which can be used with the target_type property of a UpdateVtapDetails.
    #: This constant has a value of "IP_ADDRESS"
    TARGET_TYPE_IP_ADDRESS = "IP_ADDRESS"

    #: A constant which can be used with the source_type property of a UpdateVtapDetails.
    #: This constant has a value of "VNIC"
    SOURCE_TYPE_VNIC = "VNIC"

    #: A constant which can be used with the source_type property of a UpdateVtapDetails.
    #: This constant has a value of "SUBNET"
    SOURCE_TYPE_SUBNET = "SUBNET"

    #: A constant which can be used with the source_type property of a UpdateVtapDetails.
    #: This constant has a value of "LOAD_BALANCER"
    SOURCE_TYPE_LOAD_BALANCER = "LOAD_BALANCER"

    #: A constant which can be used with the source_type property of a UpdateVtapDetails.
    #: This constant has a value of "DB_SYSTEM"
    SOURCE_TYPE_DB_SYSTEM = "DB_SYSTEM"

    #: A constant which can be used with the source_type property of a UpdateVtapDetails.
    #: This constant has a value of "EXADATA_VM_CLUSTER"
    SOURCE_TYPE_EXADATA_VM_CLUSTER = "EXADATA_VM_CLUSTER"

    #: A constant which can be used with the source_type property of a UpdateVtapDetails.
    #: This constant has a value of "AUTONOMOUS_DATA_WAREHOUSE"
    SOURCE_TYPE_AUTONOMOUS_DATA_WAREHOUSE = "AUTONOMOUS_DATA_WAREHOUSE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVtapDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVtapDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateVtapDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVtapDetails.
        :type freeform_tags: dict(str, str)

        :param source_id:
            The value to assign to the source_id property of this UpdateVtapDetails.
        :type source_id: str

        :param target_id:
            The value to assign to the target_id property of this UpdateVtapDetails.
        :type target_id: str

        :param target_ip:
            The value to assign to the target_ip property of this UpdateVtapDetails.
        :type target_ip: str

        :param capture_filter_id:
            The value to assign to the capture_filter_id property of this UpdateVtapDetails.
        :type capture_filter_id: str

        :param encapsulation_protocol:
            The value to assign to the encapsulation_protocol property of this UpdateVtapDetails.
            Allowed values for this property are: "VXLAN"
        :type encapsulation_protocol: str

        :param vxlan_network_identifier:
            The value to assign to the vxlan_network_identifier property of this UpdateVtapDetails.
        :type vxlan_network_identifier: int

        :param is_vtap_enabled:
            The value to assign to the is_vtap_enabled property of this UpdateVtapDetails.
        :type is_vtap_enabled: bool

        :param traffic_mode:
            The value to assign to the traffic_mode property of this UpdateVtapDetails.
            Allowed values for this property are: "DEFAULT", "PRIORITY"
        :type traffic_mode: str

        :param max_packet_size:
            The value to assign to the max_packet_size property of this UpdateVtapDetails.
        :type max_packet_size: int

        :param source_private_endpoint_ip:
            The value to assign to the source_private_endpoint_ip property of this UpdateVtapDetails.
        :type source_private_endpoint_ip: str

        :param source_private_endpoint_subnet_id:
            The value to assign to the source_private_endpoint_subnet_id property of this UpdateVtapDetails.
        :type source_private_endpoint_subnet_id: str

        :param target_type:
            The value to assign to the target_type property of this UpdateVtapDetails.
            Allowed values for this property are: "VNIC", "NETWORK_LOAD_BALANCER", "IP_ADDRESS"
        :type target_type: str

        :param source_type:
            The value to assign to the source_type property of this UpdateVtapDetails.
            Allowed values for this property are: "VNIC", "SUBNET", "LOAD_BALANCER", "DB_SYSTEM", "EXADATA_VM_CLUSTER", "AUTONOMOUS_DATA_WAREHOUSE"
        :type source_type: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'source_id': 'str',
            'target_id': 'str',
            'target_ip': 'str',
            'capture_filter_id': 'str',
            'encapsulation_protocol': 'str',
            'vxlan_network_identifier': 'int',
            'is_vtap_enabled': 'bool',
            'traffic_mode': 'str',
            'max_packet_size': 'int',
            'source_private_endpoint_ip': 'str',
            'source_private_endpoint_subnet_id': 'str',
            'target_type': 'str',
            'source_type': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'source_id': 'sourceId',
            'target_id': 'targetId',
            'target_ip': 'targetIp',
            'capture_filter_id': 'captureFilterId',
            'encapsulation_protocol': 'encapsulationProtocol',
            'vxlan_network_identifier': 'vxlanNetworkIdentifier',
            'is_vtap_enabled': 'isVtapEnabled',
            'traffic_mode': 'trafficMode',
            'max_packet_size': 'maxPacketSize',
            'source_private_endpoint_ip': 'sourcePrivateEndpointIp',
            'source_private_endpoint_subnet_id': 'sourcePrivateEndpointSubnetId',
            'target_type': 'targetType',
            'source_type': 'sourceType'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._source_id = None
        self._target_id = None
        self._target_ip = None
        self._capture_filter_id = None
        self._encapsulation_protocol = None
        self._vxlan_network_identifier = None
        self._is_vtap_enabled = None
        self._traffic_mode = None
        self._max_packet_size = None
        self._source_private_endpoint_ip = None
        self._source_private_endpoint_subnet_id = None
        self._target_type = None
        self._source_type = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVtapDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateVtapDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVtapDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateVtapDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVtapDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateVtapDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVtapDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateVtapDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVtapDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateVtapDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVtapDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateVtapDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def source_id(self):
        """
        Gets the source_id of this UpdateVtapDetails.
        The `OCID`__ of the source point where packets are captured.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_id of this UpdateVtapDetails.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this UpdateVtapDetails.
        The `OCID`__ of the source point where packets are captured.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this UpdateVtapDetails.
        :type: str
        """
        self._source_id = source_id

    @property
    def target_id(self):
        """
        Gets the target_id of this UpdateVtapDetails.
        The `OCID`__ of the destination resource where mirrored packets are sent.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The target_id of this UpdateVtapDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this UpdateVtapDetails.
        The `OCID`__ of the destination resource where mirrored packets are sent.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param target_id: The target_id of this UpdateVtapDetails.
        :type: str
        """
        self._target_id = target_id

    @property
    def target_ip(self):
        """
        Gets the target_ip of this UpdateVtapDetails.
        The IP address of the destination resource where mirrored packets are sent.


        :return: The target_ip of this UpdateVtapDetails.
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        """
        Sets the target_ip of this UpdateVtapDetails.
        The IP address of the destination resource where mirrored packets are sent.


        :param target_ip: The target_ip of this UpdateVtapDetails.
        :type: str
        """
        self._target_ip = target_ip

    @property
    def capture_filter_id(self):
        """
        Gets the capture_filter_id of this UpdateVtapDetails.
        The capture filter's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The capture_filter_id of this UpdateVtapDetails.
        :rtype: str
        """
        return self._capture_filter_id

    @capture_filter_id.setter
    def capture_filter_id(self, capture_filter_id):
        """
        Sets the capture_filter_id of this UpdateVtapDetails.
        The capture filter's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param capture_filter_id: The capture_filter_id of this UpdateVtapDetails.
        :type: str
        """
        self._capture_filter_id = capture_filter_id

    @property
    def encapsulation_protocol(self):
        """
        Gets the encapsulation_protocol of this UpdateVtapDetails.
        Defines an encapsulation header type for the VTAP's mirrored traffic.

        Allowed values for this property are: "VXLAN"


        :return: The encapsulation_protocol of this UpdateVtapDetails.
        :rtype: str
        """
        return self._encapsulation_protocol

    @encapsulation_protocol.setter
    def encapsulation_protocol(self, encapsulation_protocol):
        """
        Sets the encapsulation_protocol of this UpdateVtapDetails.
        Defines an encapsulation header type for the VTAP's mirrored traffic.


        :param encapsulation_protocol: The encapsulation_protocol of this UpdateVtapDetails.
        :type: str
        """
        allowed_values = ["VXLAN"]
        if not value_allowed_none_or_none_sentinel(encapsulation_protocol, allowed_values):
            raise ValueError(
                "Invalid value for `encapsulation_protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._encapsulation_protocol = encapsulation_protocol

    @property
    def vxlan_network_identifier(self):
        """
        Gets the vxlan_network_identifier of this UpdateVtapDetails.
        The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.


        :return: The vxlan_network_identifier of this UpdateVtapDetails.
        :rtype: int
        """
        return self._vxlan_network_identifier

    @vxlan_network_identifier.setter
    def vxlan_network_identifier(self, vxlan_network_identifier):
        """
        Sets the vxlan_network_identifier of this UpdateVtapDetails.
        The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.


        :param vxlan_network_identifier: The vxlan_network_identifier of this UpdateVtapDetails.
        :type: int
        """
        self._vxlan_network_identifier = vxlan_network_identifier

    @property
    def is_vtap_enabled(self):
        """
        Gets the is_vtap_enabled of this UpdateVtapDetails.
        Used to start or stop a `Vtap` resource.

        * `TRUE` directs the VTAP to start mirroring traffic.
        * `FALSE` (Default) directs the VTAP to stop mirroring traffic.


        :return: The is_vtap_enabled of this UpdateVtapDetails.
        :rtype: bool
        """
        return self._is_vtap_enabled

    @is_vtap_enabled.setter
    def is_vtap_enabled(self, is_vtap_enabled):
        """
        Sets the is_vtap_enabled of this UpdateVtapDetails.
        Used to start or stop a `Vtap` resource.

        * `TRUE` directs the VTAP to start mirroring traffic.
        * `FALSE` (Default) directs the VTAP to stop mirroring traffic.


        :param is_vtap_enabled: The is_vtap_enabled of this UpdateVtapDetails.
        :type: bool
        """
        self._is_vtap_enabled = is_vtap_enabled

    @property
    def traffic_mode(self):
        """
        Gets the traffic_mode of this UpdateVtapDetails.
        Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT

        Allowed values for this property are: "DEFAULT", "PRIORITY"


        :return: The traffic_mode of this UpdateVtapDetails.
        :rtype: str
        """
        return self._traffic_mode

    @traffic_mode.setter
    def traffic_mode(self, traffic_mode):
        """
        Sets the traffic_mode of this UpdateVtapDetails.
        Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT


        :param traffic_mode: The traffic_mode of this UpdateVtapDetails.
        :type: str
        """
        allowed_values = ["DEFAULT", "PRIORITY"]
        if not value_allowed_none_or_none_sentinel(traffic_mode, allowed_values):
            raise ValueError(
                "Invalid value for `traffic_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._traffic_mode = traffic_mode

    @property
    def max_packet_size(self):
        """
        Gets the max_packet_size of this UpdateVtapDetails.
        The maximum size of the packets to be included in the filter.


        :return: The max_packet_size of this UpdateVtapDetails.
        :rtype: int
        """
        return self._max_packet_size

    @max_packet_size.setter
    def max_packet_size(self, max_packet_size):
        """
        Sets the max_packet_size of this UpdateVtapDetails.
        The maximum size of the packets to be included in the filter.


        :param max_packet_size: The max_packet_size of this UpdateVtapDetails.
        :type: int
        """
        self._max_packet_size = max_packet_size

    @property
    def source_private_endpoint_ip(self):
        """
        Gets the source_private_endpoint_ip of this UpdateVtapDetails.
        The IP Address of the source private endpoint.


        :return: The source_private_endpoint_ip of this UpdateVtapDetails.
        :rtype: str
        """
        return self._source_private_endpoint_ip

    @source_private_endpoint_ip.setter
    def source_private_endpoint_ip(self, source_private_endpoint_ip):
        """
        Sets the source_private_endpoint_ip of this UpdateVtapDetails.
        The IP Address of the source private endpoint.


        :param source_private_endpoint_ip: The source_private_endpoint_ip of this UpdateVtapDetails.
        :type: str
        """
        self._source_private_endpoint_ip = source_private_endpoint_ip

    @property
    def source_private_endpoint_subnet_id(self):
        """
        Gets the source_private_endpoint_subnet_id of this UpdateVtapDetails.
        The `OCID`__ of the subnet that source private endpoint belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_private_endpoint_subnet_id of this UpdateVtapDetails.
        :rtype: str
        """
        return self._source_private_endpoint_subnet_id

    @source_private_endpoint_subnet_id.setter
    def source_private_endpoint_subnet_id(self, source_private_endpoint_subnet_id):
        """
        Sets the source_private_endpoint_subnet_id of this UpdateVtapDetails.
        The `OCID`__ of the subnet that source private endpoint belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_private_endpoint_subnet_id: The source_private_endpoint_subnet_id of this UpdateVtapDetails.
        :type: str
        """
        self._source_private_endpoint_subnet_id = source_private_endpoint_subnet_id

    @property
    def target_type(self):
        """
        Gets the target_type of this UpdateVtapDetails.
        The target type for the VTAP.

        Allowed values for this property are: "VNIC", "NETWORK_LOAD_BALANCER", "IP_ADDRESS"


        :return: The target_type of this UpdateVtapDetails.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this UpdateVtapDetails.
        The target type for the VTAP.


        :param target_type: The target_type of this UpdateVtapDetails.
        :type: str
        """
        allowed_values = ["VNIC", "NETWORK_LOAD_BALANCER", "IP_ADDRESS"]
        if not value_allowed_none_or_none_sentinel(target_type, allowed_values):
            raise ValueError(
                "Invalid value for `target_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._target_type = target_type

    @property
    def source_type(self):
        """
        Gets the source_type of this UpdateVtapDetails.
        The source type for the VTAP.

        Allowed values for this property are: "VNIC", "SUBNET", "LOAD_BALANCER", "DB_SYSTEM", "EXADATA_VM_CLUSTER", "AUTONOMOUS_DATA_WAREHOUSE"


        :return: The source_type of this UpdateVtapDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this UpdateVtapDetails.
        The source type for the VTAP.


        :param source_type: The source_type of this UpdateVtapDetails.
        :type: str
        """
        allowed_values = ["VNIC", "SUBNET", "LOAD_BALANCER", "DB_SYSTEM", "EXADATA_VM_CLUSTER", "AUTONOMOUS_DATA_WAREHOUSE"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            raise ValueError(
                "Invalid value for `source_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source_type = source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
