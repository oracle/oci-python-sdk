# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateStateDetails(object):

    def __init__(self):

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
