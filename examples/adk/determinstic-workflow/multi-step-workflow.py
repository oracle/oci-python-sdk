# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.addons.adk import Agent, AgentClient
from custom_functon_tools import ResearcherToolkit, WriterToolkit

"""
This examples shows how you can build "deterministically orchestrated workflows with agentic steps".
"""


# Your (existing) vanilla python code to be integrated into this agentic workflow
def get_user_preferences():
    # Simulate result you fetched from DB
    return {
        "email": "j.jing.y.yang@oracle.com",
        "style": ["casual", "humorous"],
        "topics": ["ai"]
    }


def main():

    client = AgentClient(
        auth_type="security_token",
        profile="BoatOc1",
        region="kix"
    )

    researcher = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4qaos",
        name="Researcher",
        instructions="You are a researcher. You research trending keywords based on the user preferences.",
        tools=[ResearcherToolkit()]
    )

    writer = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4qaqa6",
        name="Writer",
        instructions="You are a writer. You write a blog post based on the trending keywords and the user preferences.",
        tools=[WriterToolkit()]
    )

    researcher.setup()
    writer.setup()

    # Step 1: fetch user preferences (non-agentic step), or any pre-processing
    user_preferences = get_user_preferences()

    # Step 2: research trending keywords (agentic step), using outputs from previous steps as input
    topics = user_preferences['topics']
    researcher_prompt = f"Research trending keywords for the following topics: {topics}"
    last_run_response = researcher.run(researcher_prompt)

    # Step 3: write a blog post (agentic step), using outputs from last two steps as input
    keywords = last_run_response.output
    style = user_preferences['style']
    email = user_preferences['email']
    writer_prompt = f"Write a 5 sentences blog post and email it to {email}. Use style: {style}. Blog post should be based on: {keywords}."
    last_run_response = writer.run(writer_prompt)

    # Step 4: do whatever you want with the last step output, here we just print it
    last_run_response.pretty_print()


if __name__ == "__main__":
    main()
