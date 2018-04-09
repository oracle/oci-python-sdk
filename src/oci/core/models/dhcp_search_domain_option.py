# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .dhcp_option import DhcpOption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DhcpSearchDomainOption(DhcpOption):
    """
    DHCP option for specifying a search domain name for DNS queries. For more information, see
    `DNS in Your Virtual Cloud Network`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DhcpSearchDomainOption object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.DhcpSearchDomainOption.type` attribute
        of this class is ``SearchDomain`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DhcpSearchDomainOption.
        :type type: str

        :param search_domain_names:
            The value to assign to the search_domain_names property of this DhcpSearchDomainOption.
        :type search_domain_names: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'search_domain_names': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'search_domain_names': 'searchDomainNames'
        }

        self._type = None
        self._search_domain_names = None
        self._type = 'SearchDomain'

    @property
    def search_domain_names(self):
        """
        **[Required]** Gets the search_domain_names of this DhcpSearchDomainOption.
        A single search domain name according to `RFC 952`__
        and `RFC 1123`__. During a DNS query,
        the OS will append this search domain name to the value being queried.

        If you set :class:`DhcpDnsOption` to `VcnLocalPlusInternet`,
        and you assign a DNS label to the VCN during creation, the search domain name in the
        VCN's default set of DHCP options is automatically set to the VCN domain
        (for example, `vcn1.oraclevcn.com`).

        If you don't want to use a search domain name, omit this option from the
        set of DHCP options. Do not include this option with an empty list
        of search domain names, or with an empty string as the value for any search
        domain name.

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123


        :return: The search_domain_names of this DhcpSearchDomainOption.
        :rtype: list[str]
        """
        return self._search_domain_names

    @search_domain_names.setter
    def search_domain_names(self, search_domain_names):
        """
        Sets the search_domain_names of this DhcpSearchDomainOption.
        A single search domain name according to `RFC 952`__
        and `RFC 1123`__. During a DNS query,
        the OS will append this search domain name to the value being queried.

        If you set :class:`DhcpDnsOption` to `VcnLocalPlusInternet`,
        and you assign a DNS label to the VCN during creation, the search domain name in the
        VCN's default set of DHCP options is automatically set to the VCN domain
        (for example, `vcn1.oraclevcn.com`).

        If you don't want to use a search domain name, omit this option from the
        set of DHCP options. Do not include this option with an empty list
        of search domain names, or with an empty string as the value for any search
        domain name.

        __ https://tools.ietf.org/html/rfc952
        __ https://tools.ietf.org/html/rfc1123


        :param search_domain_names: The search_domain_names of this DhcpSearchDomainOption.
        :type: list[str]
        """
        self._search_domain_names = search_domain_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
