# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531

from .trace import Trace
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecutionTrace(Trace):
    """
    Contains trace information related to execution of tool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExecutionTrace object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_agent_runtime.models.ExecutionTrace.trace_type` attribute
        of this class is ``EXECUTION_TRACE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ExecutionTrace.
        :type key: str

        :param parent_key:
            The value to assign to the parent_key property of this ExecutionTrace.
        :type parent_key: str

        :param source:
            The value to assign to the source property of this ExecutionTrace.
        :type source: oci.generative_ai_agent_runtime.models.SourceDetails

        :param time_created:
            The value to assign to the time_created property of this ExecutionTrace.
        :type time_created: datetime

        :param time_finished:
            The value to assign to the time_finished property of this ExecutionTrace.
        :type time_finished: datetime

        :param trace_type:
            The value to assign to the trace_type property of this ExecutionTrace.
            Allowed values for this property are: "ERROR_TRACE", "RETRIEVAL_TRACE", "GENERATION_TRACE", "TOOL_INVOCATION_TRACE", "PLANNING_TRACE", "EXECUTION_TRACE"
        :type trace_type: str

        :param input:
            The value to assign to the input property of this ExecutionTrace.
        :type input: str

        :param output:
            The value to assign to the output property of this ExecutionTrace.
        :type output: str

        """
        self.swagger_types = {
            'key': 'str',
            'parent_key': 'str',
            'source': 'SourceDetails',
            'time_created': 'datetime',
            'time_finished': 'datetime',
            'trace_type': 'str',
            'input': 'str',
            'output': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'parent_key': 'parentKey',
            'source': 'source',
            'time_created': 'timeCreated',
            'time_finished': 'timeFinished',
            'trace_type': 'traceType',
            'input': 'input',
            'output': 'output'
        }
        self._key = None
        self._parent_key = None
        self._source = None
        self._time_created = None
        self._time_finished = None
        self._trace_type = None
        self._input = None
        self._output = None
        self._trace_type = 'EXECUTION_TRACE'

    @property
    def input(self):
        """
        Gets the input of this ExecutionTrace.
        Input data.


        :return: The input of this ExecutionTrace.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this ExecutionTrace.
        Input data.


        :param input: The input of this ExecutionTrace.
        :type: str
        """
        self._input = input

    @property
    def output(self):
        """
        Gets the output of this ExecutionTrace.
        Output data.


        :return: The output of this ExecutionTrace.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this ExecutionTrace.
        Output data.


        :param output: The output of this ExecutionTrace.
        :type: str
        """
        self._output = output

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
