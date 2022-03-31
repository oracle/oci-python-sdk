# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeDomainLicenseTypeDetails(object):
    """
    (For tenancies that support identity domains) Details for updating the license type of the identity domain.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeDomainLicenseTypeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param license_type:
            The value to assign to the license_type property of this ChangeDomainLicenseTypeDetails.
        :type license_type: str

        """
        self.swagger_types = {
            'license_type': 'str'
        }

        self.attribute_map = {
            'license_type': 'licenseType'
        }

        self._license_type = None

    @property
    def license_type(self):
        """
        Gets the license_type of this ChangeDomainLicenseTypeDetails.
        The license type of the identity domain.


        :return: The license_type of this ChangeDomainLicenseTypeDetails.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this ChangeDomainLicenseTypeDetails.
        The license type of the identity domain.


        :param license_type: The license_type of this ChangeDomainLicenseTypeDetails.
        :type: str
        """
        self._license_type = license_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
