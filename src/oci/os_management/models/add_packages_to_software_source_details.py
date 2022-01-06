# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddPackagesToSoftwareSourceDetails(object):
    """
    List of software package names
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddPackagesToSoftwareSourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_names:
            The value to assign to the package_names property of this AddPackagesToSoftwareSourceDetails.
        :type package_names: list[str]

        """
        self.swagger_types = {
            'package_names': 'list[str]'
        }

        self.attribute_map = {
            'package_names': 'packageNames'
        }

        self._package_names = None

    @property
    def package_names(self):
        """
        **[Required]** Gets the package_names of this AddPackagesToSoftwareSourceDetails.
        the list of package names


        :return: The package_names of this AddPackagesToSoftwareSourceDetails.
        :rtype: list[str]
        """
        return self._package_names

    @package_names.setter
    def package_names(self, package_names):
        """
        Sets the package_names of this AddPackagesToSoftwareSourceDetails.
        the list of package names


        :param package_names: The package_names of this AddPackagesToSoftwareSourceDetails.
        :type: list[str]
        """
        self._package_names = package_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
