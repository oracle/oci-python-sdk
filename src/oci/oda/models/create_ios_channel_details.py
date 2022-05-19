# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_channel_details import CreateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIosChannelDetails(CreateChannelDetails):
    """
    Properties required to create an iOS channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIosChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateIosChannelDetails.type` attribute
        of this class is ``IOS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateIosChannelDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateIosChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateIosChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateIosChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateIosChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateIosChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param max_token_expiration_time_in_minutes:
            The value to assign to the max_token_expiration_time_in_minutes property of this CreateIosChannelDetails.
        :type max_token_expiration_time_in_minutes: int

        :param is_client_authentication_enabled:
            The value to assign to the is_client_authentication_enabled property of this CreateIosChannelDetails.
        :type is_client_authentication_enabled: bool

        :param bot_id:
            The value to assign to the bot_id property of this CreateIosChannelDetails.
        :type bot_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'max_token_expiration_time_in_minutes': 'int',
            'is_client_authentication_enabled': 'bool',
            'bot_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'max_token_expiration_time_in_minutes': 'maxTokenExpirationTimeInMinutes',
            'is_client_authentication_enabled': 'isClientAuthenticationEnabled',
            'bot_id': 'botId'
        }

        self._name = None
        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._max_token_expiration_time_in_minutes = None
        self._is_client_authentication_enabled = None
        self._bot_id = None
        self._type = 'IOS'

    @property
    def max_token_expiration_time_in_minutes(self):
        """
        Gets the max_token_expiration_time_in_minutes of this CreateIosChannelDetails.
        The maximum time until the token expires (in minutes).


        :return: The max_token_expiration_time_in_minutes of this CreateIosChannelDetails.
        :rtype: int
        """
        return self._max_token_expiration_time_in_minutes

    @max_token_expiration_time_in_minutes.setter
    def max_token_expiration_time_in_minutes(self, max_token_expiration_time_in_minutes):
        """
        Sets the max_token_expiration_time_in_minutes of this CreateIosChannelDetails.
        The maximum time until the token expires (in minutes).


        :param max_token_expiration_time_in_minutes: The max_token_expiration_time_in_minutes of this CreateIosChannelDetails.
        :type: int
        """
        self._max_token_expiration_time_in_minutes = max_token_expiration_time_in_minutes

    @property
    def is_client_authentication_enabled(self):
        """
        **[Required]** Gets the is_client_authentication_enabled of this CreateIosChannelDetails.
        Whether client authentication is enabled or not.


        :return: The is_client_authentication_enabled of this CreateIosChannelDetails.
        :rtype: bool
        """
        return self._is_client_authentication_enabled

    @is_client_authentication_enabled.setter
    def is_client_authentication_enabled(self, is_client_authentication_enabled):
        """
        Sets the is_client_authentication_enabled of this CreateIosChannelDetails.
        Whether client authentication is enabled or not.


        :param is_client_authentication_enabled: The is_client_authentication_enabled of this CreateIosChannelDetails.
        :type: bool
        """
        self._is_client_authentication_enabled = is_client_authentication_enabled

    @property
    def bot_id(self):
        """
        Gets the bot_id of this CreateIosChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this CreateIosChannelDetails.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this CreateIosChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this CreateIosChannelDetails.
        :type: str
        """
        self._bot_id = bot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
