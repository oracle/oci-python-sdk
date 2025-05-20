# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import CalculatorToolkit


def main():

    # Initialize the agent client
    client = AgentClient(
        auth_type="security_token",
        profile="PROFILE_1",
        region="ap-osaka-1"
    )

    # Instantiate the local agent object (with the client, instructions, and tools to be registered)
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4",
        instructions="You are a helpful assistant that can perform calculations.",
        tools=[CalculatorToolkit()]
    )

    # Set up the agent once (this configures the instructions and tools in the remote agent resource)
    agent.setup()

    # Use the agent to process the end user request (it automatically handles the function calling)
    input = "What is the square root of 475695037565?"
    response = agent.run(input, max_steps=3)
    response.pretty_print()


if __name__ == "__main__":
    main()
