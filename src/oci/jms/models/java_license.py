# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaLicense(object):
    """
    Information about a license type for Java.
    """

    #: A constant which can be used with the license_type property of a JavaLicense.
    #: This constant has a value of "OTN"
    LICENSE_TYPE_OTN = "OTN"

    #: A constant which can be used with the license_type property of a JavaLicense.
    #: This constant has a value of "NFTC"
    LICENSE_TYPE_NFTC = "NFTC"

    #: A constant which can be used with the license_type property of a JavaLicense.
    #: This constant has a value of "RESTRICTED"
    LICENSE_TYPE_RESTRICTED = "RESTRICTED"

    def __init__(self, **kwargs):
        """
        Initializes a new JavaLicense object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this JavaLicense.
        :type display_name: str

        :param license_type:
            The value to assign to the license_type property of this JavaLicense.
            Allowed values for this property are: "OTN", "NFTC", "RESTRICTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_type: str

        :param license_url:
            The value to assign to the license_url property of this JavaLicense.
        :type license_url: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'license_type': 'str',
            'license_url': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'license_type': 'licenseType',
            'license_url': 'licenseUrl'
        }

        self._display_name = None
        self._license_type = None
        self._license_url = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this JavaLicense.
        Commonly used name for the license type.


        :return: The display_name of this JavaLicense.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JavaLicense.
        Commonly used name for the license type.


        :param display_name: The display_name of this JavaLicense.
        :type: str
        """
        self._display_name = display_name

    @property
    def license_type(self):
        """
        **[Required]** Gets the license_type of this JavaLicense.
        License Type

        Allowed values for this property are: "OTN", "NFTC", "RESTRICTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_type of this JavaLicense.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this JavaLicense.
        License Type


        :param license_type: The license_type of this JavaLicense.
        :type: str
        """
        allowed_values = ["OTN", "NFTC", "RESTRICTED"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            license_type = 'UNKNOWN_ENUM_VALUE'
        self._license_type = license_type

    @property
    def license_url(self):
        """
        **[Required]** Gets the license_url of this JavaLicense.
        Publicly accessible license URL containing the detailed terms and conditions.


        :return: The license_url of this JavaLicense.
        :rtype: str
        """
        return self._license_url

    @license_url.setter
    def license_url(self, license_url):
        """
        Sets the license_url of this JavaLicense.
        Publicly accessible license URL containing the detailed terms and conditions.


        :param license_url: The license_url of this JavaLicense.
        :type: str
        """
        self._license_url = license_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
