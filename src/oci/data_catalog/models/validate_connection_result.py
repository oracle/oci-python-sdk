# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidateConnectionResult(object):
    """
    Details regarding the validation of a connection resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidateConnectionResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this ValidateConnectionResult.
        :type message: str

        :param status:
            The value to assign to the status property of this ValidateConnectionResult.
        :type status: str

        """
        self.swagger_types = {
            'message': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'message': 'message',
            'status': 'status'
        }

        self._message = None
        self._status = None

    @property
    def message(self):
        """
        Gets the message of this ValidateConnectionResult.
        The message from the connection validation.


        :return: The message of this ValidateConnectionResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ValidateConnectionResult.
        The message from the connection validation.


        :param message: The message of this ValidateConnectionResult.
        :type: str
        """
        self._message = message

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ValidateConnectionResult.
        The status returned from the connection validation.


        :return: The status of this ValidateConnectionResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ValidateConnectionResult.
        The status returned from the connection validation.


        :param status: The status of this ValidateConnectionResult.
        :type: str
        """
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
