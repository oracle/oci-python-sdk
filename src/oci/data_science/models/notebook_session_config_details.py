# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotebookSessionConfigDetails(object):
    """
    Details for the notebook session configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NotebookSessionConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape:
            The value to assign to the shape property of this NotebookSessionConfigDetails.
        :type shape: str

        :param block_storage_size_in_gbs:
            The value to assign to the block_storage_size_in_gbs property of this NotebookSessionConfigDetails.
        :type block_storage_size_in_gbs: int

        :param subnet_id:
            The value to assign to the subnet_id property of this NotebookSessionConfigDetails.
        :type subnet_id: str

        :param notebook_session_shape_config_details:
            The value to assign to the notebook_session_shape_config_details property of this NotebookSessionConfigDetails.
        :type notebook_session_shape_config_details: oci.data_science.models.NotebookSessionShapeConfigDetails

        """
        self.swagger_types = {
            'shape': 'str',
            'block_storage_size_in_gbs': 'int',
            'subnet_id': 'str',
            'notebook_session_shape_config_details': 'NotebookSessionShapeConfigDetails'
        }

        self.attribute_map = {
            'shape': 'shape',
            'block_storage_size_in_gbs': 'blockStorageSizeInGBs',
            'subnet_id': 'subnetId',
            'notebook_session_shape_config_details': 'notebookSessionShapeConfigDetails'
        }

        self._shape = None
        self._block_storage_size_in_gbs = None
        self._subnet_id = None
        self._notebook_session_shape_config_details = None

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this NotebookSessionConfigDetails.
        The shape used to launch the notebook session compute instance.  The list of available shapes in a given compartment can be retrieved using the `ListNotebookSessionShapes` endpoint.


        :return: The shape of this NotebookSessionConfigDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this NotebookSessionConfigDetails.
        The shape used to launch the notebook session compute instance.  The list of available shapes in a given compartment can be retrieved using the `ListNotebookSessionShapes` endpoint.


        :param shape: The shape of this NotebookSessionConfigDetails.
        :type: str
        """
        self._shape = shape

    @property
    def block_storage_size_in_gbs(self):
        """
        Gets the block_storage_size_in_gbs of this NotebookSessionConfigDetails.
        A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.


        :return: The block_storage_size_in_gbs of this NotebookSessionConfigDetails.
        :rtype: int
        """
        return self._block_storage_size_in_gbs

    @block_storage_size_in_gbs.setter
    def block_storage_size_in_gbs(self, block_storage_size_in_gbs):
        """
        Sets the block_storage_size_in_gbs of this NotebookSessionConfigDetails.
        A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.


        :param block_storage_size_in_gbs: The block_storage_size_in_gbs of this NotebookSessionConfigDetails.
        :type: int
        """
        self._block_storage_size_in_gbs = block_storage_size_in_gbs

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this NotebookSessionConfigDetails.
        A notebook session instance is provided with a VNIC for network access.  This specifies the `OCID`__ of the subnet to create a VNIC in.  The subnet should be in a VCN with a NAT gateway for egress to the internet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this NotebookSessionConfigDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this NotebookSessionConfigDetails.
        A notebook session instance is provided with a VNIC for network access.  This specifies the `OCID`__ of the subnet to create a VNIC in.  The subnet should be in a VCN with a NAT gateway for egress to the internet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this NotebookSessionConfigDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def notebook_session_shape_config_details(self):
        """
        Gets the notebook_session_shape_config_details of this NotebookSessionConfigDetails.

        :return: The notebook_session_shape_config_details of this NotebookSessionConfigDetails.
        :rtype: oci.data_science.models.NotebookSessionShapeConfigDetails
        """
        return self._notebook_session_shape_config_details

    @notebook_session_shape_config_details.setter
    def notebook_session_shape_config_details(self, notebook_session_shape_config_details):
        """
        Sets the notebook_session_shape_config_details of this NotebookSessionConfigDetails.

        :param notebook_session_shape_config_details: The notebook_session_shape_config_details of this NotebookSessionConfigDetails.
        :type: oci.data_science.models.NotebookSessionShapeConfigDetails
        """
        self._notebook_session_shape_config_details = notebook_session_shape_config_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
