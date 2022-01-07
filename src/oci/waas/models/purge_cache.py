# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PurgeCache(object):
    """
    The list of cached resources to purge. If a resource is not specified, the purge targets all rules in a policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PurgeCache object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resources:
            The value to assign to the resources property of this PurgeCache.
        :type resources: list[str]

        """
        self.swagger_types = {
            'resources': 'list[str]'
        }

        self.attribute_map = {
            'resources': 'resources'
        }

        self._resources = None

    @property
    def resources(self):
        """
        Gets the resources of this PurgeCache.
        A resource to purge, specified by either a hostless absolute path starting with a single slash (Example: `/path/to/resource`) or by a relative path in which the first component will be interpreted as a domain protected by the WAAS policy (Example: `example.com/path/to/resource`).


        :return: The resources of this PurgeCache.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this PurgeCache.
        A resource to purge, specified by either a hostless absolute path starting with a single slash (Example: `/path/to/resource`) or by a relative path in which the first component will be interpreted as a domain protected by the WAAS policy (Example: `example.com/path/to/resource`).


        :param resources: The resources of this PurgeCache.
        :type: list[str]
        """
        self._resources = resources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
