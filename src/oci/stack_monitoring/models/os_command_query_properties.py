# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330

from .metric_extension_query_properties import MetricExtensionQueryProperties
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OsCommandQueryProperties(MetricExtensionQueryProperties):
    """
    Query Properties applicable to OS_COMMAND type of collection method
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OsCommandQueryProperties object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.OsCommandQueryProperties.collection_method` attribute
        of this class is ``OS_COMMAND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param collection_method:
            The value to assign to the collection_method property of this OsCommandQueryProperties.
            Allowed values for this property are: "OS_COMMAND", "SQL", "JMX"
        :type collection_method: str

        :param command:
            The value to assign to the command property of this OsCommandQueryProperties.
        :type command: str

        :param delimiter:
            The value to assign to the delimiter property of this OsCommandQueryProperties.
        :type delimiter: str

        :param script_details:
            The value to assign to the script_details property of this OsCommandQueryProperties.
        :type script_details: oci.stack_monitoring.models.ScriptFileDetails

        :param arguments:
            The value to assign to the arguments property of this OsCommandQueryProperties.
        :type arguments: str

        :param starts_with:
            The value to assign to the starts_with property of this OsCommandQueryProperties.
        :type starts_with: str

        """
        self.swagger_types = {
            'collection_method': 'str',
            'command': 'str',
            'delimiter': 'str',
            'script_details': 'ScriptFileDetails',
            'arguments': 'str',
            'starts_with': 'str'
        }

        self.attribute_map = {
            'collection_method': 'collectionMethod',
            'command': 'command',
            'delimiter': 'delimiter',
            'script_details': 'scriptDetails',
            'arguments': 'arguments',
            'starts_with': 'startsWith'
        }

        self._collection_method = None
        self._command = None
        self._delimiter = None
        self._script_details = None
        self._arguments = None
        self._starts_with = None
        self._collection_method = 'OS_COMMAND'

    @property
    def command(self):
        """
        **[Required]** Gets the command of this OsCommandQueryProperties.
        OS command to execute without arguments


        :return: The command of this OsCommandQueryProperties.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this OsCommandQueryProperties.
        OS command to execute without arguments


        :param command: The command of this OsCommandQueryProperties.
        :type: str
        """
        self._command = command

    @property
    def delimiter(self):
        """
        **[Required]** Gets the delimiter of this OsCommandQueryProperties.
        Character used to delimit multiple metric values in single line of output


        :return: The delimiter of this OsCommandQueryProperties.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """
        Sets the delimiter of this OsCommandQueryProperties.
        Character used to delimit multiple metric values in single line of output


        :param delimiter: The delimiter of this OsCommandQueryProperties.
        :type: str
        """
        self._delimiter = delimiter

    @property
    def script_details(self):
        """
        Gets the script_details of this OsCommandQueryProperties.

        :return: The script_details of this OsCommandQueryProperties.
        :rtype: oci.stack_monitoring.models.ScriptFileDetails
        """
        return self._script_details

    @script_details.setter
    def script_details(self, script_details):
        """
        Sets the script_details of this OsCommandQueryProperties.

        :param script_details: The script_details of this OsCommandQueryProperties.
        :type: oci.stack_monitoring.models.ScriptFileDetails
        """
        self._script_details = script_details

    @property
    def arguments(self):
        """
        Gets the arguments of this OsCommandQueryProperties.
        Arguments required by either command or script


        :return: The arguments of this OsCommandQueryProperties.
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this OsCommandQueryProperties.
        Arguments required by either command or script


        :param arguments: The arguments of this OsCommandQueryProperties.
        :type: str
        """
        self._arguments = arguments

    @property
    def starts_with(self):
        """
        Gets the starts_with of this OsCommandQueryProperties.
        String prefix used to identify metric output of the OS Command


        :return: The starts_with of this OsCommandQueryProperties.
        :rtype: str
        """
        return self._starts_with

    @starts_with.setter
    def starts_with(self, starts_with):
        """
        Sets the starts_with of this OsCommandQueryProperties.
        String prefix used to identify metric output of the OS Command


        :param starts_with: The starts_with of this OsCommandQueryProperties.
        :type: str
        """
        self._starts_with = starts_with

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
