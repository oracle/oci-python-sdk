# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import asyncio
import os

from mcp.client.stdio import StdioServerParameters

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.mcp import MCPClientStdio


async def main():
    # Use a pre-built MCP server from the modelcontextprotocol/server-time
    time_server_params = StdioServerParameters(
        command="uvx",
        args=["mcp-server-time", "--local-timezone=America/Los_Angeles"],
    )
    allowed_directory = os.path.join("examples", "adk", "mcp-test-files")

    # Use another pre-built MCP server from the modelcontextprotocol/server-filesystem
    # Needs npx. Disconnect to any VPN to execute this
    fs_server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", allowed_directory])

    client = AgentClient(
        auth_type="security_token",
        profile="DEFAULT",
        region="us-chicago-1"
    )

    async with MCPClientStdio(params=time_server_params) as time_mcp_client, \
            MCPClientStdio(params=fs_server_params) as fs_mcp_client:

        agent = Agent(
            client=client,
            agent_endpoint_id="ocid1.genaiagentendpoint...",
            instructions="You perform filesystem and time queries.",
            tools=[await time_mcp_client.as_toolkit(), await fs_mcp_client.as_toolkit()]
        )

        agent.setup()

        input = ("Check the allowed directories and list the files in them. "
                 "The output should contain how many days has passed since the files were created.")
        response = await agent.run_async(input)
        response.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())
