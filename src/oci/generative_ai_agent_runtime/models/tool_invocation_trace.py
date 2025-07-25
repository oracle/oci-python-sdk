# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531

from .trace import Trace
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ToolInvocationTrace(Trace):
    """
    The trace information about the tool selection from multiple tools.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ToolInvocationTrace object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_agent_runtime.models.ToolInvocationTrace.trace_type` attribute
        of this class is ``TOOL_INVOCATION_TRACE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ToolInvocationTrace.
        :type key: str

        :param parent_key:
            The value to assign to the parent_key property of this ToolInvocationTrace.
        :type parent_key: str

        :param source:
            The value to assign to the source property of this ToolInvocationTrace.
        :type source: oci.generative_ai_agent_runtime.models.SourceDetails

        :param time_created:
            The value to assign to the time_created property of this ToolInvocationTrace.
        :type time_created: datetime

        :param time_finished:
            The value to assign to the time_finished property of this ToolInvocationTrace.
        :type time_finished: datetime

        :param trace_type:
            The value to assign to the trace_type property of this ToolInvocationTrace.
            Allowed values for this property are: "ERROR_TRACE", "RETRIEVAL_TRACE", "GENERATION_TRACE", "TOOL_INVOCATION_TRACE", "PLANNING_TRACE", "EXECUTION_TRACE"
        :type trace_type: str

        :param tool_id:
            The value to assign to the tool_id property of this ToolInvocationTrace.
        :type tool_id: str

        :param tool_name:
            The value to assign to the tool_name property of this ToolInvocationTrace.
        :type tool_name: str

        :param invocation_details:
            The value to assign to the invocation_details property of this ToolInvocationTrace.
        :type invocation_details: str

        """
        self.swagger_types = {
            'key': 'str',
            'parent_key': 'str',
            'source': 'SourceDetails',
            'time_created': 'datetime',
            'time_finished': 'datetime',
            'trace_type': 'str',
            'tool_id': 'str',
            'tool_name': 'str',
            'invocation_details': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'parent_key': 'parentKey',
            'source': 'source',
            'time_created': 'timeCreated',
            'time_finished': 'timeFinished',
            'trace_type': 'traceType',
            'tool_id': 'toolId',
            'tool_name': 'toolName',
            'invocation_details': 'invocationDetails'
        }
        self._key = None
        self._parent_key = None
        self._source = None
        self._time_created = None
        self._time_finished = None
        self._trace_type = None
        self._tool_id = None
        self._tool_name = None
        self._invocation_details = None
        self._trace_type = 'TOOL_INVOCATION_TRACE'

    @property
    def tool_id(self):
        """
        Gets the tool_id of this ToolInvocationTrace.
        The ID of the selected tool based on the user query.


        :return: The tool_id of this ToolInvocationTrace.
        :rtype: str
        """
        return self._tool_id

    @tool_id.setter
    def tool_id(self, tool_id):
        """
        Sets the tool_id of this ToolInvocationTrace.
        The ID of the selected tool based on the user query.


        :param tool_id: The tool_id of this ToolInvocationTrace.
        :type: str
        """
        self._tool_id = tool_id

    @property
    def tool_name(self):
        """
        Gets the tool_name of this ToolInvocationTrace.
        The display name of the selected tool.


        :return: The tool_name of this ToolInvocationTrace.
        :rtype: str
        """
        return self._tool_name

    @tool_name.setter
    def tool_name(self, tool_name):
        """
        Sets the tool_name of this ToolInvocationTrace.
        The display name of the selected tool.


        :param tool_name: The tool_name of this ToolInvocationTrace.
        :type: str
        """
        self._tool_name = tool_name

    @property
    def invocation_details(self):
        """
        Gets the invocation_details of this ToolInvocationTrace.
        The invocation details related to the selected tool.


        :return: The invocation_details of this ToolInvocationTrace.
        :rtype: str
        """
        return self._invocation_details

    @invocation_details.setter
    def invocation_details(self, invocation_details):
        """
        Sets the invocation_details of this ToolInvocationTrace.
        The invocation details related to the selected tool.


        :param invocation_details: The invocation_details of this ToolInvocationTrace.
        :type: str
        """
        self._invocation_details = invocation_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
