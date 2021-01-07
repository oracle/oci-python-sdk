# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecommendationCount(object):
    """
    The count of recommendations in a category, grouped by importance.
    """

    #: A constant which can be used with the importance property of a RecommendationCount.
    #: This constant has a value of "CRITICAL"
    IMPORTANCE_CRITICAL = "CRITICAL"

    #: A constant which can be used with the importance property of a RecommendationCount.
    #: This constant has a value of "HIGH"
    IMPORTANCE_HIGH = "HIGH"

    #: A constant which can be used with the importance property of a RecommendationCount.
    #: This constant has a value of "MODERATE"
    IMPORTANCE_MODERATE = "MODERATE"

    #: A constant which can be used with the importance property of a RecommendationCount.
    #: This constant has a value of "LOW"
    IMPORTANCE_LOW = "LOW"

    #: A constant which can be used with the importance property of a RecommendationCount.
    #: This constant has a value of "MINOR"
    IMPORTANCE_MINOR = "MINOR"

    def __init__(self, **kwargs):
        """
        Initializes a new RecommendationCount object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param importance:
            The value to assign to the importance property of this RecommendationCount.
            Allowed values for this property are: "CRITICAL", "HIGH", "MODERATE", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type importance: str

        :param count:
            The value to assign to the count property of this RecommendationCount.
        :type count: int

        """
        self.swagger_types = {
            'importance': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'importance': 'importance',
            'count': 'count'
        }

        self._importance = None
        self._count = None

    @property
    def importance(self):
        """
        **[Required]** Gets the importance of this RecommendationCount.
        The level of importance assigned to the recommendation.

        Allowed values for this property are: "CRITICAL", "HIGH", "MODERATE", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The importance of this RecommendationCount.
        :rtype: str
        """
        return self._importance

    @importance.setter
    def importance(self, importance):
        """
        Sets the importance of this RecommendationCount.
        The level of importance assigned to the recommendation.


        :param importance: The importance of this RecommendationCount.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MODERATE", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(importance, allowed_values):
            importance = 'UNKNOWN_ENUM_VALUE'
        self._importance = importance

    @property
    def count(self):
        """
        **[Required]** Gets the count of this RecommendationCount.
        The count of recommendations.


        :return: The count of this RecommendationCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this RecommendationCount.
        The count of recommendations.


        :param count: The count of this RecommendationCount.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
