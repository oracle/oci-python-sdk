# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_agent_command_execution_output_content import InstanceAgentCommandExecutionOutputContent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandExecutionOutputViaTextDetails(InstanceAgentCommandExecutionOutputContent):
    """
    command execution output via text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandExecutionOutputViaTextDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.compute_instance_agent.models.InstanceAgentCommandExecutionOutputViaTextDetails.output_type` attribute
        of this class is ``TEXT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output_type:
            The value to assign to the output_type property of this InstanceAgentCommandExecutionOutputViaTextDetails.
            Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE"
        :type output_type: str

        :param exit_code:
            The value to assign to the exit_code property of this InstanceAgentCommandExecutionOutputViaTextDetails.
        :type exit_code: int

        :param message:
            The value to assign to the message property of this InstanceAgentCommandExecutionOutputViaTextDetails.
        :type message: str

        :param text:
            The value to assign to the text property of this InstanceAgentCommandExecutionOutputViaTextDetails.
        :type text: str

        :param text_sha256:
            The value to assign to the text_sha256 property of this InstanceAgentCommandExecutionOutputViaTextDetails.
        :type text_sha256: str

        """
        self.swagger_types = {
            'output_type': 'str',
            'exit_code': 'int',
            'message': 'str',
            'text': 'str',
            'text_sha256': 'str'
        }

        self.attribute_map = {
            'output_type': 'outputType',
            'exit_code': 'exitCode',
            'message': 'message',
            'text': 'text',
            'text_sha256': 'textSha256'
        }

        self._output_type = None
        self._exit_code = None
        self._message = None
        self._text = None
        self._text_sha256 = None
        self._output_type = 'TEXT'

    @property
    def text(self):
        """
        **[Required]** Gets the text of this InstanceAgentCommandExecutionOutputViaTextDetails.
        The command response output.


        :return: The text of this InstanceAgentCommandExecutionOutputViaTextDetails.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this InstanceAgentCommandExecutionOutputViaTextDetails.
        The command response output.


        :param text: The text of this InstanceAgentCommandExecutionOutputViaTextDetails.
        :type: str
        """
        self._text = text

    @property
    def text_sha256(self):
        """
        Gets the text_sha256 of this InstanceAgentCommandExecutionOutputViaTextDetails.
        Sha256 checksum value of the text content


        :return: The text_sha256 of this InstanceAgentCommandExecutionOutputViaTextDetails.
        :rtype: str
        """
        return self._text_sha256

    @text_sha256.setter
    def text_sha256(self, text_sha256):
        """
        Sets the text_sha256 of this InstanceAgentCommandExecutionOutputViaTextDetails.
        Sha256 checksum value of the text content


        :param text_sha256: The text_sha256 of this InstanceAgentCommandExecutionOutputViaTextDetails.
        :type: str
        """
        self._text_sha256 = text_sha256

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
