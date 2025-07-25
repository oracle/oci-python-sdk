# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531

from .tool_config import ToolConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AgentToolConfig(ToolConfig):
    """
    The configuration for Agent as a Tool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AgentToolConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_agent.models.AgentToolConfig.tool_config_type` attribute
        of this class is ``AGENT_TOOL_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tool_config_type:
            The value to assign to the tool_config_type property of this AgentToolConfig.
            Allowed values for this property are: "SQL_TOOL_CONFIG", "RAG_TOOL_CONFIG", "FUNCTION_CALLING_TOOL_CONFIG", "HTTP_ENDPOINT_TOOL_CONFIG", "AGENT_TOOL_CONFIG"
        :type tool_config_type: str

        :param agent_endpoint_id:
            The value to assign to the agent_endpoint_id property of this AgentToolConfig.
        :type agent_endpoint_id: str

        """
        self.swagger_types = {
            'tool_config_type': 'str',
            'agent_endpoint_id': 'str'
        }
        self.attribute_map = {
            'tool_config_type': 'toolConfigType',
            'agent_endpoint_id': 'agentEndpointId'
        }
        self._tool_config_type = None
        self._agent_endpoint_id = None
        self._tool_config_type = 'AGENT_TOOL_CONFIG'

    @property
    def agent_endpoint_id(self):
        """
        **[Required]** Gets the agent_endpoint_id of this AgentToolConfig.
        The AgentEndpoint OCID to be used as a tool in this agent.


        :return: The agent_endpoint_id of this AgentToolConfig.
        :rtype: str
        """
        return self._agent_endpoint_id

    @agent_endpoint_id.setter
    def agent_endpoint_id(self, agent_endpoint_id):
        """
        Sets the agent_endpoint_id of this AgentToolConfig.
        The AgentEndpoint OCID to be used as a tool in this agent.


        :param agent_endpoint_id: The agent_endpoint_id of this AgentToolConfig.
        :type: str
        """
        self._agent_endpoint_id = agent_endpoint_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
