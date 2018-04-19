# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IcmpOptions(object):
    """
    Optional object to specify a particular ICMP type and code. If you specify ICMP as the protocol
    but do not provide this object, then all ICMP types and codes are allowed. If you do provide
    this object, the type is required and the code is optional.
    See `ICMP Parameters`__
    for allowed values. To enable MTU negotiation for ingress internet traffic, make sure to allow
    type 3 (\"Destination Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\").
    If you need to specify multiple codes for a single type, create a separate security list rule for each.

    __ http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IcmpOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this IcmpOptions.
        :type code: int

        :param type:
            The value to assign to the type property of this IcmpOptions.
        :type type: int

        """
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
        **[Required]** Gets the type of this IcmpOptions.
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
