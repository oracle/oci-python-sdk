# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertLogCountSummary(object):
    """
    The details for one alert log count entry.
    """

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "UNKNOWN"
    CATEGORY_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "INCIDENT_ERROR"
    CATEGORY_INCIDENT_ERROR = "INCIDENT_ERROR"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "ERROR"
    CATEGORY_ERROR = "ERROR"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "WARNING"
    CATEGORY_WARNING = "WARNING"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "NOTIFICATION"
    CATEGORY_NOTIFICATION = "NOTIFICATION"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "TRACE"
    CATEGORY_TRACE = "TRACE"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "CRITICAL"
    CATEGORY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "SEVERE"
    CATEGORY_SEVERE = "SEVERE"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "IMPORTANT"
    CATEGORY_IMPORTANT = "IMPORTANT"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "NORMAL"
    CATEGORY_NORMAL = "NORMAL"

    #: A constant which can be used with the category property of a AlertLogCountSummary.
    #: This constant has a value of "OTHER"
    CATEGORY_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new AlertLogCountSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param category:
            The value to assign to the category property of this AlertLogCountSummary.
            Allowed values for this property are: "UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type category: str

        :param count:
            The value to assign to the count property of this AlertLogCountSummary.
        :type count: int

        """
        self.swagger_types = {
            'category': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'category': 'category',
            'count': 'count'
        }

        self._category = None
        self._count = None

    @property
    def category(self):
        """
        **[Required]** Gets the category of this AlertLogCountSummary.
        The category of different alert logs.

        Allowed values for this property are: "UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The category of this AlertLogCountSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this AlertLogCountSummary.
        The category of different alert logs.


        :param category: The category of this AlertLogCountSummary.
        :type: str
        """
        allowed_values = ["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "OTHER"]
        if not value_allowed_none_or_none_sentinel(category, allowed_values):
            category = 'UNKNOWN_ENUM_VALUE'
        self._category = category

    @property
    def count(self):
        """
        **[Required]** Gets the count of this AlertLogCountSummary.
        The count of alert logs with specific category.


        :return: The count of this AlertLogCountSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this AlertLogCountSummary.
        The count of alert logs with specific category.


        :param count: The count of this AlertLogCountSummary.
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
