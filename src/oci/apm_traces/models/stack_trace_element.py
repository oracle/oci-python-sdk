# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StackTraceElement(object):
    """
    Stack trace element.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StackTraceElement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param method_name:
            The value to assign to the method_name property of this StackTraceElement.
        :type method_name: str

        :param file_name:
            The value to assign to the file_name property of this StackTraceElement.
        :type file_name: str

        :param line_number:
            The value to assign to the line_number property of this StackTraceElement.
        :type line_number: int

        :param class_name:
            The value to assign to the class_name property of this StackTraceElement.
        :type class_name: str

        :param weightage:
            The value to assign to the weightage property of this StackTraceElement.
        :type weightage: float

        """
        self.swagger_types = {
            'method_name': 'str',
            'file_name': 'str',
            'line_number': 'int',
            'class_name': 'str',
            'weightage': 'float'
        }

        self.attribute_map = {
            'method_name': 'methodName',
            'file_name': 'fileName',
            'line_number': 'lineNumber',
            'class_name': 'className',
            'weightage': 'weightage'
        }

        self._method_name = None
        self._file_name = None
        self._line_number = None
        self._class_name = None
        self._weightage = None

    @property
    def method_name(self):
        """
        Gets the method_name of this StackTraceElement.
        Name of the method containing the execution point.


        :return: The method_name of this StackTraceElement.
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """
        Sets the method_name of this StackTraceElement.
        Name of the method containing the execution point.


        :param method_name: The method_name of this StackTraceElement.
        :type: str
        """
        self._method_name = method_name

    @property
    def file_name(self):
        """
        Gets the file_name of this StackTraceElement.
        Name of the source file containing the execution point.


        :return: The file_name of this StackTraceElement.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this StackTraceElement.
        Name of the source file containing the execution point.


        :param file_name: The file_name of this StackTraceElement.
        :type: str
        """
        self._file_name = file_name

    @property
    def line_number(self):
        """
        Gets the line_number of this StackTraceElement.
        Line number of the source line containing the execution point.


        :return: The line_number of this StackTraceElement.
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """
        Sets the line_number of this StackTraceElement.
        Line number of the source line containing the execution point.


        :param line_number: The line_number of this StackTraceElement.
        :type: int
        """
        self._line_number = line_number

    @property
    def class_name(self):
        """
        Gets the class_name of this StackTraceElement.
        Name of the class containing the execution point.


        :return: The class_name of this StackTraceElement.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """
        Sets the class_name of this StackTraceElement.
        Name of the class containing the execution point.


        :param class_name: The class_name of this StackTraceElement.
        :type: str
        """
        self._class_name = class_name

    @property
    def weightage(self):
        """
        Gets the weightage of this StackTraceElement.
        The weight distribution that denotes the percentage occurrence of a method in the captured snapshots.


        :return: The weightage of this StackTraceElement.
        :rtype: float
        """
        return self._weightage

    @weightage.setter
    def weightage(self, weightage):
        """
        Sets the weightage of this StackTraceElement.
        The weight distribution that denotes the percentage occurrence of a method in the captured snapshots.


        :param weightage: The weightage of this StackTraceElement.
        :type: float
        """
        self._weightage = weightage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
