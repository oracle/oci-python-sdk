# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
ADK Run action models
"""

from pydantic import BaseModel, Field


class FunctionCall(BaseModel):
    """Represents a function call that is required from the client."""

    name: str = Field(..., alias="name")
    arguments: str | dict = Field(..., alias="arguments")


class PerformedAction(BaseModel):
    """Represents an action that was performed by the agent."""

    action_id: str = Field(..., alias="action_id")
    performed_action_type: str = Field(..., alias="performed_action_type")
    function_call_output: str = Field(..., alias="function_call_output")


class RequiredAction(BaseModel):
    """Represents an action that is required from the client."""

    action_id: str = Field(..., alias="action_id")
    required_action_type: str = Field(..., alias="required_action_type")
    function_call: FunctionCall = Field(..., alias="function_call")
