# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .base_chat_request import BaseChatRequest
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CohereChatRequest(BaseChatRequest):
    """
    Details for the chat request for Cohere models.
    """

    #: A constant which can be used with the prompt_truncation property of a CohereChatRequest.
    #: This constant has a value of "OFF"
    PROMPT_TRUNCATION_OFF = "OFF"

    #: A constant which can be used with the prompt_truncation property of a CohereChatRequest.
    #: This constant has a value of "AUTO_PRESERVE_ORDER"
    PROMPT_TRUNCATION_AUTO_PRESERVE_ORDER = "AUTO_PRESERVE_ORDER"

    #: A constant which can be used with the citation_quality property of a CohereChatRequest.
    #: This constant has a value of "ACCURATE"
    CITATION_QUALITY_ACCURATE = "ACCURATE"

    #: A constant which can be used with the citation_quality property of a CohereChatRequest.
    #: This constant has a value of "FAST"
    CITATION_QUALITY_FAST = "FAST"

    #: A constant which can be used with the safety_mode property of a CohereChatRequest.
    #: This constant has a value of "CONTEXTUAL"
    SAFETY_MODE_CONTEXTUAL = "CONTEXTUAL"

    #: A constant which can be used with the safety_mode property of a CohereChatRequest.
    #: This constant has a value of "STRICT"
    SAFETY_MODE_STRICT = "STRICT"

    #: A constant which can be used with the safety_mode property of a CohereChatRequest.
    #: This constant has a value of "OFF"
    SAFETY_MODE_OFF = "OFF"

    def __init__(self, **kwargs):
        """
        Initializes a new CohereChatRequest object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_inference.models.CohereChatRequest.api_format` attribute
        of this class is ``COHERE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param api_format:
            The value to assign to the api_format property of this CohereChatRequest.
            Allowed values for this property are: "COHERE", "GENERIC"
        :type api_format: str

        :param message:
            The value to assign to the message property of this CohereChatRequest.
        :type message: str

        :param chat_history:
            The value to assign to the chat_history property of this CohereChatRequest.
        :type chat_history: list[oci.generative_ai_inference.models.CohereMessage]

        :param documents:
            The value to assign to the documents property of this CohereChatRequest.
        :type documents: list[object]

        :param response_format:
            The value to assign to the response_format property of this CohereChatRequest.
        :type response_format: oci.generative_ai_inference.models.CohereResponseFormat

        :param is_search_queries_only:
            The value to assign to the is_search_queries_only property of this CohereChatRequest.
        :type is_search_queries_only: bool

        :param preamble_override:
            The value to assign to the preamble_override property of this CohereChatRequest.
        :type preamble_override: str

        :param is_stream:
            The value to assign to the is_stream property of this CohereChatRequest.
        :type is_stream: bool

        :param stream_options:
            The value to assign to the stream_options property of this CohereChatRequest.
        :type stream_options: oci.generative_ai_inference.models.StreamOptions

        :param max_tokens:
            The value to assign to the max_tokens property of this CohereChatRequest.
        :type max_tokens: int

        :param max_input_tokens:
            The value to assign to the max_input_tokens property of this CohereChatRequest.
        :type max_input_tokens: int

        :param temperature:
            The value to assign to the temperature property of this CohereChatRequest.
        :type temperature: float

        :param top_k:
            The value to assign to the top_k property of this CohereChatRequest.
        :type top_k: int

        :param top_p:
            The value to assign to the top_p property of this CohereChatRequest.
        :type top_p: float

        :param prompt_truncation:
            The value to assign to the prompt_truncation property of this CohereChatRequest.
            Allowed values for this property are: "OFF", "AUTO_PRESERVE_ORDER"
        :type prompt_truncation: str

        :param frequency_penalty:
            The value to assign to the frequency_penalty property of this CohereChatRequest.
        :type frequency_penalty: float

        :param presence_penalty:
            The value to assign to the presence_penalty property of this CohereChatRequest.
        :type presence_penalty: float

        :param seed:
            The value to assign to the seed property of this CohereChatRequest.
        :type seed: int

        :param is_echo:
            The value to assign to the is_echo property of this CohereChatRequest.
        :type is_echo: bool

        :param tools:
            The value to assign to the tools property of this CohereChatRequest.
        :type tools: list[oci.generative_ai_inference.models.CohereTool]

        :param tool_results:
            The value to assign to the tool_results property of this CohereChatRequest.
        :type tool_results: list[oci.generative_ai_inference.models.CohereToolResult]

        :param is_force_single_step:
            The value to assign to the is_force_single_step property of this CohereChatRequest.
        :type is_force_single_step: bool

        :param stop_sequences:
            The value to assign to the stop_sequences property of this CohereChatRequest.
        :type stop_sequences: list[str]

        :param is_raw_prompting:
            The value to assign to the is_raw_prompting property of this CohereChatRequest.
        :type is_raw_prompting: bool

        :param citation_quality:
            The value to assign to the citation_quality property of this CohereChatRequest.
            Allowed values for this property are: "ACCURATE", "FAST"
        :type citation_quality: str

        :param safety_mode:
            The value to assign to the safety_mode property of this CohereChatRequest.
            Allowed values for this property are: "CONTEXTUAL", "STRICT", "OFF"
        :type safety_mode: str

        """
        self.swagger_types = {
            'api_format': 'str',
            'message': 'str',
            'chat_history': 'list[CohereMessage]',
            'documents': 'list[object]',
            'response_format': 'CohereResponseFormat',
            'is_search_queries_only': 'bool',
            'preamble_override': 'str',
            'is_stream': 'bool',
            'stream_options': 'StreamOptions',
            'max_tokens': 'int',
            'max_input_tokens': 'int',
            'temperature': 'float',
            'top_k': 'int',
            'top_p': 'float',
            'prompt_truncation': 'str',
            'frequency_penalty': 'float',
            'presence_penalty': 'float',
            'seed': 'int',
            'is_echo': 'bool',
            'tools': 'list[CohereTool]',
            'tool_results': 'list[CohereToolResult]',
            'is_force_single_step': 'bool',
            'stop_sequences': 'list[str]',
            'is_raw_prompting': 'bool',
            'citation_quality': 'str',
            'safety_mode': 'str'
        }
        self.attribute_map = {
            'api_format': 'apiFormat',
            'message': 'message',
            'chat_history': 'chatHistory',
            'documents': 'documents',
            'response_format': 'responseFormat',
            'is_search_queries_only': 'isSearchQueriesOnly',
            'preamble_override': 'preambleOverride',
            'is_stream': 'isStream',
            'stream_options': 'streamOptions',
            'max_tokens': 'maxTokens',
            'max_input_tokens': 'maxInputTokens',
            'temperature': 'temperature',
            'top_k': 'topK',
            'top_p': 'topP',
            'prompt_truncation': 'promptTruncation',
            'frequency_penalty': 'frequencyPenalty',
            'presence_penalty': 'presencePenalty',
            'seed': 'seed',
            'is_echo': 'isEcho',
            'tools': 'tools',
            'tool_results': 'toolResults',
            'is_force_single_step': 'isForceSingleStep',
            'stop_sequences': 'stopSequences',
            'is_raw_prompting': 'isRawPrompting',
            'citation_quality': 'citationQuality',
            'safety_mode': 'safetyMode'
        }
        self._api_format = None
        self._message = None
        self._chat_history = None
        self._documents = None
        self._response_format = None
        self._is_search_queries_only = None
        self._preamble_override = None
        self._is_stream = None
        self._stream_options = None
        self._max_tokens = None
        self._max_input_tokens = None
        self._temperature = None
        self._top_k = None
        self._top_p = None
        self._prompt_truncation = None
        self._frequency_penalty = None
        self._presence_penalty = None
        self._seed = None
        self._is_echo = None
        self._tools = None
        self._tool_results = None
        self._is_force_single_step = None
        self._stop_sequences = None
        self._is_raw_prompting = None
        self._citation_quality = None
        self._safety_mode = None
        self._api_format = 'COHERE'

    @property
    def message(self):
        """
        **[Required]** Gets the message of this CohereChatRequest.
        The text that the user inputs for the model to respond to.


        :return: The message of this CohereChatRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CohereChatRequest.
        The text that the user inputs for the model to respond to.


        :param message: The message of this CohereChatRequest.
        :type: str
        """
        self._message = message

    @property
    def chat_history(self):
        """
        Gets the chat_history of this CohereChatRequest.
        The list of previous messages between the user and the model. The chat history gives the model context for responding to the user's inputs.


        :return: The chat_history of this CohereChatRequest.
        :rtype: list[oci.generative_ai_inference.models.CohereMessage]
        """
        return self._chat_history

    @chat_history.setter
    def chat_history(self, chat_history):
        """
        Sets the chat_history of this CohereChatRequest.
        The list of previous messages between the user and the model. The chat history gives the model context for responding to the user's inputs.


        :param chat_history: The chat_history of this CohereChatRequest.
        :type: list[oci.generative_ai_inference.models.CohereMessage]
        """
        self._chat_history = chat_history

    @property
    def documents(self):
        """
        Gets the documents of this CohereChatRequest.
        A list of relevant documents that the model can refer to for generating grounded responses to the user's requests.
        Some example keys that you can add to the dictionary are \"text\", \"author\", and \"date\". Keep the total word count of the strings in the dictionary to 300 words or less.

        Example:
        `[
          { \"title\": \"Tall penguins\", \"snippet\": \"Emperor penguins are the tallest.\" },
          { \"title\": \"Penguin habitats\", \"snippet\": \"Emperor penguins only live in Antarctica.\" }
        ]`


        :return: The documents of this CohereChatRequest.
        :rtype: list[object]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this CohereChatRequest.
        A list of relevant documents that the model can refer to for generating grounded responses to the user's requests.
        Some example keys that you can add to the dictionary are \"text\", \"author\", and \"date\". Keep the total word count of the strings in the dictionary to 300 words or less.

        Example:
        `[
          { \"title\": \"Tall penguins\", \"snippet\": \"Emperor penguins are the tallest.\" },
          { \"title\": \"Penguin habitats\", \"snippet\": \"Emperor penguins only live in Antarctica.\" }
        ]`


        :param documents: The documents of this CohereChatRequest.
        :type: list[object]
        """
        self._documents = documents

    @property
    def response_format(self):
        """
        Gets the response_format of this CohereChatRequest.

        :return: The response_format of this CohereChatRequest.
        :rtype: oci.generative_ai_inference.models.CohereResponseFormat
        """
        return self._response_format

    @response_format.setter
    def response_format(self, response_format):
        """
        Sets the response_format of this CohereChatRequest.

        :param response_format: The response_format of this CohereChatRequest.
        :type: oci.generative_ai_inference.models.CohereResponseFormat
        """
        self._response_format = response_format

    @property
    def is_search_queries_only(self):
        """
        Gets the is_search_queries_only of this CohereChatRequest.
        When set to true, the response contains only a list of generated search queries without the search results and the model will not respond to the user's message.


        :return: The is_search_queries_only of this CohereChatRequest.
        :rtype: bool
        """
        return self._is_search_queries_only

    @is_search_queries_only.setter
    def is_search_queries_only(self, is_search_queries_only):
        """
        Sets the is_search_queries_only of this CohereChatRequest.
        When set to true, the response contains only a list of generated search queries without the search results and the model will not respond to the user's message.


        :param is_search_queries_only: The is_search_queries_only of this CohereChatRequest.
        :type: bool
        """
        self._is_search_queries_only = is_search_queries_only

    @property
    def preamble_override(self):
        """
        Gets the preamble_override of this CohereChatRequest.
        If specified, the default Cohere preamble is replaced with the provided preamble. A preamble is an initial guideline message that can change the model's overall chat behavior and conversation style. Default preambles vary for different models.

        Example: `You are a travel advisor. Answer with a pirate tone.`


        :return: The preamble_override of this CohereChatRequest.
        :rtype: str
        """
        return self._preamble_override

    @preamble_override.setter
    def preamble_override(self, preamble_override):
        """
        Sets the preamble_override of this CohereChatRequest.
        If specified, the default Cohere preamble is replaced with the provided preamble. A preamble is an initial guideline message that can change the model's overall chat behavior and conversation style. Default preambles vary for different models.

        Example: `You are a travel advisor. Answer with a pirate tone.`


        :param preamble_override: The preamble_override of this CohereChatRequest.
        :type: str
        """
        self._preamble_override = preamble_override

    @property
    def is_stream(self):
        """
        Gets the is_stream of this CohereChatRequest.
        Whether to stream the partial progress of the model's response. When set to true, as tokens become available, they are sent as data-only server-sent events.


        :return: The is_stream of this CohereChatRequest.
        :rtype: bool
        """
        return self._is_stream

    @is_stream.setter
    def is_stream(self, is_stream):
        """
        Sets the is_stream of this CohereChatRequest.
        Whether to stream the partial progress of the model's response. When set to true, as tokens become available, they are sent as data-only server-sent events.


        :param is_stream: The is_stream of this CohereChatRequest.
        :type: bool
        """
        self._is_stream = is_stream

    @property
    def stream_options(self):
        """
        Gets the stream_options of this CohereChatRequest.

        :return: The stream_options of this CohereChatRequest.
        :rtype: oci.generative_ai_inference.models.StreamOptions
        """
        return self._stream_options

    @stream_options.setter
    def stream_options(self, stream_options):
        """
        Sets the stream_options of this CohereChatRequest.

        :param stream_options: The stream_options of this CohereChatRequest.
        :type: oci.generative_ai_inference.models.StreamOptions
        """
        self._stream_options = stream_options

    @property
    def max_tokens(self):
        """
        Gets the max_tokens of this CohereChatRequest.
        The maximum number of output tokens that the model will generate for the response.


        :return: The max_tokens of this CohereChatRequest.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        """
        Sets the max_tokens of this CohereChatRequest.
        The maximum number of output tokens that the model will generate for the response.


        :param max_tokens: The max_tokens of this CohereChatRequest.
        :type: int
        """
        self._max_tokens = max_tokens

    @property
    def max_input_tokens(self):
        """
        Gets the max_input_tokens of this CohereChatRequest.
        The maximum number of input tokens to send to the model. If not specified, max_input_tokens is the model's context length limit minus a small buffer.


        :return: The max_input_tokens of this CohereChatRequest.
        :rtype: int
        """
        return self._max_input_tokens

    @max_input_tokens.setter
    def max_input_tokens(self, max_input_tokens):
        """
        Sets the max_input_tokens of this CohereChatRequest.
        The maximum number of input tokens to send to the model. If not specified, max_input_tokens is the model's context length limit minus a small buffer.


        :param max_input_tokens: The max_input_tokens of this CohereChatRequest.
        :type: int
        """
        self._max_input_tokens = max_input_tokens

    @property
    def temperature(self):
        """
        Gets the temperature of this CohereChatRequest.
        A number that sets the randomness of the generated output. A lower temperature means less random generations.
        Use lower numbers for tasks such as question answering or summarizing. High temperatures can generate hallucinations or factually incorrect information. Start with temperatures lower than 1.0 and increase the temperature for more creative outputs, as you regenerate the prompts to refine the outputs.


        :return: The temperature of this CohereChatRequest.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """
        Sets the temperature of this CohereChatRequest.
        A number that sets the randomness of the generated output. A lower temperature means less random generations.
        Use lower numbers for tasks such as question answering or summarizing. High temperatures can generate hallucinations or factually incorrect information. Start with temperatures lower than 1.0 and increase the temperature for more creative outputs, as you regenerate the prompts to refine the outputs.


        :param temperature: The temperature of this CohereChatRequest.
        :type: float
        """
        self._temperature = temperature

    @property
    def top_k(self):
        """
        Gets the top_k of this CohereChatRequest.
        A sampling method in which the model chooses the next token randomly from the top k most likely tokens. A higher value for k generates more random output, which makes the output text sound more natural. The default value for k is 0 which disables this method and considers all tokens. To set a number for the likely tokens, choose an integer between 1 and 500.

        If also using top p, then the model considers only the top tokens whose probabilities add up to p percent and ignores the rest of the k tokens. For example, if k is 20 but only the probabilities of the top 10 add up to the value of p, then only the top 10 tokens are chosen.


        :return: The top_k of this CohereChatRequest.
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        """
        Sets the top_k of this CohereChatRequest.
        A sampling method in which the model chooses the next token randomly from the top k most likely tokens. A higher value for k generates more random output, which makes the output text sound more natural. The default value for k is 0 which disables this method and considers all tokens. To set a number for the likely tokens, choose an integer between 1 and 500.

        If also using top p, then the model considers only the top tokens whose probabilities add up to p percent and ignores the rest of the k tokens. For example, if k is 20 but only the probabilities of the top 10 add up to the value of p, then only the top 10 tokens are chosen.


        :param top_k: The top_k of this CohereChatRequest.
        :type: int
        """
        self._top_k = top_k

    @property
    def top_p(self):
        """
        Gets the top_p of this CohereChatRequest.
        If set to a probability 0.0 < p < 1.0, it ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step.

        To eliminate tokens with low likelihood, assign p a minimum percentage for the next token's likelihood. For example, when p is set to 0.75, the model eliminates the bottom 25 percent for the next token. Set to 1.0 to consider all tokens and set to 0 to disable. If both k and p are enabled, p acts after k.


        :return: The top_p of this CohereChatRequest.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p):
        """
        Sets the top_p of this CohereChatRequest.
        If set to a probability 0.0 < p < 1.0, it ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step.

        To eliminate tokens with low likelihood, assign p a minimum percentage for the next token's likelihood. For example, when p is set to 0.75, the model eliminates the bottom 25 percent for the next token. Set to 1.0 to consider all tokens and set to 0 to disable. If both k and p are enabled, p acts after k.


        :param top_p: The top_p of this CohereChatRequest.
        :type: float
        """
        self._top_p = top_p

    @property
    def prompt_truncation(self):
        """
        Gets the prompt_truncation of this CohereChatRequest.
        Defaults to OFF. Dictates how the prompt will be constructed. With `promptTruncation` set to AUTO_PRESERVE_ORDER, some elements from `chatHistory` and `documents` will be dropped to construct a prompt that fits within the model's context length limit. During this process the order of the documents and chat history will be preserved. With `prompt_truncation` set to OFF, no elements will be dropped.

        Allowed values for this property are: "OFF", "AUTO_PRESERVE_ORDER"


        :return: The prompt_truncation of this CohereChatRequest.
        :rtype: str
        """
        return self._prompt_truncation

    @prompt_truncation.setter
    def prompt_truncation(self, prompt_truncation):
        """
        Sets the prompt_truncation of this CohereChatRequest.
        Defaults to OFF. Dictates how the prompt will be constructed. With `promptTruncation` set to AUTO_PRESERVE_ORDER, some elements from `chatHistory` and `documents` will be dropped to construct a prompt that fits within the model's context length limit. During this process the order of the documents and chat history will be preserved. With `prompt_truncation` set to OFF, no elements will be dropped.


        :param prompt_truncation: The prompt_truncation of this CohereChatRequest.
        :type: str
        """
        allowed_values = ["OFF", "AUTO_PRESERVE_ORDER"]
        if not value_allowed_none_or_none_sentinel(prompt_truncation, allowed_values):
            raise ValueError(
                f"Invalid value for `prompt_truncation`, must be None or one of {allowed_values}"
            )
        self._prompt_truncation = prompt_truncation

    @property
    def frequency_penalty(self):
        """
        Gets the frequency_penalty of this CohereChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on their frequency in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens. Set to 0 to disable.


        :return: The frequency_penalty of this CohereChatRequest.
        :rtype: float
        """
        return self._frequency_penalty

    @frequency_penalty.setter
    def frequency_penalty(self, frequency_penalty):
        """
        Sets the frequency_penalty of this CohereChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on their frequency in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens. Set to 0 to disable.


        :param frequency_penalty: The frequency_penalty of this CohereChatRequest.
        :type: float
        """
        self._frequency_penalty = frequency_penalty

    @property
    def presence_penalty(self):
        """
        Gets the presence_penalty of this CohereChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on whether they've appeared in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens.

        Similar to frequency penalty, a penalty is applied to previously present tokens, except that this penalty is applied equally to all tokens that have already appeared, regardless of how many times they've appeared. Set to 0 to disable.


        :return: The presence_penalty of this CohereChatRequest.
        :rtype: float
        """
        return self._presence_penalty

    @presence_penalty.setter
    def presence_penalty(self, presence_penalty):
        """
        Sets the presence_penalty of this CohereChatRequest.
        To reduce repetitiveness of generated tokens, this number penalizes new tokens based on whether they've appeared in the generated text so far. Greater numbers encourage the model to use new tokens, while lower numbers encourage the model to repeat the tokens.

        Similar to frequency penalty, a penalty is applied to previously present tokens, except that this penalty is applied equally to all tokens that have already appeared, regardless of how many times they've appeared. Set to 0 to disable.


        :param presence_penalty: The presence_penalty of this CohereChatRequest.
        :type: float
        """
        self._presence_penalty = presence_penalty

    @property
    def seed(self):
        """
        Gets the seed of this CohereChatRequest.
        If specified, the backend will make a best effort to sample tokens deterministically, so that repeated requests with the same seed and parameters yield the same result. However, determinism cannot be fully guaranteed.


        :return: The seed of this CohereChatRequest.
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """
        Sets the seed of this CohereChatRequest.
        If specified, the backend will make a best effort to sample tokens deterministically, so that repeated requests with the same seed and parameters yield the same result. However, determinism cannot be fully guaranteed.


        :param seed: The seed of this CohereChatRequest.
        :type: int
        """
        self._seed = seed

    @property
    def is_echo(self):
        """
        Gets the is_echo of this CohereChatRequest.
        Returns the full prompt that was sent to the model when True.


        :return: The is_echo of this CohereChatRequest.
        :rtype: bool
        """
        return self._is_echo

    @is_echo.setter
    def is_echo(self, is_echo):
        """
        Sets the is_echo of this CohereChatRequest.
        Returns the full prompt that was sent to the model when True.


        :param is_echo: The is_echo of this CohereChatRequest.
        :type: bool
        """
        self._is_echo = is_echo

    @property
    def tools(self):
        """
        Gets the tools of this CohereChatRequest.
        A list of available tools (functions) that the model may suggest invoking before producing a text response.


        :return: The tools of this CohereChatRequest.
        :rtype: list[oci.generative_ai_inference.models.CohereTool]
        """
        return self._tools

    @tools.setter
    def tools(self, tools):
        """
        Sets the tools of this CohereChatRequest.
        A list of available tools (functions) that the model may suggest invoking before producing a text response.


        :param tools: The tools of this CohereChatRequest.
        :type: list[oci.generative_ai_inference.models.CohereTool]
        """
        self._tools = tools

    @property
    def tool_results(self):
        """
        Gets the tool_results of this CohereChatRequest.
        A list of results from invoking tools recommended by the model in the previous chat turn.


        :return: The tool_results of this CohereChatRequest.
        :rtype: list[oci.generative_ai_inference.models.CohereToolResult]
        """
        return self._tool_results

    @tool_results.setter
    def tool_results(self, tool_results):
        """
        Sets the tool_results of this CohereChatRequest.
        A list of results from invoking tools recommended by the model in the previous chat turn.


        :param tool_results: The tool_results of this CohereChatRequest.
        :type: list[oci.generative_ai_inference.models.CohereToolResult]
        """
        self._tool_results = tool_results

    @property
    def is_force_single_step(self):
        """
        Gets the is_force_single_step of this CohereChatRequest.
        When enabled, the model will issue (potentially multiple) tool calls in a single step, before it receives the tool responses and directly answers the user's original message.


        :return: The is_force_single_step of this CohereChatRequest.
        :rtype: bool
        """
        return self._is_force_single_step

    @is_force_single_step.setter
    def is_force_single_step(self, is_force_single_step):
        """
        Sets the is_force_single_step of this CohereChatRequest.
        When enabled, the model will issue (potentially multiple) tool calls in a single step, before it receives the tool responses and directly answers the user's original message.


        :param is_force_single_step: The is_force_single_step of this CohereChatRequest.
        :type: bool
        """
        self._is_force_single_step = is_force_single_step

    @property
    def stop_sequences(self):
        """
        Gets the stop_sequences of this CohereChatRequest.
        Stop the model generation when it reaches a stop sequence defined in this parameter.


        :return: The stop_sequences of this CohereChatRequest.
        :rtype: list[str]
        """
        return self._stop_sequences

    @stop_sequences.setter
    def stop_sequences(self, stop_sequences):
        """
        Sets the stop_sequences of this CohereChatRequest.
        Stop the model generation when it reaches a stop sequence defined in this parameter.


        :param stop_sequences: The stop_sequences of this CohereChatRequest.
        :type: list[str]
        """
        self._stop_sequences = stop_sequences

    @property
    def is_raw_prompting(self):
        """
        Gets the is_raw_prompting of this CohereChatRequest.
        When enabled, the user\u2019s `message` will be sent to the model without any preprocessing.


        :return: The is_raw_prompting of this CohereChatRequest.
        :rtype: bool
        """
        return self._is_raw_prompting

    @is_raw_prompting.setter
    def is_raw_prompting(self, is_raw_prompting):
        """
        Sets the is_raw_prompting of this CohereChatRequest.
        When enabled, the user\u2019s `message` will be sent to the model without any preprocessing.


        :param is_raw_prompting: The is_raw_prompting of this CohereChatRequest.
        :type: bool
        """
        self._is_raw_prompting = is_raw_prompting

    @property
    def citation_quality(self):
        """
        Gets the citation_quality of this CohereChatRequest.
        When FAST is selected, citations are generated at the same time as the text output and the request will be completed sooner. May result in less accurate citations.

        Allowed values for this property are: "ACCURATE", "FAST"


        :return: The citation_quality of this CohereChatRequest.
        :rtype: str
        """
        return self._citation_quality

    @citation_quality.setter
    def citation_quality(self, citation_quality):
        """
        Sets the citation_quality of this CohereChatRequest.
        When FAST is selected, citations are generated at the same time as the text output and the request will be completed sooner. May result in less accurate citations.


        :param citation_quality: The citation_quality of this CohereChatRequest.
        :type: str
        """
        allowed_values = ["ACCURATE", "FAST"]
        if not value_allowed_none_or_none_sentinel(citation_quality, allowed_values):
            raise ValueError(
                f"Invalid value for `citation_quality`, must be None or one of {allowed_values}"
            )
        self._citation_quality = citation_quality

    @property
    def safety_mode(self):
        """
        Gets the safety_mode of this CohereChatRequest.
        Safety mode: Adds a safety instruction for the model to use when generating responses.
        Contextual: (Default) Puts fewer constraints on the output. It maintains core protections by aiming to reject harmful or illegal suggestions, but it allows profanity and some toxic content, sexually explicit and violent content, and content that contains medical, financial, or legal information. Contextual mode is suited for entertainment, creative, or academic use.
        Strict: Aims to avoid sensitive topics, such as violent or sexual acts and profanity. This mode aims to provide a safer experience by prohibiting responses or recommendations that it finds inappropriate. Strict mode is suited for corporate use, such as for corporate communications and customer service.
        Off: No safety mode is applied.
        Note: This parameter is only compatible with models cohere.command-r-08-2024, cohere.command-r-plus-08-2024 and Cohere models released after these models. See `release dates`__.

        __ https://docs.cloud.oracle.com/iaas/Content/generative-ai/deprecating.htm

        Allowed values for this property are: "CONTEXTUAL", "STRICT", "OFF"


        :return: The safety_mode of this CohereChatRequest.
        :rtype: str
        """
        return self._safety_mode

    @safety_mode.setter
    def safety_mode(self, safety_mode):
        """
        Sets the safety_mode of this CohereChatRequest.
        Safety mode: Adds a safety instruction for the model to use when generating responses.
        Contextual: (Default) Puts fewer constraints on the output. It maintains core protections by aiming to reject harmful or illegal suggestions, but it allows profanity and some toxic content, sexually explicit and violent content, and content that contains medical, financial, or legal information. Contextual mode is suited for entertainment, creative, or academic use.
        Strict: Aims to avoid sensitive topics, such as violent or sexual acts and profanity. This mode aims to provide a safer experience by prohibiting responses or recommendations that it finds inappropriate. Strict mode is suited for corporate use, such as for corporate communications and customer service.
        Off: No safety mode is applied.
        Note: This parameter is only compatible with models cohere.command-r-08-2024, cohere.command-r-plus-08-2024 and Cohere models released after these models. See `release dates`__.

        __ https://docs.cloud.oracle.com/iaas/Content/generative-ai/deprecating.htm


        :param safety_mode: The safety_mode of this CohereChatRequest.
        :type: str
        """
        allowed_values = ["CONTEXTUAL", "STRICT", "OFF"]
        if not value_allowed_none_or_none_sentinel(safety_mode, allowed_values):
            raise ValueError(
                f"Invalid value for `safety_mode`, must be None or one of {allowed_values}"
            )
        self._safety_mode = safety_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
