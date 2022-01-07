# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LevelConfiguration(object):
    """
    Details about the configuration level for the recommendation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LevelConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recommendation_id:
            The value to assign to the recommendation_id property of this LevelConfiguration.
        :type recommendation_id: str

        :param level:
            The value to assign to the level property of this LevelConfiguration.
        :type level: str

        """
        self.swagger_types = {
            'recommendation_id': 'str',
            'level': 'str'
        }

        self.attribute_map = {
            'recommendation_id': 'recommendationId',
            'level': 'level'
        }

        self._recommendation_id = None
        self._level = None

    @property
    def recommendation_id(self):
        """
        Gets the recommendation_id of this LevelConfiguration.
        The unique OCID of the recommendation.


        :return: The recommendation_id of this LevelConfiguration.
        :rtype: str
        """
        return self._recommendation_id

    @recommendation_id.setter
    def recommendation_id(self, recommendation_id):
        """
        Sets the recommendation_id of this LevelConfiguration.
        The unique OCID of the recommendation.


        :param recommendation_id: The recommendation_id of this LevelConfiguration.
        :type: str
        """
        self._recommendation_id = recommendation_id

    @property
    def level(self):
        """
        Gets the level of this LevelConfiguration.
        The pre-defined profile level.


        :return: The level of this LevelConfiguration.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this LevelConfiguration.
        The pre-defined profile level.


        :param level: The level of this LevelConfiguration.
        :type: str
        """
        self._level = level

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
