# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Filter(object):
    """
    Criteria that the Announcements service uses to match announcements in order to provide only desired, matching announcements.
    """

    #: A constant which can be used with the type property of a Filter.
    #: This constant has a value of "COMPARTMENT_ID"
    TYPE_COMPARTMENT_ID = "COMPARTMENT_ID"

    #: A constant which can be used with the type property of a Filter.
    #: This constant has a value of "PLATFORM_TYPE"
    TYPE_PLATFORM_TYPE = "PLATFORM_TYPE"

    #: A constant which can be used with the type property of a Filter.
    #: This constant has a value of "REGION"
    TYPE_REGION = "REGION"

    #: A constant which can be used with the type property of a Filter.
    #: This constant has a value of "SERVICE"
    TYPE_SERVICE = "SERVICE"

    #: A constant which can be used with the type property of a Filter.
    #: This constant has a value of "RESOURCE_ID"
    TYPE_RESOURCE_ID = "RESOURCE_ID"

    #: A constant which can be used with the type property of a Filter.
    #: This constant has a value of "ANNOUNCEMENT_TYPE"
    TYPE_ANNOUNCEMENT_TYPE = "ANNOUNCEMENT_TYPE"

    def __init__(self, **kwargs):
        """
        Initializes a new Filter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Filter.
            Allowed values for this property are: "COMPARTMENT_ID", "PLATFORM_TYPE", "REGION", "SERVICE", "RESOURCE_ID", "ANNOUNCEMENT_TYPE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param value:
            The value to assign to the value property of this Filter.
        :type value: str

        """
        self.swagger_types = {
            'type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = None
        self._value = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Filter.
        The type of filter.

        Allowed values for this property are: "COMPARTMENT_ID", "PLATFORM_TYPE", "REGION", "SERVICE", "RESOURCE_ID", "ANNOUNCEMENT_TYPE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Filter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Filter.
        The type of filter.


        :param type: The type of this Filter.
        :type: str
        """
        allowed_values = ["COMPARTMENT_ID", "PLATFORM_TYPE", "REGION", "SERVICE", "RESOURCE_ID", "ANNOUNCEMENT_TYPE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Filter.
        The value of the filter.


        :return: The value of this Filter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Filter.
        The value of the filter.


        :param value: The value of this Filter.
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
