# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateJobOperationDetails(object):
    """
    Job details that are specific to the operation type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateJobOperationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.CreateImportTfStateJobOperationDetails`
        * :class:`~oci.resource_manager.models.CreateApplyJobOperationDetails`
        * :class:`~oci.resource_manager.models.CreatePlanJobOperationDetails`
        * :class:`~oci.resource_manager.models.CreateDestroyJobOperationDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this CreateJobOperationDetails.
        :type operation: str

        """
        self.swagger_types = {
            'operation': 'str'
        }

        self.attribute_map = {
            'operation': 'operation'
        }

        self._operation = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['operation']

        if type == 'IMPORT_TF_STATE':
            return 'CreateImportTfStateJobOperationDetails'

        if type == 'APPLY':
            return 'CreateApplyJobOperationDetails'

        if type == 'PLAN':
            return 'CreatePlanJobOperationDetails'

        if type == 'DESTROY':
            return 'CreateDestroyJobOperationDetails'
        else:
            return 'CreateJobOperationDetails'

    @property
    def operation(self):
        """
        **[Required]** Gets the operation of this CreateJobOperationDetails.
        Terraform-specific operation to execute.


        :return: The operation of this CreateJobOperationDetails.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this CreateJobOperationDetails.
        Terraform-specific operation to execute.


        :param operation: The operation of this CreateJobOperationDetails.
        :type: str
        """
        self._operation = operation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
