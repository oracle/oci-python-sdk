# flake8: noqa
# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
This example shows how to access traces of an agent run.
"""

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.run.traces import RetrievalTrace, GenerationTrace, PlanningTrace, ToolInvocationTrace
from oci.addons.adk.tool.prebuilt import AgenticRagTool


def main():
    client = AgentClient(
        auth_type="security_token",
        profile="BoatOc1",
        region="us-chicago-1"
    )

    # Assuming the knowledge base is already provisioned
    knowledge_base_id = "ocid1.genaiagentknowledgebase..."

    # Create a RAG tool that uses the knowledge base
    rag_tool = AgenticRagTool(name="OCI Compute RAG Tool",
                              description="You use the knowledge base to answer questions about OCI Compute.",
                              knowledge_base_ids=[knowledge_base_id])

    # Create the agent with the RAG tool
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        instructions="Answer question using the provided RAG tool.",
        tools=[rag_tool]
    )

    # Set up the agent once
    agent.setup()

    # Run the agent with a user query
    input = "Tell me about Oracle Compute Service."
    response = agent.run(input)
    response.pretty_print()

    # Access response traces
    traces = response.traces
    for trace in traces:
        if isinstance(trace, PlanningTrace):
            input = trace.input
            output = trace.output
            usage = trace.usage

        elif isinstance(trace, ToolInvocationTrace):
            tool_id = trace.tool_id
            tool_name = trace.tool_name
            invocation_details = trace.invocation_details

        elif isinstance(trace, RetrievalTrace):
            input = trace.retrieval_input
            citations = trace.citations
            for citation in citations:
                source_text = citation.source_text
                source_location_type = citation.source_location.source_location_type
                source_location_url = citation.source_location.url
            usage = trace.usage

        elif isinstance(trace, GenerationTrace):
            input = trace.input
            output = trace.generation
            usage = trace.usage

    # Print Response Traces
    response.pretty_print_traces()


if __name__ == "__main__":
    main()
