# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
This example shows how an agent with RAG and SQL Tool work.
"""

from oci.addons import AgentClient, Agent
from oci.addons.adk.run.types import ObjectStorageInputLocation
from oci.addons.adk.tool.prebuilt import AgenticRagTool
from oci.addons.adk.tool.prebuilt.agentic_sql_tool import AgenticSqlTool, ModelSize, SqlDialect


def main():
    # Use a custom agent client for custom profile and endpoints settings
    client = AgentClient(
        auth_type="security_token",
        profile="DEFAULT",
        region="us-chicago-1",
    )

    # Instantiate a SQL Tool
    sql_tool = AgenticSqlTool(
        name="HR Manager SQL Tool",
        description="A NL2SQL tool that translates natural language queries into SQL to retrieve insights from employee, job, and recruitment data.",
        database_schema=ObjectStorageInputLocation(namespace_name="sql-namespace", bucket_name="sql-bucket",
                                                   prefox="_sql.schema.sql"),
        model_size=ModelSize.LARGE,
        dialect=SqlDialect.ORACLE_SQL,
        db_tool_connection_id="ocid1.databasetoolsconnection.oc1.us-chicago-1.amaaaaaax7756...",
        enable_sql_execution=True,
        enable_self_correction=True
    )

    # Instantiate a RAG Tool
    rag_tool = AgenticRagTool(
        name="HR Manager RAG Tool",
        description="A RAG tool to retrieve HR content such as HR policies, job policies, and job descriptions.",
        knowledge_base_ids=[
            "ocid1.genaiagentknowledgebasedev.oc1.us-chicago-1.amaaaaaax7756ra...",
        ]
    )

    # Instantiate the local agent object, with SQLTool and AgenticRagTool
    agent = Agent(
        name="HR Assistant Multi-Tool Agent",
        description="An integrated agent that uses an SQL tool to query structured HR data (e.g., jobs, applications, employees) and a RAG tool to retrieve HR content (e.g., job descriptions, policies).",
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.amaaaaaax7756raa7cyp...",
        tools=[sql_tool, rag_tool]
    )

    # Set up the agent once (which pushes local instructions and tools to the remote agent resource)
    agent.setup()

    # Run the agent with a user message
    input = ("First, use the RAG tool to list all job titles from the system. "
             "Then, use the SQL tool to retrieve corresponding job descriptions for each title.")
    response = agent.run(input)
    response.pretty_print()


if __name__ == "__main__":
    main()
