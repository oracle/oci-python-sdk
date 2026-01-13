# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import asyncio
import os
import subprocess
import time
from typing import Any

from mcp.client.session_group import StreamableHttpParameters

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.mcp import MCPClientStreamableHttp


async def main():
    # We'll run the Streamable HTTP server in a subprocess
    # Usually this would be a remote server, but for this demo, we'll run it locally
    process: subprocess.Popen[Any] | None = None
    try:
        this_dir = os.path.dirname(os.path.abspath(__file__))
        server_file = os.path.join(this_dir, "server.py")

        print("Starting Streamable HTTP server at http://localhost:8000/mcp ...")

        # Run `python server.py` to start the Streamable HTTP server
        process = subprocess.Popen(["python", server_file])
        # Give it 3 seconds to start
        time.sleep(3)

        print("Streamable HTTP server started. Running example...\n\n")

        # Connect to the HTTP MCP server
        async with MCPClientStreamableHttp(
            params=StreamableHttpParameters(
                url="http://localhost:8000/mcp",
            ),
            name="Streamable HTTP Python Server",
        ) as mcp_client:

            # Create the agent client
            client = AgentClient(
                auth_type="security_token",
                profile="DEFAULT",
                region="kix"
            )

            # Create and set up the agent
            agent = Agent(
                client=client,
                agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4qa",
                instructions="Use the tools to answer the questions.",
                tools=[await mcp_client.as_toolkit()],
            )

            agent.setup()

            # Test with various tool calls
            # Use the `add` tool to add two numbers
            input_message = "Add these numbers: 7 and 22."
            print(f"Running: {input_message}")
            response = await agent.run_async(input_message)
            response.pretty_print()

            # Run the `get_secret_word` tool
            input_message = "What's the secret word?"
            print(f"\n\nRunning: {input_message}")
            response = await agent.run_async(input_message)
            response.pretty_print()

    except Exception as e:
        print(f"Error: {e}")
        if process:
            process.terminate()
        exit(1)
    finally:
        if process:
            process.terminate()


if __name__ == "__main__":

    asyncio.run(main())
