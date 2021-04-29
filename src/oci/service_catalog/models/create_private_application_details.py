# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePrivateApplicationDetails(object):
    """
    The model for the parameters needed to create a private application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePrivateApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePrivateApplicationDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreatePrivateApplicationDetails.
        :type display_name: str

        :param short_description:
            The value to assign to the short_description property of this CreatePrivateApplicationDetails.
        :type short_description: str

        :param long_description:
            The value to assign to the long_description property of this CreatePrivateApplicationDetails.
        :type long_description: str

        :param logo_file_base64_encoded:
            The value to assign to the logo_file_base64_encoded property of this CreatePrivateApplicationDetails.
        :type logo_file_base64_encoded: str

        :param package_details:
            The value to assign to the package_details property of this CreatePrivateApplicationDetails.
        :type package_details: oci.service_catalog.models.CreatePrivateApplicationPackage

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePrivateApplicationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePrivateApplicationDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'short_description': 'str',
            'long_description': 'str',
            'logo_file_base64_encoded': 'str',
            'package_details': 'CreatePrivateApplicationPackage',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'short_description': 'shortDescription',
            'long_description': 'longDescription',
            'logo_file_base64_encoded': 'logoFileBase64Encoded',
            'package_details': 'packageDetails',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._short_description = None
        self._long_description = None
        self._logo_file_base64_encoded = None
        self._package_details = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreatePrivateApplicationDetails.
        The `OCID`__ of the compartment where you want to create the private application.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreatePrivateApplicationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePrivateApplicationDetails.
        The `OCID`__ of the compartment where you want to create the private application.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreatePrivateApplicationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreatePrivateApplicationDetails.
        The name of the private application.


        :return: The display_name of this CreatePrivateApplicationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePrivateApplicationDetails.
        The name of the private application.


        :param display_name: The display_name of this CreatePrivateApplicationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def short_description(self):
        """
        **[Required]** Gets the short_description of this CreatePrivateApplicationDetails.
        A short description of the private application.


        :return: The short_description of this CreatePrivateApplicationDetails.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this CreatePrivateApplicationDetails.
        A short description of the private application.


        :param short_description: The short_description of this CreatePrivateApplicationDetails.
        :type: str
        """
        self._short_description = short_description

    @property
    def long_description(self):
        """
        Gets the long_description of this CreatePrivateApplicationDetails.
        A long description of the private application.


        :return: The long_description of this CreatePrivateApplicationDetails.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this CreatePrivateApplicationDetails.
        A long description of the private application.


        :param long_description: The long_description of this CreatePrivateApplicationDetails.
        :type: str
        """
        self._long_description = long_description

    @property
    def logo_file_base64_encoded(self):
        """
        Gets the logo_file_base64_encoded of this CreatePrivateApplicationDetails.
        Base64-encoded logo to use as the private application icon.
        Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.


        :return: The logo_file_base64_encoded of this CreatePrivateApplicationDetails.
        :rtype: str
        """
        return self._logo_file_base64_encoded

    @logo_file_base64_encoded.setter
    def logo_file_base64_encoded(self, logo_file_base64_encoded):
        """
        Sets the logo_file_base64_encoded of this CreatePrivateApplicationDetails.
        Base64-encoded logo to use as the private application icon.
        Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.


        :param logo_file_base64_encoded: The logo_file_base64_encoded of this CreatePrivateApplicationDetails.
        :type: str
        """
        self._logo_file_base64_encoded = logo_file_base64_encoded

    @property
    def package_details(self):
        """
        **[Required]** Gets the package_details of this CreatePrivateApplicationDetails.

        :return: The package_details of this CreatePrivateApplicationDetails.
        :rtype: oci.service_catalog.models.CreatePrivateApplicationPackage
        """
        return self._package_details

    @package_details.setter
    def package_details(self, package_details):
        """
        Sets the package_details of this CreatePrivateApplicationDetails.

        :param package_details: The package_details of this CreatePrivateApplicationDetails.
        :type: oci.service_catalog.models.CreatePrivateApplicationPackage
        """
        self._package_details = package_details

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePrivateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreatePrivateApplicationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePrivateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreatePrivateApplicationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePrivateApplicationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreatePrivateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePrivateApplicationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreatePrivateApplicationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
