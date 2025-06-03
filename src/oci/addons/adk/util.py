# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import inspect
import json
from types import NoneType
from typing import Any, Callable, Dict, Optional, Tuple, Union, get_args, get_origin

from docstring_parser import parse
from oci import regions


class DocstringParser:
    """Utility class for parsing and extracting information from docstrings."""

    @staticmethod
    def get_callable_description(callable_func: Callable) -> str:
        """
        Extract a description from a callable's docstring.

        Args:
            callable_func: The function or method to extract description from

        Returns:
            A string containing the combined short and long descriptions
        """
        doc = inspect.getdoc(callable_func)
        if not doc:
            return ""

        parsed = parse(doc)

        # Combine short and long descriptions
        result = ""
        if parsed.short_description:
            result = parsed.short_description
        if parsed.long_description:
            # Preserve the double newline between short and long descriptions
            if result:
                result += "\n\n"
            result += parsed.long_description

        return result


class JsonSchemaGenerator:
    """Utility class for generating JSON schemas from Python type annotations."""

    # Constants for type mapping
    JSON_TYPE_MAPPING = {
        "int": "number",
        "float": "number",
        "complex": "number",
        "Decimal": "number",
        "str": "string",
        "string": "string",
        "bool": "boolean",
        "boolean": "boolean",
        "NoneType": "null",
        "None": "null",
        "list": "array",
        "tuple": "array",
        "set": "array",
        "frozenset": "array",
        "dict": "object",
        "mapping": "object",
    }

    # Collection types that should be treated as arrays
    ARRAY_TYPES = (list, tuple, set, frozenset)

    @classmethod
    def get_json_type_for_py_type(cls, arg_type: str) -> str:
        """
        Get the JSON schema type for a given Python type.

        Args:
            arg_type: The Python type name to convert

        Returns:
            The corresponding JSON schema type
        """
        return cls.JSON_TYPE_MAPPING.get(arg_type, "object")

    @classmethod
    def get_json_schema_for_arg(cls, t: Any) -> Optional[Dict[str, Any]]:
        """
        Generate a JSON schema for a given type annotation.

        Args:
            t: The type annotation to convert to JSON schema

        Returns:
            A dictionary representing the JSON schema for the type
        """
        type_args = get_args(t)
        type_origin = get_origin(t)

        if type_origin is not None:
            if type_origin in cls.ARRAY_TYPES:
                return cls._handle_array_type(type_args)
            elif type_origin is dict:
                return cls._handle_dict_type(type_args)
            elif type_origin is Union:
                return cls._handle_union_type(type_args)

        return {"type": cls.get_json_type_for_py_type(t.__name__)}

    @classmethod
    def _handle_array_type(cls, type_args: Tuple) -> Dict[str, Any]:
        """Helper method to handle array-like types"""
        json_schema_for_items = (
            cls.get_json_schema_for_arg(type_args[0])
            if type_args
            else {"type": "string"}
        )
        return {"type": "array", "items": json_schema_for_items}

    @classmethod
    def _handle_dict_type(cls, type_args: Tuple) -> Dict[str, Any]:
        """Helper method to handle dictionary types"""
        key_schema = (
            cls.get_json_schema_for_arg(type_args[0])
            if type_args
            else {"type": "string"}
        )
        value_schema = (
            cls.get_json_schema_for_arg(type_args[1])
            if len(type_args) > 1
            else {"type": "string"}
        )
        return {
            "type": "object",
            "propertyNames": key_schema,
            "additionalProperties": value_schema,
        }

    @classmethod
    def _handle_union_type(cls, type_args: Tuple) -> Optional[Dict[str, Any]]:
        """Helper method to handle Union types"""
        types = []
        for arg in type_args:
            if arg is not NoneType:
                try:
                    schema = cls.get_json_schema_for_arg(arg)
                    if schema:
                        types.append(schema)
                except Exception:
                    continue
        return {"anyOf": types} if types else None

    @staticmethod
    def is_optional_type(v: Any) -> Tuple[bool, Any]:
        """
        Check if a type is Optional (Union with NoneType) and extract the actual type.

        Args:
            v: The type to check

        Returns:
            A tuple of (is_optional, actual_type)
        """
        type_origin = get_origin(v)
        type_args = get_args(v)
        is_optional = (
            type_origin is Union and
            len(type_args) == 2 and
            any(arg is NoneType for arg in type_args)
        )
        if is_optional:
            actual_type = next(arg for arg in type_args if arg is not NoneType)
            return True, actual_type

        return False, v

    @classmethod
    def get_json_schema(
        cls,
        type_hints: Dict[str, Any],
        param_descriptions: Optional[Dict[str, str]] = None,
        strict: bool = False,
    ) -> Dict[str, Any]:
        """
        Generate a JSON schema from type hints and parameter descriptions.

        Args:
            type_hints: Dictionary of parameter names to their type annotations
            param_descriptions: Optional dictionary of parameter descriptions
            strict: Whether to disallow additional properties

        Returns:
            A JSON schema object
        """
        json_schema: Dict[str, Any] = {
            "type": "object",
            "properties": {},
        }
        if strict:
            json_schema["additionalProperties"] = False

        for k, v in type_hints.items():
            if k == "return":
                continue

            try:
                is_optional, actual_type = cls.is_optional_type(v)

                # Handle cases with no type hint
                if actual_type:
                    arg_json_schema = cls.get_json_schema_for_arg(actual_type)
                else:
                    arg_json_schema = {}

                if arg_json_schema is not None:
                    if is_optional:
                        # Handle null type for optional fields
                        if isinstance(arg_json_schema.get("type"), list):
                            arg_json_schema["type"].append("null")
                        else:
                            arg_json_schema["type"] = [arg_json_schema["type"], "null"]

                    # Add description
                    if (param_descriptions and k in param_descriptions and param_descriptions[k]):
                        arg_json_schema["description"] = param_descriptions[k]

                    json_schema["properties"][k] = arg_json_schema
            except Exception:
                continue

        return json_schema


