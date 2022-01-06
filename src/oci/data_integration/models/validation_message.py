# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidationMessage(object):
    """
    The level, message key, and validation message.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidationMessage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level:
            The value to assign to the level property of this ValidationMessage.
        :type level: str

        :param message_key:
            The value to assign to the message_key property of this ValidationMessage.
        :type message_key: str

        :param validation_message:
            The value to assign to the validation_message property of this ValidationMessage.
        :type validation_message: str

        """
        self.swagger_types = {
            'level': 'str',
            'message_key': 'str',
            'validation_message': 'str'
        }

        self.attribute_map = {
            'level': 'level',
            'message_key': 'messageKey',
            'validation_message': 'validationMessage'
        }

        self._level = None
        self._message_key = None
        self._validation_message = None

    @property
    def level(self):
        """
        Gets the level of this ValidationMessage.
        The total number of validation messages.


        :return: The level of this ValidationMessage.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this ValidationMessage.
        The total number of validation messages.


        :param level: The level of this ValidationMessage.
        :type: str
        """
        self._level = level

    @property
    def message_key(self):
        """
        Gets the message_key of this ValidationMessage.
        The validation message key.


        :return: The message_key of this ValidationMessage.
        :rtype: str
        """
        return self._message_key

    @message_key.setter
    def message_key(self, message_key):
        """
        Sets the message_key of this ValidationMessage.
        The validation message key.


        :param message_key: The message_key of this ValidationMessage.
        :type: str
        """
        self._message_key = message_key

    @property
    def validation_message(self):
        """
        Gets the validation_message of this ValidationMessage.
        The validation message.


        :return: The validation_message of this ValidationMessage.
        :rtype: str
        """
        return self._validation_message

    @validation_message.setter
    def validation_message(self, validation_message):
        """
        Sets the validation_message of this ValidationMessage.
        The validation message.


        :param validation_message: The validation_message of this ValidationMessage.
        :type: str
        """
        self._validation_message = validation_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
