# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531

from .tool_input import ToolInput
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericToolInput(ToolInput):
    """
    Represents a generic tool input schema that accepts flexible, freeform JSON parameters. This structure is intended for tools that do not require a fixed input schema.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericToolInput object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_agent_runtime.models.GenericToolInput.tool_input_type` attribute
        of this class is ``GENERIC_TOOL_INPUT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tool_id:
            The value to assign to the tool_id property of this GenericToolInput.
        :type tool_id: str

        :param tool_input_type:
            The value to assign to the tool_input_type property of this GenericToolInput.
            Allowed values for this property are: "GENERIC_TOOL_INPUT"
        :type tool_input_type: str

        :param input:
            The value to assign to the input property of this GenericToolInput.
        :type input: object

        """
        self.swagger_types = {
            'tool_id': 'str',
            'tool_input_type': 'str',
            'input': 'object'
        }
        self.attribute_map = {
            'tool_id': 'toolId',
            'tool_input_type': 'toolInputType',
            'input': 'input'
        }
        self._tool_id = None
        self._tool_input_type = None
        self._input = None
        self._tool_input_type = 'GENERIC_TOOL_INPUT'

    @property
    def input(self):
        """
        **[Required]** Gets the input of this GenericToolInput.
        A freeform JSON object containing the input parameters to be passed to the tool during execution.


        :return: The input of this GenericToolInput.
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this GenericToolInput.
        A freeform JSON object containing the input parameters to be passed to the tool during execution.


        :param input: The input of this GenericToolInput.
        :type: object
        """
        self._input = input

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
