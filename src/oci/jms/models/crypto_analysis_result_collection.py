# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CryptoAnalysisResultCollection(object):
    """
    List of Crypto Event Analysis results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CryptoAnalysisResultCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this CryptoAnalysisResultCollection.
        :type items: list[oci.jms.models.CryptoAnalysisResultSummary]

        """
        self.swagger_types = {
            'items': 'list[CryptoAnalysisResultSummary]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this CryptoAnalysisResultCollection.
        A list of Crypto Event Analysis results.


        :return: The items of this CryptoAnalysisResultCollection.
        :rtype: list[oci.jms.models.CryptoAnalysisResultSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CryptoAnalysisResultCollection.
        A list of Crypto Event Analysis results.


        :param items: The items of this CryptoAnalysisResultCollection.
        :type: list[oci.jms.models.CryptoAnalysisResultSummary]
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
