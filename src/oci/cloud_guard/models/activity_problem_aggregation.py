# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActivityProblemAggregation(object):
    """
    Provides the dimensions and their corresponding count.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ActivityProblemAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimensions_map:
            The value to assign to the dimensions_map property of this ActivityProblemAggregation.
        :type dimensions_map: dict(str, str)

        :param political_location:
            The value to assign to the political_location property of this ActivityProblemAggregation.
        :type political_location: oci.cloud_guard.models.PoliticalLocation

        :param geographical_location:
            The value to assign to the geographical_location property of this ActivityProblemAggregation.
        :type geographical_location: oci.cloud_guard.models.GeographicalLocation

        :param count:
            The value to assign to the count property of this ActivityProblemAggregation.
        :type count: int

        """
        self.swagger_types = {
            'dimensions_map': 'dict(str, str)',
            'political_location': 'PoliticalLocation',
            'geographical_location': 'GeographicalLocation',
            'count': 'int'
        }

        self.attribute_map = {
            'dimensions_map': 'dimensionsMap',
            'political_location': 'politicalLocation',
            'geographical_location': 'geographicalLocation',
            'count': 'count'
        }

        self._dimensions_map = None
        self._political_location = None
        self._geographical_location = None
        self._count = None

    @property
    def dimensions_map(self):
        """
        **[Required]** Gets the dimensions_map of this ActivityProblemAggregation.
        The key-value pairs of dimensions and their names.


        :return: The dimensions_map of this ActivityProblemAggregation.
        :rtype: dict(str, str)
        """
        return self._dimensions_map

    @dimensions_map.setter
    def dimensions_map(self, dimensions_map):
        """
        Sets the dimensions_map of this ActivityProblemAggregation.
        The key-value pairs of dimensions and their names.


        :param dimensions_map: The dimensions_map of this ActivityProblemAggregation.
        :type: dict(str, str)
        """
        self._dimensions_map = dimensions_map

    @property
    def political_location(self):
        """
        **[Required]** Gets the political_location of this ActivityProblemAggregation.

        :return: The political_location of this ActivityProblemAggregation.
        :rtype: oci.cloud_guard.models.PoliticalLocation
        """
        return self._political_location

    @political_location.setter
    def political_location(self, political_location):
        """
        Sets the political_location of this ActivityProblemAggregation.

        :param political_location: The political_location of this ActivityProblemAggregation.
        :type: oci.cloud_guard.models.PoliticalLocation
        """
        self._political_location = political_location

    @property
    def geographical_location(self):
        """
        **[Required]** Gets the geographical_location of this ActivityProblemAggregation.

        :return: The geographical_location of this ActivityProblemAggregation.
        :rtype: oci.cloud_guard.models.GeographicalLocation
        """
        return self._geographical_location

    @geographical_location.setter
    def geographical_location(self, geographical_location):
        """
        Sets the geographical_location of this ActivityProblemAggregation.

        :param geographical_location: The geographical_location of this ActivityProblemAggregation.
        :type: oci.cloud_guard.models.GeographicalLocation
        """
        self._geographical_location = geographical_location

    @property
    def count(self):
        """
        **[Required]** Gets the count of this ActivityProblemAggregation.
        The number of occurences with given dimension/s


        :return: The count of this ActivityProblemAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ActivityProblemAggregation.
        The number of occurences with given dimension/s


        :param count: The count of this ActivityProblemAggregation.
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
