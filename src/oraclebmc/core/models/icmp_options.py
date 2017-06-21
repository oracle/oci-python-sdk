# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class IcmpOptions(object):

    def __init__(self):

        self.swagger_types = {
            'code': 'int',
            'type': 'int'
        }

        self.attribute_map = {
            'code': 'code',
            'type': 'type'
        }

        self._code = None
        self._type = None

    @property
    def code(self):
        """
        Gets the code of this IcmpOptions.
        The ICMP code (optional).


        :return: The code of this IcmpOptions.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this IcmpOptions.
        The ICMP code (optional).


        :param code: The code of this IcmpOptions.
        :type: int
        """
        self._code = code

    @property
    def type(self):
        """
        Gets the type of this IcmpOptions.
        The ICMP type.


        :return: The type of this IcmpOptions.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IcmpOptions.
        The ICMP type.


        :param type: The type of this IcmpOptions.
        :type: int
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
