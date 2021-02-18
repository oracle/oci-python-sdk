# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DhcpOption(object):
    """
    A single DHCP option according to `RFC 1533`__.
    The two options available to use are :class:`DhcpDnsOption`
    and :class:`DhcpSearchDomainOption`. For more
    information, see `DNS in Your Virtual Cloud Network`__
    and `DHCP Options`__.

    __ https://tools.ietf.org/html/rfc1533
    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DhcpOption object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
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
