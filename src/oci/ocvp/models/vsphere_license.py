# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VsphereLicense(object):
    """
    License for vSphere upgrade.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VsphereLicense object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param license_type:
            The value to assign to the license_type property of this VsphereLicense.
        :type license_type: str

        :param license_key:
            The value to assign to the license_key property of this VsphereLicense.
        :type license_key: str

        """
        self.swagger_types = {
            'license_type': 'str',
            'license_key': 'str'
        }

        self.attribute_map = {
            'license_type': 'licenseType',
            'license_key': 'licenseKey'
        }

        self._license_type = None
        self._license_key = None

    @property
    def license_type(self):
        """
        **[Required]** Gets the license_type of this VsphereLicense.
        vSphere license type.


        :return: The license_type of this VsphereLicense.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this VsphereLicense.
        vSphere license type.


        :param license_type: The license_type of this VsphereLicense.
        :type: str
        """
        self._license_type = license_type

    @property
    def license_key(self):
        """
        **[Required]** Gets the license_key of this VsphereLicense.
        vSphere license key value.


        :return: The license_key of this VsphereLicense.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """
        Sets the license_key of this VsphereLicense.
        vSphere license key value.


        :param license_key: The license_key of this VsphereLicense.
        :type: str
        """
        self._license_key = license_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
