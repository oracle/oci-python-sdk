# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
This example shows an agent with a single SQL tool.
"""

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.run.types import InlineInputLocation, ObjectStorageInputLocation
from oci.addons.adk.tool.prebuilt.agentic_sql_tool import AgenticSqlTool, SqlDialect, ModelSize


INLINE_DATABASE_SCHEMA = "CREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(100)); \
CREATE TABLE Jobs (job_id INT PRIMARY KEY, job_title VARCHAR(100), min_salary DECIMAL(10,2), max_salary DECIMAL(10,2), department_id INT, FOREIGN KEY (department_id) REFERENCES Departments(department_id)); \
CREATE TABLE Employees (employee_id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), job_id INT, hire_date DATE, salary DECIMAL(10,2), manager_id INT, FOREIGN KEY (job_id) REFERENCES Jobs(job_id), FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)); \
CREATE TABLE Job_Postings (posting_id INT PRIMARY KEY, job_id INT, posted_date DATE, closing_date DATE, status VARCHAR(20), FOREIGN KEY (job_id) REFERENCES Jobs(job_id)); \
CREATE TABLE Applications (application_id INT PRIMARY KEY, posting_id INT, applicant_name VARCHAR(100), application_date DATE, status VARCHAR(20), FOREIGN KEY (posting_id) REFERENCES Job_Postings(posting_id)); \
CREATE TABLE Hiring_Processes (process_id INT PRIMARY KEY, application_id INT, interview_date DATE, decision VARCHAR(20), FOREIGN KEY (application_id) REFERENCES Applications(application_id));"


def main():
    # Use a custom agent client for custom profile and endpoints settings
    client = AgentClient(
        auth_type="security_token",
        profile="DEFAULT",
        region="us-chicago-1"
    )

    # Instantiate a SQL Tool
    sql_tool_with_inline_schema = AgenticSqlTool(
        name="HR Manager SQL Tool - Inline Schema",
        description="A NL2SQL tool that translates natural language queries into SQL to retrieve insights from employee, job, and recruitment data.",
        database_schema=InlineInputLocation(content=INLINE_DATABASE_SCHEMA),
        model_size=ModelSize.LARGE,
        dialect=SqlDialect.ORACLE_SQL,
        db_tool_connection_id="ocid1.databasetoolsconnection.oc1.us-chicago-1.amaaaaaax7756raa7...",
        enable_sql_execution=True,
        enable_self_correction=True,
        icl_examples=ObjectStorageInputLocation(namespace_name="namespace", bucket_name="bucket", prefix="_sql.icl_examples.txt"),
        table_and_column_description=ObjectStorageInputLocation(namespace_name="namespace", bucket_name="bucket", prefix="_sql.table_col_desc.pdf"),
        custom_instructions="instruction"
    )

    sql_tool_with_file_schema = AgenticSqlTool( # noqa
        name="HR Manager SQL Tool - File Based schema",
        description="A NL2SQL tool that translates natural language queries into SQL to retrieve insights from employee, job, and recruitment data.",
        database_schema=InlineInputLocation(content=open("_sql.database_schema.sql").read()),
        model_size=ModelSize.LARGE,
        dialect=SqlDialect.ORACLE_SQL,
        db_tool_connection_id="ocid1.databasetoolsconnection.oc1.us-chicago-1.amaaaaa...",
        enable_sql_execution=True,
        enable_self_correction=True
    )

    sql_tool_with_object_storage_schema = AgenticSqlTool( # noqa
        name="HR Manager SQL Tool - Object Storage schema",
        description="A NL2SQL tool that translates natural language queries into SQL to retrieve insights from employee, job, and recruitment data.",
        database_schema=ObjectStorageInputLocation(namespace_name="namespace", bucket_name="bucket", prefix="_sql.schema.sql"),
        model_size=ModelSize.LARGE,
        dialect=SqlDialect.ORACLE_SQL,
        db_tool_connection_id="ocid1.databasetoolsconnection.oc1.us-chicago-1.amaaaaaax...",
        enable_sql_execution=True,
        enable_self_correction=True
    )

    # Instantiate the local agent object, with SQL Tool
    agent = Agent(
        name="HR Assistant Agent",
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.amaaaaaax7756raard4...",
        tools=[sql_tool_with_inline_schema]
    )

    # Set up the agent once (which pushes local instructions and tools to the remote agent resource)
    agent.setup()

    # Run the agent with a user message
    input = "List all employees with their job titles."
    response = agent.run(input)
    response.pretty_print()

    # Print Response Traces
    response.pretty_print_traces()


if __name__ == "__main__":
    main()
