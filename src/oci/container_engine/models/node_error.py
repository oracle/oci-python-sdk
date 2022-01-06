# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeError(object):
    """
    The properties that define an upstream error while managing a node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeError object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this NodeError.
        :type code: str

        :param message:
            The value to assign to the message property of this NodeError.
        :type message: str

        :param status:
            The value to assign to the status property of this NodeError.
        :type status: str

        :param opc_request_id:
            The value to assign to the opc_request_id property of this NodeError.
        :type opc_request_id: str

        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str',
            'status': 'str',
            'opc_request_id': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'status': 'status',
            'opc_request_id': 'opc-request-id'
        }

        self._code = None
        self._message = None
        self._status = None
        self._opc_request_id = None

    @property
    def code(self):
        """
        **[Required]** Gets the code of this NodeError.
        A short error code that defines the upstream error, meant for programmatic parsing. See `API Errors`__.

        __ https://docs.cloud.oracle.com/Content/API/References/apierrors.htm


        :return: The code of this NodeError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this NodeError.
        A short error code that defines the upstream error, meant for programmatic parsing. See `API Errors`__.

        __ https://docs.cloud.oracle.com/Content/API/References/apierrors.htm


        :param code: The code of this NodeError.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this NodeError.
        A human-readable error string of the upstream error.


        :return: The message of this NodeError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this NodeError.
        A human-readable error string of the upstream error.


        :param message: The message of this NodeError.
        :type: str
        """
        self._message = message

    @property
    def status(self):
        """
        Gets the status of this NodeError.
        The status of the HTTP response encountered in the upstream error.


        :return: The status of this NodeError.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NodeError.
        The status of the HTTP response encountered in the upstream error.


        :param status: The status of this NodeError.
        :type: str
        """
        self._status = status

    @property
    def opc_request_id(self):
        """
        Gets the opc_request_id of this NodeError.
        Unique Oracle-assigned identifier for the upstream request. If you need to contact Oracle about a particular upstream request, please provide the request ID.


        :return: The opc_request_id of this NodeError.
        :rtype: str
        """
        return self._opc_request_id

    @opc_request_id.setter
    def opc_request_id(self, opc_request_id):
        """
        Sets the opc_request_id of this NodeError.
        Unique Oracle-assigned identifier for the upstream request. If you need to contact Oracle about a particular upstream request, please provide the request ID.


        :param opc_request_id: The opc_request_id of this NodeError.
        :type: str
        """
        self._opc_request_id = opc_request_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
