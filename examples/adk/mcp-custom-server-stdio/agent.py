# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import asyncio
import os

from mcp.client.stdio import StdioServerParameters

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.mcp import MCPClientStdio


async def main():

    # Use a custom MCP server written in Python locally.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    params = StdioServerParameters(
        command="python",
        args=[os.path.join(current_dir, "server.py")],
    )

    async with MCPClientStdio(params=params) as mcp_client:

        client = AgentClient(
            auth_type="security_token",
            profile="DEFAULT",
            region="us-chicago-1"
        )

        agent = Agent(
            client=client,
            agent_endpoint_id="ocid1.genaiagentendpoint...",
            instructions="Use tools to generate a greeting.",
            tools=[await mcp_client.as_toolkit()],
        )

        agent.setup()

        input = "Greet me as 'John'"
        response = await agent.run_async(input)

        response.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())
