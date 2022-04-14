# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchMonitoredResourceMembersDetails(object):
    """
    The search criteria for listing monitored resource member targets.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchMonitoredResourceMembersDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_resource_id:
            The value to assign to the destination_resource_id property of this SearchMonitoredResourceMembersDetails.
        :type destination_resource_id: str

        :param limit_level:
            The value to assign to the limit_level property of this SearchMonitoredResourceMembersDetails.
        :type limit_level: int

        """
        self.swagger_types = {
            'destination_resource_id': 'str',
            'limit_level': 'int'
        }

        self.attribute_map = {
            'destination_resource_id': 'destinationResourceId',
            'limit_level': 'limitLevel'
        }

        self._destination_resource_id = None
        self._limit_level = None

    @property
    def destination_resource_id(self):
        """
        Gets the destination_resource_id of this SearchMonitoredResourceMembersDetails.
        Destination Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The destination_resource_id of this SearchMonitoredResourceMembersDetails.
        :rtype: str
        """
        return self._destination_resource_id

    @destination_resource_id.setter
    def destination_resource_id(self, destination_resource_id):
        """
        Sets the destination_resource_id of this SearchMonitoredResourceMembersDetails.
        Destination Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param destination_resource_id: The destination_resource_id of this SearchMonitoredResourceMembersDetails.
        :type: str
        """
        self._destination_resource_id = destination_resource_id

    @property
    def limit_level(self):
        """
        Gets the limit_level of this SearchMonitoredResourceMembersDetails.
        The field which determines the depth of hierarchy while searching for members


        :return: The limit_level of this SearchMonitoredResourceMembersDetails.
        :rtype: int
        """
        return self._limit_level

    @limit_level.setter
    def limit_level(self, limit_level):
        """
        Sets the limit_level of this SearchMonitoredResourceMembersDetails.
        The field which determines the depth of hierarchy while searching for members


        :param limit_level: The limit_level of this SearchMonitoredResourceMembersDetails.
        :type: int
        """
        self._limit_level = limit_level

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
