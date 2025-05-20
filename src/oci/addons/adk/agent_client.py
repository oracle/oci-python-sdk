# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
ADK Agent Client
"""

from typing import Any, Callable, Dict, List, Literal, Optional, Tuple

import oci
from oci.constants import HEADER_REQUEST_ID
from oci.exceptions import ClientError, ServiceError
from oci.generative_ai_agent import GenerativeAiAgentClient
from oci.generative_ai_agent.models import (
    CreateToolDetails,
    Function,
    FunctionCallingToolConfig,
    KnowledgeBaseConfig,
    LlmConfig,
    LlmCustomization,
    RagToolConfig,
    UpdateAgentDetails,
    UpdateToolDetails,
)
from oci.generative_ai_agent_runtime import GenerativeAiAgentRuntimeClient
from oci.generative_ai_agent_runtime.models import (
    ChatDetails,
    ChatResult,
    CreateSessionDetails,
    FunctionCallingPerformedAction,
    Session,
)
from oci.response import Response
from oci.util import formatted_flat_dict, to_dict
from oci.pagination import list_call_get_all_results

from oci.addons.adk.agent_error import AgentError, UserError
from oci.addons.adk.auth.factory import AuthFactory, OCIAuthType
from oci.addons.adk.constants import (
    DEFAULT_SESSION_NAME,
    DEFAULT_TIMEOUT,
    DESC_SUFFIX,
    FREEFORM_TAGS,
)
from oci.addons.adk.logger import default_logger as logger
from oci.addons.adk.run.types import PerformedAction
from oci.addons.adk.tool import FunctionTool
from oci.addons.adk.tool.prebuilt import AgenticRagTool
from oci.addons.adk.util import build_custom_function_params, get_region_endpoint


class AgentClient:
    """Client for interacting with OCI Agent endpoints."""

    def __init__(
        self,
        auth_type: Optional[str] = "api_key",
        config: Optional[str] = oci.config.DEFAULT_LOCATION,
        profile: Optional[str] = oci.config.DEFAULT_PROFILE,
        token: Optional[str] = None,
        region: Optional[str] = None,
        runtime_endpoint: Optional[str] = None,
        management_endpoint: Optional[str] = None,
        timeout: Optional[float | Tuple[float, float]] = DEFAULT_TIMEOUT,
        debug: Optional[bool] = False,
    ) -> None:
        """
        Initialize the agent client.

        Args:
            auth_type: The authentication type, Must be
                one of: 'api_key', 'security_token', 'instance_principal',
                'resource_principal', 'instance_obo_user'
            config: The config file path for the agent client
            profile: The profile to use for authentication
            token: The token to use for authentication
            region: The region to use for authentication
                If provided, runtime_endpoint and management_endpoint will be
                constructed automatically unless explicitly specified
            runtime_endpoint: The runtime endpoint for OCI Generative AI Agent
            management_endpoint: The management endpoint for OCI Generative AI Agent
            timeout: The timeout for the agent client
            debug: Whether to enable debug logging

        Raises:
            AgentError: If the agent endpoint id is unknown
        """
        # use auth module
        self.auth = AuthFactory.create_oci_auth(
            auth_type=OCIAuthType(auth_type),
            config_path=config,
            profile=profile,
            token=token,
            region=region,
        )

        # endpoint
        self.runtime_endpoint = self.get_runtime_endpoint(runtime_endpoint, region)
        self.management_endpoint = self.get_management_endpoint(
            management_endpoint, region
        )

        # init Agent Runtime Client
        self._rt_client = GenerativeAiAgentRuntimeClient(
            config=self.auth.get_config(),
            signer=self.auth.get_auth_credentials(),
            service_endpoint=self.runtime_endpoint,
            timeout=timeout,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY,
        )
        # init Agent client
        self._mgmt_client = GenerativeAiAgentClient(
            config=self.auth.get_config(),
            signer=self.auth.get_auth_credentials(),
            service_endpoint=self.management_endpoint,
            timeout=timeout,
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY,
        )
        self.debug = debug
        self._handlers: Dict[str, Callable] = {}

    def create_session(
        self,
        agent_endpoint_id: str,
        display_name: str | None = None,
        description: str | None = None,
    ) -> str:
        """
        Create a new agent session.

        Args:
            agent_endpoint_id: The agent endpoint id
            display_name: Name for the session
            description: Description for the session

        Returns:
            The session ID

        Raises:
            AgentError: If session creation fails
        """
        create_session_details = CreateSessionDetails()
        create_session_details.display_name = (
            display_name if display_name else DEFAULT_SESSION_NAME
        )
        create_session_details.description = (
            description if description else DEFAULT_SESSION_NAME + DESC_SUFFIX
        )

        logger.debug(f"Creating session with details: {create_session_details}")

        create_session_response: Response = self._invoke(
            method=self._rt_client.create_session,
            success_message="Session creation succeeded",
            error_message="Failed to create session",
            debug=self.debug,
            create_session_details=create_session_details,
            agent_endpoint_id=agent_endpoint_id,
        )
        response_data: Session = create_session_response.data
        return response_data.id

    def delete_session(self, agent_endpoint_id: str, session_id: str) -> None:
        """
        Delete an existing agent session.

        Args:
            agent_endpoint_id: The agent endpoint id
            session_id: The session ID to delete

        Returns:
            None

        Raises:
            AgentError: If session deletion fails
        """
        logger.debug(f"Deleting session: {session_id}")
        self._invoke(
            method=self._rt_client.delete_session,
            success_message="Session deletion succeeded",
            error_message="Failed to delete session",
            debug=self.debug,
            session_id=session_id,
            agent_endpoint_id=agent_endpoint_id,
        )
        return

    def chat(
        self,
        agent_endpoint_id: str,
        session_id: str,
        user_message: Optional[str] = None,
        performed_actions: Optional[List[PerformedAction]] = None,
    ) -> Dict[str, Any]:
        """
        Invoke a chat session with the agent.

        Args:
            agent_endpoint_id: The agent endpoint id
            session_id: The session ID to use for the chat
            user_message: The message from the user
            performed_actions: Actions that have been performed

        Returns:
            The response from the agent

        Raises:
            AgentError: If the invocation fails
        """
        chat_details = ChatDetails()
        fc_performed_actions = []
        if performed_actions:
            fc_performed_actions = [
                FunctionCallingPerformedAction(
                    action_id=action.action_id,
                    performed_action_type=action.performed_action_type,
                    function_call_output=action.function_call_output,
                )
                for action in performed_actions
            ]
        chat_details.performed_actions = fc_performed_actions
        chat_details.user_message = user_message
        chat_details.should_stream = False
        chat_details.session_id = session_id

        logger.debug(f"Invoking chat endpoint with data: {chat_details}")

        chat_response: Response = self._invoke(
            method=self._rt_client.chat,
            success_message="Chat succeeded",
            error_message="Failed to invoke chat endpoint",
            debug=self.debug,
            chat_details=chat_details,
            agent_endpoint_id=agent_endpoint_id,
        )

        response_data: ChatResult = chat_response.data
        return to_dict(response_data)

    def update_agent(
        self,
        agent_id: str,
        name: str | None = None,
        description: str | None = None,
        instructions: str | None = None,
    ) -> None:
        """
        Update the agent.

        Args:
            agent_id: The ID of the agent to update
            name: The new name for the agent
            description: The new description for the agent
            instructions: The new instructions for the agent

        Returns:
            None

        Raises:
            AgentError: If updating the instructions fails
        """
        update_agent_details = UpdateAgentDetails(freeform_tags=FREEFORM_TAGS)
        if name is not None:
            update_agent_details.display_name = name
        if description is not None:
            update_agent_details.description = description
        if instructions is not None:
            llm_customization = LlmCustomization(
                instruction=instructions,
            )
            update_agent_details.llm_config = LlmConfig(
                routing_llm_customization=llm_customization,
            )
        self._invoke(
            method=self._mgmt_client.update_agent,
            success_message="Agent updated successfully",
            error_message="Failed to update agent",
            debug=self.debug,
            update_agent_details=update_agent_details,
            agent_id=agent_id,
        )

    def find_tools(self, compartment_id: str, agent_id: str) -> List[Dict[str, Any]]:
        """
        Find tools associated with the agent.

        Args:
            compartment_id: The compartment ID
            agent_id: The agent ID

        Returns:
            List of tools

        Raises:
            AgentError: If finding tools fails
        """
        # use pagination to eagerly get all records
        find_tools_response: Response = self._invoke(
            method=list_call_get_all_results,
            success_message="Tools retrieval succeeded",
            error_message="Failed to find tools",
            debug=self.debug,
            list_func_ref=self._mgmt_client.list_tools,
            compartment_id=compartment_id,
            agent_id=agent_id,
        )

        return [to_dict(tool) for tool in find_tools_response.data]

    def delete_tool(self, tool_id: str) -> None:
        """
        Delete a tool by ID.

        Args:
            tool_id: The ID of the tool to delete

        Returns:
            None

        Raises:
            AgentError: If tool deletion fails
        """
        self._invoke(
            method=self._mgmt_client.delete_tool,
            success_message="Tool deletion succeeded",
            error_message="Failed to delete tool",
            debug=self.debug,
            tool_id=tool_id,
        )

    def add_function_tool(
        self,
        function: FunctionTool,
        compartment_id: str,
        agent_id: str,
    ) -> Dict[str, Any]:
        """
        Add a function tool to the agent.

        Args:
            function: The function tool to add

        Returns:
            Dict[str, Any]: The added tool as a dict with its attributes

        Raises:
            AgentError: If adding the tool fails
        """
        tool_config = FunctionCallingToolConfig(
            function=Function(
                name=function.name,
                description=function.description,
                parameters=build_custom_function_params(function.parameters),
            )
        )
        create_tool_details = CreateToolDetails(
            display_name=function.name,
            description=function.description,
            compartment_id=compartment_id,
            agent_id=agent_id,
            tool_config=tool_config,
            freeform_tags=FREEFORM_TAGS,
        )

        add_tool_response: Response = self._invoke(
            method=self._mgmt_client.create_tool,
            success_message="Tool addition succeeded",
            error_message="Failed to add tool",
            debug=self.debug,
            create_tool_details=create_tool_details,
        )

        return to_dict(add_tool_response.data)

    def get_tool(self, tool_id: str) -> Dict[str, Any]:
        """
        Get a tool by ID.

        Args:
            tool_id: The ID of the tool to get

        Returns:
            Dict[str, Any]: The tool as a dict with its attributes

        Raises:
            AgentError: If getting the tool fails
        """
        get_tool_response: Response = self._invoke(
            method=self._mgmt_client.get_tool,
            success_message="Tool retrieval succeeded",
            error_message="Failed to get tool",
            debug=self.debug,
            tool_id=tool_id,
        )

        return to_dict(get_tool_response.data)

    def add_rag_tool(
        self,
        rag_tool: AgenticRagTool,
        compartment_id: str,
        agent_id: str,
    ) -> Dict[str, Any]:
        """
        Add an agentic RAG tool to the agent.

        Args:
            rag_tool: The RAG tool to add
            compartment_id: The compartment ID
            agent_id: The agent ID

        Returns:
            Dict[str, Any]: The added tool as a dict with its attributes

        Raises:
            AgentError: If adding the tool fails
        """
        tool_config = RagToolConfig(
            knowledge_base_configs=[
                KnowledgeBaseConfig(knowledge_base_id=kb_id)
                for kb_id in rag_tool.knowledge_base_ids
            ]
        )
        create_tool_details = CreateToolDetails(
            compartment_id=compartment_id,
            agent_id=agent_id,
            display_name=rag_tool.name,
            description=rag_tool.description,
            tool_config=tool_config,
            freeform_tags=FREEFORM_TAGS,
        )

        add_tool_response: Response = self._invoke(
            method=self._mgmt_client.create_tool,
            success_message="RAG tool addition succeeded",
            error_message="""
            Failed to add RAG tool
            probably because a remote RAG tool not configured by ADK already exists
            """,
            debug=self.debug,
            create_tool_details=create_tool_details,
        )

        return to_dict(add_tool_response.data)

    def update_function_tool(
        self,
        tool_id: str,
        function: FunctionTool,
    ) -> None:
        """
        Update a function tool by ID.

        Args:
            tool_id: The ID of the tool to update
            function: The function tool to update

        Returns:
            None

        Raises:
            AgentError: If updating the tool fails
        """
        tool_config = FunctionCallingToolConfig(
            function=Function(
                name=function.name,
                description=function.description,
                parameters=build_custom_function_params(function.parameters),
            )
        )
        update_tool_details = UpdateToolDetails(
            display_name=function.name,
            description=function.description,
            tool_config=tool_config,
            freeform_tags=FREEFORM_TAGS,
        )

        self._invoke(
            method=self._mgmt_client.update_tool,
            success_message="Tool update succeeded",
            error_message="Failed to update tool",
            debug=self.debug,
            tool_id=tool_id,
            update_tool_details=update_tool_details,
        )

    def update_rag_tool(
        self,
        tool_id: str,
        rag_tool: AgenticRagTool,
    ) -> None:
        """
        Update a rag tool by ID.

        Args:
            tool_id: The ID of the tool to update
            rag_tool: The rag tool to update

        Returns:
            None

        Raises:
            AgentError: If updating the tool fails
        """
        tool_config = RagToolConfig(
            knowledge_base_configs=[
                KnowledgeBaseConfig(knowledge_base_id=kb_id)
                for kb_id in rag_tool.knowledge_base_ids
            ]
        )
        update_tool_details = UpdateToolDetails(
            display_name=rag_tool.name,
            description=rag_tool.description,
            tool_config=tool_config,
            freeform_tags=FREEFORM_TAGS,
        )

        self._invoke(
            method=self._mgmt_client.update_tool,
            success_message="RAG tool update succeeded",
            error_message="Failed to update RAG tool",
            debug=self.debug,
            tool_id=tool_id,
            update_tool_details=update_tool_details,
        )

    def get_agent(self, agent_id: str) -> Dict[str, Any]:
        """
        Get the agent details.

        Args:
            agent_id: The ID of the agent

        Returns:
            The agent details

        Raises:
            AgentError: If getting the agent fails
        """

        get_agent_response: Response = self._invoke(
            method=self._mgmt_client.get_agent,
            success_message="Agent retrieval succeeded",
            error_message="Failed to get agent",
            debug=self.debug,
            agent_id=agent_id,
        )

        return to_dict(get_agent_response.data)

    def get_agent_endpoint_details(self, agent_endpoint_id: str) -> Dict[str, Any]:
        """
        Get the agent endpoint details.

        Args:
            agent_endpoint_id: The agent endpoint id

        Returns:
            The agent endpoint details

        Raises:
            AgentError: If getting the agent endpoint fails
        """
        get_agent_endpoint_response: Response = self._invoke(
            method=self._mgmt_client.get_agent_endpoint,
            success_message="Agent endpoint retrieval succeeded",
            error_message="Failed to get agent endpoint",
            debug=self.debug,
            agent_endpoint_id=agent_endpoint_id,
        )

        return to_dict(get_agent_endpoint_response.data)

    def get_runtime_endpoint(
        self, endpoint_url: Optional[str], region: Optional[str]
    ) -> str:
        """
        Get the runtime endpoint.

        Args:
            endpoint_url: The runtime endpoint
            region: The region

        Returns:
            The runtime endpoint
        """
        return self._get_service_endpoint(endpoint_url, region, "agent-runtime")

    def get_management_endpoint(
        self, endpoint_url: Optional[str], region: Optional[str]
    ) -> str:
        """
        Get the management endpoint.

        Args:
            endpoint_url: The management endpoint
            region: The region

        Returns:
            The management endpoint
        """
        return self._get_service_endpoint(endpoint_url, region, "agent")

    def _get_service_endpoint(
        self,
        endpoint_url: Optional[str] = None,
        region: Optional[str] = None,
        endpoint_type: Literal["agent-runtime", "agent"] = "agent-runtime",
    ) -> str:
        """
        Set the service endpoint.

        Args:
            endpoint_url: The service endpoint
            region: The region
            endpoint_type: The endpoint type

        Returns:
            The service endpoint
        """
        # use endpoint if provided, otherwise use region
        if endpoint_url:
            return endpoint_url
        elif region:
            return get_region_endpoint(region, endpoint_type)
        else:
            raise UserError(
                message="At least one of endpoint_url or region must be provided"
            )

    def _invoke(
        self,
        method: Callable,
        success_message: str,
        error_message: str,
        debug: Optional[bool],
        **kwargs,
    ) -> Response:
        """
        Invoke a method.

        Args:
            method: The method to invoke
            success_message: The success message for debug purposes
            error_message: The error message
            debug: Whether to enable debug logging
            **kwargs: Additional keyword arguments to pass in method

        Returns:
            The response
        """
        response: Response | None = None
        try:
            response = method(**kwargs)
            if response is None:
                raise UserError(
                    message=error_message,
                    response=response,
                )

            if response.status not in (200, 202):
                raise AgentError(message=error_message, response=response)

            logger.debug(
                f"{success_message} response: {formatted_flat_dict(response.data)}"
            )
            logger.debug(f"{success_message} {HEADER_REQUEST_ID}: {response.request_id}")

            return response

        except ServiceError as e:
            raise AgentError(
                message=f"{error_message}: {str(e)}",
                response=response,
            ) from e

        except (ValueError, ClientError) as e:
            raise UserError(
                message=f"{error_message}: {str(e)}",
                response=response,
            ) from e
