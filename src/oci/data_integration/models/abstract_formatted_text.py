# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractFormattedText(object):
    """
    The type of the formatted text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractFormattedText object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_values:
            The value to assign to the config_values property of this AbstractFormattedText.
        :type config_values: oci.data_integration.models.ConfigValues

        """
        self.swagger_types = {
            'config_values': 'ConfigValues'
        }

        self.attribute_map = {
            'config_values': 'configValues'
        }

        self._config_values = None

    @property
    def config_values(self):
        """
        Gets the config_values of this AbstractFormattedText.

        :return: The config_values of this AbstractFormattedText.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this AbstractFormattedText.

        :param config_values: The config_values of this AbstractFormattedText.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
