# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import AgenticRagTool
from custom_functon_tools import BillingToolkit


def main():

    client = AgentClient(
        auth_type="api_key",
        profile="CUSTOM",
        region="us-chicago-1"
    )

    product_specialist = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.amaaaaaabcd",
        name="Product Specialist",
        instructions="You are a product specialist. You answer user question using the tools provided.",
        tools=[AgenticRagTool(knowledge_base_ids=["ocid1.genaiagentknowledgebase.oc1.us-chicago-1.amaaaaaefgh"])]
    )

    billing_specialist = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.amaaaaaijkl",
        name="Billing Specialist",
        instructions="You are a billing specialist. You answer user question using the tools provided.",
        tools=[BillingToolkit()]
    )

    support_supervisor = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.amaaaaamnpq",
        name="Support Supervisor",
        instructions="You are a support supervisor. You answer user question using the tools provided.",
        tools=[product_specialist.as_tool(), billing_specialist.as_tool()]
    )

    product_specialist.setup()
    billing_specialist.setup()
    support_supervisor.setup()

    context = "Context: Customer ID: cust_123. User question: "

    input = "What is OCI Compute?"
    last_run_response = product_specialist.run(input)
    last_run_response.pretty_print()

    input = context + "Refund my most recent order"
    last_run_response = billing_specialist.run(input)
    last_run_response.pretty_print()

    input = context + "Refund my most recent order"
    last_run_response = support_supervisor.run(input)
    last_run_response.pretty_print()


if __name__ == "__main__":
    main()
