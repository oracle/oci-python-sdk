# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_channel_result import CreateChannelResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOSSChannelResult(CreateChannelResult):
    """
    The configuration for an Oracle Streaming Service (OSS) channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOSSChannelResult object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateOSSChannelResult.type` attribute
        of this class is ``OSS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CreateOSSChannelResult.
        :type id: str

        :param name:
            The value to assign to the name property of this CreateOSSChannelResult.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateOSSChannelResult.
        :type description: str

        :param category:
            The value to assign to the category property of this CreateOSSChannelResult.
            Allowed values for this property are: "AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"
        :type category: str

        :param type:
            The value to assign to the type property of this CreateOSSChannelResult.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateOSSChannelResult.
        :type session_expiry_duration_in_milliseconds: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateOSSChannelResult.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this CreateOSSChannelResult.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CreateOSSChannelResult.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOSSChannelResult.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOSSChannelResult.
        :type defined_tags: dict(str, dict(str, object))

        :param event_sink_bot_ids:
            The value to assign to the event_sink_bot_ids property of this CreateOSSChannelResult.
        :type event_sink_bot_ids: list[str]

        :param inbound_message_topic:
            The value to assign to the inbound_message_topic property of this CreateOSSChannelResult.
        :type inbound_message_topic: str

        :param outbound_message_topic:
            The value to assign to the outbound_message_topic property of this CreateOSSChannelResult.
        :type outbound_message_topic: str

        :param bootstrap_servers:
            The value to assign to the bootstrap_servers property of this CreateOSSChannelResult.
        :type bootstrap_servers: str

        :param security_protocol:
            The value to assign to the security_protocol property of this CreateOSSChannelResult.
        :type security_protocol: str

        :param sasl_mechanism:
            The value to assign to the sasl_mechanism property of this CreateOSSChannelResult.
        :type sasl_mechanism: str

        :param tenancy_name:
            The value to assign to the tenancy_name property of this CreateOSSChannelResult.
        :type tenancy_name: str

        :param user_name:
            The value to assign to the user_name property of this CreateOSSChannelResult.
        :type user_name: str

        :param stream_pool_id:
            The value to assign to the stream_pool_id property of this CreateOSSChannelResult.
        :type stream_pool_id: str

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
            'event_sink_bot_ids': 'list[str]',
            'inbound_message_topic': 'str',
            'outbound_message_topic': 'str',
            'bootstrap_servers': 'str',
            'security_protocol': 'str',
            'sasl_mechanism': 'str',
            'tenancy_name': 'str',
            'user_name': 'str',
            'stream_pool_id': 'str'
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
            'event_sink_bot_ids': 'eventSinkBotIds',
            'inbound_message_topic': 'inboundMessageTopic',
            'outbound_message_topic': 'outboundMessageTopic',
            'bootstrap_servers': 'bootstrapServers',
            'security_protocol': 'securityProtocol',
            'sasl_mechanism': 'saslMechanism',
            'tenancy_name': 'tenancyName',
            'user_name': 'userName',
            'stream_pool_id': 'streamPoolId'
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
        self._event_sink_bot_ids = None
        self._inbound_message_topic = None
        self._outbound_message_topic = None
        self._bootstrap_servers = None
        self._security_protocol = None
        self._sasl_mechanism = None
        self._tenancy_name = None
        self._user_name = None
        self._stream_pool_id = None
        self._type = 'OSS'

    @property
    def event_sink_bot_ids(self):
        """
        Gets the event_sink_bot_ids of this CreateOSSChannelResult.
        The IDs of the Skills and Digital Assistants that the Channel is routed to.


        :return: The event_sink_bot_ids of this CreateOSSChannelResult.
        :rtype: list[str]
        """
        return self._event_sink_bot_ids

    @event_sink_bot_ids.setter
    def event_sink_bot_ids(self, event_sink_bot_ids):
        """
        Sets the event_sink_bot_ids of this CreateOSSChannelResult.
        The IDs of the Skills and Digital Assistants that the Channel is routed to.


        :param event_sink_bot_ids: The event_sink_bot_ids of this CreateOSSChannelResult.
        :type: list[str]
        """
        self._event_sink_bot_ids = event_sink_bot_ids

    @property
    def inbound_message_topic(self):
        """
        **[Required]** Gets the inbound_message_topic of this CreateOSSChannelResult.
        The topic inbound messages are received on.


        :return: The inbound_message_topic of this CreateOSSChannelResult.
        :rtype: str
        """
        return self._inbound_message_topic

    @inbound_message_topic.setter
    def inbound_message_topic(self, inbound_message_topic):
        """
        Sets the inbound_message_topic of this CreateOSSChannelResult.
        The topic inbound messages are received on.


        :param inbound_message_topic: The inbound_message_topic of this CreateOSSChannelResult.
        :type: str
        """
        self._inbound_message_topic = inbound_message_topic

    @property
    def outbound_message_topic(self):
        """
        **[Required]** Gets the outbound_message_topic of this CreateOSSChannelResult.
        The topic outbound messages are sent on.


        :return: The outbound_message_topic of this CreateOSSChannelResult.
        :rtype: str
        """
        return self._outbound_message_topic

    @outbound_message_topic.setter
    def outbound_message_topic(self, outbound_message_topic):
        """
        Sets the outbound_message_topic of this CreateOSSChannelResult.
        The topic outbound messages are sent on.


        :param outbound_message_topic: The outbound_message_topic of this CreateOSSChannelResult.
        :type: str
        """
        self._outbound_message_topic = outbound_message_topic

    @property
    def bootstrap_servers(self):
        """
        **[Required]** Gets the bootstrap_servers of this CreateOSSChannelResult.
        The Oracle Streaming Service bootstrap servers.


        :return: The bootstrap_servers of this CreateOSSChannelResult.
        :rtype: str
        """
        return self._bootstrap_servers

    @bootstrap_servers.setter
    def bootstrap_servers(self, bootstrap_servers):
        """
        Sets the bootstrap_servers of this CreateOSSChannelResult.
        The Oracle Streaming Service bootstrap servers.


        :param bootstrap_servers: The bootstrap_servers of this CreateOSSChannelResult.
        :type: str
        """
        self._bootstrap_servers = bootstrap_servers

    @property
    def security_protocol(self):
        """
        **[Required]** Gets the security_protocol of this CreateOSSChannelResult.
        The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.


        :return: The security_protocol of this CreateOSSChannelResult.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this CreateOSSChannelResult.
        The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.


        :param security_protocol: The security_protocol of this CreateOSSChannelResult.
        :type: str
        """
        self._security_protocol = security_protocol

    @property
    def sasl_mechanism(self):
        """
        **[Required]** Gets the sasl_mechanism of this CreateOSSChannelResult.
        The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.


        :return: The sasl_mechanism of this CreateOSSChannelResult.
        :rtype: str
        """
        return self._sasl_mechanism

    @sasl_mechanism.setter
    def sasl_mechanism(self, sasl_mechanism):
        """
        Sets the sasl_mechanism of this CreateOSSChannelResult.
        The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.


        :param sasl_mechanism: The sasl_mechanism of this CreateOSSChannelResult.
        :type: str
        """
        self._sasl_mechanism = sasl_mechanism

    @property
    def tenancy_name(self):
        """
        **[Required]** Gets the tenancy_name of this CreateOSSChannelResult.
        The tenancy to use when connecting to the Oracle Streaming Service.


        :return: The tenancy_name of this CreateOSSChannelResult.
        :rtype: str
        """
        return self._tenancy_name

    @tenancy_name.setter
    def tenancy_name(self, tenancy_name):
        """
        Sets the tenancy_name of this CreateOSSChannelResult.
        The tenancy to use when connecting to the Oracle Streaming Service.


        :param tenancy_name: The tenancy_name of this CreateOSSChannelResult.
        :type: str
        """
        self._tenancy_name = tenancy_name

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this CreateOSSChannelResult.
        The user name to use when connecting to the Oracle Streaming Service.


        :return: The user_name of this CreateOSSChannelResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this CreateOSSChannelResult.
        The user name to use when connecting to the Oracle Streaming Service.


        :param user_name: The user_name of this CreateOSSChannelResult.
        :type: str
        """
        self._user_name = user_name

    @property
    def stream_pool_id(self):
        """
        **[Required]** Gets the stream_pool_id of this CreateOSSChannelResult.
        The stream pool OCI to use when connecting to the Oracle Streaming Service.


        :return: The stream_pool_id of this CreateOSSChannelResult.
        :rtype: str
        """
        return self._stream_pool_id

    @stream_pool_id.setter
    def stream_pool_id(self, stream_pool_id):
        """
        Sets the stream_pool_id of this CreateOSSChannelResult.
        The stream pool OCI to use when connecting to the Oracle Streaming Service.


        :param stream_pool_id: The stream_pool_id of this CreateOSSChannelResult.
        :type: str
        """
        self._stream_pool_id = stream_pool_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
