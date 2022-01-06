# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestError(object):
    """
    An error encountered while executing a work request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestError object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkRequestError.
        :type id: str

        :param work_request_id:
            The value to assign to the work_request_id property of this WorkRequestError.
        :type work_request_id: str

        :param code:
            The value to assign to the code property of this WorkRequestError.
        :type code: str

        :param message:
            The value to assign to the message property of this WorkRequestError.
        :type message: str

        :param is_retryable:
            The value to assign to the is_retryable property of this WorkRequestError.
        :type is_retryable: bool

        :param timestamp:
            The value to assign to the timestamp property of this WorkRequestError.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'work_request_id': 'str',
            'code': 'str',
            'message': 'str',
            'is_retryable': 'bool',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'work_request_id': 'workRequestId',
            'code': 'code',
            'message': 'message',
            'is_retryable': 'isRetryable',
            'timestamp': 'timestamp'
        }

        self._id = None
        self._work_request_id = None
        self._code = None
        self._message = None
        self._is_retryable = None
        self._timestamp = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestError.
        The identifier of the work request error.


        :return: The id of this WorkRequestError.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestError.
        The identifier of the work request error.


        :param id: The id of this WorkRequestError.
        :type: str
        """
        self._id = id

    @property
    def work_request_id(self):
        """
        **[Required]** Gets the work_request_id of this WorkRequestError.
        The OCID of the work request.


        :return: The work_request_id of this WorkRequestError.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this WorkRequestError.
        The OCID of the work request.


        :param work_request_id: The work_request_id of this WorkRequestError.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def code(self):
        """
        **[Required]** Gets the code of this WorkRequestError.
        A machine-usable code for the error that occurred. Error codes are listed on
        (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm).


        :return: The code of this WorkRequestError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this WorkRequestError.
        A machine-usable code for the error that occurred. Error codes are listed on
        (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm).


        :param code: The code of this WorkRequestError.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this WorkRequestError.
        A human-readable description of the issue that occurred.


        :return: The message of this WorkRequestError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequestError.
        A human-readable description of the issue that occurred.


        :param message: The message of this WorkRequestError.
        :type: str
        """
        self._message = message

    @property
    def is_retryable(self):
        """
        Gets the is_retryable of this WorkRequestError.
        Determines if the work request error can be reproduced and tried again.


        :return: The is_retryable of this WorkRequestError.
        :rtype: bool
        """
        return self._is_retryable

    @is_retryable.setter
    def is_retryable(self, is_retryable):
        """
        Sets the is_retryable of this WorkRequestError.
        Determines if the work request error can be reproduced and tried again.


        :param is_retryable: The is_retryable of this WorkRequestError.
        :type: bool
        """
        self._is_retryable = is_retryable

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this WorkRequestError.
        The date and time the error occurred as described in `RFC 3339`__. The precision for the time object is in milliseconds.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The timestamp of this WorkRequestError.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this WorkRequestError.
        The date and time the error occurred as described in `RFC 3339`__. The precision for the time object is in milliseconds.

        __ https://tools.ietf.org/rfc/rfc3339


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
