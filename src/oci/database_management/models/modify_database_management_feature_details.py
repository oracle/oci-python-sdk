# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModifyDatabaseManagementFeatureDetails(object):
    """
    The details required to modify a Database Management feature for an Oracle cloud database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModifyDatabaseManagementFeatureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_details:
            The value to assign to the feature_details property of this ModifyDatabaseManagementFeatureDetails.
        :type feature_details: oci.database_management.models.DatabaseFeatureDetails

        """
        self.swagger_types = {
            'feature_details': 'DatabaseFeatureDetails'
        }
        self.attribute_map = {
            'feature_details': 'featureDetails'
        }
        self._feature_details = None

    @property
    def feature_details(self):
        """
        **[Required]** Gets the feature_details of this ModifyDatabaseManagementFeatureDetails.

        :return: The feature_details of this ModifyDatabaseManagementFeatureDetails.
        :rtype: oci.database_management.models.DatabaseFeatureDetails
        """
        return self._feature_details

    @feature_details.setter
    def feature_details(self, feature_details):
        """
        Sets the feature_details of this ModifyDatabaseManagementFeatureDetails.

        :param feature_details: The feature_details of this ModifyDatabaseManagementFeatureDetails.
        :type: oci.database_management.models.DatabaseFeatureDetails
        """
        self._feature_details = feature_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
