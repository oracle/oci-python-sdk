# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from typing import Dict
from oci.addons.adk import Agent, AgentClient, tool

"""
This example shows an agent with a single function tool.
"""


@tool
def get_weather(location: str) -> Dict[str, str]:
    """Get the weather for a given location"""
    return {"location": location, "temperature": 72, "unit": "F"}


def main():

    # Use a custom agent client for custom profile settings
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="ORD"
    )

    # Instantiate the local agent object, with a single function tool (plain Python function)
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4",
        instructions="You are a helpful assistant that can perform weather queries.",
        tools=[get_weather]
    )

    # Set up the agent once (which configures the instructions and tools in the remote agent resource)
    agent.setup()

    # Run the agent with an input
    input = "Is it cold in Seattle?"
    response = agent.run(input)

    # Should print like "It's not cold in Seattle. The current temperature is 72 degrees Fahrenheit. "
    response.pretty_print()


if __name__ == "__main__":
    main()
