# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectStackDriftDetails(object):
    """
    The details for detecting drift in a stack
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetectStackDriftDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_addresses:
            The value to assign to the resource_addresses property of this DetectStackDriftDetails.
        :type resource_addresses: list[str]

        """
        self.swagger_types = {
            'resource_addresses': 'list[str]'
        }

        self.attribute_map = {
            'resource_addresses': 'resourceAddresses'
        }

        self._resource_addresses = None

    @property
    def resource_addresses(self):
        """
        Gets the resource_addresses of this DetectStackDriftDetails.
        The list of resources in the specified stack to detect drift for. Each resource is identified by a resource address,
        which is a string derived from the resource type and name specified in the stack's Terraform configuration plus an optional index.
        For example, the resource address for the fourth Compute instance with the name \"test_instance\" is oci_core_instance.test_instance`3].
        For more details and examples of resource addresses, see the Terraform documentation at [Resource spec`__.

        __ https://www.terraform.io/docs/internals/resource-addressing.html#examples


        :return: The resource_addresses of this DetectStackDriftDetails.
        :rtype: list[str]
        """
        return self._resource_addresses

    @resource_addresses.setter
    def resource_addresses(self, resource_addresses):
        """
        Sets the resource_addresses of this DetectStackDriftDetails.
        The list of resources in the specified stack to detect drift for. Each resource is identified by a resource address,
        which is a string derived from the resource type and name specified in the stack's Terraform configuration plus an optional index.
        For example, the resource address for the fourth Compute instance with the name \"test_instance\" is oci_core_instance.test_instance`3].
        For more details and examples of resource addresses, see the Terraform documentation at [Resource spec`__.

        __ https://www.terraform.io/docs/internals/resource-addressing.html#examples


        :param resource_addresses: The resource_addresses of this DetectStackDriftDetails.
        :type: list[str]
        """
        self._resource_addresses = resource_addresses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
