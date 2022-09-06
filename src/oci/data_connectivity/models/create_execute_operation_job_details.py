# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExecuteOperationJobDetails(object):
    """
    Input details to execute an operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExecuteOperationJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this CreateExecuteOperationJobDetails.
        :type operation: oci.data_connectivity.models.Operation

        :param call_operation_config:
            The value to assign to the call_operation_config property of this CreateExecuteOperationJobDetails.
        :type call_operation_config: oci.data_connectivity.models.CallOperationConfig

        :param input_records:
            The value to assign to the input_records property of this CreateExecuteOperationJobDetails.
        :type input_records: list[oci.data_connectivity.models.OperationInputRecord]

        """
        self.swagger_types = {
            'operation': 'Operation',
            'call_operation_config': 'CallOperationConfig',
            'input_records': 'list[OperationInputRecord]'
        }

        self.attribute_map = {
            'operation': 'operation',
            'call_operation_config': 'callOperationConfig',
            'input_records': 'inputRecords'
        }

        self._operation = None
        self._call_operation_config = None
        self._input_records = None

    @property
    def operation(self):
        """
        Gets the operation of this CreateExecuteOperationJobDetails.

        :return: The operation of this CreateExecuteOperationJobDetails.
        :rtype: oci.data_connectivity.models.Operation
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this CreateExecuteOperationJobDetails.

        :param operation: The operation of this CreateExecuteOperationJobDetails.
        :type: oci.data_connectivity.models.Operation
        """
        self._operation = operation

    @property
    def call_operation_config(self):
        """
        Gets the call_operation_config of this CreateExecuteOperationJobDetails.

        :return: The call_operation_config of this CreateExecuteOperationJobDetails.
        :rtype: oci.data_connectivity.models.CallOperationConfig
        """
        return self._call_operation_config

    @call_operation_config.setter
    def call_operation_config(self, call_operation_config):
        """
        Sets the call_operation_config of this CreateExecuteOperationJobDetails.

        :param call_operation_config: The call_operation_config of this CreateExecuteOperationJobDetails.
        :type: oci.data_connectivity.models.CallOperationConfig
        """
        self._call_operation_config = call_operation_config

    @property
    def input_records(self):
        """
        Gets the input_records of this CreateExecuteOperationJobDetails.
        Collection of the input parameters supplied.


        :return: The input_records of this CreateExecuteOperationJobDetails.
        :rtype: list[oci.data_connectivity.models.OperationInputRecord]
        """
        return self._input_records

    @input_records.setter
    def input_records(self, input_records):
        """
        Sets the input_records of this CreateExecuteOperationJobDetails.
        Collection of the input parameters supplied.


        :param input_records: The input_records of this CreateExecuteOperationJobDetails.
        :type: list[oci.data_connectivity.models.OperationInputRecord]
        """
        self._input_records = input_records

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
