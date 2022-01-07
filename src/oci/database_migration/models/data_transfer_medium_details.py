# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataTransferMediumDetails(object):
    """
    Data Transfer Medium details for the Migration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataTransferMediumDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_link_details:
            The value to assign to the database_link_details property of this DataTransferMediumDetails.
        :type database_link_details: oci.database_migration.models.DatabaseLinkDetails

        :param object_storage_details:
            The value to assign to the object_storage_details property of this DataTransferMediumDetails.
        :type object_storage_details: oci.database_migration.models.ObjectStoreBucket

        """
        self.swagger_types = {
            'database_link_details': 'DatabaseLinkDetails',
            'object_storage_details': 'ObjectStoreBucket'
        }

        self.attribute_map = {
            'database_link_details': 'databaseLinkDetails',
            'object_storage_details': 'objectStorageDetails'
        }

        self._database_link_details = None
        self._object_storage_details = None

    @property
    def database_link_details(self):
        """
        Gets the database_link_details of this DataTransferMediumDetails.

        :return: The database_link_details of this DataTransferMediumDetails.
        :rtype: oci.database_migration.models.DatabaseLinkDetails
        """
        return self._database_link_details

    @database_link_details.setter
    def database_link_details(self, database_link_details):
        """
        Sets the database_link_details of this DataTransferMediumDetails.

        :param database_link_details: The database_link_details of this DataTransferMediumDetails.
        :type: oci.database_migration.models.DatabaseLinkDetails
        """
        self._database_link_details = database_link_details

    @property
    def object_storage_details(self):
        """
        Gets the object_storage_details of this DataTransferMediumDetails.

        :return: The object_storage_details of this DataTransferMediumDetails.
        :rtype: oci.database_migration.models.ObjectStoreBucket
        """
        return self._object_storage_details

    @object_storage_details.setter
    def object_storage_details(self, object_storage_details):
        """
        Sets the object_storage_details of this DataTransferMediumDetails.

        :param object_storage_details: The object_storage_details of this DataTransferMediumDetails.
        :type: oci.database_migration.models.ObjectStoreBucket
        """
        self._object_storage_details = object_storage_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
