# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import requests

# OCI Setup
oci_config = oci.config.from_file()

generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(
    oci_config, service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com")

# NewsAPI Setup
# Create an API Key on NewsAPI, https://newsapi.org/.
# Replace 'YOUR_API_KEY' with the actual API key you obtained from NewsAPI
api_key = 'YOUR_API_KEY'


def create_media_dataset(api_key):
    # We will collect the latest technology news.
    news_dataset = str("Here is the latest technology news. ")

    response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={api_key}')

    if response.status_code == 200:
        articles = response.json()['articles']

        for article in articles:
            if article['description']:
                news_dataset = news_dataset + article['description'] + '. '

        print("\n=== Today's Tech News ===\n", news_dataset)
        return news_dataset

    elif response.status_code == 401:
        print("Unable to fetch news data. Make sure your API Key is set within the script.")
        quit(-1)

    else:
        print(f"Unresolved Error: {response.status_code}")
        quit(-1)


def generative_ai_function(oci_config, generative_ai_inference_client, news_dataset):
    # Gen AI API Summary Model will be invoked with News Data.

    summarize_text_response = generative_ai_inference_client.summarize_text(
        summarize_text_details=oci.generative_ai_inference.models.SummarizeTextDetails(
            input=news_dataset,
            serving_mode=oci.generative_ai_inference.models.OnDemandServingMode(model_id="cohere.command"),
            compartment_id=oci_config['tenancy'],
            is_echo=False,
            temperature=1,
            length="MEDIUM",
            format="PARAGRAPH",
            extractiveness="AUTO")).data
    print("\n=== Generative AI Tech News Summary ===\n", summarize_text_response.summary)


news_dataset = create_media_dataset(api_key)
generative_ai_function(oci_config, generative_ai_inference_client, news_dataset)
