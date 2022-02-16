# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Outlier(object):
    """
    To capture all the Outlier details related to profiling
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Outlier object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param low:
            The value to assign to the low property of this Outlier.
        :type low: str

        :param high:
            The value to assign to the high property of this Outlier.
        :type high: str

        :param low_count:
            The value to assign to the low_count property of this Outlier.
        :type low_count: str

        :param high_count:
            The value to assign to the high_count property of this Outlier.
        :type high_count: str

        """
        self.swagger_types = {
            'low': 'str',
            'high': 'str',
            'low_count': 'str',
            'high_count': 'str'
        }

        self.attribute_map = {
            'low': 'low',
            'high': 'high',
            'low_count': 'lowCount',
            'high_count': 'highCount'
        }

        self._low = None
        self._high = None
        self._low_count = None
        self._high_count = None

    @property
    def low(self):
        """
        Gets the low of this Outlier.
        low value of outlier


        :return: The low of this Outlier.
        :rtype: str
        """
        return self._low

    @low.setter
    def low(self, low):
        """
        Sets the low of this Outlier.
        low value of outlier


        :param low: The low of this Outlier.
        :type: str
        """
        self._low = low

    @property
    def high(self):
        """
        Gets the high of this Outlier.
        high value of outlier


        :return: The high of this Outlier.
        :rtype: str
        """
        return self._high

    @high.setter
    def high(self, high):
        """
        Sets the high of this Outlier.
        high value of outlier


        :param high: The high of this Outlier.
        :type: str
        """
        self._high = high

    @property
    def low_count(self):
        """
        Gets the low_count of this Outlier.
        lowCount value of outlier


        :return: The low_count of this Outlier.
        :rtype: str
        """
        return self._low_count

    @low_count.setter
    def low_count(self, low_count):
        """
        Sets the low_count of this Outlier.
        lowCount value of outlier


        :param low_count: The low_count of this Outlier.
        :type: str
        """
        self._low_count = low_count

    @property
    def high_count(self):
        """
        Gets the high_count of this Outlier.
        highCount value of outlier


        :return: The high_count of this Outlier.
        :rtype: str
        """
        return self._high_count

    @high_count.setter
    def high_count(self, high_count):
        """
        Sets the high_count of this Outlier.
        highCount value of outlier


        :param high_count: The high_count of this Outlier.
        :type: str
        """
        self._high_count = high_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
