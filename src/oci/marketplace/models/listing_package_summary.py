# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListingPackageSummary(object):
    """
    The model for a summary of a package.
    """

    #: A constant which can be used with the package_type property of a ListingPackageSummary.
    #: This constant has a value of "ORCHESTRATION"
    PACKAGE_TYPE_ORCHESTRATION = "ORCHESTRATION"

    #: A constant which can be used with the package_type property of a ListingPackageSummary.
    #: This constant has a value of "IMAGE"
    PACKAGE_TYPE_IMAGE = "IMAGE"

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

        :param package_type:
            The value to assign to the package_type property of this ListingPackageSummary.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param pricing:
            The value to assign to the pricing property of this ListingPackageSummary.
        :type pricing: oci.marketplace.models.PricingModel

        :param regions:
            The value to assign to the regions property of this ListingPackageSummary.
        :type regions: list[oci.marketplace.models.Region]

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
            'package_type': 'str',
            'pricing': 'PricingModel',
            'regions': 'list[Region]',
            'resource_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'listing_id': 'listingId',
            'package_version': 'packageVersion',
            'package_type': 'packageType',
            'pricing': 'pricing',
            'regions': 'regions',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated'
        }

        self._listing_id = None
        self._package_version = None
        self._package_type = None
        self._pricing = None
        self._regions = None
        self._resource_id = None
        self._time_created = None

    @property
    def listing_id(self):
        """
        Gets the listing_id of this ListingPackageSummary.
        The ID of the listing that the specified package belongs to.


        :return: The listing_id of this ListingPackageSummary.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this ListingPackageSummary.
        The ID of the listing that the specified package belongs to.


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
    def package_type(self):
        """
        Gets the package_type of this ListingPackageSummary.
        The specified package's type.

        Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this ListingPackageSummary.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this ListingPackageSummary.
        The specified package's type.


        :param package_type: The package_type of this ListingPackageSummary.
        :type: str
        """
        allowed_values = ["ORCHESTRATION", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def pricing(self):
        """
        Gets the pricing of this ListingPackageSummary.

        :return: The pricing of this ListingPackageSummary.
        :rtype: oci.marketplace.models.PricingModel
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """
        Sets the pricing of this ListingPackageSummary.

        :param pricing: The pricing of this ListingPackageSummary.
        :type: oci.marketplace.models.PricingModel
        """
        self._pricing = pricing

    @property
    def regions(self):
        """
        Gets the regions of this ListingPackageSummary.
        The regions where you can deploy the listing package. (Some packages have restrictions that limit their deployment to United States regions only.)


        :return: The regions of this ListingPackageSummary.
        :rtype: list[oci.marketplace.models.Region]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this ListingPackageSummary.
        The regions where you can deploy the listing package. (Some packages have restrictions that limit their deployment to United States regions only.)


        :param regions: The regions of this ListingPackageSummary.
        :type: list[oci.marketplace.models.Region]
        """
        self._regions = regions

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
