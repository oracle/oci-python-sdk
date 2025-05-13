# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import CalculatorToolkit
from oci.addons.adk.run.types import RequiredAction, PerformedAction


def handle_fulfilled_required_action(required_action: RequiredAction, performed_action: PerformedAction):
    tool_call_name = required_action.function_call.name
    tool_call_args = required_action.function_call.arguments
    tool_call_output = performed_action.function_call_output

    # Format JSON strings with proper indentation
    try:
        formatted_args = json.dumps(json.loads(tool_call_args), indent=2)
    except ValueError:
        formatted_args = tool_call_args

    try:
        formatted_output = json.dumps(json.loads(tool_call_output), indent=2)
    except ValueError:
        formatted_output = tool_call_output

    base_message = f"Executed client-side function tool: **{tool_call_name}**"
    details = f"Function Tool call arguments:\n```json\n{formatted_args}\n```\nFunction Tool call output:\n```json\n{formatted_output}\n```"

    # Display the status
    print(base_message)
    print(details)


def handle_invoked_remote_service(chat_request, chat_response):
    label = "Invoked Agent Service API: "
    if chat_response.get("required_actions"):
        label += f" received {len(chat_response.get('required_actions'))} action(s) for client to take"
    else:
        label += " received agent text message"

    content = f"Agent Service call request:\n```json\n{json.dumps(chat_request, indent=2)}\n```\nAgent Service call response:\n```json\n{json.dumps(chat_response, indent=2)}\n```"

    # Display the status
    print(label)
    print(content)


def main():

    # Assuming the agent and agent endpoint resources were already provisioned
    adk_demo_agent_endpoint_id = "ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4qa"

    try:
        # Initialize the agent client
        client = AgentClient(
            auth_type="security_token",
            profile="BoatOc1",
            region="AP-OSAKA-1"
        )

        # Instantiate the local agent object (with the client, instructions, and tools to be registered)
        agent = Agent(
            client=client,
            agent_endpoint_id=adk_demo_agent_endpoint_id,
            instructions="You are a helpful assistant that can perform calculations.",
            tools=[CalculatorToolkit()]
        )

        # Set up the agent once (this configures the instructions and tools in the remote agent resource)
        agent.setup()

        # Use the agent to process the end user request (it automatically handles the function calling)
        input = "What is the square root of 475695037565?"
        response = agent.run(
            input,
            max_steps=6,
            on_fulfilled_required_action=handle_fulfilled_required_action,
            on_invoked_remote_service=handle_invoked_remote_service,
        )

        response.pretty_print()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
