# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStateDetails(object):
    """
    UpdateStateDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param blocked:
            The value to assign to the blocked property of this UpdateStateDetails.
        :type blocked: bool

        """
        self.swagger_types = {
            'blocked': 'bool'
        }

        self.attribute_map = {
            'blocked': 'blocked'
        }

        self._blocked = None

    @property
    def blocked(self):
        """
        Gets the blocked of this UpdateStateDetails.
        Update state to blocked or unblocked. Only \"false\" is supported (for changing the state to unblocked).


        :return: The blocked of this UpdateStateDetails.
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """
        Sets the blocked of this UpdateStateDetails.
        Update state to blocked or unblocked. Only \"false\" is supported (for changing the state to unblocked).


        :param blocked: The blocked of this UpdateStateDetails.
        :type: bool
        """
        self._blocked = blocked

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
