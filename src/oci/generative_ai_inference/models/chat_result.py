# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChatResult(object):
    """
    The response to the chat conversation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChatResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_id:
            The value to assign to the model_id property of this ChatResult.
        :type model_id: str

        :param model_version:
            The value to assign to the model_version property of this ChatResult.
        :type model_version: str

        :param chat_response:
            The value to assign to the chat_response property of this ChatResult.
        :type chat_response: oci.generative_ai_inference.models.BaseChatResponse

        """
        self.swagger_types = {
            'model_id': 'str',
            'model_version': 'str',
            'chat_response': 'BaseChatResponse'
        }
        self.attribute_map = {
            'model_id': 'modelId',
            'model_version': 'modelVersion',
            'chat_response': 'chatResponse'
        }
        self._model_id = None
        self._model_version = None
        self._chat_response = None

    @property
    def model_id(self):
        """
        **[Required]** Gets the model_id of this ChatResult.
        The OCID of the model that's used in this inference request.


        :return: The model_id of this ChatResult.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this ChatResult.
        The OCID of the model that's used in this inference request.


        :param model_id: The model_id of this ChatResult.
        :type: str
        """
        self._model_id = model_id

    @property
    def model_version(self):
        """
        **[Required]** Gets the model_version of this ChatResult.
        The version of the model.


        :return: The model_version of this ChatResult.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ChatResult.
        The version of the model.


        :param model_version: The model_version of this ChatResult.
        :type: str
        """
        self._model_version = model_version

    @property
    def chat_response(self):
        """
        **[Required]** Gets the chat_response of this ChatResult.

        :return: The chat_response of this ChatResult.
        :rtype: oci.generative_ai_inference.models.BaseChatResponse
        """
        return self._chat_response

    @chat_response.setter
    def chat_response(self, chat_response):
        """
        Sets the chat_response of this ChatResult.

        :param chat_response: The chat_response of this ChatResult.
        :type: oci.generative_ai_inference.models.BaseChatResponse
        """
        self._chat_response = chat_response

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
