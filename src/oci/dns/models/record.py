# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Record(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Record object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param domain:
            The value to assign to the domain property of this Record.
        :type domain: str

        :param record_hash:
            The value to assign to the record_hash property of this Record.
        :type record_hash: str

        :param is_protected:
            The value to assign to the is_protected property of this Record.
        :type is_protected: bool

        :param rdata:
            The value to assign to the rdata property of this Record.
        :type rdata: str

        :param rrset_version:
            The value to assign to the rrset_version property of this Record.
        :type rrset_version: str

        :param rtype:
            The value to assign to the rtype property of this Record.
        :type rtype: str

        :param ttl:
            The value to assign to the ttl property of this Record.
        :type ttl: int

        """
        self.swagger_types = {
            'domain': 'str',
            'record_hash': 'str',
            'is_protected': 'bool',
            'rdata': 'str',
            'rrset_version': 'str',
            'rtype': 'str',
            'ttl': 'int'
        }

        self.attribute_map = {
            'domain': 'domain',
            'record_hash': 'recordHash',
            'is_protected': 'isProtected',
            'rdata': 'rdata',
            'rrset_version': 'rrsetVersion',
            'rtype': 'rtype',
            'ttl': 'ttl'
        }

        self._domain = None
        self._record_hash = None
        self._is_protected = None
        self._rdata = None
        self._rrset_version = None
        self._rtype = None
        self._ttl = None

    @property
    def domain(self):
        """
        Gets the domain of this Record.
        The fully qualified domain name where the record can be located.


        :return: The domain of this Record.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this Record.
        The fully qualified domain name where the record can be located.


        :param domain: The domain of this Record.
        :type: str
        """
        self._domain = domain

    @property
    def record_hash(self):
        """
        Gets the record_hash of this Record.
        A unique identifier for the record within its zone.


        :return: The record_hash of this Record.
        :rtype: str
        """
        return self._record_hash

    @record_hash.setter
    def record_hash(self, record_hash):
        """
        Sets the record_hash of this Record.
        A unique identifier for the record within its zone.


        :param record_hash: The record_hash of this Record.
        :type: str
        """
        self._record_hash = record_hash

    @property
    def is_protected(self):
        """
        Gets the is_protected of this Record.
        A Boolean flag indicating whether or not parts of the record
        are unable to be explicitly managed.


        :return: The is_protected of this Record.
        :rtype: bool
        """
        return self._is_protected

    @is_protected.setter
    def is_protected(self, is_protected):
        """
        Sets the is_protected of this Record.
        A Boolean flag indicating whether or not parts of the record
        are unable to be explicitly managed.


        :param is_protected: The is_protected of this Record.
        :type: bool
        """
        self._is_protected = is_protected

    @property
    def rdata(self):
        """
        Gets the rdata of this Record.
        The record's data, as whitespace-delimited tokens in
        type-specific presentation format.


        :return: The rdata of this Record.
        :rtype: str
        """
        return self._rdata

    @rdata.setter
    def rdata(self, rdata):
        """
        Sets the rdata of this Record.
        The record's data, as whitespace-delimited tokens in
        type-specific presentation format.


        :param rdata: The rdata of this Record.
        :type: str
        """
        self._rdata = rdata

    @property
    def rrset_version(self):
        """
        Gets the rrset_version of this Record.
        The latest version of the record's zone in which its RRSet differs
        from the preceding version.


        :return: The rrset_version of this Record.
        :rtype: str
        """
        return self._rrset_version

    @rrset_version.setter
    def rrset_version(self, rrset_version):
        """
        Sets the rrset_version of this Record.
        The latest version of the record's zone in which its RRSet differs
        from the preceding version.


        :param rrset_version: The rrset_version of this Record.
        :type: str
        """
        self._rrset_version = rrset_version

    @property
    def rtype(self):
        """
        Gets the rtype of this Record.
        The canonical name for the record's type, such as A or CNAME. For more
        information, see `Resource Record (RR) TYPEs`__.

        __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4


        :return: The rtype of this Record.
        :rtype: str
        """
        return self._rtype

    @rtype.setter
    def rtype(self, rtype):
        """
        Sets the rtype of this Record.
        The canonical name for the record's type, such as A or CNAME. For more
        information, see `Resource Record (RR) TYPEs`__.

        __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4


        :param rtype: The rtype of this Record.
        :type: str
        """
        self._rtype = rtype

    @property
    def ttl(self):
        """
        Gets the ttl of this Record.
        The Time To Live for the record, in seconds.


        :return: The ttl of this Record.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this Record.
        The Time To Live for the record, in seconds.


        :param ttl: The ttl of this Record.
        :type: int
        """
        self._ttl = ttl

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
