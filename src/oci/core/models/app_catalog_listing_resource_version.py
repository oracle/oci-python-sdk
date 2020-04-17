# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppCatalogListingResourceVersion(object):
    """
    Listing Resource Version
    """

    #: A constant which can be used with the allowed_actions property of a AppCatalogListingResourceVersion.
    #: This constant has a value of "SNAPSHOT"
    ALLOWED_ACTIONS_SNAPSHOT = "SNAPSHOT"

    #: A constant which can be used with the allowed_actions property of a AppCatalogListingResourceVersion.
    #: This constant has a value of "BOOT_VOLUME_DETACH"
    ALLOWED_ACTIONS_BOOT_VOLUME_DETACH = "BOOT_VOLUME_DETACH"

    #: A constant which can be used with the allowed_actions property of a AppCatalogListingResourceVersion.
    #: This constant has a value of "PRESERVE_BOOT_VOLUME"
    ALLOWED_ACTIONS_PRESERVE_BOOT_VOLUME = "PRESERVE_BOOT_VOLUME"

    #: A constant which can be used with the allowed_actions property of a AppCatalogListingResourceVersion.
    #: This constant has a value of "SERIAL_CONSOLE_ACCESS"
    ALLOWED_ACTIONS_SERIAL_CONSOLE_ACCESS = "SERIAL_CONSOLE_ACCESS"

    #: A constant which can be used with the allowed_actions property of a AppCatalogListingResourceVersion.
    #: This constant has a value of "BOOT_RECOVERY"
    ALLOWED_ACTIONS_BOOT_RECOVERY = "BOOT_RECOVERY"

    #: A constant which can be used with the allowed_actions property of a AppCatalogListingResourceVersion.
    #: This constant has a value of "BACKUP_BOOT_VOLUME"
    ALLOWED_ACTIONS_BACKUP_BOOT_VOLUME = "BACKUP_BOOT_VOLUME"

    #: A constant which can be used with the allowed_actions property of a AppCatalogListingResourceVersion.
    #: This constant has a value of "CAPTURE_CONSOLE_HISTORY"
    ALLOWED_ACTIONS_CAPTURE_CONSOLE_HISTORY = "CAPTURE_CONSOLE_HISTORY"

    def __init__(self, **kwargs):
        """
        Initializes a new AppCatalogListingResourceVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_id:
            The value to assign to the listing_id property of this AppCatalogListingResourceVersion.
        :type listing_id: str

        :param time_published:
            The value to assign to the time_published property of this AppCatalogListingResourceVersion.
        :type time_published: datetime

        :param listing_resource_id:
            The value to assign to the listing_resource_id property of this AppCatalogListingResourceVersion.
        :type listing_resource_id: str

        :param listing_resource_version:
            The value to assign to the listing_resource_version property of this AppCatalogListingResourceVersion.
        :type listing_resource_version: str

        :param available_regions:
            The value to assign to the available_regions property of this AppCatalogListingResourceVersion.
        :type available_regions: list[str]

        :param compatible_shapes:
            The value to assign to the compatible_shapes property of this AppCatalogListingResourceVersion.
        :type compatible_shapes: list[str]

        :param accessible_ports:
            The value to assign to the accessible_ports property of this AppCatalogListingResourceVersion.
        :type accessible_ports: list[int]

        :param allowed_actions:
            The value to assign to the allowed_actions property of this AppCatalogListingResourceVersion.
            Allowed values for items in this list are: "SNAPSHOT", "BOOT_VOLUME_DETACH", "PRESERVE_BOOT_VOLUME", "SERIAL_CONSOLE_ACCESS", "BOOT_RECOVERY", "BACKUP_BOOT_VOLUME", "CAPTURE_CONSOLE_HISTORY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type allowed_actions: list[str]

        """
        self.swagger_types = {
            'listing_id': 'str',
            'time_published': 'datetime',
            'listing_resource_id': 'str',
            'listing_resource_version': 'str',
            'available_regions': 'list[str]',
            'compatible_shapes': 'list[str]',
            'accessible_ports': 'list[int]',
            'allowed_actions': 'list[str]'
        }

        self.attribute_map = {
            'listing_id': 'listingId',
            'time_published': 'timePublished',
            'listing_resource_id': 'listingResourceId',
            'listing_resource_version': 'listingResourceVersion',
            'available_regions': 'availableRegions',
            'compatible_shapes': 'compatibleShapes',
            'accessible_ports': 'accessiblePorts',
            'allowed_actions': 'allowedActions'
        }

        self._listing_id = None
        self._time_published = None
        self._listing_resource_id = None
        self._listing_resource_version = None
        self._available_regions = None
        self._compatible_shapes = None
        self._accessible_ports = None
        self._allowed_actions = None

    @property
    def listing_id(self):
        """
        Gets the listing_id of this AppCatalogListingResourceVersion.
        The OCID of the listing this resource version belongs to.


        :return: The listing_id of this AppCatalogListingResourceVersion.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this AppCatalogListingResourceVersion.
        The OCID of the listing this resource version belongs to.


        :param listing_id: The listing_id of this AppCatalogListingResourceVersion.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def time_published(self):
        """
        Gets the time_published of this AppCatalogListingResourceVersion.
        Date and time the listing resource version was published, in RFC3339 format.
        Example: `2018-03-20T12:32:53.532Z`


        :return: The time_published of this AppCatalogListingResourceVersion.
        :rtype: datetime
        """
        return self._time_published

    @time_published.setter
    def time_published(self, time_published):
        """
        Sets the time_published of this AppCatalogListingResourceVersion.
        Date and time the listing resource version was published, in RFC3339 format.
        Example: `2018-03-20T12:32:53.532Z`


        :param time_published: The time_published of this AppCatalogListingResourceVersion.
        :type: datetime
        """
        self._time_published = time_published

    @property
    def listing_resource_id(self):
        """
        Gets the listing_resource_id of this AppCatalogListingResourceVersion.
        OCID of the listing resource.


        :return: The listing_resource_id of this AppCatalogListingResourceVersion.
        :rtype: str
        """
        return self._listing_resource_id

    @listing_resource_id.setter
    def listing_resource_id(self, listing_resource_id):
        """
        Sets the listing_resource_id of this AppCatalogListingResourceVersion.
        OCID of the listing resource.


        :param listing_resource_id: The listing_resource_id of this AppCatalogListingResourceVersion.
        :type: str
        """
        self._listing_resource_id = listing_resource_id

    @property
    def listing_resource_version(self):
        """
        Gets the listing_resource_version of this AppCatalogListingResourceVersion.
        Resource Version.


        :return: The listing_resource_version of this AppCatalogListingResourceVersion.
        :rtype: str
        """
        return self._listing_resource_version

    @listing_resource_version.setter
    def listing_resource_version(self, listing_resource_version):
        """
        Sets the listing_resource_version of this AppCatalogListingResourceVersion.
        Resource Version.


        :param listing_resource_version: The listing_resource_version of this AppCatalogListingResourceVersion.
        :type: str
        """
        self._listing_resource_version = listing_resource_version

    @property
    def available_regions(self):
        """
        Gets the available_regions of this AppCatalogListingResourceVersion.
        List of regions that this listing resource version is available.

        For information about Regions, see
        `Regions`__.

        Example: `[\"us-ashburn-1\", \"us-phoenix-1\"]`

        __ https://docs.cloud.oracle.com/#General/Concepts/regions.htm


        :return: The available_regions of this AppCatalogListingResourceVersion.
        :rtype: list[str]
        """
        return self._available_regions

    @available_regions.setter
    def available_regions(self, available_regions):
        """
        Sets the available_regions of this AppCatalogListingResourceVersion.
        List of regions that this listing resource version is available.

        For information about Regions, see
        `Regions`__.

        Example: `[\"us-ashburn-1\", \"us-phoenix-1\"]`

        __ https://docs.cloud.oracle.com/#General/Concepts/regions.htm


        :param available_regions: The available_regions of this AppCatalogListingResourceVersion.
        :type: list[str]
        """
        self._available_regions = available_regions

    @property
    def compatible_shapes(self):
        """
        Gets the compatible_shapes of this AppCatalogListingResourceVersion.
        Array of shapes compatible with this resource.

        You may enumerate all available shapes by calling :func:`list_shapes`.

        Example: `[\"VM.Standard1.1\", \"VM.Standard1.2\"]`


        :return: The compatible_shapes of this AppCatalogListingResourceVersion.
        :rtype: list[str]
        """
        return self._compatible_shapes

    @compatible_shapes.setter
    def compatible_shapes(self, compatible_shapes):
        """
        Sets the compatible_shapes of this AppCatalogListingResourceVersion.
        Array of shapes compatible with this resource.

        You may enumerate all available shapes by calling :func:`list_shapes`.

        Example: `[\"VM.Standard1.1\", \"VM.Standard1.2\"]`


        :param compatible_shapes: The compatible_shapes of this AppCatalogListingResourceVersion.
        :type: list[str]
        """
        self._compatible_shapes = compatible_shapes

    @property
    def accessible_ports(self):
        """
        Gets the accessible_ports of this AppCatalogListingResourceVersion.
        List of accessible ports for instances launched with this listing resource version.


        :return: The accessible_ports of this AppCatalogListingResourceVersion.
        :rtype: list[int]
        """
        return self._accessible_ports

    @accessible_ports.setter
    def accessible_ports(self, accessible_ports):
        """
        Sets the accessible_ports of this AppCatalogListingResourceVersion.
        List of accessible ports for instances launched with this listing resource version.


        :param accessible_ports: The accessible_ports of this AppCatalogListingResourceVersion.
        :type: list[int]
        """
        self._accessible_ports = accessible_ports

    @property
    def allowed_actions(self):
        """
        Gets the allowed_actions of this AppCatalogListingResourceVersion.
        Allowed actions for the listing resource.

        Allowed values for items in this list are: "SNAPSHOT", "BOOT_VOLUME_DETACH", "PRESERVE_BOOT_VOLUME", "SERIAL_CONSOLE_ACCESS", "BOOT_RECOVERY", "BACKUP_BOOT_VOLUME", "CAPTURE_CONSOLE_HISTORY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The allowed_actions of this AppCatalogListingResourceVersion.
        :rtype: list[str]
        """
        return self._allowed_actions

    @allowed_actions.setter
    def allowed_actions(self, allowed_actions):
        """
        Sets the allowed_actions of this AppCatalogListingResourceVersion.
        Allowed actions for the listing resource.


        :param allowed_actions: The allowed_actions of this AppCatalogListingResourceVersion.
        :type: list[str]
        """
        allowed_values = ["SNAPSHOT", "BOOT_VOLUME_DETACH", "PRESERVE_BOOT_VOLUME", "SERIAL_CONSOLE_ACCESS", "BOOT_RECOVERY", "BACKUP_BOOT_VOLUME", "CAPTURE_CONSOLE_HISTORY"]
        if allowed_actions:
            allowed_actions[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in allowed_actions]
        self._allowed_actions = allowed_actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
