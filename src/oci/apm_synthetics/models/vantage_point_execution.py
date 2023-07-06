# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VantagePointExecution(object):
    """
    Details of a vantage point execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VantagePointExecution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this VantagePointExecution.
        :type name: str

        :param executions:
            The value to assign to the executions property of this VantagePointExecution.
        :type executions: list[int]

        """
        self.swagger_types = {
            'name': 'str',
            'executions': 'list[int]'
        }

        self.attribute_map = {
            'name': 'name',
            'executions': 'executions'
        }

        self._name = None
        self._executions = None

    @property
    def name(self):
        """
        Gets the name of this VantagePointExecution.
        Name of the vantage point.


        :return: The name of this VantagePointExecution.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VantagePointExecution.
        Name of the vantage point.


        :param name: The name of this VantagePointExecution.
        :type: str
        """
        self._name = name

    @property
    def executions(self):
        """
        Gets the executions of this VantagePointExecution.
        List of execution times in milliseconds.


        :return: The executions of this VantagePointExecution.
        :rtype: list[int]
        """
        return self._executions

    @executions.setter
    def executions(self, executions):
        """
        Sets the executions of this VantagePointExecution.
        List of execution times in milliseconds.


        :param executions: The executions of this VantagePointExecution.
        :type: list[int]
        """
        self._executions = executions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
