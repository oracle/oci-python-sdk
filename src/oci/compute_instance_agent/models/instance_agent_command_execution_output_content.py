# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandExecutionOutputContent(object):
    """
    command execution output.
    """

    #: A constant which can be used with the output_type property of a InstanceAgentCommandExecutionOutputContent.
    #: This constant has a value of "TEXT"
    OUTPUT_TYPE_TEXT = "TEXT"

    #: A constant which can be used with the output_type property of a InstanceAgentCommandExecutionOutputContent.
    #: This constant has a value of "OBJECT_STORAGE_URI"
    OUTPUT_TYPE_OBJECT_STORAGE_URI = "OBJECT_STORAGE_URI"

    #: A constant which can be used with the output_type property of a InstanceAgentCommandExecutionOutputContent.
    #: This constant has a value of "OBJECT_STORAGE_TUPLE"
    OUTPUT_TYPE_OBJECT_STORAGE_TUPLE = "OBJECT_STORAGE_TUPLE"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandExecutionOutputContent object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandExecutionOutputViaTextDetails`
        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails`
        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandExecutionOutputViaObjectStorageTupleDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output_type:
            The value to assign to the output_type property of this InstanceAgentCommandExecutionOutputContent.
            Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type output_type: str

        :param exit_code:
            The value to assign to the exit_code property of this InstanceAgentCommandExecutionOutputContent.
        :type exit_code: int

        :param message:
            The value to assign to the message property of this InstanceAgentCommandExecutionOutputContent.
        :type message: str

        """
        self.swagger_types = {
            'output_type': 'str',
            'exit_code': 'int',
            'message': 'str'
        }

        self.attribute_map = {
            'output_type': 'outputType',
            'exit_code': 'exitCode',
            'message': 'message'
        }

        self._output_type = None
        self._exit_code = None
        self._message = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['outputType']

        if type == 'TEXT':
            return 'InstanceAgentCommandExecutionOutputViaTextDetails'

        if type == 'OBJECT_STORAGE_URI':
            return 'InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails'

        if type == 'OBJECT_STORAGE_TUPLE':
            return 'InstanceAgentCommandExecutionOutputViaObjectStorageTupleDetails'
        else:
            return 'InstanceAgentCommandExecutionOutputContent'

    @property
    def output_type(self):
        """
        **[Required]** Gets the output_type of this InstanceAgentCommandExecutionOutputContent.
        The response type where the command reponse is made available

        Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The output_type of this InstanceAgentCommandExecutionOutputContent.
        :rtype: str
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """
        Sets the output_type of this InstanceAgentCommandExecutionOutputContent.
        The response type where the command reponse is made available


        :param output_type: The output_type of this InstanceAgentCommandExecutionOutputContent.
        :type: str
        """
        allowed_values = ["TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE"]
        if not value_allowed_none_or_none_sentinel(output_type, allowed_values):
            output_type = 'UNKNOWN_ENUM_VALUE'
        self._output_type = output_type

    @property
    def exit_code(self):
        """
        **[Required]** Gets the exit_code of this InstanceAgentCommandExecutionOutputContent.
        command exit code.


        :return: The exit_code of this InstanceAgentCommandExecutionOutputContent.
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """
        Sets the exit_code of this InstanceAgentCommandExecutionOutputContent.
        command exit code.


        :param exit_code: The exit_code of this InstanceAgentCommandExecutionOutputContent.
        :type: int
        """
        self._exit_code = exit_code

    @property
    def message(self):
        """
        Gets the message of this InstanceAgentCommandExecutionOutputContent.
        optional status message that agent's can populate for additional troubleshooting.


        :return: The message of this InstanceAgentCommandExecutionOutputContent.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InstanceAgentCommandExecutionOutputContent.
        optional status message that agent's can populate for additional troubleshooting.


        :param message: The message of this InstanceAgentCommandExecutionOutputContent.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
