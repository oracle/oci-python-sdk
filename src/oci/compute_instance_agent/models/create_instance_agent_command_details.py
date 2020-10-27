# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInstanceAgentCommandDetails(object):
    """
    Create Command Details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInstanceAgentCommandDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateInstanceAgentCommandDetails.
        :type compartment_id: str

        :param execution_time_out_in_seconds:
            The value to assign to the execution_time_out_in_seconds property of this CreateInstanceAgentCommandDetails.
        :type execution_time_out_in_seconds: int

        :param display_name:
            The value to assign to the display_name property of this CreateInstanceAgentCommandDetails.
        :type display_name: str

        :param target:
            The value to assign to the target property of this CreateInstanceAgentCommandDetails.
        :type target: InstanceAgentCommandTarget

        :param content:
            The value to assign to the content property of this CreateInstanceAgentCommandDetails.
        :type content: InstanceAgentCommandContent

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'execution_time_out_in_seconds': 'int',
            'display_name': 'str',
            'target': 'InstanceAgentCommandTarget',
            'content': 'InstanceAgentCommandContent'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'execution_time_out_in_seconds': 'executionTimeOutInSeconds',
            'display_name': 'displayName',
            'target': 'target',
            'content': 'content'
        }

        self._compartment_id = None
        self._execution_time_out_in_seconds = None
        self._display_name = None
        self._target = None
        self._content = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateInstanceAgentCommandDetails.
        The OCID of the compartment you want to create the command.


        :return: The compartment_id of this CreateInstanceAgentCommandDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateInstanceAgentCommandDetails.
        The OCID of the compartment you want to create the command.


        :param compartment_id: The compartment_id of this CreateInstanceAgentCommandDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def execution_time_out_in_seconds(self):
        """
        **[Required]** Gets the execution_time_out_in_seconds of this CreateInstanceAgentCommandDetails.
        Command execution time limit. Zero means no timeout.


        :return: The execution_time_out_in_seconds of this CreateInstanceAgentCommandDetails.
        :rtype: int
        """
        return self._execution_time_out_in_seconds

    @execution_time_out_in_seconds.setter
    def execution_time_out_in_seconds(self, execution_time_out_in_seconds):
        """
        Sets the execution_time_out_in_seconds of this CreateInstanceAgentCommandDetails.
        Command execution time limit. Zero means no timeout.


        :param execution_time_out_in_seconds: The execution_time_out_in_seconds of this CreateInstanceAgentCommandDetails.
        :type: int
        """
        self._execution_time_out_in_seconds = execution_time_out_in_seconds

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateInstanceAgentCommandDetails.
        A user-friendly name for the command. It does not have to be unique.
        Avoid entering confidential information.
        Example: `Database Backup Command`


        :return: The display_name of this CreateInstanceAgentCommandDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateInstanceAgentCommandDetails.
        A user-friendly name for the command. It does not have to be unique.
        Avoid entering confidential information.
        Example: `Database Backup Command`


        :param display_name: The display_name of this CreateInstanceAgentCommandDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def target(self):
        """
        **[Required]** Gets the target of this CreateInstanceAgentCommandDetails.

        :return: The target of this CreateInstanceAgentCommandDetails.
        :rtype: InstanceAgentCommandTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this CreateInstanceAgentCommandDetails.

        :param target: The target of this CreateInstanceAgentCommandDetails.
        :type: InstanceAgentCommandTarget
        """
        self._target = target

    @property
    def content(self):
        """
        **[Required]** Gets the content of this CreateInstanceAgentCommandDetails.

        :return: The content of this CreateInstanceAgentCommandDetails.
        :rtype: InstanceAgentCommandContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this CreateInstanceAgentCommandDetails.

        :param content: The content of this CreateInstanceAgentCommandDetails.
        :type: InstanceAgentCommandContent
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
