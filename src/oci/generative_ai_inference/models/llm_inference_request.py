# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LlmInferenceRequest(object):
    """
    The base class for the inference requests.
    """

    #: A constant which can be used with the runtime_type property of a LlmInferenceRequest.
    #: This constant has a value of "COHERE"
    RUNTIME_TYPE_COHERE = "COHERE"

    #: A constant which can be used with the runtime_type property of a LlmInferenceRequest.
    #: This constant has a value of "LLAMA"
    RUNTIME_TYPE_LLAMA = "LLAMA"

    def __init__(self, **kwargs):
        """
        Initializes a new LlmInferenceRequest object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_inference.models.LlamaLlmInferenceRequest`
        * :class:`~oci.generative_ai_inference.models.CohereLlmInferenceRequest`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param runtime_type:
            The value to assign to the runtime_type property of this LlmInferenceRequest.
            Allowed values for this property are: "COHERE", "LLAMA"
        :type runtime_type: str

        """
        self.swagger_types = {
            'runtime_type': 'str'
        }
        self.attribute_map = {
            'runtime_type': 'runtimeType'
        }
        self._runtime_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['runtimeType']

        if type == 'LLAMA':
            return 'LlamaLlmInferenceRequest'

        if type == 'COHERE':
            return 'CohereLlmInferenceRequest'
        else:
            return 'LlmInferenceRequest'

    @property
    def runtime_type(self):
        """
        **[Required]** Gets the runtime_type of this LlmInferenceRequest.
        The runtime of the provided model.

        Allowed values for this property are: "COHERE", "LLAMA"


        :return: The runtime_type of this LlmInferenceRequest.
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        """
        Sets the runtime_type of this LlmInferenceRequest.
        The runtime of the provided model.


        :param runtime_type: The runtime_type of this LlmInferenceRequest.
        :type: str
        """
        allowed_values = ["COHERE", "LLAMA"]
        if not value_allowed_none_or_none_sentinel(runtime_type, allowed_values):
            raise ValueError(
                f"Invalid value for `runtime_type`, must be None or one of {allowed_values}"
            )
        self._runtime_type = runtime_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
