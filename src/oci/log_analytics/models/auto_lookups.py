# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoLookups(object):
    """
    AutoLookups
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutoLookups object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param canonical_link:
            The value to assign to the canonical_link property of this AutoLookups.
        :type canonical_link: str

        :param total_count:
            The value to assign to the total_count property of this AutoLookups.
        :type total_count: int

        """
        self.swagger_types = {
            'canonical_link': 'str',
            'total_count': 'int'
        }

        self.attribute_map = {
            'canonical_link': 'canonicalLink',
            'total_count': 'totalCount'
        }

        self._canonical_link = None
        self._total_count = None

    @property
    def canonical_link(self):
        """
        Gets the canonical_link of this AutoLookups.
        The canonical link.


        :return: The canonical_link of this AutoLookups.
        :rtype: str
        """
        return self._canonical_link

    @canonical_link.setter
    def canonical_link(self, canonical_link):
        """
        Sets the canonical_link of this AutoLookups.
        The canonical link.


        :param canonical_link: The canonical_link of this AutoLookups.
        :type: str
        """
        self._canonical_link = canonical_link

    @property
    def total_count(self):
        """
        Gets the total_count of this AutoLookups.
        The total count.


        :return: The total_count of this AutoLookups.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this AutoLookups.
        The total count.


        :param total_count: The total_count of this AutoLookups.
        :type: int
        """
        self._total_count = total_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
