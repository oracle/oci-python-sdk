# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

################################################################################################################
# A basic example of OCI AI Language service using the OCI Python SDK.
# This script will do the following:
#   * Create an AI services client from an OCI Config file.
#   * Create a text document object for the text analysis to be performed on.
#   * Run the text document on the default OCI Language model provided out of the box.
#   * Following analysis will be performed on the text document object:
#       * Sentiment analysis
#       * Key phrase extraction
#       * Named entity recognition
#       * Text extraction
#   * Prints all the results
#
# This script assumes you have created an OCI config on your local machine to interact with the SDK.
# For more information: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#
# Information on OCI AI Language service: https://www.oracle.com/artificial-intelligence/language/
#
################################################################################################################


import oci

# Please fill out all paramaters
config_path = "~/.oci/config"
# From https://www.oracle.com/cloud/
test_string = "Oracle Cloud Infrastructure is built for enterprises seeking higher performance, lower costs, and easier cloud migration for their applications. Customers choose Oracle Cloud Infrastructure over AWS for several reasons: First, they can consume cloud services in the public cloud or within their own data center with Oracle Dedicated Region Cloud@Customer. Second, they can migrate and run any workload as is on Oracle Cloud, including Oracle databases and applications, VMware, or bare metal servers. Third, customers can easily implement security controls and automation to prevent misconfiguration errors and implement security best practices. Fourth, they have lower risks with Oracle’s end-to-end SLAs covering performance, availability, and manageability of services. Finally, their workloads achieve better performance at a significantly lower cost with Oracle Cloud Infrastructure than AWS. Take a look at what makes Oracle Cloud Infrastructure a better cloud platform than AWS."


def createLanguageClient(config_path):
    """
    Create an OCI language client from a config file.

    This function authenticates an OCI connection from a local file and creates an OCI language client
    where several OCI functions will be called from.

    Parameters:
    config_path (str): Path for OCI config file on local machine.
                       https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
                       for setup instructions.

    Returns:
    AIServiceLanguageClient: OCI AI service object for calling several Language functions

    """

    config = oci.config.from_file(
        config_path, "DEFAULT")
    return oci.ai_language.AIServiceLanguageClient(config)


def createTextDocument(key_, data, language_code_="en"):
    """

    Create a text document for the language model to run on.

    This function creates an object type TextDocument that is used by the Language model.

    Parameters:
    key_(str): Document unique identifier defined by the user.
    data(str): String that the text analysis will be run on.
    language_code_(str): Language code for the document, ISO 639-1 standard.

    Returns:
    TextDocument: The document details for language service call.

    """

    return oci.ai_language.models.TextDocument(
        key=key_,
        text=data,
        language_code=language_code_
    )


def SentimentAnalysis(AI_client, text_document):
    """
    Run sentiment analysis on a text document.

    This function makes an API request to the OCI Language Sentiment Analysis endpoint using credentials previously created.

    Parameters:
    AI_client(AIServiceLanguageClient):  OCI AI service object for calling several Language functions, previously created.
    text_document(TextDocument): Has the text and metadata the sentiment analysis will be run on.

    Returns:
    BatchDetectLanguageSentimentsResult: Upon success, JSON object that includes the sentiment analysis information.

    """

    try:
        # Run sentiment analysis on text_document
        detect_language_sentiments_response = AI_client.batch_detect_language_sentiments(
            batch_detect_language_sentiments_details=oci.ai_language.models.BatchDetectLanguageSentimentsDetails(documents=[text_document])
        )
        return detect_language_sentiments_response.data

    # Print service error for debugging
    except Exception as e:
        print(e)
    return


def KeyPhraseExtraction(AI_client, text_document):
    """
    Run key phrase extraction on a text document.

    This function makes an API request to the OCI Language Sentiment Analysis endpoint using credentials previously created.

    Parameters:
    AI_client(AIServiceLanguageClient):  OCI AI service object for calling several Language functions, previously created.
    text_document(TextDocument): Has the text and metadata the sentiment analysis will be run on.

    Returns:
    BatchDetectLanguageKeyPhrasesResult: Upon success, JSON object that includes the key phrase information.

    """
    try:
        keyphrase_extraction = AI_client.batch_detect_language_key_phrases(
            batch_detect_language_key_phrases_details=oci.ai_language.models.BatchDetectLanguageKeyPhrasesDetails(documents=[text_document])
        )
        return keyphrase_extraction.data
    except Exception as e:
        print(e)


def NamedEntityExtraction(AI_client, text_document):
    """
    Run named entity extraction on a text document.

    This function makes an API request to the OCI Language entity extraction endpoint using credentials previously created.

    Parameters:
    AI_client(AIServiceLanguageClient):  OCI AI service object for calling several Language functions, previously created.
    text_document(TextDocument): Has the text the sentiment analysis will be run on.

    Returns:
    BatchDetectNamedEntityExtractionResult: Upon successful API call, this function returns a JSON object that includes named entity extraction information.

    """
    try:
        language_entities = AI_client.batch_detect_language_entities(
            batch_detect_language_entities_details=oci.ai_language.models.BatchDetectLanguageEntitiesDetails(documents=[text_document])
        )

        return language_entities.data

    # Print service error for debugging
    except Exception as e:
        print(e)
    return


