# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import AgenticRagTool

"""
This example shows an agent with a single Agentic RAG tool that uses a single knowledge base.
"""


def main():

    # Use a custom agent client for custom profile and endpoints settings
    client = AgentClient(
        auth_type="api_key",
        profile="PROFILE_1",
        region="kix"
    )

    # Instantiate the local agent object, with a AgenticRagTool that uses a single knowledge base
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaabced",
        instructions="You are a support agent for OCI Compute. You use the knowledge base to answer questions about OCI Compute.",
        tools=[
            AgenticRagTool(
                name="OCI Compute RAG Tool",
                description="You use the knowledge base to answer questions about OCI Compute.",
                knowledge_base_ids=[
                    "ocid1.genaiagentknowledgebase.oc1.ap-osaka-1.amaaaaa12345",
                ]
            )
        ]
    )

    # Set up the agent once (which pushes local instructions and tools to the remote agent resource)
    agent.setup()

    # Run the agent with a user message
    input = "What is OCI Compute?"
    response = agent.run(input)
    response.pretty_print()


if __name__ == "__main__":
    main()
