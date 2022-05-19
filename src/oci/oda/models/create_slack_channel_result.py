# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_channel_result import CreateChannelResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSlackChannelResult(CreateChannelResult):
    """
    The configuration for a Slack channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSlackChannelResult object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateSlackChannelResult.type` attribute
        of this class is ``SLACK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CreateSlackChannelResult.
        :type id: str

        :param name:
            The value to assign to the name property of this CreateSlackChannelResult.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateSlackChannelResult.
        :type description: str

        :param category:
            The value to assign to the category property of this CreateSlackChannelResult.
            Allowed values for this property are: "AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"
        :type category: str

        :param type:
            The value to assign to the type property of this CreateSlackChannelResult.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateSlackChannelResult.
        :type session_expiry_duration_in_milliseconds: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateSlackChannelResult.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this CreateSlackChannelResult.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CreateSlackChannelResult.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSlackChannelResult.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSlackChannelResult.
        :type defined_tags: dict(str, dict(str, object))

        :param client_id:
            The value to assign to the client_id property of this CreateSlackChannelResult.
        :type client_id: str

        :param auth_success_url:
            The value to assign to the auth_success_url property of this CreateSlackChannelResult.
        :type auth_success_url: str

        :param auth_error_url:
            The value to assign to the auth_error_url property of this CreateSlackChannelResult.
        :type auth_error_url: str

        :param bot_id:
            The value to assign to the bot_id property of this CreateSlackChannelResult.
        :type bot_id: str

        :param webhook_url:
            The value to assign to the webhook_url property of this CreateSlackChannelResult.
        :type webhook_url: str

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
            'client_id': 'str',
            'auth_success_url': 'str',
            'auth_error_url': 'str',
            'bot_id': 'str',
            'webhook_url': 'str'
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
            'client_id': 'clientId',
            'auth_success_url': 'authSuccessUrl',
            'auth_error_url': 'authErrorUrl',
            'bot_id': 'botId',
            'webhook_url': 'webhookUrl'
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
        self._client_id = None
        self._auth_success_url = None
        self._auth_error_url = None
        self._bot_id = None
        self._webhook_url = None
        self._type = 'SLACK'

    @property
    def client_id(self):
        """
        **[Required]** Gets the client_id of this CreateSlackChannelResult.
        The Slack Client Id for the Slack app.


        :return: The client_id of this CreateSlackChannelResult.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CreateSlackChannelResult.
        The Slack Client Id for the Slack app.


        :param client_id: The client_id of this CreateSlackChannelResult.
        :type: str
        """
        self._client_id = client_id

    @property
    def auth_success_url(self):
        """
        Gets the auth_success_url of this CreateSlackChannelResult.
        The URL to redirect to when authentication is successful.


        :return: The auth_success_url of this CreateSlackChannelResult.
        :rtype: str
        """
        return self._auth_success_url

    @auth_success_url.setter
    def auth_success_url(self, auth_success_url):
        """
        Sets the auth_success_url of this CreateSlackChannelResult.
        The URL to redirect to when authentication is successful.


        :param auth_success_url: The auth_success_url of this CreateSlackChannelResult.
        :type: str
        """
        self._auth_success_url = auth_success_url

    @property
    def auth_error_url(self):
        """
        Gets the auth_error_url of this CreateSlackChannelResult.
        The URL to redirect to when authentication is unsuccessful.


        :return: The auth_error_url of this CreateSlackChannelResult.
        :rtype: str
        """
        return self._auth_error_url

    @auth_error_url.setter
    def auth_error_url(self, auth_error_url):
        """
        Sets the auth_error_url of this CreateSlackChannelResult.
        The URL to redirect to when authentication is unsuccessful.


        :param auth_error_url: The auth_error_url of this CreateSlackChannelResult.
        :type: str
        """
        self._auth_error_url = auth_error_url

    @property
    def bot_id(self):
        """
        Gets the bot_id of this CreateSlackChannelResult.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this CreateSlackChannelResult.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this CreateSlackChannelResult.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this CreateSlackChannelResult.
        :type: str
        """
        self._bot_id = bot_id

    @property
    def webhook_url(self):
        """
        **[Required]** Gets the webhook_url of this CreateSlackChannelResult.
        The URL to use to send messages to this channel.
        This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.


        :return: The webhook_url of this CreateSlackChannelResult.
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """
        Sets the webhook_url of this CreateSlackChannelResult.
        The URL to use to send messages to this channel.
        This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.


        :param webhook_url: The webhook_url of this CreateSlackChannelResult.
        :type: str
        """
        self._webhook_url = webhook_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
