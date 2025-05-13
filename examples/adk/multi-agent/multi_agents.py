# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
from oci.addons.adk import Agent, AgentClient, tool


@tool
def get_trending_keywords(topic):
    """ Get the trending keywords for a given topic. """
    return json.dumps({"topic": topic, "keywords": ["agent", "stargate", "openai"]})


@tool
def send_email(recipient, subject, body):
    """ Send an email to a recipient. """
    print("Sending email to ", recipient, "with subject", subject, "and body", body)
    return "Sent!"


def main():
    client = AgentClient(
        auth_type="security_token",
        profile="BoatOc1",
        region="ap-osaka-1"
    )

    # trend analyzer collaborator agent (use tools to get trending keywords)
    trend_analyzer = Agent(
        name="Trend Analyzer",
        instructions="You use the tools provided to analyze the trend of .",
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4q",
        client=client,
        tools=[
            get_trending_keywords,
        ]
    )

    # content writer collaborator agent (use LLM to write content)
    content_writer = Agent(
        name="Content Writer",
        instructions="You write a mini blog post (4 sentences) about the trending topics.",
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4qaos",
        client=client,
    )

    # marketing director supervisor agent (use the other agents to complete tasks)
    marketing_director = Agent(
        name="Marketing Director",
        instructions="You ask the trend analyzer for trending topics and " +
        " You then ask the content writer to write a blog post about them. " +
        " You then send email to 'j.jing.y.yang@oracle.com' with the blog post. " +
        " Then summarize the actions you took and reply to the user.",
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.ap-osaka-1.amaaaaaacqy6p4qaq",
        client=client,
        tools=[
            trend_analyzer,
            content_writer,
            send_email,
        ]
    )

    # Set up the agent once (this configures the instructions and tools in the remote agent resource)
    trend_analyzer.setup()
    content_writer.setup()
    marketing_director.setup()

    # Use the agent to process the end user request (it automatically handles the function calling)
    input = "Produce a blog post about current trends in the AI industry."
    response = marketing_director.run(input, max_steps=5)
    response.pretty_print()


if __name__ == "__main__":
    main()
