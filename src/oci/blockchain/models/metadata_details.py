# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetadataDetails(object):
    """
    Metadata parameter details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetadataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param param_name:
            The value to assign to the param_name property of this MetadataDetails.
        :type param_name: str

        :param param_value:
            The value to assign to the param_value property of this MetadataDetails.
        :type param_value: str

        :param is_json_value:
            The value to assign to the is_json_value property of this MetadataDetails.
        :type is_json_value: bool

        """
        self.swagger_types = {
            'param_name': 'str',
            'param_value': 'str',
            'is_json_value': 'bool'
        }

        self.attribute_map = {
            'param_name': 'paramName',
            'param_value': 'paramValue',
            'is_json_value': 'isJsonValue'
        }

        self._param_name = None
        self._param_value = None
        self._is_json_value = None

    @property
    def param_name(self):
        """
        **[Required]** Gets the param_name of this MetadataDetails.
        Metadata param name


        :return: The param_name of this MetadataDetails.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """
        Sets the param_name of this MetadataDetails.
        Metadata param name


        :param param_name: The param_name of this MetadataDetails.
        :type: str
        """
        self._param_name = param_name

    @property
    def param_value(self):
        """
        **[Required]** Gets the param_value of this MetadataDetails.
        Metadata param value. Complex value will be a JSON string.


        :return: The param_value of this MetadataDetails.
        :rtype: str
        """
        return self._param_value

    @param_value.setter
    def param_value(self, param_value):
        """
        Sets the param_value of this MetadataDetails.
        Metadata param value. Complex value will be a JSON string.


        :param param_value: The param_value of this MetadataDetails.
        :type: str
        """
        self._param_value = param_value

    @property
    def is_json_value(self):
        """
        **[Required]** Gets the is_json_value of this MetadataDetails.
        Indicates if the value is a JSON string


        :return: The is_json_value of this MetadataDetails.
        :rtype: bool
        """
        return self._is_json_value

    @is_json_value.setter
    def is_json_value(self, is_json_value):
        """
        Sets the is_json_value of this MetadataDetails.
        Indicates if the value is a JSON string


        :param is_json_value: The is_json_value of this MetadataDetails.
        :type: bool
        """
        self._is_json_value = is_json_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
