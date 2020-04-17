# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EdgeSubnet(object):
    """
    The details about an edge node subnet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EdgeSubnet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr:
            The value to assign to the cidr property of this EdgeSubnet.
        :type cidr: str

        :param time_modified:
            The value to assign to the time_modified property of this EdgeSubnet.
        :type time_modified: datetime

        :param region:
            The value to assign to the region property of this EdgeSubnet.
        :type region: str

        """
        self.swagger_types = {
            'cidr': 'str',
            'time_modified': 'datetime',
            'region': 'str'
        }

        self.attribute_map = {
            'cidr': 'cidr',
            'time_modified': 'timeModified',
            'region': 'region'
        }

        self._cidr = None
        self._time_modified = None
        self._region = None

    @property
    def cidr(self):
        """
        Gets the cidr of this EdgeSubnet.
        An edge node subnet. This can include /24 or /8 addresses.


        :return: The cidr of this EdgeSubnet.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """
        Sets the cidr of this EdgeSubnet.
        An edge node subnet. This can include /24 or /8 addresses.


        :param cidr: The cidr of this EdgeSubnet.
        :type: str
        """
        self._cidr = cidr

    @property
    def time_modified(self):
        """
        Gets the time_modified of this EdgeSubnet.
        The date and time the last change was made to the indicated edge node subnet, expressed in RFC 3339 timestamp format.


        :return: The time_modified of this EdgeSubnet.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this EdgeSubnet.
        The date and time the last change was made to the indicated edge node subnet, expressed in RFC 3339 timestamp format.


        :param time_modified: The time_modified of this EdgeSubnet.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def region(self):
        """
        Gets the region of this EdgeSubnet.
        The name of the region containing the indicated subnet.


        :return: The region of this EdgeSubnet.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this EdgeSubnet.
        The name of the region containing the indicated subnet.


        :param region: The region of this EdgeSubnet.
        :type: str
        """
        self._region = region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
