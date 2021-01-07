# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FilterQueryParameterPolicy(object):
    """
    Filter parameters from the query string as they pass through the gateway.  The gateway applies filters after other
    transformations, so any parameters set or renamed must also be listed here when using an ALLOW type policy.
    """

    #: A constant which can be used with the type property of a FilterQueryParameterPolicy.
    #: This constant has a value of "ALLOW"
    TYPE_ALLOW = "ALLOW"

    #: A constant which can be used with the type property of a FilterQueryParameterPolicy.
    #: This constant has a value of "BLOCK"
    TYPE_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new FilterQueryParameterPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FilterQueryParameterPolicy.
            Allowed values for this property are: "ALLOW", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param items:
            The value to assign to the items property of this FilterQueryParameterPolicy.
        :type items: list[oci.apigateway.models.FilterQueryParameterPolicyItem]

        """
        self.swagger_types = {
            'type': 'str',
            'items': 'list[FilterQueryParameterPolicyItem]'
        }

        self.attribute_map = {
            'type': 'type',
            'items': 'items'
        }

        self._type = None
        self._items = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this FilterQueryParameterPolicy.
        BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list.  ALLOW
        permits only the parameters in the list and removes all others, so it acts as an inclusion list.

        Allowed values for this property are: "ALLOW", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this FilterQueryParameterPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FilterQueryParameterPolicy.
        BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list.  ALLOW
        permits only the parameters in the list and removes all others, so it acts as an inclusion list.


        :param type: The type of this FilterQueryParameterPolicy.
        :type: str
        """
        allowed_values = ["ALLOW", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def items(self):
        """
        **[Required]** Gets the items of this FilterQueryParameterPolicy.
        The list of query parameters.


        :return: The items of this FilterQueryParameterPolicy.
        :rtype: list[oci.apigateway.models.FilterQueryParameterPolicyItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this FilterQueryParameterPolicy.
        The list of query parameters.


        :param items: The items of this FilterQueryParameterPolicy.
        :type: list[oci.apigateway.models.FilterQueryParameterPolicyItem]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
