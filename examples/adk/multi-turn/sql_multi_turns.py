# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
This example shows how multi-turn works with a SQL Tool Agent.
"""

from oci.addons import AgentClient, Agent
from oci.addons.adk.run.types import ObjectStorageInputLocation
from oci.addons.adk.tool.prebuilt.agentic_sql_tool import AgenticSqlTool, SqlDialect, ModelSize


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
        database_schema=ObjectStorageInputLocation(namespace_name="sql-namespace", bucket_name="sql-bucket", prefox="_sql.schema.sql"),
        model_size=ModelSize.LARGE,
        dialect=SqlDialect.ORACLE_SQL,
        db_tool_connection_id="ocid1.databasetoolsconnection.oc1.us-chicago-1.amaaaaaax7756ra...",
        enable_sql_execution=True,
        enable_self_correction=True
    )

    # Instantiate the local agent object, with a SQL Tool
    agent = Agent(
        name="HR Assistant Agent",
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.amaaaaaax7...",
        tools=[sql_tool]
    )

    # Set up the agent once (which pushes local instructions and tools to the remote agent resource)
    agent.setup()

    # Run the agent to list all employees
    input = "List all employees with their job titles."
    response = agent.run(input)
    response.pretty_print()

    # second turn, add session_id to maintain context
    input = "Can you show me only the top 5?"
    response = agent.run(input, session_id=response.session_id)
    response.pretty_print()


if __name__ == "__main__":
    main()
