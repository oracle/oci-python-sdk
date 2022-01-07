# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourceEntityType(object):
    """
    LogAnalyticsSourceEntityType
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourceEntityType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsSourceEntityType.
        :type source_id: int

        :param entity_type:
            The value to assign to the entity_type property of this LogAnalyticsSourceEntityType.
        :type entity_type: str

        :param entity_type_category:
            The value to assign to the entity_type_category property of this LogAnalyticsSourceEntityType.
        :type entity_type_category: str

        :param entity_type_display_name:
            The value to assign to the entity_type_display_name property of this LogAnalyticsSourceEntityType.
        :type entity_type_display_name: str

        """
        self.swagger_types = {
            'source_id': 'int',
            'entity_type': 'str',
            'entity_type_category': 'str',
            'entity_type_display_name': 'str'
        }

        self.attribute_map = {
            'source_id': 'sourceId',
            'entity_type': 'entityType',
            'entity_type_category': 'entityTypeCategory',
            'entity_type_display_name': 'entityTypeDisplayName'
        }

        self._source_id = None
        self._entity_type = None
        self._entity_type_category = None
        self._entity_type_display_name = None

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsSourceEntityType.
        The source unique identifier.


        :return: The source_id of this LogAnalyticsSourceEntityType.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsSourceEntityType.
        The source unique identifier.


        :param source_id: The source_id of this LogAnalyticsSourceEntityType.
        :type: int
        """
        self._source_id = source_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this LogAnalyticsSourceEntityType.
        The entity type.


        :return: The entity_type of this LogAnalyticsSourceEntityType.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this LogAnalyticsSourceEntityType.
        The entity type.


        :param entity_type: The entity_type of this LogAnalyticsSourceEntityType.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def entity_type_category(self):
        """
        Gets the entity_type_category of this LogAnalyticsSourceEntityType.
        The type category.


        :return: The entity_type_category of this LogAnalyticsSourceEntityType.
        :rtype: str
        """
        return self._entity_type_category

    @entity_type_category.setter
    def entity_type_category(self, entity_type_category):
        """
        Sets the entity_type_category of this LogAnalyticsSourceEntityType.
        The type category.


        :param entity_type_category: The entity_type_category of this LogAnalyticsSourceEntityType.
        :type: str
        """
        self._entity_type_category = entity_type_category

    @property
    def entity_type_display_name(self):
        """
        Gets the entity_type_display_name of this LogAnalyticsSourceEntityType.
        The entity type display name.


        :return: The entity_type_display_name of this LogAnalyticsSourceEntityType.
        :rtype: str
        """
        return self._entity_type_display_name

    @entity_type_display_name.setter
    def entity_type_display_name(self, entity_type_display_name):
        """
        Sets the entity_type_display_name of this LogAnalyticsSourceEntityType.
        The entity type display name.


        :param entity_type_display_name: The entity_type_display_name of this LogAnalyticsSourceEntityType.
        :type: str
        """
        self._entity_type_display_name = entity_type_display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
