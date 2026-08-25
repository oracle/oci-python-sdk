# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""Run the same three calls with both sync and async OCI clients."""

import asyncio
import os
import time

import oci
from oci.generative_ai_inference import AsyncGenerativeAiInferenceClient
from oci.generative_ai_inference.models import (
    ChatDetails,
    GenericChatRequest,
    OnDemandServingMode,
    TextContent,
    UserMessage,
)


PROMPTS = (
    "What is 2 + 2? Answer with only the number.",
    "What is the capital of France? Answer with only the city.",
    "Name the largest planet in our solar system. Answer with only its name.",
)


def load_settings():
    config_file = os.environ.get("OCI_CONFIG_FILE", oci.config.DEFAULT_LOCATION)
    profile = os.environ.get("OCI_CONFIG_PROFILE", oci.config.DEFAULT_PROFILE)
    config = oci.config.from_file(config_file, profile)

    compartment_id = os.environ.get("OCI_COMPARTMENT_ID")
    if not compartment_id:
        raise ValueError("Set OCI_COMPARTMENT_ID to the compartment OCID to use.")

    model_id = os.environ.get(
        "OCI_GENAI_MODEL_ID", "meta.llama-3.3-70b-instruct"
    )
    endpoint = os.environ.get(
        "OCI_GENAI_ENDPOINT",
        "https://inference.generativeai.{}.oci.oraclecloud.com".format(
            config["region"]
        ),
    )
    return config, compartment_id, model_id, endpoint


def make_chat_details(prompt, compartment_id, model_id):
    return ChatDetails(
        compartment_id=compartment_id,
        serving_mode=OnDemandServingMode(model_id=model_id),
        chat_request=GenericChatRequest(
            messages=[UserMessage(content=[TextContent(text=prompt)])],
            max_tokens=40,
            temperature=0.1,
            is_stream=False,
        ),
    )


def print_responses(label, responses):
    print("\n{} responses:".format(label))
    for number, response in enumerate(responses, 1):
        text = response.data.chat_response.choices[0].message.content[0].text
        print("Call {} (HTTP {}): {}".format(number, response.status, text))


def run_sync(config, compartment_id, model_id, endpoint):
    client = oci.generative_ai_inference.GenerativeAiInferenceClient(
        config=config, service_endpoint=endpoint
    )
    started = time.perf_counter()
    responses = [
        client.chat(make_chat_details(prompt, compartment_id, model_id))
        for prompt in PROMPTS
    ]
    return responses, time.perf_counter() - started


async def run_async(config, compartment_id, model_id, endpoint):
    started = time.perf_counter()
    async with AsyncGenerativeAiInferenceClient(
        config=config, service_endpoint=endpoint
    ) as client:
        responses = await asyncio.gather(
            *(
                client.chat(make_chat_details(prompt, compartment_id, model_id))
                for prompt in PROMPTS
            )
        )
    return responses, time.perf_counter() - started


async def main():
    config, compartment_id, model_id, endpoint = load_settings()

    sync_responses, sync_elapsed = run_sync(
        config, compartment_id, model_id, endpoint
    )
    async_responses, async_elapsed = await run_async(
        config, compartment_id, model_id, endpoint
    )

    print_responses("Sync", sync_responses)
    print_responses("Async", async_responses)
    print("\nSync elapsed time:  {:.2f} seconds".format(sync_elapsed))
    print("Async elapsed time: {:.2f} seconds".format(async_elapsed))


if __name__ == "__main__":
    event_loop = asyncio.new_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
