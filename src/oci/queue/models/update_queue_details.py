# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateQueueDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateQueueDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateQueueDetails.
        :type display_name: str

        :param visibility_in_seconds:
            The value to assign to the visibility_in_seconds property of this UpdateQueueDetails.
        :type visibility_in_seconds: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this UpdateQueueDetails.
        :type timeout_in_seconds: int

        :param dead_letter_queue_delivery_count:
            The value to assign to the dead_letter_queue_delivery_count property of this UpdateQueueDetails.
        :type dead_letter_queue_delivery_count: int

        :param custom_encryption_key_id:
            The value to assign to the custom_encryption_key_id property of this UpdateQueueDetails.
        :type custom_encryption_key_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateQueueDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateQueueDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'visibility_in_seconds': 'int',
            'timeout_in_seconds': 'int',
            'dead_letter_queue_delivery_count': 'int',
            'custom_encryption_key_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'visibility_in_seconds': 'visibilityInSeconds',
            'timeout_in_seconds': 'timeoutInSeconds',
            'dead_letter_queue_delivery_count': 'deadLetterQueueDeliveryCount',
            'custom_encryption_key_id': 'customEncryptionKeyId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._visibility_in_seconds = None
        self._timeout_in_seconds = None
        self._dead_letter_queue_delivery_count = None
        self._custom_encryption_key_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateQueueDetails.
        Queue Identifier


        :return: The display_name of this UpdateQueueDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateQueueDetails.
        Queue Identifier


        :param display_name: The display_name of this UpdateQueueDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def visibility_in_seconds(self):
        """
        Gets the visibility_in_seconds of this UpdateQueueDetails.
        The default visibility of the messages consumed from the queue.


        :return: The visibility_in_seconds of this UpdateQueueDetails.
        :rtype: int
        """
        return self._visibility_in_seconds

    @visibility_in_seconds.setter
    def visibility_in_seconds(self, visibility_in_seconds):
        """
        Sets the visibility_in_seconds of this UpdateQueueDetails.
        The default visibility of the messages consumed from the queue.


        :param visibility_in_seconds: The visibility_in_seconds of this UpdateQueueDetails.
        :type: int
        """
        self._visibility_in_seconds = visibility_in_seconds

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this UpdateQueueDetails.
        The default polling timeout of the messages in the queue, in seconds.


        :return: The timeout_in_seconds of this UpdateQueueDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this UpdateQueueDetails.
        The default polling timeout of the messages in the queue, in seconds.


        :param timeout_in_seconds: The timeout_in_seconds of this UpdateQueueDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def dead_letter_queue_delivery_count(self):
        """
        Gets the dead_letter_queue_delivery_count of this UpdateQueueDetails.
        The number of times a message can be delivered to a consumer before being moved to the dead letter queue.
        A value of 0 indicates that the DLQ is not used.
        Changing that value to a lower threshold does not retro-actively move in-flight messages in the dead letter queue.


        :return: The dead_letter_queue_delivery_count of this UpdateQueueDetails.
        :rtype: int
        """
        return self._dead_letter_queue_delivery_count

    @dead_letter_queue_delivery_count.setter
    def dead_letter_queue_delivery_count(self, dead_letter_queue_delivery_count):
        """
        Sets the dead_letter_queue_delivery_count of this UpdateQueueDetails.
        The number of times a message can be delivered to a consumer before being moved to the dead letter queue.
        A value of 0 indicates that the DLQ is not used.
        Changing that value to a lower threshold does not retro-actively move in-flight messages in the dead letter queue.


        :param dead_letter_queue_delivery_count: The dead_letter_queue_delivery_count of this UpdateQueueDetails.
        :type: int
        """
        self._dead_letter_queue_delivery_count = dead_letter_queue_delivery_count

    @property
    def custom_encryption_key_id(self):
        """
        Gets the custom_encryption_key_id of this UpdateQueueDetails.
        Id of the custom master encryption key which will be used to encrypt messages content. String of length 0 means the custom key should be removed from queue


        :return: The custom_encryption_key_id of this UpdateQueueDetails.
        :rtype: str
        """
        return self._custom_encryption_key_id

    @custom_encryption_key_id.setter
    def custom_encryption_key_id(self, custom_encryption_key_id):
        """
        Sets the custom_encryption_key_id of this UpdateQueueDetails.
        Id of the custom master encryption key which will be used to encrypt messages content. String of length 0 means the custom key should be removed from queue


        :param custom_encryption_key_id: The custom_encryption_key_id of this UpdateQueueDetails.
        :type: str
        """
        self._custom_encryption_key_id = custom_encryption_key_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateQueueDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateQueueDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateQueueDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateQueueDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateQueueDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateQueueDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateQueueDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateQueueDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
