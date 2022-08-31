# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileStat(object):
    """
    To capture all the statistical data related to profiling.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileStat object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param confidence:
            The value to assign to the confidence property of this ProfileStat.
        :type confidence: int

        :param value:
            The value to assign to the value property of this ProfileStat.
        :type value: str

        """
        self.swagger_types = {
            'confidence': 'int',
            'value': 'str'
        }

        self.attribute_map = {
            'confidence': 'confidence',
            'value': 'value'
        }

        self._confidence = None
        self._value = None

    @property
    def confidence(self):
        """
        Gets the confidence of this ProfileStat.
        Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not whole data)


        :return: The confidence of this ProfileStat.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this ProfileStat.
        Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not whole data)


        :param confidence: The confidence of this ProfileStat.
        :type: int
        """
        self._confidence = confidence

    @property
    def value(self):
        """
        Gets the value of this ProfileStat.
        Value of the confidence of the profile result.


        :return: The value of this ProfileStat.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ProfileStat.
        Value of the confidence of the profile result.


        :param value: The value of this ProfileStat.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
