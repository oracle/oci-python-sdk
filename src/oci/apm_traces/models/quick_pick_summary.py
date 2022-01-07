# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QuickPickSummary(object):
    """
    Summary of quick pick query objects that contains the quick pick queries.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QuickPickSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param quick_pick_name:
            The value to assign to the quick_pick_name property of this QuickPickSummary.
        :type quick_pick_name: str

        :param quick_pick_query:
            The value to assign to the quick_pick_query property of this QuickPickSummary.
        :type quick_pick_query: str

        """
        self.swagger_types = {
            'quick_pick_name': 'str',
            'quick_pick_query': 'str'
        }

        self.attribute_map = {
            'quick_pick_name': 'quickPickName',
            'quick_pick_query': 'quickPickQuery'
        }

        self._quick_pick_name = None
        self._quick_pick_query = None

    @property
    def quick_pick_name(self):
        """
        **[Required]** Gets the quick_pick_name of this QuickPickSummary.
        Quick pick name for the query.


        :return: The quick_pick_name of this QuickPickSummary.
        :rtype: str
        """
        return self._quick_pick_name

    @quick_pick_name.setter
    def quick_pick_name(self, quick_pick_name):
        """
        Sets the quick_pick_name of this QuickPickSummary.
        Quick pick name for the query.


        :param quick_pick_name: The quick_pick_name of this QuickPickSummary.
        :type: str
        """
        self._quick_pick_name = quick_pick_name

    @property
    def quick_pick_query(self):
        """
        **[Required]** Gets the quick_pick_query of this QuickPickSummary.
        Query for the quick pick.


        :return: The quick_pick_query of this QuickPickSummary.
        :rtype: str
        """
        return self._quick_pick_query

    @quick_pick_query.setter
    def quick_pick_query(self, quick_pick_query):
        """
        Sets the quick_pick_query of this QuickPickSummary.
        Query for the quick pick.


        :param quick_pick_query: The quick_pick_query of this QuickPickSummary.
        :type: str
        """
        self._quick_pick_query = quick_pick_query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
