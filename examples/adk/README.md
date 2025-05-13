# OCI Agent Development Kit (ADK)

OCI Agent Development Kit (ADK) is a client-side library that simplifies building agents on OCI Generative AI Agent Service, offering a developer experience (DX) comparable to other leading agent frameworks.

Alternatively, you can also use the `GenerativeAiAgentClient` and `GenerativeAiAgentRuntimeClient` to directly interact with OCI Agent Service, but the ADK addon within the OCI SDK provides a much simpler way to build agents, especially when implementing custom function tools and agent orchestration.

OCI Generative AI Agent Service official doc: 

https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/home.htm

## Getting Started

### Prerequisites

- Python 3.10+

### Installation
```bash
pip install --upgrade "oci[adk]>=2.151.1"

```

### Authentication

The ADK provides a `AgentClient` class to handle authentication and management of agent resources.
Four types of authentication are supported:
- `api_key`: API key authentication, Default authentication method
- `instance_principal`: Instance principal authentication, recommended for OCI compute instances
- `security_token`: Security token authentication, internal auth method for OCI developers
- `resource_principal`: Resource principals authentication, recommended for OCI resources

Most of the time, `api_key` is the best choice for authentication. Here is a doc on how to setup 
API key and OCI config: 
https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm

For more details, please refer to OCI official authentication doc: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm

Sample AgentClient initiation with API key and Default profile. 
The region is also required to automatically select the service endpoint.
```python
from oci.addons.adk import AgentClient

client = AgentClient(
    auth_type="api_key",
    profile="DEFAULT",
    region="us-chicago-1",  # airport code is also valid, i.e. "ORD"
)
```

### Example
```python
from typing import Dict
from oci.addons.adk import Agent, AgentClient, tool

"""
This example shows an agent with a single function tool.
"""

@tool
def get_weather(location: str) -> Dict[str, str]:
    """Get the weather for a given location"""
    return {"location": location, "temperature": 72, "unit": "F"}


def main():

    # Use a custom agent client for custom profile settings
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="us-chicago-1",
    )

    # Instantiate the local agent object, with a single function tool (plain Python function)
    agent = Agent(
        client=client,
        agent_endpoint_id="YOUR_AGENT_ENDPOINT_ID",
        instructions="You are a helpful assistant that can perform weather queries.",
        tools=[get_weather]
    )

    # Set up the agent once (which configures the instructions and tools in the remote agent resource)
    agent.setup()

    # Run the agent with an input
    input = "Is it cold in Seattle?"
    response = agent.run(input)

    # Should print like "It's not cold in Seattle. The current temperature is 72 degrees Fahrenheit. "
    response.pretty_print()

if __name__ == "__main__":
    main()
```

## Examples Directory Overview

| Example | Description |
|---------|-------------|
| `single-agent-single-tool` | Minimal agent with single function tool |
| `single-agent-multiple-tools` | Minimal agent with multiple function tools |
| `multi-turn` | Minimal agent with multiple user turns |
| `multi-agent` | Collaborative agents with workflow orchestration |
| `deterministic-workflow` | Predictable execution patterns for business processes |
| `lifecycle-hook` | Custom handlers for agent state transitions |
