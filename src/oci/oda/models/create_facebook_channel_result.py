# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_channel_result import CreateChannelResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFacebookChannelResult(CreateChannelResult):
    """
    The configuration for a Facebook channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFacebookChannelResult object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateFacebookChannelResult.type` attribute
        of this class is ``FACEBOOK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CreateFacebookChannelResult.
        :type id: str

        :param name:
            The value to assign to the name property of this CreateFacebookChannelResult.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateFacebookChannelResult.
        :type description: str

        :param category:
            The value to assign to the category property of this CreateFacebookChannelResult.
            Allowed values for this property are: "AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"
        :type category: str

        :param type:
            The value to assign to the type property of this CreateFacebookChannelResult.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateFacebookChannelResult.
        :type session_expiry_duration_in_milliseconds: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateFacebookChannelResult.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this CreateFacebookChannelResult.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CreateFacebookChannelResult.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateFacebookChannelResult.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateFacebookChannelResult.
        :type defined_tags: dict(str, dict(str, object))

        :param verify_token:
            The value to assign to the verify_token property of this CreateFacebookChannelResult.
        :type verify_token: str

        :param bot_id:
            The value to assign to the bot_id property of this CreateFacebookChannelResult.
        :type bot_id: str

        :param webhook_url:
            The value to assign to the webhook_url property of this CreateFacebookChannelResult.
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
            'verify_token': 'str',
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
            'verify_token': 'verifyToken',
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
        self._verify_token = None
        self._bot_id = None
        self._webhook_url = None
        self._type = 'FACEBOOK'

    @property
    def verify_token(self):
        """
        **[Required]** Gets the verify_token of this CreateFacebookChannelResult.
        The Facebook verify token.
        This is used by Facebook when verifying the webhook channel.
        This is only returned this once.  If it is lost the keys will need to be rotated to generate a new verify token.


        :return: The verify_token of this CreateFacebookChannelResult.
        :rtype: str
        """
        return self._verify_token

    @verify_token.setter
    def verify_token(self, verify_token):
        """
        Sets the verify_token of this CreateFacebookChannelResult.
        The Facebook verify token.
        This is used by Facebook when verifying the webhook channel.
        This is only returned this once.  If it is lost the keys will need to be rotated to generate a new verify token.


        :param verify_token: The verify_token of this CreateFacebookChannelResult.
        :type: str
        """
        self._verify_token = verify_token

    @property
    def bot_id(self):
        """
        Gets the bot_id of this CreateFacebookChannelResult.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this CreateFacebookChannelResult.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this CreateFacebookChannelResult.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this CreateFacebookChannelResult.
        :type: str
        """
        self._bot_id = bot_id

    @property
    def webhook_url(self):
        """
        **[Required]** Gets the webhook_url of this CreateFacebookChannelResult.
        The URL to use to send messages to this channel.
        This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.


        :return: The webhook_url of this CreateFacebookChannelResult.
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """
        Sets the webhook_url of this CreateFacebookChannelResult.
        The URL to use to send messages to this channel.
        This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.


        :param webhook_url: The webhook_url of this CreateFacebookChannelResult.
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
