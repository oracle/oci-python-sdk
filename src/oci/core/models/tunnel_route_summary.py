# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TunnelRouteSummary(object):
    """
    The routes advertised to the Customer and the routes received from the Customer
    """

    #: A constant which can be used with the advertiser property of a TunnelRouteSummary.
    #: This constant has a value of "CUSTOMER"
    ADVERTISER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the advertiser property of a TunnelRouteSummary.
    #: This constant has a value of "ORACLE"
    ADVERTISER_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new TunnelRouteSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param prefix:
            The value to assign to the prefix property of this TunnelRouteSummary.
        :type prefix: str

        :param age:
            The value to assign to the age property of this TunnelRouteSummary.
        :type age: int

        :param is_best_path:
            The value to assign to the is_best_path property of this TunnelRouteSummary.
        :type is_best_path: bool

        :param as_path:
            The value to assign to the as_path property of this TunnelRouteSummary.
        :type as_path: list[int]

        :param advertiser:
            The value to assign to the advertiser property of this TunnelRouteSummary.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type advertiser: str

        """
        self.swagger_types = {
            'prefix': 'str',
            'age': 'int',
            'is_best_path': 'bool',
            'as_path': 'list[int]',
            'advertiser': 'str'
        }

        self.attribute_map = {
            'prefix': 'prefix',
            'age': 'age',
            'is_best_path': 'isBestPath',
            'as_path': 'asPath',
            'advertiser': 'advertiser'
        }

        self._prefix = None
        self._age = None
        self._is_best_path = None
        self._as_path = None
        self._advertiser = None

    @property
    def prefix(self):
        """
        Gets the prefix of this TunnelRouteSummary.
        BGP Network Layer Reachability Information


        :return: The prefix of this TunnelRouteSummary.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this TunnelRouteSummary.
        BGP Network Layer Reachability Information


        :param prefix: The prefix of this TunnelRouteSummary.
        :type: str
        """
        self._prefix = prefix

    @property
    def age(self):
        """
        Gets the age of this TunnelRouteSummary.
        The age of the route


        :return: The age of this TunnelRouteSummary.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """
        Sets the age of this TunnelRouteSummary.
        The age of the route


        :param age: The age of this TunnelRouteSummary.
        :type: int
        """
        self._age = age

    @property
    def is_best_path(self):
        """
        Gets the is_best_path of this TunnelRouteSummary.
        Is this the best route


        :return: The is_best_path of this TunnelRouteSummary.
        :rtype: bool
        """
        return self._is_best_path

    @is_best_path.setter
    def is_best_path(self, is_best_path):
        """
        Sets the is_best_path of this TunnelRouteSummary.
        Is this the best route


        :param is_best_path: The is_best_path of this TunnelRouteSummary.
        :type: bool
        """
        self._is_best_path = is_best_path

    @property
    def as_path(self):
        """
        Gets the as_path of this TunnelRouteSummary.
        List of ASNs in AS Path


        :return: The as_path of this TunnelRouteSummary.
        :rtype: list[int]
        """
        return self._as_path

    @as_path.setter
    def as_path(self, as_path):
        """
        Sets the as_path of this TunnelRouteSummary.
        List of ASNs in AS Path


        :param as_path: The as_path of this TunnelRouteSummary.
        :type: list[int]
        """
        self._as_path = as_path

    @property
    def advertiser(self):
        """
        Gets the advertiser of this TunnelRouteSummary.
        Route advertiser

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The advertiser of this TunnelRouteSummary.
        :rtype: str
        """
        return self._advertiser

    @advertiser.setter
    def advertiser(self, advertiser):
        """
        Sets the advertiser of this TunnelRouteSummary.
        Route advertiser


        :param advertiser: The advertiser of this TunnelRouteSummary.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(advertiser, allowed_values):
            advertiser = 'UNKNOWN_ENUM_VALUE'
        self._advertiser = advertiser

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
