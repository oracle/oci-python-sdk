# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkEditTagsDetails(object):
    """
    BulkEditTagsDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkEditTagsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this BulkEditTagsDetails.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this BulkEditTagsDetails.
        :type resources: list[oci.identity.models.BulkEditResource]

        :param bulk_edit_operations:
            The value to assign to the bulk_edit_operations property of this BulkEditTagsDetails.
        :type bulk_edit_operations: list[oci.identity.models.BulkEditOperationDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'resources': 'list[BulkEditResource]',
            'bulk_edit_operations': 'list[BulkEditOperationDetails]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'bulk_edit_operations': 'bulkEditOperations'
        }

        self._compartment_id = None
        self._resources = None
        self._bulk_edit_operations = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BulkEditTagsDetails.
        The OCID of the compartment where the bulk tag edit request is submitted.


        :return: The compartment_id of this BulkEditTagsDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BulkEditTagsDetails.
        The OCID of the compartment where the bulk tag edit request is submitted.


        :param compartment_id: The compartment_id of this BulkEditTagsDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this BulkEditTagsDetails.
        The resources to be updated.


        :return: The resources of this BulkEditTagsDetails.
        :rtype: list[oci.identity.models.BulkEditResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this BulkEditTagsDetails.
        The resources to be updated.


        :param resources: The resources of this BulkEditTagsDetails.
        :type: list[oci.identity.models.BulkEditResource]
        """
        self._resources = resources

    @property
    def bulk_edit_operations(self):
        """
        **[Required]** Gets the bulk_edit_operations of this BulkEditTagsDetails.
        The operations associated with the request to bulk edit tags.


        :return: The bulk_edit_operations of this BulkEditTagsDetails.
        :rtype: list[oci.identity.models.BulkEditOperationDetails]
        """
        return self._bulk_edit_operations

    @bulk_edit_operations.setter
    def bulk_edit_operations(self, bulk_edit_operations):
        """
        Sets the bulk_edit_operations of this BulkEditTagsDetails.
        The operations associated with the request to bulk edit tags.


        :param bulk_edit_operations: The bulk_edit_operations of this BulkEditTagsDetails.
        :type: list[oci.identity.models.BulkEditOperationDetails]
        """
        self._bulk_edit_operations = bulk_edit_operations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
