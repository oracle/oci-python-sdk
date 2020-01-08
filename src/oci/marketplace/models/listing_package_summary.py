# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListingPackageSummary(object):
    """
    The model for a summary of a package.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ListingPackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_id:
            The value to assign to the listing_id property of this ListingPackageSummary.
        :type listing_id: str

        :param package_version:
            The value to assign to the package_version property of this ListingPackageSummary.
        :type package_version: str

        :param resource_id:
            The value to assign to the resource_id property of this ListingPackageSummary.
        :type resource_id: str

        :param time_created:
            The value to assign to the time_created property of this ListingPackageSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'listing_id': 'str',
            'package_version': 'str',
            'resource_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'listing_id': 'listingId',
            'package_version': 'packageVersion',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated'
        }

        self._listing_id = None
        self._package_version = None
        self._resource_id = None
        self._time_created = None

    @property
    def listing_id(self):
        """
        Gets the listing_id of this ListingPackageSummary.
        The id of the listing the specified package belongs to.


        :return: The listing_id of this ListingPackageSummary.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this ListingPackageSummary.
        The id of the listing the specified package belongs to.


        :param listing_id: The listing_id of this ListingPackageSummary.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def package_version(self):
        """
        Gets the package_version of this ListingPackageSummary.
        The version of the specified package.


        :return: The package_version of this ListingPackageSummary.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this ListingPackageSummary.
        The version of the specified package.


        :param package_version: The package_version of this ListingPackageSummary.
        :type: str
        """
        self._package_version = package_version

    @property
    def resource_id(self):
        """
        Gets the resource_id of this ListingPackageSummary.
        The unique identifier for the package resource.


        :return: The resource_id of this ListingPackageSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ListingPackageSummary.
        The unique identifier for the package resource.


        :param resource_id: The resource_id of this ListingPackageSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def time_created(self):
        """
        Gets the time_created of this ListingPackageSummary.
        The date and time this listing package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ListingPackageSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ListingPackageSummary.
        The date and time this listing package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ListingPackageSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
