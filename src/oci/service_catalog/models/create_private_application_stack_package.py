# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_private_application_package import CreatePrivateApplicationPackage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePrivateApplicationStackPackage(CreatePrivateApplicationPackage):
    """
    An object for creating a private application stack package.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePrivateApplicationStackPackage object with values from keyword arguments. The default value of the :py:attr:`~oci.service_catalog.models.CreatePrivateApplicationStackPackage.package_type` attribute
        of this class is ``STACK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_type:
            The value to assign to the package_type property of this CreatePrivateApplicationStackPackage.
            Allowed values for this property are: "STACK"
        :type package_type: str

        :param version:
            The value to assign to the version property of this CreatePrivateApplicationStackPackage.
        :type version: str

        :param zip_file_base64_encoded:
            The value to assign to the zip_file_base64_encoded property of this CreatePrivateApplicationStackPackage.
        :type zip_file_base64_encoded: str

        """
        self.swagger_types = {
            'package_type': 'str',
            'version': 'str',
            'zip_file_base64_encoded': 'str'
        }

        self.attribute_map = {
            'package_type': 'packageType',
            'version': 'version',
            'zip_file_base64_encoded': 'zipFileBase64Encoded'
        }

        self._package_type = None
        self._version = None
        self._zip_file_base64_encoded = None
        self._package_type = 'STACK'

    @property
    def zip_file_base64_encoded(self):
        """
        Gets the zip_file_base64_encoded of this CreatePrivateApplicationStackPackage.
        Base-64 payload of the Terraform zip package.


        :return: The zip_file_base64_encoded of this CreatePrivateApplicationStackPackage.
        :rtype: str
        """
        return self._zip_file_base64_encoded

    @zip_file_base64_encoded.setter
    def zip_file_base64_encoded(self, zip_file_base64_encoded):
        """
        Sets the zip_file_base64_encoded of this CreatePrivateApplicationStackPackage.
        Base-64 payload of the Terraform zip package.


        :param zip_file_base64_encoded: The zip_file_base64_encoded of this CreatePrivateApplicationStackPackage.
        :type: str
        """
        self._zip_file_base64_encoded = zip_file_base64_encoded

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