# Maintain backward compatibility with the original function names
def get_callable_description(callable_func: Callable) -> str:
    return DocstringParser.get_callable_description(callable_func)


def get_json_type_for_py_type(arg_type: str) -> str:
    return JsonSchemaGenerator.get_json_type_for_py_type(arg_type)


def get_json_schema_for_arg(t: Any) -> Optional[Dict[str, Any]]:
    return JsonSchemaGenerator.get_json_schema_for_arg(t)


def get_json_schema(
    type_hints: Dict[str, Any],
    param_descriptions: Optional[Dict[str, str]] = None,
    strict: bool = False,
) -> Dict[str, Any]:
    return JsonSchemaGenerator.get_json_schema(type_hints, param_descriptions, strict)


def build_custom_function_params(func_params: Dict[str, Any]) -> Dict[str, str]:
    """
    Build a dictionary of function parameters for customizing a function.
    This function ensures that all values are json serialized
    which is required for current OCI Agent function calls API.

    Args:
        func_params: Dictionary of function parameters to customize

    Returns:
        A dictionary of parameters with string values
    """
    new_func_params = {}
    for k, v in func_params.items():
        if isinstance(v, str):
            new_func_params[k] = v
        elif isinstance(v, dict):
            new_func_params[k] = json.dumps(v)
        elif isinstance(v, list):
            new_func_params[k] = json.dumps(v)
        else:
            new_func_params[k] = str(v)
    return new_func_params


def read_custom_function_params(func_params: Dict[str, str]) -> Dict[str, Any]:
    """
    Read a dictionary of function parameters from a dictionary of string values.

    Args:
        func_params: Dictionary of function parameters with string values

    Returns:
        A dictionary of parameters with their original types
    """
    new_func_params = {}
    for k, v in func_params.items():
        if isinstance(v, dict):
            new_func_params[k] = json.loads(v)
        else:
            new_func_params[k] = v
    return new_func_params


def get_region_endpoint(
    region: str, endpoint: str, service: str = "generativeai"
) -> str:
    """
    Get the endpoint for a given region and service.

    Args:
        region: The region to use, e.g. "FRA" or "us-chicago-1"
        endpoint: The endpoint to use, e.g. "agent" or "agent-runtime"
        service: The service to use, default "generativeai"

    Returns:
        The endpoint for the given region and service
    """
    service_endpoint_template = (
        f"https://{endpoint}.{service}" + ".{region}.oci.{secondLevelDomain}"
    )
    return regions.endpoint_for(
        service=service,
        region=region,
        service_endpoint_template=service_endpoint_template,
    )
