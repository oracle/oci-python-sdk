# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigProvider(object):
    """
    The information about the configuration provider.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigProvider object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bindings:
            The value to assign to the bindings property of this ConfigProvider.
        :type bindings: dict(str, ParameterValue)

        :param child_providers:
            The value to assign to the child_providers property of this ConfigProvider.
        :type child_providers: dict(str, ConfigProvider)

        """
        self.swagger_types = {
            'bindings': 'dict(str, ParameterValue)',
            'child_providers': 'dict(str, ConfigProvider)'
        }

        self.attribute_map = {
            'bindings': 'bindings',
            'child_providers': 'childProviders'
        }

        self._bindings = None
        self._child_providers = None

    @property
    def bindings(self):
        """
        Gets the bindings of this ConfigProvider.
        The configuration provider bindings.


        :return: The bindings of this ConfigProvider.
        :rtype: dict(str, ParameterValue)
        """
        return self._bindings

    @bindings.setter
    def bindings(self, bindings):
        """
        Sets the bindings of this ConfigProvider.
        The configuration provider bindings.


        :param bindings: The bindings of this ConfigProvider.
        :type: dict(str, ParameterValue)
        """
        self._bindings = bindings

    @property
    def child_providers(self):
        """
        Gets the child_providers of this ConfigProvider.
        The child providers.


        :return: The child_providers of this ConfigProvider.
        :rtype: dict(str, ConfigProvider)
        """
        return self._child_providers

    @child_providers.setter
    def child_providers(self, child_providers):
        """
        Sets the child_providers of this ConfigProvider.
        The child providers.


        :param child_providers: The child_providers of this ConfigProvider.
        :type: dict(str, ConfigProvider)
        """
        self._child_providers = child_providers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
