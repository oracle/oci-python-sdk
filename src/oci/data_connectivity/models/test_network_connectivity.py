# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TestNetworkConnectivity(object):
    """
    The network validation response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TestNetworkConnectivity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_validation_output:
            The value to assign to the network_validation_output property of this TestNetworkConnectivity.
        :type network_validation_output: str

        :param is_reachable:
            The value to assign to the is_reachable property of this TestNetworkConnectivity.
        :type is_reachable: bool

        :param exception_message:
            The value to assign to the exception_message property of this TestNetworkConnectivity.
        :type exception_message: str

        """
        self.swagger_types = {
            'network_validation_output': 'str',
            'is_reachable': 'bool',
            'exception_message': 'str'
        }

        self.attribute_map = {
            'network_validation_output': 'networkValidationOutput',
            'is_reachable': 'isReachable',
            'exception_message': 'exceptionMessage'
        }

        self._network_validation_output = None
        self._is_reachable = None
        self._exception_message = None

    @property
    def network_validation_output(self):
        """
        Gets the network_validation_output of this TestNetworkConnectivity.
        Last line from network validation command execution output.


        :return: The network_validation_output of this TestNetworkConnectivity.
        :rtype: str
        """
        return self._network_validation_output

    @network_validation_output.setter
    def network_validation_output(self, network_validation_output):
        """
        Sets the network_validation_output of this TestNetworkConnectivity.
        Last line from network validation command execution output.


        :param network_validation_output: The network_validation_output of this TestNetworkConnectivity.
        :type: str
        """
        self._network_validation_output = network_validation_output

    @property
    def is_reachable(self):
        """
        **[Required]** Gets the is_reachable of this TestNetworkConnectivity.
        True if the data asset is has a valid network path.


        :return: The is_reachable of this TestNetworkConnectivity.
        :rtype: bool
        """
        return self._is_reachable

    @is_reachable.setter
    def is_reachable(self, is_reachable):
        """
        Sets the is_reachable of this TestNetworkConnectivity.
        True if the data asset is has a valid network path.


        :param is_reachable: The is_reachable of this TestNetworkConnectivity.
        :type: bool
        """
        self._is_reachable = is_reachable

    @property
    def exception_message(self):
        """
        Gets the exception_message of this TestNetworkConnectivity.
        Exception or error message encountered while testing network reachability for the data asset.


        :return: The exception_message of this TestNetworkConnectivity.
        :rtype: str
        """
        return self._exception_message

    @exception_message.setter
    def exception_message(self, exception_message):
        """
        Sets the exception_message of this TestNetworkConnectivity.
        Exception or error message encountered while testing network reachability for the data asset.


        :param exception_message: The exception_message of this TestNetworkConnectivity.
        :type: str
        """
        self._exception_message = exception_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
