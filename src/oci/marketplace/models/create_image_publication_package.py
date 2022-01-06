# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_publication_package import CreatePublicationPackage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateImagePublicationPackage(CreatePublicationPackage):
    """
    An object for creating an image publication package.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateImagePublicationPackage object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace.models.CreateImagePublicationPackage.package_type` attribute
        of this class is ``IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_version:
            The value to assign to the package_version property of this CreateImagePublicationPackage.
        :type package_version: str

        :param package_type:
            The value to assign to the package_type property of this CreateImagePublicationPackage.
            Allowed values for this property are: "ORCHESTRATION", "IMAGE"
        :type package_type: str

        :param operating_system:
            The value to assign to the operating_system property of this CreateImagePublicationPackage.
        :type operating_system: oci.marketplace.models.OperatingSystem

        :param eula:
            The value to assign to the eula property of this CreateImagePublicationPackage.
        :type eula: list[oci.marketplace.models.Eula]

        :param image_id:
            The value to assign to the image_id property of this CreateImagePublicationPackage.
        :type image_id: str

        """
        self.swagger_types = {
            'package_version': 'str',
            'package_type': 'str',
            'operating_system': 'OperatingSystem',
            'eula': 'list[Eula]',
            'image_id': 'str'
        }

        self.attribute_map = {
            'package_version': 'packageVersion',
            'package_type': 'packageType',
            'operating_system': 'operatingSystem',
            'eula': 'eula',
            'image_id': 'imageId'
        }

        self._package_version = None
        self._package_type = None
        self._operating_system = None
        self._eula = None
        self._image_id = None
        self._package_type = 'IMAGE'

    @property
    def image_id(self):
        """
        Gets the image_id of this CreateImagePublicationPackage.
        The unique identifier for the base image of the publication.


        :return: The image_id of this CreateImagePublicationPackage.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this CreateImagePublicationPackage.
        The unique identifier for the base image of the publication.


        :param image_id: The image_id of this CreateImagePublicationPackage.
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
