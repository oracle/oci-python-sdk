# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicationSummary(object):
    """
    The model for a summary of an Oracle Cloud Infrastructure publication.
    """

    #: A constant which can be used with the package_type property of a PublicationSummary.
    #: This constant has a value of "ORCHESTRATION"
    PACKAGE_TYPE_ORCHESTRATION = "ORCHESTRATION"

    #: A constant which can be used with the package_type property of a PublicationSummary.
    #: This constant has a value of "IMAGE"
    PACKAGE_TYPE_IMAGE = "IMAGE"

    #: A constant which can be used with the listing_type property of a PublicationSummary.
    #: This constant has a value of "COMMUNITY"
    LISTING_TYPE_COMMUNITY = "COMMUNITY"

    #: A constant which can be used with the listing_type property of a PublicationSummary.
    #: This constant has a value of "PARTNER"
    LISTING_TYPE_PARTNER = "PARTNER"

    #: A constant which can be used with the listing_type property of a PublicationSummary.
    #: This constant has a value of "PRIVATE"
    LISTING_TYPE_PRIVATE = "PRIVATE"

    def __init__(self, **kwargs):
        """
        Initializes a new PublicationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PublicationSummary.
        :type lifecycle_state: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PublicationSummary.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this PublicationSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this PublicationSummary.
        :type name: str

        :param short_description:
            The value to assign to the short_description property of this PublicationSummary.
        :type short_description: str

        :param icon:
            The value to assign to the icon property of this PublicationSummary.
        :type icon: oci.marketplace.models.UploadData

        :param package_type:
            The value to assign to the package_type property of this PublicationSummary.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param supported_operating_systems:
            The value to assign to the supported_operating_systems property of this PublicationSummary.
        :type supported_operating_systems: list[oci.marketplace.models.OperatingSystem]

        :param listing_type:
            The value to assign to the listing_type property of this PublicationSummary.
            Allowed values for this property are: "COMMUNITY", "PARTNER", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type listing_type: str

        :param time_created:
            The value to assign to the time_created property of this PublicationSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'name': 'str',
            'short_description': 'str',
            'icon': 'UploadData',
            'package_type': 'str',
            'supported_operating_systems': 'list[OperatingSystem]',
            'listing_type': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'name': 'name',
            'short_description': 'shortDescription',
            'icon': 'icon',
            'package_type': 'packageType',
            'supported_operating_systems': 'supportedOperatingSystems',
            'listing_type': 'listingType',
            'time_created': 'timeCreated'
        }

        self._lifecycle_state = None
        self._compartment_id = None
        self._id = None
        self._name = None
        self._short_description = None
        self._icon = None
        self._package_type = None
        self._supported_operating_systems = None
        self._listing_type = None
        self._time_created = None

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PublicationSummary.
        The lifecycle state of the publication.


        :return: The lifecycle_state of this PublicationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PublicationSummary.
        The lifecycle state of the publication.


        :param lifecycle_state: The lifecycle_state of this PublicationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PublicationSummary.
        The `OCID`__ of the compartment where the publication exists.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PublicationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PublicationSummary.
        The `OCID`__ of the compartment where the publication exists.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PublicationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PublicationSummary.
        The unique identifier for the publication in Marketplace.


        :return: The id of this PublicationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PublicationSummary.
        The unique identifier for the publication in Marketplace.


        :param id: The id of this PublicationSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PublicationSummary.
        The name of the publication, which is also used in the listing.


        :return: The name of this PublicationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PublicationSummary.
        The name of the publication, which is also used in the listing.


        :param name: The name of this PublicationSummary.
        :type: str
        """
        self._name = name

    @property
    def short_description(self):
        """
        Gets the short_description of this PublicationSummary.
        A short description of the publication to use in the listing.


        :return: The short_description of this PublicationSummary.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this PublicationSummary.
        A short description of the publication to use in the listing.


        :param short_description: The short_description of this PublicationSummary.
        :type: str
        """
        self._short_description = short_description

    @property
    def icon(self):
        """
        Gets the icon of this PublicationSummary.

        :return: The icon of this PublicationSummary.
        :rtype: oci.marketplace.models.UploadData
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this PublicationSummary.

        :param icon: The icon of this PublicationSummary.
        :type: oci.marketplace.models.UploadData
        """
        self._icon = icon

    @property
    def package_type(self):
        """
        Gets the package_type of this PublicationSummary.
        The listing's package type.

        Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this PublicationSummary.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this PublicationSummary.
        The listing's package type.


        :param package_type: The package_type of this PublicationSummary.
        :type: str
        """
        allowed_values = ["ORCHESTRATION", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def supported_operating_systems(self):
        """
        Gets the supported_operating_systems of this PublicationSummary.
        The list of operating systems supported by the listing.


        :return: The supported_operating_systems of this PublicationSummary.
        :rtype: list[oci.marketplace.models.OperatingSystem]
        """
        return self._supported_operating_systems

    @supported_operating_systems.setter
    def supported_operating_systems(self, supported_operating_systems):
        """
        Sets the supported_operating_systems of this PublicationSummary.
        The list of operating systems supported by the listing.


        :param supported_operating_systems: The supported_operating_systems of this PublicationSummary.
        :type: list[oci.marketplace.models.OperatingSystem]
        """
        self._supported_operating_systems = supported_operating_systems

    @property
    def listing_type(self):
        """
        **[Required]** Gets the listing_type of this PublicationSummary.
        The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.

        Allowed values for this property are: "COMMUNITY", "PARTNER", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The listing_type of this PublicationSummary.
        :rtype: str
        """
        return self._listing_type

    @listing_type.setter
    def listing_type(self, listing_type):
        """
        Sets the listing_type of this PublicationSummary.
        The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.


        :param listing_type: The listing_type of this PublicationSummary.
        :type: str
        """
        allowed_values = ["COMMUNITY", "PARTNER", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(listing_type, allowed_values):
            listing_type = 'UNKNOWN_ENUM_VALUE'
        self._listing_type = listing_type

    @property
    def time_created(self):
        """
        Gets the time_created of this PublicationSummary.
        The date and time the publication was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PublicationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PublicationSummary.
        The date and time the publication was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PublicationSummary.
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
