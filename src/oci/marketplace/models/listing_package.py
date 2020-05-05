# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListingPackage(object):
    """
    A base object for all types of listing packages.
    """

    #: A constant which can be used with the package_type property of a ListingPackage.
    #: This constant has a value of "ORCHESTRATION"
    PACKAGE_TYPE_ORCHESTRATION = "ORCHESTRATION"

    #: A constant which can be used with the package_type property of a ListingPackage.
    #: This constant has a value of "IMAGE"
    PACKAGE_TYPE_IMAGE = "IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new ListingPackage object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace.models.OrchestrationListingPackage`
        * :class:`~oci.marketplace.models.ImageListingPackage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this ListingPackage.
        :type description: str

        :param listing_id:
            The value to assign to the listing_id property of this ListingPackage.
        :type listing_id: str

        :param version:
            The value to assign to the version property of this ListingPackage.
        :type version: str

        :param package_type:
            The value to assign to the package_type property of this ListingPackage.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param pricing:
            The value to assign to the pricing property of this ListingPackage.
        :type pricing: PricingModel

        :param resource_id:
            The value to assign to the resource_id property of this ListingPackage.
        :type resource_id: str

        :param time_created:
            The value to assign to the time_created property of this ListingPackage.
        :type time_created: datetime

        """
        self.swagger_types = {
            'description': 'str',
            'listing_id': 'str',
            'version': 'str',
            'package_type': 'str',
            'pricing': 'PricingModel',
            'resource_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'description': 'description',
            'listing_id': 'listingId',
            'version': 'version',
            'package_type': 'packageType',
            'pricing': 'pricing',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated'
        }

        self._description = None
        self._listing_id = None
        self._version = None
        self._package_type = None
        self._pricing = None
        self._resource_id = None
        self._time_created = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['packageType']

        if type == 'ORCHESTRATION':
            return 'OrchestrationListingPackage'

        if type == 'IMAGE':
            return 'ImageListingPackage'
        else:
            return 'ListingPackage'

    @property
    def description(self):
        """
        Gets the description of this ListingPackage.
        Description of this package.


        :return: The description of this ListingPackage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ListingPackage.
        Description of this package.


        :param description: The description of this ListingPackage.
        :type: str
        """
        self._description = description

    @property
    def listing_id(self):
        """
        **[Required]** Gets the listing_id of this ListingPackage.
        The ID of the listing this package belongs to.


        :return: The listing_id of this ListingPackage.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this ListingPackage.
        The ID of the listing this package belongs to.


        :param listing_id: The listing_id of this ListingPackage.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ListingPackage.
        The package version.


        :return: The version of this ListingPackage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ListingPackage.
        The package version.


        :param version: The version of this ListingPackage.
        :type: str
        """
        self._version = version

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this ListingPackage.
        The specified package's type.

        Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this ListingPackage.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this ListingPackage.
        The specified package's type.


        :param package_type: The package_type of this ListingPackage.
        :type: str
        """
        allowed_values = ["ORCHESTRATION", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def pricing(self):
        """
        Gets the pricing of this ListingPackage.

        :return: The pricing of this ListingPackage.
        :rtype: PricingModel
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """
        Sets the pricing of this ListingPackage.

        :param pricing: The pricing of this ListingPackage.
        :type: PricingModel
        """
        self._pricing = pricing

    @property
    def resource_id(self):
        """
        Gets the resource_id of this ListingPackage.
        The unique identifier for the package resource.


        :return: The resource_id of this ListingPackage.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ListingPackage.
        The unique identifier for the package resource.


        :param resource_id: The resource_id of this ListingPackage.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def time_created(self):
        """
        Gets the time_created of this ListingPackage.
        The date and time this listing package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ListingPackage.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ListingPackage.
        The date and time this listing package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ListingPackage.
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
