# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .publication_package import PublicationPackage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImagePublicationPackage(PublicationPackage):
    """
    A publication package for image publications.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImagePublicationPackage object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace.models.ImagePublicationPackage.package_type` attribute
        of this class is ``IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this ImagePublicationPackage.
        :type description: str

        :param listing_id:
            The value to assign to the listing_id property of this ImagePublicationPackage.
        :type listing_id: str

        :param version:
            The value to assign to the version property of this ImagePublicationPackage.
        :type version: str

        :param package_type:
            The value to assign to the package_type property of this ImagePublicationPackage.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE"
        :type package_type: str

        :param resource_id:
            The value to assign to the resource_id property of this ImagePublicationPackage.
        :type resource_id: str

        :param time_created:
            The value to assign to the time_created property of this ImagePublicationPackage.
        :type time_created: datetime

        :param operating_system:
            The value to assign to the operating_system property of this ImagePublicationPackage.
        :type operating_system: oci.marketplace.models.OperatingSystem

        :param app_catalog_listing_id:
            The value to assign to the app_catalog_listing_id property of this ImagePublicationPackage.
        :type app_catalog_listing_id: str

        :param app_catalog_listing_resource_version:
            The value to assign to the app_catalog_listing_resource_version property of this ImagePublicationPackage.
        :type app_catalog_listing_resource_version: str

        :param image_id:
            The value to assign to the image_id property of this ImagePublicationPackage.
        :type image_id: str

        """
        self.swagger_types = {
            'description': 'str',
            'listing_id': 'str',
            'version': 'str',
            'package_type': 'str',
            'resource_id': 'str',
            'time_created': 'datetime',
            'operating_system': 'OperatingSystem',
            'app_catalog_listing_id': 'str',
            'app_catalog_listing_resource_version': 'str',
            'image_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'listing_id': 'listingId',
            'version': 'version',
            'package_type': 'packageType',
            'resource_id': 'resourceId',
            'time_created': 'timeCreated',
            'operating_system': 'operatingSystem',
            'app_catalog_listing_id': 'appCatalogListingId',
            'app_catalog_listing_resource_version': 'appCatalogListingResourceVersion',
            'image_id': 'imageId'
        }

        self._description = None
        self._listing_id = None
        self._version = None
        self._package_type = None
        self._resource_id = None
        self._time_created = None
        self._operating_system = None
        self._app_catalog_listing_id = None
        self._app_catalog_listing_resource_version = None
        self._image_id = None
        self._package_type = 'IMAGE'

    @property
    def app_catalog_listing_id(self):
        """
        Gets the app_catalog_listing_id of this ImagePublicationPackage.
        The ID of the listing resource associated with this publication package. For more information, see `AppCatalogListing`__ in the Core Services API.

        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListing/


        :return: The app_catalog_listing_id of this ImagePublicationPackage.
        :rtype: str
        """
        return self._app_catalog_listing_id

    @app_catalog_listing_id.setter
    def app_catalog_listing_id(self, app_catalog_listing_id):
        """
        Sets the app_catalog_listing_id of this ImagePublicationPackage.
        The ID of the listing resource associated with this publication package. For more information, see `AppCatalogListing`__ in the Core Services API.

        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListing/


        :param app_catalog_listing_id: The app_catalog_listing_id of this ImagePublicationPackage.
        :type: str
        """
        self._app_catalog_listing_id = app_catalog_listing_id

    @property
    def app_catalog_listing_resource_version(self):
        """
        Gets the app_catalog_listing_resource_version of this ImagePublicationPackage.
        The resource version of the listing resource associated with this publication package.


        :return: The app_catalog_listing_resource_version of this ImagePublicationPackage.
        :rtype: str
        """
        return self._app_catalog_listing_resource_version

    @app_catalog_listing_resource_version.setter
    def app_catalog_listing_resource_version(self, app_catalog_listing_resource_version):
        """
        Sets the app_catalog_listing_resource_version of this ImagePublicationPackage.
        The resource version of the listing resource associated with this publication package.


        :param app_catalog_listing_resource_version: The app_catalog_listing_resource_version of this ImagePublicationPackage.
        :type: str
        """
        self._app_catalog_listing_resource_version = app_catalog_listing_resource_version

    @property
    def image_id(self):
        """
        Gets the image_id of this ImagePublicationPackage.
        The ID of the image that corresponds to the package.


        :return: The image_id of this ImagePublicationPackage.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this ImagePublicationPackage.
        The ID of the image that corresponds to the package.


        :param image_id: The image_id of this ImagePublicationPackage.
        :type: str
        """
        self._image_id = image_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
