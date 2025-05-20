# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
from oci.addons.adk import Agent, AgentClient, tool


@tool
def get_trending_keywords(topic):
    """ Get the trending keywords for a given topic. """
    # Here is a mock implementation
    return json.dumps({"topic": topic, "keywords": ["agent", "stargate", "openai"]})


@tool
def send_email(recipient, subject, body):
    """ Send an email to a recipient. """
    # Here is a mock implementation
    print("Sending email to ", recipient, "with subject", subject, "and body", body)
    return "Sent!"


def main():

    # A shared client for all agents
    client = AgentClient(
        auth_type="security_token",
        profile="DEFAULT",
        region="us-chicago-1"
    )

    # trend analyzer collaborator agent
    trend_analyzer = Agent(
        name="Trend Analyzer",
        instructions="You use the tools provided to analyze the trending keywords of given topics.",
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        client=client,
        tools=[
            get_trending_keywords,
        ]
    )

    # content writer collaborator agent
    content_writer = Agent(
        name="Content Writer",
        instructions="You write a mini blog post (4 sentences) using the trending keywords.",
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        client=client,
    )

    # marketing director supervisor agent
    marketing_director = Agent(
        name="Marketing Director",
        instructions="You ask the trend analyzer for trending keywords and " +
        "You then ask the content writer to write a blog post using the trending keywords. " +
        "You then send email to 'jane.doe@example.com' with the blog post. " +
        "Then summarize the actions you took and reply to the user.",
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        client=client,
        tools=[
            trend_analyzer.as_tool(
                tool_name="analyze_trending_keywords",
                tool_description="Analyze the trending keywords of given topics",
            ),
            content_writer.as_tool(
                tool_name="write_blog_post",
                tool_description="Write a blog post using the trending keywords.",
            ),
            send_email,
        ]
    )

    # Set up the agents once
    trend_analyzer.setup()
    content_writer.setup()
    marketing_director.setup()

    # Use the supervisor agent to process the end user request
    input = "Produce a blog post about current trends in the AI industry."
    response = marketing_director.run(input, max_steps=5)
    response.pretty_print()


if __name__ == "__main__":
    main()
