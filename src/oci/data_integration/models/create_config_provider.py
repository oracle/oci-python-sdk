# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConfigProvider(object):
    """
    The type to create a config provider.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConfigProvider object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bindings:
            The value to assign to the bindings property of this CreateConfigProvider.
        :type bindings: dict(str, ParameterValue)

        """
        self.swagger_types = {
            'bindings': 'dict(str, ParameterValue)'
        }

        self.attribute_map = {
            'bindings': 'bindings'
        }

        self._bindings = None

    @property
    def bindings(self):
        """
        Gets the bindings of this CreateConfigProvider.
        bindings


        :return: The bindings of this CreateConfigProvider.
        :rtype: dict(str, ParameterValue)
        """
        return self._bindings

    @bindings.setter
    def bindings(self, bindings):
        """
        Sets the bindings of this CreateConfigProvider.
        bindings


        :param bindings: The bindings of this CreateConfigProvider.
        :type: dict(str, ParameterValue)
        """
        self._bindings = bindings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
