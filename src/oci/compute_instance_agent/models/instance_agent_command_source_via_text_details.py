# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_agent_command_source_details import InstanceAgentCommandSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandSourceViaTextDetails(InstanceAgentCommandSourceDetails):
    """
    The source of the command when provided using plain text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandSourceViaTextDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.compute_instance_agent.models.InstanceAgentCommandSourceViaTextDetails.source_type` attribute
        of this class is ``TEXT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceAgentCommandSourceViaTextDetails.
            Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE"
        :type source_type: str

        :param text:
            The value to assign to the text property of this InstanceAgentCommandSourceViaTextDetails.
        :type text: str

        :param text_sha256:
            The value to assign to the text_sha256 property of this InstanceAgentCommandSourceViaTextDetails.
        :type text_sha256: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'text': 'str',
            'text_sha256': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'text': 'text',
            'text_sha256': 'textSha256'
        }

        self._source_type = None
        self._text = None
        self._text_sha256 = None
        self._source_type = 'TEXT'

    @property
    def text(self):
        """
        **[Required]** Gets the text of this InstanceAgentCommandSourceViaTextDetails.
        The plain text command.


        :return: The text of this InstanceAgentCommandSourceViaTextDetails.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this InstanceAgentCommandSourceViaTextDetails.
        The plain text command.


        :param text: The text of this InstanceAgentCommandSourceViaTextDetails.
        :type: str
        """
        self._text = text

    @property
    def text_sha256(self):
        """
        Gets the text_sha256 of this InstanceAgentCommandSourceViaTextDetails.
        SHA-256 checksum value of the text content.


        :return: The text_sha256 of this InstanceAgentCommandSourceViaTextDetails.
        :rtype: str
        """
        return self._text_sha256

    @text_sha256.setter
    def text_sha256(self, text_sha256):
        """
        Sets the text_sha256 of this InstanceAgentCommandSourceViaTextDetails.
        SHA-256 checksum value of the text content.


        :param text_sha256: The text_sha256 of this InstanceAgentCommandSourceViaTextDetails.
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
