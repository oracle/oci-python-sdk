# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Capabilities(object):
    """
    Status of capabilities that can be enabled for an environment family.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Capabilities object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_data_masking_enabled:
            The value to assign to the is_data_masking_enabled property of this Capabilities.
        :type is_data_masking_enabled: bool

        :param is_break_glass_enabled:
            The value to assign to the is_break_glass_enabled property of this Capabilities.
        :type is_break_glass_enabled: bool

        :param is_byok_enabled:
            The value to assign to the is_byok_enabled property of this Capabilities.
        :type is_byok_enabled: bool

        """
        self.swagger_types = {
            'is_data_masking_enabled': 'bool',
            'is_break_glass_enabled': 'bool',
            'is_byok_enabled': 'bool'
        }

        self.attribute_map = {
            'is_data_masking_enabled': 'isDataMaskingEnabled',
            'is_break_glass_enabled': 'isBreakGlassEnabled',
            'is_byok_enabled': 'isByokEnabled'
        }

        self._is_data_masking_enabled = None
        self._is_break_glass_enabled = None
        self._is_byok_enabled = None

    @property
    def is_data_masking_enabled(self):
        """
        Gets the is_data_masking_enabled of this Capabilities.
        Indicates whether data masking is enabled for the environment family. When enabled, data masking activities are supported.


        :return: The is_data_masking_enabled of this Capabilities.
        :rtype: bool
        """
        return self._is_data_masking_enabled

    @is_data_masking_enabled.setter
    def is_data_masking_enabled(self, is_data_masking_enabled):
        """
        Sets the is_data_masking_enabled of this Capabilities.
        Indicates whether data masking is enabled for the environment family. When enabled, data masking activities are supported.


        :param is_data_masking_enabled: The is_data_masking_enabled of this Capabilities.
        :type: bool
        """
        self._is_data_masking_enabled = is_data_masking_enabled

    @property
    def is_break_glass_enabled(self):
        """
        Gets the is_break_glass_enabled of this Capabilities.
        Indicates whether Break Glass is enabled for the environment family.


        :return: The is_break_glass_enabled of this Capabilities.
        :rtype: bool
        """
        return self._is_break_glass_enabled

    @is_break_glass_enabled.setter
    def is_break_glass_enabled(self, is_break_glass_enabled):
        """
        Sets the is_break_glass_enabled of this Capabilities.
        Indicates whether Break Glass is enabled for the environment family.


        :param is_break_glass_enabled: The is_break_glass_enabled of this Capabilities.
        :type: bool
        """
        self._is_break_glass_enabled = is_break_glass_enabled

    @property
    def is_byok_enabled(self):
        """
        Gets the is_byok_enabled of this Capabilities.
        Indicates whether customers can use their own encryption keys.


        :return: The is_byok_enabled of this Capabilities.
        :rtype: bool
        """
        return self._is_byok_enabled

    @is_byok_enabled.setter
    def is_byok_enabled(self, is_byok_enabled):
        """
        Sets the is_byok_enabled of this Capabilities.
        Indicates whether customers can use their own encryption keys.


        :param is_byok_enabled: The is_byok_enabled of this Capabilities.
        :type: bool
        """
        self._is_byok_enabled = is_byok_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
