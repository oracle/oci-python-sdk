# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseInsights(object):
    """
    Logical grouping used for Operations Insights database-targeted operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseInsights object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_insights:
            The value to assign to the database_insights property of this DatabaseInsights.
        :type database_insights: object

        """
        self.swagger_types = {
            'database_insights': 'object'
        }

        self.attribute_map = {
            'database_insights': 'databaseInsights'
        }

        self._database_insights = None

    @property
    def database_insights(self):
        """
        Gets the database_insights of this DatabaseInsights.
        Database Insights Object.


        :return: The database_insights of this DatabaseInsights.
        :rtype: object
        """
        return self._database_insights

    @database_insights.setter
    def database_insights(self, database_insights):
        """
        Sets the database_insights of this DatabaseInsights.
        Database Insights Object.


        :param database_insights: The database_insights of this DatabaseInsights.
        :type: object
        """
        self._database_insights = database_insights

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
