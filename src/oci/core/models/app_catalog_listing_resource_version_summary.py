# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppCatalogListingResourceVersionSummary(object):
    """
    Listing Resource Version summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppCatalogListingResourceVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_id:
            The value to assign to the listing_id property of this AppCatalogListingResourceVersionSummary.
        :type listing_id: str

        :param time_published:
            The value to assign to the time_published property of this AppCatalogListingResourceVersionSummary.
        :type time_published: datetime

        :param listing_resource_id:
            The value to assign to the listing_resource_id property of this AppCatalogListingResourceVersionSummary.
        :type listing_resource_id: str

        :param listing_resource_version:
            The value to assign to the listing_resource_version property of this AppCatalogListingResourceVersionSummary.
        :type listing_resource_version: str

        """
        self.swagger_types = {
            'listing_id': 'str',
            'time_published': 'datetime',
            'listing_resource_id': 'str',
            'listing_resource_version': 'str'
        }

        self.attribute_map = {
            'listing_id': 'listingId',
            'time_published': 'timePublished',
            'listing_resource_id': 'listingResourceId',
            'listing_resource_version': 'listingResourceVersion'
        }

        self._listing_id = None
        self._time_published = None
        self._listing_resource_id = None
        self._listing_resource_version = None

    @property
    def listing_id(self):
        """
        Gets the listing_id of this AppCatalogListingResourceVersionSummary.
        The OCID of the listing this resource version belongs to.


        :return: The listing_id of this AppCatalogListingResourceVersionSummary.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this AppCatalogListingResourceVersionSummary.
        The OCID of the listing this resource version belongs to.


        :param listing_id: The listing_id of this AppCatalogListingResourceVersionSummary.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def time_published(self):
        """
        Gets the time_published of this AppCatalogListingResourceVersionSummary.
        Date and time the listing resource version was published, in RFC3339 format.
        Example: `2018-03-20T12:32:53.532Z`


        :return: The time_published of this AppCatalogListingResourceVersionSummary.
        :rtype: datetime
        """
        return self._time_published

    @time_published.setter
    def time_published(self, time_published):
        """
        Sets the time_published of this AppCatalogListingResourceVersionSummary.
        Date and time the listing resource version was published, in RFC3339 format.
        Example: `2018-03-20T12:32:53.532Z`


        :param time_published: The time_published of this AppCatalogListingResourceVersionSummary.
        :type: datetime
        """
        self._time_published = time_published

    @property
    def listing_resource_id(self):
        """
        Gets the listing_resource_id of this AppCatalogListingResourceVersionSummary.
        OCID of the listing resource.


        :return: The listing_resource_id of this AppCatalogListingResourceVersionSummary.
        :rtype: str
        """
        return self._listing_resource_id

    @listing_resource_id.setter
    def listing_resource_id(self, listing_resource_id):
        """
        Sets the listing_resource_id of this AppCatalogListingResourceVersionSummary.
        OCID of the listing resource.


        :param listing_resource_id: The listing_resource_id of this AppCatalogListingResourceVersionSummary.
        :type: str
        """
        self._listing_resource_id = listing_resource_id

    @property
    def listing_resource_version(self):
        """
        Gets the listing_resource_version of this AppCatalogListingResourceVersionSummary.
        Resource Version.


        :return: The listing_resource_version of this AppCatalogListingResourceVersionSummary.
        :rtype: str
        """
        return self._listing_resource_version

    @listing_resource_version.setter
    def listing_resource_version(self, listing_resource_version):
        """
        Sets the listing_resource_version of this AppCatalogListingResourceVersionSummary.
        Resource Version.


        :param listing_resource_version: The listing_resource_version of this AppCatalogListingResourceVersionSummary.
        :type: str
        """
        self._listing_resource_version = listing_resource_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
