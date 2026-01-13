# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
A prebuilt SQL Tool
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from oci.addons.adk.run.types import InputLocation


class SqlDialect(str, Enum):
    """Represents SQL Dialect"""
    ORACLE_SQL = "ORACLE_SQL"
    SQLITE = "SQLITE"


class ModelSize(str, Enum):
    """Represents Model Size"""
    SMALL = "SMALL"
    LARGE = "LARGE"


class AgenticSqlTool(BaseModel):
    """A server-side tool that converts natural language queries into SQL"""

    name: str = Field(
        default="SQL Tool",
        description="The name of the tool, used for identification and invocation."
    )

    description: str = Field(
        default="",
        description="A human-readable summary of the tool's purpose and usage."
    )

    database_schema: InputLocation = Field(
        ...,
        description=(
            "The database schema definition, either provided inline or referenced from OCI Object Storage."
        )
    )

    db_tool_connection_id: Optional[str] = Field(
        default=None,
        description="OCI Database Tools connection OCID used for executing queries against the target database."
    )

    dialect: SqlDialect = Field(
        default=SqlDialect.ORACLE_SQL,
        description="The SQL dialect used for query generation, ORACLE_SQL or SQLITE."
    )

    model_size: ModelSize = Field(
        default=ModelSize.SMALL,
        description=(
            "Specifies the model used for SQL generation. "
            "'SMALL' provides faster response times, while 'LARGE' improves output quality."
        )
    )

    enable_sql_execution: bool = Field(
        default=False,
        description="If True, enables SQL query execution using the provided database connection."
    )

    enable_self_correction: bool = Field(
        default=False,
        description="If True, allows the tool to automatically correct SQL errors using additional attempts."
    )

    icl_examples: Optional[InputLocation] = Field(
        default=None,
        description=(
            "In-context learning examples for enhancing SQL query generation. "
        )
    )

    table_and_column_description: Optional[InputLocation] = Field(
        default=None,
        description=(
            "Detailed metadata describing table and column semantics. "
            "This helps improve the quality and accuracy of generated SQL queries."
        )
    )

    custom_instructions: Optional[str] = Field(
        default=None,
        description="User-provided instructions to customize SQL generation behavior."
    )

    @model_validator(mode="after")
    def validate_db_tool_connection_id_required_when_execution_or_correction(self) -> "AgenticSqlTool":
        if (self.enable_sql_execution or self.enable_self_correction) and not self.db_tool_connection_id:
            raise ValueError("`db_tool_connection_id` must be provided when SQL execution or self-correction is enabled.")
        return self
