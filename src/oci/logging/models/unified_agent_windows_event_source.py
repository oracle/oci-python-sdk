# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .unified_agent_logging_source import UnifiedAgentLoggingSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentWindowsEventSource(UnifiedAgentLoggingSource):
    """
    Windows events log source object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentWindowsEventSource object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.UnifiedAgentWindowsEventSource.source_type` attribute
        of this class is ``WINDOWS_EVENT_LOG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UnifiedAgentWindowsEventSource.
        :type name: str

        :param source_type:
            The value to assign to the source_type property of this UnifiedAgentWindowsEventSource.
            Allowed values for this property are: "LOG_TAIL", "WINDOWS_EVENT_LOG"
        :type source_type: str

        :param channels:
            The value to assign to the channels property of this UnifiedAgentWindowsEventSource.
        :type channels: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'source_type': 'str',
            'channels': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'source_type': 'sourceType',
            'channels': 'channels'
        }

        self._name = None
        self._source_type = None
        self._channels = None
        self._source_type = 'WINDOWS_EVENT_LOG'

    @property
    def channels(self):
        """
        Gets the channels of this UnifiedAgentWindowsEventSource.

        :return: The channels of this UnifiedAgentWindowsEventSource.
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """
        Sets the channels of this UnifiedAgentWindowsEventSource.

        :param channels: The channels of this UnifiedAgentWindowsEventSource.
        :type: list[str]
        """
        self._channels = channels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
