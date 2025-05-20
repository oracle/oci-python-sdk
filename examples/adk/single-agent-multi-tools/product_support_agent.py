# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import AgenticRagTool
from custom_function_tools import AccountToolkit

"""
This example shows how an agent with multiple tools work, and how multi-turn runs work.
"""


def main():

    # Assuming the resources were already provisioned
    agent_endpoint_id = "<YOUR-AGENT-ENDPOINT-ID>"
    knowledge_base_id = "<YOUR-KNOWLEDGE-BASE-ID>"

    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
    )

    instructions = """
    You are customer support agent.
    Use KB tool to answer product questions.
    Use tools to fetch user and org info by id.
    Only orgs of Enterprise plan can use Responses API.
    """

    agent = Agent(
        client=client,
        agent_endpoint_id=agent_endpoint_id,
        instructions=instructions,
        tools=[
            AgenticRagTool(
                name="Response API RAG Tool",
                description="You use the knowledge base to answer questions about Response API.",
                knowledge_base_ids=[knowledge_base_id]
            ),
            AccountToolkit()
        ]
    )

    agent.setup()

    # This is a context your existing code is best at producing (e.g., fetching the authenticated user id)
    client_provided_context = "[Context: The logged in user ID is: user_123] "

    # Handle the first user turn of the conversation
    input = "What is the Responses API?"
    input = client_provided_context + " " + input
    response = agent.run(input)
    response.pretty_print()

    # Handle the second user turn of the conversation
    input = "Is my user account eligible for the Responses API?"
    input = client_provided_context + " " + input
    response = agent.run(input, session_id=response.session_id)
    response.pretty_print()


if __name__ == "__main__":
    main()