def TextClassification(AI_client, text_document):
    """
    Run text classification on a text document.

    This function makes an API request to the OCI Language Text Classification endpoint using credentials previously created.

    Parameters:
    AI_client(AIServiceLanguageClient):  OCI AI service object for calling several Language functions, previously created.
    text_document(TextDocument): Has the text the sentiment analysis will be run on.

    Returns:
    BatchDetectLanguageTextClassificationResult: JSON object that includes the text classification information.

    """
    try:
        # Run text classification on text_document
        text_classification = AI_client.batch_detect_language_text_classification(
            batch_detect_language_text_classification_details=oci.ai_language.models.BatchDetectLanguageTextClassificationDetails(
                documents=[text_document]
            )
        )
        # return the data
        return text_classification.data

    # Print any API errors
    except Exception as e:
        print(e)
    return


def printWelcomeMessage():
    print("Welcome to OCI AI Language example.")


def printDivider():
    # Helper function to print a divider between analysis'
    for i in range(50):
        print("-", end=""),
    print("\n")


def printAllResponses(sentiment_response, key_phrase_response, named_entity_response, text_classification_response):
    """
    Prints all OCI AI Language responses.

    Parameters:
    sentiment_response(BatchDetectLanguageSentimentsResult): JSON object that holds the result of API call to OCI Language endpoint for sentiment response.
    key_phrase_response(): JSON object that holds the result of API call to OCI Language endpoint for key phrase response.
    named_entity_response(): JSON object that holds the result of API call to OCI Language endpoint for named entity response.
    text_classification_response(): JSON object that holds the result of API call to OCI Language endpoint for text classification response.

    """
    print("Sentiment Analysis on text:")
    for i in range(0, len(sentiment_response.documents)):
        for j in range(0, len(sentiment_response.documents[i].aspects)):
            print("\tText: ", sentiment_response.documents[i].aspects[j].text)
            print("\tOverall sentiment: ", sentiment_response.documents[i].aspects[j].sentiment)
            print("\tLength: ", sentiment_response.documents[i].aspects[j].length)
            print("\tOffset: ", sentiment_response.documents[i].aspects[j].offset)

    printDivider()
    print("Key phrase extraction on text:")

    for i in range(len(key_phrase_response.documents)):
        for j in range(len(key_phrase_response.documents[i].key_phrases)):
            print("\tphrase: ", key_phrase_response.documents[i].key_phrases[j].text)
            print("\tscore: ", key_phrase_response.documents[i].key_phrases[j].score)

    printDivider()
    print("Named entity extraction on text:")

    for i in range(len(named_entity_response.documents)):
        for j in range(len(named_entity_response.documents[i].entities)):
            print("\tText: ", named_entity_response.documents[i].entities[j].text)
            print("\tType: ", named_entity_response.documents[i].entities[j].type)
            print("\tSub_Type: ", named_entity_response.documents[i].entities[j].sub_type)
            print("\tLength: ", named_entity_response.documents[i].entities[j].length)
            print("\tOffset: ", named_entity_response.documents[i].entities[j].offset)

    printDivider()
    print("Text classification analysis on text:")
    for i in range(len(text_classification_response.documents)):
        for j in range(len(text_classification_response.documents[i].text_classification)):
            print("\tLabel: ", text_classification_response.documents[i].text_classification[j].label)
            print("\tScore: ", text_classification_response.documents[i].text_classification[j].score)


def runModel(data, config_path="~/.oci/config", text_model_key="Example", language_code="en"):
    """
    Runs all functions needed for this example.

    Creates language client, 4 text analysis reponses and prints all the necessary output.

    Parameters:
    data(str): The text that will be analyzed.
    config_path(str): Path to OCI config file. Default value: ~/.oci/config
    text_model_key(str): Added to the metadata of the text document, required. Default value: Example
    language_code(str): Language code for a text document, required. Default value: en
    Returns:
    TextDocument: The document details for language service call.

    """

    # Create language client and text document to be analyzed, up to 100 can be analyzed at the same time.
    language_client = createLanguageClient(config_path)
    text_document = createTextDocument(key_=text_model_key, language_code_="en", data=data)

    # Grab all responses by the AI client
    sentiment_response = SentimentAnalysis(language_client, text_document)
    key_phrase_response = KeyPhraseExtraction(language_client, text_document)
    named_entity_response = NamedEntityExtraction(language_client, text_document)
    text_classification_response = TextClassification(language_client, text_document)

    printWelcomeMessage()

    printAllResponses(sentiment_response, key_phrase_response, named_entity_response, text_classification_response)


# Run example model
runModel(test_string, config_path, text_model_key="example", language_code="en")
