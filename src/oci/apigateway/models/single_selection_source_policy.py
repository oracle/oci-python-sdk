# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .selection_source_policy import SelectionSourcePolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SingleSelectionSourcePolicy(SelectionSourcePolicy):
    """
    Information around selector used for branching among routes/ authentication servers in dynamic routing/ authentication where we are allowed to specify only a single context variable as selector.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SingleSelectionSourcePolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.SingleSelectionSourcePolicy.type` attribute
        of this class is ``SINGLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SingleSelectionSourcePolicy.
            Allowed values for this property are: "SINGLE"
        :type type: str

        :param selector:
            The value to assign to the selector property of this SingleSelectionSourcePolicy.
        :type selector: str

        """
        self.swagger_types = {
            'type': 'str',
            'selector': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'selector': 'selector'
        }

        self._type = None
        self._selector = None
        self._type = 'SINGLE'

    @property
    def selector(self):
        """
        **[Required]** Gets the selector of this SingleSelectionSourcePolicy.
        String describing the context variable used as selector.


        :return: The selector of this SingleSelectionSourcePolicy.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this SingleSelectionSourcePolicy.
        String describing the context variable used as selector.


        :param selector: The selector of this SingleSelectionSourcePolicy.
        :type: str
        """
        self._selector = selector

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
