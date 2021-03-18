# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicationPackage(object):
    """
    A base object for all types of publication packages.
    """

    #: A constant which can be used with the package_type property of a PublicationPackage.
    #: This constant has a value of "ORCHESTRATION"
    PACKAGE_TYPE_ORCHESTRATION = "ORCHESTRATION"

    #: A constant which can be used with the package_type property of a PublicationPackage.
    #: This constant has a value of "IMAGE"
    PACKAGE_TYPE_IMAGE = "IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new PublicationPackage object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace.models.OrchestrationPublicationPackage`
        * :class:`~oci.marketplace.models.ImagePublicationPackage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this PublicationPackage.
        :type description: str

        :param listing_id:
            The value to assign to the listing_id property of this PublicationPackage.
        :type listing_id: str

        :param version:
            The value to assign to the version property of this PublicationPackage.
        :type version: str

        :param package_type:
            The value to assign to the package_type property of this PublicationPackage.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param resource_id:
            The value to assign to the resource_id property of this PublicationPackage.
        :type resource_id: str

        :param time_created:
            The value to assign to the time_created property of this PublicationPackage.
        :type time_created: datetime

        :param operating_system:
            The value to assign to the operating_system property of this PublicationPackage.
        :type operating_system: oci.marketplace.models.OperatingSystem

        """
        self.swagger_types = {
            'description': 'str',
            'listing_id': 'str',
            'version': 'str',
            'package_type': 'str',
            'resource_id': 'str',
            'time_created': 'datetime',
            'operating_system': 'OperatingSystem'
        }

        self.attribute_map = {
            'description': 'description',
            'listing_id': 'listingId',
            'version': 'version',
            'package_type': 'packageType',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated',
            'operating_system': 'operatingSystem'
        }

        self._description = None
        self._listing_id = None
        self._version = None
        self._package_type = None
        self._resource_id = None
        self._time_created = None
        self._operating_system = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['packageType']

        if type == 'ORCHESTRATION':
            return 'OrchestrationPublicationPackage'

        if type == 'IMAGE':
            return 'ImagePublicationPackage'
        else:
            return 'PublicationPackage'

    @property
    def description(self):
        """
        Gets the description of this PublicationPackage.
        Description of this package.


        :return: The description of this PublicationPackage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PublicationPackage.
        Description of this package.


        :param description: The description of this PublicationPackage.
        :type: str
        """
        self._description = description

    @property
    def listing_id(self):
        """
        **[Required]** Gets the listing_id of this PublicationPackage.
        The ID of the listing this package belongs to.


        :return: The listing_id of this PublicationPackage.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this PublicationPackage.
        The ID of the listing this package belongs to.


        :param listing_id: The listing_id of this PublicationPackage.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def version(self):
        """
        **[Required]** Gets the version of this PublicationPackage.
        The package version.


        :return: The version of this PublicationPackage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PublicationPackage.
        The package version.


        :param version: The version of this PublicationPackage.
        :type: str
        """
        self._version = version

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this PublicationPackage.
        The specified package's type.

        Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this PublicationPackage.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this PublicationPackage.
        The specified package's type.


        :param package_type: The package_type of this PublicationPackage.
        :type: str
        """
        allowed_values = ["ORCHESTRATION", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def resource_id(self):
        """
        Gets the resource_id of this PublicationPackage.
        The unique identifier for the package resource.


        :return: The resource_id of this PublicationPackage.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this PublicationPackage.
        The unique identifier for the package resource.


        :param resource_id: The resource_id of this PublicationPackage.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def time_created(self):
        """
        Gets the time_created of this PublicationPackage.
        The date and time this listing package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PublicationPackage.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PublicationPackage.
        The date and time this listing package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PublicationPackage.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def operating_system(self):
        """
        Gets the operating_system of this PublicationPackage.

        :return: The operating_system of this PublicationPackage.
        :rtype: oci.marketplace.models.OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this PublicationPackage.

        :param operating_system: The operating_system of this PublicationPackage.
        :type: oci.marketplace.models.OperatingSystem
        """
        self._operating_system = operating_system

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
