# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Vlan(object):
    """
    A resource to be used only with the Oracle Cloud VMware Solution.

    Conceptually, a virtual LAN (VLAN) is a broadcast domain that is created
    by partitioning and isolating a network at the data link layer (a *layer 2 network*).
    VLANs work by using IEEE 802.1Q VLAN tags. Layer 2 traffic is forwarded within the
    VLAN based on MAC learning.

    In the Networking service, a VLAN is an object within a VCN. You use VLANs to
    partition the VCN at the data link layer (layer 2). A VLAN is analagous to a subnet,
    which is an object for partitioning the VCN at the IP layer (layer 3).
    """

    #: A constant which can be used with the lifecycle_state property of a Vlan.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Vlan.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Vlan.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Vlan.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a Vlan.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new Vlan object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this Vlan.
        :type availability_domain: str

        :param cidr_block:
            The value to assign to the cidr_block property of this Vlan.
        :type cidr_block: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Vlan.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Vlan.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Vlan.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Vlan.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Vlan.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Vlan.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this Vlan.
        :type nsg_ids: list[str]

        :param vlan_tag:
            The value to assign to the vlan_tag property of this Vlan.
        :type vlan_tag: int

        :param route_table_id:
            The value to assign to the route_table_id property of this Vlan.
        :type route_table_id: str

        :param time_created:
            The value to assign to the time_created property of this Vlan.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this Vlan.
        :type vcn_id: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'cidr_block': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'nsg_ids': 'list[str]',
            'vlan_tag': 'int',
            'route_table_id': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'nsg_ids': 'nsgIds',
            'vlan_tag': 'vlanTag',
            'route_table_id': 'routeTableId',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._availability_domain = None
        self._cidr_block = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._nsg_ids = None
        self._vlan_tag = None
        self._route_table_id = None
        self._time_created = None
        self._vcn_id = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Vlan.
        The availability domain of the VLAN.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this Vlan.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Vlan.
        The availability domain of the VLAN.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this Vlan.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this Vlan.
        The range of IPv4 addresses that will be used for layer 3 communication with
        hosts outside the VLAN.

        Example: `192.168.1.0/24`


        :return: The cidr_block of this Vlan.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Vlan.
        The range of IPv4 addresses that will be used for layer 3 communication with
        hosts outside the VLAN.

        Example: `192.168.1.0/24`


        :param cidr_block: The cidr_block of this Vlan.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Vlan.
        The OCID of the compartment containing the VLAN.


        :return: The compartment_id of this Vlan.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vlan.
        The OCID of the compartment containing the VLAN.


        :param compartment_id: The compartment_id of this Vlan.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Vlan.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Vlan.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Vlan.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Vlan.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this Vlan.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Vlan.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vlan.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Vlan.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Vlan.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Vlan.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Vlan.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Vlan.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Vlan.
        The VLAN's Oracle ID (OCID).


        :return: The id of this Vlan.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vlan.
        The VLAN's Oracle ID (OCID).


        :param id: The id of this Vlan.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Vlan.
        The VLAN's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Vlan.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Vlan.
        The VLAN's current state.


        :param lifecycle_state: The lifecycle_state of this Vlan.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this Vlan.
        A list of the OCIDs of the network security groups (NSGs) to use with this VLAN.
        All VNICs in the VLAN belong to these NSGs. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this Vlan.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this Vlan.
        A list of the OCIDs of the network security groups (NSGs) to use with this VLAN.
        All VNICs in the VLAN belong to these NSGs. For more
        information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this Vlan.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def vlan_tag(self):
        """
        Gets the vlan_tag of this Vlan.
        The IEEE 802.1Q VLAN tag of this VLAN.

        Example: `100`


        :return: The vlan_tag of this Vlan.
        :rtype: int
        """
        return self._vlan_tag

    @vlan_tag.setter
    def vlan_tag(self, vlan_tag):
        """
        Sets the vlan_tag of this Vlan.
        The IEEE 802.1Q VLAN tag of this VLAN.

        Example: `100`


        :param vlan_tag: The vlan_tag of this Vlan.
        :type: int
        """
        self._vlan_tag = vlan_tag

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this Vlan.
        The OCID of the route table that the VLAN uses.


        :return: The route_table_id of this Vlan.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this Vlan.
        The OCID of the route table that the VLAN uses.


        :param route_table_id: The route_table_id of this Vlan.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Vlan.
        The date and time the VLAN was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Vlan.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vlan.
        The date and time the VLAN was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Vlan.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this Vlan.
        The OCID of the VCN the VLAN is in.


        :return: The vcn_id of this Vlan.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this Vlan.
        The OCID of the VCN the VLAN is in.


        :param vcn_id: The vcn_id of this Vlan.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
