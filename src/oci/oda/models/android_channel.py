# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .channel import Channel
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AndroidChannel(Channel):
    """
    The configuration for an Android channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AndroidChannel object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.AndroidChannel.type` attribute
        of this class is ``ANDROID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AndroidChannel.
        :type id: str

        :param name:
            The value to assign to the name property of this AndroidChannel.
        :type name: str

        :param description:
            The value to assign to the description property of this AndroidChannel.
        :type description: str

        :param category:
            The value to assign to the category property of this AndroidChannel.
            Allowed values for this property are: "AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"
        :type category: str

        :param type:
            The value to assign to the type property of this AndroidChannel.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this AndroidChannel.
        :type session_expiry_duration_in_milliseconds: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AndroidChannel.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this AndroidChannel.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AndroidChannel.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AndroidChannel.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AndroidChannel.
        :type defined_tags: dict(str, dict(str, object))

        :param max_token_expiration_time_in_minutes:
            The value to assign to the max_token_expiration_time_in_minutes property of this AndroidChannel.
        :type max_token_expiration_time_in_minutes: int

        :param is_client_authentication_enabled:
            The value to assign to the is_client_authentication_enabled property of this AndroidChannel.
        :type is_client_authentication_enabled: bool

        :param bot_id:
            The value to assign to the bot_id property of this AndroidChannel.
        :type bot_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'category': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'max_token_expiration_time_in_minutes': 'int',
            'is_client_authentication_enabled': 'bool',
            'bot_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'category': 'category',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'max_token_expiration_time_in_minutes': 'maxTokenExpirationTimeInMinutes',
            'is_client_authentication_enabled': 'isClientAuthenticationEnabled',
            'bot_id': 'botId'
        }

        self._id = None
        self._name = None
        self._description = None
        self._category = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._max_token_expiration_time_in_minutes = None
        self._is_client_authentication_enabled = None
        self._bot_id = None
        self._type = 'ANDROID'

    @property
    def max_token_expiration_time_in_minutes(self):
        """
        Gets the max_token_expiration_time_in_minutes of this AndroidChannel.
        The maximum time until the token expires (in minutes).


        :return: The max_token_expiration_time_in_minutes of this AndroidChannel.
        :rtype: int
        """
        return self._max_token_expiration_time_in_minutes

    @max_token_expiration_time_in_minutes.setter
    def max_token_expiration_time_in_minutes(self, max_token_expiration_time_in_minutes):
        """
        Sets the max_token_expiration_time_in_minutes of this AndroidChannel.
        The maximum time until the token expires (in minutes).


        :param max_token_expiration_time_in_minutes: The max_token_expiration_time_in_minutes of this AndroidChannel.
        :type: int
        """
        self._max_token_expiration_time_in_minutes = max_token_expiration_time_in_minutes

    @property
    def is_client_authentication_enabled(self):
        """
        **[Required]** Gets the is_client_authentication_enabled of this AndroidChannel.
        Whether client authentication is enabled or not.


        :return: The is_client_authentication_enabled of this AndroidChannel.
        :rtype: bool
        """
        return self._is_client_authentication_enabled

    @is_client_authentication_enabled.setter
    def is_client_authentication_enabled(self, is_client_authentication_enabled):
        """
        Sets the is_client_authentication_enabled of this AndroidChannel.
        Whether client authentication is enabled or not.


        :param is_client_authentication_enabled: The is_client_authentication_enabled of this AndroidChannel.
        :type: bool
        """
        self._is_client_authentication_enabled = is_client_authentication_enabled

    @property
    def bot_id(self):
        """
        Gets the bot_id of this AndroidChannel.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this AndroidChannel.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this AndroidChannel.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this AndroidChannel.
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
