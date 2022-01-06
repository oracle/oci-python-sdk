# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .task_details import TaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionTaskDetails(TaskDetails):
    """
    The Functions task.
    Batch input for a function can be limited by either size or time. The first limit reached determines the boundary of the batch.
    For configuration instructions, see
    `To create a service connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionTaskDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.FunctionTaskDetails.kind` attribute
        of this class is ``function`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this FunctionTaskDetails.
            Allowed values for this property are: "function", "logRule"
        :type kind: str

        :param function_id:
            The value to assign to the function_id property of this FunctionTaskDetails.
        :type function_id: str

        :param batch_size_in_kbs:
            The value to assign to the batch_size_in_kbs property of this FunctionTaskDetails.
        :type batch_size_in_kbs: int

        :param batch_time_in_sec:
            The value to assign to the batch_time_in_sec property of this FunctionTaskDetails.
        :type batch_time_in_sec: int

        """
        self.swagger_types = {
            'kind': 'str',
            'function_id': 'str',
            'batch_size_in_kbs': 'int',
            'batch_time_in_sec': 'int'
        }

        self.attribute_map = {
            'kind': 'kind',
            'function_id': 'functionId',
            'batch_size_in_kbs': 'batchSizeInKbs',
            'batch_time_in_sec': 'batchTimeInSec'
        }

        self._kind = None
        self._function_id = None
        self._batch_size_in_kbs = None
        self._batch_time_in_sec = None
        self._kind = 'function'

    @property
    def function_id(self):
        """
        **[Required]** Gets the function_id of this FunctionTaskDetails.
        The `OCID`__ of the function to be used as a task.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The function_id of this FunctionTaskDetails.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this FunctionTaskDetails.
        The `OCID`__ of the function to be used as a task.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param function_id: The function_id of this FunctionTaskDetails.
        :type: str
        """
        self._function_id = function_id

    @property
    def batch_size_in_kbs(self):
        """
        Gets the batch_size_in_kbs of this FunctionTaskDetails.
        Size limit (kilobytes) for batch sent to invoke the function.


        :return: The batch_size_in_kbs of this FunctionTaskDetails.
        :rtype: int
        """
        return self._batch_size_in_kbs

    @batch_size_in_kbs.setter
    def batch_size_in_kbs(self, batch_size_in_kbs):
        """
        Sets the batch_size_in_kbs of this FunctionTaskDetails.
        Size limit (kilobytes) for batch sent to invoke the function.


        :param batch_size_in_kbs: The batch_size_in_kbs of this FunctionTaskDetails.
        :type: int
        """
        self._batch_size_in_kbs = batch_size_in_kbs

    @property
    def batch_time_in_sec(self):
        """
        Gets the batch_time_in_sec of this FunctionTaskDetails.
        Time limit (seconds) for batch sent to invoke the function.


        :return: The batch_time_in_sec of this FunctionTaskDetails.
        :rtype: int
        """
        return self._batch_time_in_sec

    @batch_time_in_sec.setter
    def batch_time_in_sec(self, batch_time_in_sec):
        """
        Sets the batch_time_in_sec of this FunctionTaskDetails.
        Time limit (seconds) for batch sent to invoke the function.


        :param batch_time_in_sec: The batch_time_in_sec of this FunctionTaskDetails.
        :type: int
        """
        self._batch_time_in_sec = batch_time_in_sec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
