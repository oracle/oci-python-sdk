# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLogAnalyticsEntityTypeDetails(object):
    """
    Log analytics entity type definition to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLogAnalyticsEntityTypeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param category:
            The value to assign to the category property of this UpdateLogAnalyticsEntityTypeDetails.
        :type category: str

        :param properties:
            The value to assign to the properties property of this UpdateLogAnalyticsEntityTypeDetails.
        :type properties: list[oci.log_analytics.models.EntityTypeProperty]

        """
        self.swagger_types = {
            'category': 'str',
            'properties': 'list[EntityTypeProperty]'
        }

        self.attribute_map = {
            'category': 'category',
            'properties': 'properties'
        }

        self._category = None
        self._properties = None

    @property
    def category(self):
        """
        Gets the category of this UpdateLogAnalyticsEntityTypeDetails.
        Log analytics entity type category. Category will be used for grouping and filtering.


        :return: The category of this UpdateLogAnalyticsEntityTypeDetails.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this UpdateLogAnalyticsEntityTypeDetails.
        Log analytics entity type category. Category will be used for grouping and filtering.


        :param category: The category of this UpdateLogAnalyticsEntityTypeDetails.
        :type: str
        """
        self._category = category

    @property
    def properties(self):
        """
        Gets the properties of this UpdateLogAnalyticsEntityTypeDetails.
        A single log analytics entity type property definition.


        :return: The properties of this UpdateLogAnalyticsEntityTypeDetails.
        :rtype: list[oci.log_analytics.models.EntityTypeProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateLogAnalyticsEntityTypeDetails.
        A single log analytics entity type property definition.


        :param properties: The properties of this UpdateLogAnalyticsEntityTypeDetails.
        :type: list[oci.log_analytics.models.EntityTypeProperty]
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
