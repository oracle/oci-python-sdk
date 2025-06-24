# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from datetime import datetime
from mcp.server.fastmcp import FastMCP

# Run this MCP Server from CLI
#
# uv --directory /ABSOLUTE/PATH/TO/FOLDER/CONTAINING/THIS run server.py
#

mcp = FastMCP("hello_mcp")


@mcp.tool()
async def say_hello(name: str) -> str:
    """Say hello to a person.

    Args:
        name: Name of the person
    """
    print(f"Hello, {name}!")


@mcp.tool()
async def get_greeting(name: str) -> dict[str, str]:
    """Get greeting for a person.

    Args:
        name: Name of the person
    """
    return {
        "greeting": f"Hello, {name}!",
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    # Do not put any statements after mcp.run()
    # Otherwise, the server will not stop upon receiving the exit signal
    mcp.run(transport='stdio')
