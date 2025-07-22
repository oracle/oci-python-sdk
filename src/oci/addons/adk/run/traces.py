# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
ADK Traces models
"""
from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict, Any, Union

from pydantic import BaseModel


class TraceType(str, Enum):
    """Represents the type of the trace."""

    ERROR_TRACE = "ERROR_TRACE"
    RETRIEVAL_TRACE = "RETRIEVAL_TRACE"
    TOOL_INVOCATION_TRACE = "TOOL_INVOCATION_TRACE"
    GENERATION_TRACE = "GENERATION_TRACE"
    PLANNING_TRACE = "PLANNING_TRACE"
    EXECUTION_TRACE = "EXECUTION_TRACE"

    def get_class(self):
        return {
            TraceType.ERROR_TRACE: ErrorTrace,
            TraceType.RETRIEVAL_TRACE: RetrievalTrace,
            TraceType.TOOL_INVOCATION_TRACE: ToolInvocationTrace,
            TraceType.GENERATION_TRACE: GenerationTrace,
            TraceType.PLANNING_TRACE: PlanningTrace,
            TraceType.EXECUTION_TRACE: ExecutionTrace,
        }.get(self)

    def title(self) -> str:
        return self.value.replace("_TRACE", "").replace("_", " ")


class SourceDetails(BaseModel):
    """Represents the details about the origin of a particular event."""

    key: Optional[str] = None
    name: Optional[str] = None


class Trace(BaseModel):
    """Represents trace that captures the internal steps such as reasoning and actions during an execution."""

    trace_type: TraceType
    key: Optional[str] = None
    parent_key: Optional[str] = None
    time_created: Optional[datetime] = None
    time_finished: Optional[datetime] = None
    source: Optional[SourceDetails] = None

    @property
    def to_dict(self) -> dict:
        return self.model_dump(mode="json", exclude_none=True)


class ToolInvocationTrace(Trace):
    """Represents trace information related to the selection and invocation of a tool."""

    tool_id: str
    tool_name: Optional[str] = None
    invocation_details: Optional[str] = None


class ModelParams(BaseModel):
    """Represents Model Parameters."""

    max_tokens: Optional[int] = None
    temperature: Optional[int] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None


class ModelDetails(BaseModel):
    """Represents Model Details."""

    model_params: Optional[ModelParams] = None
    model_name: Optional[str] = None
    model_version: Optional[str] = None


class UsageDetails(BaseModel):
    """Represents Model Usage Details."""

    input_token_count: Optional[int] = None
    output_token_count: Optional[int] = None
    input_char_count: Optional[int] = None
    output_char_count: Optional[int] = None


class Usage(BaseModel):
    """Represents Model Details and Model Usage."""

    model_details: Optional[ModelDetails] = None
    usage_details: Optional[UsageDetails] = None


class PlanningTrace(Trace):
    """Represents trace information associated with the planning stage."""

    input: Optional[str] = None
    output: Optional[str] = None
    usage: Optional[List[Usage]] = None


class GenerationTrace(Trace):
    """Represents trace information about the response generated from LLM."""

    generation: str
    input: Optional[str] = None
    usage: Optional[List[Usage]] = None


class ExecutionTrace(Trace):
    """Represents trace information related to the execution of a selected tool."""

    input: str
    output: Optional[str] = None


class ErrorTrace(Trace):
    """Represents trace information about the error."""

    error_message: str
    code: Optional[str] = None


class SourceLocationType(str, Enum):
    """Represents the type of location where the source files are stored."""

    OCI_OPEN_SEARCH = "OCI_OPEN_SEARCH"
    OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"
    OCI_DATABASE = "OCI_DATABASE"
    INLINE_DATA = "INLINE_DATA"


class SourceLocation(BaseModel):
    """Represents the location of the data files that the agent will use."""

    source_location_type: SourceLocationType


class OCIOpenSearchSourceLocation(SourceLocation):
    """Represents a data source location of the OCI OpenSearch."""

    id: str
    index_name: str
    url: Optional[str] = None


class InlineDataSourceLocation(SourceLocation):
    """Represents an Inline data source location that contains the data files."""

    id: Optional[str] = None
    data_source: Optional[str] = None
    url: Optional[str] = None


class OCIObjectStorageSourceLocation(SourceLocation):
    """Represents a data source stored in OCI Object Storage."""

    url: Optional[str] = None


class OCIDatabaseSourceLocation(SourceLocation):
    """Represents a data source location of the OCI Database."""

    id: str
    function_name: str
    url: Optional[str] = None


class Citation(BaseModel):
    """Represents a reference to a source used in the agent’s response, including location, metadata, and context."""

    source_text: str
    source_location: Union[
        OCIOpenSearchSourceLocation, OCIObjectStorageSourceLocation, OCIDatabaseSourceLocation, InlineDataSourceLocation
    ]
    title: Optional[str] = None
    doc_id: Optional[str] = None
    page_numbers: Optional[List[int]] = None
    metadata: Optional[Dict[str, Any]] = None


class RetrievalTrace(Trace):
    """Represents trace information about the retrieval process, including input queries and associated citations."""

    retrieval_input: str
    citations: List[Citation]
    usage: Optional[List[Usage]] = None
