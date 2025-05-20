# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from typing import Dict, Any, List, TypeVar

from oci.addons.adk.tool.function_tool import FunctionTool
from oci.addons.adk.tool.prebuilt.agentic_rag_tool import AgenticRagTool
from oci.addons.adk.logger import default_logger as logger
from oci.addons.adk.util import build_custom_function_params


def diff_local_and_remote_tool(
    local_tool: FunctionTool | AgenticRagTool,
    remote_tool: Dict[str, Any],
) -> bool:
    """
    Return true if the local tool and the remote tool are different.

    Args:
        local_tool: The local tool
        remote_tool: The remote tool

    Returns:
        True if the local tool and the remote tool are different, False otherwise
    """
    local_tool_json_spec: Dict[str, Any] = {}
    remote_tool_json_spec: Dict[str, Any] = {}

    if isinstance(local_tool, FunctionTool):
        local_tool_json_spec = {
            "tool_name": local_tool.name,
            "tool_description": local_tool.description,
            "name": local_tool.name,
            "description": local_tool.description,
            "parameters": build_custom_function_params(local_tool.parameters),
        }

        remote_tool_json_spec = {
            "tool_name": remote_tool.get("display_name", ""),
            "tool_description": remote_tool.get("description", ""),
            **remote_tool["tool_config"]["function"],
        }

    elif isinstance(local_tool, AgenticRagTool):
        local_tool_json_spec = {
            "name": local_tool.name,
            "description": local_tool.description,
            "knowledge_base_ids": sorted(local_tool.knowledge_base_ids),
        }
        remote_tool_json_spec = {
            "name": remote_tool.get("display_name", ""),
            "description": remote_tool.get("description", ""),
            "knowledge_base_ids": sorted(
                [
                    kb_config.get("knowledge_base_id")
                    for kb_config in remote_tool.get("tool_config", {}).get(
                        "knowledge_base_configs", []
                    )
                ]
            )
        }

    logger.debug(f"Local tool JSON spec: {local_tool_json_spec}")
    logger.debug(f"Remote tool JSON spec: {remote_tool_json_spec}")

    return local_tool_json_spec != remote_tool_json_spec


def compare_local_and_remote_tools(
    local_tools: List[FunctionTool] | List[AgenticRagTool],
    remote_tools: List[Dict[str, Any]],
) -> bool:
    """
    Return true if the local tools and the remote tools are the same.

    Args:
        local_tools: The local tools
        remote_tools: The remote tools

    Returns:
        True if the all local tools and the remote tools are the same, False otherwise
    """
    same_list: List[bool] = []
    # different number of tools
    if len(local_tools) != len(remote_tools):
        return False
    for local_tool in local_tools:
        # any remote tool is the same with local tool
        same_list.append(
            any(
                not diff_local_and_remote_tool(local_tool, remote_tool)
                for remote_tool in remote_tools
            )
        )
    # all local tools are the same with remote tools
    return all(same_list)


T = TypeVar('T')


def dedupe_tools_list(
    tools_list: List[T],
) -> List[T]:
    """
    Return a list of unique tools.

    Args:
        tools_list: The tools list of any type

    Returns:
        A list of unique tools of the same type as input
    """
    result_tools_list: List[T] = []
    for tool in tools_list:
        if any(tool == exist_tool for exist_tool in result_tools_list):
            continue
        result_tools_list.append(tool)
    return result_tools_list
