# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
ADK Main Agent models
"""
import asyncio
import json

import time
from typing import Any, Callable, Dict, List, Optional, Union

from oci.addons.adk.agent_client import AgentClient
from oci.addons.adk.agent_error import AgentError, UserError
from oci.addons.adk.constants import MAX_STATUS_CHECK, FREEFORM_TAGS
from oci.addons.adk.logger import default_logger as logger
from oci.addons.adk.run.response import RunResponse
from oci.addons.adk.run.types import FunctionCall, PerformedAction, RequiredAction, RawResponse
from oci.addons.adk.tool import FunctionTool, Toolkit, tool
from oci.addons.adk.tool.utils import dedupe_tools_list, diff_local_and_remote_tool
from oci.addons.adk.tool.prebuilt import AgenticRagTool


class Agent:
    """
    An AI agent that can execute tasks using provided tools and instructions.

    The agent maintains synchronization between local and remote tools, handles
    function execution, and manages the interaction loop with the AI.
    """

    # Agent endpoint ID
    agent_endpoint_id: str

    # Agent client
    _client: Optional[AgentClient] = None

    # Base instructions for the agent
    instructions: Optional[str] = None

    # List of tools the agent can use
    tools: Optional[
        List[Union[Callable, FunctionTool, Toolkit, "Agent", AgenticRagTool]]
    ] = None

    # Optional name for the agent
    name: Optional[str] = None

    # Optional description for the agent
    description: Optional[str] = None

    def __init__(
        self,
        agent_endpoint_id: str,
        client: Optional[AgentClient] = None,
        instructions: str = "You are a helpful assistant",
        tools: Optional[
            List[Callable | FunctionTool | Toolkit | "Agent" | AgenticRagTool]
        ] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Initialize an agent instance.

        Args:
            agent_endpoint_id: The agent endpoint ID
            client: The agent client for API communication
            instructions: The base instructions for the agent
            tools: List of tools the agent can use
                (functions, toolkits, or other agents)
            name: Optional name for the agent
            description: Optional description for the agent
        """
        self.agent_endpoint_id = agent_endpoint_id
        self._client = client
        self.instructions = instructions
        self.tools = tools
        self.name = name
        self.description = description

        # varibles not set up user
        self._agent_details: Dict[str, Any] = {}
        self._local_handler_functions: List[FunctionTool] = (
            self._process_function_tools()
        )
        self._local_rag_tools: List[AgenticRagTool] = (
            self._process_agentic_rag_tools()
        )

        # initialization
        self._init_client()

    @property
    def client(self) -> AgentClient:
        """
        Get the agent client, raising an error if it's not initialized.

        Returns:
            The initialized agent client

        Raises:
            UserError: If the client is not initialized
        """
        if self._client is None:
            raise UserError("Agent client is not initialized")
        return self._client

    @property
    def agent_details(self) -> Dict[str, Any]:
        """
        Get the agent details.

        Returns:
            The agent details
        """
        if not self._agent_details:
            self._fetch_and_cache_agent_details()
        return self._agent_details

    def setup(self) -> None:
        """
        Initialize the agent by
        1. checking agent details integrity,
        2. synchronizing agent to remote,
        3. synchronizing local and remote function tools.
        4. synchronizing local and remote rag tools.
        """
        self._check_agent_details_integrity()
        self._sync_agent_to_remote()
        self._sync_function_tools_to_remote()
        self._sync_rag_tools_to_remote()

    def run(
        self,
        input: str,
        session_name: Optional[str] = None,
        session_description: Optional[str] = None,
        session_id: Optional[str] = None,
        delete_session: Optional[bool] = False,
        max_steps: int = 10,
        on_fulfilled_required_action: Optional[
            Callable[[RequiredAction, PerformedAction | None], None]
        ] = None,
        on_invoked_remote_service: Optional[
            Callable[[Dict[str, Any], Dict[str, Any]], None]
        ] = None,
        **kwargs: Optional[Dict[str, Any]],
    ) -> RunResponse:
        """
        Run the agent's react loop to process the user message.

        Args:
            input: The user input to process (required)
            session_name: Name for the processing session
            session_description: Description of the processing session
            session_id: Optional session ID for the processing session
                - if session_id is not provided,
                    the API contract means a new session should be created
                - otherwise, the API contract means
                    we should reuse the provided session id
                    (for same session multi-turn chat)
            delete_session: Optional flag to delete the session after run
                (default: False)
            max_steps: Maximum number of steps before terminating
            on_fulfilled_required_action: Optional callback function
                to handle fulfilled required actions
            on_invoked_remote_service: Optional callback function
                to handle invoked remote services
        Returns:
            RunResponse containing the final result
        """
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(
            self.run_async(
                input,
                session_name,
                session_description,
                session_id,
                delete_session,
                max_steps,
                on_fulfilled_required_action,
                on_invoked_remote_service,
                **kwargs,
            ),
        )

    async def run_async(
            self,
            input: str,
            session_name: Optional[str] = None,
            session_description: Optional[str] = None,
            session_id: Optional[str] = None,
            delete_session: Optional[bool] = False,
            max_steps: int = 10,
            on_fulfilled_required_action: Optional[
                Callable[[RequiredAction, PerformedAction | None], None]
            ] = None,
            on_invoked_remote_service: Optional[
                Callable[[Dict[str, Any], Dict[str, Any]], None]
            ] = None,
            **kwargs: Optional[Dict[str, Any]],
    ) -> RunResponse:
        """
        Run the agent's react loop asynchronously to process the user message.

        Args:
            input: The user input to process
            session_name: Name for the processing session
            session_description: Description of the processing session
            session_id: Optional session ID for the processing session
                - if session_id is not provided,
                    the API contract means a new session should be created
                - otherwise, the API contract means
                    we should reuse the provided session id
                    (for same session multi-turn chat)
            delete_session: Optional flag to delete the session after run
                (default: False)
            max_steps: Maximum number of steps before terminating
            on_fulfilled_required_action: Optional callback function
                to handle fulfilled required actions
            on_invoked_remote_service: Optional callback function
                to handle invoked remote services
        Returns:
            RunResponse containing the final result
        """
        try:
            raw_responses: List[RawResponse] = []
            # if session_id is not provided, create a new one
            if session_id is None:
                session_id = self.client.create_session(
                    agent_endpoint_id=self.agent_endpoint_id,
                    display_name=session_name,
                    description=session_description,
                )
            elif session_name or session_description:
                logger.warning(
                    "session_id is provided, session_name and session_description will be ignored"  # noqa: E501
                )

            # In case agent as tools, kwargs will be passed in, and
            # we want to include them in the user input
            user_message = f"{input} {kwargs}" if kwargs else input

            response = self._handle_chat(
                user_message=user_message,
                session_id=session_id,
                on_invoked_remote_service=on_invoked_remote_service,
            )
            raw_responses.append(RawResponse(raw_data=response))

            step_count = 0
            while self._has_required_actions(response) and step_count < max_steps:
                performed_actions = await self._handle_required_actions(
                    response, on_fulfilled_required_action
                )
                # put a dummy user message before server bug fix
                # it should have been None
                next_user_message = "null"
                # next_user_message = None

                time.sleep(2)  # to avoid throttle by GenAI service
                response = self._handle_chat(
                    user_message=next_user_message,
                    session_id=session_id,
                    performed_actions=performed_actions,
                    on_invoked_remote_service=on_invoked_remote_service,
                )
                raw_responses.append(RawResponse(raw_data=response))
                step_count += 1

            if step_count >= max_steps:
                logger.warning(
                    f"Reached maximum number of steps ({max_steps}). Exiting loop."
                )

        except Exception as e:
            logger.error(f"Error during agent execution: {e}", exc_info=True)
            raise
        finally:
            if delete_session and session_id:
                self.client.delete_session(
                    agent_endpoint_id=self.agent_endpoint_id,
                    session_id=session_id,
                )
        return RunResponse(session_id=session_id, data=response, raw_responses=raw_responses)

    def as_tool(
        self,
        tool_name: str | None = None,
        tool_description: str | None = None,
    ) -> FunctionTool:
        """
        Convert this agent to a FunctionTool that can be used by other agents.

        This allows agents to be composed and used as tools by other agents,
        enabling complex hierarchical agent structures.

        Args:
            tool_name: Optional custom name for the tool. If not provided,
                uses the agent's name or a default.
            tool_description: Optional custom description for the tool. If not provided,
                uses an empty string.

        Returns:
            A FunctionTool representing this agent
        """
        # Use provided tool name or agent name, or fall back to a default
        name = (tool_name or self.name or
                self.client.get_agent(self.agent_details["agent_id"]).get("display_name", None) or
                "run_sub_agent"
                )

        # Use provided description, or fall back to an empty string
        description = (
            tool_description or self.description or
            self.client.get_agent(self.agent_details["agent_id"])
            .get("description", None) or ""
        )

        # Create a decorated wrapper function using the @tool decorator
        @tool(name=name, description=description)
        async def agent_async_run_wrapper(input: str, **kwargs) -> Dict[str, Any] | None:
            """Execute this agent with the given user input and additional params."""
            response = await self.run_async(input=input, **kwargs)
            return response.data

        # Create a FunctionTool from the wrapper
        return FunctionTool.from_callable(agent_async_run_wrapper)

    def create_session(
        self,
        session_name: Optional[str] = None,
        session_description: Optional[str] = None,
    ) -> str:
        """
        Create a new session.
        Wrapper method for client.create_session.

        Args:
            session_name: Name for the session
            session_description: Description of the session

        Returns:
            The session ID
        """
        return self.client.create_session(
            agent_endpoint_id=self.agent_endpoint_id,
            display_name=session_name,
            description=session_description,
        )

    def delete_session(
        self,
        session_id: str
    ) -> None:
        """
        Delete a session.
        Wrapper method for client.delete_session.

        When to use:
        - When you want to explicitly delete a session after the run is complete
        - When the number of sessions exceeds the maximum allowed for the agent endpoint

        Args:
            session_id: The session ID
        """
        self.client.delete_session(
            agent_endpoint_id=self.agent_endpoint_id,
            session_id=session_id,
        )

    def print_local_agent_tools_details(self) -> None:
        """Print the local agent tools details."""
        logger.info(f"Found {len(self._local_handler_functions)} local tools")
        for local_tool in self._local_handler_functions:
            logger.info(local_tool.to_dict())

    def print_remote_agent_details(self) -> None:
        """Print the remote agent details."""
        response = self.client.get_agent(self.agent_details["agent_id"])
        logger.info(f"Agent details: {response}")

    def print_remote_agent_endpoint_details(self) -> None:
        """Print the agent endpoint details."""
        response = self.client.get_agent_endpoint_details(self.agent_endpoint_id)
        logger.info(f"Agent endpoint details: {response}")

    def print_remote_agent_tools_details(
        self, print_deleted_tools: bool = False
    ) -> None:
        """Print the agent tools details."""
        tools = self.client.find_tools(
            compartment_id=self.agent_details["compartment_id"],
            agent_id=self.agent_details["agent_id"],
        )
        active_tools = [
            tool for tool in tools if tool.get("lifecycle_state") == "ACTIVE"
        ]
        deleted_tools = [
            tool for tool in tools if tool.get("lifecycle_state") == "DELETED"
        ]
        logger.info(
            f"Found {len(active_tools)} active tools"
            f"and {len(deleted_tools)} deleted tools"
        )

        if len(active_tools) > 0:
            logger.info("Active tools:")
            for active_tool in active_tools:
                logger.info(active_tool)

        if print_deleted_tools and len(deleted_tools) > 0:
            logger.info("Deleted tools:")
            for deleted_tool in deleted_tools:
                logger.info(deleted_tool)

    def wait_tool_active(self, tool_id: str) -> None:
        """
        Wait for the tool to be active
        """
        count = 0
        while self.client.get_tool(tool_id).get("lifecycle_state") != "ACTIVE":
            time.sleep(5)
            logger.info(f"Waiting for tool {tool_id} to be active...")
            count += 1
            if count > MAX_STATUS_CHECK:
                raise AgentError("Tool did not become active within the timeout period")

    def wait_tool_delete(self, tool_id: str) -> None:
        """
        Wait for the tool to be deleted
        """
        count = 0
        while self.client.get_tool(tool_id).get("lifecycle_state") != "DELETED":
            time.sleep(5)
            logger.info(f"Waiting for tool {tool_id} to be deleted...")
            count += 1
            if count > MAX_STATUS_CHECK:
                raise AgentError("Tool did not become deleted within the timeout period")

    def wait_agent_active(self) -> None:
        """Wait for the agent to be active."""
        count = 0
        while (
            self.client.get_agent(self.agent_details["agent_id"])
                .get("lifecycle_state") != "ACTIVE"
        ):
            time.sleep(5)
            logger.info(f"Waiting for agent {self.agent_details['agent_id']} to be active...")
            count += 1
            if count > MAX_STATUS_CHECK:
                raise AgentError(
                    "Agent did not become active within the timeout period"
                )

    def _handle_chat(
        self,
        user_message: str,
        session_id: str,
        performed_actions: Optional[List[PerformedAction]] = None,
        on_invoked_remote_service: Optional[
            Callable[[Dict[str, Any], Dict[str, Any]], None]
        ] = None,
    ) -> Dict[str, Any]:
        """
        Handle a chat request.

        Args:
            user_message: The user message to display
            session_id: The session ID
            performed_actions: The performed actions
            on_invoked_remote_service: Optional callback function
                to handle invoked remote services

        Returns:
            The response from the agent
        """
        self._log_chat_request(user_message, session_id, performed_actions)

        response = self.client.chat(
            agent_endpoint_id=self.agent_endpoint_id,
            session_id=session_id,
            user_message=user_message,
            performed_actions=performed_actions,
        )

        self._log_chat_response(response)

        if on_invoked_remote_service:
            on_invoked_remote_service(
                {
                    "user_message": user_message,
                    "performed_actions": [
                        action.model_dump() for action in performed_actions
                    ]
                    if performed_actions
                    else None,
                },
                response,
            )

        return response

    def _fetch_and_cache_agent_details(self) -> None:
        """Fetch and cache the agent details."""
        self._agent_details = self.client.get_agent_endpoint_details(self.agent_endpoint_id)

    def _init_client(self) -> None:
        """Initialize the client."""
        if self._client is None:
            self._client = AgentClient()

    def _check_agent_details_integrity(self) -> None:
        """Check the integrity of the agent details."""
        logger.info("Checking integrity of agent details...")
        if not self.agent_details.get("agent_id"):
            raise AgentError("Agent needs to be setup first")

        if self.agent_details.get("should_enable_session") is False:
            raise AgentError("Agent endpoint is not session enabled")

        if self.agent_details.get("lifecycle_state") != "ACTIVE":
            raise AgentError(
                f"Agent endpoint is not active, "
                f"current state: {self.agent_details.get('lifecycle_state')}"
            )

    def _sync_agent_to_remote(self) -> None:
        """Synchronize the local agent settings to the remote agent."""
        logger.info("Checking synchronization of local and remote agent settings...")
        response = self.client.get_agent(self.agent_details["agent_id"])
        display_name = response.get("display_name", None)
        description = response.get("description", None)
        llm_config = response.get("llm_config", {}) or {}
        routing_llm_customization = (
            llm_config.get("routing_llm_customization", {}) or {}
        )
        instruction = routing_llm_customization.get("instruction", "") or ""
        if (
            instruction != self.instructions or
            (self.name is not None and display_name != self.name) or
            (self.description is not None and description != self.description)
        ):
            logger.info(
                "Agent settings are not synchronized. Updating remote agent settings"
            )
            logger.debug(f"Local agent settings: {self.name}, {self.description}, {self.instructions}")
            logger.debug(f"Remote agent settings: {display_name}, {description}, {instruction}")
            self.client.update_agent(
                self.agent_details["agent_id"],
                name=self.name,
                description=self.description,
                instructions=self.instructions,
            )
            self.wait_agent_active()

    def _sync_function_tools_to_remote(self) -> None:
        """
        Synchronize local and remote function tools.

        """
        logger.info("Checking synchronization of local and remote function tools...")
        local_func_tools = self._local_handler_functions
        remote_func_tools = self.client.find_tools(
            compartment_id=self.agent_details["compartment_id"],
            agent_id=self.agent_details["agent_id"],
        )
        remote_func_tools = [
            tool
            for tool in remote_func_tools
            if tool.get("lifecycle_state") == "ACTIVE" and tool.get("tool_config", {})
            .get("tool_config_type") == "FUNCTION_CALLING_TOOL_CONFIG"
        ]
        self._log_tool_counts(local_func_tools, remote_func_tools)
        self._sync_local_and_remote_tools(local_func_tools, remote_func_tools)
        return

    def _sync_rag_tools_to_remote(self) -> None:
        """
        Synchronize local and remote agentic RAG tools.
        """
        logger.info("Checking synchronization of local and remote RAG tools...")
        local_rag_tools = self._local_rag_tools
        # Get existing remote RAG tools
        remote_rag_tools = self.client.find_tools(
            compartment_id=self.agent_details["compartment_id"],
            agent_id=self.agent_details["agent_id"],
        )
        # Filter for active RAG tools with ADK tags
        remote_rag_tools = [
            tool for tool in remote_rag_tools
            if tool.get("lifecycle_state") == "ACTIVE" and
            set(FREEFORM_TAGS.keys()).issubset(tool.get("freeform_tags", {}).keys()) and
            tool.get("tool_config", {}).get("tool_config_type") == "RAG_TOOL_CONFIG"
        ]
        self._sync_local_and_remote_tools(local_rag_tools, remote_rag_tools)
        return

    def _sync_local_and_remote_tools(
        self,
        local_tools: List[FunctionTool] | List[AgenticRagTool],
        remote_tools: List[Dict[str, Any]]
    ) -> None:
        """
        Synchronize local and remote tools.
        Local tools are considered the source of truth. This method will:
            - Remove remote tools that don't exist locally
            - Add local tools that don't exist remotely

        Args:
            local_tools: The local tools
                types: List[FunctionTool] | List[AgenticRagTool]
            remote_tools: The remote tools
                types: List[Dict[str, Any]]
        """
        # Remove remote tools that don't exist locally
        for remote_tool in remote_tools:
            if all(
                diff_local_and_remote_tool(local_tool, remote_tool)
                for local_tool in local_tools
            ):
                logger.info(f"Removing remote tool {remote_tool.get('display_name', '')}...")
                self.client.delete_tool(remote_tool["id"])
                self.wait_tool_delete(remote_tool["id"])
        # Add local tools to remote
        for local_tool in local_tools:
            if all(
                    diff_local_and_remote_tool(local_tool, remote_tool)
                    for remote_tool in remote_tools
            ):
                logger.info(f"Adding local tool {local_tool.name} to remote...")
                if isinstance(local_tool, FunctionTool):
                    new_tool = self.client.add_function_tool(
                        local_tool,
                        compartment_id=self.agent_details["compartment_id"],
                        agent_id=self.agent_details["agent_id"],
                    )
                elif isinstance(local_tool, AgenticRagTool):
                    new_tool = self.client.add_rag_tool(
                        local_tool,
                        compartment_id=self.agent_details["compartment_id"],
                        agent_id=self.agent_details["agent_id"],
                    )
                new_tool_id = new_tool.get("id", "")
                self.wait_tool_active(new_tool_id)
        return

    def _process_function_tools(self) -> List[FunctionTool]:
        """
        Convert all tools to FunctionTool format.
        And de-duplicate tools

        Returns:
            List of processed FunctionTool objects
        """
        available_func_tools: List[FunctionTool] = []

        if self.tools is not None:
            for local_tool in self.tools:
                if isinstance(local_tool, FunctionTool):
                    available_func_tools.append(local_tool)
                elif callable(local_tool):
                    available_func_tools.append(FunctionTool.from_callable(local_tool))
                elif isinstance(local_tool, Toolkit):
                    available_func_tools.extend(local_tool.functions.values())
                elif isinstance(local_tool, Agent):
                    available_func_tools.append(local_tool.as_tool())
        # de-duplicate tools
        return dedupe_tools_list(available_func_tools)

    def _process_agentic_rag_tools(self) -> List[AgenticRagTool]:
        """
        Convert all tools to AgenticRagTool format.
        """
        available_agentic_rag_tools: List[AgenticRagTool] = []
        if self.tools is not None:
            for local_tool in self.tools:
                if isinstance(local_tool, AgenticRagTool):
                    available_agentic_rag_tools.append(local_tool)
        # Check if there is more than one RAG tool for better user experience
        if len(available_agentic_rag_tools) > 1:
            logger.warning(
                "Only one RAG tool is supported at the moment. "
                "You can use multiple knowledge bases IDs in the same RAG tool."
            )
        # de-duplicate tools
        return dedupe_tools_list(available_agentic_rag_tools)

    @staticmethod
    def _has_required_actions(response: Dict[str, Any]) -> bool:
        """Check if the response contains required actions."""
        return response.get("required_actions") is not None

    async def _handle_required_actions(
        self,
        response: Dict[str, Any],
        on_fulfilled_required_action: Optional[
            Callable[[RequiredAction, PerformedAction | None], None]
        ] = None,
    ) -> List[PerformedAction]:
        """
        Process and execute required actions from the response.

        Args:
            response: The response containing required actions
            on_fulfilled_required_action: Optional callback function that will be called
                with performed actions
        Returns:
            List of performed actions
        """
        required_actions = response.get("required_actions", [])
        performed_actions = []

        for action in required_actions:
            required_action = RequiredAction.model_validate(action)
            if (
                required_action.required_action_type ==
                "FUNCTION_CALLING_REQUIRED_ACTION"
            ):
                performed_action = await self._execute_function_call(
                    required_action.function_call, required_action.action_id
                )
                if performed_action:
                    performed_actions.append(performed_action)
                if on_fulfilled_required_action:
                    on_fulfilled_required_action(required_action, performed_action)

        return performed_actions

    async def _execute_function_call(
        self, function_call: FunctionCall, action_id: str
    ) -> Optional[PerformedAction]:
        """
        Execute a single function call action.

        Args:
            function_call: The function call to execute
            action_id: The ID of the action

        Returns:
            Dictionary containing the performed action details
            or None if execution failed
        """
        try:
            function_name = function_call.name
            function_args = (
                json.loads(function_call.arguments)
                if isinstance(function_call.arguments, str)
                else function_call.arguments
            )

            handler = None
            for f in self._local_handler_functions:
                if f.name == function_name:
                    handler = f
                    break

            if not handler:
                logger.info(f"No handler found for function: {function_name}")
                return None

            self._log_function_execution_start(
                handler.name, handler.callable.__name__, function_args
            )
            result = await handler.execute(function_args)
            self._log_function_execution_result(result)

            return PerformedAction(
                action_id=action_id,
                performed_action_type="FUNCTION_CALLING_PERFORMED_ACTION",
                function_call_output=result if isinstance(result, str) else json.dumps(result, default=str),
            )

        except Exception as e:
            logger.error(f"[red]Error executing function '{function_name}':[/red]")
            logger.print_exception(show_locals=True)
            return PerformedAction(
                action_id=action_id,
                performed_action_type="FUNCTION_CALLING_PERFORMED_ACTION",
                function_call_output=str(e),
            )

    def _log_chat_request(
        self,
        message: str,
        session_id: str,
        performed_actions: Optional[List[PerformedAction]] = None,
    ) -> None:
        """
        Log a chat to remote agent.

        Args:
            message: The user message to display
        """
        if not performed_actions:
            actions = []
        else:
            actions = [action.model_dump(mode='json', by_alias=True) for action in performed_actions]

        message_text = (
            f"(Local --> Remote)\n\n"
            f"user message:\n"
            f"[bold green]{message}[/bold green]\n\n"
            f"performed actions by client:\n"
            f"[bold magenta]{actions}[/bold magenta]\n\n"  # noqa: E501
            f"session id:\n"
            f"[bold cyan]{session_id}[/bold cyan]"
        )
        logger.print(
            message_text,
            title=f"Chat request to remote agent: {self.name}",
            border_style="blue",
            expand=False,
        )

    def _log_chat_response(self, response: Dict[str, Any]) -> None:
        """
        Log a chat response from the remote agent.

        Args:
            response: The response containing the chat details
        """

        response_message = json.dumps(response.get("message"), indent=4)
        guardrail_result = None
        if response is not None and "guardrail_result" in response and response["guardrail_result"] is not None:
            guardrail_result = json.loads(str(response.get("guardrail_result")))
            guardrail_result = json.dumps(guardrail_result, indent=4)
        message_text = (
            f"(Local <-- Remote)\n\n"
            f"agent message:\n[bold green]{response_message}[/bold green]\n\n"
            f"required actions for client to take:\n"
            f"[bold magenta]{json.dumps(response.get('required_actions', []), indent=4)}[/bold magenta]\n\n"
            f"guardrail result:\n[bold green]{guardrail_result}[/bold green]\n\n"  # noqa: E501
        )
        logger.print(
            message_text,
            title="Chat response from remote agent",
            border_style="blue",
            expand=False,
        )

    def _log_function_execution_start(
        self, function_tool_name: str, callable_name: str, function_args: Dict[str, Any]
    ) -> None:
        """
        Log the start of a function execution.

        Args:
            function_tool_name: Name of the function tool being executed
            callable_name: Name of the callable function
            function_args: Arguments passed to the function
        """
        message_text = (
            f"Agent function tool name:\n[bold cyan]{function_tool_name}[/bold cyan]\n\n"  # noqa: E501
            f"Agent function tool call arguments:\n[bold green]{function_args}[/bold green]\n\n"  # noqa: E501
            f"Mapped local handler function name:\n[bold cyan]{callable_name}[/bold cyan]"  # noqa: E501
        )
        logger.print(
            message_text,
            title="Function call requested by agent and mapped local handler function",  # noqa: E501
            border_style="light_salmon3",
            expand=False,
        )

    def _log_function_execution_result(self, result: Any) -> None:
        """
        Log the result of a function execution.

        Args:
            result: The result returned by the function
        """
        logger.print(
            f"[bold green]{result}[/bold green]",
            title="Obtained local function execution result",
            border_style="light_salmon3",
            expand=False,
        )

    def _log_tool_counts(
        self, local_tools: List[FunctionTool], remote_tools: List[Dict[str, Any]]
    ) -> None:
        """
        Log the number of local and remote function tools found.

        Args:
            local_tools: List of local FunctionTool objects
            remote_tools: List of remote tool dictionaries
        """
        message_text = (
            f"Local function tools ({len(local_tools)}):\n"
            f"[bold green]{sorted([tool.name for tool in local_tools])}[/bold green]\n\n"  # noqa: E501
            f"Remote function tools ({len(remote_tools)}):\n"
            f"[bold cyan]{sorted([tool['tool_config']['function']['name'] for tool in remote_tools])}[/bold cyan]"
            # noqa: E501
        )
        logger.print(
            message_text,
            title="Local and remote function tools found",
            border_style="blue",
            expand=False,
        )
