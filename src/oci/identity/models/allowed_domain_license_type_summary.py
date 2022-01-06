# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowedDomainLicenseTypeSummary(object):
    """
    The 'AllowedDomainLicenseTypeSummary' object contains information about the 'Domain License type'.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AllowedDomainLicenseTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AllowedDomainLicenseTypeSummary.
        :type name: str

        :param license_type:
            The value to assign to the license_type property of this AllowedDomainLicenseTypeSummary.
        :type license_type: str

        :param description:
            The value to assign to the description property of this AllowedDomainLicenseTypeSummary.
        :type description: str

        """
        self.swagger_types = {
            'name': 'str',
            'license_type': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'license_type': 'licenseType',
            'description': 'description'
        }

        self._name = None
        self._license_type = None
        self._description = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AllowedDomainLicenseTypeSummary.
        The license type name.

        Example: \"Oracle Apps Premium\"


        :return: The name of this AllowedDomainLicenseTypeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AllowedDomainLicenseTypeSummary.
        The license type name.

        Example: \"Oracle Apps Premium\"


        :param name: The name of this AllowedDomainLicenseTypeSummary.
        :type: str
        """
        self._name = name

    @property
    def license_type(self):
        """
        **[Required]** Gets the license_type of this AllowedDomainLicenseTypeSummary.
        The license type identifier.

        Example: \"oracle-apps-premium\"


        :return: The license_type of this AllowedDomainLicenseTypeSummary.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this AllowedDomainLicenseTypeSummary.
        The license type identifier.

        Example: \"oracle-apps-premium\"


        :param license_type: The license_type of this AllowedDomainLicenseTypeSummary.
        :type: str
        """
        self._license_type = license_type

    @property
    def description(self):
        """
        **[Required]** Gets the description of this AllowedDomainLicenseTypeSummary.
        The license type description.


        :return: The description of this AllowedDomainLicenseTypeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AllowedDomainLicenseTypeSummary.
        The license type description.


        :param description: The description of this AllowedDomainLicenseTypeSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
