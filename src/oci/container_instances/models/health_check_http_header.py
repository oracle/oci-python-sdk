# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HealthCheckHttpHeader(object):
    """
    Container Http headers for Http health check.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HealthCheckHttpHeader object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this HealthCheckHttpHeader.
        :type name: str

        :param value:
            The value to assign to the value property of this HealthCheckHttpHeader.
        :type value: str

        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value'
        }

        self._name = None
        self._value = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this HealthCheckHttpHeader.
        Container Http header Key.


        :return: The name of this HealthCheckHttpHeader.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HealthCheckHttpHeader.
        Container Http header Key.


        :param name: The name of this HealthCheckHttpHeader.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this HealthCheckHttpHeader.
        Container Http header value.


        :return: The value of this HealthCheckHttpHeader.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this HealthCheckHttpHeader.
        Container Http header value.


        :param value: The value of this HealthCheckHttpHeader.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
