# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_job_operation_details import CreateJobOperationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateImportTfStateJobOperationDetails(CreateJobOperationDetails):
    """
    Job details that are specific to import Terraform state operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateImportTfStateJobOperationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateImportTfStateJobOperationDetails.operation` attribute
        of this class is ``IMPORT_TF_STATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this CreateImportTfStateJobOperationDetails.
        :type operation: str

        :param tf_state_base64_encoded:
            The value to assign to the tf_state_base64_encoded property of this CreateImportTfStateJobOperationDetails.
        :type tf_state_base64_encoded: str

        """
        self.swagger_types = {
            'operation': 'str',
            'tf_state_base64_encoded': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'tf_state_base64_encoded': 'tfStateBase64Encoded'
        }

        self._operation = None
        self._tf_state_base64_encoded = None
        self._operation = 'IMPORT_TF_STATE'

    @property
    def tf_state_base64_encoded(self):
        """
        **[Required]** Gets the tf_state_base64_encoded of this CreateImportTfStateJobOperationDetails.
        Base64-encoded state file


        :return: The tf_state_base64_encoded of this CreateImportTfStateJobOperationDetails.
        :rtype: str
        """
        return self._tf_state_base64_encoded

    @tf_state_base64_encoded.setter
    def tf_state_base64_encoded(self, tf_state_base64_encoded):
        """
        Sets the tf_state_base64_encoded of this CreateImportTfStateJobOperationDetails.
        Base64-encoded state file


        :param tf_state_base64_encoded: The tf_state_base64_encoded of this CreateImportTfStateJobOperationDetails.
        :type: str
        """
        self._tf_state_base64_encoded = tf_state_base64_encoded

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
