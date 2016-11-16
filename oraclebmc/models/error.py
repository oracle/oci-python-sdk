# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.


from ..util import formatted_flat_dict


class Error(object):

    def __init__(self):

        self.swagger_types = {
            'code': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = None
        self._message = None

    @property
    def code(self):
        """
        Gets the code of this Error.
        A short error code that defines the error, meant for programmatic parsing.

        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Error.
        A short error code that defines the error, meant for programmatic parsing.

        :param code: The code of this Error.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        Gets the message of this Error.
        A human-readable error string.

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Error.
        A human-readable error string.

        :param message: The message of this Error.
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
