# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .channel import Channel
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TwilioChannel(Channel):
    """
    The configuration for a Twilio channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TwilioChannel object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.TwilioChannel.type` attribute
        of this class is ``TWILIO`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TwilioChannel.
        :type id: str

        :param name:
            The value to assign to the name property of this TwilioChannel.
        :type name: str

        :param description:
            The value to assign to the description property of this TwilioChannel.
        :type description: str

        :param category:
            The value to assign to the category property of this TwilioChannel.
            Allowed values for this property are: "AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"
        :type category: str

        :param type:
            The value to assign to the type property of this TwilioChannel.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this TwilioChannel.
        :type session_expiry_duration_in_milliseconds: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TwilioChannel.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this TwilioChannel.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TwilioChannel.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TwilioChannel.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TwilioChannel.
        :type defined_tags: dict(str, dict(str, object))

        :param account_sid:
            The value to assign to the account_sid property of this TwilioChannel.
        :type account_sid: str

        :param phone_number:
            The value to assign to the phone_number property of this TwilioChannel.
        :type phone_number: str

        :param is_mms_enabled:
            The value to assign to the is_mms_enabled property of this TwilioChannel.
        :type is_mms_enabled: bool

        :param original_connectors_url:
            The value to assign to the original_connectors_url property of this TwilioChannel.
        :type original_connectors_url: str

        :param bot_id:
            The value to assign to the bot_id property of this TwilioChannel.
        :type bot_id: str

        :param webhook_url:
            The value to assign to the webhook_url property of this TwilioChannel.
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
            'account_sid': 'str',
            'phone_number': 'str',
            'is_mms_enabled': 'bool',
            'original_connectors_url': 'str',
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
            'account_sid': 'accountSID',
            'phone_number': 'phoneNumber',
            'is_mms_enabled': 'isMmsEnabled',
            'original_connectors_url': 'originalConnectorsUrl',
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
        self._account_sid = None
        self._phone_number = None
        self._is_mms_enabled = None
        self._original_connectors_url = None
        self._bot_id = None
        self._webhook_url = None
        self._type = 'TWILIO'

    @property
    def account_sid(self):
        """
        **[Required]** Gets the account_sid of this TwilioChannel.
        The Account SID for the Twilio number.


        :return: The account_sid of this TwilioChannel.
        :rtype: str
        """
        return self._account_sid

    @account_sid.setter
    def account_sid(self, account_sid):
        """
        Sets the account_sid of this TwilioChannel.
        The Account SID for the Twilio number.


        :param account_sid: The account_sid of this TwilioChannel.
        :type: str
        """
        self._account_sid = account_sid

    @property
    def phone_number(self):
        """
        **[Required]** Gets the phone_number of this TwilioChannel.
        The Twilio phone number.


        :return: The phone_number of this TwilioChannel.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this TwilioChannel.
        The Twilio phone number.


        :param phone_number: The phone_number of this TwilioChannel.
        :type: str
        """
        self._phone_number = phone_number

    @property
    def is_mms_enabled(self):
        """
        **[Required]** Gets the is_mms_enabled of this TwilioChannel.
        Whether MMS is enabled for this channel or not.


        :return: The is_mms_enabled of this TwilioChannel.
        :rtype: bool
        """
        return self._is_mms_enabled

    @is_mms_enabled.setter
    def is_mms_enabled(self, is_mms_enabled):
        """
        Sets the is_mms_enabled of this TwilioChannel.
        Whether MMS is enabled for this channel or not.


        :param is_mms_enabled: The is_mms_enabled of this TwilioChannel.
        :type: bool
        """
        self._is_mms_enabled = is_mms_enabled

    @property
    def original_connectors_url(self):
        """
        Gets the original_connectors_url of this TwilioChannel.
        The original connectors URL (used for backward compatibility).


        :return: The original_connectors_url of this TwilioChannel.
        :rtype: str
        """
        return self._original_connectors_url

    @original_connectors_url.setter
    def original_connectors_url(self, original_connectors_url):
        """
        Sets the original_connectors_url of this TwilioChannel.
        The original connectors URL (used for backward compatibility).


        :param original_connectors_url: The original_connectors_url of this TwilioChannel.
        :type: str
        """
        self._original_connectors_url = original_connectors_url

    @property
    def bot_id(self):
        """
        Gets the bot_id of this TwilioChannel.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this TwilioChannel.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this TwilioChannel.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this TwilioChannel.
        :type: str
        """
        self._bot_id = bot_id

    @property
    def webhook_url(self):
        """
        **[Required]** Gets the webhook_url of this TwilioChannel.
        The URL to use to send messages to this channel.
        This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.


        :return: The webhook_url of this TwilioChannel.
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """
        Sets the webhook_url of this TwilioChannel.
        The URL to use to send messages to this channel.
        This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.


        :param webhook_url: The webhook_url of this TwilioChannel.
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
