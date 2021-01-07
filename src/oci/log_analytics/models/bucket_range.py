# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BucketRange(object):
    """
    Represents querylanguage bucket command input arguments in parse output.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BucketRange object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lower:
            The value to assign to the lower property of this BucketRange.
        :type lower: float

        :param upper:
            The value to assign to the upper property of this BucketRange.
        :type upper: float

        :param alias:
            The value to assign to the alias property of this BucketRange.
        :type alias: str

        """
        self.swagger_types = {
            'lower': 'float',
            'upper': 'float',
            'alias': 'str'
        }

        self.attribute_map = {
            'lower': 'lower',
            'upper': 'upper',
            'alias': 'alias'
        }

        self._lower = None
        self._upper = None
        self._alias = None

    @property
    def lower(self):
        """
        Gets the lower of this BucketRange.
        Lower bound of the bucket range specified in the querystring for the numeric field referenced in tbe bucket command.


        :return: The lower of this BucketRange.
        :rtype: float
        """
        return self._lower

    @lower.setter
    def lower(self, lower):
        """
        Sets the lower of this BucketRange.
        Lower bound of the bucket range specified in the querystring for the numeric field referenced in tbe bucket command.


        :param lower: The lower of this BucketRange.
        :type: float
        """
        self._lower = lower

    @property
    def upper(self):
        """
        Gets the upper of this BucketRange.
        Upper bound of the bucket range specified in the querystring for the numeric field referenced in tbe bucket command.


        :return: The upper of this BucketRange.
        :rtype: float
        """
        return self._upper

    @upper.setter
    def upper(self, upper):
        """
        Sets the upper of this BucketRange.
        Upper bound of the bucket range specified in the querystring for the numeric field referenced in tbe bucket command.


        :param upper: The upper of this BucketRange.
        :type: float
        """
        self._upper = upper

    @property
    def alias(self):
        """
        Gets the alias of this BucketRange.
        Optional alias of the bucket range if specified in the querystring.


        :return: The alias of this BucketRange.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this BucketRange.
        Optional alias of the bucket range if specified in the querystring.


        :param alias: The alias of this BucketRange.
        :type: str
        """
        self._alias = alias

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
