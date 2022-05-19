# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDigitalAssistantParameterDetails(object):
    """
    Properties to update a Digital Assistant Parameter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDigitalAssistantParameterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UpdateDigitalAssistantParameterDetails.
        :type value: str

        """
        self.swagger_types = {
            'value': 'str'
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UpdateDigitalAssistantParameterDetails.
        The current value.  The value will be interpreted based on the `type`.


        :return: The value of this UpdateDigitalAssistantParameterDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UpdateDigitalAssistantParameterDetails.
        The current value.  The value will be interpreted based on the `type`.


        :param value: The value of this UpdateDigitalAssistantParameterDetails.
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
