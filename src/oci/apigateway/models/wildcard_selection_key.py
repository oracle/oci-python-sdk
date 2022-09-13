# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dynamic_selection_key import DynamicSelectionKey
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WildcardSelectionKey(DynamicSelectionKey):
    """
    Information around the Wildcard expression matching the value for selector of a dynamic authentication/ routing branch.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WildcardSelectionKey object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.WildcardSelectionKey.type` attribute
        of this class is ``WILDCARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this WildcardSelectionKey.
            Allowed values for this property are: "ANY_OF", "WILDCARD"
        :type type: str

        :param is_default:
            The value to assign to the is_default property of this WildcardSelectionKey.
        :type is_default: bool

        :param name:
            The value to assign to the name property of this WildcardSelectionKey.
        :type name: str

        :param expression:
            The value to assign to the expression property of this WildcardSelectionKey.
        :type expression: str

        """
        self.swagger_types = {
            'type': 'str',
            'is_default': 'bool',
            'name': 'str',
            'expression': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'is_default': 'isDefault',
            'name': 'name',
            'expression': 'expression'
        }

        self._type = None
        self._is_default = None
        self._name = None
        self._expression = None
        self._type = 'WILDCARD'

    @property
    def expression(self):
        """
        **[Required]** Gets the expression of this WildcardSelectionKey.
        String describing the expression with wildcards.


        :return: The expression of this WildcardSelectionKey.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this WildcardSelectionKey.
        String describing the expression with wildcards.


        :param expression: The expression of this WildcardSelectionKey.
        :type: str
        """
        self._expression = expression

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
