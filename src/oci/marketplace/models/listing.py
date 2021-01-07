# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Listing(object):
    """
    The model for an Oracle Cloud Infrastructure Marketplace listing.
    """

    #: A constant which can be used with the package_type property of a Listing.
    #: This constant has a value of "ORCHESTRATION"
    PACKAGE_TYPE_ORCHESTRATION = "ORCHESTRATION"

    #: A constant which can be used with the package_type property of a Listing.
    #: This constant has a value of "IMAGE"
    PACKAGE_TYPE_IMAGE = "IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new Listing object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Listing.
        :type id: str

        :param name:
            The value to assign to the name property of this Listing.
        :type name: str

        :param version:
            The value to assign to the version property of this Listing.
        :type version: str

        :param tagline:
            The value to assign to the tagline property of this Listing.
        :type tagline: str

        :param keywords:
            The value to assign to the keywords property of this Listing.
        :type keywords: str

        :param short_description:
            The value to assign to the short_description property of this Listing.
        :type short_description: str

        :param usage_information:
            The value to assign to the usage_information property of this Listing.
        :type usage_information: str

        :param long_description:
            The value to assign to the long_description property of this Listing.
        :type long_description: str

        :param license_model_description:
            The value to assign to the license_model_description property of this Listing.
        :type license_model_description: str

        :param system_requirements:
            The value to assign to the system_requirements property of this Listing.
        :type system_requirements: str

        :param time_released:
            The value to assign to the time_released property of this Listing.
        :type time_released: datetime

        :param release_notes:
            The value to assign to the release_notes property of this Listing.
        :type release_notes: str

        :param categories:
            The value to assign to the categories property of this Listing.
        :type categories: list[str]

        :param publisher:
            The value to assign to the publisher property of this Listing.
        :type publisher: oci.marketplace.models.Publisher

        :param languages:
            The value to assign to the languages property of this Listing.
        :type languages: list[oci.marketplace.models.Item]

        :param screenshots:
            The value to assign to the screenshots property of this Listing.
        :type screenshots: list[oci.marketplace.models.Screenshot]

        :param videos:
            The value to assign to the videos property of this Listing.
        :type videos: list[oci.marketplace.models.NamedLink]

        :param support_contacts:
            The value to assign to the support_contacts property of this Listing.
        :type support_contacts: list[oci.marketplace.models.SupportContact]

        :param support_links:
            The value to assign to the support_links property of this Listing.
        :type support_links: list[oci.marketplace.models.NamedLink]

        :param documentation_links:
            The value to assign to the documentation_links property of this Listing.
        :type documentation_links: list[oci.marketplace.models.DocumentationLink]

        :param icon:
            The value to assign to the icon property of this Listing.
        :type icon: oci.marketplace.models.UploadData

        :param banner:
            The value to assign to the banner property of this Listing.
        :type banner: oci.marketplace.models.UploadData

        :param regions:
            The value to assign to the regions property of this Listing.
        :type regions: list[oci.marketplace.models.Region]

        :param package_type:
            The value to assign to the package_type property of this Listing.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param default_package_version:
            The value to assign to the default_package_version property of this Listing.
        :type default_package_version: str

        :param links:
            The value to assign to the links property of this Listing.
        :type links: list[oci.marketplace.models.Link]

        :param is_featured:
            The value to assign to the is_featured property of this Listing.
        :type is_featured: bool

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'version': 'str',
            'tagline': 'str',
            'keywords': 'str',
            'short_description': 'str',
            'usage_information': 'str',
            'long_description': 'str',
            'license_model_description': 'str',
            'system_requirements': 'str',
            'time_released': 'datetime',
            'release_notes': 'str',
            'categories': 'list[str]',
            'publisher': 'Publisher',
            'languages': 'list[Item]',
            'screenshots': 'list[Screenshot]',
            'videos': 'list[NamedLink]',
            'support_contacts': 'list[SupportContact]',
            'support_links': 'list[NamedLink]',
            'documentation_links': 'list[DocumentationLink]',
            'icon': 'UploadData',
            'banner': 'UploadData',
            'regions': 'list[Region]',
            'package_type': 'str',
            'default_package_version': 'str',
            'links': 'list[Link]',
            'is_featured': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'version': 'version',
            'tagline': 'tagline',
            'keywords': 'keywords',
            'short_description': 'shortDescription',
            'usage_information': 'usageInformation',
            'long_description': 'longDescription',
            'license_model_description': 'licenseModelDescription',
            'system_requirements': 'systemRequirements',
            'time_released': 'timeReleased',
            'release_notes': 'releaseNotes',
            'categories': 'categories',
            'publisher': 'publisher',
            'languages': 'languages',
            'screenshots': 'screenshots',
            'videos': 'videos',
            'support_contacts': 'supportContacts',
            'support_links': 'supportLinks',
            'documentation_links': 'documentationLinks',
            'icon': 'icon',
            'banner': 'banner',
            'regions': 'regions',
            'package_type': 'packageType',
            'default_package_version': 'defaultPackageVersion',
            'links': 'links',
            'is_featured': 'isFeatured'
        }

        self._id = None
        self._name = None
        self._version = None
        self._tagline = None
        self._keywords = None
        self._short_description = None
        self._usage_information = None
        self._long_description = None
        self._license_model_description = None
        self._system_requirements = None
        self._time_released = None
        self._release_notes = None
        self._categories = None
        self._publisher = None
        self._languages = None
        self._screenshots = None
        self._videos = None
        self._support_contacts = None
        self._support_links = None
        self._documentation_links = None
        self._icon = None
        self._banner = None
        self._regions = None
        self._package_type = None
        self._default_package_version = None
        self._links = None
        self._is_featured = None

    @property
    def id(self):
        """
        Gets the id of this Listing.
        The unique identifier for the listing in Marketplace.


        :return: The id of this Listing.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Listing.
        The unique identifier for the listing in Marketplace.


        :param id: The id of this Listing.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Listing.
        The name of the listing.


        :return: The name of this Listing.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Listing.
        The name of the listing.


        :param name: The name of this Listing.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        Gets the version of this Listing.
        The version of the listing.


        :return: The version of this Listing.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Listing.
        The version of the listing.


        :param version: The version of this Listing.
        :type: str
        """
        self._version = version

    @property
    def tagline(self):
        """
        Gets the tagline of this Listing.
        The tagline of the listing.


        :return: The tagline of this Listing.
        :rtype: str
        """
        return self._tagline

    @tagline.setter
    def tagline(self, tagline):
        """
        Sets the tagline of this Listing.
        The tagline of the listing.


        :param tagline: The tagline of this Listing.
        :type: str
        """
        self._tagline = tagline

    @property
    def keywords(self):
        """
        Gets the keywords of this Listing.
        Keywords associated with the listing.


        :return: The keywords of this Listing.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this Listing.
        Keywords associated with the listing.


        :param keywords: The keywords of this Listing.
        :type: str
        """
        self._keywords = keywords

    @property
    def short_description(self):
        """
        Gets the short_description of this Listing.
        A short description of the listing.


        :return: The short_description of this Listing.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this Listing.
        A short description of the listing.


        :param short_description: The short_description of this Listing.
        :type: str
        """
        self._short_description = short_description

    @property
    def usage_information(self):
        """
        Gets the usage_information of this Listing.
        Usage information for the listing.


        :return: The usage_information of this Listing.
        :rtype: str
        """
        return self._usage_information

    @usage_information.setter
    def usage_information(self, usage_information):
        """
        Sets the usage_information of this Listing.
        Usage information for the listing.


        :param usage_information: The usage_information of this Listing.
        :type: str
        """
        self._usage_information = usage_information

    @property
    def long_description(self):
        """
        Gets the long_description of this Listing.
        A long description of the listing.


        :return: The long_description of this Listing.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this Listing.
        A long description of the listing.


        :param long_description: The long_description of this Listing.
        :type: str
        """
        self._long_description = long_description

    @property
    def license_model_description(self):
        """
        Gets the license_model_description of this Listing.
        A description of the publisher's licensing model for the listing.


        :return: The license_model_description of this Listing.
        :rtype: str
        """
        return self._license_model_description

    @license_model_description.setter
    def license_model_description(self, license_model_description):
        """
        Sets the license_model_description of this Listing.
        A description of the publisher's licensing model for the listing.


        :param license_model_description: The license_model_description of this Listing.
        :type: str
        """
        self._license_model_description = license_model_description

    @property
    def system_requirements(self):
        """
        Gets the system_requirements of this Listing.
        System requirements for the listing.


        :return: The system_requirements of this Listing.
        :rtype: str
        """
        return self._system_requirements

    @system_requirements.setter
    def system_requirements(self, system_requirements):
        """
        Sets the system_requirements of this Listing.
        System requirements for the listing.


        :param system_requirements: The system_requirements of this Listing.
        :type: str
        """
        self._system_requirements = system_requirements

    @property
    def time_released(self):
        """
        Gets the time_released of this Listing.
        The release date of the listing.


        :return: The time_released of this Listing.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this Listing.
        The release date of the listing.


        :param time_released: The time_released of this Listing.
        :type: datetime
        """
        self._time_released = time_released

    @property
    def release_notes(self):
        """
        Gets the release_notes of this Listing.
        Release notes for the listing.


        :return: The release_notes of this Listing.
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """
        Sets the release_notes of this Listing.
        Release notes for the listing.


        :param release_notes: The release_notes of this Listing.
        :type: str
        """
        self._release_notes = release_notes

    @property
    def categories(self):
        """
        Gets the categories of this Listing.
        Categories that the listing belongs to.


        :return: The categories of this Listing.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this Listing.
        Categories that the listing belongs to.


        :param categories: The categories of this Listing.
        :type: list[str]
        """
        self._categories = categories

    @property
    def publisher(self):
        """
        Gets the publisher of this Listing.

        :return: The publisher of this Listing.
        :rtype: oci.marketplace.models.Publisher
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this Listing.

        :param publisher: The publisher of this Listing.
        :type: oci.marketplace.models.Publisher
        """
        self._publisher = publisher

    @property
    def languages(self):
        """
        Gets the languages of this Listing.
        Languages supported by the listing.


        :return: The languages of this Listing.
        :rtype: list[oci.marketplace.models.Item]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this Listing.
        Languages supported by the listing.


        :param languages: The languages of this Listing.
        :type: list[oci.marketplace.models.Item]
        """
        self._languages = languages

    @property
    def screenshots(self):
        """
        Gets the screenshots of this Listing.
        Screenshots of the listing.


        :return: The screenshots of this Listing.
        :rtype: list[oci.marketplace.models.Screenshot]
        """
        return self._screenshots

    @screenshots.setter
    def screenshots(self, screenshots):
        """
        Sets the screenshots of this Listing.
        Screenshots of the listing.


        :param screenshots: The screenshots of this Listing.
        :type: list[oci.marketplace.models.Screenshot]
        """
        self._screenshots = screenshots

    @property
    def videos(self):
        """
        Gets the videos of this Listing.
        Videos of the listing.


        :return: The videos of this Listing.
        :rtype: list[oci.marketplace.models.NamedLink]
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        """
        Sets the videos of this Listing.
        Videos of the listing.


        :param videos: The videos of this Listing.
        :type: list[oci.marketplace.models.NamedLink]
        """
        self._videos = videos

    @property
    def support_contacts(self):
        """
        Gets the support_contacts of this Listing.
        Contact information to use to get support from the publisher for the listing.


        :return: The support_contacts of this Listing.
        :rtype: list[oci.marketplace.models.SupportContact]
        """
        return self._support_contacts

    @support_contacts.setter
    def support_contacts(self, support_contacts):
        """
        Sets the support_contacts of this Listing.
        Contact information to use to get support from the publisher for the listing.


        :param support_contacts: The support_contacts of this Listing.
        :type: list[oci.marketplace.models.SupportContact]
        """
        self._support_contacts = support_contacts

    @property
    def support_links(self):
        """
        Gets the support_links of this Listing.
        Links to support resources for the listing.


        :return: The support_links of this Listing.
        :rtype: list[oci.marketplace.models.NamedLink]
        """
        return self._support_links

    @support_links.setter
    def support_links(self, support_links):
        """
        Sets the support_links of this Listing.
        Links to support resources for the listing.


        :param support_links: The support_links of this Listing.
        :type: list[oci.marketplace.models.NamedLink]
        """
        self._support_links = support_links

    @property
    def documentation_links(self):
        """
        Gets the documentation_links of this Listing.
        Links to additional documentation provided by the publisher specifically for the listing.


        :return: The documentation_links of this Listing.
        :rtype: list[oci.marketplace.models.DocumentationLink]
        """
        return self._documentation_links

    @documentation_links.setter
    def documentation_links(self, documentation_links):
        """
        Sets the documentation_links of this Listing.
        Links to additional documentation provided by the publisher specifically for the listing.


        :param documentation_links: The documentation_links of this Listing.
        :type: list[oci.marketplace.models.DocumentationLink]
        """
        self._documentation_links = documentation_links

    @property
    def icon(self):
        """
        Gets the icon of this Listing.

        :return: The icon of this Listing.
        :rtype: oci.marketplace.models.UploadData
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this Listing.

        :param icon: The icon of this Listing.
        :type: oci.marketplace.models.UploadData
        """
        self._icon = icon

    @property
    def banner(self):
        """
        Gets the banner of this Listing.

        :return: The banner of this Listing.
        :rtype: oci.marketplace.models.UploadData
        """
        return self._banner

    @banner.setter
    def banner(self, banner):
        """
        Sets the banner of this Listing.

        :param banner: The banner of this Listing.
        :type: oci.marketplace.models.UploadData
        """
        self._banner = banner

    @property
    def regions(self):
        """
        Gets the regions of this Listing.
        The regions where you can deploy the listing. (Some listings have restrictions that limit their deployment to United States regions only.)


        :return: The regions of this Listing.
        :rtype: list[oci.marketplace.models.Region]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this Listing.
        The regions where you can deploy the listing. (Some listings have restrictions that limit their deployment to United States regions only.)


        :param regions: The regions of this Listing.
        :type: list[oci.marketplace.models.Region]
        """
        self._regions = regions

    @property
    def package_type(self):
        """
        Gets the package_type of this Listing.
        The listing's package type.

        Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this Listing.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this Listing.
        The listing's package type.


        :param package_type: The package_type of this Listing.
        :type: str
        """
        allowed_values = ["ORCHESTRATION", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def default_package_version(self):
        """
        Gets the default_package_version of this Listing.
        The default package version.


        :return: The default_package_version of this Listing.
        :rtype: str
        """
        return self._default_package_version

    @default_package_version.setter
    def default_package_version(self, default_package_version):
        """
        Sets the default_package_version of this Listing.
        The default package version.


        :param default_package_version: The default_package_version of this Listing.
        :type: str
        """
        self._default_package_version = default_package_version

    @property
    def links(self):
        """
        Gets the links of this Listing.
        Links to reference material.


        :return: The links of this Listing.
        :rtype: list[oci.marketplace.models.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Listing.
        Links to reference material.


        :param links: The links of this Listing.
        :type: list[oci.marketplace.models.Link]
        """
        self._links = links

    @property
    def is_featured(self):
        """
        Gets the is_featured of this Listing.
        Indicates whether the listing is included in Featured Listings.


        :return: The is_featured of this Listing.
        :rtype: bool
        """
        return self._is_featured

    @is_featured.setter
    def is_featured(self, is_featured):
        """
        Sets the is_featured of this Listing.
        Indicates whether the listing is included in Featured Listings.


        :param is_featured: The is_featured of this Listing.
        :type: bool
        """
        self._is_featured = is_featured

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
