# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VnicAttachment(object):

    def __init__(self, **kwargs):
        """
        Initializes a new VnicAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this VnicAttachment.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VnicAttachment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this VnicAttachment.
        :type display_name: str

        :param id:
            The value to assign to the id property of this VnicAttachment.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this VnicAttachment.
        :type instance_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VnicAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param nic_index:
            The value to assign to the nic_index property of this VnicAttachment.
        :type nic_index: int

        :param subnet_id:
            The value to assign to the subnet_id property of this VnicAttachment.
        :type subnet_id: str

        :param time_created:
            The value to assign to the time_created property of this VnicAttachment.
        :type time_created: datetime

        :param vlan_tag:
            The value to assign to the vlan_tag property of this VnicAttachment.
        :type vlan_tag: int

        :param vnic_id:
            The value to assign to the vnic_id property of this VnicAttachment.
        :type vnic_id: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str',
            'nic_index': 'int',
            'subnet_id': 'str',
            'time_created': 'datetime',
            'vlan_tag': 'int',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState',
            'nic_index': 'nicIndex',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated',
            'vlan_tag': 'vlanTag',
            'vnic_id': 'vnicId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None
        self._nic_index = None
        self._subnet_id = None
        self._time_created = None
        self._vlan_tag = None
        self._vnic_id = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this VnicAttachment.
        The Availability Domain of the instance.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this VnicAttachment.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VnicAttachment.
        The Availability Domain of the instance.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this VnicAttachment.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VnicAttachment.
        The OCID of the compartment the VNIC attachment is in, which is the same
        compartment the instance is in.


        :return: The compartment_id of this VnicAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VnicAttachment.
        The OCID of the compartment the VNIC attachment is in, which is the same
        compartment the instance is in.


        :param compartment_id: The compartment_id of this VnicAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VnicAttachment.
        A user-friendly name. Does not have to be unique.
        Avoid entering confidential information.


        :return: The display_name of this VnicAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VnicAttachment.
        A user-friendly name. Does not have to be unique.
        Avoid entering confidential information.


        :param display_name: The display_name of this VnicAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VnicAttachment.
        The OCID of the VNIC attachment.


        :return: The id of this VnicAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VnicAttachment.
        The OCID of the VNIC attachment.


        :param id: The id of this VnicAttachment.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this VnicAttachment.
        The OCID of the instance.


        :return: The instance_id of this VnicAttachment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this VnicAttachment.
        The OCID of the instance.


        :param instance_id: The instance_id of this VnicAttachment.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VnicAttachment.
        The current state of the VNIC attachment.

        Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VnicAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VnicAttachment.
        The current state of the VNIC attachment.


        :param lifecycle_state: The lifecycle_state of this VnicAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def nic_index(self):
        """
        Gets the nic_index of this VnicAttachment.
        Which physical network interface card (NIC) the VNIC uses.
        Certain bare metal instance shapes have two active physical NICs (0 and 1). If
        you add a secondary VNIC to one of these instances, you can specify which NIC
        the VNIC will use. For more information, see
        `Virtual Network Interface Cards (VNICs)`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVNICs.htm


        :return: The nic_index of this VnicAttachment.
        :rtype: int
        """
        return self._nic_index

    @nic_index.setter
    def nic_index(self, nic_index):
        """
        Sets the nic_index of this VnicAttachment.
        Which physical network interface card (NIC) the VNIC uses.
        Certain bare metal instance shapes have two active physical NICs (0 and 1). If
        you add a secondary VNIC to one of these instances, you can specify which NIC
        the VNIC will use. For more information, see
        `Virtual Network Interface Cards (VNICs)`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVNICs.htm


        :param nic_index: The nic_index of this VnicAttachment.
        :type: int
        """
        self._nic_index = nic_index

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this VnicAttachment.
        The OCID of the VNIC's subnet.


        :return: The subnet_id of this VnicAttachment.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this VnicAttachment.
        The OCID of the VNIC's subnet.


        :param subnet_id: The subnet_id of this VnicAttachment.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VnicAttachment.
        The date and time the VNIC attachment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this VnicAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VnicAttachment.
        The date and time the VNIC attachment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this VnicAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vlan_tag(self):
        """
        Gets the vlan_tag of this VnicAttachment.
        The Oracle-assigned VLAN tag of the attached VNIC. Available after the
        attachment process is complete.

        Example: `0`


        :return: The vlan_tag of this VnicAttachment.
        :rtype: int
        """
        return self._vlan_tag

    @vlan_tag.setter
    def vlan_tag(self, vlan_tag):
        """
        Sets the vlan_tag of this VnicAttachment.
        The Oracle-assigned VLAN tag of the attached VNIC. Available after the
        attachment process is complete.

        Example: `0`


        :param vlan_tag: The vlan_tag of this VnicAttachment.
        :type: int
        """
        self._vlan_tag = vlan_tag

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this VnicAttachment.
        The OCID of the VNIC. Available after the attachment process is complete.


        :return: The vnic_id of this VnicAttachment.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this VnicAttachment.
        The OCID of the VNIC. Available after the attachment process is complete.


        :param vnic_id: The vnic_id of this VnicAttachment.
        :type: str
        """
        self._vnic_id = vnic_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
