# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import inspect
import json
from types import MethodType
from typing import Any, Callable, Dict, List

from pydantic import BaseModel, Field

from oci.addons.adk.logger import default_logger as logger
from oci.addons.adk.tool import FunctionTool


class Toolkit(BaseModel):
    """A base class where subclass can declare a collection
    of tools related to a specific task."""

    name: str

    functions: Dict[str, FunctionTool] = Field(default_factory=dict)
    openai_tools_file: str = ""

    def __init__(self, name: str = "toolkit", openai_tools_file: str = ""):
        """Initialize a new Toolkit.

        Args:
            name:
                A descriptive name for the toolkit
            openai_tools_file:
                Optional JSON containing the function definition
                per OpenAI Responses API function tool format
        """
        super().__init__(name=name, functions={}, openai_tools_file=openai_tools_file)

        # Load OpenAI tool definitions if specified
        openai_tools_json = {}
        if openai_tools_file != "":
            try:
                with open(openai_tools_file, "r", encoding="utf-8") as f:
                    openai_tools_json = json.load(f)

                # check it's a JSON object that contains a "tools" key
                if "tools" not in openai_tools_json:
                    raise ValueError("OpenAI tools file must contain a 'tools' key")

                # check the "tools" key is a list
                if not isinstance(openai_tools_json["tools"], list):
                    raise ValueError(
                        "OpenAI tools file must contain a 'tools' key that is a list"
                    )

                # check each item in the list is a JSON object that contains key "type"
                for tool in openai_tools_json["tools"]:
                    if "type" not in tool:
                        raise ValueError(
                            "OpenAI tools file must contain a 'type' key for each tool"
                        )

                    # check the "type" key is "function"
                    if tool["type"] != "function":
                        raise ValueError(
                            "OpenAI tools file must contain a 'type' key "
                            "for each tool that is 'function'"
                        )

                # get the number of tools
                num_tools = len(openai_tools_json["tools"])
                logger.debug(
                    f"[green]Success:[/green] Loaded {num_tools} "
                    f"OpenAI tools from {openai_tools_file}"
                )
            except Exception as e:
                logger.debug(
                    f"[yellow]Warning:[/yellow] Failed to load OpenAI tools "
                    f"from {openai_tools_file}: {e}"
                )

        # Auto-register methods marked with @tool decorator
        for attr_name in dir(self):
            # skip private methods
            if attr_name.startswith("__"):
                continue

            if attr_name.startswith("model_"):
                continue

            attr = getattr(self, attr_name)

            # skip non-callable attributes
            if not callable(attr):
                continue

            # skip non-tool attributes
            if not getattr(attr, "_is_tool", False):
                continue

            # skip not method attributes
            if not isinstance(attr, MethodType):
                continue

            # Ensure method first argument is self
            original_func = attr.__func__
            sig = inspect.signature(original_func)
            params = list(sig.parameters.values())
            if len(params) == 0 or params[0].name != "self":
                raise ValueError(
                    f"@Tool decorated method {attr_name} of {self.__class__.__name__} "
                    "must have a first argument of self"
                )

            matching_openai_tool = None
            if openai_tools_json:
                # Find the matching OpenAI tool def with the same name as the method
                openai_tool_list = openai_tools_json["tools"]
                matching_openai_tool = next(
                    (
                        tool
                        for tool in openai_tool_list
                        if tool.get("name") == attr_name and tool.get("type") == "function"
                    ),
                    None,
                )

            if matching_openai_tool:
                # Create FunctionTool from OpenAI definition
                self._add_function_tool_from_openai(attr, matching_openai_tool)
            else:
                # Create FunctionTool from method decoration
                self._add_function_tool_from_callable(attr)

    def add_function_tool(self, func_tool: FunctionTool) -> None:
        """Add a function tool to the toolkit."""
        self.functions[func_tool.name] = func_tool

    def add_function_tools(self, func_tools: list[FunctionTool]) -> None:
        """Add a list of function tools to the toolkit."""
        for func_tool in func_tools:
            self.add_function_tool(func_tool)

    def get_registered_tools(self) -> List[FunctionTool]:
        """Return a list of all registered tools in the toolkit."""
        return list(self.functions.values())

    def print_arguments_received(self) -> None:
        """Print the arguments received by the tool."""
        # Get the frame of the calling function
        caller_frame = inspect.currentframe()
        if caller_frame is None:
            logger.info("Could not get caller frame")
            return

        caller_frame = caller_frame.f_back
        if caller_frame is None:
            logger.info("Could not get caller's parent frame")
            return

        # Get all arguments of the calling function
        args_info = inspect.getargvalues(caller_frame)
        # Create a dictionary of arguments (excluding 'self')
        args = {arg: args_info.locals[arg] for arg in args_info.args if arg != "self"}
        logger.info(
            f"Executing mock function implementation with received arguments: {args}"
        )

    def _add_function_tool_from_callable(self, callable: Callable[..., Any]) -> None:
        """Internal method to add a function as a tool to the toolkit.

        Args:
            callable: The callable to add as a tool
        """
        try:
            f = FunctionTool.from_callable(callable)
            self.functions[f.name] = f
        except Exception as e:
            raise e

    def _add_function_tool_from_openai(
        self, callable: Callable[..., Any], openai_tool: Dict[str, Any]
    ) -> None:
        """Internal method to add a function as a tool using OpenAI tool definition.

        Args:
            callable: The callable to add as a tool
            openai_tool: The OpenAI tool definition
        """
        try:
            f = FunctionTool.from_callable_openai_tool(callable, openai_tool)
            self.functions[f.name] = f
        except Exception as e:
            raise e

    def __repr__(self):
        return f"<{self.__class__.__name__} name={self.name} functions={list(self.functions.keys())}>"  # noqa: E501

    def __str__(self):
        return self.__repr__()
