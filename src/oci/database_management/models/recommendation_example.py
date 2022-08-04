# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecommendationExample(object):
    """
    An example of the recommendation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RecommendationExample object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lines:
            The value to assign to the lines property of this RecommendationExample.
        :type lines: list[oci.database_management.models.RecommendationExampleLine]

        """
        self.swagger_types = {
            'lines': 'list[RecommendationExampleLine]'
        }

        self.attribute_map = {
            'lines': 'lines'
        }

        self._lines = None

    @property
    def lines(self):
        """
        Gets the lines of this RecommendationExample.
        The list of examples for the recommendation.


        :return: The lines of this RecommendationExample.
        :rtype: list[oci.database_management.models.RecommendationExampleLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this RecommendationExample.
        The list of examples for the recommendation.


        :param lines: The lines of this RecommendationExample.
        :type: list[oci.database_management.models.RecommendationExampleLine]
        """
        self._lines = lines

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
