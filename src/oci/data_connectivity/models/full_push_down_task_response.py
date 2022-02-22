# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FullPushDownTaskResponse(object):
    """
    The full pushdown task
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FullPushDownTaskResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this FullPushDownTaskResponse.
        :type model_type: str

        :param error_message:
            The value to assign to the error_message property of this FullPushDownTaskResponse.
        :type error_message: str

        :param status:
            The value to assign to the status property of this FullPushDownTaskResponse.
        :type status: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'error_message': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'error_message': 'errorMessage',
            'status': 'status'
        }

        self._model_type = None
        self._error_message = None
        self._status = None

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this FullPushDownTaskResponse.
        The type of of FullPushDownTask Response.


        :return: The model_type of this FullPushDownTaskResponse.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this FullPushDownTaskResponse.
        The type of of FullPushDownTask Response.


        :param model_type: The model_type of this FullPushDownTaskResponse.
        :type: str
        """
        self._model_type = model_type

    @property
    def error_message(self):
        """
        Gets the error_message of this FullPushDownTaskResponse.
        The error message in response object.


        :return: The error_message of this FullPushDownTaskResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this FullPushDownTaskResponse.
        The error message in response object.


        :param error_message: The error_message of this FullPushDownTaskResponse.
        :type: str
        """
        self._error_message = error_message

    @property
    def status(self):
        """
        Gets the status of this FullPushDownTaskResponse.
        The status of FullPushDownTask.


        :return: The status of this FullPushDownTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FullPushDownTaskResponse.
        The status of FullPushDownTask.


        :param status: The status of this FullPushDownTaskResponse.
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
