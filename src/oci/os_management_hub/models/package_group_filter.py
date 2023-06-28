# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PackageGroupFilter(object):
    """
    Used to select groups from VendorSoftwareSources to create/update CustomSoftwareSources.
    """

    #: A constant which can be used with the filter_type property of a PackageGroupFilter.
    #: This constant has a value of "INCLUDE"
    FILTER_TYPE_INCLUDE = "INCLUDE"

    #: A constant which can be used with the filter_type property of a PackageGroupFilter.
    #: This constant has a value of "EXCLUDE"
    FILTER_TYPE_EXCLUDE = "EXCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new PackageGroupFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_groups:
            The value to assign to the package_groups property of this PackageGroupFilter.
        :type package_groups: list[str]

        :param filter_type:
            The value to assign to the filter_type property of this PackageGroupFilter.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type filter_type: str

        """
        self.swagger_types = {
            'package_groups': 'list[str]',
            'filter_type': 'str'
        }

        self.attribute_map = {
            'package_groups': 'packageGroups',
            'filter_type': 'filterType'
        }

        self._package_groups = None
        self._filter_type = None

    @property
    def package_groups(self):
        """
        Gets the package_groups of this PackageGroupFilter.
        List of package group names.


        :return: The package_groups of this PackageGroupFilter.
        :rtype: list[str]
        """
        return self._package_groups

    @package_groups.setter
    def package_groups(self, package_groups):
        """
        Sets the package_groups of this PackageGroupFilter.
        List of package group names.


        :param package_groups: The package_groups of this PackageGroupFilter.
        :type: list[str]
        """
        self._package_groups = package_groups

    @property
    def filter_type(self):
        """
        **[Required]** Gets the filter_type of this PackageGroupFilter.
        The type of the filter, which can be of two types - INCLUDE or EXCLUDE.

        Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The filter_type of this PackageGroupFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this PackageGroupFilter.
        The type of the filter, which can be of two types - INCLUDE or EXCLUDE.


        :param filter_type: The filter_type of this PackageGroupFilter.
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]
        if not value_allowed_none_or_none_sentinel(filter_type, allowed_values):
            filter_type = 'UNKNOWN_ENUM_VALUE'
        self._filter_type = filter_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
