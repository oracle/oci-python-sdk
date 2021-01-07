# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Routing(object):
    """
    The routing information for a vantage point.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Routing object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param as_label:
            The value to assign to the as_label property of this Routing.
        :type as_label: str

        :param asn:
            The value to assign to the asn property of this Routing.
        :type asn: int

        :param prefix:
            The value to assign to the prefix property of this Routing.
        :type prefix: str

        :param weight:
            The value to assign to the weight property of this Routing.
        :type weight: int

        """
        self.swagger_types = {
            'as_label': 'str',
            'asn': 'int',
            'prefix': 'str',
            'weight': 'int'
        }

        self.attribute_map = {
            'as_label': 'asLabel',
            'asn': 'asn',
            'prefix': 'prefix',
            'weight': 'weight'
        }

        self._as_label = None
        self._asn = None
        self._prefix = None
        self._weight = None

    @property
    def as_label(self):
        """
        Gets the as_label of this Routing.
        The registry label for `asn`, usually the name of the organization that
        owns the ASN. May be omitted or null.


        :return: The as_label of this Routing.
        :rtype: str
        """
        return self._as_label

    @as_label.setter
    def as_label(self, as_label):
        """
        Sets the as_label of this Routing.
        The registry label for `asn`, usually the name of the organization that
        owns the ASN. May be omitted or null.


        :param as_label: The as_label of this Routing.
        :type: str
        """
        self._as_label = as_label

    @property
    def asn(self):
        """
        Gets the asn of this Routing.
        The Autonomous System Number (ASN) identifying the organization
        responsible for routing packets to `prefix`.


        :return: The asn of this Routing.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """
        Sets the asn of this Routing.
        The Autonomous System Number (ASN) identifying the organization
        responsible for routing packets to `prefix`.


        :param asn: The asn of this Routing.
        :type: int
        """
        self._asn = asn

    @property
    def prefix(self):
        """
        Gets the prefix of this Routing.
        An IP prefix (CIDR syntax) that is less specific than
        `address`, through which `address` is routed.


        :return: The prefix of this Routing.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this Routing.
        An IP prefix (CIDR syntax) that is less specific than
        `address`, through which `address` is routed.


        :param prefix: The prefix of this Routing.
        :type: str
        """
        self._prefix = prefix

    @property
    def weight(self):
        """
        Gets the weight of this Routing.
        An integer between 0 and 100 used to select between multiple
        origin ASNs when routing to `prefix`. Most prefixes have
        exactly one origin ASN, in which case `weight` will be 100.


        :return: The weight of this Routing.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this Routing.
        An integer between 0 and 100 used to select between multiple
        origin ASNs when routing to `prefix`. Most prefixes have
        exactly one origin ASN, in which case `weight` will be 100.


        :param weight: The weight of this Routing.
        :type: int
        """
        self._weight = weight

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
