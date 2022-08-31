# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RetrieveDimensionStatesDetails(object):
    """
    The configuration details for retrieving the alarm state entries.
    Filter retrieved alarm state entries by status value and dimension key-value pairs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RetrieveDimensionStatesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimension_filters:
            The value to assign to the dimension_filters property of this RetrieveDimensionStatesDetails.
        :type dimension_filters: dict(str, str)

        :param status:
            The value to assign to the status property of this RetrieveDimensionStatesDetails.
        :type status: str

        """
        self.swagger_types = {
            'dimension_filters': 'dict(str, str)',
            'status': 'str'
        }

        self.attribute_map = {
            'dimension_filters': 'dimensionFilters',
            'status': 'status'
        }

        self._dimension_filters = None
        self._status = None

    @property
    def dimension_filters(self):
        """
        Gets the dimension_filters of this RetrieveDimensionStatesDetails.
        A filter to return only alarm state entries that match the exact set of specified dimension key-value pairs.
        If you specify `\"availabilityDomain\": \"phx-ad-1\"` but the alarm state entry corresponds to the set `\"availabilityDomain\": \"phx-ad-1\"`
        and `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`, then no results are returned.


        :return: The dimension_filters of this RetrieveDimensionStatesDetails.
        :rtype: dict(str, str)
        """
        return self._dimension_filters

    @dimension_filters.setter
    def dimension_filters(self, dimension_filters):
        """
        Sets the dimension_filters of this RetrieveDimensionStatesDetails.
        A filter to return only alarm state entries that match the exact set of specified dimension key-value pairs.
        If you specify `\"availabilityDomain\": \"phx-ad-1\"` but the alarm state entry corresponds to the set `\"availabilityDomain\": \"phx-ad-1\"`
        and `\"resourceId\": \"ocid1.instance.region1.phx.exampleuniqueID\"`, then no results are returned.


        :param dimension_filters: The dimension_filters of this RetrieveDimensionStatesDetails.
        :type: dict(str, str)
        """
        self._dimension_filters = dimension_filters

    @property
    def status(self):
        """
        Gets the status of this RetrieveDimensionStatesDetails.
        A filter to return only alarm state entries that match the status value.
        Example: `FIRING`


        :return: The status of this RetrieveDimensionStatesDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RetrieveDimensionStatesDetails.
        A filter to return only alarm state entries that match the status value.
        Example: `FIRING`


        :param status: The status of this RetrieveDimensionStatesDetails.
        :type: str
        """
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
