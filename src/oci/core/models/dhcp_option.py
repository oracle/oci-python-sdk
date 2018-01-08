# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DhcpOption(object):

    def __init__(self, **kwargs):
        """
        Initializes a new DhcpOption object with values from values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.DhcpDnsOption`
        * :class:`~oci.core.models.DhcpSearchDomainOption`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DhcpOption.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'DomainNameServer':
            return 'DhcpDnsOption'

        if type == 'SearchDomain':
            return 'DhcpSearchDomainOption'
        else:
            return 'DhcpOption'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DhcpOption.
        The specific DHCP option. Either `DomainNameServer`
        (for :class:`DhcpDnsOption`) or
        `SearchDomain` (for :class:`DhcpSearchDomainOption`).


        :return: The type of this DhcpOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DhcpOption.
        The specific DHCP option. Either `DomainNameServer`
        (for :class:`DhcpDnsOption`) or
        `SearchDomain` (for :class:`DhcpSearchDomainOption`).


        :param type: The type of this DhcpOption.
        :type: str
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
