# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwarePackageDependency(object):
    """
    A dependecy for a software package
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwarePackageDependency object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dependency:
            The value to assign to the dependency property of this SoftwarePackageDependency.
        :type dependency: str

        :param dependency_type:
            The value to assign to the dependency_type property of this SoftwarePackageDependency.
        :type dependency_type: str

        :param dependency_modifier:
            The value to assign to the dependency_modifier property of this SoftwarePackageDependency.
        :type dependency_modifier: str

        """
        self.swagger_types = {
            'dependency': 'str',
            'dependency_type': 'str',
            'dependency_modifier': 'str'
        }

        self.attribute_map = {
            'dependency': 'dependency',
            'dependency_type': 'dependencyType',
            'dependency_modifier': 'dependencyModifier'
        }

        self._dependency = None
        self._dependency_type = None
        self._dependency_modifier = None

    @property
    def dependency(self):
        """
        Gets the dependency of this SoftwarePackageDependency.
        the software package's dependency


        :return: The dependency of this SoftwarePackageDependency.
        :rtype: str
        """
        return self._dependency

    @dependency.setter
    def dependency(self, dependency):
        """
        Sets the dependency of this SoftwarePackageDependency.
        the software package's dependency


        :param dependency: The dependency of this SoftwarePackageDependency.
        :type: str
        """
        self._dependency = dependency

    @property
    def dependency_type(self):
        """
        Gets the dependency_type of this SoftwarePackageDependency.
        the type of the dependency


        :return: The dependency_type of this SoftwarePackageDependency.
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """
        Sets the dependency_type of this SoftwarePackageDependency.
        the type of the dependency


        :param dependency_type: The dependency_type of this SoftwarePackageDependency.
        :type: str
        """
        self._dependency_type = dependency_type

    @property
    def dependency_modifier(self):
        """
        Gets the dependency_modifier of this SoftwarePackageDependency.
        the modifier for the dependency


        :return: The dependency_modifier of this SoftwarePackageDependency.
        :rtype: str
        """
        return self._dependency_modifier

    @dependency_modifier.setter
    def dependency_modifier(self, dependency_modifier):
        """
        Sets the dependency_modifier of this SoftwarePackageDependency.
        the modifier for the dependency


        :param dependency_modifier: The dependency_modifier of this SoftwarePackageDependency.
        :type: str
        """
        self._dependency_modifier = dependency_modifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
