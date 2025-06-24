# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import asyncio
import os

from mcp.client.stdio import StdioServerParameters

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.mcp import MCPClientStdio


async def main():
    allowed_directory = os.path.join("examples", "adk", "mcp-test-files")
    # Use a pre-built MCP server from the modelcontextprotocol/server-filesystem package
    # Needs npx. Disconnect to any VPN to execute this
    params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", allowed_directory],
    )

    async with MCPClientStdio(params=params) as mcp_client:
        client = AgentClient(
            auth_type="security_token",
            profile="BoatOc1",
            region="us-chicago-1"
        )

        filesystem_agent = Agent(
            client=client,
            agent_endpoint_id="ocid1.genaiagentendpoint...",
            instructions="Check the allowed directories and list the files in them.",
            tools=[await mcp_client.as_toolkit()]
        )

        content_writer = Agent(
            name="Content Writer",
            instructions="You write a mini blog post (4 sentences) using the trending keywords.",
            agent_endpoint_id="ocid1.genaiagentendpoint...",
            client=client,
            tools=[filesystem_agent]
        )

        filesystem_agent.setup()
        content_writer.setup()

        input = ("Look for trending topics by checking the allowed directories and listing the files provided."
                 " Compose a blog post from those trending topics that is at-least 500 words long.")
        response = await content_writer.run_async(input, max_steps=10)
        response.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())
