# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdvisorReportLocationDetails(object):
    """
    Details to access Pre-Migration Advisor report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdvisorReportLocationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_storage_details:
            The value to assign to the object_storage_details property of this AdvisorReportLocationDetails.
        :type object_storage_details: oci.database_migration.models.AdvisorReportBucketDetails

        :param location_in_source:
            The value to assign to the location_in_source property of this AdvisorReportLocationDetails.
        :type location_in_source: str

        """
        self.swagger_types = {
            'object_storage_details': 'AdvisorReportBucketDetails',
            'location_in_source': 'str'
        }

        self.attribute_map = {
            'object_storage_details': 'objectStorageDetails',
            'location_in_source': 'locationInSource'
        }

        self._object_storage_details = None
        self._location_in_source = None

    @property
    def object_storage_details(self):
        """
        Gets the object_storage_details of this AdvisorReportLocationDetails.

        :return: The object_storage_details of this AdvisorReportLocationDetails.
        :rtype: oci.database_migration.models.AdvisorReportBucketDetails
        """
        return self._object_storage_details

    @object_storage_details.setter
    def object_storage_details(self, object_storage_details):
        """
        Sets the object_storage_details of this AdvisorReportLocationDetails.

        :param object_storage_details: The object_storage_details of this AdvisorReportLocationDetails.
        :type: oci.database_migration.models.AdvisorReportBucketDetails
        """
        self._object_storage_details = object_storage_details

    @property
    def location_in_source(self):
        """
        Gets the location_in_source of this AdvisorReportLocationDetails.
        Path in the Source Registered Connection where the Pre-Migration advisor report can be accessed.


        :return: The location_in_source of this AdvisorReportLocationDetails.
        :rtype: str
        """
        return self._location_in_source

    @location_in_source.setter
    def location_in_source(self, location_in_source):
        """
        Sets the location_in_source of this AdvisorReportLocationDetails.
        Path in the Source Registered Connection where the Pre-Migration advisor report can be accessed.


        :param location_in_source: The location_in_source of this AdvisorReportLocationDetails.
        :type: str
        """
        self._location_in_source = location_in_source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
