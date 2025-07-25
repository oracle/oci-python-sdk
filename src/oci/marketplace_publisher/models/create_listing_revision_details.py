# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateListingRevisionDetails(object):
    """
    The model for an Oracle Cloud Infrastructure Marketplace Publisher listing revision.
    """

    #: A constant which can be used with the listing_type property of a CreateListingRevisionDetails.
    #: This constant has a value of "OCI_APPLICATION"
    LISTING_TYPE_OCI_APPLICATION = "OCI_APPLICATION"

    #: A constant which can be used with the listing_type property of a CreateListingRevisionDetails.
    #: This constant has a value of "LEAD_GENERATION"
    LISTING_TYPE_LEAD_GENERATION = "LEAD_GENERATION"

    #: A constant which can be used with the listing_type property of a CreateListingRevisionDetails.
    #: This constant has a value of "SERVICE"
    LISTING_TYPE_SERVICE = "SERVICE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateListingRevisionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace_publisher.models.CreateOciListingRevisionDetails`
        * :class:`~oci.marketplace_publisher.models.CreateServiceListingRevisionDetails`
        * :class:`~oci.marketplace_publisher.models.CreateLeadGenListingRevisionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateListingRevisionDetails.
        :type display_name: str

        :param listing_id:
            The value to assign to the listing_id property of this CreateListingRevisionDetails.
        :type listing_id: str

        :param listing_type:
            The value to assign to the listing_type property of this CreateListingRevisionDetails.
            Allowed values for this property are: "OCI_APPLICATION", "LEAD_GENERATION", "SERVICE"
        :type listing_type: str

        :param headline:
            The value to assign to the headline property of this CreateListingRevisionDetails.
        :type headline: str

        :param tagline:
            The value to assign to the tagline property of this CreateListingRevisionDetails.
        :type tagline: str

        :param keywords:
            The value to assign to the keywords property of this CreateListingRevisionDetails.
        :type keywords: str

        :param short_description:
            The value to assign to the short_description property of this CreateListingRevisionDetails.
        :type short_description: str

        :param usage_information:
            The value to assign to the usage_information property of this CreateListingRevisionDetails.
        :type usage_information: str

        :param long_description:
            The value to assign to the long_description property of this CreateListingRevisionDetails.
        :type long_description: str

        :param content_language:
            The value to assign to the content_language property of this CreateListingRevisionDetails.
        :type content_language: oci.marketplace_publisher.models.LanguageItem

        :param supportedlanguages:
            The value to assign to the supportedlanguages property of this CreateListingRevisionDetails.
        :type supportedlanguages: list[oci.marketplace_publisher.models.LanguageItem]

        :param support_contacts:
            The value to assign to the support_contacts property of this CreateListingRevisionDetails.
        :type support_contacts: list[oci.marketplace_publisher.models.SupportContact]

        :param support_links:
            The value to assign to the support_links property of this CreateListingRevisionDetails.
        :type support_links: list[oci.marketplace_publisher.models.NamedLink]

        :param status:
            The value to assign to the status property of this CreateListingRevisionDetails.
        :type status: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateListingRevisionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateListingRevisionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'listing_id': 'str',
            'listing_type': 'str',
            'headline': 'str',
            'tagline': 'str',
            'keywords': 'str',
            'short_description': 'str',
            'usage_information': 'str',
            'long_description': 'str',
            'content_language': 'LanguageItem',
            'supportedlanguages': 'list[LanguageItem]',
            'support_contacts': 'list[SupportContact]',
            'support_links': 'list[NamedLink]',
            'status': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'listing_id': 'listingId',
            'listing_type': 'listingType',
            'headline': 'headline',
            'tagline': 'tagline',
            'keywords': 'keywords',
            'short_description': 'shortDescription',
            'usage_information': 'usageInformation',
            'long_description': 'longDescription',
            'content_language': 'contentLanguage',
            'supportedlanguages': 'supportedlanguages',
            'support_contacts': 'supportContacts',
            'support_links': 'supportLinks',
            'status': 'status',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._listing_id = None
        self._listing_type = None
        self._headline = None
        self._tagline = None
        self._keywords = None
        self._short_description = None
        self._usage_information = None
        self._long_description = None
        self._content_language = None
        self._supportedlanguages = None
        self._support_contacts = None
        self._support_links = None
        self._status = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['listingType']

        if type == 'OCI_APPLICATION':
            return 'CreateOciListingRevisionDetails'

        if type == 'SERVICE':
            return 'CreateServiceListingRevisionDetails'

        if type == 'LEAD_GENERATION':
            return 'CreateLeadGenListingRevisionDetails'
        else:
            return 'CreateListingRevisionDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateListingRevisionDetails.
        The name for the listing revision.


        :return: The display_name of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateListingRevisionDetails.
        The name for the listing revision.


        :param display_name: The display_name of this CreateListingRevisionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def listing_id(self):
        """
        **[Required]** Gets the listing_id of this CreateListingRevisionDetails.
        The unique identifier for the listing this revision belongs to.


        :return: The listing_id of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this CreateListingRevisionDetails.
        The unique identifier for the listing this revision belongs to.


        :param listing_id: The listing_id of this CreateListingRevisionDetails.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def listing_type(self):
        """
        **[Required]** Gets the listing_type of this CreateListingRevisionDetails.
        The listing's type. Populated from the listing.

        Allowed values for this property are: "OCI_APPLICATION", "LEAD_GENERATION", "SERVICE"


        :return: The listing_type of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._listing_type

    @listing_type.setter
    def listing_type(self, listing_type):
        """
        Sets the listing_type of this CreateListingRevisionDetails.
        The listing's type. Populated from the listing.


        :param listing_type: The listing_type of this CreateListingRevisionDetails.
        :type: str
        """
        allowed_values = ["OCI_APPLICATION", "LEAD_GENERATION", "SERVICE"]
        if not value_allowed_none_or_none_sentinel(listing_type, allowed_values):
            raise ValueError(
                f"Invalid value for `listing_type`, must be None or one of {allowed_values}"
            )
        self._listing_type = listing_type

    @property
    def headline(self):
        """
        **[Required]** Gets the headline of this CreateListingRevisionDetails.
        Single line introduction for the listing revision.


        :return: The headline of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this CreateListingRevisionDetails.
        Single line introduction for the listing revision.


        :param headline: The headline of this CreateListingRevisionDetails.
        :type: str
        """
        self._headline = headline

    @property
    def tagline(self):
        """
        Gets the tagline of this CreateListingRevisionDetails.
        The tagline for the listing revision.


        :return: The tagline of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._tagline

    @tagline.setter
    def tagline(self, tagline):
        """
        Sets the tagline of this CreateListingRevisionDetails.
        The tagline for the listing revision.


        :param tagline: The tagline of this CreateListingRevisionDetails.
        :type: str
        """
        self._tagline = tagline

    @property
    def keywords(self):
        """
        Gets the keywords of this CreateListingRevisionDetails.
        Keywords associated with the listing revision.


        :return: The keywords of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this CreateListingRevisionDetails.
        Keywords associated with the listing revision.


        :param keywords: The keywords of this CreateListingRevisionDetails.
        :type: str
        """
        self._keywords = keywords

    @property
    def short_description(self):
        """
        Gets the short_description of this CreateListingRevisionDetails.
        A short description for the listing revision.


        :return: The short_description of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this CreateListingRevisionDetails.
        A short description for the listing revision.


        :param short_description: The short_description of this CreateListingRevisionDetails.
        :type: str
        """
        self._short_description = short_description

    @property
    def usage_information(self):
        """
        Gets the usage_information of this CreateListingRevisionDetails.
        Usage information for the listing revision.


        :return: The usage_information of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._usage_information

    @usage_information.setter
    def usage_information(self, usage_information):
        """
        Sets the usage_information of this CreateListingRevisionDetails.
        Usage information for the listing revision.


        :param usage_information: The usage_information of this CreateListingRevisionDetails.
        :type: str
        """
        self._usage_information = usage_information

    @property
    def long_description(self):
        """
        Gets the long_description of this CreateListingRevisionDetails.
        A long description for the listing revision.


        :return: The long_description of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this CreateListingRevisionDetails.
        A long description for the listing revision.


        :param long_description: The long_description of this CreateListingRevisionDetails.
        :type: str
        """
        self._long_description = long_description

    @property
    def content_language(self):
        """
        Gets the content_language of this CreateListingRevisionDetails.

        :return: The content_language of this CreateListingRevisionDetails.
        :rtype: oci.marketplace_publisher.models.LanguageItem
        """
        return self._content_language

    @content_language.setter
    def content_language(self, content_language):
        """
        Sets the content_language of this CreateListingRevisionDetails.

        :param content_language: The content_language of this CreateListingRevisionDetails.
        :type: oci.marketplace_publisher.models.LanguageItem
        """
        self._content_language = content_language

    @property
    def supportedlanguages(self):
        """
        Gets the supportedlanguages of this CreateListingRevisionDetails.
        Languages supported by the publisher for the listing revision.


        :return: The supportedlanguages of this CreateListingRevisionDetails.
        :rtype: list[oci.marketplace_publisher.models.LanguageItem]
        """
        return self._supportedlanguages

    @supportedlanguages.setter
    def supportedlanguages(self, supportedlanguages):
        """
        Sets the supportedlanguages of this CreateListingRevisionDetails.
        Languages supported by the publisher for the listing revision.


        :param supportedlanguages: The supportedlanguages of this CreateListingRevisionDetails.
        :type: list[oci.marketplace_publisher.models.LanguageItem]
        """
        self._supportedlanguages = supportedlanguages

    @property
    def support_contacts(self):
        """
        Gets the support_contacts of this CreateListingRevisionDetails.
        Contact information to use to get support from the publisher for the listing revision.


        :return: The support_contacts of this CreateListingRevisionDetails.
        :rtype: list[oci.marketplace_publisher.models.SupportContact]
        """
        return self._support_contacts

    @support_contacts.setter
    def support_contacts(self, support_contacts):
        """
        Sets the support_contacts of this CreateListingRevisionDetails.
        Contact information to use to get support from the publisher for the listing revision.


        :param support_contacts: The support_contacts of this CreateListingRevisionDetails.
        :type: list[oci.marketplace_publisher.models.SupportContact]
        """
        self._support_contacts = support_contacts

    @property
    def support_links(self):
        """
        Gets the support_links of this CreateListingRevisionDetails.
        Links to support resources for the listing revision.


        :return: The support_links of this CreateListingRevisionDetails.
        :rtype: list[oci.marketplace_publisher.models.NamedLink]
        """
        return self._support_links

    @support_links.setter
    def support_links(self, support_links):
        """
        Sets the support_links of this CreateListingRevisionDetails.
        Links to support resources for the listing revision.


        :param support_links: The support_links of this CreateListingRevisionDetails.
        :type: list[oci.marketplace_publisher.models.NamedLink]
        """
        self._support_links = support_links

    @property
    def status(self):
        """
        Gets the status of this CreateListingRevisionDetails.
        The current status of the Listing revision.


        :return: The status of this CreateListingRevisionDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CreateListingRevisionDetails.
        The current status of the Listing revision.


        :param status: The status of this CreateListingRevisionDetails.
        :type: str
        """
        self._status = status

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateListingRevisionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateListingRevisionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateListingRevisionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateListingRevisionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateListingRevisionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateListingRevisionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateListingRevisionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateListingRevisionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
