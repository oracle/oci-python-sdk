# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101

from .realtime_message import RealtimeMessage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RealtimeMessageConnect(RealtimeMessage):
    """
    The websocket connection message received from service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RealtimeMessageConnect object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_speech.models.RealtimeMessageConnect.event` attribute
        of this class is ``CONNECT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param event:
            The value to assign to the event property of this RealtimeMessageConnect.
            Allowed values for this property are: "RESULT", "ACKAUDIO", "ERROR", "CONNECT"
        :type event: str

        :param session_id:
            The value to assign to the session_id property of this RealtimeMessageConnect.
        :type session_id: str

        """
        self.swagger_types = {
            'event': 'str',
            'session_id': 'str'
        }
        self.attribute_map = {
            'event': 'event',
            'session_id': 'sessionId'
        }
        self._event = None
        self._session_id = None
        self._event = 'CONNECT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
