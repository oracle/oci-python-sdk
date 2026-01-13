# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import inspect
from functools import wraps

from oci.addons.adk.util import get_callable_description


def tool(func=None, *, name=None, description=None):
    """
    Decorator to mark a function as a tool for the agent.

    Args:
        func: The function to decorate
        name: Optional name for the tool (defaults to function name)
        description: Optional description (defaults to function docstring)
    """

    def decorator(func):
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        if inspect.iscoroutinefunction(func):
            wrapper = async_wrapper
        else:
            wrapper = sync_wrapper

        # wrap the function with tool metadata
        wrapper._is_tool = True
        wrapper._tool_name = name or func.__name__
        wrapper._tool_description = (
            description or get_callable_description(callable_func=func) or ""
        )

        return wrapper

    # Handle both @tool and @tool(name="name", description="desc") syntax
    if func is None:
        return decorator
    return decorator(func)
