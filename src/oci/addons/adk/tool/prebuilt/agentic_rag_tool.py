# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
A prebuilt toolkit for performing RAG
"""

from typing import List

from pydantic import BaseModel, Field


class AgenticRagTool(BaseModel):
    """A server-side tool that uses an agentic RAG pipeline to answer a question.
    This tool is hosted in OCI Agent Platform, behind an provisioned agent endpoint.

    This tool performs an agentic RAG that runs its own smart agentic loop workflow,
    rather than a statically configured RAG, for best quality results.
    """

    name: str = Field(
        "RAG tool with Knowledge Bases",
        description="The name of the tool, used for identification and invocation",
    )

    description: str = Field(
        """Use this tool to answer questions that require searching,
        retrieving, and synthesizing information from knowledge bases.
        This tool accesses specified knowledge bases to find relevant information
        and generates comprehensive, accurate responses based on the retrieved content.
        Ideal for questions about documents, policies, technical information,
        or any data stored in the connected knowledge bases.""",
        description="Human-readable description of what the tool does and how to use it",  # noqa: E501
    )

    knowledge_base_ids: List[str] = Field(
        description="A list of knowledge base IDs this RAG tool uses"
    )

    # Equality comparison
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AgenticRagTool):
            return NotImplemented
        return (
            self.name == other.name and
            self.description == other.description and
            sorted(self.knowledge_base_ids) == sorted(other.knowledge_base_ids)
        )
