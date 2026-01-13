# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import asyncio
from typing import Dict
from oci.addons.adk import Agent, AgentClient, tool

"""
This example shows an agent with a single function tool running in an async mode.
"""


@tool
async def get_weather_async(location: str) -> Dict[str, str]:

    """Get the weather for a given location"""
    await asyncio.sleep(5)
    return {"location": location, "temperature": 72, "unit": "F"}

# Tool can also be defined in the following way
# class WeatherToolkit(Toolkit):
#     @tool
#     async def get_weather_async(location: str) -> Dict[str, str]:
#
#         """Get the weather for a given location"""
#         await asyncio.sleep(5)
#         return {"location": location, "temperature": 72, "unit": "F"}


async def main():

    # Use a custom agent client for custom profile settings
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="kix"
    )

    # Instantiate the local agent object, with a single function tool (plain Python function)
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        instructions="You are a helpful assistant that can perform weather queries.",
        tools=[get_weather_async]
    )

    # Set up the agent once (which configures the instructions and tools in the remote agent resource)
    agent.setup()

    # Run the agent with an input
    input = "Is it cold in Seattle?"
    response = await agent.run_async(input)

    # Should print like "It's not cold in Seattle. The current temperature is 72 degrees Fahrenheit. "
    response.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())
