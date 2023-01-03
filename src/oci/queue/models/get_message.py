# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GetMessage(object):
    """
    A message consumed from a queue.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GetMessage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GetMessage.
        :type id: int

        :param content:
            The value to assign to the content property of this GetMessage.
        :type content: str

        :param receipt:
            The value to assign to the receipt property of this GetMessage.
        :type receipt: str

        :param delivery_count:
            The value to assign to the delivery_count property of this GetMessage.
        :type delivery_count: int

        :param visible_after:
            The value to assign to the visible_after property of this GetMessage.
        :type visible_after: datetime

        :param expire_after:
            The value to assign to the expire_after property of this GetMessage.
        :type expire_after: datetime

        """
        self.swagger_types = {
            'id': 'int',
            'content': 'str',
            'receipt': 'str',
            'delivery_count': 'int',
            'visible_after': 'datetime',
            'expire_after': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'content': 'content',
            'receipt': 'receipt',
            'delivery_count': 'deliveryCount',
            'visible_after': 'visibleAfter',
            'expire_after': 'expireAfter'
        }

        self._id = None
        self._content = None
        self._receipt = None
        self._delivery_count = None
        self._visible_after = None
        self._expire_after = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this GetMessage.
        The id of the message - this is only used for tracing and debugging purposes and isn't used as a parameter in any request.


        :return: The id of this GetMessage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GetMessage.
        The id of the message - this is only used for tracing and debugging purposes and isn't used as a parameter in any request.


        :param id: The id of this GetMessage.
        :type: int
        """
        self._id = id

    @property
    def content(self):
        """
        **[Required]** Gets the content of this GetMessage.
        The content of the message


        :return: The content of this GetMessage.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this GetMessage.
        The content of the message


        :param content: The content of this GetMessage.
        :type: str
        """
        self._content = content

    @property
    def receipt(self):
        """
        **[Required]** Gets the receipt of this GetMessage.
        A receipt is a base64urlencode opaque token, uniquely representing a message.
        The receipt can be used to delete a message or update its visibility.


        :return: The receipt of this GetMessage.
        :rtype: str
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """
        Sets the receipt of this GetMessage.
        A receipt is a base64urlencode opaque token, uniquely representing a message.
        The receipt can be used to delete a message or update its visibility.


        :param receipt: The receipt of this GetMessage.
        :type: str
        """
        self._receipt = receipt

    @property
    def delivery_count(self):
        """
        **[Required]** Gets the delivery_count of this GetMessage.
        The number of time the message has been delivered to a consumer.


        :return: The delivery_count of this GetMessage.
        :rtype: int
        """
        return self._delivery_count

    @delivery_count.setter
    def delivery_count(self, delivery_count):
        """
        Sets the delivery_count of this GetMessage.
        The number of time the message has been delivered to a consumer.


        :param delivery_count: The delivery_count of this GetMessage.
        :type: int
        """
        self._delivery_count = delivery_count

    @property
    def visible_after(self):
        """
        **[Required]** Gets the visible_after of this GetMessage.
        The time after which the message will be visible to other consumers. An RFC3339 formatted datetime string


        :return: The visible_after of this GetMessage.
        :rtype: datetime
        """
        return self._visible_after

    @visible_after.setter
    def visible_after(self, visible_after):
        """
        Sets the visible_after of this GetMessage.
        The time after which the message will be visible to other consumers. An RFC3339 formatted datetime string


        :param visible_after: The visible_after of this GetMessage.
        :type: datetime
        """
        self._visible_after = visible_after

    @property
    def expire_after(self):
        """
        **[Required]** Gets the expire_after of this GetMessage.
        The time after which the message will be automatically deleted. An RFC3339 formatted datetime string


        :return: The expire_after of this GetMessage.
        :rtype: datetime
        """
        return self._expire_after

    @expire_after.setter
    def expire_after(self, expire_after):
        """
        Sets the expire_after of this GetMessage.
        The time after which the message will be automatically deleted. An RFC3339 formatted datetime string


        :param expire_after: The expire_after of this GetMessage.
        :type: datetime
        """
        self._expire_after = expire_after

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
