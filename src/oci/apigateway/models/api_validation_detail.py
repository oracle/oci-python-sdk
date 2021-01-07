# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiValidationDetail(object):
    """
    Detail of a single error or warning.
    """

    #: A constant which can be used with the severity property of a ApiValidationDetail.
    #: This constant has a value of "INFO"
    SEVERITY_INFO = "INFO"

    #: A constant which can be used with the severity property of a ApiValidationDetail.
    #: This constant has a value of "WARNING"
    SEVERITY_WARNING = "WARNING"

    #: A constant which can be used with the severity property of a ApiValidationDetail.
    #: This constant has a value of "ERROR"
    SEVERITY_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new ApiValidationDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param msg:
            The value to assign to the msg property of this ApiValidationDetail.
        :type msg: str

        :param severity:
            The value to assign to the severity property of this ApiValidationDetail.
            Allowed values for this property are: "INFO", "WARNING", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param src:
            The value to assign to the src property of this ApiValidationDetail.
        :type src: list[list[float]]

        """
        self.swagger_types = {
            'msg': 'str',
            'severity': 'str',
            'src': 'list[list[float]]'
        }

        self.attribute_map = {
            'msg': 'msg',
            'severity': 'severity',
            'src': 'src'
        }

        self._msg = None
        self._severity = None
        self._src = None

    @property
    def msg(self):
        """
        Gets the msg of this ApiValidationDetail.
        Description of the warning/error.


        :return: The msg of this ApiValidationDetail.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """
        Sets the msg of this ApiValidationDetail.
        Description of the warning/error.


        :param msg: The msg of this ApiValidationDetail.
        :type: str
        """
        self._msg = msg

    @property
    def severity(self):
        """
        Gets the severity of this ApiValidationDetail.
        Severity of the issue.

        Allowed values for this property are: "INFO", "WARNING", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this ApiValidationDetail.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this ApiValidationDetail.
        Severity of the issue.


        :param severity: The severity of this ApiValidationDetail.
        :type: str
        """
        allowed_values = ["INFO", "WARNING", "ERROR"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def src(self):
        """
        Gets the src of this ApiValidationDetail.
        Position of the issue in the specification file (line, column).


        :return: The src of this ApiValidationDetail.
        :rtype: list[list[float]]
        """
        return self._src

    @src.setter
    def src(self, src):
        """
        Sets the src of this ApiValidationDetail.
        Position of the issue in the specification file (line, column).


        :param src: The src of this ApiValidationDetail.
        :type: list[list[float]]
        """
        self._src = src

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
