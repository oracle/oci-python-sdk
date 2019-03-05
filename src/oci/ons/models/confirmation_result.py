# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfirmationResult(object):
    """
    The confirmation result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfirmationResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param topic_name:
            The value to assign to the topic_name property of this ConfirmationResult.
        :type topic_name: str

        :param topic_id:
            The value to assign to the topic_id property of this ConfirmationResult.
        :type topic_id: str

        :param endpoint:
            The value to assign to the endpoint property of this ConfirmationResult.
        :type endpoint: str

        :param unsubscribe_url:
            The value to assign to the unsubscribe_url property of this ConfirmationResult.
        :type unsubscribe_url: str

        :param message:
            The value to assign to the message property of this ConfirmationResult.
        :type message: str

        :param subscription_id:
            The value to assign to the subscription_id property of this ConfirmationResult.
        :type subscription_id: str

        """
        self.swagger_types = {
            'topic_name': 'str',
            'topic_id': 'str',
            'endpoint': 'str',
            'unsubscribe_url': 'str',
            'message': 'str',
            'subscription_id': 'str'
        }

        self.attribute_map = {
            'topic_name': 'topicName',
            'topic_id': 'topicId',
            'endpoint': 'endpoint',
            'unsubscribe_url': 'unsubscribeUrl',
            'message': 'message',
            'subscription_id': 'subscriptionId'
        }

        self._topic_name = None
        self._topic_id = None
        self._endpoint = None
        self._unsubscribe_url = None
        self._message = None
        self._subscription_id = None

    @property
    def topic_name(self):
        """
        **[Required]** Gets the topic_name of this ConfirmationResult.
        The name of the subscribed topic.


        :return: The topic_name of this ConfirmationResult.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """
        Sets the topic_name of this ConfirmationResult.
        The name of the subscribed topic.


        :param topic_name: The topic_name of this ConfirmationResult.
        :type: str
        """
        self._topic_name = topic_name

    @property
    def topic_id(self):
        """
        **[Required]** Gets the topic_id of this ConfirmationResult.
        The `OCID`__ of the topic to delete.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The topic_id of this ConfirmationResult.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """
        Sets the topic_id of this ConfirmationResult.
        The `OCID`__ of the topic to delete.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param topic_id: The topic_id of this ConfirmationResult.
        :type: str
        """
        self._topic_id = topic_id

    @property
    def endpoint(self):
        """
        **[Required]** Gets the endpoint of this ConfirmationResult.
        The endpoint of the subscription. Valid values depend on the protocol.
        For EMAIL, only an email address is valid. For HTTPS, only a PagerDuty URL is valid. A URL cannot exceed 512 characters.
        Avoid entering confidential information.


        :return: The endpoint of this ConfirmationResult.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this ConfirmationResult.
        The endpoint of the subscription. Valid values depend on the protocol.
        For EMAIL, only an email address is valid. For HTTPS, only a PagerDuty URL is valid. A URL cannot exceed 512 characters.
        Avoid entering confidential information.


        :param endpoint: The endpoint of this ConfirmationResult.
        :type: str
        """
        self._endpoint = endpoint

    @property
    def unsubscribe_url(self):
        """
        **[Required]** Gets the unsubscribe_url of this ConfirmationResult.
        The URL user can use to unsubscribe the topic.


        :return: The unsubscribe_url of this ConfirmationResult.
        :rtype: str
        """
        return self._unsubscribe_url

    @unsubscribe_url.setter
    def unsubscribe_url(self, unsubscribe_url):
        """
        Sets the unsubscribe_url of this ConfirmationResult.
        The URL user can use to unsubscribe the topic.


        :param unsubscribe_url: The unsubscribe_url of this ConfirmationResult.
        :type: str
        """
        self._unsubscribe_url = unsubscribe_url

    @property
    def message(self):
        """
        **[Required]** Gets the message of this ConfirmationResult.
        Human readable text which tells the user if the confirmation succeeds.


        :return: The message of this ConfirmationResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ConfirmationResult.
        Human readable text which tells the user if the confirmation succeeds.


        :param message: The message of this ConfirmationResult.
        :type: str
        """
        self._message = message

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this ConfirmationResult.
        The `OCID`__ of the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subscription_id of this ConfirmationResult.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this ConfirmationResult.
        The `OCID`__ of the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subscription_id: The subscription_id of this ConfirmationResult.
        :type: str
        """
        self._subscription_id = subscription_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
