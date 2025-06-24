# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import random

from mcp.server.fastmcp import FastMCP

# Run this MCP Server from CLI
#
# uv --directory /ABSOLUTE/PATH/TO/FOLDER/CONTAINING/THIS run hello_mcp.py
#


# Create server
mcp = FastMCP("Echo Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"[debug-server] add({a}, {b})")
    return a + b


@mcp.tool()
def get_secret_word() -> str:
    """Get a secret word"""
    print("[debug-server] get_secret_word()")
    return random.choice(["apple", "banana", "cherry"])


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
