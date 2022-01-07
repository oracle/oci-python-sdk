# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationSummary(object):
    """
    The model for summary of an application in service catalog.
    """

    #: A constant which can be used with the pricing_type property of a ApplicationSummary.
    #: This constant has a value of "FREE"
    PRICING_TYPE_FREE = "FREE"

    #: A constant which can be used with the pricing_type property of a ApplicationSummary.
    #: This constant has a value of "BYOL"
    PRICING_TYPE_BYOL = "BYOL"

    #: A constant which can be used with the pricing_type property of a ApplicationSummary.
    #: This constant has a value of "PAYGO"
    PRICING_TYPE_PAYGO = "PAYGO"

    #: A constant which can be used with the package_type property of a ApplicationSummary.
    #: This constant has a value of "STACK"
    PACKAGE_TYPE_STACK = "STACK"

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_id:
            The value to assign to the entity_id property of this ApplicationSummary.
        :type entity_id: str

        :param entity_type:
            The value to assign to the entity_type property of this ApplicationSummary.
        :type entity_type: str

        :param display_name:
            The value to assign to the display_name property of this ApplicationSummary.
        :type display_name: str

        :param is_featured:
            The value to assign to the is_featured property of this ApplicationSummary.
        :type is_featured: bool

        :param publisher:
            The value to assign to the publisher property of this ApplicationSummary.
        :type publisher: oci.service_catalog.models.PublisherSummary

        :param short_description:
            The value to assign to the short_description property of this ApplicationSummary.
        :type short_description: str

        :param logo:
            The value to assign to the logo property of this ApplicationSummary.
        :type logo: oci.service_catalog.models.UploadData

        :param pricing_type:
            The value to assign to the pricing_type property of this ApplicationSummary.
            Allowed values for this property are: "FREE", "BYOL", "PAYGO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pricing_type: str

        :param package_type:
            The value to assign to the package_type property of this ApplicationSummary.
            Allowed values for this property are: "STACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        """
        self.swagger_types = {
            'entity_id': 'str',
            'entity_type': 'str',
            'display_name': 'str',
            'is_featured': 'bool',
            'publisher': 'PublisherSummary',
            'short_description': 'str',
            'logo': 'UploadData',
            'pricing_type': 'str',
            'package_type': 'str'
        }

        self.attribute_map = {
            'entity_id': 'entityId',
            'entity_type': 'entityType',
            'display_name': 'displayName',
            'is_featured': 'isFeatured',
            'publisher': 'publisher',
            'short_description': 'shortDescription',
            'logo': 'logo',
            'pricing_type': 'pricingType',
            'package_type': 'packageType'
        }

        self._entity_id = None
        self._entity_type = None
        self._display_name = None
        self._is_featured = None
        self._publisher = None
        self._short_description = None
        self._logo = None
        self._pricing_type = None
        self._package_type = None

    @property
    def entity_id(self):
        """
        **[Required]** Gets the entity_id of this ApplicationSummary.
        Identifier of the application from a service catalog.


        :return: The entity_id of this ApplicationSummary.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ApplicationSummary.
        Identifier of the application from a service catalog.


        :param entity_id: The entity_id of this ApplicationSummary.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this ApplicationSummary.
        The type of an application in the service catalog.


        :return: The entity_type of this ApplicationSummary.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this ApplicationSummary.
        The type of an application in the service catalog.


        :param entity_type: The entity_type of this ApplicationSummary.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ApplicationSummary.
        The name that service catalog should use to display this application.


        :return: The display_name of this ApplicationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApplicationSummary.
        The name that service catalog should use to display this application.


        :param display_name: The display_name of this ApplicationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_featured(self):
        """
        Gets the is_featured of this ApplicationSummary.
        Indicates whether the application is featured.


        :return: The is_featured of this ApplicationSummary.
        :rtype: bool
        """
        return self._is_featured

    @is_featured.setter
    def is_featured(self, is_featured):
        """
        Sets the is_featured of this ApplicationSummary.
        Indicates whether the application is featured.


        :param is_featured: The is_featured of this ApplicationSummary.
        :type: bool
        """
        self._is_featured = is_featured

    @property
    def publisher(self):
        """
        Gets the publisher of this ApplicationSummary.

        :return: The publisher of this ApplicationSummary.
        :rtype: oci.service_catalog.models.PublisherSummary
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this ApplicationSummary.

        :param publisher: The publisher of this ApplicationSummary.
        :type: oci.service_catalog.models.PublisherSummary
        """
        self._publisher = publisher

    @property
    def short_description(self):
        """
        Gets the short_description of this ApplicationSummary.
        A short description of the application.


        :return: The short_description of this ApplicationSummary.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this ApplicationSummary.
        A short description of the application.


        :param short_description: The short_description of this ApplicationSummary.
        :type: str
        """
        self._short_description = short_description

    @property
    def logo(self):
        """
        Gets the logo of this ApplicationSummary.

        :return: The logo of this ApplicationSummary.
        :rtype: oci.service_catalog.models.UploadData
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this ApplicationSummary.

        :param logo: The logo of this ApplicationSummary.
        :type: oci.service_catalog.models.UploadData
        """
        self._logo = logo

    @property
    def pricing_type(self):
        """
        Gets the pricing_type of this ApplicationSummary.
        Summary of the pricing types available across all packages in the application.

        Allowed values for this property are: "FREE", "BYOL", "PAYGO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pricing_type of this ApplicationSummary.
        :rtype: str
        """
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, pricing_type):
        """
        Sets the pricing_type of this ApplicationSummary.
        Summary of the pricing types available across all packages in the application.


        :param pricing_type: The pricing_type of this ApplicationSummary.
        :type: str
        """
        allowed_values = ["FREE", "BYOL", "PAYGO"]
        if not value_allowed_none_or_none_sentinel(pricing_type, allowed_values):
            pricing_type = 'UNKNOWN_ENUM_VALUE'
        self._pricing_type = pricing_type

    @property
    def package_type(self):
        """
        Gets the package_type of this ApplicationSummary.
        The type of the packages withing the application.

        Allowed values for this property are: "STACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this ApplicationSummary.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this ApplicationSummary.
        The type of the packages withing the application.


        :param package_type: The package_type of this ApplicationSummary.
        :type: str
        """
        allowed_values = ["STACK"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
