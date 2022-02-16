# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Message(object):
    """
    The details of a message.
    """

    #: A constant which can be used with the type property of a Message.
    #: This constant has a value of "ERROR"
    TYPE_ERROR = "ERROR"

    #: A constant which can be used with the type property of a Message.
    #: This constant has a value of "WARNING"
    TYPE_WARNING = "WARNING"

    #: A constant which can be used with the type property of a Message.
    #: This constant has a value of "INFO"
    TYPE_INFO = "INFO"

    def __init__(self, **kwargs):
        """
        Initializes a new Message object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Message.
            Allowed values for this property are: "ERROR", "WARNING", "INFO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param code:
            The value to assign to the code property of this Message.
        :type code: str

        :param message:
            The value to assign to the message property of this Message.
        :type message: str

        """
        self.swagger_types = {
            'type': 'str',
            'code': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'code': 'code',
            'message': 'message'
        }

        self._type = None
        self._code = None
        self._message = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Message.
        The type of message (error, warning, or info).

        Allowed values for this property are: "ERROR", "WARNING", "INFO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Message.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Message.
        The type of message (error, warning, or info).


        :param type: The type of this Message.
        :type: str
        """
        allowed_values = ["ERROR", "WARNING", "INFO"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def code(self):
        """
        **[Required]** Gets the code of this Message.
        The message code.


        :return: The code of this Message.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Message.
        The message code.


        :param code: The code of this Message.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this Message.
        The message text.


        :return: The message of this Message.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Message.
        The message text.


        :param message: The message of this Message.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
