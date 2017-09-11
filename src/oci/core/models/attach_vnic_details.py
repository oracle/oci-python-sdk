# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class AttachVnicDetails(object):

    def __init__(self):

        self.swagger_types = {
            'create_vnic_details': 'CreateVnicDetails',
            'display_name': 'str',
            'instance_id': 'str'
        }

        self.attribute_map = {
            'create_vnic_details': 'createVnicDetails',
            'display_name': 'displayName',
            'instance_id': 'instanceId'
        }

        self._create_vnic_details = None
        self._display_name = None
        self._instance_id = None

    @property
    def create_vnic_details(self):
        """
        Gets the create_vnic_details of this AttachVnicDetails.
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
        Gets the instance_id of this AttachVnicDetails.
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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
