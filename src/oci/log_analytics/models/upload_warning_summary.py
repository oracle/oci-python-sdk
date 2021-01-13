# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UploadWarningSummary(object):
    """
    Summary of Upload warnings.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UploadWarningSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reference:
            The value to assign to the reference property of this UploadWarningSummary.
        :type reference: str

        :param status:
            The value to assign to the status property of this UploadWarningSummary.
        :type status: str

        :param time_started:
            The value to assign to the time_started property of this UploadWarningSummary.
        :type time_started: datetime

        :param error_message:
            The value to assign to the error_message property of this UploadWarningSummary.
        :type error_message: str

        """
        self.swagger_types = {
            'reference': 'str',
            'status': 'str',
            'time_started': 'datetime',
            'error_message': 'str'
        }

        self.attribute_map = {
            'reference': 'reference',
            'status': 'status',
            'time_started': 'timeStarted',
            'error_message': 'errorMessage'
        }

        self._reference = None
        self._status = None
        self._time_started = None
        self._error_message = None

    @property
    def reference(self):
        """
        **[Required]** Gets the reference of this UploadWarningSummary.
        Unique internal identifier to refer upload warning.


        :return: The reference of this UploadWarningSummary.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this UploadWarningSummary.
        Unique internal identifier to refer upload warning.


        :param reference: The reference of this UploadWarningSummary.
        :type: str
        """
        self._reference = reference

    @property
    def status(self):
        """
        Gets the status of this UploadWarningSummary.
        Status of the upload. Ex - Failed.


        :return: The status of this UploadWarningSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UploadWarningSummary.
        Status of the upload. Ex - Failed.


        :param status: The status of this UploadWarningSummary.
        :type: str
        """
        self._status = status

    @property
    def time_started(self):
        """
        Gets the time_started of this UploadWarningSummary.
        The time when the upload processing started.


        :return: The time_started of this UploadWarningSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this UploadWarningSummary.
        The time when the upload processing started.


        :param time_started: The time_started of this UploadWarningSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def error_message(self):
        """
        Gets the error_message of this UploadWarningSummary.
        The details about upload processing failure.


        :return: The error_message of this UploadWarningSummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this UploadWarningSummary.
        The details about upload processing failure.


        :param error_message: The error_message of this UploadWarningSummary.
        :type: str
        """
        self._error_message = error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
