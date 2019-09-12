# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .job_operation_details_summary import JobOperationDetailsSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportTfStateJobOperationDetailsSummary(JobOperationDetailsSummary):
    """
    Job details that are specific to import Terraform state operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportTfStateJobOperationDetailsSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.ImportTfStateJobOperationDetailsSummary.operation` attribute
        of this class is ``IMPORT_TF_STATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this ImportTfStateJobOperationDetailsSummary.
        :type operation: str

        """
        self.swagger_types = {
            'operation': 'str'
        }

        self.attribute_map = {
            'operation': 'operation'
        }

        self._operation = None
        self._operation = 'IMPORT_TF_STATE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
