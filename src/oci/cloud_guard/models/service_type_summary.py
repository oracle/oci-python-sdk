# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceTypeSummary(object):
    """
    Summary of Service type
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ServiceTypeSummary.
        :type name: str

        :param resource_types:
            The value to assign to the resource_types property of this ServiceTypeSummary.
        :type resource_types: list[oci.cloud_guard.models.ResourceTypeSummary]

        """
        self.swagger_types = {
            'name': 'str',
            'resource_types': 'list[ResourceTypeSummary]'
        }

        self.attribute_map = {
            'name': 'name',
            'resource_types': 'resourceTypes'
        }

        self._name = None
        self._resource_types = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ServiceTypeSummary.
        name of the service type


        :return: The name of this ServiceTypeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ServiceTypeSummary.
        name of the service type


        :param name: The name of this ServiceTypeSummary.
        :type: str
        """
        self._name = name

    @property
    def resource_types(self):
        """
        **[Required]** Gets the resource_types of this ServiceTypeSummary.
        List of Resource


        :return: The resource_types of this ServiceTypeSummary.
        :rtype: list[oci.cloud_guard.models.ResourceTypeSummary]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """
        Sets the resource_types of this ServiceTypeSummary.
        List of Resource


        :param resource_types: The resource_types of this ServiceTypeSummary.
        :type: list[oci.cloud_guard.models.ResourceTypeSummary]
        """
        self._resource_types = resource_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
