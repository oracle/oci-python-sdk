# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceVnicMappingDetails(object):
    """
    A compute instance's source and destination VNIC mapping.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceVnicMappingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_vnic_id:
            The value to assign to the source_vnic_id property of this ComputeInstanceVnicMappingDetails.
        :type source_vnic_id: str

        :param destination_subnet_id:
            The value to assign to the destination_subnet_id property of this ComputeInstanceVnicMappingDetails.
        :type destination_subnet_id: str

        :param destination_nsg_id_list:
            The value to assign to the destination_nsg_id_list property of this ComputeInstanceVnicMappingDetails.
        :type destination_nsg_id_list: list[str]

        """
        self.swagger_types = {
            'source_vnic_id': 'str',
            'destination_subnet_id': 'str',
            'destination_nsg_id_list': 'list[str]'
        }

        self.attribute_map = {
            'source_vnic_id': 'sourceVnicId',
            'destination_subnet_id': 'destinationSubnetId',
            'destination_nsg_id_list': 'destinationNsgIdList'
        }

        self._source_vnic_id = None
        self._destination_subnet_id = None
        self._destination_nsg_id_list = None

    @property
    def source_vnic_id(self):
        """
        **[Required]** Gets the source_vnic_id of this ComputeInstanceVnicMappingDetails.
        The OCID of the VNIC.

        Example: `ocid1.vnic.oc1.phx.exampleocid1`


        :return: The source_vnic_id of this ComputeInstanceVnicMappingDetails.
        :rtype: str
        """
        return self._source_vnic_id

    @source_vnic_id.setter
    def source_vnic_id(self, source_vnic_id):
        """
        Sets the source_vnic_id of this ComputeInstanceVnicMappingDetails.
        The OCID of the VNIC.

        Example: `ocid1.vnic.oc1.phx.exampleocid1`


        :param source_vnic_id: The source_vnic_id of this ComputeInstanceVnicMappingDetails.
        :type: str
        """
        self._source_vnic_id = source_vnic_id

    @property
    def destination_subnet_id(self):
        """
        **[Required]** Gets the destination_subnet_id of this ComputeInstanceVnicMappingDetails.
        The OCID of the destination (remote) subnet to which this VNIC should connect.

        Example: `ocid1.subnet.oc1.iad.exampleocid2`


        :return: The destination_subnet_id of this ComputeInstanceVnicMappingDetails.
        :rtype: str
        """
        return self._destination_subnet_id

    @destination_subnet_id.setter
    def destination_subnet_id(self, destination_subnet_id):
        """
        Sets the destination_subnet_id of this ComputeInstanceVnicMappingDetails.
        The OCID of the destination (remote) subnet to which this VNIC should connect.

        Example: `ocid1.subnet.oc1.iad.exampleocid2`


        :param destination_subnet_id: The destination_subnet_id of this ComputeInstanceVnicMappingDetails.
        :type: str
        """
        self._destination_subnet_id = destination_subnet_id

    @property
    def destination_nsg_id_list(self):
        """
        Gets the destination_nsg_id_list of this ComputeInstanceVnicMappingDetails.
        A list of destination region's network security group (NSG) Ids which this VNIC should use.

        Example: `[ ocid1.networksecuritygroup.oc1.iad.abcd1, ocid1.networksecuritygroup.oc1.iad.wxyz2 ]`


        :return: The destination_nsg_id_list of this ComputeInstanceVnicMappingDetails.
        :rtype: list[str]
        """
        return self._destination_nsg_id_list

    @destination_nsg_id_list.setter
    def destination_nsg_id_list(self, destination_nsg_id_list):
        """
        Sets the destination_nsg_id_list of this ComputeInstanceVnicMappingDetails.
        A list of destination region's network security group (NSG) Ids which this VNIC should use.

        Example: `[ ocid1.networksecuritygroup.oc1.iad.abcd1, ocid1.networksecuritygroup.oc1.iad.wxyz2 ]`


        :param destination_nsg_id_list: The destination_nsg_id_list of this ComputeInstanceVnicMappingDetails.
        :type: list[str]
        """
        self._destination_nsg_id_list = destination_nsg_id_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
