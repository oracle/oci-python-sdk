# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dynamic_selection_key import DynamicSelectionKey
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnyOfSelectionKey(DynamicSelectionKey):
    """
    When dynamically routing and dynamically authenticating requests, the route or authentication server associated with a set of selection keys is used if the context variable in an incoming request exactly matches one of the keys in the set.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnyOfSelectionKey object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.AnyOfSelectionKey.type` attribute
        of this class is ``ANY_OF`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AnyOfSelectionKey.
            Allowed values for this property are: "ANY_OF", "WILDCARD"
        :type type: str

        :param is_default:
            The value to assign to the is_default property of this AnyOfSelectionKey.
        :type is_default: bool

        :param name:
            The value to assign to the name property of this AnyOfSelectionKey.
        :type name: str

        :param values:
            The value to assign to the values property of this AnyOfSelectionKey.
        :type values: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'is_default': 'bool',
            'name': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'is_default': 'isDefault',
            'name': 'name',
            'values': 'values'
        }

        self._type = None
        self._is_default = None
        self._name = None
        self._values = None
        self._type = 'ANY_OF'

    @property
    def values(self):
        """
        Gets the values of this AnyOfSelectionKey.
        The set of selection keys to match with the context variable in an incoming request. If the context variable exactly matches one of the keys in the set, the request is sent to the route or authentication server associated with the set.


        :return: The values of this AnyOfSelectionKey.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this AnyOfSelectionKey.
        The set of selection keys to match with the context variable in an incoming request. If the context variable exactly matches one of the keys in the set, the request is sent to the route or authentication server associated with the set.


        :param values: The values of this AnyOfSelectionKey.
        :type: list[str]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
