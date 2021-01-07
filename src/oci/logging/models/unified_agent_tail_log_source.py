# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .unified_agent_logging_source import UnifiedAgentLoggingSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentTailLogSource(UnifiedAgentLoggingSource):
    """
    Tail log source object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentTailLogSource object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.UnifiedAgentTailLogSource.source_type` attribute
        of this class is ``LOG_TAIL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UnifiedAgentTailLogSource.
        :type name: str

        :param source_type:
            The value to assign to the source_type property of this UnifiedAgentTailLogSource.
            Allowed values for this property are: "LOG_TAIL", "WINDOWS_EVENT_LOG"
        :type source_type: str

        :param paths:
            The value to assign to the paths property of this UnifiedAgentTailLogSource.
        :type paths: list[str]

        :param parser:
            The value to assign to the parser property of this UnifiedAgentTailLogSource.
        :type parser: oci.logging.models.UnifiedAgentParser

        """
        self.swagger_types = {
            'name': 'str',
            'source_type': 'str',
            'paths': 'list[str]',
            'parser': 'UnifiedAgentParser'
        }

        self.attribute_map = {
            'name': 'name',
            'source_type': 'sourceType',
            'paths': 'paths',
            'parser': 'parser'
        }

        self._name = None
        self._source_type = None
        self._paths = None
        self._parser = None
        self._source_type = 'LOG_TAIL'

    @property
    def paths(self):
        """
        Gets the paths of this UnifiedAgentTailLogSource.

        :return: The paths of this UnifiedAgentTailLogSource.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this UnifiedAgentTailLogSource.

        :param paths: The paths of this UnifiedAgentTailLogSource.
        :type: list[str]
        """
        self._paths = paths

    @property
    def parser(self):
        """
        Gets the parser of this UnifiedAgentTailLogSource.

        :return: The parser of this UnifiedAgentTailLogSource.
        :rtype: oci.logging.models.UnifiedAgentParser
        """
        return self._parser

    @parser.setter
    def parser(self, parser):
        """
        Sets the parser of this UnifiedAgentTailLogSource.

        :param parser: The parser of this UnifiedAgentTailLogSource.
        :type: oci.logging.models.UnifiedAgentParser
        """
        self._parser = parser

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
