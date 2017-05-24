# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class WorkRequestError(object):

    def __init__(self):

        self.swagger_types = {
            'error_code': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'message': 'message'
        }

        self._error_code = None
        self._message = None

    @property
    def error_code(self):
        """
        Gets the error_code of this WorkRequestError.
        Allowed values for this property are: "BAD_INPUT", "INTERNAL_ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The error_code of this WorkRequestError.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this WorkRequestError.

        :param error_code: The error_code of this WorkRequestError.
        :type: str
        """
        allowed_values = ["BAD_INPUT", "INTERNAL_ERROR"]
        if error_code not in allowed_values:
            error_code = 'UNKNOWN_ENUM_VALUE'
        self._error_code = error_code

    @property
    def message(self):
        """
        Gets the message of this WorkRequestError.
        A human-readable error string.


        :return: The message of this WorkRequestError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequestError.
        A human-readable error string.


        :param message: The message of this WorkRequestError.
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
