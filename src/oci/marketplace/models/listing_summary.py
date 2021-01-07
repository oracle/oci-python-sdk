# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListingSummary(object):
    """
    The model for a summary of an Oracle Cloud Infrastructure Marketplace listing.
    """

    #: A constant which can be used with the package_type property of a ListingSummary.
    #: This constant has a value of "ORCHESTRATION"
    PACKAGE_TYPE_ORCHESTRATION = "ORCHESTRATION"

    #: A constant which can be used with the package_type property of a ListingSummary.
    #: This constant has a value of "IMAGE"
    PACKAGE_TYPE_IMAGE = "IMAGE"

    #: A constant which can be used with the pricing_types property of a ListingSummary.
    #: This constant has a value of "FREE"
    PRICING_TYPES_FREE = "FREE"

    #: A constant which can be used with the pricing_types property of a ListingSummary.
    #: This constant has a value of "BYOL"
    PRICING_TYPES_BYOL = "BYOL"

    #: A constant which can be used with the pricing_types property of a ListingSummary.
    #: This constant has a value of "PAYGO"
    PRICING_TYPES_PAYGO = "PAYGO"

    def __init__(self, **kwargs):
        """
        Initializes a new ListingSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ListingSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this ListingSummary.
        :type name: str

        :param short_description:
            The value to assign to the short_description property of this ListingSummary.
        :type short_description: str

        :param tagline:
            The value to assign to the tagline property of this ListingSummary.
        :type tagline: str

        :param icon:
            The value to assign to the icon property of this ListingSummary.
        :type icon: oci.marketplace.models.UploadData

        :param package_type:
            The value to assign to the package_type property of this ListingSummary.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param pricing_types:
            The value to assign to the pricing_types property of this ListingSummary.
            Allowed values for items in this list are: "FREE", "BYOL", "PAYGO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pricing_types: list[str]

        :param regions:
            The value to assign to the regions property of this ListingSummary.
        :type regions: list[oci.marketplace.models.Region]

        :param is_featured:
            The value to assign to the is_featured property of this ListingSummary.
        :type is_featured: bool

        :param categories:
            The value to assign to the categories property of this ListingSummary.
        :type categories: list[str]

        :param publisher:
            The value to assign to the publisher property of this ListingSummary.
        :type publisher: oci.marketplace.models.PublisherSummary

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'short_description': 'str',
            'tagline': 'str',
            'icon': 'UploadData',
            'package_type': 'str',
            'pricing_types': 'list[str]',
            'regions': 'list[Region]',
            'is_featured': 'bool',
            'categories': 'list[str]',
            'publisher': 'PublisherSummary'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'short_description': 'shortDescription',
            'tagline': 'tagline',
            'icon': 'icon',
            'package_type': 'packageType',
            'pricing_types': 'pricingTypes',
            'regions': 'regions',
            'is_featured': 'isFeatured',
            'categories': 'categories',
            'publisher': 'publisher'
        }

        self._id = None
        self._name = None
        self._short_description = None
        self._tagline = None
        self._icon = None
        self._package_type = None
        self._pricing_types = None
        self._regions = None
        self._is_featured = None
        self._categories = None
        self._publisher = None

    @property
    def id(self):
        """
        Gets the id of this ListingSummary.
        The unique identifier for the listing in Marketplace.


        :return: The id of this ListingSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ListingSummary.
        The unique identifier for the listing in Marketplace.


        :param id: The id of this ListingSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ListingSummary.
        The name of the listing.


        :return: The name of this ListingSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ListingSummary.
        The name of the listing.


        :param name: The name of this ListingSummary.
        :type: str
        """
        self._name = name

    @property
    def short_description(self):
        """
        Gets the short_description of this ListingSummary.
        A short description of the listing.


        :return: The short_description of this ListingSummary.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this ListingSummary.
        A short description of the listing.


        :param short_description: The short_description of this ListingSummary.
        :type: str
        """
        self._short_description = short_description

    @property
    def tagline(self):
        """
        Gets the tagline of this ListingSummary.
        The tagline of the listing.


        :return: The tagline of this ListingSummary.
        :rtype: str
        """
        return self._tagline

    @tagline.setter
    def tagline(self, tagline):
        """
        Sets the tagline of this ListingSummary.
        The tagline of the listing.


        :param tagline: The tagline of this ListingSummary.
        :type: str
        """
        self._tagline = tagline

    @property
    def icon(self):
        """
        Gets the icon of this ListingSummary.

        :return: The icon of this ListingSummary.
        :rtype: oci.marketplace.models.UploadData
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this ListingSummary.

        :param icon: The icon of this ListingSummary.
        :type: oci.marketplace.models.UploadData
        """
        self._icon = icon

    @property
    def package_type(self):
        """
        Gets the package_type of this ListingSummary.
        The listing's package type.

        Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this ListingSummary.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this ListingSummary.
        The listing's package type.


        :param package_type: The package_type of this ListingSummary.
        :type: str
        """
        allowed_values = ["ORCHESTRATION", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def pricing_types(self):
        """
        Gets the pricing_types of this ListingSummary.
        Summary of the pricing types available across all packages in the listing.

        Allowed values for items in this list are: "FREE", "BYOL", "PAYGO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pricing_types of this ListingSummary.
        :rtype: list[str]
        """
        return self._pricing_types

    @pricing_types.setter
    def pricing_types(self, pricing_types):
        """
        Sets the pricing_types of this ListingSummary.
        Summary of the pricing types available across all packages in the listing.


        :param pricing_types: The pricing_types of this ListingSummary.
        :type: list[str]
        """
        allowed_values = ["FREE", "BYOL", "PAYGO"]
        if pricing_types:
            pricing_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in pricing_types]
        self._pricing_types = pricing_types

    @property
    def regions(self):
        """
        Gets the regions of this ListingSummary.
        The regions where you can deploy the listing. (Some listings have restrictions that limit their deployment to United States regions only.)


        :return: The regions of this ListingSummary.
        :rtype: list[oci.marketplace.models.Region]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this ListingSummary.
        The regions where you can deploy the listing. (Some listings have restrictions that limit their deployment to United States regions only.)


        :param regions: The regions of this ListingSummary.
        :type: list[oci.marketplace.models.Region]
        """
        self._regions = regions

    @property
    def is_featured(self):
        """
        Gets the is_featured of this ListingSummary.
        Indicates whether the listing is featured.


        :return: The is_featured of this ListingSummary.
        :rtype: bool
        """
        return self._is_featured

    @is_featured.setter
    def is_featured(self, is_featured):
        """
        Sets the is_featured of this ListingSummary.
        Indicates whether the listing is featured.


        :param is_featured: The is_featured of this ListingSummary.
        :type: bool
        """
        self._is_featured = is_featured

    @property
    def categories(self):
        """
        Gets the categories of this ListingSummary.
        Product categories that the listing belongs to.


        :return: The categories of this ListingSummary.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this ListingSummary.
        Product categories that the listing belongs to.


        :param categories: The categories of this ListingSummary.
        :type: list[str]
        """
        self._categories = categories

    @property
    def publisher(self):
        """
        Gets the publisher of this ListingSummary.

        :return: The publisher of this ListingSummary.
        :rtype: oci.marketplace.models.PublisherSummary
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this ListingSummary.

        :param publisher: The publisher of this ListingSummary.
        :type: oci.marketplace.models.PublisherSummary
        """
        self._publisher = publisher

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
