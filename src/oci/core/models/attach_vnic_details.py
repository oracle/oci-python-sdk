# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachVnicDetails(object):
    """
    AttachVnicDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachVnicDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param create_vnic_details:
            The value to assign to the create_vnic_details property of this AttachVnicDetails.
        :type create_vnic_details: CreateVnicDetails

        :param display_name:
            The value to assign to the display_name property of this AttachVnicDetails.
        :type display_name: str

        :param instance_id:
            The value to assign to the instance_id property of this AttachVnicDetails.
        :type instance_id: str

        :param nic_index:
            The value to assign to the nic_index property of this AttachVnicDetails.
        :type nic_index: int

        """
        self.swagger_types = {
            'create_vnic_details': 'CreateVnicDetails',
            'display_name': 'str',
            'instance_id': 'str',
            'nic_index': 'int'
        }

        self.attribute_map = {
            'create_vnic_details': 'createVnicDetails',
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'nic_index': 'nicIndex'
        }

        self._create_vnic_details = None
        self._display_name = None
        self._instance_id = None
        self._nic_index = None

    @property
    def create_vnic_details(self):
        """
        **[Required]** Gets the create_vnic_details of this AttachVnicDetails.
        Details for creating a new VNIC.


        :return: The create_vnic_details of this AttachVnicDetails.
        :rtype: CreateVnicDetails
        """
        return self._create_vnic_details

    @create_vnic_details.setter
    def create_vnic_details(self, create_vnic_details):
        """
        Sets the create_vnic_details of this AttachVnicDetails.
        Details for creating a new VNIC.


        :param create_vnic_details: The create_vnic_details of this AttachVnicDetails.
        :type: CreateVnicDetails
        """
        self._create_vnic_details = create_vnic_details

    @property
    def display_name(self):
        """
        Gets the display_name of this AttachVnicDetails.
        A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.


        :return: The display_name of this AttachVnicDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AttachVnicDetails.
        A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.


        :param display_name: The display_name of this AttachVnicDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this AttachVnicDetails.
        The OCID of the instance.


        :return: The instance_id of this AttachVnicDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this AttachVnicDetails.
        The OCID of the instance.


        :param instance_id: The instance_id of this AttachVnicDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def nic_index(self):
        """
        Gets the nic_index of this AttachVnicDetails.
        Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
        Certain bare metal instance shapes have two active physical NICs (0 and 1). If
        you add a secondary VNIC to one of these instances, you can specify which NIC
        the VNIC will use. For more information, see
        `Virtual Network Interface Cards (VNICs)`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVNICs.htm


        :return: The nic_index of this AttachVnicDetails.
        :rtype: int
        """
        return self._nic_index

    @nic_index.setter
    def nic_index(self, nic_index):
        """
        Sets the nic_index of this AttachVnicDetails.
        Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
        Certain bare metal instance shapes have two active physical NICs (0 and 1). If
        you add a secondary VNIC to one of these instances, you can specify which NIC
        the VNIC will use. For more information, see
        `Virtual Network Interface Cards (VNICs)`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVNICs.htm


        :param nic_index: The nic_index of this AttachVnicDetails.
        :type: int
        """
        self._nic_index = nic_index

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
