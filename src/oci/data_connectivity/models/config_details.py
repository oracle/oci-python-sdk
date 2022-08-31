# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigDetails(object):
    """
    The connector-specific engine configurations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_map:
            The value to assign to the config_map property of this ConfigDetails.
        :type config_map: dict(str, str)

        """
        self.swagger_types = {
            'config_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'config_map': 'configMap'
        }

        self._config_map = None

    @property
    def config_map(self):
        """
        **[Required]** Gets the config_map of this ConfigDetails.
        The connector-specific engine configurations configuration represented in a key-value map. Example - \"spark.sql.catalogImplementation\", \"hive\"


        :return: The config_map of this ConfigDetails.
        :rtype: dict(str, str)
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """
        Sets the config_map of this ConfigDetails.
        The connector-specific engine configurations configuration represented in a key-value map. Example - \"spark.sql.catalogImplementation\", \"hive\"


        :param config_map: The config_map of this ConfigDetails.
        :type: dict(str, str)
        """
        self._config_map = config_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
