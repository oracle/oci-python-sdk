# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationAttachVnicDetails(object):
    """
    InstanceConfigurationAttachVnicDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationAttachVnicDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param create_vnic_details:
            The value to assign to the create_vnic_details property of this InstanceConfigurationAttachVnicDetails.
        :type create_vnic_details: InstanceConfigurationCreateVnicDetails

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationAttachVnicDetails.
        :type display_name: str

        :param nic_index:
            The value to assign to the nic_index property of this InstanceConfigurationAttachVnicDetails.
        :type nic_index: int

        """
        self.swagger_types = {
            'create_vnic_details': 'InstanceConfigurationCreateVnicDetails',
            'display_name': 'str',
            'nic_index': 'int'
        }

        self.attribute_map = {
            'create_vnic_details': 'createVnicDetails',
            'display_name': 'displayName',
            'nic_index': 'nicIndex'
        }

        self._create_vnic_details = None
        self._display_name = None
        self._nic_index = None

    @property
    def create_vnic_details(self):
        """
        Gets the create_vnic_details of this InstanceConfigurationAttachVnicDetails.
        Details for creating a new VNIC.


        :return: The create_vnic_details of this InstanceConfigurationAttachVnicDetails.
        :rtype: InstanceConfigurationCreateVnicDetails
        """
        return self._create_vnic_details

    @create_vnic_details.setter
    def create_vnic_details(self, create_vnic_details):
        """
        Sets the create_vnic_details of this InstanceConfigurationAttachVnicDetails.
        Details for creating a new VNIC.


        :param create_vnic_details: The create_vnic_details of this InstanceConfigurationAttachVnicDetails.
        :type: InstanceConfigurationCreateVnicDetails
        """
        self._create_vnic_details = create_vnic_details

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfigurationAttachVnicDetails.
        A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.


        :return: The display_name of this InstanceConfigurationAttachVnicDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfigurationAttachVnicDetails.
        A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.


        :param display_name: The display_name of this InstanceConfigurationAttachVnicDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def nic_index(self):
        """
        Gets the nic_index of this InstanceConfigurationAttachVnicDetails.
        Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
        Certain bare metal instance shapes have two active physical NICs (0 and 1). If
        you add a secondary VNIC to one of these instances, you can specify which NIC
        the VNIC will use. For more information, see
        `Virtual Network Interface Cards (VNICs)`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVNICs.htm


        :return: The nic_index of this InstanceConfigurationAttachVnicDetails.
        :rtype: int
        """
        return self._nic_index

    @nic_index.setter
    def nic_index(self, nic_index):
        """
        Sets the nic_index of this InstanceConfigurationAttachVnicDetails.
        Which physical network interface card (NIC) the VNIC will use. Defaults to 0.
        Certain bare metal instance shapes have two active physical NICs (0 and 1). If
        you add a secondary VNIC to one of these instances, you can specify which NIC
        the VNIC will use. For more information, see
        `Virtual Network Interface Cards (VNICs)`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVNICs.htm


        :param nic_index: The nic_index of this InstanceConfigurationAttachVnicDetails.
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
