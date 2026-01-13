# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import asyncio
from inspect import getdoc, ismethod, signature
from typing import Any, Callable, Dict, get_type_hints

from docstring_parser import parse
from pydantic import BaseModel, ConfigDict, Field, validate_call

from oci.addons.adk.logger import default_logger as logger
from oci.addons.adk.util import DocstringParser, JsonSchemaGenerator


class FunctionTool(BaseModel):
    """Represents a callable function with metadata for tool-based execution."""

    name: str = Field(
        description="The name of the tool, used for identification and invocation"
    )

    description: str = Field(
        description="Human-readable description of what the tool does and how to use it"
    )

    parameters: Dict[str, Any] = Field(
        default_factory=lambda: {"type": "object", "properties": {}, "required": []},
        description="JSON Schema object describing function parameters, their types, and requirements",  # noqa: E501
    )

    callable: Callable = Field(
        description="The actual function that will be executed when the tool is invoked"
    )

    @classmethod
    def from_callable(
        cls, callable_func: Callable, strict: bool = False
    ) -> "FunctionTool":
        """
        Create a FunctionTool from a callable function,
        using docstring for function description and parameter descriptions

        Args:
            callable_func: The function to convert to a tool
            strict: If True, mark all parameters as required regardless of defaults

        Returns:
            A FunctionTool instance representing the callable

        Raises:
            ValueError: If the function is not marked as a tool
        """
        # Verify the function is marked as a tool
        if not hasattr(callable_func, "_is_tool"):
            raise ValueError(
                f"Function {callable_func.__name__} is not marked as a tool"
            )

        # Extract function name
        # use _tool_name if provided, otherwise use the function's name
        function_name = getattr(callable_func, "_tool_name", callable_func.__name__)

        # Extract function description
        # use _tool_description if provided, otherwise use the function's docstring
        function_description = getattr(
            callable_func,
            "_tool_description",
            DocstringParser.get_callable_description(callable_func),
        )

        # Build parameter schema
        function_parameters = cls._build_parameter_schema(callable_func, strict)

        return cls(
            name=function_name,
            description=function_description,
            parameters=function_parameters,
            callable=validate_call(config=ConfigDict(arbitrary_types_allowed=True))(
                callable_func
            ),
        )

    @classmethod
    def from_callable_openai_tool(
        cls, callable_func: Callable, openai_tool: Dict[str, Any], strict: bool = False
    ) -> "FunctionTool":
        """
        Create a FunctionTool from a callable function
        and dictionary loaded from an OpenAI JSON schema.

        Args:
            callable_func: The function to convert to a tool
            openai_tool: Dictionary containing OpenAI JSON schema

        Returns:
            A FunctionTool instance using the given callable
            but with the OpenAI tool JSON schema
        """

        # Verify the function is marked as a tool
        if not hasattr(callable_func, "_is_tool"):
            raise ValueError(
                f"Function {callable_func.__name__} is not marked as a tool"
            )

        function_name = openai_tool.get("name")
        function_description = openai_tool.get("description")
        function_parameters_oai = openai_tool.get("parameters")

        if (
            not isinstance(function_parameters_oai, dict) or
            function_name is None or
            function_description is None
        ):
            raise ValueError(
                f"Invalid OpenAI tool schema: "
                f"name: {function_name}, "
                f"description: {function_description}, "
                f"parameters: {function_parameters_oai}"
            )

        # validate the function parameters name
        # and type are the same as the OpenAI tool parameters
        function_parameters_func = cls._build_parameter_schema(callable_func, strict)
        for param_name, param_type in function_parameters_func.get(
            "properties", {}
        ).items():
            if (
                param_name not in function_parameters_oai.get("properties", {})
            ):
                raise ValueError(
                    f"Local function and OpenAI tool parameters mismatch:"
                    f" Function parameter {param_name} of local function "
                    f"{callable_func.__name__} cannot be found "
                    "in the OpenAI tool parameters"
                )
            if param_type.get("type") != function_parameters_oai.get(
                "properties", {}
            ).get(param_name).get("type"):
                # Convert both 'integer' and OpenAI types to 'number'
                local_type = (
                    "number"
                    if param_type.get("type") == "integer"
                    else param_type.get("type")
                )
                oai_type = (
                    "number"
                    if function_parameters_oai.get("properties", {})
                    .get(param_name)
                    .get("type") == "integer"
                    else function_parameters_oai.get("properties", {})
                    .get(param_name)
                    .get("type")
                )
                if local_type != oai_type:
                    raise ValueError(
                        f"Local function and OpenAI tool parameters mismatch: "
                        f" Function parameter {param_name} of local function "
                        f"{callable_func.__name__} has type {local_type} "
                        f" which does not match OpenAI tool parameter type {oai_type}"
                    )

        # validate all parameters present in OpenAI tool parameters
        # are present in the local function parameters
        for param_name in function_parameters_oai.get("properties", {}):
            if param_name not in function_parameters_func.get("properties", {}):
                raise ValueError(
                    f"Local function and OpenAI tool parameters mismatch: "
                    f"Function parameter {param_name} is not "
                    "in the local function parameters"
                )

        return cls(
            name=function_name,
            description=function_description,
            parameters=function_parameters_oai,
            callable=validate_call(config=ConfigDict(arbitrary_types_allowed=True))(
                callable_func
            ),
        )

    async def execute(self, arguments: Dict[str, Any]) -> Any:
        """
        Execute the function with the given arguments.

        Args:
            arguments: Dictionary of arguments to pass to the function

        Returns:
            The result of the function execution

        Raises:
            ValueError: If required arguments are missing or invalid
        """
        # Clean and filter arguments
        filtered_args = self._prepare_arguments(arguments)

        if asyncio.iscoroutinefunction(self.callable):
            result = await self.callable(**filtered_args)
        else:
            # Invoke the callable with the filtered arguments
            result = self.callable(**filtered_args)

        return result

    def to_dict(self) -> Dict[str, Any]:
        """Convert the tool to a dictionary representation, excluding the callable."""
        return self.model_dump(
            exclude_none=True, include={"name", "description", "parameters"}
        )

    # Private helper methods
    def _prepare_arguments(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Clean and filter arguments for execution.

        Args:
            arguments: Raw arguments dictionary

        Returns:
            Cleaned and filtered arguments dictionary
        """
        # Clean up argument keys - remove any trailing colons and whitespace
        cleaned_args = {
            key.rstrip(":").strip(): value for key, value in arguments.items()
        }

        # Filter out any arguments that aren't in the function's parameters
        valid_params = self.parameters.get("properties", {}).keys()
        return {k: v for k, v in cleaned_args.items() if k in valid_params}

    @staticmethod
    def _build_parameter_schema(
        callable_func: Callable, strict: bool
    ) -> Dict[str, Any]:
        """
        Build a JSON schema for the function's parameters.

        Args:
            callable_func: The function to analyze
            strict: If True, mark all parameters as required

        Returns:
            A JSON schema object describing the function parameters
        """
        parameters = {"type": "object", "properties": {}, "required": []}

        try:
            sig = signature(callable_func)
            type_hints = get_type_hints(callable_func)

            # If it's a bound method (like method of Toolkit),
            # we need to get the original function's signature
            if ismethod(callable_func):
                sig = signature(callable_func.__func__)
                type_hints = get_type_hints(callable_func.__func__)

            # Remove agent parameter if present
            if "agent" in sig.parameters:
                type_hints.pop("agent", None)

            # Filter out return type and only process parameters
            param_type_hints = {
                name: type_hints.get(name)
                for name in sig.parameters
                if name != "return" and name != "agent" and name != "self"
            }

            # Parse docstring for parameter descriptions
            param_descriptions = FunctionTool._extract_param_descriptions(callable_func)

            # Generate JSON schema for parameters
            parameters = JsonSchemaGenerator.get_json_schema(
                type_hints=param_type_hints,
                param_descriptions=param_descriptions,
                strict=strict,
            )

            logger.debug(f"Parameters: {parameters}")

            # Determine required parameters
            if strict:
                parameters["required"] = [
                    name for name in parameters["properties"] if name != "agent"
                ]
            else:
                parameters["required"] = [
                    name
                    for name, param in sig.parameters.items()
                    if param.default == param.empty and
                    name != "self" and
                    name != "agent"
                ]

        except Exception as e:
            logger.print(
                f"[yellow]Warning:[/] "
                f"Could not parse args for {callable_func.__name__}: {e}"
            )

        return parameters

    @staticmethod
    def _extract_param_descriptions(callable_func: Callable) -> Dict[str, str]:
        """
        Extract parameter descriptions from function docstring.

        Args:
            callable_func: The function to analyze

        Returns:
            Dictionary mapping parameter names to their descriptions
        """
        param_descriptions = {}
        docstring = getdoc(callable_func)
        if docstring:
            parsed_doc = parse(docstring)
            param_docs = parsed_doc.params

            if param_docs is not None:
                for param in param_docs:
                    param_name = param.arg_name
                    param_type = param.type_name
                    param_descriptions[param_name] = (
                        f"({param_type}) {param.description}"
                    )

        return param_descriptions

    # Equality comparison
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FunctionTool):
            return NotImplemented
        return (
            self.name == other.name and
            self.description == other.description and
            self.parameters == other.parameters
        )
