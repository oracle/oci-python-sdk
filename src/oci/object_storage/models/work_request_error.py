# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestError(object):
    """
    WorkRequestError model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestError object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this WorkRequestError.
        :type code: str

        :param message:
            The value to assign to the message property of this WorkRequestError.
        :type message: str

        :param timestamp:
            The value to assign to the timestamp property of this WorkRequestError.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'timestamp': 'timestamp'
        }

        self._code = None
        self._message = None
        self._timestamp = None

    @property
    def code(self):
        """
        Gets the code of this WorkRequestError.
        A machine-usable code for the error that occured. Error codes are listed on
        (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm)


        :return: The code of this WorkRequestError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this WorkRequestError.
        A machine-usable code for the error that occured. Error codes are listed on
        (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm)


        :param code: The code of this WorkRequestError.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        Gets the message of this WorkRequestError.
        A human readable description of the issue encountered.


        :return: The message of this WorkRequestError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequestError.
        A human readable description of the issue encountered.


        :param message: The message of this WorkRequestError.
        :type: str
        """
        self._message = message

    @property
    def timestamp(self):
        """
        Gets the timestamp of this WorkRequestError.
        The time the error happened


        :return: The timestamp of this WorkRequestError.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this WorkRequestError.
        The time the error happened


        :param timestamp: The timestamp of this WorkRequestError.
        :type: datetime
        """
        self._timestamp = timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
