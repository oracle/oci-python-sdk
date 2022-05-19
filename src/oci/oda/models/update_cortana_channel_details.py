# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_channel_details import UpdateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCortanaChannelDetails(UpdateChannelDetails):
    """
    Properties to update a Cortana channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCortanaChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.UpdateCortanaChannelDetails.type` attribute
        of this class is ``CORTANA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateCortanaChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this UpdateCortanaChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this UpdateCortanaChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCortanaChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCortanaChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param msa_app_id:
            The value to assign to the msa_app_id property of this UpdateCortanaChannelDetails.
        :type msa_app_id: str

        :param msa_app_password:
            The value to assign to the msa_app_password property of this UpdateCortanaChannelDetails.
        :type msa_app_password: str

        :param bot_id:
            The value to assign to the bot_id property of this UpdateCortanaChannelDetails.
        :type bot_id: str

        """
        self.swagger_types = {
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'msa_app_id': 'str',
            'msa_app_password': 'str',
            'bot_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'msa_app_id': 'msaAppId',
            'msa_app_password': 'msaAppPassword',
            'bot_id': 'botId'
        }

        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._msa_app_id = None
        self._msa_app_password = None
        self._bot_id = None
        self._type = 'CORTANA'

    @property
    def msa_app_id(self):
        """
        Gets the msa_app_id of this UpdateCortanaChannelDetails.
        The Microsoft App ID that you obtained when you created your bot registration in Azure.


        :return: The msa_app_id of this UpdateCortanaChannelDetails.
        :rtype: str
        """
        return self._msa_app_id

    @msa_app_id.setter
    def msa_app_id(self, msa_app_id):
        """
        Sets the msa_app_id of this UpdateCortanaChannelDetails.
        The Microsoft App ID that you obtained when you created your bot registration in Azure.


        :param msa_app_id: The msa_app_id of this UpdateCortanaChannelDetails.
        :type: str
        """
        self._msa_app_id = msa_app_id

    @property
    def msa_app_password(self):
        """
        Gets the msa_app_password of this UpdateCortanaChannelDetails.
        The client secret that you obtained from your bot registration.


        :return: The msa_app_password of this UpdateCortanaChannelDetails.
        :rtype: str
        """
        return self._msa_app_password

    @msa_app_password.setter
    def msa_app_password(self, msa_app_password):
        """
        Sets the msa_app_password of this UpdateCortanaChannelDetails.
        The client secret that you obtained from your bot registration.


        :param msa_app_password: The msa_app_password of this UpdateCortanaChannelDetails.
        :type: str
        """
        self._msa_app_password = msa_app_password

    @property
    def bot_id(self):
        """
        Gets the bot_id of this UpdateCortanaChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this UpdateCortanaChannelDetails.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this UpdateCortanaChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this UpdateCortanaChannelDetails.
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
