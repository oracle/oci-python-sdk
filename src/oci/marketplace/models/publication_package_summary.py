# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicationPackageSummary(object):
    """
    The model for a summary of a publication package.
    """

    #: A constant which can be used with the package_type property of a PublicationPackageSummary.
    #: This constant has a value of "ORCHESTRATION"
    PACKAGE_TYPE_ORCHESTRATION = "ORCHESTRATION"

    #: A constant which can be used with the package_type property of a PublicationPackageSummary.
    #: This constant has a value of "IMAGE"
    PACKAGE_TYPE_IMAGE = "IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new PublicationPackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_id:
            The value to assign to the listing_id property of this PublicationPackageSummary.
        :type listing_id: str

        :param package_version:
            The value to assign to the package_version property of this PublicationPackageSummary.
        :type package_version: str

        :param package_type:
            The value to assign to the package_type property of this PublicationPackageSummary.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param resource_id:
            The value to assign to the resource_id property of this PublicationPackageSummary.
        :type resource_id: str

        :param time_created:
            The value to assign to the time_created property of this PublicationPackageSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'listing_id': 'str',
            'package_version': 'str',
            'package_type': 'str',
            'resource_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'listing_id': 'listingId',
            'package_version': 'packageVersion',
            'package_type': 'packageType',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated'
        }

        self._listing_id = None
        self._package_version = None
        self._package_type = None
        self._resource_id = None
        self._time_created = None

    @property
    def listing_id(self):
        """
        **[Required]** Gets the listing_id of this PublicationPackageSummary.
        The ID of the listing that the specified package belongs to.


        :return: The listing_id of this PublicationPackageSummary.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this PublicationPackageSummary.
        The ID of the listing that the specified package belongs to.


        :param listing_id: The listing_id of this PublicationPackageSummary.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def package_version(self):
        """
        **[Required]** Gets the package_version of this PublicationPackageSummary.
        The version of the specified package.


        :return: The package_version of this PublicationPackageSummary.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this PublicationPackageSummary.
        The version of the specified package.


        :param package_version: The package_version of this PublicationPackageSummary.
        :type: str
        """
        self._package_version = package_version

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this PublicationPackageSummary.
        The specified package's type.

        Allowed values for this property are: "ORCHESTRATION", "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this PublicationPackageSummary.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this PublicationPackageSummary.
        The specified package's type.


        :param package_type: The package_type of this PublicationPackageSummary.
        :type: str
        """
        allowed_values = ["ORCHESTRATION", "IMAGE"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this PublicationPackageSummary.
        The unique identifier for the package resource.


        :return: The resource_id of this PublicationPackageSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this PublicationPackageSummary.
        The unique identifier for the package resource.


        :param resource_id: The resource_id of this PublicationPackageSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def time_created(self):
        """
        Gets the time_created of this PublicationPackageSummary.
        The date and time the publication package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PublicationPackageSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PublicationPackageSummary.
        The date and time the publication package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PublicationPackageSummary.
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
