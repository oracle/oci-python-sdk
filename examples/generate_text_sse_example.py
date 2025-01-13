# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# generate_text_demo.py
# Supports Python 3
##########################################################################
# Info:
# Get texts from LLM model for given prompts using OCI Generative AI Service.
##########################################################################
# Application Command line(no parameter needed)
# python generate_text_demo.py
##########################################################################
import oci
import json

# Setup basic variables
# Auth Config
# TODO: Please update config profile name and use the compartmentId that has policies grant permissions for using Generative AI Service
compartment_id = "<compartment_ocid>"
CONFIG_PROFILE = "DEFAULT"
config = oci.config.from_file('~/.oci/config', CONFIG_PROFILE)

# Service endpoint
endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"

generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10, 240))

cohere_generate_text_request = oci.generative_ai_inference.models.CohereLlmInferenceRequest()
cohere_generate_text_request.prompt = "Tell me one fact about earth"
cohere_generate_text_request.is_stream = True
cohere_generate_text_request.max_tokens = 20
cohere_generate_text_request.temperature = 0.75
cohere_generate_text_request.top_p = 0.7
cohere_generate_text_request.frequency_penalty = 1.0

generate_text_detail = oci.generative_ai_inference.models.GenerateTextDetails()
generate_text_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id="cohere.command")
# generate_text_detail.serving_mode = oci.generative_ai.models.DedicatedServingMode(endpoint_id="custom-model-endpoint") # for custom model from Dedicated AI Cluster
generate_text_detail.compartment_id = compartment_id
generate_text_detail.inference_request = cohere_generate_text_request

if "<compartment_ocid>" in compartment_id:
    print("ERROR:Please update your compartment id in target python file")
    quit()

generate_text_response = generative_ai_inference_client.generate_text(generate_text_detail)

# Print result
print("**************************Generate Texts Result**************************")
print(vars(generate_text_response))

for event in generate_text_response.data.events():
    print(json.loads(event.data)["text"])
