# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppCatalogListingSummary(object):
    """
    A summary of a listing.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppCatalogListingSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_id:
            The value to assign to the listing_id property of this AppCatalogListingSummary.
        :type listing_id: str

        :param display_name:
            The value to assign to the display_name property of this AppCatalogListingSummary.
        :type display_name: str

        :param summary:
            The value to assign to the summary property of this AppCatalogListingSummary.
        :type summary: str

        :param publisher_name:
            The value to assign to the publisher_name property of this AppCatalogListingSummary.
        :type publisher_name: str

        """
        self.swagger_types = {
            'listing_id': 'str',
            'display_name': 'str',
            'summary': 'str',
            'publisher_name': 'str'
        }

        self.attribute_map = {
            'listing_id': 'listingId',
            'display_name': 'displayName',
            'summary': 'summary',
            'publisher_name': 'publisherName'
        }

        self._listing_id = None
        self._display_name = None
        self._summary = None
        self._publisher_name = None

    @property
    def listing_id(self):
        """
        Gets the listing_id of this AppCatalogListingSummary.
        the region free ocid of the listing resource.


        :return: The listing_id of this AppCatalogListingSummary.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this AppCatalogListingSummary.
        the region free ocid of the listing resource.


        :param listing_id: The listing_id of this AppCatalogListingSummary.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def display_name(self):
        """
        Gets the display_name of this AppCatalogListingSummary.
        The display name of the listing.


        :return: The display_name of this AppCatalogListingSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AppCatalogListingSummary.
        The display name of the listing.


        :param display_name: The display_name of this AppCatalogListingSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def summary(self):
        """
        Gets the summary of this AppCatalogListingSummary.
        The short summary for the listing.


        :return: The summary of this AppCatalogListingSummary.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this AppCatalogListingSummary.
        The short summary for the listing.


        :param summary: The summary of this AppCatalogListingSummary.
        :type: str
        """
        self._summary = summary

    @property
    def publisher_name(self):
        """
        Gets the publisher_name of this AppCatalogListingSummary.
        The name of the publisher who published this listing.


        :return: The publisher_name of this AppCatalogListingSummary.
        :rtype: str
        """
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, publisher_name):
        """
        Sets the publisher_name of this AppCatalogListingSummary.
        The name of the publisher who published this listing.


        :param publisher_name: The publisher_name of this AppCatalogListingSummary.
        :type: str
        """
        self._publisher_name = publisher_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
