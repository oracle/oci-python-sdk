# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_channel_details import UpdateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateApplicationChannelDetails(UpdateChannelDetails):
    """
    Properties to update an Application channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateApplicationChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.UpdateApplicationChannelDetails.type` attribute
        of this class is ``APPLICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateApplicationChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this UpdateApplicationChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this UpdateApplicationChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateApplicationChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateApplicationChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param outbound_url:
            The value to assign to the outbound_url property of this UpdateApplicationChannelDetails.
        :type outbound_url: str

        :param is_authenticated_user_id:
            The value to assign to the is_authenticated_user_id property of this UpdateApplicationChannelDetails.
        :type is_authenticated_user_id: bool

        """
        self.swagger_types = {
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'outbound_url': 'str',
            'is_authenticated_user_id': 'bool'
        }

        self.attribute_map = {
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'outbound_url': 'outboundUrl',
            'is_authenticated_user_id': 'isAuthenticatedUserId'
        }

        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._outbound_url = None
        self._is_authenticated_user_id = None
        self._type = 'APPLICATION'

    @property
    def outbound_url(self):
        """
        Gets the outbound_url of this UpdateApplicationChannelDetails.
        The URL to send response and error messages to.


        :return: The outbound_url of this UpdateApplicationChannelDetails.
        :rtype: str
        """
        return self._outbound_url

    @outbound_url.setter
    def outbound_url(self, outbound_url):
        """
        Sets the outbound_url of this UpdateApplicationChannelDetails.
        The URL to send response and error messages to.


        :param outbound_url: The outbound_url of this UpdateApplicationChannelDetails.
        :type: str
        """
        self._outbound_url = outbound_url

    @property
    def is_authenticated_user_id(self):
        """
        Gets the is_authenticated_user_id of this UpdateApplicationChannelDetails.
        True if the user id in the AIC message should be treated as an authenticated user id.


        :return: The is_authenticated_user_id of this UpdateApplicationChannelDetails.
        :rtype: bool
        """
        return self._is_authenticated_user_id

    @is_authenticated_user_id.setter
    def is_authenticated_user_id(self, is_authenticated_user_id):
        """
        Sets the is_authenticated_user_id of this UpdateApplicationChannelDetails.
        True if the user id in the AIC message should be treated as an authenticated user id.


        :param is_authenticated_user_id: The is_authenticated_user_id of this UpdateApplicationChannelDetails.
        :type: bool
        """
        self._is_authenticated_user_id = is_authenticated_user_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
