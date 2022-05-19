# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceTypeDefaultParameterValues(object):
    """
    Default values needed to import a resource type for a package.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceTypeDefaultParameterValues object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type:
            The value to assign to the resource_type property of this ResourceTypeDefaultParameterValues.
        :type resource_type: str

        :param parameter_values:
            The value to assign to the parameter_values property of this ResourceTypeDefaultParameterValues.
        :type parameter_values: dict(str, str)

        """
        self.swagger_types = {
            'resource_type': 'str',
            'parameter_values': 'dict(str, str)'
        }

        self.attribute_map = {
            'resource_type': 'resourceType',
            'parameter_values': 'parameterValues'
        }

        self._resource_type = None
        self._parameter_values = None

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this ResourceTypeDefaultParameterValues.
        The type of resource to which these resourceType-specific parameter values apply


        :return: The resource_type of this ResourceTypeDefaultParameterValues.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this ResourceTypeDefaultParameterValues.
        The type of resource to which these resourceType-specific parameter values apply


        :param resource_type: The resource_type of this ResourceTypeDefaultParameterValues.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def parameter_values(self):
        """
        **[Required]** Gets the parameter_values of this ResourceTypeDefaultParameterValues.
        A list of parameter values used to import the package.


        :return: The parameter_values of this ResourceTypeDefaultParameterValues.
        :rtype: dict(str, str)
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, parameter_values):
        """
        Sets the parameter_values of this ResourceTypeDefaultParameterValues.
        A list of parameter values used to import the package.


        :param parameter_values: The parameter_values of this ResourceTypeDefaultParameterValues.
        :type: dict(str, str)
        """
        self._parameter_values = parameter_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
