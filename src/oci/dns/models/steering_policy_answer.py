# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyAnswer(object):
    """
    DNS record data with metadata for processing in a steering policy.

    *Warning:* Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyAnswer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SteeringPolicyAnswer.
        :type name: str

        :param rtype:
            The value to assign to the rtype property of this SteeringPolicyAnswer.
        :type rtype: str

        :param rdata:
            The value to assign to the rdata property of this SteeringPolicyAnswer.
        :type rdata: str

        :param pool:
            The value to assign to the pool property of this SteeringPolicyAnswer.
        :type pool: str

        :param is_disabled:
            The value to assign to the is_disabled property of this SteeringPolicyAnswer.
        :type is_disabled: bool

        """
        self.swagger_types = {
            'name': 'str',
            'rtype': 'str',
            'rdata': 'str',
            'pool': 'str',
            'is_disabled': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'rtype': 'rtype',
            'rdata': 'rdata',
            'pool': 'pool',
            'is_disabled': 'isDisabled'
        }

        self._name = None
        self._rtype = None
        self._rdata = None
        self._pool = None
        self._is_disabled = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SteeringPolicyAnswer.
        A user-friendly name for the answer, unique within the steering policy.


        :return: The name of this SteeringPolicyAnswer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SteeringPolicyAnswer.
        A user-friendly name for the answer, unique within the steering policy.


        :param name: The name of this SteeringPolicyAnswer.
        :type: str
        """
        self._name = name

    @property
    def rtype(self):
        """
        **[Required]** Gets the rtype of this SteeringPolicyAnswer.
        The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more
        information, see `Resource Record (RR) TYPEs`__.

        __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4


        :return: The rtype of this SteeringPolicyAnswer.
        :rtype: str
        """
        return self._rtype

    @rtype.setter
    def rtype(self, rtype):
        """
        Sets the rtype of this SteeringPolicyAnswer.
        The canonical name for the record's type. Only A, AAAA, and CNAME are supported. For more
        information, see `Resource Record (RR) TYPEs`__.

        __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4


        :param rtype: The rtype of this SteeringPolicyAnswer.
        :type: str
        """
        self._rtype = rtype

    @property
    def rdata(self):
        """
        **[Required]** Gets the rdata of this SteeringPolicyAnswer.
        The record's data, as whitespace-delimited tokens in
        type-specific presentation format.


        :return: The rdata of this SteeringPolicyAnswer.
        :rtype: str
        """
        return self._rdata

    @rdata.setter
    def rdata(self, rdata):
        """
        Sets the rdata of this SteeringPolicyAnswer.
        The record's data, as whitespace-delimited tokens in
        type-specific presentation format.


        :param rdata: The rdata of this SteeringPolicyAnswer.
        :type: str
        """
        self._rdata = rdata

    @property
    def pool(self):
        """
        Gets the pool of this SteeringPolicyAnswer.
        The freeform name of a group of one or more records (e.g., a data center or a geographic
        region) in which this one is included.


        :return: The pool of this SteeringPolicyAnswer.
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """
        Sets the pool of this SteeringPolicyAnswer.
        The freeform name of a group of one or more records (e.g., a data center or a geographic
        region) in which this one is included.


        :param pool: The pool of this SteeringPolicyAnswer.
        :type: str
        """
        self._pool = pool

    @property
    def is_disabled(self):
        """
        Gets the is_disabled of this SteeringPolicyAnswer.
        Whether or not an answer should be excluded from responses, e.g. because the corresponding
        server is down for maintenance. Note, however, that such filtering is not automatic and
        will only take place if a rule implements it.


        :return: The is_disabled of this SteeringPolicyAnswer.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """
        Sets the is_disabled of this SteeringPolicyAnswer.
        Whether or not an answer should be excluded from responses, e.g. because the corresponding
        server is down for maintenance. Note, however, that such filtering is not automatic and
        will only take place if a rule implements it.


        :param is_disabled: The is_disabled of this SteeringPolicyAnswer.
        :type: bool
        """
        self._is_disabled = is_disabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
