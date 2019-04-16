# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTagDefaultDetails(object):
    """
    UpdateTagDefaultDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTagDefaultDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UpdateTagDefaultDetails.
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
        **[Required]** Gets the value of this UpdateTagDefaultDetails.
        The default value for the tag definition. This will be applied to all resources created in the Compartment.


        :return: The value of this UpdateTagDefaultDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UpdateTagDefaultDetails.
        The default value for the tag definition. This will be applied to all resources created in the Compartment.


        :param value: The value of this UpdateTagDefaultDetails.
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
