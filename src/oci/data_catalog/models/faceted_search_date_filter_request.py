# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FacetedSearchDateFilterRequest(object):
    """
    Object with date filter criteria
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FacetedSearchDateFilterRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_name:
            The value to assign to the field_name property of this FacetedSearchDateFilterRequest.
        :type field_name: str

        :param time_after:
            The value to assign to the time_after property of this FacetedSearchDateFilterRequest.
        :type time_after: datetime

        :param time_before:
            The value to assign to the time_before property of this FacetedSearchDateFilterRequest.
        :type time_before: datetime

        """
        self.swagger_types = {
            'field_name': 'str',
            'time_after': 'datetime',
            'time_before': 'datetime'
        }

        self.attribute_map = {
            'field_name': 'fieldName',
            'time_after': 'timeAfter',
            'time_before': 'timeBefore'
        }

        self._field_name = None
        self._time_after = None
        self._time_before = None

    @property
    def field_name(self):
        """
        Gets the field_name of this FacetedSearchDateFilterRequest.
        Date field name that needs to be filtered by.


        :return: The field_name of this FacetedSearchDateFilterRequest.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this FacetedSearchDateFilterRequest.
        Date field name that needs to be filtered by.


        :param field_name: The field_name of this FacetedSearchDateFilterRequest.
        :type: str
        """
        self._field_name = field_name

    @property
    def time_after(self):
        """
        Gets the time_after of this FacetedSearchDateFilterRequest.
        The date and time the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_after of this FacetedSearchDateFilterRequest.
        :rtype: datetime
        """
        return self._time_after

    @time_after.setter
    def time_after(self, time_after):
        """
        Sets the time_after of this FacetedSearchDateFilterRequest.
        The date and time the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_after: The time_after of this FacetedSearchDateFilterRequest.
        :type: datetime
        """
        self._time_after = time_after

    @property
    def time_before(self):
        """
        Gets the time_before of this FacetedSearchDateFilterRequest.
        The date and time the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_before of this FacetedSearchDateFilterRequest.
        :rtype: datetime
        """
        return self._time_before

    @time_before.setter
    def time_before(self, time_before):
        """
        Sets the time_before of this FacetedSearchDateFilterRequest.
        The date and time the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_before: The time_before of this FacetedSearchDateFilterRequest.
        :type: datetime
        """
        self._time_before = time_before

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
